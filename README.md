# Estudos de Cibersegurança · Certificação CCST

Material de estudo interativo, feito a partir dos meus resumos dos cursos da Cisco Networking Academy, organizado em trilhas rumo à certificação **Cisco Certified Support Technician (CCST)**. As trilhas atuais cobrem a prova **CCST Networking (100-150)**.

🔗 **Acesse:** https://mpmirandasilva.github.io/estudos-ciberseguranca-ccst/

## Trilhas

Cada resumo é uma trilha independente, com módulos, glossário, exercícios e progresso próprios.

| Trilha | Curso de origem | Módulos |
|---|---|---|
| Fundamentos de Redes de Computadores | Networking Basics | 20 |
| Dispositivos de Rede e Configuração Inicial | Networking Devices and Initial Configuration | 13 |

## Como funciona

- **Cards em sequência**: os tópicos começam fechados e se revelam ao clicar; o próximo só abre depois do anterior.
- **Exercícios por módulo**, em duas partes:
  - *fixação*: conceitos e cálculos (binário, máscaras, sub-redes, IPv6), corrigidos na hora;
  - *estilo CCST*: cenários de suporte, saídas de comandos para interpretar (`ipconfig`, `show ip route`, `tracert`, `netstat`…), questões de "escolha duas", associação e ordenação. Cada questão é marcada com o domínio do blueprint (1.0 a 6.0).
- **Simulado CCST**: 40 questões em 50 minutos (ou versão curta), sorteadas das duas trilhas, com resultado por domínio e correção comentada.
- **Grifos da autora**: com o login da conta definida em `ownerEmail` (no `firebase-config.js`), é possível selecionar um trecho para grifar em turquesa e tocar em um grifo para apagá-lo. Os grifos ficam salvos na conta dela; para outras pessoas, o modo de grifar não aparece.
- **Explicação em cada resposta**, com link para o item do material que deve ser revisado.
- **Padrão visual único**: figuras desenhadas em SVG (acompanham o tema claro e escuro), tabelas, terminais, notas e fluxos com o mesmo estilo em todas as trilhas.
- **Progresso salvo** no navegador e, com login Google, sincronizado entre aparelhos.

As questões são autorais, escritas a partir dos tópicos oficiais do exame. Não são questões reais da prova.

## Ativar o login com Google (Firebase)

O site é estático (GitHub Pages), então o login usa o Firebase, gratuito no plano Spark. Sem configuração, o botão "Entrar" não aparece e o progresso fica só no navegador.

1. Em https://console.firebase.google.com, crie um projeto (o Google Analytics pode ficar desativado).
2. **Authentication → Começar → Método de login → Google → Ativar** e salve.
3. **Authentication → Configurações → Domínios autorizados → Adicionar domínio**: `mpmirandasilva.github.io`.
4. **Firestore Database → Criar banco de dados** (modo de produção, região `southamerica-east1`). Em **Regras**, cole o conteúdo de [`firestore.rules`](firestore.rules) e publique.
5. **Configurações do projeto → Seus apps → Web (`</>`)**: registre o app e copie `apiKey`, `authDomain`, `projectId` e `appId` para o arquivo [`firebase-config.js`](firebase-config.js).

A `apiKey` do Firebase não é secreta: ela só identifica o projeto. Quem protege os dados são as regras do Firestore, que deixam cada pessoa ler e gravar apenas o próprio progresso.

## Estrutura

```
index.html            página única (rotas por #)
assets/site.css       estilos (tokens de cor, componentes)
assets/app.js         aplicação: trilhas, exercícios, simulado, sincronização
data/<trilha>.js      conteúdo gerado de cada trilha
firebase-config.js    configuração opcional do login
firestore.rules       regras de segurança do Firestore
tools/                fontes e gerador (python3 tools/build.py)
```

Para incluir uma nova trilha: adicione as fontes em `tools/src`, registre-a em `tools/build.py` e rode `python3 tools/build.py` (requer `pandoc` e `beautifulsoup4`).

## Créditos

Resumos, organização e curadoria do conteúdo: **Maria Paula Miranda da Silva**.
Conteúdo baseado nos cursos da Cisco Networking Academy. Projeto pessoal de estudo, sem vínculo com a Cisco.
