import { useState, useEffect, useCallback } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "axios";
import { ArrowLeft, Trophy, Sword, Shield, Gem } from "lucide-react";
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";
import { toast } from "sonner";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL || "http://localhost:8001";
const API = `${BACKEND_URL}/api`;

// Receitas dos objetivos lendários
const LEGENDARY_RECIPES = {
  arma: {
    name: "Arma Lendária",
    icon: Sword,
    color: "text-red-400",
    bgColor: "bg-red-500/10",
    borderColor: "border-red-500/30",
    ingredients: [
      { key: "aco_lendario", name: "Aço Lendário", required: 300 },
      { key: "esfera_lendaria", name: "Esfera Lendária", required: 100 },
      { key: "lunar_lendario", name: "Lunar Lendário", required: 100 }
    ]
  },
  torso: {
    name: "Torso Lendário",
    icon: Shield,
    color: "text-blue-400",
    bgColor: "bg-blue-500/10",
    borderColor: "border-blue-500/30",
    ingredients: [
      { key: "aco_lendario", name: "Aço Lendário", required: 300 },
      { key: "quintessencia_lendaria", name: "Quintessência Lendária", required: 100 },
      { key: "bugiganga_lendaria", name: "Bugiganga Lendária", required: 100 }
    ]
  },
  colar: {
    name: "Colar Lendário",
    icon: Gem,
    color: "text-purple-400",
    bgColor: "bg-purple-500/10",
    borderColor: "border-purple-500/30",
    ingredients: [
      { key: "platina_lendaria", name: "Platina Lendária", required: 300 },
      { key: "iluminado_lendario", name: "Iluminado Lendário", required: 100 },
      { key: "anima_lendaria", name: "Anima Lendária", required: 100 }
    ]
  }
};

// Todos os recursos únicos
const ALL_RESOURCES = [
  { key: "aco_lendario", name: "Aço Lendário" },
  { key: "esfera_lendaria", name: "Esfera Lendária" },
  { key: "lunar_lendario", name: "Lunar Lendário" },
  { key: "quintessencia_lendaria", name: "Quintessência Lendária" },
  { key: "bugiganga_lendaria", name: "Bugiganga Lendária" },
  { key: "platina_lendaria", name: "Platina Lendária" },
  { key: "iluminado_lendario", name: "Iluminado Lendário" },
  { key: "anima_lendaria", name: "Anima Lendária" }
];

export default function AccountResources() {
  const { accountId } = useParams();
  const navigate = useNavigate();
  const [account, setAccount] = useState(null);
  const [loading, setLoading] = useState(true);
  const [localResources, setLocalResources] = useState({});

  const fetchAccount = useCallback(async () => {
    try {
      const response = await axios.get(`${API}/accounts/${accountId}`);
      setAccount(response.data);
      // Inicializa recursos locais com valores do servidor
      const resources = response.data.legendary_resources || {};
      setLocalResources(resources);
    } catch (error) {
      console.error("Erro ao carregar conta:", error);
      toast.error("Erro ao carregar dados da conta");
      navigate("/");
    } finally {
      setLoading(false);
    }
  }, [accountId, navigate]);

  useEffect(() => {
    fetchAccount();
  }, [fetchAccount]);

  const handleResourceChange = (key, value) => {
    const numValue = Math.max(0, parseInt(value) || 0);
    setLocalResources(prev => ({ ...prev, [key]: numValue }));
  };

  const handleResourceBlur = async (key) => {
    try {
      const updatedResources = { ...localResources };
      await axios.put(`${API}/accounts/${accountId}`, {
        legendary_resources: updatedResources
      });
      // Atualiza o account local sem reload
      setAccount(prev => ({
        ...prev,
        legendary_resources: updatedResources
      }));
    } catch (error) {
      console.error("Erro ao salvar recurso:", error);
      toast.error("Erro ao salvar recurso");
    }
  };

  // Calcula progresso de um objetivo
  const calculateObjectiveProgress = (objectiveKey) => {
    const recipe = LEGENDARY_RECIPES[objectiveKey];
    const resources = localResources || {};
    
    let minProgress = 1;
    const details = [];
    
    recipe.ingredients.forEach(ing => {
      const have = resources[ing.key] || 0;
      const progress = Math.min(1, have / ing.required);
      const missing = Math.max(0, ing.required - have);
      
      minProgress = Math.min(minProgress, progress);
      details.push({ ...ing, have, missing, progress });
    });
    
    return {
      progress: minProgress,
      percentage: Math.round(minProgress * 100),
      details
    };
  };

  // Encontra o objetivo mais próximo
  const findClosestObjective = () => {
    let closest = null;
    let highestProgress = -1;
    
    Object.keys(LEGENDARY_RECIPES).forEach(key => {
      const result = calculateObjectiveProgress(key);
      if (result.progress > highestProgress) {
        highestProgress = result.progress;
        closest = { key, ...LEGENDARY_RECIPES[key], ...result };
      }
    });
    
    return closest;
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-mir-gold font-secondary text-2xl">Carregando...</div>
      </div>
    );
  }

  if (!account) return null;

  const closest = findClosestObjective();

  return (
    <div className="min-h-screen py-4 px-3">
      <div className="max-w-[1200px] mx-auto">
        {/* Header */}
        <div className="mb-4 bg-mir-charcoal/80 border border-white/5 rounded-lg p-4 shadow-xl">
          <div className="flex justify-between items-center">
            <div className="flex items-center gap-3">
              <Button
                onClick={() => navigate("/")}
                variant="ghost"
                className="text-slate-400 hover:text-white p-2"
                data-testid="back-btn"
              >
                <ArrowLeft className="w-5 h-5" />
              </Button>
              <div>
                <h1 className="text-2xl font-secondary font-bold text-mir-gold tracking-wide uppercase" data-testid="account-name">
                  {account.name}
                </h1>
                <p className="text-slate-400 font-primary text-xs mt-1">
                  Recursos Lendários
                </p>
              </div>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
          {/* Bloco: Meus Recursos */}
          <div className="bg-mir-charcoal/50 border border-white/5 rounded-lg p-4 shadow-xl">
            <h2 className="text-lg font-secondary font-bold text-white mb-4" data-testid="resources-title">
              Meus Recursos
            </h2>
            <div className="grid grid-cols-2 gap-3">
              {ALL_RESOURCES.map(resource => (
                <div key={resource.key} className="flex items-center gap-2">
                  <label className="text-xs text-slate-400 w-32 truncate" title={resource.name}>
                    {resource.name}
                  </label>
                  <Input
                    type="number"
                    value={localResources[resource.key] || 0}
                    onChange={(e) => handleResourceChange(resource.key, e.target.value)}
                    onBlur={() => handleResourceBlur(resource.key)}
                    className="h-8 w-20 bg-mir-obsidian border-white/10 text-white text-xs text-center"
                    data-testid={`resource-input-${resource.key}`}
                  />
                </div>
              ))}
            </div>
          </div>

          {/* Bloco: Objetivos Lendários */}
          <div className="bg-mir-charcoal/50 border border-white/5 rounded-lg p-4 shadow-xl">
            <div className="flex items-center gap-2 mb-4">
              <Trophy className="w-5 h-5 text-mir-gold" />
              <h2 className="text-lg font-secondary font-bold text-white" data-testid="objectives-title">
                Objetivos Lendários
              </h2>
            </div>

            {/* Objetivo Mais Próximo */}
            {closest && (
              <div className={`mb-4 p-3 rounded-lg ${closest.bgColor} border ${closest.borderColor}`} data-testid="closest-objective">
                <div className="flex items-center gap-2 mb-2">
                  <closest.icon className={`w-4 h-4 ${closest.color}`} />
                  <span className={`text-sm font-bold ${closest.color}`}>
                    Mais Próximo: {closest.name}
                  </span>
                  <span className="ml-auto text-lg font-bold text-white">
                    {closest.percentage}%
                  </span>
                </div>
                {/* Barra de progresso */}
                <div className="h-2 bg-black/30 rounded-full overflow-hidden mb-2">
                  <div 
                    className={`h-full ${closest.color.replace('text-', 'bg-')} transition-all duration-300`}
                    style={{ width: `${closest.percentage}%` }}
                  />
                </div>
                {/* Itens faltando */}
                <div className="space-y-1">
                  {closest.details.filter(d => d.missing > 0).map(detail => (
                    <div key={detail.key} className="flex justify-between text-xs">
                      <span className="text-slate-300">{detail.name}</span>
                      <span className="text-red-400">
                        Falta: {detail.missing}
                      </span>
                    </div>
                  ))}
                  {closest.details.every(d => d.missing === 0) && (
                    <div className="text-green-400 text-xs font-bold">
                      ✓ Recursos completos!
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* Todos os Objetivos */}
            <div className="space-y-3">
              {Object.entries(LEGENDARY_RECIPES).map(([key, recipe]) => {
                const result = calculateObjectiveProgress(key);
                const Icon = recipe.icon;
                const isClosest = closest?.key === key;
                
                return (
                  <div 
                    key={key} 
                    className={`p-3 rounded-lg border transition-all ${
                      isClosest 
                        ? `${recipe.bgColor} ${recipe.borderColor}` 
                        : 'bg-white/5 border-white/10 hover:border-white/20'
                    }`}
                    data-testid={`objective-${key}`}
                  >
                    <div className="flex items-center gap-2 mb-2">
                      <Icon className={`w-4 h-4 ${recipe.color}`} />
                      <span className={`text-sm font-medium ${isClosest ? recipe.color : 'text-white'}`}>
                        {recipe.name}
                      </span>
                      <span className={`ml-auto text-sm font-bold ${
                        result.percentage === 100 ? 'text-green-400' : 'text-slate-300'
                      }`}>
                        {result.percentage}%
                      </span>
                    </div>
                    {/* Mini barra de progresso */}
                    <div className="h-1.5 bg-black/30 rounded-full overflow-hidden mb-2">
                      <div 
                        className={`h-full ${result.percentage === 100 ? 'bg-green-400' : recipe.color.replace('text-', 'bg-')} transition-all duration-300`}
                        style={{ width: `${result.percentage}%` }}
                      />
                    </div>
                    {/* Detalhes compactos */}
                    <div className="grid grid-cols-3 gap-1 text-[10px]">
                      {result.details.map(detail => (
                        <div key={detail.key} className="flex flex-col">
                          <span className="text-slate-500 truncate" title={detail.name}>
                            {detail.name.split(' ')[0]}
                          </span>
                          <span className={detail.missing > 0 ? 'text-red-400' : 'text-green-400'}>
                            {detail.have}/{detail.required}
                          </span>
                        </div>
                      ))}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
