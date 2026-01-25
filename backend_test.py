import requests
import sys
import json
from datetime import datetime

class MIR4APITester:
    def __init__(self, base_url="https://mir4-account-tracker.preview.emergentagent.com"):
        self.base_url = base_url
        self.api_url = f"{base_url}/api"
        self.tests_run = 0
        self.tests_passed = 0
        self.test_account_id = None

    def run_test(self, name, method, endpoint, expected_status, data=None):
        """Run a single API test"""
        url = f"{self.api_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        print(f"   URL: {url}")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=10)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=10)
            elif method == 'PUT':
                response = requests.put(url, json=data, headers=headers, timeout=10)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers, timeout=10)

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                try:
                    response_data = response.json()
                    print(f"   Response: {json.dumps(response_data, indent=2)[:200]}...")
                    return True, response_data
                except:
                    return True, {}
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                try:
                    error_data = response.json()
                    print(f"   Error: {error_data}")
                except:
                    print(f"   Error: {response.text}")
                return False, {}

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            return False, {}

    def test_root_endpoint(self):
        """Test root API endpoint"""
        return self.run_test("Root API", "GET", "", 200)

    def test_get_boss_prices(self):
        """Test getting boss prices"""
        success, response = self.run_test("Get Boss Prices", "GET", "boss-prices", 200)
        if success:
            # Verify default prices structure
            expected_fields = ['medio2_price', 'grande2_price', 'medio4_price', 'grande4_price', 
                             'medio6_price', 'grande6_price', 'outro_pico_price', 'xama_price', 
                             'praca_4f_price', 'cracha_epica_price']
            for field in expected_fields:
                if field not in response:
                    print(f"❌ Missing field in boss prices: {field}")
                    return False
            print("✅ Boss prices structure is correct")
        return success

    def test_update_boss_prices(self):
        """Test updating boss prices"""
        price_data = {
            "medio2_price": 0.05,
            "grande2_price": 0.10,
            "medio4_price": 0.15
        }
        return self.run_test("Update Boss Prices", "PUT", "boss-prices", 200, price_data)

    def test_create_account(self):
        """Test creating a new account"""
        account_data = {
            "name": f"TestAccount_{datetime.now().strftime('%H%M%S')}",
            "bosses": {
                "medio2": 5,
                "grande2": 3,
                "medio4": 2,
                "grande4": 1,
                "medio6": 1,
                "grande6": 0,
                "outro_pico": 0
            },
            "sala_pico": "Pico 2F",
            "special_bosses": {
                "xama": 1,
                "praca_4f": 0,
                "cracha_epica": 0
            },
            "gold": 1500.50
        }
        
        success, response = self.run_test("Create Account", "POST", "accounts", 200, account_data)
        if success and 'id' in response:
            self.test_account_id = response['id']
            print(f"✅ Created account with ID: {self.test_account_id}")
            
            # Verify USD calculation
            if 'total_usd' in response:
                print(f"✅ USD calculation present: ${response['total_usd']}")
            else:
                print("❌ Missing USD calculation in response")
                return False
        return success

    def test_get_accounts(self):
        """Test getting all accounts"""
        success, response = self.run_test("Get All Accounts", "GET", "accounts", 200)
        if success:
            if isinstance(response, list):
                print(f"✅ Retrieved {len(response)} accounts")
                if len(response) > 0:
                    # Check first account structure
                    account = response[0]
                    required_fields = ['id', 'name', 'bosses', 'special_bosses', 'gold', 'total_usd']
                    for field in required_fields:
                        if field not in account:
                            print(f"❌ Missing field in account: {field}")
                            return False
                    print("✅ Account structure is correct")
            else:
                print("❌ Response is not a list")
                return False
        return success

    def test_get_single_account(self):
        """Test getting a single account by ID"""
        if not self.test_account_id:
            print("❌ No test account ID available")
            return False
        
        return self.run_test("Get Single Account", "GET", f"accounts/{self.test_account_id}", 200)

    def test_update_account(self):
        """Test updating an account"""
        if not self.test_account_id:
            print("❌ No test account ID available")
            return False
        
        update_data = {
            "name": "UpdatedTestAccount",
            "gold": 2000.75,
            "bosses": {
                "medio2": 10,
                "grande2": 5
            }
        }
        
        return self.run_test("Update Account", "PUT", f"accounts/{self.test_account_id}", 200, update_data)

    def test_get_statistics(self):
        """Test getting statistics"""
        success, response = self.run_test("Get Statistics", "GET", "statistics", 200)
        if success:
            required_fields = ['total_accounts', 'total_bosses', 'total_special_bosses', 'total_gold', 'total_usd']
            for field in required_fields:
                if field not in response:
                    print(f"❌ Missing field in statistics: {field}")
                    return False
            print("✅ Statistics structure is correct")
        return success

    def test_delete_account(self):
        """Test deleting an account"""
        if not self.test_account_id:
            print("❌ No test account ID available")
            return False
        
        return self.run_test("Delete Account", "DELETE", f"accounts/{self.test_account_id}", 200)

    def test_error_cases(self):
        """Test error handling"""
        print("\n🔍 Testing Error Cases...")
        
        # Test getting non-existent account
        success, _ = self.run_test("Get Non-existent Account", "GET", "accounts/non-existent-id", 404)
        
        # Test updating non-existent account
        success2, _ = self.run_test("Update Non-existent Account", "PUT", "accounts/non-existent-id", 404, {"name": "test"})
        
        # Test deleting non-existent account
        success3, _ = self.run_test("Delete Non-existent Account", "DELETE", "accounts/non-existent-id", 404)
        
        return success and success2 and success3

def main():
    print("🚀 Starting MIR4 Account Manager API Tests")
    print("=" * 50)
    
    tester = MIR4APITester()
    
    # Run all tests in sequence
    test_results = []
    
    # Basic API tests
    test_results.append(tester.test_root_endpoint())
    test_results.append(tester.test_get_boss_prices())
    test_results.append(tester.test_update_boss_prices())
    
    # Account CRUD tests
    test_results.append(tester.test_create_account())
    test_results.append(tester.test_get_accounts())
    test_results.append(tester.test_get_single_account())
    test_results.append(tester.test_update_account())
    test_results.append(tester.test_get_statistics())
    
    # Error handling tests
    test_results.append(tester.test_error_cases())
    
    # Clean up - delete test account
    test_results.append(tester.test_delete_account())
    
    # Print final results
    print("\n" + "=" * 50)
    print(f"📊 Final Results: {tester.tests_passed}/{tester.tests_run} tests passed")
    
    if tester.tests_passed == tester.tests_run:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())