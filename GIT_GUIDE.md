# Comandos Git para Publicar no GitHub

## 1️⃣ Inicializar Git (se ainda não foi feito)

```bash
cd /app
git init
git branch -M main
```

## 2️⃣ Adicionar Arquivos

```bash
# Adicionar todos os arquivos
git add .

# Verificar status
git status
```

## 3️⃣ Fazer Commit

```bash
git commit -m "Initial commit - MIR4 Account Manager"
```

## 4️⃣ Criar Repositório no GitHub

1. Acesse: https://github.com/new
2. Nome: `mir4-account-manager`
3. Descrição: `Sistema de gerenciamento de contas MIR4 com cálculo USD`
4. **NÃO** inicialize com README (já temos)
5. Clique em "Create repository"

## 5️⃣ Conectar e Enviar

```bash
# Substituir SEU_USUARIO pelo seu username do GitHub
git remote add origin https://github.com/SEU_USUARIO/mir4-account-manager.git

# Enviar código
git push -u origin main
```

## 6️⃣ Fazer Push de Atualizações Futuras

```bash
# Adicionar mudanças
git add .

# Commit
git commit -m "Descrição das mudanças"

# Push
git push
```

## 📝 Comandos Úteis

```bash
# Ver histórico de commits
git log --oneline

# Ver mudanças não commitadas
git diff

# Desfazer mudanças não commitadas
git checkout -- arquivo.js

# Criar nova branch
git checkout -b feature/nova-funcionalidade

# Voltar para main
git checkout main

# Merge de branch
git merge feature/nova-funcionalidade

# Ver branches
git branch -a

# Deletar branch
git branch -d feature/nova-funcionalidade
```

## 🔧 Configurar Git (Primeira Vez)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"
```

## 🌐 Depois do Push

Seu projeto estará disponível em:
```
https://github.com/SEU_USUARIO/mir4-account-manager
```

## 📚 Próximos Passos

1. ✅ Push para GitHub
2. 🚀 Deploy (ver DEPLOY.md)
3. 🎨 Adicionar badge no README
4. 📄 Adicionar LICENSE
5. 🐛 Criar issues para melhorias

## 🏷️ Tags de Versão

```bash
# Criar tag
git tag -a v1.0.0 -m "Primeira versão"

# Push tags
git push --tags
```

## 🔐 SSH (Opcional - Recomendado)

Para não precisar digitar senha toda vez:

```bash
# Gerar chave SSH
ssh-keygen -t ed25519 -C "seu.email@example.com"

# Copiar chave pública
cat ~/.ssh/id_ed25519.pub

# Adicionar em: GitHub → Settings → SSH and GPG keys

# Mudar remote para SSH
git remote set-url origin git@github.com:SEU_USUARIO/mir4-account-manager.git
```

## 📊 Estatísticas

```bash
# Linhas de código
git ls-files | xargs wc -l

# Contribuidores
git shortlog -sn

# Últimas mudanças
git log --since="1 week ago" --oneline
```

## 🆘 Problemas Comuns

### Erro: "Updates were rejected"
```bash
git pull origin main --rebase
git push
```

### Arquivo grande demais
```bash
# Remover arquivo do histórico
git filter-branch --tree-filter 'rm -f arquivo-grande.zip' HEAD
```

### Desfazer último commit
```bash
# Manter mudanças
git reset --soft HEAD~1

# Descartar mudanças
git reset --hard HEAD~1
```

---

💡 **Dica**: Faça commits pequenos e frequentes com mensagens descritivas!

📖 Documentação completa: https://git-scm.com/doc
