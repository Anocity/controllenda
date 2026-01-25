# ⚡ COMANDOS RÁPIDOS - Deploy Vercel + Railway

## 🎯 O QUE VAI ONDE?

```
Frontend (React)  →  Vercel     ✅ Gratuito
Backend (FastAPI) →  Railway    ✅ $5/mês grátis  
Database          →  MongoDB Atlas ✅ 512MB grátis
```

---

## 📝 ORDEM DE EXECUÇÃO

### 1️⃣ MongoDB Atlas (Database)
```
1. Criar conta: https://mongodb.com/cloud/atlas
2. Criar cluster M0 (Free)
3. Network Access → 0.0.0.0/0
4. Database User → criar usuário
5. Copiar connection string
```

### 2️⃣ Railway (Backend)
```
1. Login: https://railway.app
2. New Project → Deploy from GitHub
3. Selecionar repositório
4. Configurar backend:
   - Root Directory: backend
   - Start Command: uvicorn server:app --host 0.0.0.0 --port $PORT
   
5. Variáveis:
   MONGO_URL=sua_connection_string
   DB_NAME=mir4_manager
   CORS_ORIGINS=*
   
6. Generate Domain → Copiar URL
```

### 3️⃣ Atualizar GitHub
```bash
# Editar /app/frontend/.env com URL do Railway
cd /app
nano frontend/.env
# Mudar: REACT_APP_BACKEND_URL=https://sua-url.railway.app

git add .
git commit -m "Configure production backend URL"
git push
```

### 4️⃣ Vercel (Frontend)
```
1. Login: https://vercel.com
2. Import Project → Selecionar repo
3. Configurar:
   Framework: Create React App
   Root Directory: frontend
   Build Command: yarn build
   Output Directory: build
   
4. Environment Variables:
   REACT_APP_BACKEND_URL=https://sua-url.railway.app
   
5. Deploy
```

### 5️⃣ Atualizar CORS
```
Voltar no Railway:
Variables → CORS_ORIGINS
Mudar de * para: https://seu-app.vercel.app
```

---

## 🔑 VARIÁVEIS DE AMBIENTE

### Railway (Backend)
```env
MONGO_URL=mongodb+srv://usuario:senha@cluster.mongodb.net/
DB_NAME=mir4_manager
CORS_ORIGINS=https://seu-app.vercel.app
```

### Vercel (Frontend)
```env
REACT_APP_BACKEND_URL=https://sua-api.railway.app
```

---

## ✅ TESTAR

```
1. Backend: https://sua-api.railway.app/api/accounts
   Deve retornar: []

2. Frontend: https://seu-app.vercel.app
   Deve carregar o site

3. Criar conta no site
   Se salvar → Funcionou! 🎉
```

---

## 🐛 TROUBLESHOOTING RÁPIDO

### Erro CORS
```
Railway → Variables → CORS_ORIGINS
Colocar URL do Vercel
```

### Backend não conecta MongoDB
```
Railway → Variables → MONGO_URL
Verificar se a connection string está correta
MongoDB Atlas → Network Access → 0.0.0.0/0
```

### Frontend tela branca
```
Vercel → Settings → Environment Variables
Verificar REACT_APP_BACKEND_URL
Vercel → Deployments → Redeploy
```

---

## 📋 CHECKLIST MÍNIMO

- [ ] MongoDB Atlas configurado
- [ ] Backend no Railway rodando
- [ ] URL do Railway copiada
- [ ] Código atualizado no GitHub
- [ ] Frontend no Vercel deployado
- [ ] CORS configurado
- [ ] Site funcionando

---

**Tempo total: ~20 minutos** ⏱️

Leia o guia completo em: **DEPLOY_VERCEL_RAILWAY.md**
