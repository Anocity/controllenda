# 📋 Changelog - Versão 2.0

## 🎉 Versão 2.0 - Layout Compacto + Sistema de Confirmação

### ✨ Novas Funcionalidades

#### 1. Layout Compacto
- **Tamanho**: 1200x800px (aproximadamente 1/4 de um monitor Full HD)
- **Design**: Otimizado para ocupar menos espaço
- **Fontes**: Reduzidas para melhor aproveitamento
- **Espaçamento**: Compactado mantendo legibilidade

#### 2. Numeração de Contas
- Coluna `#` adicionada na primeira posição
- Numeração sequencial automática (1, 2, 3, ...)
- Facilita organização e referência visual

#### 3. Campos Numéricos Sem Spinners
- Setas de incremento/decremento removidas
- Interface mais limpa
- Apenas digitação manual permitida
- CSS customizado: `.no-spinner`

#### 4. Sistema de Confirmação Automática
**Funcionalidade Principal:**
- Botão de confirmação por conta (⭕ → ✅)
- Status salvo no banco de dados
- Data de confirmação registrada
- Reset automático após 30 dias

**Como funciona:**
1. Usuário clica no botão ⭕
2. Conta é marcada como "confirmada" (✅)
3. Data atual é salva
4. Linha fica verde (indicador visual)
5. Após 30 dias, sistema reseta automaticamente:
   - Todos os bosses voltam para 0
   - Gold volta para 0
   - Status volta para não confirmado

**Lógica de Reset:**
- Executa automaticamente ao listar contas
- Verifica data de confirmação
- Compara com data atual
- Reseta se passaram 30+ dias

#### 5. Backend Completo
- FastAPI + Motor (MongoDB async)
- Endpoint `/api/accounts/{id}/confirm`
- Lógica de verificação e reset automático
- Validações Pydantic
- CORS configurável

### 🔧 Melhorias Técnicas

#### Backend:
- Novo campo `confirmed: bool`
- Novo campo `confirmed_at: datetime`
- Função `check_and_reset_accounts()`
- Endpoint POST `/accounts/{id}/confirm`

#### Frontend:
- Coluna de confirmação na tabela
- Ícones visuais (Circle/CheckCircle2)
- Background verde para contas confirmadas
- Toast notifications

#### CSS:
```css
.no-spinner::-webkit-outer-spin-button,
.no-spinner::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
```

### 📦 Estrutura de Dados

**Account Model:**
```json
{
  "id": "uuid",
  "name": "string",
  "bosses": {
    "medio2": 0,
    "grande2": 0,
    // ... até grande8
  },
  "sala_pico": "string",
  "special_bosses": {
    "xama": 0,
    "praca_4f": 0,
    "cracha_epica": 0
  },
  "gold": 0,
  "confirmed": false,
  "confirmed_at": null,
  "created_at": "2025-01-27T..."
}
```

### 🎨 Design

**Cores:**
- Confirmado: Verde (#10b981)
- Não confirmado: Transparente
- Hover: Branco 10% opacidade
- Números > 0: Verde claro
- Números = 0: Invisível

**Tamanhos:**
- Header: 2xl (24px)
- Texto tabela: xs (12px)
- Labels: [10px]
- Padding: Reduzido (py-1, py-2)

### 📊 Comparação com Versão 1.0

| Funcionalidade | v1.0 | v2.0 |
|----------------|------|------|
| Layout | Expansivo | Compacto (1200px) |
| Numeração | ❌ | ✅ |
| Confirmação | ❌ | ✅ |
| Reset Automático | ❌ | ✅ |
| Spinners | ✅ | ❌ |
| Backend | localStorage | MongoDB |
| Tamanho Fonte | 14px | 10-12px |

### 🚀 Melhorias Futuras (Sugestões)

- [ ] Notificação antes do reset (avisar 3 dias antes)
- [ ] Histórico de confirmações
- [ ] Exportar dados para Excel
- [ ] Dashboard com gráficos
- [ ] Filtros e busca
- [ ] Ordenação por coluna
- [ ] Backup automático

---

## 📝 Notas de Upgrade

**De v1.0 para v2.0:**

1. Backend agora é obrigatório (MongoDB)
2. Dados do localStorage NÃO migram automaticamente
3. Novo campo `confirmed` em todas as contas
4. Layout é mais compacto (pode precisar ajustar monitores pequenos)

**Breaking Changes:**
- localStorage não é mais suportado
- Necessário MongoDB configurado
- Variáveis de ambiente obrigatórias

---

## 🐛 Bug Fixes

- Corrigido: Nova conta não funcionava sem backend
- Corrigido: Spinners apareciam em campos number
- Corrigido: Layout não era responsivo em telas pequenas
- Corrigido: Totais USD não atualizavam após edição

---

## 👨‍💻 Créditos

Desenvolvido para gerenciamento pessoal de contas MIR4.

Versão 2.0 - Janeiro 2025
