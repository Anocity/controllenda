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

export default function BossPriceDialog({ open, onOpenChange, bossPrices, onSave }) {
  const [formData, setFormData] = useState({
    medio2_price: 0,
    grande2_price: 0,
    medio4_price: 0,
    grande4_price: 0,
    medio6_price: 0,
    grande6_price: 0,
    medio7_price: 0,
    grande7_price: 0,
    medio8_price: 0,
    grande8_price: 0,
    medio9_price: 0,
    grande9_price: 0,
    medio10_price: 0,
    grande10_price: 0,
    xama_price: 0,
    praca_4f_price: 0,
    cracha_epica_price: 0
  });

  useEffect(() => {
    if (bossPrices) {
      setFormData({
        medio2_price: bossPrices.medio2_price,
        grande2_price: bossPrices.grande2_price,
        medio4_price: bossPrices.medio4_price,
        grande4_price: bossPrices.grande4_price,
        medio6_price: bossPrices.medio6_price,
        grande6_price: bossPrices.grande6_price,
        medio7_price: bossPrices.medio7_price || 0,
        grande7_price: bossPrices.grande7_price || 0,
        medio8_price: bossPrices.medio8_price || 0,
        grande8_price: bossPrices.grande8_price || 0,
        medio9_price: bossPrices.medio9_price || 0,
        grande9_price: bossPrices.grande9_price || 0,
        medio10_price: bossPrices.medio10_price || 0,
        grande10_price: bossPrices.grande10_price || 0,
        xama_price: bossPrices.xama_price,
        praca_4f_price: bossPrices.praca_4f_price,
        cracha_epica_price: bossPrices.cracha_epica_price
      });
    }
  }, [bossPrices, open]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSave(formData);
  };

  const handlePriceChange = (priceType, value) => {
    const numValue = parseFloat(value) || 0;
    setFormData({
      ...formData,
      [priceType]: Math.max(0, numValue)
    });
  };

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="bg-mir-charcoal border-white/10 text-white max-w-2xl" data-testid="boss-price-dialog">
        <DialogHeader>
          <DialogTitle className="text-2xl font-secondary text-mir-gold uppercase tracking-wide" data-testid="price-dialog-title">
            Configurar Preços USD
          </DialogTitle>
          <DialogDescription className="text-slate-400">
            Configure o valor em USD de cada tipo de boss
          </DialogDescription>
        </DialogHeader>
        
        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Boss de Pico */}
          <div>
            <Label className="text-mir-gold font-secondary uppercase text-sm mb-3 block">
              Boss de Pico
            </Label>
            <div className="grid grid-cols-2 gap-4">
              <div>
                <Label htmlFor="medio2_price" className="text-xs text-slate-400">Médio 2 (USD)</Label>
                <Input
                  id="medio2_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.medio2_price}
                  onChange={(e) => handlePriceChange('medio2_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-medio2-price"
                />
              </div>
              <div>
                <Label htmlFor="grande2_price" className="text-xs text-slate-400">Grande 2 (USD)</Label>
                <Input
                  id="grande2_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.grande2_price}
                  onChange={(e) => handlePriceChange('grande2_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-grande2-price"
                />
              </div>
              <div>
                <Label htmlFor="medio4_price" className="text-xs text-slate-400">Médio 4 (USD)</Label>
                <Input
                  id="medio4_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.medio4_price}
                  onChange={(e) => handlePriceChange('medio4_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-medio4-price"
                />
              </div>
              <div>
                <Label htmlFor="grande4_price" className="text-xs text-slate-400">Grande 4 (USD)</Label>
                <Input
                  id="grande4_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.grande4_price}
                  onChange={(e) => handlePriceChange('grande4_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-grande4-price"
                />
              </div>
              <div>
                <Label htmlFor="medio6_price" className="text-xs text-slate-400">Médio 6 (USD)</Label>
                <Input
                  id="medio6_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.medio6_price}
                  onChange={(e) => handlePriceChange('medio6_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-medio6-price"
                />
              </div>
              <div>
                <Label htmlFor="grande6_price" className="text-xs text-slate-400">Grande 6 (USD)</Label>
                <Input
                  id="grande6_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.grande6_price}
                  onChange={(e) => handlePriceChange('grande6_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-grande6-price"
                />
              </div>
              <div>
                <Label htmlFor="medio7_price" className="text-xs text-slate-400">Médio 7 (USD)</Label>
                <Input
                  id="medio7_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.medio7_price}
                  onChange={(e) => handlePriceChange('medio7_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-medio7-price"
                />
              </div>
              <div>
                <Label htmlFor="grande7_price" className="text-xs text-slate-400">Grande 7 (USD)</Label>
                <Input
                  id="grande7_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.grande7_price}
                  onChange={(e) => handlePriceChange('grande7_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-grande7-price"
                />
              </div>
              <div>
                <Label htmlFor="medio8_price" className="text-xs text-slate-400">Médio 8 (USD)</Label>
                <Input
                  id="medio8_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.medio8_price}
                  onChange={(e) => handlePriceChange('medio8_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-medio8-price"
                />
              </div>
              <div>
                <Label htmlFor="grande8_price" className="text-xs text-slate-400">Grande 8 (USD)</Label>
                <Input
                  id="grande8_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.grande8_price}
                  onChange={(e) => handlePriceChange('grande8_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-grande8-price"
                />
              </div>
              <div>
                <Label htmlFor="medio9_price" className="text-xs text-slate-400">Médio 9 (USD)</Label>
                <Input
                  id="medio9_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.medio9_price}
                  onChange={(e) => handlePriceChange('medio9_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-medio9-price"
                />
              </div>
              <div>
                <Label htmlFor="grande9_price" className="text-xs text-slate-400">Grande 9 (USD)</Label>
                <Input
                  id="grande9_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.grande9_price}
                  onChange={(e) => handlePriceChange('grande9_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-grande9-price"
                />
              </div>
              <div>
                <Label htmlFor="medio10_price" className="text-xs text-slate-400">Médio 10 (USD)</Label>
                <Input
                  id="medio10_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.medio10_price}
                  onChange={(e) => handlePriceChange('medio10_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-medio10-price"
                />
              </div>
              <div>
                <Label htmlFor="grande10_price" className="text-xs text-slate-400">Grande 10 (USD)</Label>
                <Input
                  id="grande10_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.grande10_price}
                  onChange={(e) => handlePriceChange('grande10_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-grande10-price"
                />
              </div>
            </div>
          </div>

          {/* Bosses Especiais */}
          <div>
            <Label className="text-mir-gold font-secondary uppercase text-sm mb-3 block">
              Bosses Especiais
            </Label>
            <div className="grid grid-cols-3 gap-4">
              <div>
                <Label htmlFor="xama_price" className="text-xs text-slate-400">Xama (USD)</Label>
                <Input
                  id="xama_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.xama_price}
                  onChange={(e) => handlePriceChange('xama_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-xama-price"
                />
              </div>
              <div>
                <Label htmlFor="praca_4f_price" className="text-xs text-slate-400">Praça 4F (USD)</Label>
                <Input
                  id="praca_4f_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.praca_4f_price}
                  onChange={(e) => handlePriceChange('praca_4f_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-praca-4f-price"
                />
              </div>
              <div>
                <Label htmlFor="cracha_epica_price" className="text-xs text-slate-400">Cracha Épica (USD)</Label>
                <Input
                  id="cracha_epica_price"
                  type="number"
                  min="0"
                  step="0.001"
                  value={formData.cracha_epica_price}
                  onChange={(e) => handlePriceChange('cracha_epica_price', e.target.value)}
                  className="bg-black/50 border-white/10 text-white mt-1"
                  data-testid="input-cracha-epica-price"
                />
              </div>
            </div>
          </div>

          <DialogFooter>
            <Button
              type="button"
              variant="outline"
              onClick={() => onOpenChange(false)}
              className="bg-white/5 text-white border-white/10 hover:bg-white/10"
              data-testid="cancel-price-btn"
            >
              Cancelar
            </Button>
            <Button
              type="submit"
              className="bg-mir-gold text-black font-bold hover:bg-amber-400"
              data-testid="save-price-btn"
            >
              Salvar Preços
            </Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
}
