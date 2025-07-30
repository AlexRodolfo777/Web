# 🚀 Guia de Deploy no Vercel

## Pré-requisitos

- Conta no GitHub (recomendado)
- Conta no Vercel (gratuita)
- Projeto organizado conforme estrutura abaixo

## Estrutura do Projeto

```
projeto/
├── app_parafusos.html    # Aplicação principal
├── vercel.json           # Configuração do Vercel
├── package.json          # Configuração do projeto
├── README.md            # Documentação
├── .gitignore           # Arquivos ignorados pelo Git
├── _redirects           # Redirecionamentos
└── public/              # Arquivos públicos
    ├── _headers         # Headers de segurança
    ├── robots.txt       # SEO
    └── sitemap.xml     # Sitemap
```

## Métodos de Deploy

### 1. Deploy via GitHub (Recomendado)

#### Passo 1: Preparar o Repositório
```bash
# Inicializar Git
git init

# Adicionar arquivos
git add .

# Fazer commit inicial
git commit -m "Initial commit: Guia de Parafusos"

# Configurar branch principal
git branch -M main

# Adicionar repositório remoto (substitua pela sua URL)
git remote add origin https://github.com/seu-usuario/guia-parafusos.git

# Fazer push
git push -u origin main
```

#### Passo 2: Conectar ao Vercel
1. Acesse [vercel.com](https://vercel.com)
2. Faça login com sua conta GitHub
3. Clique em "New Project"
4. Selecione seu repositório `guia-parafusos`
5. Clique em "Deploy"

### 2. Deploy via Vercel CLI

#### Instalar Vercel CLI
```bash
npm i -g vercel
```

#### Fazer Login
```bash
vercel login
```

#### Deploy
```bash
vercel
```

### 3. Deploy Manual (Drag & Drop)

1. Acesse [vercel.com](https://vercel.com)
2. Clique em "New Project"
3. Arraste a pasta do projeto
4. Clique em "Deploy"

## Configurações Importantes

### vercel.json
O arquivo `vercel.json` já está configurado com:
- Build para arquivos HTML estáticos
- Headers de segurança
- Cache otimizado
- Região Brasil (gru1)

### Headers de Segurança
O projeto inclui headers para:
- Proteção XSS
- Prevenção de clickjacking
- Cache otimizado
- Políticas de segurança

## Domínio Personalizado

Após o deploy, você pode configurar um domínio personalizado:

1. No dashboard do Vercel, vá em "Settings"
2. Clique em "Domains"
3. Adicione seu domínio
4. Configure os registros DNS conforme instruções

## Monitoramento

O Vercel oferece:
- Analytics de performance
- Logs de erro
- Métricas de uso
- Deploy automático (com GitHub)

## Troubleshooting

### Problema: Página não carrega
- Verifique se o arquivo `app_parafusos.html` está na raiz
- Confirme se o `vercel.json` está correto

### Problema: CSS não carrega
- O CSS está inline no HTML, não deve haver problemas

### Problema: JavaScript não funciona
- Verifique o console do navegador
- Confirme se não há erros de sintaxe

### Problema: Deploy falha
- Verifique os logs no dashboard do Vercel
- Confirme se todos os arquivos estão no repositório

## Otimizações

### Performance
- ✅ CSS inline (carregamento rápido)
- ✅ JavaScript otimizado
- ✅ Imagens SVG (leves)
- ✅ Cache configurado

### SEO
- ✅ Meta tags configuradas
- ✅ Sitemap.xml
- ✅ Robots.txt
- ✅ Headers otimizados

### Segurança
- ✅ Headers de segurança
- ✅ CSP configurado
- ✅ XSS Protection
- ✅ Content Type Options

## Próximos Passos

Após o deploy bem-sucedido:

1. **Teste a aplicação** em diferentes dispositivos
2. **Configure analytics** (Google Analytics, etc.)
3. **Monitore performance** no dashboard do Vercel
4. **Configure backup** do repositório
5. **Documente mudanças** no README

## Suporte

Se encontrar problemas:
- Consulte a [documentação do Vercel](https://vercel.com/docs)
- Abra uma issue no GitHub
- Entre em contato com o suporte do Vercel

---

**🎉 Seu site estará online em minutos!** 