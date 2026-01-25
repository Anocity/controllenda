# 🖥️ MIR4 Account Manager - VERSÃO DESKTOP

## 🎯 O QUE É?

Versão executável (.exe) do MIR4 Account Manager para Windows.

**Características:**
- ✅ Funciona 100% OFFLINE (sem internet)
- ✅ Banco de dados local (SQLite)
- ✅ Janela ajustada (50% do monitor)
- ✅ Instalador profissional
- ✅ Dados salvos localmente
- ✅ Não precisa configurar nada!

---

## 📥 OPÇÃO 1: BAIXAR EXECUTÁVEL PRONTO

**(Se você já tem o .exe compilado)**

1. Execute: `MIR4 Account Manager Setup.exe`
2. Siga o instalador
3. Pronto! Use o programa

**Tamanho:** ~150 MB

---

## 🛠️ OPÇÃO 2: COMPILAR VOCÊ MESMO

### Requisitos:
- Windows 10/11
- Node.js 18+
- Python 3.11+
- Yarn

### Passo a Passo:

```bash
# 1. Clone ou baixe o repositório
git clone https://github.com/seu-usuario/mir4-account-manager.git
cd mir4-account-manager

# 2. Execute o script de build
build-desktop.bat

# 3. Aguarde ~10 minutos

# 4. Executável estará em:
desktop\dist\MIR4 Account Manager Setup.exe
```

**Detalhes completos:** Veja `DESKTOP_BUILD_GUIDE.md`

---

## 🎮 COMO USAR

### Primeira vez:
1. Instale o programa
2. Abra "MIR4 Account Manager"
3. Click em "Nova Conta"
4. Preencha os dados
5. Seus dados são salvos automaticamente!

### Editar dados:
- Clique diretamente na célula que quer editar
- Digite o novo valor
- Pressione Enter ou clique fora

### Configurar preços:
- Click no botão "Preços USD"
- Defina o valor de cada tipo de boss
- Click em "Salvar Preços"

---

## 💾 ONDE OS DADOS SÃO SALVOS?

```
C:\Users\SeuUsuario\AppData\Local\MIR4 Account Manager\mir4_data.db
```

**Backup:**
- Copie o arquivo `mir4_data.db` para pendrive
- Para restaurar, cole de volta na mesma pasta

---

## 🔧 DIFERENÇAS: WEB vs DESKTOP

| | Versão Web | Versão Desktop |
|-|------------|----------------|
| **Internet** | ✅ Necessária | ❌ Não precisa |
| **Instalação** | ❌ Não precisa | ✅ Precisa instalar |
| **Velocidade** | Média | ⚡ Muito rápida |
| **Dados** | Cloud | 💾 Local |
| **Backup** | Automático | Manual |
| **Acesso** | Qualquer lugar | Só no PC |

---

## 📐 TAMANHO DA JANELA

- **50%** da largura da tela
- **70%** da altura da tela
- **Mínimo:** 800x600 pixels
- **Redimensionável:** Sim

---

## 🐛 PROBLEMAS

### O programa não abre
1. Verifique se instalou corretamente
2. Execute como Administrador
3. Verifique Windows Defender

### Dados não salvam
1. Verifique permissões da pasta AppData
2. Execute como Administrador

### Janela muito pequena/grande
1. Redimensione manualmente
2. O tamanho será salvo automaticamente

---

## 🔄 ATUALIZAR VERSÃO

1. Desinstale a versão antiga
2. Instale a versão nova
3. Seus dados serão mantidos (não se preocupe!)

---

## ❓ FAQ

**P: Preciso de internet?**
R: Não! Tudo funciona offline.

**P: Meus dados ficam seguros?**
R: Sim! Tudo fica salvo localmente no seu PC.

**P: Posso usar em vários PCs?**
R: Sim, mas precisa instalar em cada um. Use backup do arquivo .db para transferir dados.

**P: É grátis?**
R: Sim, completamente gratuito!

**P: Posso distribuir o .exe?**
R: Sim! Pode compartilhar com outros jogadores.

---

## 📦 ARQUIVOS DO PROJETO

```
/app/
├── desktop/              ← Pasta da versão desktop
│   ├── server_desktop.py ← Backend com SQLite
│   ├── main.js           ← Electron principal
│   ├── package.json      ← Config Electron
│   └── build/            ← Frontend compilado
├── build-desktop.bat     ← Script de build Windows
├── build-desktop.ps1     ← Script PowerShell
└── DESKTOP_BUILD_GUIDE.md ← Guia completo
```

---

## 💡 VANTAGENS DA VERSÃO DESKTOP

1. **Privacidade:** Dados ficam no seu PC
2. **Velocidade:** Sem latência de rede
3. **Confiabilidade:** Funciona sem internet
4. **Simplicidade:** Não precisa configurar servidor
5. **Portabilidade:** Pode levar em pendrive

---

## 🎯 TECNOLOGIAS USADAS

- **Electron:** Interface desktop
- **React:** Frontend
- **FastAPI:** Backend
- **SQLite:** Banco de dados local
- **PyInstaller:** Compilar Python para .exe

---

## 📞 SUPORTE

Problemas? Abra uma issue no GitHub!

---

**Aproveite seu MIR4 Account Manager Desktop! 🎮**
