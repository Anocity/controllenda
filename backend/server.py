from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict
import uuid
from datetime import datetime, timezone


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")


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
    medio9_price: float = Field(default=0, ge=0)
    grande9_price: float = Field(default=0, ge=0)
    medio10_price: float = Field(default=0, ge=0)
    grande10_price: float = Field(default=0, ge=0)
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
    medio9_price: Optional[float] = Field(default=None, ge=0)
    grande9_price: Optional[float] = Field(default=None, ge=0)
    medio10_price: Optional[float] = Field(default=None, ge=0)
    grande10_price: Optional[float] = Field(default=None, ge=0)
    xama_price: Optional[float] = Field(default=None, ge=0)
    praca_4f_price: Optional[float] = Field(default=None, ge=0)
    cracha_epica_price: Optional[float] = Field(default=None, ge=0)

class AccountWithValues(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    id: str
    name: str
    bosses: BossQuantities
    sala_pico: str
    special_bosses: SpecialBosses
    gold: float
    created_at: str
    total_usd: float

class Statistics(BaseModel):
    total_accounts: int
    total_bosses: Dict[str, int]
    total_special_bosses: Dict[str, int]
    total_gold: float
    total_usd: float


# Helper function to calculate USD for an account
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
    total += bosses.get('medio9', 0) * prices.medio9_price
    total += bosses.get('grande9', 0) * prices.grande9_price
    total += bosses.get('medio10', 0) * prices.medio10_price
    total += bosses.get('grande10', 0) * prices.grande10_price
    total += special.get('xama', 0) * prices.xama_price
    total += special.get('praca_4f', 0) * prices.praca_4f_price
    total += special.get('cracha_epica', 0) * prices.cracha_epica_price
    
    return round(total, 2)


# Routes
@api_router.get("/")
async def root():
    return {"message": "MIR4 Account Manager API"}

# Boss Prices Routes
@api_router.get("/boss-prices", response_model=BossPrices)
async def get_boss_prices():
    prices = await db.boss_prices.find_one({"id": "default"}, {"_id": 0})
    if not prices:
        # Create default prices
        default_prices = BossPrices()
        await db.boss_prices.insert_one(default_prices.model_dump())
        return default_prices
    return BossPrices(**prices)

@api_router.put("/boss-prices", response_model=BossPrices)
async def update_boss_prices(update: BossPricesUpdate):
    current_prices = await db.boss_prices.find_one({"id": "default"}, {"_id": 0})
    
    if not current_prices:
        current_prices = BossPrices().model_dump()
    
    # Update only provided fields
    update_data = update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        current_prices[key] = value
    
    await db.boss_prices.update_one(
        {"id": "default"},
        {"$set": current_prices},
        upsert=True
    )
    
    return BossPrices(**current_prices)

# Account Routes
@api_router.get("/accounts")
async def get_accounts():
    accounts = await db.accounts.find({}, {"_id": 0}).to_list(1000)
    prices = await get_boss_prices()
    
    accounts_with_values = []
    for account in accounts:
        total_usd = calculate_account_usd(account, prices)
        account_with_value = {**account, "total_usd": total_usd}
        accounts_with_values.append(account_with_value)
    
    return accounts_with_values

@api_router.get("/accounts/{account_id}")
async def get_account(account_id: str):
    account = await db.accounts.find_one({"id": account_id}, {"_id": 0})
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    prices = await get_boss_prices()
    total_usd = calculate_account_usd(account, prices)
    
    return {**account, "total_usd": total_usd}

@api_router.post("/accounts", response_model=AccountWithValues)
async def create_account(account_data: AccountCreate):
    account = Account(**account_data.model_dump())
    
    await db.accounts.insert_one(account.model_dump())
    
    prices = await get_boss_prices()
    total_usd = calculate_account_usd(account.model_dump(), prices)
    
    return {**account.model_dump(), "total_usd": total_usd}

@api_router.put("/accounts/{account_id}", response_model=AccountWithValues)
async def update_account(account_id: str, update: AccountUpdate):
    existing = await db.accounts.find_one({"id": account_id}, {"_id": 0})
    if not existing:
        raise HTTPException(status_code=404, detail="Account not found")
    
    update_data = update.model_dump(exclude_unset=True)
    
    await db.accounts.update_one(
        {"id": account_id},
        {"$set": update_data}
    )
    
    updated_account = await db.accounts.find_one({"id": account_id}, {"_id": 0})
    prices = await get_boss_prices()
    total_usd = calculate_account_usd(updated_account, prices)
    
    return {**updated_account, "total_usd": total_usd}

@api_router.delete("/accounts/{account_id}")
async def delete_account(account_id: str):
    result = await db.accounts.delete_one({"id": account_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"message": "Account deleted successfully"}

@api_router.get("/statistics", response_model=Statistics)
async def get_statistics():
    accounts = await db.accounts.find({}, {"_id": 0}).to_list(1000)
    prices = await get_boss_prices()
    
    total_accounts = len(accounts)
    total_bosses = {
        "medio2": 0,
        "grande2": 0,
        "medio4": 0,
        "grande4": 0,
        "medio6": 0,
        "grande6": 0,
        "medio7": 0,
        "grande7": 0,
        "medio8": 0,
        "grande8": 0,
        "medio9": 0,
        "grande9": 0,
        "medio10": 0,
        "grande10": 0
    }
    total_special_bosses = {
        "xama": 0,
        "praca_4f": 0,
        "cracha_epica": 0
    }
    total_gold = 0.0
    total_usd = 0.0
    
    for account in accounts:
        bosses = account.get('bosses', {})
        special = account.get('special_bosses', {})
        
        for boss_type in total_bosses.keys():
            total_bosses[boss_type] += bosses.get(boss_type, 0)
        
        for special_type in total_special_bosses.keys():
            total_special_bosses[special_type] += special.get(special_type, 0)
        
        total_gold += account.get('gold', 0)
        total_usd += calculate_account_usd(account, prices)
    
    return Statistics(
        total_accounts=total_accounts,
        total_bosses=total_bosses,
        total_special_bosses=total_special_bosses,
        total_gold=round(total_gold, 2),
        total_usd=round(total_usd, 2)
    )


# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
