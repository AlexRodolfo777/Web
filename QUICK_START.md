# ⚡ Deploy Rápido no Vercel

## 🚀 Deploy em 3 Passos

### 1. Upload para GitHub
```bash
git init
git add .
git commit -m "Guia de Parafusos - Deploy inicial"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/guia-parafusos.git
git push -u origin main
```

### 2. Conectar ao Vercel
- Acesse [vercel.com](https://vercel.com)
- Login com GitHub
- Clique "New Project"
- Selecione seu repositório
- Clique "Deploy"

### 3. Pronto! 🎉
Seu site estará online em: `https://seu-projeto.vercel.app`

## 📁 Arquivos Importantes

- ✅ `app_parafusos.html` - Aplicação principal
- ✅ `vercel.json` - Configuração do Vercel
- ✅ `package.json` - Configuração do projeto
- ✅ `_redirects` - Redirecionamentos
- ✅ `public/_headers` - Headers de segurança
- ✅ `public/robots.txt` - SEO
- ✅ `public/sitemap.xml` - Sitemap

## 🔧 Configurações Automáticas

O projeto já está configurado com:
- ✅ Headers de segurança
- ✅ Cache otimizado
- ✅ SEO básico
- ✅ Região Brasil
- ✅ Redirecionamentos

## 📱 Teste Local (Opcional)

```bash
npm install
npm run dev
```

## 🆘 Problemas Comuns

**Página não carrega?**
- Verifique se `app_parafusos.html` está na raiz

**Deploy falha?**
- Confirme se todos os arquivos estão no Git

**CSS não carrega?**
- CSS está inline, não deve haver problemas

---

**🎯 Resultado: Site profissional online em minutos!** 