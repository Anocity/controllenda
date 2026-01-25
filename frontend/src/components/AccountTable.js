import { Edit2, Trash2 } from "lucide-react";
import { Button } from "./ui/button";

export default function AccountTable({ accounts, bossPrices, onEdit, onDelete }) {
  if (!accounts || accounts.length === 0) {
    return (
      <div className="p-12 text-center">
        <p className="text-slate-400 font-primary text-lg" data-testid="no-accounts-message">
          Nenhuma conta cadastrada. Adicione sua primeira conta!
        </p>
      </div>
    );
  }

  return (
    <div className="overflow-x-auto">
      <table className="w-full" data-testid="accounts-table">
        <thead className="bg-white/5">
          <tr>
            <th className="py-4 px-6 text-left text-xs uppercase tracking-wider font-secondary text-slate-400">
              Nome
            </th>
            <th className="py-4 px-4 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              M2
            </th>
            <th className="py-4 px-4 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              G2
            </th>
            <th className="py-4 px-4 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              M4
            </th>
            <th className="py-4 px-4 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              G4
            </th>
            <th className="py-4 px-4 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              M6
            </th>
            <th className="py-4 px-4 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              G6
            </th>
            <th className="py-4 px-4 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              Outro
            </th>
            <th className="py-4 px-6 text-left text-xs uppercase tracking-wider font-secondary text-slate-400">
              Sala Pico
            </th>
            <th className="py-4 px-4 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              Xama
            </th>
            <th className="py-4 px-4 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              Praça 4F
            </th>
            <th className="py-4 px-4 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              Cracha
            </th>
            <th className="py-4 px-6 text-right text-xs uppercase tracking-wider font-secondary text-slate-400">
              Gold
            </th>
            <th className="py-4 px-6 text-right text-xs uppercase tracking-wider font-secondary text-slate-400">
              USD
            </th>
            <th className="py-4 px-6 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              Ações
            </th>
          </tr>
        </thead>
        <tbody>
          {accounts.map((account, index) => (
            <tr
              key={account.id}
              className="border-b border-white/5 hover:bg-white/5 transition-colors"
              data-testid={`account-row-${index}`}
            >
              <td className="py-4 px-6 font-primary font-medium text-white" data-testid={`account-name-${index}`}>
                {account.name}
              </td>
              <td className="py-4 px-4 text-center font-mono text-sm text-slate-300" data-testid={`account-medio2-${index}`}>
                {account.bosses.medio2}
              </td>
              <td className="py-4 px-4 text-center font-mono text-sm text-slate-300" data-testid={`account-grande2-${index}`}>
                {account.bosses.grande2}
              </td>
              <td className="py-4 px-4 text-center font-mono text-sm text-slate-300" data-testid={`account-medio4-${index}`}>
                {account.bosses.medio4}
              </td>
              <td className="py-4 px-4 text-center font-mono text-sm text-slate-300" data-testid={`account-grande4-${index}`}>
                {account.bosses.grande4}
              </td>
              <td className="py-4 px-4 text-center font-mono text-sm text-slate-300" data-testid={`account-medio6-${index}`}>
                {account.bosses.medio6}
              </td>
              <td className="py-4 px-4 text-center font-mono text-sm text-slate-300" data-testid={`account-grande6-${index}`}>
                {account.bosses.grande6}
              </td>
              <td className="py-4 px-4 text-center font-mono text-sm text-slate-300" data-testid={`account-outro-${index}`}>
                {account.bosses.outro_pico}
              </td>
              <td className="py-4 px-6 font-primary text-sm text-mir-gold" data-testid={`account-sala-${index}`}>
                {account.sala_pico || "-"}
              </td>
              <td className="py-4 px-4 text-center font-mono text-sm text-slate-300" data-testid={`account-xama-${index}`}>
                {account.special_bosses.xama}
              </td>
              <td className="py-4 px-4 text-center font-mono text-sm text-slate-300" data-testid={`account-praca-${index}`}>
                {account.special_bosses.praca_4f}
              </td>
              <td className="py-4 px-4 text-center font-mono text-sm text-slate-300" data-testid={`account-cracha-${index}`}>
                {account.special_bosses.cracha_epica}
              </td>
              <td className="py-4 px-6 text-right font-mono text-sm text-mir-blue" data-testid={`account-gold-${index}`}>
                {account.gold.toLocaleString('pt-BR')}
              </td>
              <td className="py-4 px-6 text-right font-mono font-bold text-sm text-green-400" data-testid={`account-usd-${index}`}>
                ${account.total_usd.toFixed(2)}
              </td>
              <td className="py-4 px-6">
                <div className="flex items-center justify-center gap-2">
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => onEdit(account)}
                    className="text-mir-gold hover:text-amber-400 hover:bg-white/5"
                    data-testid={`edit-account-btn-${index}`}
                  >
                    <Edit2 className="w-4 h-4" />
                  </Button>
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => onDelete(account.id)}
                    className="text-mir-red hover:text-red-400 hover:bg-white/5"
                    data-testid={`delete-account-btn-${index}`}
                  >
                    <Trash2 className="w-4 h-4" />
                  </Button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
