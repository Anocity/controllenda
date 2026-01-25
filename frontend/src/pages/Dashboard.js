import { useState, useEffect } from "react";
import axios from "axios";
import { Plus, Settings } from "lucide-react";
import { Button } from "../components/ui/button";
import EditableTable from "../components/EditableTable";
import BossPriceDialog from "../components/BossPriceDialog";
import { toast } from "sonner";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

export default function Dashboard() {
  const [accounts, setAccounts] = useState([]);
  const [bossPrices, setBossPrices] = useState(null);
  const [loading, setLoading] = useState(true);
  const [showPriceDialog, setShowPriceDialog] = useState(false);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [accountsRes, pricesRes] = await Promise.all([
        axios.get(`${API}/accounts`),
        axios.get(`${API}/boss-prices`)
      ]);
      
      setAccounts(accountsRes.data);
      setBossPrices(pricesRes.data);
    } catch (error) {
      console.error("Erro ao carregar dados:", error);
      toast.error("Erro ao carregar dados");
    } finally {
      setLoading(false);
    }
  };

  const handleAddAccount = async () => {
    try {
      const newAccount = {
        name: "Nova Conta",
        bosses: {
          medio2: 0,
          grande2: 0,
          medio4: 0,
          grande4: 0,
          medio6: 0,
          grande6: 0,
          outro_pico: 0
        },
        sala_pico: "",
        special_bosses: {
          xama: 0,
          praca_4f: 0,
          cracha_epica: 0
        },
        gold: 0
      };
      
      const response = await axios.post(`${API}/accounts`, newAccount);
      setAccounts([...accounts, response.data]);
      toast.success("Nova conta adicionada!");
    } catch (error) {
      console.error("Erro ao adicionar conta:", error);
      toast.error("Erro ao adicionar conta");
    }
  };

  const handleUpdateAccount = async (accountId, field, value) => {
    try {
      await axios.put(`${API}/accounts/${accountId}`, { [field]: value });
      // Update local state
      const updatedAccounts = accounts.map(acc => 
        acc.id === accountId ? { ...acc, [field]: value } : acc
      );
      setAccounts(updatedAccounts);
    } catch (error) {
      console.error("Erro ao atualizar conta:", error);
      toast.error("Erro ao atualizar conta");
    }
  };

  const handleDeleteAccount = async (accountId) => {
    try {
      await axios.delete(`${API}/accounts/${accountId}`);
      setAccounts(accounts.filter(acc => acc.id !== accountId));
      toast.success("Conta deletada!");
    } catch (error) {
      console.error("Erro ao deletar conta:", error);
      toast.error("Erro ao deletar conta");
    }
  };

  const handleSavePrices = async (priceData) => {
    try {
      await axios.put(`${API}/boss-prices`, priceData);
      toast.success("Preços atualizados com sucesso!");
      setShowPriceDialog(false);
      fetchData();
    } catch (error) {
      console.error("Erro ao atualizar preços:", error);
      toast.error("Erro ao atualizar preços");
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-mir-gold font-secondary text-2xl">Carregando...</div>
      </div>
    );
  }

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
            onRefresh={fetchData}
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
