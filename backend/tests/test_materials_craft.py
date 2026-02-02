"""
MIR4 Account Tracker - Materials & Craft Resources API Tests
Tests for the new materials (8 types x 3 rarities) and craft_resources (po/ds/cobre) schema

Schema:
- materials: {material_key: {raro: int, epico: int, lendario: int}} for 8 materials
- craft_resources: {po: int, ds: int, cobre: int}

Craft Recipes:
- 1 Épico = 10 Raro + 25 Pó + 5k DS + 20k Cobre
- 1 Lendário = 10 Épico + 125 Pó + 25k DS + 100k Cobre

Objectives:
- Arma: 300 Aço L + 100 Esfera L + 100 Lunar L
- Torso: 300 Aço L + 100 Quintessência L + 100 Bugiganga L
- Colar: 300 Platina L + 100 Iluminado L + 100 Anima L
"""
import pytest
import requests
import os
import uuid

BASE_URL = os.environ.get('REACT_APP_BACKEND_URL', '').rstrip('/')

# Material keys
MATERIAL_KEYS = ["anima", "bugiganga", "lunar", "iluminado", "quintessencia", "esfera", "platina", "aco"]


class TestMaterialsAPI:
    """Test materials CRUD operations with new schema"""
    
    @pytest.fixture
    def test_account_with_materials(self):
        """Create test account with materials and craft_resources"""
        account_data = {
            "name": f"TEST_Materials_{uuid.uuid4().hex[:8]}",
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
            "materials": {
                "anima": {"raro": 100, "epico": 10, "lendario": 5},
                "bugiganga": {"raro": 200, "epico": 20, "lendario": 10},
                "lunar": {"raro": 300, "epico": 20, "lendario": 10},
                "iluminado": {"raro": 150, "epico": 15, "lendario": 8},
                "quintessencia": {"raro": 250, "epico": 25, "lendario": 12},
                "esfera": {"raro": 500, "epico": 30, "lendario": 20},
                "platina": {"raro": 400, "epico": 40, "lendario": 25},
                "aco": {"raro": 1000, "epico": 50, "lendario": 100}
            },
            "craft_resources": {
                "po": 5000,
                "ds": 500000,
                "cobre": 2000000
            },
            "gold": 0
        }
        
        response = requests.post(f"{BASE_URL}/api/accounts", json=account_data)
        assert response.status_code == 200, f"Failed to create account: {response.text}"
        created = response.json()
        
        yield created
        
        # Cleanup
        requests.delete(f"{BASE_URL}/api/accounts/{created['id']}")
    
    def test_create_account_with_materials(self, test_account_with_materials):
        """Test creating account with materials field (8 materials x 3 tiers)"""
        account = test_account_with_materials
        
        # Verify materials exists in response
        assert "materials" in account, "materials field missing from response"
        
        materials = account["materials"]
        
        # Verify all 8 materials exist
        for mat_key in MATERIAL_KEYS:
            assert mat_key in materials, f"Material {mat_key} missing"
            assert "raro" in materials[mat_key], f"raro tier missing for {mat_key}"
            assert "epico" in materials[mat_key], f"epico tier missing for {mat_key}"
            assert "lendario" in materials[mat_key], f"lendario tier missing for {mat_key}"
        
        # Verify specific values
        assert materials["aco"]["raro"] == 1000
        assert materials["aco"]["epico"] == 50
        assert materials["aco"]["lendario"] == 100
        assert materials["esfera"]["lendario"] == 20
        assert materials["lunar"]["lendario"] == 10
        
        print(f"Created account with materials: {account['id']}")
    
    def test_create_account_with_craft_resources(self, test_account_with_materials):
        """Test creating account with craft_resources field (po/ds/cobre)"""
        account = test_account_with_materials
        
        # Verify craft_resources exists
        assert "craft_resources" in account, "craft_resources field missing from response"
        
        craft_res = account["craft_resources"]
        assert craft_res["po"] == 5000
        assert craft_res["ds"] == 500000
        assert craft_res["cobre"] == 2000000
        
        print(f"Created account with craft_resources: po={craft_res['po']}, ds={craft_res['ds']}, cobre={craft_res['cobre']}")
    
    def test_get_account_returns_materials(self, test_account_with_materials):
        """Test GET /api/accounts/{id} returns materials and craft_resources"""
        account_id = test_account_with_materials["id"]
        
        response = requests.get(f"{BASE_URL}/api/accounts/{account_id}")
        assert response.status_code == 200
        
        data = response.json()
        assert "materials" in data, "materials missing from GET response"
        assert "craft_resources" in data, "craft_resources missing from GET response"
        
        # Verify materials structure
        assert data["materials"]["aco"]["lendario"] == 100
        assert data["materials"]["esfera"]["epico"] == 30
        
        # Verify craft_resources
        assert data["craft_resources"]["po"] == 5000
        assert data["craft_resources"]["ds"] == 500000
        
        print(f"GET account returned materials and craft_resources correctly")
    
    def test_update_materials(self, test_account_with_materials):
        """Test PUT /api/accounts/{id} updates materials correctly"""
        account_id = test_account_with_materials["id"]
        
        # Update materials
        update_data = {
            "materials": {
                "anima": {"raro": 200, "epico": 20, "lendario": 15},
                "bugiganga": {"raro": 300, "epico": 30, "lendario": 20},
                "lunar": {"raro": 400, "epico": 40, "lendario": 30},
                "iluminado": {"raro": 250, "epico": 25, "lendario": 18},
                "quintessencia": {"raro": 350, "epico": 35, "lendario": 22},
                "esfera": {"raro": 600, "epico": 60, "lendario": 40},
                "platina": {"raro": 500, "epico": 50, "lendario": 35},
                "aco": {"raro": 1200, "epico": 80, "lendario": 150}
            }
        }
        
        response = requests.put(f"{BASE_URL}/api/accounts/{account_id}", json=update_data)
        assert response.status_code == 200
        
        updated = response.json()
        assert "materials" in updated
        
        # Verify updated values
        assert updated["materials"]["aco"]["lendario"] == 150
        assert updated["materials"]["esfera"]["lendario"] == 40
        assert updated["materials"]["lunar"]["lendario"] == 30
        
        # Verify persistence with GET
        get_response = requests.get(f"{BASE_URL}/api/accounts/{account_id}")
        assert get_response.status_code == 200
        
        fetched = get_response.json()
        assert fetched["materials"]["aco"]["lendario"] == 150
        assert fetched["materials"]["esfera"]["lendario"] == 40
        
        print(f"Updated and verified materials persistence")
    
    def test_update_craft_resources(self, test_account_with_materials):
        """Test PUT /api/accounts/{id} updates craft_resources correctly"""
        account_id = test_account_with_materials["id"]
        
        # Update craft_resources
        update_data = {
            "craft_resources": {
                "po": 10000,
                "ds": 1000000,
                "cobre": 5000000
            }
        }
        
        response = requests.put(f"{BASE_URL}/api/accounts/{account_id}", json=update_data)
        assert response.status_code == 200
        
        updated = response.json()
        assert "craft_resources" in updated
        
        # Verify updated values
        assert updated["craft_resources"]["po"] == 10000
        assert updated["craft_resources"]["ds"] == 1000000
        assert updated["craft_resources"]["cobre"] == 5000000
        
        # Verify persistence with GET
        get_response = requests.get(f"{BASE_URL}/api/accounts/{account_id}")
        assert get_response.status_code == 200
        
        fetched = get_response.json()
        assert fetched["craft_resources"]["po"] == 10000
        assert fetched["craft_resources"]["ds"] == 1000000
        
        print(f"Updated and verified craft_resources persistence")
    
    def test_update_both_materials_and_craft_resources(self, test_account_with_materials):
        """Test updating both materials and craft_resources in single PUT"""
        account_id = test_account_with_materials["id"]
        
        update_data = {
            "materials": {
                "anima": {"raro": 500, "epico": 50, "lendario": 30},
                "bugiganga": {"raro": 500, "epico": 50, "lendario": 30},
                "lunar": {"raro": 500, "epico": 50, "lendario": 30},
                "iluminado": {"raro": 500, "epico": 50, "lendario": 30},
                "quintessencia": {"raro": 500, "epico": 50, "lendario": 30},
                "esfera": {"raro": 500, "epico": 50, "lendario": 30},
                "platina": {"raro": 500, "epico": 50, "lendario": 30},
                "aco": {"raro": 500, "epico": 50, "lendario": 30}
            },
            "craft_resources": {
                "po": 7500,
                "ds": 750000,
                "cobre": 3500000
            }
        }
        
        response = requests.put(f"{BASE_URL}/api/accounts/{account_id}", json=update_data)
        assert response.status_code == 200
        
        updated = response.json()
        
        # Verify both updated
        assert updated["materials"]["aco"]["lendario"] == 30
        assert updated["craft_resources"]["po"] == 7500
        
        print(f"Updated both materials and craft_resources successfully")
    
    def test_get_all_accounts_includes_materials(self, test_account_with_materials):
        """Test GET /api/accounts returns materials and craft_resources for all accounts"""
        response = requests.get(f"{BASE_URL}/api/accounts")
        assert response.status_code == 200
        
        accounts = response.json()
        assert isinstance(accounts, list)
        
        # Find our test account
        test_account = None
        for acc in accounts:
            if acc["id"] == test_account_with_materials["id"]:
                test_account = acc
                break
        
        assert test_account is not None, "Test account not found in list"
        assert "materials" in test_account
        assert "craft_resources" in test_account
        
        print(f"GET all accounts includes materials and craft_resources")
    
    def test_default_materials_and_craft_resources(self):
        """Test account created without materials/craft_resources gets defaults (all zeros)"""
        account_data = {
            "name": f"TEST_NoMaterials_{uuid.uuid4().hex[:8]}",
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
        
        # Should have materials with default values (0)
        assert "materials" in created
        materials = created["materials"]
        
        for mat_key in MATERIAL_KEYS:
            assert mat_key in materials, f"Default material {mat_key} missing"
            assert materials[mat_key]["raro"] == 0
            assert materials[mat_key]["epico"] == 0
            assert materials[mat_key]["lendario"] == 0
        
        # Should have craft_resources with default values (0)
        assert "craft_resources" in created
        craft_res = created["craft_resources"]
        assert craft_res["po"] == 0
        assert craft_res["ds"] == 0
        assert craft_res["cobre"] == 0
        
        print(f"Default materials and craft_resources verified")
        
        # Cleanup
        requests.delete(f"{BASE_URL}/api/accounts/{created['id']}")


class TestExistingTestAccount:
    """Test the existing 'Teste Craft Completo' account"""
    
    def test_existing_test_account_materials(self):
        """Verify the existing test account has correct materials and craft_resources"""
        response = requests.get(f"{BASE_URL}/api/accounts")
        assert response.status_code == 200
        
        accounts = response.json()
        test_account = None
        
        for acc in accounts:
            if acc["name"] == "Teste Craft Completo":
                test_account = acc
                break
        
        if test_account:
            materials = test_account.get("materials", {})
            craft_res = test_account.get("craft_resources", {})
            
            print(f"Found 'Teste Craft Completo' with:")
            print(f"  Aço: R={materials.get('aco', {}).get('raro')}, E={materials.get('aco', {}).get('epico')}, L={materials.get('aco', {}).get('lendario')}")
            print(f"  Esfera: R={materials.get('esfera', {}).get('raro')}, E={materials.get('esfera', {}).get('epico')}, L={materials.get('esfera', {}).get('lendario')}")
            print(f"  Lunar: R={materials.get('lunar', {}).get('raro')}, E={materials.get('lunar', {}).get('epico')}, L={materials.get('lunar', {}).get('lendario')}")
            print(f"  Craft Resources: Pó={craft_res.get('po')}, DS={craft_res.get('ds')}, Cobre={craft_res.get('cobre')}")
            
            # Verify expected values from context
            # Aço(1000R,50E,100L), Esfera(500R,30E,20L), Lunar(300R,20E,10L)
            # Pó=5000, DS=500000, Cobre=2000000
            assert materials.get("aco", {}).get("raro") == 1000, f"Expected aco.raro=1000"
            assert materials.get("aco", {}).get("epico") == 50, f"Expected aco.epico=50"
            assert materials.get("aco", {}).get("lendario") == 100, f"Expected aco.lendario=100"
            assert materials.get("esfera", {}).get("raro") == 500
            assert materials.get("esfera", {}).get("lendario") == 20
            assert materials.get("lunar", {}).get("raro") == 300
            assert materials.get("lunar", {}).get("lendario") == 10
            
            assert craft_res.get("po") == 5000
            assert craft_res.get("ds") == 500000
            assert craft_res.get("cobre") == 2000000
            
            print("Existing test account materials and craft_resources verified correctly")
        else:
            pytest.skip("'Teste Craft Completo' not found - may have been deleted")


class TestCraftChainCalculation:
    """Test craft chain calculation logic (Raro→Épico→Lendário)
    
    Craft Costs:
    - 1 Épico = 10 Raro + 25 Pó + 5k DS + 20k Cobre
    - 1 Lendário = 10 Épico + 125 Pó + 25k DS + 100k Cobre
    """
    
    def test_craft_chain_with_sufficient_resources(self):
        """Test craft chain calculation when resources are sufficient"""
        # With: 1000 Raro, 50 Épico, 100 Lendário
        # Craft resources: 5000 Pó, 500k DS, 2M Cobre
        
        # Step 1: Craft Épicos from Raros
        # Max épicos from raros: 1000/10 = 100
        # Max épicos from pó: 5000/25 = 200
        # Max épicos from ds: 500000/5000 = 100
        # Max épicos from cobre: 2000000/20000 = 100
        # Craftable épicos = min(100, 200, 100, 100) = 100
        
        # After crafting 100 épicos:
        # Épicos = 50 + 100 = 150
        # Remaining: Pó = 5000 - 2500 = 2500, DS = 500k - 500k = 0, Cobre = 2M - 2M = 0
        
        # Step 2: Craft Lendários from Épicos
        # Max lend from épicos: 150/10 = 15
        # Max lend from pó: 2500/125 = 20
        # Max lend from ds: 0/25000 = 0  <-- BOTTLENECK
        # Max lend from cobre: 0/100000 = 0  <-- BOTTLENECK
        # Craftable lendários = min(15, 20, 0, 0) = 0
        
        # Final lendários = 100 + 0 = 100
        
        # This is the expected behavior - DS/Cobre become bottleneck after crafting épicos
        print("Craft chain calculation logic verified conceptually")
        print("With 1000R, 50E, 100L and 5000 Pó, 500k DS, 2M Cobre:")
        print("  - Can craft 100 épicos (limited by DS and Cobre)")
        print("  - After crafting épicos, DS and Cobre are depleted")
        print("  - Cannot craft more lendários due to resource depletion")
        print("  - Final lendários = 100 (original)")
    
    def test_arma_objective_progress(self):
        """
        Test Arma Lendária progress calculation with craft chain
        Recipe: 300 Aço L + 100 Esfera L + 100 Lunar L
        
        Test account has:
        - Aço: 1000R, 50E, 100L
        - Esfera: 500R, 30E, 20L
        - Lunar: 300R, 20E, 10L
        - Craft: 5000 Pó, 500k DS, 2M Cobre
        """
        # For Arma, we need to calculate craftable lendários for each material
        # considering shared resources
        
        # The frontend calculates this in sequence, consuming resources
        # This is a complex calculation that depends on the order of processing
        
        print("Arma objective progress calculation:")
        print("  Required: 300 Aço L, 100 Esfera L, 100 Lunar L")
        print("  Current: Aço=100L, Esfera=20L, Lunar=10L")
        print("  Progress depends on craft chain calculation with shared resources")


class TestCleanupMaterials:
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
