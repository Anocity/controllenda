# Estrutura do Projeto

```
mir4-account-manager/
├── backend/
│   ├── server.py              # API FastAPI principal
│   ├── requirements.txt       # Dependências Python
│   ├── Dockerfile            # Container Docker
│   ├── .env                  # Variáveis de ambiente (não commitar)
│   └── .env.example          # Exemplo de configuração
│
├── frontend/
│   ├── public/               # Arquivos estáticos
│   ├── src/
│   │   ├── components/
│   │   │   ├── ui/          # Componentes Shadcn UI
│   │   │   ├── EditableTable.js      # Tabela editável principal
│   │   │   └── BossPriceDialog.js    # Modal de configuração de preços
│   │   ├── pages/
│   │   │   └── Dashboard.js          # Página principal
│   │   ├── hooks/
│   │   │   └── use-toast.js          # Hook para notificações
│   │   ├── lib/
│   │   │   └── utils.js              # Utilidades
│   │   ├── App.js            # Componente raiz
│   │   ├── App.css           # Estilos do App
│   │   ├── index.js          # Entry point
│   │   └── index.css         # Estilos globais + Tailwind
│   ├── package.json          # Dependências Node.js
│   ├── tailwind.config.js    # Configuração Tailwind
│   ├── postcss.config.js     # Configuração PostCSS
│   ├── .env                  # Variáveis de ambiente (não commitar)
│   └── .env.example          # Exemplo de configuração
│
├── .gitignore               # Arquivos ignorados pelo Git
├── README.md                # Documentação principal
└── DEPLOY.md                # Guia de deploy

## Arquivos Principais

### Backend
- **server.py**: API REST com endpoints para contas, preços e estatísticas
- **requirements.txt**: FastAPI, Motor, Pydantic, etc.

### Frontend
- **Dashboard.js**: Componente principal com gerenciamento de estado
- **EditableTable.js**: Tabela com edição inline e cálculos
- **BossPriceDialog.js**: Modal para configurar preços USD

## Componentes Utilizados

### UI Components (Shadcn)
- Button
- Input
- Label
- Dialog
- Sonner (Toast)

## Fluxo de Dados

1. **Frontend** faz requisição HTTP → **Backend API**
2. **Backend** valida dados com Pydantic → **MongoDB**
3. **MongoDB** retorna dados → **Backend** calcula USD
4. **Backend** envia JSON → **Frontend** atualiza UI

## Tecnologias por Camada

### Backend
- FastAPI (Framework web)
- Motor (MongoDB async driver)
- Pydantic (Validação)
- Python 3.11+

### Frontend
- React 18
- Tailwind CSS
- Shadcn UI
- Axios
- React Router
- Sonner

### Database
- MongoDB (NoSQL)
- Collections: accounts, boss_prices
