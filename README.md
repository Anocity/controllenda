# MIR4 Account Manager

Sistema simples de gerenciamento de contas do jogo MIR4 com cálculo automático de valores em USD.

**100% Frontend** - Roda direto no navegador, sem backend ou banco de dados!

## 🎮 Funcionalidades

- ✅ **Tabela Editável**: Clique em qualquer célula para editar
- ✅ **Gerenciamento de Bosses**: M2, G2, M4, G4, M6, G6, M7, G7, M8, G8
- ✅ **Bosses Especiais**: Xama, Praça 4F, Cracha Épica
- ✅ **Cálculo USD Automático**: Configure preços e veja totais em tempo real
- ✅ **Totais Automáticos**: Soma de cada tipo de boss e valores USD
- ✅ **Dados Locais**: Tudo salvo no navegador (localStorage)
- ✅ **Sem Instalação**: Funciona direto no navegador

## 🚀 Como Usar Localmente

```bash
cd frontend
yarn install
yarn start
```

Abra: `http://localhost:3000`

## 📦 Deploy no Vercel (1 clique)

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/seu-usuario/mir4-account-manager)

### Ou manualmente:

1. Faça fork/clone deste repositório
2. Crie conta no [Vercel](https://vercel.com)
3. Clique em "New Project"
4. Import seu repositório
5. **Root Directory:** `frontend`
6. **Framework Preset:** `Create React App`
7. Deploy!

Pronto! Seu site estará no ar em ~2 minutos.

## 🎨 Tecnologias

- **React 18** - Interface
- **Tailwind CSS** - Estilos
- **Shadcn UI** - Componentes
- **localStorage** - Armazenamento local

## 💾 Armazenamento

Todos os dados são salvos localmente no navegador usando `localStorage`:
- ✅ Não precisa de conta
- ✅ Não precisa de internet (depois do primeiro acesso)
- ✅ Privacidade total (dados só no seu navegador)
- ⚠️ Dados perdidos se limpar cache do navegador

## 🎯 Como Usar

1. **Adicionar Conta**: Clique em "Nova Conta"
2. **Editar**: Clique em qualquer célula para editar inline
3. **Salvar**: Pressione Enter ou clique fora
4. **Configurar Preços**: Botão "Preços USD"
5. **Deletar**: Clique no ícone de lixeira

## 🌈 Sistema de Cores

- 🟢 **Verde**: Números > 0
- ⚪ **Branco**: Nome e Sala Pico
- 🔵 **Azul**: Gold
- ⚫ **Vazio**: Valores = 0

## 📊 Estrutura

```
frontend/
├── src/
│   ├── components/
│   │   ├── ui/                    # Componentes Shadcn
│   │   ├── EditableTable.js       # Tabela principal
│   │   └── BossPriceDialog.js     # Config preços
│   ├── pages/
│   │   └── Dashboard.js           # Página principal
│   ├── App.js
│   └── index.css
└── package.json
```

## 🔧 Desenvolvimento

```bash
# Instalar dependências
cd frontend
yarn install

# Rodar localmente
yarn start

# Build para produção
yarn build
```

## 📱 Outras Opções de Deploy

### Netlify
1. Arraste a pasta `frontend/build` para [Netlify Drop](https://app.netlify.com/drop)

### GitHub Pages
```bash
cd frontend
yarn build
# Configure GitHub Pages para servir da pasta build
```

### Qualquer hosting estático
Basta fazer upload da pasta `frontend/build`

## 💡 Backup dos Dados

### Exportar:
1. Abra Console do navegador (F12)
2. Execute:
```javascript
const backup = {
  accounts: localStorage.getItem('mir4_accounts'),
  prices: localStorage.getItem('mir4_boss_prices')
};
console.log(JSON.stringify(backup));
// Copie e salve em arquivo .txt
```

### Importar:
```javascript
const backup = /* cole seu backup aqui */;
localStorage.setItem('mir4_accounts', backup.accounts);
localStorage.setItem('mir4_boss_prices', backup.prices);
location.reload();
```

## 📄 Licença

MIT - Use livremente!

## 🤝 Contribuições

Pull requests são bem-vindos!

---

**Feito para a comunidade MIR4** ❤️
