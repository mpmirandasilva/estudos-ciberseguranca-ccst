# Estudos de Cibersegurança · Certificação CCST

Material de estudo interativo, feito a partir dos meus roteiros de estudo dos cursos da Cisco Networking Academy e organizado em trilhas rumo à certificação **Cisco Certified Support Technician (CCST)**. O nome aponta para o objetivo maior, a cibersegurança: as trilhas 1 e 2 cobrem a prova **CCST Networking (100-150)**, e as trilhas 3 a 5 seguem o caminho para a **CCST Cybersecurity**, na ordem em que um conteúdo prepara o seguinte.

🔗 **Acesse:** https://mpmirandasilva.github.io/estudos-ciberseguranca-ccst/

## Trilhas

Cada resumo é uma trilha independente, com módulos, glossário, exercícios e progresso próprios.

| Trilha | Curso de origem | Módulos | Tópicos | Questões (estilo CCST) |
|---|---|---|---|---|
| Fundamentos de Redes de Computadores | Networking Basics | 20 | 146 | 263 (89) |
| Dispositivos de Rede e Configuração Inicial | Networking Devices and Initial Configuration | 13 | 70 | 194 (59) |
| Segurança de Endpoint | Endpoint Security | 30 | 189 | 121 (—) |
| Defesa de Rede | Network Defense | 30 | 181 | 140 (—) |
| Gerenciamento de Ameaças Cibernéticas | Cyber Threat Management | 17 | 101 | 77 (—) |
| **Total** | | **110** | **687** | **795 (148)** |

## Como funciona

- **Cards em sequência**: os tópicos começam fechados e se revelam ao clicar; o próximo só abre depois do anterior.
- **Exercícios por módulo**, em duas partes (nas trilhas 3 a 5, por enquanto, só a de fixação):
  - *fixação*: conceitos e cálculos (binário, máscaras, sub-redes, IPv6), corrigidos na hora;
  - *estilo CCST*: cenários de suporte, saídas de comandos para interpretar (`ipconfig`, `show ip route`, `tracert`, `netstat`…), questões de "escolha duas", associação e ordenação. Cada questão é marcada com o domínio do blueprint (1.0 a 6.0).
- **Prova CCST Cybersecurity** (`#prova`): as 200 questões da apostila da autora, com enunciados reescritos e explicações próprias. Depois de cada resposta aparecem a correção, a explicação e os tópicos das trilhas onde estudar o assunto; a nota (geral e por domínio do exame) só sai no fim, junto com um índice de estudo dos tópicos ligados às questões erradas. Banco em `tools/prova/` e `tools/prova_cyber.py`.
- **Simulado CCST**: 40 questões em 50 minutos (ou versão curta), sorteadas das trilhas 1 e 2 (as de redes), com resultado por domínio e correção comentada.
- **Grifos e edição pela autora**: com o login da conta definida em `ownerEmail` (no `firebase-config.js`), é possível grifar trechos em turquesa, apagar grifos (inclusive os originais do resumo) e editar o texto de cada tópico (negrito, itálico, grifo e listas), com opção de voltar ao original. As mudanças ficam no Firestore (`conteudo/<trilha>`) e aparecem para todos os visitantes; as regras em `firestore.rules` deixam só essa conta gravar.
- **Explicação em cada resposta**, com link para o item do material que deve ser revisado.
- **Padrão visual único**: figuras desenhadas em SVG (acompanham o tema claro e escuro), tabelas, terminais, notas e fluxos com o mesmo estilo em todas as trilhas.
- **Progresso salvo** no navegador e, com login Google, sincronizado entre aparelhos.

As questões são originais, escritas para este projeto a partir dos tópicos oficiais do exame. Não são questões reais da prova.

## Login e progresso (Firebase)

O site é estático (GitHub Pages), então o login usa o Firebase no plano gratuito (Spark), sem forma de pagamento cadastrada. O projeto `estudos-ccst` já está configurado:

- **Authentication** com o provedor Google, e `mpmirandasilva.github.io` entre os domínios autorizados;
- **Firestore** (região `southamerica-east1`, modo de produção) com as regras de [`firestore.rules`](firestore.rules): cada pessoa só lê e grava o próprio documento em `progresso/{uid}`;
- chaves públicas do app web em [`firebase-config.js`](firebase-config.js).

A `apiKey` do Firebase não é secreta: ela só identifica o projeto. Quem protege os dados são as regras do Firestore. Sem login, o progresso fica salvo apenas no navegador.

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

## Autoria

- **Idealização, roteiros e direção do projeto:** Maria Paula Miranda da Silva. Ela definiu o conteúdo, o modelo de resumo, a organização em trilhas e cada funcionalidade do site (cards em sequência, exercícios no estilo CCST, simulado, login, grifos, edição dos textos e padrão visual).
- **Desenvolvimento** (HTML, CSS, JavaScript, gerador em Python, figuras em SVG e questões no estilo CCST): feito com o [Claude](https://claude.ai), assistente de IA da Anthropic, seguindo as orientações dela. Por isso os commits aparecem com o autor "Claude".

Conteúdo baseado nos cursos da Cisco Networking Academy. Projeto pessoal de estudo, sem vínculo com a Cisco. Cisco, CCST e Networking Academy são marcas da Cisco Systems.
