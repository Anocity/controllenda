# MIR4 Account Manager

Sistema de gerenciamento de contas do jogo MIR4 com cálculo automático de valores em USD.

## 🎮 Funcionalidades

- **Tabela Editável Inline**: Clique em qualquer célula para editar diretamente
- **Gerenciamento de Bosses**: Acompanhe M2, G2, M4, G4, M6, G6, M7, G7, M8, G8
- **Bosses Especiais**: Xama, Praça 4F, Cracha Épica
- **Cálculo Automático de USD**: Configure preços e veja totais em tempo real
- **Sistema de Cores**:
  - 🟢 Verde: Números de bosses > 0
  - ⚪ Branco: Nome e Sala Pico
  - 🔵 Azul: Gold
  - ⚫ Vazio: Valores = 0
- **Totais Automáticos**: Soma total de cada tipo de boss e valores USD individuais

## 🚀 Tecnologias

### Backend
- **FastAPI**: Framework web Python
- **MongoDB**: Banco de dados NoSQL
- **Motor**: Driver assíncrono MongoDB
- **Pydantic**: Validação de dados

### Frontend
- **React**: Biblioteca JavaScript
- **Tailwind CSS**: Framework de estilização
- **Shadcn UI**: Componentes de interface
- **Axios**: Cliente HTTP
- **React Router**: Roteamento
- **Sonner**: Notificações toast

## 📦 Instalação

### Requisitos
- Python 3.11+
- Node.js 18+
- MongoDB

### Backend

```bash
cd backend
pip install -r requirements.txt
```

Configure o arquivo `.env`:
```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=mir4_manager
CORS_ORIGINS=http://localhost:3000
```

Execute o servidor:
```bash
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

### Frontend

```bash
cd frontend
yarn install
```

Configure o arquivo `.env`:
```env
REACT_APP_BACKEND_URL=http://localhost:8001
```

Execute o app:
```bash
yarn start
```

Acesse: `http://localhost:3000`

## 🎯 Como Usar

1. **Adicionar Conta**: Clique em "Nova Conta" no topo
2. **Editar Valores**: Clique em qualquer célula para editar
3. **Salvar**: Pressione Enter ou clique fora da célula
4. **Configurar Preços**: Botão "Preços USD" para definir valores por tipo de boss
5. **Deletar Conta**: Clique no ícone de lixeira

## 📊 Estrutura de Dados

### Conta (Account)
```json
{
  "name": "Nome da Conta",
  "bosses": {
    "medio2": 0,
    "grande2": 0,
    "medio4": 0,
    "grande4": 0,
    "medio6": 0,
    "grande6": 0,
    "medio7": 0,
    "grande7": 0,
    "medio8": 0,
    "grande8": 0
  },
  "sala_pico": "Pico 7F",
  "special_bosses": {
    "xama": 0,
    "praca_4f": 0,
    "cracha_epica": 0
  },
  "gold": 0
}
```

### Preços (Boss Prices)
```json
{
  "medio2_price": 0.045,
  "grande2_price": 0.09,
  "medio4_price": 0.14,
  "grande4_price": 0.18,
  "medio6_price": 0.36,
  "grande6_price": 0.45,
  "medio7_price": 0,
  "grande7_price": 0,
  "medio8_price": 0,
  "grande8_price": 0,
  "xama_price": 0,
  "praca_4f_price": 0,
  "cracha_epica_price": 0
}
```

## 🌐 Deploy

### Backend (Railway/Render/Heroku)
1. Configure as variáveis de ambiente
2. Use Dockerfile ou buildpack Python
3. Conecte ao MongoDB Atlas

### Frontend (Vercel/Netlify)
1. Build: `yarn build`
2. Configure `REACT_APP_BACKEND_URL` com URL do backend em produção
3. Deploy da pasta `build`

## 📝 API Endpoints

### Contas
- `GET /api/accounts` - Listar todas as contas
- `POST /api/accounts` - Criar nova conta
- `GET /api/accounts/{id}` - Buscar conta específica
- `PUT /api/accounts/{id}` - Atualizar conta
- `DELETE /api/accounts/{id}` - Deletar conta

### Preços
- `GET /api/boss-prices` - Obter preços dos bosses
- `PUT /api/boss-prices` - Atualizar preços

### Estatísticas
- `GET /api/statistics` - Obter totais e estatísticas

## 🎨 Customização

### Cores (tailwind.config.js)
```javascript
colors: {
  'mir-black': '#050505',
  'mir-obsidian': '#0A0A0A',
  'mir-charcoal': '#121212',
  'mir-gold': '#FFD700',
  'mir-red': '#FF3B30',
  'mir-blue': '#007AFF'
}
```

## 📄 Licença

MIT License - Sinta-se livre para usar e modificar.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

Feito com ❤️ para a comunidade MIR4
