# Guia de Deploy - MIR4 Account Manager

## 🚀 Opções de Deploy

### 1. Deploy com Vercel (Frontend) + Railway (Backend)

#### Backend no Railway

1. **Criar conta no Railway**: https://railway.app
2. **Novo Projeto**:
   - Clique em "New Project"
   - Selecione "Deploy from GitHub repo"
   - Conecte seu repositório

3. **Configurar Variáveis de Ambiente**:
   ```
   MONGO_URL=sua_url_mongodb_atlas
   DB_NAME=mir4_manager
   CORS_ORIGINS=https://seu-frontend.vercel.app
   ```

4. **Configurar MongoDB Atlas**:
   - Criar conta em https://www.mongodb.com/cloud/atlas
   - Criar cluster gratuito
   - Configurar Network Access (permitir 0.0.0.0/0)
   - Copiar connection string

5. **Deploy automático** será feito após push no GitHub

#### Frontend no Vercel

1. **Criar conta no Vercel**: https://vercel.com
2. **Importar Projeto**:
   - Clique em "New Project"
   - Conecte seu repositório GitHub
   - Selecione a pasta `frontend`

3. **Configurar Build**:
   ```
   Build Command: yarn build
   Output Directory: build
   Install Command: yarn install
   ```

4. **Variáveis de Ambiente**:
   ```
   REACT_APP_BACKEND_URL=https://sua-api.railway.app
   ```

5. **Deploy** e aguardar finalização

---

### 2. Deploy com Render (Full Stack)

#### Backend

1. **Criar conta no Render**: https://render.com
2. **Novo Web Service**:
   - Conecte GitHub
   - Selecione repositório
   - Escolha pasta `backend`

3. **Configurações**:
   ```
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn server:app --host 0.0.0.0 --port $PORT
   ```

4. **Variáveis de Ambiente**:
   ```
   MONGO_URL=sua_url_mongodb_atlas
   DB_NAME=mir4_manager
   CORS_ORIGINS=https://seu-frontend.onrender.com
   ```

#### Frontend

1. **Novo Static Site**:
   - Selecione repositório
   - Pasta `frontend`

2. **Configurações**:
   ```
   Build Command: yarn build
   Publish Directory: build
   ```

3. **Variáveis de Ambiente**:
   ```
   REACT_APP_BACKEND_URL=https://sua-api.onrender.com
   ```

---

### 3. Deploy com Netlify (Frontend) + Heroku (Backend)

#### Backend no Heroku

1. **Criar conta no Heroku**: https://heroku.com
2. **Instalar Heroku CLI**:
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

3. **Deploy**:
   ```bash
   cd backend
   heroku login
   heroku create mir4-api
   heroku addons:create mongolab:sandbox
   git push heroku main
   ```

4. **Configurar Variáveis**:
   ```bash
   heroku config:set CORS_ORIGINS=https://seu-app.netlify.app
   ```

#### Frontend no Netlify

1. **Criar conta no Netlify**: https://netlify.com
2. **Novo Site**:
   - Conecte GitHub
   - Selecione repositório
   - Base directory: `frontend`

3. **Build Settings**:
   ```
   Build command: yarn build
   Publish directory: frontend/build
   ```

4. **Variáveis de Ambiente**:
   ```
   REACT_APP_BACKEND_URL=https://sua-api.herokuapp.com
   ```

---

## 🗄️ MongoDB Atlas (Recomendado)

1. **Criar Cluster Gratuito**:
   - Acesse https://www.mongodb.com/cloud/atlas
   - Crie conta gratuita
   - Crie cluster M0 (Free Tier)

2. **Configurar Acesso**:
   - Network Access → Add IP Address → Allow Access from Anywhere (0.0.0.0/0)
   - Database Access → Add New Database User → Criar usuário

3. **Connection String**:
   ```
   mongodb+srv://usuario:senha@cluster.mongodb.net/mir4_manager?retryWrites=true&w=majority
   ```

---

## 📝 Checklist Pré-Deploy

- [ ] Criar repositório no GitHub
- [ ] Adicionar .gitignore
- [ ] Configurar .env.example
- [ ] Testar build local (`yarn build`)
- [ ] Criar banco MongoDB Atlas
- [ ] Configurar CORS corretamente
- [ ] Testar conexão backend → MongoDB
- [ ] Testar conexão frontend → backend

---

## 🔧 Troubleshooting

### CORS Error
- Verifique se CORS_ORIGINS no backend inclui URL do frontend
- Formato: `https://seu-app.vercel.app` (sem / no final)

### MongoDB Connection Error
- Verifique connection string
- Confirme Network Access configurado
- Teste conexão localmente primeiro

### Build Failed (Frontend)
- Verifique Node.js version (18+)
- Limpe cache: `yarn cache clean`
- Delete node_modules e reinstale

### API 404 Error
- Confirme REACT_APP_BACKEND_URL está correto
- Verifique se backend está rodando
- Teste endpoints direto no navegador

---

## 🌐 URLs Exemplo

Após deploy, suas URLs serão algo como:

- **Frontend**: https://mir4-manager.vercel.app
- **Backend**: https://mir4-api.railway.app
- **API**: https://mir4-api.railway.app/api/accounts

---

## 💡 Dicas

1. **Use variáveis de ambiente** - nunca commite .env com dados reais
2. **Teste localmente primeiro** - antes de fazer deploy
3. **MongoDB Atlas** - use tier gratuito M0 (512 MB)
4. **Monitoramento** - Railway e Render têm logs integrados
5. **Custom Domain** - todos os serviços permitem domínio próprio

---

Precisa de ajuda? Abra uma issue no GitHub!
