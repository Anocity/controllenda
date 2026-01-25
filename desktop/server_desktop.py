from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict
import uuid
from datetime import datetime, timezone
import sqlite3
import json
import os
import sys

# Get the directory where the executable is located
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(application_path, 'mir4_data.db')

# Create the main app
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Initialize SQLite Database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create accounts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            bosses TEXT NOT NULL,
            sala_pico TEXT,
            special_bosses TEXT NOT NULL,
            gold REAL DEFAULT 0,
            created_at TEXT
        )
    ''')
    
    # Create boss_prices table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS boss_prices (
            id TEXT PRIMARY KEY,
            medio2_price REAL,
            grande2_price REAL,
            medio4_price REAL,
            grande4_price REAL,
            medio6_price REAL,
            grande6_price REAL,
            medio7_price REAL,
            grande7_price REAL,
            medio8_price REAL,
            grande8_price REAL,
            xama_price REAL,
            praca_4f_price REAL,
            cracha_epica_price REAL
        )
    ''')
    
    # Insert default boss prices if not exists
    cursor.execute("SELECT COUNT(*) FROM boss_prices WHERE id = 'default'")
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO boss_prices VALUES (
                'default', 0.045, 0.09, 0.14, 0.18, 0.36, 0.45, 0, 0, 0, 0, 0, 0, 0
            )
        ''')
    
    conn.commit()
    conn.close()

init_db()

# Models
class BossQuantities(BaseModel):
    medio2: int = Field(default=0, ge=0)
    grande2: int = Field(default=0, ge=0)
    medio4: int = Field(default=0, ge=0)
    grande4: int = Field(default=0, ge=0)
    medio6: int = Field(default=0, ge=0)
    grande6: int = Field(default=0, ge=0)
    medio7: int = Field(default=0, ge=0)
    grande7: int = Field(default=0, ge=0)
    medio8: int = Field(default=0, ge=0)
    grande8: int = Field(default=0, ge=0)

class SpecialBosses(BaseModel):
    xama: int = Field(default=0, ge=0)
    praca_4f: int = Field(default=0, ge=0)
    cracha_epica: int = Field(default=0, ge=0)

class Account(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    bosses: BossQuantities
    sala_pico: str = ""
    special_bosses: SpecialBosses
    gold: float = Field(default=0, ge=0)
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class AccountCreate(BaseModel):
    name: str
    bosses: BossQuantities
    sala_pico: str = ""
    special_bosses: SpecialBosses
    gold: float = Field(default=0, ge=0)

class AccountUpdate(BaseModel):
    name: Optional[str] = None
    bosses: Optional[BossQuantities] = None
    sala_pico: Optional[str] = None
    special_bosses: Optional[SpecialBosses] = None
    gold: Optional[float] = Field(default=None, ge=0)

class BossPrices(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    id: str = "default"
    medio2_price: float = Field(default=0.045, ge=0)
    grande2_price: float = Field(default=0.09, ge=0)
    medio4_price: float = Field(default=0.14, ge=0)
    grande4_price: float = Field(default=0.18, ge=0)
    medio6_price: float = Field(default=0.36, ge=0)
    grande6_price: float = Field(default=0.45, ge=0)
    medio7_price: float = Field(default=0, ge=0)
    grande7_price: float = Field(default=0, ge=0)
    medio8_price: float = Field(default=0, ge=0)
    grande8_price: float = Field(default=0, ge=0)
    xama_price: float = Field(default=0, ge=0)
    praca_4f_price: float = Field(default=0, ge=0)
    cracha_epica_price: float = Field(default=0, ge=0)

class BossPricesUpdate(BaseModel):
    medio2_price: Optional[float] = Field(default=None, ge=0)
    grande2_price: Optional[float] = Field(default=None, ge=0)
    medio4_price: Optional[float] = Field(default=None, ge=0)
    grande4_price: Optional[float] = Field(default=None, ge=0)
    medio6_price: Optional[float] = Field(default=None, ge=0)
    grande6_price: Optional[float] = Field(default=None, ge=0)
    medio7_price: Optional[float] = Field(default=None, ge=0)
    grande7_price: Optional[float] = Field(default=None, ge=0)
    medio8_price: Optional[float] = Field(default=None, ge=0)
    grande8_price: Optional[float] = Field(default=None, ge=0)
    xama_price: Optional[float] = Field(default=None, ge=0)
    praca_4f_price: Optional[float] = Field(default=None, ge=0)
    cracha_epica_price: Optional[float] = Field(default=None, ge=0)

# Helper function
def calculate_account_usd(account: dict, prices: BossPrices) -> float:
    bosses = account.get('bosses', {})
    special = account.get('special_bosses', {})
    
    total = 0.0
    total += bosses.get('medio2', 0) * prices.medio2_price
    total += bosses.get('grande2', 0) * prices.grande2_price
    total += bosses.get('medio4', 0) * prices.medio4_price
    total += bosses.get('grande4', 0) * prices.grande4_price
    total += bosses.get('medio6', 0) * prices.medio6_price
    total += bosses.get('grande6', 0) * prices.grande6_price
    total += bosses.get('medio7', 0) * prices.medio7_price
    total += bosses.get('grande7', 0) * prices.grande7_price
    total += bosses.get('medio8', 0) * prices.medio8_price
    total += bosses.get('grande8', 0) * prices.grande8_price
    total += special.get('xama', 0) * prices.xama_price
    total += special.get('praca_4f', 0) * prices.praca_4f_price
    total += special.get('cracha_epica', 0) * prices.cracha_epica_price
    
    return round(total, 2)

# Routes
@api_router.get("/")
def root():
    return {"message": "MIR4 Account Manager Desktop"}

@api_router.get("/boss-prices")
def get_boss_prices():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM boss_prices WHERE id = 'default'")
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return {
            "id": row[0],
            "medio2_price": row[1],
            "grande2_price": row[2],
            "medio4_price": row[3],
            "grande4_price": row[4],
            "medio6_price": row[5],
            "grande6_price": row[6],
            "medio7_price": row[7],
            "grande7_price": row[8],
            "medio8_price": row[9],
            "grande8_price": row[10],
            "xama_price": row[11],
            "praca_4f_price": row[12],
            "cracha_epica_price": row[13]
        }
    return BossPrices().model_dump()

@api_router.put("/boss-prices")
def update_boss_prices(update: BossPricesUpdate):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM boss_prices WHERE id = 'default'")
    current = cursor.fetchone()
    
    if current:
        update_data = update.model_dump(exclude_unset=True)
        set_clauses = []
        values = []
        
        for key, value in update_data.items():
            set_clauses.append(f"{key} = ?")
            values.append(value)
        
        if set_clauses:
            values.append('default')
            cursor.execute(
                f"UPDATE boss_prices SET {', '.join(set_clauses)} WHERE id = ?",
                values
            )
            conn.commit()
    
    conn.close()
    return get_boss_prices()

@api_router.get("/accounts")
def get_accounts():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts")
    rows = cursor.fetchall()
    conn.close()
    
    prices = BossPrices(**get_boss_prices())
    accounts = []
    
    for row in rows:
        account = {
            "id": row[0],
            "name": row[1],
            "bosses": json.loads(row[2]),
            "sala_pico": row[3],
            "special_bosses": json.loads(row[4]),
            "gold": row[5],
            "created_at": row[6]
        }
        account["total_usd"] = calculate_account_usd(account, prices)
        accounts.append(account)
    
    return accounts

@api_router.get("/accounts/{account_id}")
def get_account(account_id: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE id = ?", (account_id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="Account not found")
    
    account = {
        "id": row[0],
        "name": row[1],
        "bosses": json.loads(row[2]),
        "sala_pico": row[3],
        "special_bosses": json.loads(row[4]),
        "gold": row[5],
        "created_at": row[6]
    }
    
    prices = BossPrices(**get_boss_prices())
    account["total_usd"] = calculate_account_usd(account, prices)
    
    return account

@api_router.post("/accounts")
def create_account(account_data: AccountCreate):
    account = Account(**account_data.model_dump())
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO accounts (id, name, bosses, sala_pico, special_bosses, gold, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        account.id,
        account.name,
        json.dumps(account.bosses.model_dump()),
        account.sala_pico,
        json.dumps(account.special_bosses.model_dump()),
        account.gold,
        account.created_at
    ))
    conn.commit()
    conn.close()
    
    prices = BossPrices(**get_boss_prices())
    result = account.model_dump()
    result["total_usd"] = calculate_account_usd(result, prices)
    
    return result

@api_router.put("/accounts/{account_id}")
def update_account(account_id: str, update: AccountUpdate):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM accounts WHERE id = ?", (account_id,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="Account not found")
    
    update_data = update.model_dump(exclude_unset=True)
    set_clauses = []
    values = []
    
    for key, value in update_data.items():
        if key in ['bosses', 'special_bosses']:
            set_clauses.append(f"{key} = ?")
            values.append(json.dumps(value))
        else:
            set_clauses.append(f"{key} = ?")
            values.append(value)
    
    if set_clauses:
        values.append(account_id)
        cursor.execute(
            f"UPDATE accounts SET {', '.join(set_clauses)} WHERE id = ?",
            values
        )
        conn.commit()
    
    conn.close()
    return get_account(account_id)

@api_router.delete("/accounts/{account_id}")
def delete_account(account_id: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM accounts WHERE id = ?", (account_id,))
    deleted = cursor.rowcount
    conn.commit()
    conn.close()
    
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Account not found")
    
    return {"message": "Account deleted successfully"}

@api_router.get("/statistics")
def get_statistics():
    accounts = get_accounts()
    prices = BossPrices(**get_boss_prices())
    
    total_bosses = {
        "medio2": 0, "grande2": 0, "medio4": 0, "grande4": 0,
        "medio6": 0, "grande6": 0, "medio7": 0, "grande7": 0,
        "medio8": 0, "grande8": 0
    }
    total_special = {"xama": 0, "praca_4f": 0, "cracha_epica": 0}
    total_gold = 0.0
    total_usd = 0.0
    
    for account in accounts:
        for boss_type in total_bosses.keys():
            total_bosses[boss_type] += account['bosses'].get(boss_type, 0)
        for special_type in total_special.keys():
            total_special[special_type] += account['special_bosses'].get(special_type, 0)
        total_gold += account.get('gold', 0)
        total_usd += account.get('total_usd', 0)
    
    return {
        "total_accounts": len(accounts),
        "total_bosses": total_bosses,
        "total_special_bosses": total_special,
        "total_gold": round(total_gold, 2),
        "total_usd": round(total_usd, 2)
    }

# Include router
app.include_router(api_router)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
