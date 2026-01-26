import { useState, useEffect } from "react";
import { Plus, Settings } from "lucide-react";
import { Button } from "../components/ui/button";
import EditableTable from "../components/EditableTable";
import BossPriceDialog from "../components/BossPriceDialog";
import { toast } from "sonner";

// Helper functions for localStorage
const getAccounts = () => {
  const data = localStorage.getItem('mir4_accounts');
  return data ? JSON.parse(data) : [];
};

const saveAccounts = (accounts) => {
  localStorage.setItem('mir4_accounts', JSON.stringify(accounts));
};

const getBossPrices = () => {
  const data = localStorage.getItem('mir4_boss_prices');
  return data ? JSON.parse(data) : {
    medio2_price: 0.045,
    grande2_price: 0.09,
    medio4_price: 0.14,
    grande4_price: 0.18,
    medio6_price: 0.36,
    grande6_price: 0.45,
    medio7_price: 0,
    grande7_price: 0,
    medio8_price: 0,
    grande8_price: 0,
    xama_price: 0,
    praca_4f_price: 0,
    cracha_epica_price: 0
  };
};

const saveBossPrices = (prices) => {
  localStorage.setItem('mir4_boss_prices', JSON.stringify(prices));
};

const calculateAccountUSD = (account, prices) => {
  let total = 0;
  const bosses = account.bosses || {};
  const special = account.special_bosses || {};
  
  total += (bosses.medio2 || 0) * prices.medio2_price;
  total += (bosses.grande2 || 0) * prices.grande2_price;
  total += (bosses.medio4 || 0) * prices.medio4_price;
  total += (bosses.grande4 || 0) * prices.grande4_price;
  total += (bosses.medio6 || 0) * prices.medio6_price;
  total += (bosses.grande6 || 0) * prices.grande6_price;
  total += (bosses.medio7 || 0) * prices.medio7_price;
  total += (bosses.grande7 || 0) * prices.grande7_price;
  total += (bosses.medio8 || 0) * prices.medio8_price;
  total += (bosses.grande8 || 0) * prices.grande8_price;
  total += (special.xama || 0) * prices.xama_price;
  total += (special.praca_4f || 0) * prices.praca_4f_price;
  total += (special.cracha_epica || 0) * prices.cracha_epica_price;
  
  return parseFloat(total.toFixed(2));
};

export default function Dashboard() {
  const [accounts, setAccounts] = useState([]);
  const [bossPrices, setBossPrices] = useState(null);
  const [showPriceDialog, setShowPriceDialog] = useState(false);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = () => {
    const loadedAccounts = getAccounts();
    const loadedPrices = getBossPrices();
    
    // Calculate USD for each account
    const accountsWithUSD = loadedAccounts.map(account => ({
      ...account,
      total_usd: calculateAccountUSD(account, loadedPrices)
    }));
    
    setAccounts(accountsWithUSD);
    setBossPrices(loadedPrices);
  };

  const handleAddAccount = () => {
    const newAccount = {
      id: Date.now().toString(),
      name: "Nova Conta",
      bosses: {
        medio2: 0,
        grande2: 0,
        medio4: 0,
        grande4: 0,
        medio6: 0,
        grande6: 0,
        medio7: 0,
        grande7: 0,
        medio8: 0,
        grande8: 0
      },
      sala_pico: "",
      special_bosses: {
        xama: 0,
        praca_4f: 0,
        cracha_epica: 0
      },
      gold: 0,
      created_at: new Date().toISOString()
    };
    
    const updatedAccounts = [...accounts, { ...newAccount, total_usd: 0 }];
    setAccounts(updatedAccounts);
    saveAccounts(updatedAccounts);
    toast.success("Nova conta adicionada!");
  };

  const handleUpdateAccount = (accountId, field, value) => {
    const updatedAccounts = accounts.map(acc => {
      if (acc.id === accountId) {
        const updated = { ...acc, [field]: value };
        updated.total_usd = calculateAccountUSD(updated, bossPrices);
        return updated;
      }
      return acc;
    });
    
    setAccounts(updatedAccounts);
    saveAccounts(updatedAccounts);
  };

  const handleDeleteAccount = (accountId) => {
    const updatedAccounts = accounts.filter(acc => acc.id !== accountId);
    setAccounts(updatedAccounts);
    saveAccounts(updatedAccounts);
    toast.success("Conta deletada!");
  };

  const handleRefresh = () => {
    loadData();
  };

  const handleSavePrices = (priceData) => {
    saveBossPrices(priceData);
    setBossPrices(priceData);
    toast.success("Preços atualizados com sucesso!");
    setShowPriceDialog(false);
    loadData(); // Recalculate all USD values
  };

  return (
    <div className="min-h-screen py-6 px-4">
      <div className="max-w-[98%] mx-auto">
        {/* Header */}
        <div className="mb-6 bg-mir-charcoal/80 border border-white/5 rounded-xl p-6 shadow-xl">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-3xl font-secondary font-bold text-mir-gold tracking-wide uppercase" data-testid="dashboard-title">
                MIR4 Manager
              </h1>
              <p className="text-slate-400 font-primary text-sm mt-1">
                Gerencie suas contas e bosses
              </p>
            </div>
            <div className="flex gap-3">
              <Button
                onClick={handleAddAccount}
                className="bg-mir-gold text-black font-bold uppercase tracking-wider hover:bg-amber-400 shadow-[0_0_10px_rgba(255,215,0,0.3)] transition-all"
                data-testid="add-account-btn"
              >
                <Plus className="w-4 h-4 mr-2" />
                Nova Conta
              </Button>
              <Button
                onClick={() => setShowPriceDialog(true)}
                variant="outline"
                className="bg-white/5 text-white border-white/10 hover:bg-white/10 hover:border-white/20"
                data-testid="config-prices-btn"
              >
                <Settings className="w-4 h-4 mr-2" />
                Preços USD
              </Button>
            </div>
          </div>
        </div>

        {/* Editable Table */}
        <div className="bg-mir-charcoal/50 border border-white/5 rounded-xl shadow-2xl overflow-hidden">
          <EditableTable
            accounts={accounts}
            bossPrices={bossPrices}
            onUpdate={handleUpdateAccount}
            onDelete={handleDeleteAccount}
            onRefresh={handleRefresh}
          />
        </div>
      </div>

      {/* Price Dialog */}
      <BossPriceDialog
        open={showPriceDialog}
        onOpenChange={setShowPriceDialog}
        bossPrices={bossPrices}
        onSave={handleSavePrices}
      />
    </div>
  );
}
