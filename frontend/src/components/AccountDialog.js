import { useState, useEffect } from "react";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
  DialogDescription
} from "./ui/dialog";
import { Button } from "./ui/button";
import { Input } from "./ui/input";
import { Label } from "./ui/label";

export default function AccountDialog({ open, onOpenChange, account, onSave }) {
  const [formData, setFormData] = useState({
    name: "",
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
  });

  useEffect(() => {
    if (account) {
      setFormData({
        name: account.name,
        bosses: { ...account.bosses },
        sala_pico: account.sala_pico || "",
        special_bosses: { ...account.special_bosses },
        gold: account.gold
      });
    } else {
      setFormData({
        name: "",
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
      });
    }
  }, [account, open]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSave(formData);
  };

  const handleBossChange = (bossType, value) => {
    setFormData({
      ...formData,
      bosses: {
        ...formData.bosses,
        [bossType]: parseInt(value) || 0
      }
    });
  };

  const handleSpecialChange = (specialType, value) => {
    setFormData({
      ...formData,
      special_bosses: {
        ...formData.special_bosses,
        [specialType]: parseInt(value) || 0
      }
    });
  };

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="bg-mir-charcoal border-white/10 text-white max-w-3xl max-h-[90vh] overflow-y-auto" data-testid="account-dialog">
        <DialogHeader>
          <DialogTitle className="text-2xl font-secondary text-mir-gold uppercase tracking-wide" data-testid="dialog-title">
            {account ? "Editar Conta" : "Nova Conta"}
          </DialogTitle>
          <DialogDescription className="text-slate-400">
            Preencha os dados da conta e quantidades de bosses
          </DialogDescription>
        </DialogHeader>
        
        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Nome */}
          <div>
            <Label htmlFor="name" className="text-slate-300 font-secondary uppercase text-sm">
              Nome da Conta
            </Label>
            <Input
              id="name"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              className="bg-black/50 border-white/10 focus:border-mir-gold/50 focus:ring-1 focus:ring-mir-gold/50 text-white mt-2"
              required
              data-testid="input-account-name"
            />
          </div>

          {/* Boss de Pico */}
          <div>
            <Label className="text-mir-gold font-secondary uppercase text-sm mb-3 block">
              Boss de Pico
            </Label>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
              <div>
                <Label htmlFor="medio2" className="text-xs text-slate-400">Médio 2</Label>
                <Input
                  id="medio2"
                  type="number"
                  min="0"
                  value={formData.bosses.medio2}
                  onChange={(e) => handleBossChange('medio2', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-medio2"
                />
              </div>
              <div>
                <Label htmlFor="grande2" className="text-xs text-slate-400">Grande 2</Label>
                <Input
                  id="grande2"
                  type="number"
                  min="0"
                  value={formData.bosses.grande2}
                  onChange={(e) => handleBossChange('grande2', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-grande2"
                />
              </div>
              <div>
                <Label htmlFor="medio4" className="text-xs text-slate-400">Médio 4</Label>
                <Input
                  id="medio4"
                  type="number"
                  min="0"
                  value={formData.bosses.medio4}
                  onChange={(e) => handleBossChange('medio4', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-medio4"
                />
              </div>
              <div>
                <Label htmlFor="grande4" className="text-xs text-slate-400">Grande 4</Label>
                <Input
                  id="grande4"
                  type="number"
                  min="0"
                  value={formData.bosses.grande4}
                  onChange={(e) => handleBossChange('grande4', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-grande4"
                />
              </div>
              <div>
                <Label htmlFor="medio6" className="text-xs text-slate-400">Médio 6</Label>
                <Input
                  id="medio6"
                  type="number"
                  min="0"
                  value={formData.bosses.medio6}
                  onChange={(e) => handleBossChange('medio6', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-medio6"
                />
              </div>
              <div>
                <Label htmlFor="grande6" className="text-xs text-slate-400">Grande 6</Label>
                <Input
                  id="grande6"
                  type="number"
                  min="0"
                  value={formData.bosses.grande6}
                  onChange={(e) => handleBossChange('grande6', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-grande6"
                />
              </div>
              <div>
                <Label htmlFor="outro_pico" className="text-xs text-slate-400">Outro Pico</Label>
                <Input
                  id="outro_pico"
                  type="number"
                  min="0"
                  value={formData.bosses.outro_pico}
                  onChange={(e) => handleBossChange('outro_pico', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-outro-pico"
                />
              </div>
            </div>
          </div>

          {/* Sala de Pico */}
          <div>
            <Label htmlFor="sala_pico" className="text-slate-300 font-secondary uppercase text-sm">
              Sala de Pico
            </Label>
            <Input
              id="sala_pico"
              value={formData.sala_pico}
              onChange={(e) => setFormData({ ...formData, sala_pico: e.target.value })}
              className="bg-black/50 border-white/10 text-white mt-2"
              placeholder="Ex: Pico 2F"
              data-testid="input-sala-pico"
            />
          </div>

          {/* Bosses Especiais */}
          <div>
            <Label className="text-mir-gold font-secondary uppercase text-sm mb-3 block">
              Bosses Especiais
            </Label>
            <div className="grid grid-cols-3 gap-4">
              <div>
                <Label htmlFor="xama" className="text-xs text-slate-400">Xama</Label>
                <Input
                  id="xama"
                  type="number"
                  min="0"
                  value={formData.special_bosses.xama}
                  onChange={(e) => handleSpecialChange('xama', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-xama"
                />
              </div>
              <div>
                <Label htmlFor="praca_4f" className="text-xs text-slate-400">Praça 4F</Label>
                <Input
                  id="praca_4f"
                  type="number"
                  min="0"
                  value={formData.special_bosses.praca_4f}
                  onChange={(e) => handleSpecialChange('praca_4f', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-praca-4f"
                />
              </div>
              <div>
                <Label htmlFor="cracha_epica" className="text-xs text-slate-400">Cracha Épica</Label>
                <Input
                  id="cracha_epica"
                  type="number"
                  min="0"
                  value={formData.special_bosses.cracha_epica}
                  onChange={(e) => handleSpecialChange('cracha_epica', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-cracha-epica"
                />
              </div>
            </div>
          </div>

          {/* Gold */}
          <div>
            <Label htmlFor="gold" className="text-slate-300 font-secondary uppercase text-sm">
              Gold
            </Label>
            <Input
              id="gold"
              type="number"
              min="0"
              step="0.01"
              value={formData.gold}
              onChange={(e) => setFormData({ ...formData, gold: parseFloat(e.target.value) || 0 })}
              className="bg-black/50 border-white/10 text-white mt-2"
              data-testid="input-gold"
            />
          </div>

          <DialogFooter>
            <Button
              type="button"
              variant="outline"
              onClick={() => onOpenChange(false)}
              className="bg-white/5 text-white border-white/10 hover:bg-white/10"
              data-testid="cancel-btn"
            >
              Cancelar
            </Button>
            <Button
              type="submit"
              className="bg-mir-gold text-black font-bold hover:bg-amber-400"
              data-testid="save-account-btn"
            >
              Salvar
            </Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
}
