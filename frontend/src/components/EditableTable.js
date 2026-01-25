import { useState } from "react";
import { Trash2 } from "lucide-react";
import { Button } from "./ui/button";
import { Input } from "./ui/input";

export default function EditableTable({ accounts, bossPrices, onUpdate, onDelete, onRefresh }) {
  const [editingCell, setEditingCell] = useState(null);
  const [tempValue, setTempValue] = useState("");

  const handleCellClick = (accountId, field, currentValue) => {
    setEditingCell({ accountId, field });
    setTempValue(currentValue?.toString() || "");
  };

  const handleCellBlur = async (accountId, field) => {
    if (editingCell) {
      let finalValue = tempValue;

      // Parse based on field type
      if (field === "name" || field === "sala_pico") {
        finalValue = tempValue;
      } else if (field === "gold") {
        finalValue = parseFloat(tempValue) || 0;
      } else if (field.startsWith("bosses.") || field.startsWith("special_bosses.")) {
        finalValue = Math.max(0, parseInt(tempValue) || 0);
      }

      // Update the account
      const [mainField, subField] = field.split(".");
      if (subField) {
        const account = accounts.find(acc => acc.id === accountId);
        const updatedSubField = {
          ...account[mainField],
          [subField]: finalValue
        };
        await onUpdate(accountId, mainField, updatedSubField);
      } else {
        await onUpdate(accountId, field, finalValue);
      }

      await onRefresh();
    }
    setEditingCell(null);
    setTempValue("");
  };

  const handleKeyDown = (e, accountId, field) => {
    if (e.key === "Enter") {
      handleCellBlur(accountId, field);
    } else if (e.key === "Escape") {
      setEditingCell(null);
      setTempValue("");
    }
  };

  const renderCell = (account, field, value) => {
    const isEditing = editingCell?.accountId === account.id && editingCell?.field === field;

    if (isEditing) {
      return (
        <Input
          autoFocus
          value={tempValue}
          onChange={(e) => setTempValue(e.target.value)}
          onBlur={() => handleCellBlur(account.id, field)}
          onKeyDown={(e) => handleKeyDown(e, account.id, field)}
          className="h-8 bg-mir-obsidian border-mir-gold/50 text-white font-mono text-sm px-2"
          type={field === "name" || field === "sala_pico" ? "text" : "number"}
        />
      );
    }

    return (
      <div
        onClick={() => handleCellClick(account.id, field, value)}
        className="cursor-pointer hover:bg-white/10 h-8 flex items-center px-2 rounded transition-colors"
        data-testid={`cell-${field}-${account.id}`}
      >
        {value || value === 0 ? value : "-"}
      </div>
    );
  };

  if (!accounts || accounts.length === 0) {
    return (
      <div className="p-12 text-center">
        <p className="text-slate-400 font-primary text-lg" data-testid="no-accounts-message">
          Nenhuma conta cadastrada. Clique em "Nova Conta" para começar!
        </p>
      </div>
    );
  }

  return (
    <div className="overflow-x-auto">
      <table className="w-full" data-testid="accounts-table">
        <thead className="bg-white/5 sticky top-0">
          <tr>
            <th className="py-3 px-4 text-left text-xs uppercase tracking-wider font-secondary text-slate-400 border-r border-white/5">
              Nome
            </th>
            <th className="py-3 px-3 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              M2
            </th>
            <th className="py-3 px-3 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              G2
            </th>
            <th className="py-3 px-3 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              M4
            </th>
            <th className="py-3 px-3 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              G4
            </th>
            <th className="py-3 px-3 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              M6
            </th>
            <th className="py-3 px-3 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              G6
            </th>
            <th className="py-3 px-3 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              Outro
            </th>
            <th className="py-3 px-4 text-left text-xs uppercase tracking-wider font-secondary text-slate-400 border-l border-white/5">
              Sala Pico
            </th>
            <th className="py-3 px-3 text-center text-xs uppercase tracking-wider font-secondary text-slate-400 border-l border-white/5">
              Xama
            </th>
            <th className="py-3 px-3 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              Praça 4F
            </th>
            <th className="py-3 px-3 text-center text-xs uppercase tracking-wider font-secondary text-slate-400">
              Cracha
            </th>
            <th className="py-3 px-4 text-right text-xs uppercase tracking-wider font-secondary text-slate-400 border-l border-white/5">
              Gold
            </th>
            <th className="py-3 px-4 text-right text-xs uppercase tracking-wider font-secondary text-slate-400">
              USD
            </th>
            <th className="py-3 px-4 text-center text-xs uppercase tracking-wider font-secondary text-slate-400 border-l border-white/5">
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
              <td className="py-2 px-4 font-primary text-white text-sm border-r border-white/5">
                {renderCell(account, "name", account.name)}
              </td>
              <td className="py-2 px-3 text-center font-mono text-sm text-slate-300">
                {renderCell(account, "bosses.medio2", account.bosses.medio2)}
              </td>
              <td className="py-2 px-3 text-center font-mono text-sm text-slate-300">
                {renderCell(account, "bosses.grande2", account.bosses.grande2)}
              </td>
              <td className="py-2 px-3 text-center font-mono text-sm text-slate-300">
                {renderCell(account, "bosses.medio4", account.bosses.medio4)}
              </td>
              <td className="py-2 px-3 text-center font-mono text-sm text-slate-300">
                {renderCell(account, "bosses.grande4", account.bosses.grande4)}
              </td>
              <td className="py-2 px-3 text-center font-mono text-sm text-slate-300">
                {renderCell(account, "bosses.medio6", account.bosses.medio6)}
              </td>
              <td className="py-2 px-3 text-center font-mono text-sm text-slate-300">
                {renderCell(account, "bosses.grande6", account.bosses.grande6)}
              </td>
              <td className="py-2 px-3 text-center font-mono text-sm text-slate-300">
                {renderCell(account, "bosses.outro_pico", account.bosses.outro_pico)}
              </td>
              <td className="py-2 px-4 font-primary text-sm text-mir-gold border-l border-white/5">
                {renderCell(account, "sala_pico", account.sala_pico)}
              </td>
              <td className="py-2 px-3 text-center font-mono text-sm text-slate-300 border-l border-white/5">
                {renderCell(account, "special_bosses.xama", account.special_bosses.xama)}
              </td>
              <td className="py-2 px-3 text-center font-mono text-sm text-slate-300">
                {renderCell(account, "special_bosses.praca_4f", account.special_bosses.praca_4f)}
              </td>
              <td className="py-2 px-3 text-center font-mono text-sm text-slate-300">
                {renderCell(account, "special_bosses.cracha_epica", account.special_bosses.cracha_epica)}
              </td>
              <td className="py-2 px-4 text-right font-mono text-sm text-mir-blue border-l border-white/5">
                {renderCell(account, "gold", account.gold.toLocaleString('pt-BR'))}
              </td>
              <td className="py-2 px-4 text-right font-mono font-bold text-sm text-green-400">
                ${account.total_usd.toFixed(2)}
              </td>
              <td className="py-2 px-4 text-center border-l border-white/5">
                <Button
                  variant="ghost"
                  size="sm"
                  onClick={() => onDelete(account.id)}
                  className="text-mir-red hover:text-red-400 hover:bg-white/5"
                  data-testid={`delete-account-btn-${index}`}
                >
                  <Trash2 className="w-4 h-4" />
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
