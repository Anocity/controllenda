# 🖥️ GUIA COMPLETO - Criar Executável Windows (.exe)

## 📋 Requisitos

Antes de começar, instale:

1. **Node.js** (v18+): https://nodejs.org
2. **Python** (v3.11+): https://python.org
3. **Yarn**: `npm install -g yarn`
4. **Git**: https://git-scm.com

---

## ⚡ MÉTODO RÁPIDO (Recomendado)

### Windows PowerShell:
```powershell
cd /app
.\build-desktop.bat
```

### Ou use o PowerShell script:
```powershell
cd /app
.\build-desktop.ps1
```

**Tempo:** ~10-15 minutos

**Resultado:** Arquivo `MIR4 Account Manager Setup.exe` em `/app/desktop/dist/`

---

## 🔧 MÉTODO MANUAL (Passo a Passo)

### 1️⃣ Preparar Frontend

```bash
cd frontend

# Configurar para rodar localmente
echo REACT_APP_BACKEND_URL=http://127.0.0.1:8001 > .env

# Build
yarn install
yarn build

# Copiar para pasta desktop
xcopy /E /I /Y build ..\desktop\build

cd ..
```

### 2️⃣ Criar Backend Executável

```bash
# Instalar PyInstaller
pip install pyinstaller

# Criar executável do backend
python -m PyInstaller ^
  --onefile ^
  --name server_desktop ^
  --hidden-import uvicorn.protocols.http.auto ^
  --hidden-import uvicorn.protocols.websockets.auto ^
  desktop\server_desktop.py

# Organizar arquivos
mkdir desktop\backend
move dist\server_desktop.exe desktop\backend\

# Limpar arquivos temporários
rmdir /S /Q build dist
del server_desktop.spec
```

### 3️⃣ Build Electron App

```bash
cd desktop

# Instalar dependências
yarn install

# Criar executável
yarn build

# Pronto! O .exe está em: dist\
```

---

## 📦 O QUE VAI SER CRIADO

```
desktop/
├── dist/
│   └── MIR4 Account Manager Setup.exe  ← ESTE É SEU INSTALADOR!
```

**Tamanho aproximado:** 150-200 MB

---

## 💾 INSTALAR O PROGRAMA

1. Vá para: `/app/desktop/dist/`
2. Execute: `MIR4 Account Manager Setup.exe`
3. Siga o instalador
4. O programa será instalado em `C:\Program Files\MIR4 Account Manager\`
5. Atalho será criado na área de trabalho

---

## 🎯 CARACTERÍSTICAS DO EXECUTÁVEL

### ✅ O que inclui:
- Frontend React completo
- Backend FastAPI embarcado
- Banco de dados SQLite local
- Tudo roda offline (sem internet necessária)
- Janela ajustada para 50% do monitor
- Ícone personalizado
- Instalador profissional

### 📐 Tamanho da Janela:
- **Largura:** 50% da tela
- **Altura:** 70% da tela
- **Mínimo:** 800x600
- **Redimensionável:** Sim

### 💾 Dados Salvos:
Todos os dados ficam salvos em:
```
C:\Users\SeuUsuario\AppData\Local\MIR4 Account Manager\mir4_data.db
```

---

## 🐛 PROBLEMAS COMUNS

### ❌ "PyInstaller não encontrado"
```bash
pip install --upgrade pip
pip install pyinstaller
```

### ❌ "Yarn não reconhecido"
```bash
npm install -g yarn
```

### ❌ "Build do Electron falhou"
```bash
cd desktop
rmdir /S /Q node_modules
yarn install
yarn build
```

### ❌ "Backend não inicia"
Verifique se todas as bibliotecas Python estão instaladas:
```bash
pip install fastapi uvicorn pydantic
```

---

## 🔄 ATUALIZAR O PROGRAMA

Para criar uma nova versão do executável:

1. Faça suas mudanças no código
2. Execute novamente:
   ```bash
   .\build-desktop.bat
   ```
3. Novo `.exe` será gerado em `desktop\dist\`

---

## 📊 COMPARAÇÃO: WEB vs DESKTOP

| Característica | Versão Web | Versão Desktop |
|----------------|------------|----------------|
| **Instalação** | Não precisa | Precisa instalar |
| **Internet** | Necessária | Não precisa |
| **Velocidade** | Depende da rede | Muito rápido |
| **Dados** | Cloud (MongoDB) | Local (SQLite) |
| **Acessibilidade** | Qualquer dispositivo | Só no PC instalado |
| **Atualização** | Automática | Manual |

---

## 💡 DICAS

### Tornar o .exe menor:
```bash
# Use UPX para comprimir (reduz ~40%)
pip install pyinstaller[encryption]
python -m PyInstaller --upx-dir=C:\upx desktop\server_desktop.py
```

### Criar versão portátil (sem instalador):
```bash
cd desktop
yarn run pack
# Cria pasta em dist\ que pode ser copiada para pendrive
```

### Adicionar ícone personalizado:
1. Coloque `icon.ico` em `/app/desktop/`
2. Rebuild: `yarn build`

---

## 📁 ESTRUTURA DO EXECUTÁVEL

```
MIR4 Account Manager/
├── MIR4 Account Manager.exe    ← Executável principal
├── resources/
│   ├── app.asar                ← Frontend empacotado
│   └── backend/
│       └── server_desktop.exe  ← Backend
└── mir4_data.db                ← Banco de dados
```

---

## 🎯 PRÓXIMOS PASSOS

Após gerar o `.exe`:

1. ✅ Testar instalação
2. ✅ Criar contas de teste
3. ✅ Verificar se dados são salvos
4. ✅ Compartilhar com outros usuários!

---

## 📞 SUPORTE

### Logs do Electron:
```
C:\Users\SeuUsuario\AppData\Roaming\mir4-account-manager-desktop\logs\
```

### Testar sem instalar:
```bash
cd desktop
yarn start
```

---

**Pronto! Agora você tem um programa desktop profissional! 🎉**

O executável pode ser distribuído para outros usuários sem eles precisarem instalar Python, Node.js ou qualquer outra coisa!
