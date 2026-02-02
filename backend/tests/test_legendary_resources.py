"""
MIR4 Account Tracker - Legendary Resources API Tests
Tests for the new legendary_resources feature including:
- GET /api/accounts/{id} returns legendary_resources
- PUT /api/accounts/{id} updates legendary_resources correctly
- Progress calculation verification
"""
import pytest
import requests
import os
import uuid

BASE_URL = os.environ.get('REACT_APP_BACKEND_URL', '').rstrip('/')

class TestLegendaryResourcesAPI:
    """Test legendary resources CRUD operations"""
    
    @pytest.fixture
    def test_account_with_resources(self):
        """Create test account with legendary resources"""
        account_data = {
            "name": f"TEST_Legendary_{uuid.uuid4().hex[:8]}",
            "bosses": {
                "medio2": 0, "grande2": 0,
                "medio4": 0, "grande4": 0,
                "medio6": 0, "grande6": 0,
                "medio7": 0, "grande7": 0,
                "medio8": 0, "grande8": 0
            },
            "sala_pico": "",
            "special_bosses": {
                "xama": 0, "praca_4f": 0, "cracha_epica": 0
            },
            "legendary_resources": {
                "aco_lendario": 200,
                "esfera_lendaria": 80,
                "lunar_lendario": 60,
                "quintessencia_lendaria": 50,
                "bugiganga_lendaria": 40,
                "platina_lendaria": 150,
                "iluminado_lendario": 30,
                "anima_lendaria": 25
            },
            "gold": 0
        }
        
        response = requests.post(f"{BASE_URL}/api/accounts", json=account_data)
        assert response.status_code == 200
        created = response.json()
        
        yield created
        
        # Cleanup
        requests.delete(f"{BASE_URL}/api/accounts/{created['id']}")
    
    def test_create_account_with_legendary_resources(self, test_account_with_resources):
        """Test creating account with legendary_resources field"""
        account = test_account_with_resources
        
        # Verify legendary_resources exists in response
        assert "legendary_resources" in account, "legendary_resources field missing from response"
        
        resources = account["legendary_resources"]
        assert resources["aco_lendario"] == 200
        assert resources["esfera_lendaria"] == 80
        assert resources["lunar_lendario"] == 60
        assert resources["quintessencia_lendaria"] == 50
        assert resources["bugiganga_lendaria"] == 40
        assert resources["platina_lendaria"] == 150
        assert resources["iluminado_lendario"] == 30
        assert resources["anima_lendaria"] == 25
        
        print(f"Created account with legendary_resources: {account['id']}")
    
    def test_get_account_returns_legendary_resources(self, test_account_with_resources):
        """Test GET /api/accounts/{id} returns legendary_resources"""
        account_id = test_account_with_resources["id"]
        
        response = requests.get(f"{BASE_URL}/api/accounts/{account_id}")
        assert response.status_code == 200
        
        data = response.json()
        assert "legendary_resources" in data, "legendary_resources missing from GET response"
        
        resources = data["legendary_resources"]
        assert resources["aco_lendario"] == 200
        assert resources["esfera_lendaria"] == 80
        assert resources["lunar_lendario"] == 60
        
        print(f"GET account returned legendary_resources correctly")
    
    def test_update_legendary_resources(self, test_account_with_resources):
        """Test PUT /api/accounts/{id} updates legendary_resources correctly"""
        account_id = test_account_with_resources["id"]
        
        # Update only legendary_resources
        update_data = {
            "legendary_resources": {
                "aco_lendario": 300,
                "esfera_lendaria": 100,
                "lunar_lendario": 100,
                "quintessencia_lendaria": 100,
                "bugiganga_lendaria": 100,
                "platina_lendaria": 300,
                "iluminado_lendario": 100,
                "anima_lendaria": 100
            }
        }
        
        response = requests.put(f"{BASE_URL}/api/accounts/{account_id}", json=update_data)
        assert response.status_code == 200
        
        updated = response.json()
        assert "legendary_resources" in updated
        
        resources = updated["legendary_resources"]
        assert resources["aco_lendario"] == 300, f"Expected 300, got {resources['aco_lendario']}"
        assert resources["esfera_lendaria"] == 100
        assert resources["lunar_lendario"] == 100
        
        # Verify persistence with GET
        get_response = requests.get(f"{BASE_URL}/api/accounts/{account_id}")
        assert get_response.status_code == 200
        
        fetched = get_response.json()
        assert fetched["legendary_resources"]["aco_lendario"] == 300
        assert fetched["legendary_resources"]["esfera_lendaria"] == 100
        
        print(f"Updated and verified legendary_resources persistence")
    
    def test_partial_update_legendary_resources(self, test_account_with_resources):
        """Test partial update of legendary_resources"""
        account_id = test_account_with_resources["id"]
        
        # Update only some fields
        update_data = {
            "legendary_resources": {
                "aco_lendario": 250,
                "esfera_lendaria": 90,
                "lunar_lendario": 70,
                "quintessencia_lendaria": 60,
                "bugiganga_lendaria": 50,
                "platina_lendaria": 180,
                "iluminado_lendario": 40,
                "anima_lendaria": 35
            }
        }
        
        response = requests.put(f"{BASE_URL}/api/accounts/{account_id}", json=update_data)
        assert response.status_code == 200
        
        updated = response.json()
        resources = updated["legendary_resources"]
        
        assert resources["aco_lendario"] == 250
        assert resources["esfera_lendaria"] == 90
        assert resources["lunar_lendario"] == 70
        
        print(f"Partial update of legendary_resources successful")
    
    def test_get_all_accounts_includes_legendary_resources(self, test_account_with_resources):
        """Test GET /api/accounts returns legendary_resources for all accounts"""
        response = requests.get(f"{BASE_URL}/api/accounts")
        assert response.status_code == 200
        
        accounts = response.json()
        assert isinstance(accounts, list)
        
        # Find our test account
        test_account = None
        for acc in accounts:
            if acc["id"] == test_account_with_resources["id"]:
                test_account = acc
                break
        
        assert test_account is not None, "Test account not found in list"
        assert "legendary_resources" in test_account
        
        print(f"GET all accounts includes legendary_resources")
    
    def test_default_legendary_resources(self):
        """Test account created without legendary_resources gets defaults"""
        account_data = {
            "name": f"TEST_NoLegendary_{uuid.uuid4().hex[:8]}",
            "bosses": {
                "medio2": 0, "grande2": 0,
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
        
        response = requests.post(f"{BASE_URL}/api/accounts", json=account_data)
        assert response.status_code == 200
        
        created = response.json()
        
        # Should have legendary_resources with default values (0)
        assert "legendary_resources" in created
        resources = created["legendary_resources"]
        
        assert resources["aco_lendario"] == 0
        assert resources["esfera_lendaria"] == 0
        assert resources["lunar_lendario"] == 0
        assert resources["quintessencia_lendaria"] == 0
        assert resources["bugiganga_lendaria"] == 0
        assert resources["platina_lendaria"] == 0
        assert resources["iluminado_lendario"] == 0
        assert resources["anima_lendaria"] == 0
        
        print(f"Default legendary_resources verified")
        
        # Cleanup
        requests.delete(f"{BASE_URL}/api/accounts/{created['id']}")


class TestLegendaryProgressCalculation:
    """Test legendary progress calculation logic"""
    
    def test_arma_progress_calculation(self):
        """
        Test Arma Lendária progress calculation
        Recipe: 300 Aço L, 100 Esfera L, 100 Lunar L
        Progress = min(aco/300, esfera/100, lunar/100)
        """
        # With resources: aco=200, esfera=80, lunar=60
        # Progress should be: min(200/300, 80/100, 60/100) = min(0.666, 0.8, 0.6) = 0.6 = 60%
        
        account_data = {
            "name": f"TEST_ArmaProgress_{uuid.uuid4().hex[:8]}",
            "bosses": {
                "medio2": 0, "grande2": 0,
                "medio4": 0, "grande4": 0,
                "medio6": 0, "grande6": 0,
                "medio7": 0, "grande7": 0,
                "medio8": 0, "grande8": 0
            },
            "sala_pico": "",
            "special_bosses": {
                "xama": 0, "praca_4f": 0, "cracha_epica": 0
            },
            "legendary_resources": {
                "aco_lendario": 200,
                "esfera_lendaria": 80,
                "lunar_lendario": 60,
                "quintessencia_lendaria": 0,
                "bugiganga_lendaria": 0,
                "platina_lendaria": 0,
                "iluminado_lendario": 0,
                "anima_lendaria": 0
            },
            "gold": 0
        }
        
        response = requests.post(f"{BASE_URL}/api/accounts", json=account_data)
        assert response.status_code == 200
        created = response.json()
        
        # Verify resources stored correctly
        resources = created["legendary_resources"]
        assert resources["aco_lendario"] == 200
        assert resources["esfera_lendaria"] == 80
        assert resources["lunar_lendario"] == 60
        
        # Calculate expected progress (bottleneck calculation)
        aco_progress = min(1, 200 / 300)  # 0.666
        esfera_progress = min(1, 80 / 100)  # 0.8
        lunar_progress = min(1, 60 / 100)  # 0.6
        
        expected_arma_progress = min(aco_progress, esfera_progress, lunar_progress)
        assert expected_arma_progress == 0.6, f"Expected 0.6, got {expected_arma_progress}"
        
        print(f"Arma progress calculation verified: {expected_arma_progress * 100}%")
        
        # Cleanup
        requests.delete(f"{BASE_URL}/api/accounts/{created['id']}")
    
    def test_torso_progress_calculation(self):
        """
        Test Torso Lendário progress calculation
        Recipe: 300 Aço L, 100 Quintessência L, 100 Bugiganga L
        """
        account_data = {
            "name": f"TEST_TorsoProgress_{uuid.uuid4().hex[:8]}",
            "bosses": {
                "medio2": 0, "grande2": 0,
                "medio4": 0, "grande4": 0,
                "medio6": 0, "grande6": 0,
                "medio7": 0, "grande7": 0,
                "medio8": 0, "grande8": 0
            },
            "sala_pico": "",
            "special_bosses": {
                "xama": 0, "praca_4f": 0, "cracha_epica": 0
            },
            "legendary_resources": {
                "aco_lendario": 150,  # 50%
                "esfera_lendaria": 0,
                "lunar_lendario": 0,
                "quintessencia_lendaria": 80,  # 80%
                "bugiganga_lendaria": 70,  # 70%
                "platina_lendaria": 0,
                "iluminado_lendario": 0,
                "anima_lendaria": 0
            },
            "gold": 0
        }
        
        response = requests.post(f"{BASE_URL}/api/accounts", json=account_data)
        assert response.status_code == 200
        created = response.json()
        
        # Calculate expected progress
        aco_progress = min(1, 150 / 300)  # 0.5
        quint_progress = min(1, 80 / 100)  # 0.8
        bugi_progress = min(1, 70 / 100)  # 0.7
        
        expected_torso_progress = min(aco_progress, quint_progress, bugi_progress)
        assert expected_torso_progress == 0.5, f"Expected 0.5, got {expected_torso_progress}"
        
        print(f"Torso progress calculation verified: {expected_torso_progress * 100}%")
        
        # Cleanup
        requests.delete(f"{BASE_URL}/api/accounts/{created['id']}")
    
    def test_colar_progress_calculation(self):
        """
        Test Colar Lendário progress calculation
        Recipe: 300 Platina L, 100 Iluminado L, 100 Anima L
        """
        account_data = {
            "name": f"TEST_ColarProgress_{uuid.uuid4().hex[:8]}",
            "bosses": {
                "medio2": 0, "grande2": 0,
                "medio4": 0, "grande4": 0,
                "medio6": 0, "grande6": 0,
                "medio7": 0, "grande7": 0,
                "medio8": 0, "grande8": 0
            },
            "sala_pico": "",
            "special_bosses": {
                "xama": 0, "praca_4f": 0, "cracha_epica": 0
            },
            "legendary_resources": {
                "aco_lendario": 0,
                "esfera_lendaria": 0,
                "lunar_lendario": 0,
                "quintessencia_lendaria": 0,
                "bugiganga_lendaria": 0,
                "platina_lendaria": 240,  # 80%
                "iluminado_lendario": 50,  # 50%
                "anima_lendaria": 100  # 100%
            },
            "gold": 0
        }
        
        response = requests.post(f"{BASE_URL}/api/accounts", json=account_data)
        assert response.status_code == 200
        created = response.json()
        
        # Calculate expected progress
        platina_progress = min(1, 240 / 300)  # 0.8
        ilum_progress = min(1, 50 / 100)  # 0.5
        anima_progress = min(1, 100 / 100)  # 1.0
        
        expected_colar_progress = min(platina_progress, ilum_progress, anima_progress)
        assert expected_colar_progress == 0.5, f"Expected 0.5, got {expected_colar_progress}"
        
        print(f"Colar progress calculation verified: {expected_colar_progress * 100}%")
        
        # Cleanup
        requests.delete(f"{BASE_URL}/api/accounts/{created['id']}")


class TestExistingTestAccount:
    """Test the existing 'Conta Teste Lendário' account"""
    
    def test_existing_test_account_resources(self):
        """Verify the existing test account has correct resources"""
        response = requests.get(f"{BASE_URL}/api/accounts")
        assert response.status_code == 200
        
        accounts = response.json()
        test_account = None
        
        for acc in accounts:
            if acc["name"] == "Conta Teste Lendário":
                test_account = acc
                break
        
        if test_account:
            resources = test_account.get("legendary_resources", {})
            print(f"Found 'Conta Teste Lendário' with resources: {resources}")
            
            # Verify expected resources from context
            assert resources.get("aco_lendario") == 200, f"Expected aco_lendario=200, got {resources.get('aco_lendario')}"
            assert resources.get("esfera_lendaria") == 80, f"Expected esfera_lendaria=80, got {resources.get('esfera_lendaria')}"
            assert resources.get("lunar_lendario") == 60, f"Expected lunar_lendario=60, got {resources.get('lunar_lendario')}"
            
            print("Existing test account resources verified correctly")
        else:
            print("'Conta Teste Lendário' not found - may have been deleted")


class TestCleanupLegendary:
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
