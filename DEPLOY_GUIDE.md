# 🚀 Guia de Deploy - Railway + Vercel

## Arquitetura

```
Frontend (Vercel) → Backend (Railway) → MongoDB Atlas
```

---

## 1️⃣ MongoDB Atlas (5 minutos)

### Criar Cluster:
1. https://mongodb.com/cloud/atlas/register
2. Create Free Cluster (M0)
3. Região: São Paulo (sa-east-1)

### Configurar Acesso:
1. Network Access → Add IP → `0.0.0.0/0`
2. Database Access → Add User
   - Username: `mir4admin`
   - Password: (anote!)

### Connection String:
```
mongodb+srv://mir4admin:SENHA@cluster.mongodb.net/?retryWrites=true&w=majority
```

---

## 2️⃣ Backend no Railway (5 minutos)

### Deploy:
1. https://railway.app → Login GitHub
2. New Project → Deploy from GitHub
3. Selecionar repositório
4. Root Directory: `backend`

### Variáveis:
```env
MONGO_URL=mongodb+srv://mir4admin:SENHA@...
DB_NAME=mir4_manager
CORS_ORIGINS=*
```

### Configurar:
- Start Command: `uvicorn server:app --host 0.0.0.0 --port $PORT`
- Generate Domain → Copiar URL

---

## 3️⃣ Frontend no Vercel (3 minutos)

### Deploy:
1. https://vercel.com → New Project
2. Import repositório GitHub
3. Configure:
   - **Root Directory:** `frontend`
   - **Framework:** Create React App
   - **Build:** `yarn build`
   - **Output:** `build`

### Variáveis:
```env
REACT_APP_BACKEND_URL=https://sua-api.railway.app
```

### Deploy!

---

## 4️⃣ Atualizar CORS

Voltar no Railway:
```env
CORS_ORIGINS=https://seu-app.vercel.app
```

---

## ✅ Testar

1. Abrir Vercel URL
2. Criar conta
3. Adicionar dados
4. Confirmar contagem

**Funcionou?** 🎉

---

## 💡 Dicas

- Railway: $5 grátis/mês
- Vercel: Gratuito
- MongoDB: 512MB grátis
- Total: Gratuito para começar!

---

## 🐛 Troubleshooting

**Backend não conecta MongoDB:**
- Verificar connection string
- Network Access = 0.0.0.0/0

**Frontend erro CORS:**
- Atualizar CORS_ORIGINS no Railway
- Usar URL completa do Vercel

**Build falha:**
- Verificar Root Directory
- Verificar variáveis de ambiente
