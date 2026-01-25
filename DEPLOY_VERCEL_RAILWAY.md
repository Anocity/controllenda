# 🚀 GUIA COMPLETO - Deploy Vercel + Railway

## ⚠️ IMPORTANTE
- **Frontend (React)** → Vercel
- **Backend (FastAPI)** → Railway  
- **Database** → MongoDB Atlas

O Vercel NÃO suporta Python/FastAPI. Por isso usamos Railway para o backend.

---

## 📋 PASSO 1: Preparar MongoDB Atlas (5 minutos)

### 1.1 Criar Conta e Cluster
1. Acesse: https://www.mongodb.com/cloud/atlas/register
2. Crie conta gratuita
3. Clique em "Build a Database"
4. Escolha **M0 FREE** (512 MB grátis)
5. Escolha região **São Paulo (sa-east-1)** ou mais próxima
6. Clique em "Create Cluster" (aguarde 3-5 minutos)

### 1.2 Configurar Acesso
1. **Network Access**:
   - Menu lateral → Network Access
   - Click "Add IP Address"
   - Click "Allow Access from Anywhere" (0.0.0.0/0)
   - Click "Confirm"

2. **Database User**:
   - Menu lateral → Database Access
   - Click "Add New Database User"
   - Username: `mir4admin`
   - Password: `SuaSenhaForte123` (anote!)
   - Role: Atlas Admin
   - Click "Add User"

### 1.3 Obter Connection String
1. Volte para "Database"
2. Click no botão "Connect" do seu cluster
3. Escolha "Connect your application"
4. Driver: Python, Version: 3.12 or later
5. Copie a connection string:
   ```
   mongodb+srv://mir4admin:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```
6. **IMPORTANTE**: Substitua `<password>` pela senha que você criou

**Exemplo final:**
```
mongodb+srv://mir4admin:SuaSenhaForte123@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
```

---

## 📋 PASSO 2: Deploy Backend no Railway (10 minutos)

### 2.1 Criar Conta Railway
1. Acesse: https://railway.app
2. Click "Login" → "Login with GitHub"
3. Autorize Railway no GitHub

### 2.2 Criar Novo Projeto
1. Click "New Project"
2. Escolha "Deploy from GitHub repo"
3. Click "Configure GitHub App"
4. Selecione seu repositório `mir4-account-manager`
5. Click "Deploy Now"

### 2.3 Configurar Backend
1. Railway vai detectar 2 pastas (backend e frontend)
2. Click no card do **backend**
3. Vá em "Settings" (engrenagem)
4. Em "Root Directory" coloque: `backend`
5. Em "Start Command" coloque:
   ```
   uvicorn server:app --host 0.0.0.0 --port $PORT
   ```

### 2.4 Configurar Variáveis de Ambiente
1. Ainda em Settings, vá em "Variables"
2. Click "New Variable" e adicione:

```env
MONGO_URL=mongodb+srv://mir4admin:SuaSenhaForte123@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
DB_NAME=mir4_manager
CORS_ORIGINS=*
```

**IMPORTANTE**: 
- Use SUA connection string do MongoDB Atlas
- Por enquanto deixe `CORS_ORIGINS=*` (vamos mudar depois)

3. Click "Deploy" (aguarde 2-3 minutos)

### 2.5 Obter URL do Backend
1. Após deploy bem-sucedido
2. Vá em "Settings" → "Networking"
3. Click "Generate Domain"
4. Copie a URL gerada (exemplo: `mir4-backend-production.up.railway.app`)
5. **ANOTE ESSA URL!** Você vai precisar

**Sua URL será algo como:**
```
https://mir4-backend-production.up.railway.app
```

### 2.6 Testar Backend
Abra no navegador:
```
https://SUA-URL-RAILWAY.up.railway.app/api/accounts
```

Deve retornar: `[]` (array vazio, está funcionando!)

---

## 📋 PASSO 3: Deploy Frontend no Vercel (5 minutos)

### 3.1 Atualizar Código no GitHub

**ANTES de fazer deploy no Vercel**, você precisa atualizar o arquivo `.env` do frontend:

1. No seu computador, edite `/app/frontend/.env`:
```env
REACT_APP_BACKEND_URL=https://SUA-URL-RAILWAY.up.railway.app
```

2. **Substitua** pela URL do Railway que você copiou

3. Commit e push:
```bash
cd /app
git add .
git commit -m "Configure backend URL for production"
git push
```

### 3.2 Deploy no Vercel

1. Acesse: https://vercel.com
2. Click "Add New" → "Project"
3. Click "Import" no seu repositório `mir4-account-manager`

### 3.3 Configurar Projeto

**Configure assim:**

```
Framework Preset: Create React App
Root Directory: frontend
Build Command: yarn build
Output Directory: build
Install Command: yarn install
```

### 3.4 Variáveis de Ambiente

1. Click em "Environment Variables"
2. Adicione:

```
Name: REACT_APP_BACKEND_URL
Value: https://SUA-URL-RAILWAY.up.railway.app
```

**IMPORTANTE**: Use a URL do Railway (sem barra / no final)

3. Click "Deploy" (aguarde 2-3 minutos)

### 3.5 Seu Site Está no Ar! 🎉

Vercel vai gerar uma URL tipo:
```
https://mir4-account-manager.vercel.app
```

---

## 📋 PASSO 4: Configurar CORS no Backend

Agora que você tem a URL do Vercel, precisa configurar CORS:

1. Volte no **Railway**
2. Click no projeto do backend
3. Vá em "Variables"
4. Edite `CORS_ORIGINS`:
```
https://mir4-account-manager.vercel.app
```

5. Railway vai fazer redeploy automático

---

## ✅ CHECKLIST FINAL

- [ ] MongoDB Atlas criado e configurado
- [ ] Connection string do MongoDB copiada
- [ ] Backend deployado no Railway
- [ ] URL do Railway copiada e testada
- [ ] Variáveis de ambiente do Railway configuradas
- [ ] Frontend deployado no Vercel
- [ ] Variáveis de ambiente do Vercel configuradas
- [ ] CORS configurado no Railway com URL do Vercel
- [ ] Site acessível e funcionando

---

## 🧪 TESTAR O SITE

1. Abra sua URL do Vercel: `https://seu-app.vercel.app`
2. Click em "Nova Conta"
3. Preencha dados e salve
4. Se funcionar → **SUCESSO!** 🎉

---

## 🔧 PROBLEMAS COMUNS

### ❌ Erro: "Network Error" ou "Failed to fetch"

**Causa**: Frontend não consegue conectar com backend

**Solução**:
1. Verifique se `REACT_APP_BACKEND_URL` está correto no Vercel
2. Teste a URL do Railway direto no navegador
3. Verifique CORS no Railway

### ❌ Backend não inicia no Railway

**Causa**: Variáveis de ambiente incorretas

**Solução**:
1. Verifique `MONGO_URL` no Railway
2. Teste connection string no MongoDB Compass
3. Veja logs no Railway: Settings → Deployments → View Logs

### ❌ Frontend mostra tela branca

**Causa**: Erro de build ou variável de ambiente

**Solução**:
1. Vá em Vercel → Deployments → Ver logs de build
2. Verifique se `REACT_APP_BACKEND_URL` está configurado
3. Tente redeploy: Deployments → ⋯ → Redeploy

---

## 📱 URLs FINAIS

Após configurar tudo:

- **Frontend**: https://mir4-account-manager.vercel.app
- **Backend**: https://mir4-backend-production.up.railway.app
- **API Test**: https://mir4-backend-production.up.railway.app/api/accounts
- **Database**: MongoDB Atlas

---

## 🎯 RESUMO DOS SERVIÇOS

| Serviço | Uso | Custo | Link |
|---------|-----|-------|------|
| Vercel | Frontend (React) | Gratuito | vercel.com |
| Railway | Backend (FastAPI) | $5 grátis/mês | railway.app |
| MongoDB Atlas | Database | 512MB grátis | mongodb.com |

---

## 💡 DICAS

1. **Railway tem $5 grátis/mês** - suficiente para começar
2. **Vercel é 100% gratuito** para projetos pessoais
3. **MongoDB Atlas M0** é gratuito para sempre (512 MB)
4. Todos os 3 tem planos gratuitos generosos!

---

## 🔄 ATUALIZAR O SITE

Quando fizer mudanças no código:

```bash
git add .
git commit -m "Descrição da mudança"
git push
```

**Deploy automático:**
- Vercel: redeploy automático
- Railway: redeploy automático

---

## 📞 PRECISA DE AJUDA?

1. Veja os logs no Vercel: Deployments → View Function Logs
2. Veja os logs no Railway: Settings → Deployments
3. Teste o backend direto: `https://sua-url.railway.app/api/accounts`

---

**Pronto! Seu site está no ar! 🚀**
