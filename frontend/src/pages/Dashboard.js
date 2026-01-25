import { useState, useEffect } from "react";
import axios from "axios";
import { Coins, TrendingUp, Users, Settings, Plus } from "lucide-react";
import { Button } from "../components/ui/button";
import AccountTable from "../components/AccountTable";
import AccountDialog from "../components/AccountDialog";
import BossPriceDialog from "../components/BossPriceDialog";
import StatCard from "../components/StatCard";
import { toast } from "sonner";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

export default function Dashboard() {
  const [accounts, setAccounts] = useState([]);
  const [statistics, setStatistics] = useState(null);
  const [bossPrices, setBossPrices] = useState(null);
  const [loading, setLoading] = useState(true);
  const [showAccountDialog, setShowAccountDialog] = useState(false);
  const [showPriceDialog, setShowPriceDialog] = useState(false);
  const [editingAccount, setEditingAccount] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [accountsRes, statsRes, pricesRes] = await Promise.all([
        axios.get(`${API}/accounts`),
        axios.get(`${API}/statistics`),
        axios.get(`${API}/boss-prices`)
      ]);
      
      setAccounts(accountsRes.data);
      setStatistics(statsRes.data);
      setBossPrices(pricesRes.data);
    } catch (error) {
      console.error("Erro ao carregar dados:", error);
      toast.error("Erro ao carregar dados");
    } finally {
      setLoading(false);
    }
  };

  const handleAddAccount = () => {
    setEditingAccount(null);
    setShowAccountDialog(true);
  };

  const handleEditAccount = (account) => {
    setEditingAccount(account);
    setShowAccountDialog(true);
  };

  const handleDeleteAccount = async (accountId) => {
    try {
      await axios.delete(`${API}/accounts/${accountId}`);
      toast.success("Conta deletada com sucesso!");
      fetchData();
    } catch (error) {
      console.error("Erro ao deletar conta:", error);
      toast.error("Erro ao deletar conta");
    }
  };

  const handleSaveAccount = async (accountData) => {
    try {
      if (editingAccount) {
        await axios.put(`${API}/accounts/${editingAccount.id}`, accountData);
        toast.success("Conta atualizada com sucesso!");
      } else {
        await axios.post(`${API}/accounts`, accountData);
        toast.success("Conta criada com sucesso!");
      }
      setShowAccountDialog(false);
      setEditingAccount(null);
      fetchData();
    } catch (error) {
      console.error("Erro ao salvar conta:", error);
      toast.error("Erro ao salvar conta");
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
    <div className="min-h-screen py-8 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8 relative">
          <div
            className="absolute inset-0 opacity-10 bg-cover bg-center rounded-2xl"
            style={{
              backgroundImage: `url('https://images.unsplash.com/photo-1594968549077-43f0a90bd7aa?auto=format&fit=crop&w=2000&q=80')`
            }}
          />
          <div className="relative bg-mir-charcoal/80 backdrop-blur-xl border border-white/5 rounded-2xl p-8 shadow-2xl">
            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
              <div>
                <h1 className="text-4xl sm:text-5xl font-secondary font-bold text-mir-gold tracking-wide uppercase mb-2" data-testid="dashboard-title">
                  MIR4 Manager
                </h1>
                <p className="text-slate-400 font-primary" data-testid="dashboard-subtitle">
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
                  Preços
                </Button>
              </div>
            </div>
          </div>
        </div>

        {/* Statistics Cards */}
        {statistics && (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
            <StatCard
              title="Total de Contas"
              value={statistics.total_accounts}
              icon={<Users className="w-6 h-6" />}
              color="gold"
              testId="stat-total-accounts"
            />
            <StatCard
              title="Total Gold"
              value={statistics.total_gold.toLocaleString('pt-BR')}
              icon={<Coins className="w-6 h-6" />}
              color="blue"
              testId="stat-total-gold"
            />
            <StatCard
              title="Total USD"
              value={`$${statistics.total_usd.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}`}
              icon={<TrendingUp className="w-6 h-6" />}
              color="green"
              testId="stat-total-usd"
            />
            <StatCard
              title="Boss de Pico"
              value={
                Object.values(statistics.total_bosses).reduce((a, b) => a + b, 0)
              }
              icon={<Coins className="w-6 h-6" />}
              color="red"
              testId="stat-total-bosses"
            />
          </div>
        )}

        {/* Accounts Table */}
        <div className="bg-mir-charcoal/50 border border-white/5 rounded-xl shadow-2xl overflow-hidden">
          <AccountTable
            accounts={accounts}
            bossPrices={bossPrices}
            onEdit={handleEditAccount}
            onDelete={handleDeleteAccount}
          />
        </div>
      </div>

      {/* Dialogs */}
      <AccountDialog
        open={showAccountDialog}
        onOpenChange={setShowAccountDialog}
        account={editingAccount}
        onSave={handleSaveAccount}
      />

      <BossPriceDialog
        open={showPriceDialog}
        onOpenChange={setShowPriceDialog}
        bossPrices={bossPrices}
        onSave={handleSavePrices}
      />
    </div>
  );
}
