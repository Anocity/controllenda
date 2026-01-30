"""
MIR4 Account Tracker API Tests
Tests all CRUD operations for accounts, boss prices, and scheduler status
"""
import pytest
import requests
import os
import uuid

BASE_URL = os.environ.get('REACT_APP_BACKEND_URL', '').rstrip('/')

class TestHealthAndScheduler:
    """Test health check and scheduler status endpoints"""
    
    def test_api_root(self):
        """Test API root endpoint"""
        response = requests.get(f"{BASE_URL}/api/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "MIR4" in data["message"]
        print(f"API root response: {data}")
    
    def test_scheduler_status(self):
        """Test scheduler status endpoint - should show scheduler running"""
        response = requests.get(f"{BASE_URL}/api/scheduler-status")
        assert response.status_code == 200
        data = response.json()
        assert "scheduler_running" in data
        assert data["scheduler_running"] == True
        assert "jobs" in data
        print(f"Scheduler status: {data}")


class TestBossPrices:
    """Test boss prices CRUD operations"""
    
    def test_get_boss_prices(self):
        """Test GET boss prices - should return default or existing prices"""
        response = requests.get(f"{BASE_URL}/api/boss-prices")
        assert response.status_code == 200
        data = response.json()
        
        # Verify all price fields exist
        expected_fields = [
            "medio2_price", "grande2_price", "medio4_price", "grande4_price",
            "medio6_price", "grande6_price", "medio7_price", "grande7_price",
            "medio8_price", "grande8_price", "xama_price", "praca_4f_price",
            "cracha_epica_price"
        ]
        for field in expected_fields:
            assert field in data, f"Missing field: {field}"
            assert isinstance(data[field], (int, float)), f"Field {field} should be numeric"
        
        print(f"Boss prices: {data}")
    
    def test_update_boss_prices(self):
        """Test PUT boss prices - update and verify persistence"""
        # Update prices
        update_data = {
            "medio2_price": 0.05,
            "grande2_price": 0.10,
            "xama_price": 0.25
        }
        response = requests.put(f"{BASE_URL}/api/boss-prices", json=update_data)
        assert response.status_code == 200
        data = response.json()
        
        # Verify updated values
        assert data["medio2_price"] == 0.05
        assert data["grande2_price"] == 0.10
        assert data["xama_price"] == 0.25
        
        # GET to verify persistence
        get_response = requests.get(f"{BASE_URL}/api/boss-prices")
        assert get_response.status_code == 200
        get_data = get_response.json()
        assert get_data["medio2_price"] == 0.05
        assert get_data["grande2_price"] == 0.10
        assert get_data["xama_price"] == 0.25
        
        print(f"Updated boss prices verified: {get_data}")


class TestAccountsCRUD:
    """Test accounts CRUD operations"""
    
    @pytest.fixture
    def test_account_data(self):
        """Generate test account data"""
        return {
            "name": f"TEST_Account_{uuid.uuid4().hex[:8]}",
            "bosses": {
                "medio2": 5, "grande2": 3,
                "medio4": 2, "grande4": 1,
                "medio6": 0, "grande6": 0,
                "medio7": 0, "grande7": 0,
                "medio8": 0, "grande8": 0
            },
            "sala_pico": "Sala 42",
            "special_bosses": {
                "xama": 2, "praca_4f": 1, "cracha_epica": 0
            },
            "gold": 1500.50
        }
    
    def test_get_accounts(self):
        """Test GET all accounts"""
        response = requests.get(f"{BASE_URL}/api/accounts")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        print(f"Found {len(data)} accounts")
    
    def test_create_account(self, test_account_data):
        """Test POST create account"""
        response = requests.post(f"{BASE_URL}/api/accounts", json=test_account_data)
        assert response.status_code == 200
        data = response.json()
        
        # Verify response structure
        assert "id" in data
        assert data["name"] == test_account_data["name"]
        assert data["bosses"]["medio2"] == 5
        assert data["bosses"]["grande2"] == 3
        assert data["sala_pico"] == "Sala 42"
        assert data["special_bosses"]["xama"] == 2
        assert data["gold"] == 1500.50
        assert "total_usd" in data
        assert data["confirmed"] == False
        
        print(f"Created account: {data['id']}")
        
        # Cleanup
        requests.delete(f"{BASE_URL}/api/accounts/{data['id']}")
    
    def test_create_and_get_account(self, test_account_data):
        """Test create account and verify with GET"""
        # Create
        create_response = requests.post(f"{BASE_URL}/api/accounts", json=test_account_data)
        assert create_response.status_code == 200
        created = create_response.json()
        account_id = created["id"]
        
        # GET single account
        get_response = requests.get(f"{BASE_URL}/api/accounts/{account_id}")
        assert get_response.status_code == 200
        fetched = get_response.json()
        
        # Verify data matches
        assert fetched["id"] == account_id
        assert fetched["name"] == test_account_data["name"]
        assert fetched["bosses"]["medio2"] == 5
        assert fetched["gold"] == 1500.50
        
        print(f"Verified account persistence: {account_id}")
        
        # Cleanup
        requests.delete(f"{BASE_URL}/api/accounts/{account_id}")
    
    def test_update_account(self, test_account_data):
        """Test PUT update account"""
        # Create account first
        create_response = requests.post(f"{BASE_URL}/api/accounts", json=test_account_data)
        assert create_response.status_code == 200
        account_id = create_response.json()["id"]
        
        # Update account
        update_data = {
            "name": "TEST_Updated_Name",
            "gold": 2500.75,
            "bosses": {
                "medio2": 10, "grande2": 5,
                "medio4": 3, "grande4": 2,
                "medio6": 1, "grande6": 0,
                "medio7": 0, "grande7": 0,
                "medio8": 0, "grande8": 0
            }
        }
        update_response = requests.put(f"{BASE_URL}/api/accounts/{account_id}", json=update_data)
        assert update_response.status_code == 200
        updated = update_response.json()
        
        # Verify update response
        assert updated["name"] == "TEST_Updated_Name"
        assert updated["gold"] == 2500.75
        assert updated["bosses"]["medio2"] == 10
        
        # GET to verify persistence
        get_response = requests.get(f"{BASE_URL}/api/accounts/{account_id}")
        assert get_response.status_code == 200
        fetched = get_response.json()
        assert fetched["name"] == "TEST_Updated_Name"
        assert fetched["gold"] == 2500.75
        
        print(f"Updated and verified account: {account_id}")
        
        # Cleanup
        requests.delete(f"{BASE_URL}/api/accounts/{account_id}")
    
    def test_confirm_account(self, test_account_data):
        """Test POST confirm account"""
        # Create account
        create_response = requests.post(f"{BASE_URL}/api/accounts", json=test_account_data)
        assert create_response.status_code == 200
        account_id = create_response.json()["id"]
        
        # Confirm account
        confirm_response = requests.post(f"{BASE_URL}/api/accounts/{account_id}/confirm")
        assert confirm_response.status_code == 200
        confirmed = confirm_response.json()
        
        # Verify confirmation
        assert confirmed["confirmed"] == True
        assert confirmed["confirmed_at"] is not None
        
        # GET to verify persistence
        get_response = requests.get(f"{BASE_URL}/api/accounts/{account_id}")
        assert get_response.status_code == 200
        fetched = get_response.json()
        assert fetched["confirmed"] == True
        assert fetched["confirmed_at"] is not None
        
        print(f"Confirmed account: {account_id}, confirmed_at: {fetched['confirmed_at']}")
        
        # Cleanup
        requests.delete(f"{BASE_URL}/api/accounts/{account_id}")
    
    def test_delete_account(self, test_account_data):
        """Test DELETE account"""
        # Create account
        create_response = requests.post(f"{BASE_URL}/api/accounts", json=test_account_data)
        assert create_response.status_code == 200
        account_id = create_response.json()["id"]
        
        # Delete account
        delete_response = requests.delete(f"{BASE_URL}/api/accounts/{account_id}")
        assert delete_response.status_code == 200
        
        # Verify deletion - GET should return 404
        get_response = requests.get(f"{BASE_URL}/api/accounts/{account_id}")
        assert get_response.status_code == 404
        
        print(f"Deleted and verified removal: {account_id}")
    
    def test_get_nonexistent_account(self):
        """Test GET non-existent account returns 404"""
        fake_id = str(uuid.uuid4())
        response = requests.get(f"{BASE_URL}/api/accounts/{fake_id}")
        assert response.status_code == 404
        print(f"Correctly returned 404 for non-existent account")
    
    def test_delete_nonexistent_account(self):
        """Test DELETE non-existent account returns 404"""
        fake_id = str(uuid.uuid4())
        response = requests.delete(f"{BASE_URL}/api/accounts/{fake_id}")
        assert response.status_code == 404
        print(f"Correctly returned 404 for delete non-existent account")


class TestUSDCalculation:
    """Test USD calculation functionality"""
    
    def test_total_usd_calculation(self):
        """Test that total_usd is calculated correctly"""
        # Get current prices
        prices_response = requests.get(f"{BASE_URL}/api/boss-prices")
        prices = prices_response.json()
        
        # Create account with known values
        account_data = {
            "name": "TEST_USD_Calc",
            "bosses": {
                "medio2": 10, "grande2": 5,
                "medio4": 0, "grande4": 0,
                "medio6": 0, "grande6": 0,
                "medio7": 0, "grande7": 0,
                "medio8": 0, "grande8": 0
            },
            "sala_pico": "",
            "special_bosses": {
                "xama": 0, "praca_4f": 0, "cracha_epica": 0
            },
            "gold": 0
        }
        
        create_response = requests.post(f"{BASE_URL}/api/accounts", json=account_data)
        assert create_response.status_code == 200
        created = create_response.json()
        
        # Calculate expected USD
        expected_usd = (10 * prices["medio2_price"]) + (5 * prices["grande2_price"])
        expected_usd = round(expected_usd, 2)
        
        # Verify calculation
        assert created["total_usd"] == expected_usd, f"Expected {expected_usd}, got {created['total_usd']}"
        
        print(f"USD calculation verified: {created['total_usd']} (expected: {expected_usd})")
        
        # Cleanup
        requests.delete(f"{BASE_URL}/api/accounts/{created['id']}")


class TestCleanup:
    """Cleanup test data"""
    
    def test_cleanup_test_accounts(self):
        """Remove all TEST_ prefixed accounts"""
        response = requests.get(f"{BASE_URL}/api/accounts")
        accounts = response.json()
        
        deleted_count = 0
        for account in accounts:
            if account["name"].startswith("TEST_"):
                requests.delete(f"{BASE_URL}/api/accounts/{account['id']}")
                deleted_count += 1
        
        print(f"Cleaned up {deleted_count} test accounts")
