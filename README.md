# 🔩 Guia Completo de Parafusos

Uma aplicação web interativa e completa sobre parafusos, incluindo tipos, medidas, tratamentos e calculadoras técnicas.

## ✨ Funcionalidades

- **📚 Guia Completo**: Informações detalhadas sobre parafusos, porcas, arruelas e barras roscadas
- **🧮 Calculadoras Técnicas**: 
  - Calculadora de torque avançada
  - Conversor de medidas (métrico/imperial)
  - Calculadora de roscas
  - Calculadora de carga
- **📊 Tabelas de Referência**: Medidas, tratamentos e aplicações
- **💾 Histórico de Cálculos**: Salve e exporte seus cálculos
- **📱 Design Responsivo**: Funciona em desktop, tablet e mobile

## 🚀 Deploy no Vercel

### Opção 1: Deploy via GitHub (Recomendado)

1. **Faça upload do projeto para o GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/seu-usuario/seu-repositorio.git
   git push -u origin main
   ```

2. **Conecte ao Vercel**
   - Acesse [vercel.com](https://vercel.com)
   - Faça login com sua conta GitHub
   - Clique em "New Project"
   - Selecione seu repositório
   - Clique em "Deploy"

### Opção 2: Deploy via Vercel CLI

1. **Instale o Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Faça login no Vercel**
   ```bash
   vercel login
   ```

3. **Deploy do projeto**
   ```bash
   vercel
   ```

### Opção 3: Deploy Manual

1. **Baixe o projeto**
2. **Acesse [vercel.com](https://vercel.com)**
3. **Clique em "New Project"**
4. **Arraste a pasta do projeto**
5. **Clique em "Deploy"**

## 🛠️ Desenvolvimento Local

### Pré-requisitos
- Node.js 14+ (opcional, para servidor local)

### Instalação
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# Instale as dependências (opcional)
npm install

# Inicie o servidor local
npm run dev
```

### Estrutura do Projeto
```
projeto/
├── app_parafusos.html    # Aplicação principal
├── vercel.json           # Configuração do Vercel
├── package.json          # Configuração do projeto
└── README.md            # Este arquivo
```

## 📋 Funcionalidades Detalhadas

### 🔧 Calculadora de Torque
- Diâmetros: M3 a M24
- Classes de resistência: 4.6, 5.6, 8.8, 10.9, 12.9
- Coeficientes de atrito configuráveis
- Fatores de segurança ajustáveis

### 📐 Conversor de Medidas
- Milímetros ↔ Polegadas
- Centímetros ↔ Metros
- Precisão de 3 casas decimais

### 🔩 Calculadora de Rosca
- Sistema métrico (ISO)
- Sistema imperial (UNC/UNF)
- Cálculo de dimensões da rosca

### ⚖️ Calculadora de Carga
- Materiais: Aço, Alumínio, Titânio, Bronze, Latão
- Tipos de carga: Estática, Dinâmica, Impacto
- Recomendação automática de parafuso

## 🎨 Design e UX

- **Interface Moderna**: Design limpo e profissional
- **Animações Suaves**: Transições e efeitos visuais
- **Responsivo**: Adapta-se a qualquer dispositivo
- **Acessibilidade**: Cores contrastantes e navegação clara
- **Performance**: Carregamento rápido e otimizado

## 📱 Compatibilidade

- ✅ Chrome 80+
- ✅ Firefox 75+
- ✅ Safari 13+
- ✅ Edge 80+
- ✅ Mobile browsers

## 🔧 Tecnologias Utilizadas

- **HTML5**: Estrutura semântica
- **CSS3**: Estilos modernos e responsivos
- **JavaScript**: Interatividade e cálculos
- **SVG**: Gráficos vetoriais para parafusos
- **Vercel**: Deploy e hospedagem

## 📄 Licença

MIT License - veja o arquivo LICENSE para detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature
3. Fazer commit das mudanças
4. Fazer push para a branch
5. Abrir um Pull Request

## 📞 Suporte

Se você encontrar algum problema ou tiver sugestões:

- Abra uma issue no GitHub
- Entre em contato via email
- Consulte a documentação técnica

---

**Desenvolvido com ❤️ para a comunidade técnica** 