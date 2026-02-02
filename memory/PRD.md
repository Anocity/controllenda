# MIR4 Account Manager - PRD

## Problema Original
O usuário quer criar um aplicativo web para rastrear suas contas do jogo MIR4.

### Requisitos Principais
1. **Listagem de Contas**: Listar todas as contas MIR4
2. **Rastreamento por Conta**:
   - Quantidade de bosses mortos (vários tipos: M2-G8)
   - Quantidade de gold
   - Sala de Pico que a conta entra
   - Bosses especiais (Xama, Praça 4F, Cracha Épica)
3. **Layout Compacto**: Tamanho fixo de ~1200px, centralizado
4. **Numeração Sequencial**: Coluna de numeração nas contas
5. **Inputs sem Spinners**: Ocultar setas up/down dos inputs numéricos
6. **Sistema de Confirmação e Reset Automático**:
   - Botão de confirmação por conta
   - Reset automático dos contadores após 30 dias da confirmação
7. **Objetivos Lendários** (Novo):
   - Página de recursos por conta
   - Cálculo automático de qual item lendário está mais perto
   - Mostra exatamente o que falta para cada objetivo

## Arquitetura Técnica

### Stack
- **Frontend**: React + Tailwind CSS + Shadcn/UI
- **Backend**: FastAPI + Motor (async MongoDB driver)
- **Database**: MongoDB
- **Scheduler**: APScheduler (reset automático)

### Estrutura de Arquivos
```
/app/
├── backend/
│   ├── server.py          # API FastAPI + scheduler
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Dashboard.js        # Página principal
│   │   │   └── AccountResources.js # Objetivos Lendários
│   │   ├── components/
│   │   │   ├── EditableTable.js    # Tabela editável inline
│   │   │   └── BossPriceDialog.js  # Dialog de preços
│   │   └── index.css               # CSS global
│   └── .env
└── memory/
    └── PRD.md
```

### Schema MongoDB - Collection `accounts`
```json
{
  "id": "uuid",
  "name": "string",
  "bosses": {
    "medio2": 0, "grande2": 0, "medio4": 0, "grande4": 0,
    "medio6": 0, "grande6": 0, "medio7": 0, "grande7": 0,
    "medio8": 0, "grande8": 0
  },
  "special_bosses": {
    "xama": 0, "praca_4f": 0, "cracha_epica": 0
  },
  "legendary_resources": {
    "aco_lendario": 0,
    "esfera_lendaria": 0,
    "lunar_lendario": 0,
    "quintessencia_lendaria": 0,
    "bugiganga_lendaria": 0,
    "platina_lendaria": 0,
    "iluminado_lendario": 0,
    "anima_lendaria": 0
  },
  "sala_pico": "string",
  "gold": 0,
  "confirmed": false,
  "confirmed_at": "datetime|null",
  "created_at": "datetime"
}
```

### Receitas dos Objetivos Lendários
| Objetivo | Ingrediente 1 | Ingrediente 2 | Ingrediente 3 |
|----------|---------------|---------------|---------------|
| Arma Lendária | 300 Aço L | 100 Esfera L | 100 Lunar L |
| Torso Lendário | 300 Aço L | 100 Quintessência L | 100 Bugiganga L |
| Colar Lendário | 300 Platina L | 100 Iluminado L | 100 Anima L |

**Cálculo de Progresso**: Por gargalo (mínimo dos 3 ingredientes)

### API Endpoints
- `GET /api/accounts` - Lista todas as contas
- `POST /api/accounts` - Cria nova conta
- `PUT /api/accounts/{id}` - Atualiza conta (incluindo legendary_resources)
- `DELETE /api/accounts/{id}` - Deleta conta
- `POST /api/accounts/{id}/confirm` - Confirma conta
- `GET /api/boss-prices` - Obtém preços USD
- `PUT /api/boss-prices` - Atualiza preços USD
- `GET /api/scheduler-status` - Status do scheduler

## Funcionalidades Implementadas

### ✅ Concluído (Janeiro 2026)
- [x] CRUD completo de contas
- [x] Edição inline tipo Excel
- [x] Numeração sequencial
- [x] Cálculo de totais (quantidade e USD)
- [x] Layout compacto 1200px centralizado
- [x] Inputs sem spinners (CSS global)
- [x] Sistema de confirmação com data
- [x] Reset automático após 30 dias (APScheduler - executa a cada 6h)
- [x] Dialog de configuração de preços USD
- [x] Persistência em MongoDB
- [x] **Página de Recursos Lendários** (/account/:id/resources)
- [x] **Cálculo de Objetivos Lendários** (Arma, Torso, Colar)
- [x] **Identificação do objetivo mais próximo**
- [x] **Exibição de itens faltando**

## Backlog Futuro

### P1 - Melhorias Potenciais
- [ ] Filtro/busca por nome de conta
- [ ] Exportar dados para Excel/CSV
- [ ] Histórico de resets
- [ ] Notificação antes do reset (ex: 5 dias antes)

### P2 - Nice to Have
- [ ] Autenticação de usuário
- [ ] Múltiplos usuários com contas separadas
- [ ] Tema claro/escuro
- [ ] Versão mobile responsiva
