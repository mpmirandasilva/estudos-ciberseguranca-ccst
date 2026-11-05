# Defesa de Rede

Nov 4, 2026 · Maria Paula

## 1. Fundamentos da Defesa de Redes

A **defesa de rede** é o conjunto de medidas, tecnologias e processos usados para **proteger os recursos de uma organização contra ataques** e para reagir rapidamente quando um ataque acontece.

Antes de escolher qualquer ferramenta, o profissional de segurança precisa saber três coisas: o que deve ser protegido, quais são os pontos fracos e quais perigos existem. Esta seção apresenta esses conceitos e os objetivos que toda defesa busca garantir.

### 1.1 Tríade CIA: Confidencialidade, Integridade e Disponibilidade

A **tríade CIA** (*Confidentiality, Integrity, Availability* — Confidencialidade, Integridade e Disponibilidade) reúne os **três objetivos principais da segurança da informação**. Toda medida de defesa estudada neste resumo protege pelo menos um deles.

| Objetivo | O que garante | Exemplo de ameaça |
| --- | --- | --- |
| Confidencialidade | Só pessoas autorizadas leem a informação | Funcionário de fora do RH abrindo a folha de pagamento |
| Integridade | A informação está completa e não foi alterada | Valor de uma transferência modificado no caminho |
| Disponibilidade | A informação e os serviços funcionam quando necessários | Servidor do site fora do ar por um ataque |

**Observação:** a sigla CIA vem do inglês e não tem relação com a agência de inteligência americana. Em português, também se usa **tríade CID**.

### 1.2 Ativos, Vulnerabilidades e Ameaças

Para se preparar contra qualquer tipo de ataque, o analista de segurança precisa identificar primeiro três elementos:

- **ativos**: qualquer coisa de valor para a organização que deve ser protegida, como servidores, dispositivos de infraestrutura, dispositivos finais e, principalmente, os **dados**, que são o maior ativo;
- **vulnerabilidades**: uma fraqueza em um sistema ou no seu projeto que pode ser explorada;
- **ameaças**: qualquer perigo potencial para um ativo.

Quem explora uma vulnerabilidade para atingir um ativo é chamado de **agente de ameaça** (ou ator de ameaça): um criminoso digital, um funcionário mal-intencionado, um grupo organizado.

O conjunto de todos os ativos de uma organização forma a sua **superfície de ataque**, isto é, tudo aquilo que um agente de ameaça pode tentar atingir. Quanto mais a organização cresce, maior fica a superfície de ataque.

**Importante:** é comum confundir vulnerabilidade com ameaça. A vulnerabilidade é o **ponto fraco** (uma senha padrão nunca trocada); a ameaça é o **perigo** que pode se aproveitar dele (alguém que tenta entrar com essa senha).

### 1.3 Gerenciamento de Ativos

O **gerenciamento de ativos** consiste em **inventariar todos os ativos e, em seguida, criar e aplicar políticas e procedimentos para protegê-los**. Muitas organizações só têm uma ideia geral do que precisam proteger, principalmente depois de fusões com outras empresas.

Também é preciso saber onde ficam os ativos de informação mais importantes e como se chega até eles. Cada tipo de negócio guarda ativos diferentes, que atraem agentes de ameaça diferentes.

Exemplos:

- uma loja guarda dados de cartão de crédito dos clientes;
- uma empresa de engenharia guarda projetos e softwares que interessam à concorrência;
- um banco guarda dados de contas e outras informações financeiras.

### 1.4 Classificação de Ativos

A **classificação de ativos** distribui todos os recursos da organização em **grupos com características comuns**. As informações mais importantes recebem o nível mais alto de proteção e podem exigir tratamento especial.

Para isso, a organização pode adotar um sistema de rótulos de acordo com o valor, a confidencialidade e a importância de cada informação. De forma simplificada, o processo ocorre em quatro etapas:

1. determinar a categoria de cada ativo: ativo de informação, de software, físico ou serviço;
2. estabelecer a responsabilidade, identificando o **proprietário** de cada ativo de informação e de cada software de aplicação;
3. definir os critérios de classificação: confidencialidade, valor, tempo, direitos de acesso e destruição;
4. implementar um esquema de classificação, isto é, uma forma uniforme de identificar as informações para que todas recebam a mesma proteção.

### 1.5 Padronização de Ativos

Os **padrões de ativos** definem **quais produtos de hardware e software a organização usa e dá suporte**.

Sem padronização, é difícil encontrar uma peça de reposição quando algo falha, a equipe precisa conhecer muitos produtos diferentes e os custos de manutenção e de inventário aumentam. Com padronização, a substituição é rápida e o acesso e a segurança se mantêm.

### 1.6 Ciclo de Vida dos Ativos

Todo ativo passa por um **ciclo de vida**, e cabe ao profissional de segurança protegê-lo em todas as etapas:

Aquisição → Implantação → Utilização → Manutenção → Descarte

| Etapa | O que acontece |
| --- | --- |
| Aquisição | O ativo é comprado conforme uma necessidade comprovada e entra no inventário |
| Implantação | O ativo é montado, inspecionado, testado e recebe etiquetas ou código de barras para rastreamento |
| Utilização | É a fase mais longa: o desempenho é verificado e recebe atualizações, correções, licenças e auditorias |
| Manutenção | O ativo é ajustado ou atualizado para prolongar sua vida útil |
| Descarte | Todos os dados são apagados e as peças com risco ambiental seguem as regras locais |

**Importante:** no descarte, apagar os dados é obrigatório. Um disco vendido ou jogado fora com dados ainda gravados é uma porta para vazamentos.

### 1.7 Identificação de Ameaças e de Vulnerabilidades

A **identificação de ameaças** produz uma **lista das ameaças prováveis para um ambiente específico**. Para montá-la, a organização responde a três perguntas:

- quais são as possíveis vulnerabilidades do sistema?
- quem pode querer explorar essas vulnerabilidades para chegar a quais ativos?
- quais são as consequências se as vulnerabilidades forem exploradas e os ativos forem perdidos?

Já a **identificação de vulnerabilidades** exige conhecer os aplicativos importantes da rede e as fraquezas desses aplicativos e do hardware, o que costuma demandar bastante pesquisa.

#### 1.7.1 Exemplo Resolvido: Ameaças a um Sistema de Banco On-line

Para um sistema de banco pela internet, a lista de ameaças incluiria:

- comprometimento interno: o atacante usa os servidores do banco expostos à internet para invadir o sistema interno;
- roubo de dados de clientes: dados pessoais e financeiros são copiados do banco de dados;
- transações falsas a partir de um servidor externo: o atacante altera o código do aplicativo e faz transações se passando por um cliente;
- transações falsas com PIN ou cartão roubado: o atacante usa a identidade de um cliente;
- ataque interno (*insider*): um funcionário encontra uma falha e a usa para atacar;
- erros de entrada de dados: um usuário digita dados ou pedidos incorretos;
- destruição do data center: um evento grave, como incêndio ou enchente, danifica o local.

**Observação:** nem toda ameaça é um ataque. Erros de digitação e desastres naturais também entram na lista, porque também afetam a integridade e a disponibilidade.

## 2. Defesa em Profundidade

A **defesa em profundidade** é a abordagem que **usa várias camadas de segurança na borda da rede, dentro da rede e nos dispositivos finais**, de modo que a falha de uma proteção não comprometa as outras.

A ideia é simples: se a organização tem uma única barreira, o criminoso digital só precisa vencê-la para chegar aos dados. Com várias camadas, cada uma diferente da anterior, ele encontra um novo obstáculo a cada passo.

### 2.1 Camadas de uma Rede Protegida

Na topologia mais simples de defesa em profundidade, o tráfego que chega da internet atravessa três linhas de defesa antes de alcançar a rede interna (LAN):

Internet → Roteador de borda → Firewall → Roteador interno → Rede interna

| Linha de defesa | Função |
| --- | --- |
| Roteador de borda | Primeira linha: aplica regras que permitem ou negam tráfego e repassa ao firewall o que se destina à rede interna |
| Firewall | Segunda linha: faz uma filtragem adicional e acompanha o estado das conexões |
| Roteador interno | Última linha: aplica as regras de filtragem finais antes de entregar o tráfego ao destino |

O **firewall** é um dispositivo de controle que fica entre redes e decide qual tráfego pode passar. Na posição de segunda linha, ele **nega conexões iniciadas na rede externa (não confiável) em direção à rede interna (confiável)**, mas permite que os usuários internos abram conexões com a internet e recebam as respostas. Ele também pode exigir que usuários remotos se autentiquem antes de acessar recursos internos. Um exemplo de firewall dedicado é o Cisco ASA.

Roteadores e firewalls não são as únicas camadas. Outros dispositivos de segurança incluem:

- sistemas de prevenção de intrusão (**IPS**, *Intrusion Prevention System*), que analisam o tráfego em busca de ataques e os bloqueiam;
- proteção avançada contra malware (**AMP**, *Advanced Malware Protection*);
- sistemas de segurança de conteúdo web e de e-mail;
- serviços de identidade e controle de acesso à rede.

### 2.2 A Cebola e a Alcachofra da Segurança

Duas analogias são usadas para descrever a defesa em profundidade.

Na **cebola de segurança**, o agente de ameaça precisa **descascar as defesas camada por camada** para chegar aos dados, que ficam no centro. As camadas típicas, de fora para dentro, são: firewall, IPS, filtragem de conteúdo, autenticação e controle de acesso e dispositivos reforçados (configurados de forma segura).

Com as **redes sem fronteiras**, em que funcionários acessam a rede de celulares, de casa e da nuvem, a analogia mudou para a **alcachofra de segurança**. Agora o agente de ameaça **não precisa remover todas as camadas, basta arrancar algumas folhas**. Cada folha pode revelar dados mal protegidos e abrir caminho até o “coração”, onde estão os dados mais confidenciais.

Exemplos de folhas: senhas, ataques ao lado do cliente, bancos de dados, aplicativos web e estouros de buffer. Um celular de funcionário, por exemplo, costuma ser mais fácil de comprometer do que um servidor interno cercado de defesas.

| Característica | Cebola | Alcachofra |
| --- | --- | --- |
| Cenário | Rede com perímetro bem definido | Rede sem fronteiras |
| Caminho do atacante | Atravessar todas as camadas | Remover só algumas folhas |
| Quem se beneficia da mudança | — | O agente de ameaça |

**Importante:** a “cebola de segurança” desta seção é só uma forma de visualizar camadas. Não confundir com o **Security Onion**, um conjunto de ferramentas de monitoramento de rede.

### 2.3 Estratégias de Defesa em Profundidade

Para que as camadas realmente protejam, a organização combina cinco estratégias:

| Estratégia | Ideia central | Exemplo |
| --- | --- | --- |
| Sobreposição (camadas) | Várias defesas, cada uma mais difícil de vencer | Documento em servidor com senha, num prédio trancado e cercado |
| Limitação | Cada pessoa tem só o acesso necessário ao trabalho | Documentos sigilosos só consultados em sala com câmeras |
| Diversidade | Camadas diferentes entre si | Crachá de um fabricante e leitor de digital de outro |
| Ofuscação | Não revelar detalhes que ajudem o atacante | Mensagem de erro sem a versão do sistema operacional |
| Simplicidade | Simples por dentro, complexo por fora | Configuração que a equipe entende e mantém corretamente |

A diversidade importa porque, se todas as camadas fossem iguais, a mesma técnica que vence uma venceria todas. Por esse motivo, usa-se, por exemplo, algoritmos de criptografia ou sistemas de autenticação diferentes em cada camada.

**Observação:** complexidade não é sinônimo de segurança. Uma solução tão complicada que a equipe não consegue configurar direito pode ser tão fácil de invadir quanto uma solução fraca.

**Importante:** a defesa em profundidade não cria um escudo impenetrável. Ela **reduz o risco e mantém a organização um passo à frente** dos criminosos.

## 3. Gerenciamento de Operações de Segurança

O **gerenciamento de operações de segurança** reúne os processos do dia a dia que mantêm a rede segura: **controlar as configurações dos sistemas, registrar o que acontece neles e observar o tráfego**.

### 3.1 Gerenciamento de Configuração

O **gerenciamento de configuração** é a **identificação, o controle e a auditoria da implantação de um sistema e de qualquer alteração feita na sua linha de base**.

A **linha de base** (*baseline*) é o conjunto de configurações definidas para um sistema que serve de **modelo para todos os sistemas semelhantes**. Exemplo: todas as estações Windows de uma empresa saem com os mesmos aplicativos e as mesmas configurações, conforme um documento padrão.

Entre os recursos de configuração que devem ser documentados estão:

- mapas de rede, diagramas de cabeamento e especificações de configuração dos aplicativos;
- convenções de nomes usadas para os computadores;
- esquema de endereçamento IP, para rastrear os endereços em uso.

### 3.2 Reforço do Sistema Operacional

O **reforço** (*hardening*) do sistema operacional é o processo de **configurá-lo de forma segura, reduzindo as brechas que um atacante poderia usar**. As principais medidas são:

- configurar arquivos de log e auditoria;
- alterar nomes de conta e senhas padrão;
- aplicar políticas de conta;
- aplicar controle de acesso no nível de arquivo.

### 3.3 Arquivos de Log

Um **log** (registro) é o **registro dos eventos que ocorrem em um sistema**. Cada **entrada de log** guarda todas as informações sobre um evento específico, e o conjunto das entradas forma o **arquivo de log**.

Exemplos:

- log de auditoria: registra as tentativas de autenticação dos usuários;
- log de acesso: registra os pedidos feitos a arquivos específicos.

Analisando os logs, é possível descobrir **como um ataque aconteceu e se as defesas funcionaram**. Como os sistemas geram cada vez mais logs, a organização precisa de um processo de gerenciamento de logs que defina os procedimentos para cada etapa:

Gerar → Transmitir → Armazenar → Analisar → Descartar

Os logs vêm de duas fontes principais:

| Fonte | O que registra | Para que serve |
| --- | --- | --- |
| Sistema operacional | Pedidos de clientes e respostas do servidor (como autenticações bem-sucedidas) e informações de uso (número e tamanho das transações em um período) | Acompanhar a operação do sistema |
| Software de segurança | Atividades mal-intencionadas detectadas na rede ou no sistema | Auditoria, identificação de tendências e de problemas de longo prazo, comprovação de que a empresa cumpre leis e regulamentos |

### 3.4 Analisadores de Pacotes

Um **analisador de pacotes** (*packet analyzer* ou *sniffer*) **intercepta e registra o tráfego da rede**, com ou sem fio. Ele captura cada pacote, mostra o valor de cada campo e analisa o conteúdo. Exemplos conhecidos são o Wireshark e o tcpdump.

Entre suas principais funções estão:

- registrar o tráfego;
- analisar problemas de rede;
- detectar uso indevido da rede;
- detectar tentativas de invasão;
- isolar um sistema que foi explorado.

**Importante:** a mesma ferramenta que ajuda o defensor também ajuda o atacante. Um criminoso com um sniffer na rede consegue ler tudo o que trafega sem criptografia, inclusive senhas.

## 4. Políticas, Regulamentos e Padrões

As **políticas** são as regras que a própria organização cria para orientar o comportamento; os **regulamentos** são regras externas, como leis, que ela é obrigada a cumprir. Juntos, **definem o que é permitido e o que é proibido** na rede e nos dados.

### 4.1 Políticas de Negócios

As **políticas de negócios** são diretrizes desenvolvidas pela organização para governar suas ações. Na rede, elas definem as atividades permitidas e formam uma **linha de base de uso aceitável**.

Por esse motivo, um comportamento que viola a política e é detectado na rede pode indicar que **ocorreu uma violação de segurança**.

As organizações costumam ter três tipos de política:

| Política | O que define | Exemplos |
| --- | --- | --- |
| Da empresa | Regras de conduta e responsabilidades de funcionários e empregadores | Assiduidade, vestimenta, privacidade |
| De funcionários | Itens criados e mantidos pelo RH, assinados na contratação | Salário, pagamento, benefícios, horário, férias |
| De segurança | Objetivos de segurança, regras para usuários e administradores e requisitos dos sistemas | Senhas, acesso remoto, uso aceitável |

**Observação:** assim como um plano de continuidade, a política de segurança é um documento **em constante evolução**, atualizado conforme mudam as ameaças, as vulnerabilidades e as necessidades do negócio.

### 4.2 Política de Segurança

A **política de segurança** informa usuários, funcionários e gerentes sobre os requisitos para proteger os ativos de tecnologia e de informação. Ela também especifica os mecanismos necessários e serve de linha de base para comprar, configurar e auditar sistemas.

Entre os principais benefícios de uma política de segurança abrangente estão:

- demonstrar o compromisso da organização com a segurança;
- definir as regras para o comportamento esperado;
- garantir consistência na operação, na compra, no uso e na manutenção de hardware e software;
- definir as consequências legais das violações;
- dar à equipe de segurança o apoio da direção.

Uma política de segurança pode reunir várias políticas menores:

| Política | O que especifica |
| --- | --- |
| Identificação e autenticação | Quem pode acessar os recursos e como a identidade é verificada |
| Senhas | Requisitos mínimos das senhas e a troca regular |
| Uso aceitável (AUP) | Aplicativos e usos da rede aceitáveis e as consequências da violação |
| Acesso remoto | Como usuários remotos acessam a rede e o que podem acessar |
| Manutenção de rede | Procedimentos para atualizar os sistemas dos dispositivos de rede e os aplicativos |
| Tratamento de incidentes | Como os incidentes de segurança são tratados |

### 4.3 Política de Uso Aceitável (AUP)

A **AUP** (*Acceptable Use Policy* — Política de Uso Aceitável), também chamada de política de uso apropriado, é um dos componentes mais comuns da política de segurança. Ela define **o que os usuários podem ou não fazer nos sistemas**, incluindo o tipo de tráfego permitido na rede.

A AUP deve ser **o mais explícita possível**, para evitar mal-entendidos. Exemplo: listar sites e aplicativos de alto consumo de banda que não podem ser acessados pelos computadores da empresa.

**Importante:** todo funcionário deve assinar a AUP, e a versão assinada fica guardada durante todo o período do emprego.

### 4.4 Políticas de BYOD

O **BYOD** (*Bring Your Own Device* — Traga seu Próprio Dispositivo) permite que os funcionários usem **seus próprios aparelhos para acessar sistemas, redes e informações da empresa**.

O BYOD traz benefícios, como mais produtividade, menos custos de TI, mais mobilidade e mais atração na hora de contratar. Em contrapartida, aumenta o risco de **vazamento de dados** e a responsabilidade da empresa.

Por esse motivo, a política de BYOD deve:

- especificar os objetivos do programa;
- identificar quais funcionários podem trazer dispositivos e quais dispositivos são aceitos;
- definir o nível de acesso concedido aos dispositivos pessoais;
- descrever o que a equipe de segurança pode fazer no dispositivo;
- indicar quais regulamentos devem ser cumpridos;
- definir as medidas a tomar se um dispositivo for comprometido.

As boas práticas de BYOD estão resumidas na tabela:

| Prática | O que fazer |
| --- | --- |
| Acesso protegido por senha | Usar uma senha diferente para cada dispositivo e conta |
| Controle manual do sem fio | Desligar Wi-Fi e Bluetooth quando não estiverem em uso e conectar-se só a redes confiáveis |
| Atualização | Manter o sistema e os aplicativos atualizados, com as correções de segurança |
| Backup | Ativar o backup para o caso de perda ou roubo |
| “Localizar meu dispositivo” | Usar um serviço de localização com apagamento remoto |
| Antivírus | Fornecer antivírus para os dispositivos aprovados |
| MDM | Usar software de gerenciamento de dispositivos móveis |

O **MDM** (*Mobile Device Management* — Gerenciamento de Dispositivos Móveis) é o software que permite à equipe de TI **aplicar configurações de segurança e de software em todos os dispositivos que se conectam à rede da empresa**.

### 4.5 Conformidade com Regulamentos e Padrões

Além das políticas internas, existem regulamentos externos de segurança. Os **regulamentos de conformidade** definem **pelo que a organização é responsável e quais são as consequências se ela não cumprir**.

Os regulamentos que se aplicam dependem do tipo de organização e dos dados que ela trata. No Brasil, por exemplo, toda empresa que trata dados pessoais deve seguir a LGPD (Lei Geral de Proteção de Dados).

Os profissionais de segurança também precisam conhecer as leis e os códigos de ética que se aplicam aos profissionais de segurança de sistemas de informação (**INFOSEC**).

## 5. Criptografia e Confidencialidade

A **criptografia** é a técnica de **embaralhar os dados para que só quem conhece o segredo certo consiga lê-los**. Ela é a principal ferramenta para garantir a confidencialidade e aparece em quase todas as defesas deste resumo: acesso remoto seguro, sites com HTTPS, redes sem fio e VPNs.

### 5.1 Conceitos Básicos de Criptografia

Os dados legíveis são chamados de **texto claro** (*plaintext*); depois de criptografados, viram **texto cifrado** (*ciphertext*), uma mensagem ilegível. O processo de volta, que transforma o texto cifrado em texto claro, é a **descriptografia**.

Texto claro → Criptografia (com a chave) → Texto cifrado → Descriptografia (com a chave) → Texto claro

A **chave** é o valor secreto usado pelo algoritmo para criptografar e descriptografar. **Quem tem a chave certa consegue transformar o texto cifrado de volta em texto claro.** Quanto maior a chave, mais tempo um atacante leva para descobri-la por tentativa.

De acordo com a forma como usam as chaves, os algoritmos de criptografia são classificados em duas categorias:

- **simétricos**: usam a mesma chave para criptografar e descriptografar;
- **assimétricos**: usam um par de chaves diferentes, uma para cada operação.

### 5.2 Estados dos Dados

Os dados precisam ser protegidos em **três estados**:

| Estado | Situação | Exemplo |
| --- | --- | --- |
| Em repouso | Armazenados, sem ninguém acessando ou alterando | Arquivo no disco de um servidor ou na nuvem |
| Em trânsito | Sendo transmitidos | Mensagem viajando pela internet |
| Em processamento | Sendo inseridos, modificados, calculados ou exibidos | Planilha aberta sendo editada |

**Observação:** a criptografia protege principalmente os dados em repouso e em trânsito. Na nuvem, proteger os dados em trânsito é essencial, porque eles passam o tempo todo pela internet.

### 5.3 Criptografia Simétrica

Na **criptografia simétrica**, **as duas partes usam a mesma chave**, chamada de **chave pré-compartilhada** ou chave secreta. Essa chave precisa ser combinada **antes** de qualquer comunicação criptografada.

Uma analogia ajuda: Alice e Bob têm cópias idênticas da chave de um mesmo cadeado. Alice coloca a mensagem numa caixa, tranca e envia pelo correio. A caixa viaja trancada, e só Bob, que tem a outra cópia da chave, consegue abri-la.

Os algoritmos simétricos gastam pouco processamento e por isso são rápidos. Por esse motivo, são usados para **criptografar grandes volumes de dados**, como o tráfego de uma VPN (rede privada virtual, que cria um túnel protegido pela internet).

**Importante:** a maioria das chaves simétricas tem entre 112 e 256 bits. Para que a criptografia seja segura, deve-se usar **no mínimo 128 bits**.

Os algoritmos simétricos podem funcionar de duas formas:

- **cifra de bloco**: criptografa o texto em blocos de tamanho fixo, de 64 ou 128 bits; exemplos: DES (bloco de 64 bits) e AES (bloco de 128 bits);
- **cifra de fluxo**: criptografa um byte ou um bit de cada vez, continuamente, e por isso costuma ser mais rápida; exemplos: RC4 e A5, usado nas chamadas de celular GSM.

Os algoritmos simétricos mais conhecidos são:

| Algoritmo | Características | Situação |
| --- | --- | --- |
| DES (*Data Encryption Standard*) | Chave curta | Legado, inseguro, não usar |
| 3DES (Triple DES) | Repete o DES três vezes | Evitar; descontinuado pelo NIST desde 2023 |
| AES (*Advanced Encryption Standard*) | Bloco de 128 bits; chaves de 128, 192 ou 256 bits | Recomendado; usado pelo governo dos EUA |
| SEAL (*Software-Optimized Encryption Algorithm*) | Cifra de fluxo, chave de 160 bits, pouco uso de processador | Alternativa mais rápida ao AES |
| RC4 (série Rivest Ciphers) | Cifra de fluxo, criada por Ron Rivest | Vulnerável, não usar |

**Observação:** no AES, o que varia é o tamanho da **chave** (128, 192 ou 256 bits); o **bloco** é sempre de 128 bits.

### 5.4 Criptografia Assimétrica

Na **criptografia assimétrica**, também chamada de **criptografia de chave pública**, cada participante tem **um par de chaves**: uma **chave pública**, que pode ser divulgada a qualquer pessoa, e uma **chave privada**, que só o dono conhece.

As duas chaves são complementares: **o que uma chave criptografa, só a outra do mesmo par descriptografa**. Além disso, não é possível calcular a chave privada a partir da pública em um tempo razoável.

Como as partes não compartilham um segredo, as chaves precisam ser muito longas: entre 512 e 4.096 bits. Chaves de **2.048 bits ou mais** são consideradas confiáveis; chaves de 1.024 bits ou menos, insuficientes.

Os algoritmos assimétricos se baseiam em problemas matemáticos muito difíceis, como fatorar números enormes. Por isso são **bem mais lentos** que os simétricos e são usados em operações de pouco volume: **troca de chaves e assinaturas digitais**. Em compensação, o gerenciamento das chaves é mais simples, porque uma delas pode ser pública.

Exemplos de protocolos que usam algoritmos assimétricos:

- IKE (*Internet Key Exchange*): troca de chaves nas VPNs IPsec;
- SSL/TLS: protege a navegação em sites (HTTPS);
- SSH: acesso remoto seguro a dispositivos de rede;
- PGP (*Pretty Good Privacy*): privacidade e autenticação em e-mails.

Os algoritmos assimétricos mais comuns são:

| Algoritmo | Tamanho de chave (bits) | Características |
| --- | --- | --- |
| Diffie-Hellman (DH) | 512 a 4.096 | Permite que duas partes combinem uma chave secreta |
| DSA (*Digital Signature Algorithm*) | 512 a 1.024 | Algoritmo de assinatura digital do padrão DSS; verificação de 10 a 40 vezes mais lenta que a do RSA |
| RSA (Rivest, Shamir e Adleman) | 512 a 4.096 (hoje, pelo menos 2.048) | Baseado na dificuldade de fatorar números grandes; o primeiro a servir para assinatura e para criptografia |
| ElGamal | 512 a 1.024 | Baseado no Diffie-Hellman; a mensagem cifrada fica com cerca do dobro do tamanho, então é usado só para mensagens pequenas, como chaves |
| Curvas elípticas (ECC) | 224 ou mais | Adapta outros algoritmos (DH, ElGamal) com chaves muito menores |

### 5.5 Confidencialidade e Autenticação com Chaves Assimétricas

O resultado depende de qual chave é usada para criptografar:

| Objetivo | Criptografa com | Descriptografa com | Por que funciona |
| --- | --- | --- | --- |
| Confidencialidade | Chave **pública** do destinatário | Chave **privada** do destinatário | Só o destinatário tem a chave privada, então só ele lê |
| Autenticação | Chave **privada** do remetente | Chave **pública** do remetente | Só o remetente poderia ter criptografado com aquela chave |

De forma simplificada, as duas regras são:

- Chave pública (criptografar) + chave privada (descriptografar) → confidencialidade;
- Chave privada (criptografar) + chave pública (descriptografar) → autenticação.

#### 5.5.1 Exemplo Resolvido: Alice Envia uma Mensagem Sigilosa a Bob

1. Alice pede e recebe a chave pública de Bob;
2. Alice criptografa a mensagem com a chave pública de Bob e a envia;
3. Bob descriptografa com a própria chave privada. Como só Bob tem essa chave, só ele pode ler a mensagem.

Se Alice quisesse provar que foi ela quem escreveu, faria o contrário: criptografaria com a própria chave privada, e Bob conferiria com a chave pública de Alice.

**Importante:** se uma chave privada for comprometida, todo o par deve ser substituído por um novo.

### 5.6 Diffie-Hellman

O **Diffie-Hellman (DH)** é um algoritmo assimétrico que permite que **dois computadores gerem o mesmo segredo compartilhado sem nunca terem se comunicado antes e sem que esse segredo seja enviado pela rede**. É usado, por exemplo, nas VPNs IPsec e no SSH.

#### 5.6.1 Exemplo Resolvido: a Analogia das Cores

No lugar dos números enormes, imagine tintas:

1. Alice e Bob combinam uma cor comum, que não precisa ser secreta: amarelo;
2. cada um escolhe uma cor secreta, que nunca será revelada: Alice, vermelho; Bob, azul;
3. cada um mistura o amarelo com a sua cor secreta e obtém uma cor pública: Alice obtém laranja; Bob, verde;
4. os dois trocam as cores públicas: Alice envia o laranja, Bob envia o verde;
5. cada um mistura a cor recebida com a própria cor secreta: Alice mistura verde + vermelho; Bob, laranja + azul;
6. os dois chegam ao mesmo marrom, que representa a chave secreta compartilhada.

Quem interceptar a troca só vê o amarelo, o laranja e o verde, e não consegue chegar ao marrom.

Na prática, o DH trabalha com números gigantes: um número de 1.024 bits tem cerca de 309 dígitos decimais. A força da chave é definida pelo **grupo DH**; quanto maior o grupo, mais seguro e mais demorado o cálculo.

| Grupo DH | Tamanho |
| --- | --- |
| 1 | 768 bits |
| 2 | 1.024 bits |
| 5 | 1.536 bits |
| 14 | 2.048 bits |
| 15 | 3.072 bits |
| 16 | 4.096 bits |
| 19 e 20 | Baseados em curvas elípticas |

### 5.7 Resumo de Criptografia Simétrica e Assimétrica

| Característica | Simétrica | Assimétrica |
| --- | --- | --- |
| Chaves | A mesma para criptografar e descriptografar | Par de chaves: pública e privada |
| Tamanho da chave | Curto: 40 a 256 bits | Longo: 512 a 4.096 bits |
| Velocidade | Rápida | Lenta |
| Uso típico | Grandes volumes de dados, como VPN | Troca de chaves e assinaturas digitais |
| Exemplos | AES, 3DES, SEAL | RSA, DH, DSA, ECC |

**Importante:** na prática, as duas são usadas juntas. O algoritmo assimétrico (como o DH) cria ou troca a chave com segurança, e o **algoritmo simétrico (como o AES) criptografa o grande volume de dados** com essa chave.

## 6. Hash, Integridade e Autenticidade

A criptografia garante que ninguém leia os dados, mas não garante que eles chegaram sem alteração nem que vieram de quem diz ter enviado. Para isso existem o **hash** e o **HMAC**, que garantem a **integridade e a autenticidade** das mensagens.

### 6.1 Elementos das Comunicações Seguras

As comunicações seguras se apoiam em **quatro elementos**:

| Elemento | O que garante | Como é obtido |
| --- | --- | --- |
| Integridade dos dados | A mensagem não foi alterada no caminho | Hash (SHA-2 ou SHA-3) |
| Autenticação de origem | A mensagem vem de quem diz ter enviado | HMAC |
| Confidencialidade | Só usuários autorizados leem a mensagem | Criptografia simétrica e assimétrica |
| Não repúdio | O remetente não pode negar que enviou | Assinatura digital |

A tendência atual é que **toda comunicação seja criptografada**, inclusive o tráfego interno da organização.

### 6.2 Funções Hash

Uma **função hash** recebe dados de qualquer tamanho, chamados de mensagem, e produz uma **representação de tamanho fixo**, chamada de **hash** (também *digest*, resumo ou impressão digital). Matematicamente, escreve-se h = H(x): a função H recebe a entrada x e devolve o valor h.

A função hash é **unidirecional**: é fácil calcular o hash, mas praticamente impossível fazer o caminho de volta. A moagem de café é uma boa analogia: moer os grãos é fácil, mas ninguém consegue juntar o pó e reconstruir os grãos originais.

Entre suas principais características estão:

- a entrada pode ter qualquer tamanho;
- a saída tem sempre o mesmo tamanho;
- o cálculo é rápido para qualquer entrada;
- é unidirecional e não pode ser revertida;
- é livre de colisões: duas entradas diferentes **praticamente nunca geram o mesmo hash**.

Por esse motivo, **qualquer alteração nos dados, por menor que seja, muda o hash**. Isso permite detectar arquivos duplicados, mudanças de versão e dados corrompidos.

### 6.3 Algoritmos de Hash

| Algoritmo | Tamanho do hash | Situação |
| --- | --- | --- |
| MD5 (criado por Ron Rivest) | 128 bits | Legado e inseguro; usar só se não houver alternativa |
| SHA-1 (criado pela NSA) | 160 bits | Antigo, com falhas conhecidas; evitar |
| SHA-2 (criado pela NSA) | SHA-224, SHA-256, SHA-384 e SHA-512 | Seguro; preferir SHA-256 ou maior |
| SHA-3 (padronizado pelo NIST) | SHA3-224, SHA3-256, SHA3-384 e SHA3-512 | O mais novo; sucessor do SHA-2; usar sempre que possível |

A sigla **SHA** significa *Secure Hash Algorithm* (Algoritmo de Hash Seguro). O **NIST** é o instituto de padrões dos EUA, e a **NSA**, a agência de segurança nacional dos EUA.

**Importante:** para escolher um hash hoje, use **SHA-256 ou superior**. MD5 e SHA-1 devem ser evitados.

### 6.4 Verificação de Integridade com Hash

A verificação de integridade compara dois hashes: o calculado antes e o calculado depois da transmissão. De forma simplificada, o processo ocorre da seguinte maneira:

1. o remetente passa a mensagem pela função hash e obtém o hash;
2. o hash é anexado à mensagem, e os dois são enviados;
3. o destinatário separa o hash e calcula de novo o hash da mensagem recebida;
4. se os dois forem iguais, a mensagem não foi alterada; se forem diferentes, a integridade não é mais confiável.

Exemplo: a mensagem “Pagar a Alex US$ 100” gera o hash 4ehiDx67NMop9. Se no caminho ela virar “Pagar a Jeremy US$ 1.000”, o destinatário calcula 12ehqPx67NMoX, percebe que os hashes são diferentes e descarta a mensagem.

O **checksum** (soma de verificação) é uma forma simples dessa ideia: converte os dados em um valor numérico e o soma; o receptor repete a conta e compara.

O hash é usado em várias situações do dia a dia da segurança:

- **downloads**: a Cisco publica o hash MD5 e SHA de cada imagem do sistema dos seus equipamentos; basta comparar com o hash do arquivo baixado para ter certeza de que ele não foi modificado;
- **perícia forense**: o perito cria uma cópia bit a bit da mídia e calcula o hash das duas; hashes iguais provam que a cópia é idêntica, e a análise é feita na cópia, deixando o original intacto.

### 6.5 Limitação do Hash

O hash detecta alterações **acidentais**, mas **não protege contra alterações deliberadas**. Isso acontece porque o hash não carrega nenhuma informação que identifique o remetente: qualquer pessoa com a mesma função consegue calculá-lo.

Um atacante no meio do caminho pode interceptar a mensagem, alterá-la, calcular um novo hash e anexá-lo. O destinatário confere o hash recebido, que bate, e aceita a mensagem falsa. Esse tipo de ataque, em que o criminoso se coloca entre as duas partes, é chamado de **ataque *man-in-the-middle* (MitM)**, ou homem no meio.

**Importante:** o hash sozinho **é vulnerável ao ataque man-in-the-middle**. Para garantir também a origem, é preciso acrescentar uma chave secreta: o HMAC.

### 6.6 HMAC

O **HMAC** (*Hash-based Message Authentication Code* — Código de Autenticação de Mensagem Baseado em Hash) é um hash calculado **a partir da mensagem e de uma chave secreta que só o remetente e o destinatário conhecem**.

Como o resultado depende da chave, um atacante que altere a mensagem não consegue gerar um HMAC válido. Assim, o HMAC garante ao mesmo tempo a **integridade e a autenticação da origem**.

De forma simplificada, o processo ocorre da seguinte maneira:

1. o remetente passa a mensagem e a chave secreta pela função hash e obtém o HMAC;
2. o HMAC é anexado à mensagem e enviado;
3. o destinatário calcula o HMAC da mensagem recebida com a mesma chave secreta;
4. se os valores forem iguais, a mensagem está íntegra e veio de quem tem a chave; se forem diferentes, é descartada.

O HMAC é usado em SSL/TLS, IPsec e SSH. Outro exemplo é a autenticação do protocolo de roteamento OSPF entre roteadores Cisco:

1. o roteador R1 calcula o hash da atualização de rotas junto com a chave secreta;
2. R1 envia a atualização e o hash para o roteador R2;
3. R2 calcula o hash com a sua chave e só aceita a atualização se os valores coincidirem.

| Característica | Hash | HMAC |
| --- | --- | --- |
| Entrada | Só a mensagem | Mensagem + chave secreta |
| Quem consegue calcular | Qualquer pessoa | Só quem tem a chave |
| Garante | Integridade contra alterações acidentais | Integridade e autenticação da origem |
| Resiste ao man-in-the-middle | Não | Sim |

### 6.7 Hash de Senhas

Os sistemas não devem guardar as senhas dos usuários. Em vez disso, **guardam apenas o hash da senha**. No login, o sistema calcula o hash da senha digitada e compara com o hash guardado; se forem iguais, a senha está correta.

Como o hash não pode ser revertido, o atacante que rouba o banco de hashes precisa **adivinhar** as senhas. Os dois ataques principais são:

- **ataque de dicionário**: usa um arquivo de palavras e senhas comuns com os hashes já calculados e compara com os hashes roubados;
- **ataque de força bruta**: testa todas as combinações possíveis de caracteres até um certo tamanho; consome muito tempo e processamento, por isso a senha precisa ser longa.

#### 6.7.1 Salt

Se dois usuários têm a mesma senha, eles teriam o mesmo hash. O **salt** resolve isso: é uma **sequência aleatória acrescentada à senha antes do cálculo do hash**, o que gera hashes diferentes mesmo para senhas iguais.

O banco de dados guarda o hash e o salt de cada usuário. O salt não precisa ser secreto, porque é só um número aleatório. A melhor forma de gerá-lo é um **CSPRNG** (*Cryptographically Secure Pseudo-Random Number Generator* — gerador de números pseudoaleatórios criptograficamente seguro), que produz números imprevisíveis.

As boas práticas de salt são:

- o salt deve ser exclusivo para cada senha;
- nunca reutilizar um salt;
- o tamanho do salt deve ser igual ao tamanho da saída da função hash;
- em aplicativos web, calcular o hash sempre no servidor.

Para guardar uma senha:

1. gerar um salt longo e aleatório com CSPRNG;
2. acrescentar o salt no início da senha;
3. calcular o hash com SHA-256;
4. salvar o salt e o hash no registro do usuário.

Para validar uma senha:

1. buscar o salt e o hash do usuário no banco de dados;
2. acrescentar o salt à senha digitada e calcular o hash com a mesma função;
3. comparar com o hash guardado; se forem diferentes, a senha está incorreta.

O salt torna inúteis as tabelas preparadas com antecedência pelos atacantes:

| Tabela | Como funciona |
| --- | --- |
| Tabela de pesquisa | Guarda hashes pré-calculados de um dicionário, junto com a senha de cada um |
| Tabela de pesquisa reversa | Liga cada hash do banco roubado à lista de usuários que o usam; um único palpite revela todos com a mesma senha |
| Tabela rainbow | Ocupa menos espaço que a tabela de pesquisa, em troca de quebrar as senhas mais devagar |

**Observação:** outra técnica de proteção é o **alongamento de chave** (*key stretching*), que torna cada tentativa de descobrir a senha muito lenta e reduz a vantagem de computadores que calculam bilhões de hashes por segundo.

## 7. Assinaturas Digitais e Infraestrutura de Chave Pública (PKI)

A **assinatura digital** combina o hash e a criptografia assimétrica para provar quem enviou uma mensagem e que ela não foi alterada. Para que todos confiem nas chaves públicas usadas nessa prova, existe a **infraestrutura de chave pública (PKI)**.

### 7.1 Assinatura Digital

A **assinatura digital** é uma técnica matemática que garante **autenticidade, integridade e não repúdio**. Ela serve como **prova legal** de que a troca de dados aconteceu.

Entre suas principais características estão:

- autêntica: não pode ser falsificada e prova que o signatário, e ninguém mais, assinou;
- inalterável: depois de assinado, o documento não pode ser modificado;
- não reutilizável: a assinatura não pode ser transferida para outro documento;
- não repudiável: o documento assinado vale como um documento físico assinado pela pessoa.

O **DSS** (*Digital Signature Standard*) é o padrão de assinatura digital e admite três algoritmos:

- **DSA**: o padrão original para gerar o par de chaves e gerar e verificar assinaturas;
- **RSA**: algoritmo assimétrico muito usado para gerar e verificar assinaturas;
- **ECDSA** (*Elliptic Curve Digital Signature Algorithm*): variante mais nova do DSA, baseada em curvas elípticas, mais eficiente, com assinaturas menores e menos uso de banda.

**Observação:** nos anos 1990, a empresa RSA Security publicou os **PKCS** (*Public Key Cryptography Standards*), um conjunto de padrões de criptografia de chave pública. Não são padrões oficiais do setor, mas são bem reconhecidos.

### 7.2 Como a Assinatura É Criada e Verificada

A assinatura usa a chave **privada** do remetente para assinar e a chave **pública** do remetente para conferir.

#### 7.2.1 Exemplo Resolvido: Bob Confirma um Pedido de Alice

Para assinar:

1. o computador de Bob calcula o hash da confirmação do pedido;
2. o hash é criptografado com a chave privada de Bob; esse hash criptografado é a assinatura digital;
3. a assinatura é anexada ao documento, que é enviado a Alice.

Para verificar:

1. o computador de Alice obtém a chave pública de Bob;
2. descriptografa a assinatura com essa chave e recupera o hash calculado por Bob;
3. calcula o hash do documento recebido e compara com o recuperado; se forem iguais, o documento é autêntico e não foi alterado desde a assinatura.

**Importante:** o que se criptografa na assinatura é o **hash** do documento, e não o documento inteiro. Por isso, a assinatura sozinha não dá confidencialidade: o documento continua legível.

Para ter confidencialidade, autenticidade e integridade ao mesmo tempo, os dois processos se combinam: Alice criptografa a mensagem com a chave **pública de Bob** (só ele lê) e assina o hash com a própria chave **privada** (prova que foi ela e que nada mudou).

### 7.3 Assinatura de Código

A **assinatura de código** aplica a assinatura digital a programas. Os arquivos executáveis são colocados em um envelope assinado, e o usuário pode conferir a assinatura antes de instalar.

A assinatura de código garante que:

- o código é autêntico e veio realmente da editora;
- o código não foi modificado desde que saiu da editora;
- a editora publicou o código e não pode negar isso.

O padrão FIPS 140-3, do governo dos EUA, que valida módulos criptográficos, exige que eles confiram a integridade do próprio software, normalmente por meio de assinatura digital.

Exemplo: nas propriedades de um executável da Cisco baixado da internet, a aba de assinaturas digitais mostra quem assinou (Cisco Systems), o algoritmo do resumo (SHA-256), a data e a contra-assinatura de uma autoridade de carimbo de tempo. O certificado mostra para quem foi emitido, quem o emitiu e o período de validade.

### 7.4 Certificados Digitais

Um **certificado digital** é o equivalente a um **passaporte eletrônico**: ele **associa uma chave pública a uma identidade confirmada**, seja de um site, de uma pessoa ou de uma organização.

Como um certificado em papel, o certificado digital informa para quem foi emitido, quem o emitiu e por quanto tempo é válido. Ele também pode ser usado para criptografar uma resposta ao seu dono.

**Importante:** é comum confundir os dois. O **certificado verifica a identidade**; a **assinatura verifica que algo veio dessa identidade**.

### 7.5 Infraestrutura de Chave Pública (PKI)

Para confiar na chave pública de um site, é preciso ter certeza de que ela pertence mesmo a ele. Quem garante isso é um terceiro confiável, que investiga a identidade antes de emitir o certificado. A lógica é a mesma da carteira de motorista: o órgão de trânsito comprova a identidade uma vez, e depois qualquer pessoa aceita a carteira como prova.

A **PKI** (*Public Key Infrastructure* — Infraestrutura de Chave Pública) é o conjunto de especificações, sistemas, ferramentas, pessoas, políticas e procedimentos usados para **criar, gerenciar, distribuir, usar, armazenar e revogar certificados digitais**. Ela permite distribuir chaves públicas em grande escala e cria uma relação de confiança que cresce com facilidade.

A **autoridade de certificação (CA)** é a organização que **emite os certificados, vinculando uma chave pública a uma identidade confirmada**, e os assina com a própria chave privada. Exemplos: IdenTrust, DigiCert, Sectigo, GlobalSign e GoDaddy, que cobram pelo serviço, e Let's Encrypt, sem fins lucrativos e gratuita.

Os principais elementos da PKI são:

| Elemento | Função |
| --- | --- |
| Certificado PKI | Contém a chave pública da entidade, sua finalidade, a CA emissora, o período de validade e o algoritmo da assinatura |
| Armazenamento de certificados | Fica no computador local e guarda os certificados e as chaves privadas |
| Autoridade de certificação (CA) | Verifica a identidade e emite e assina os certificados |
| Banco de dados de certificados | Guarda todos os certificados aprovados pela CA |

De forma simplificada, o processo ocorre da seguinte maneira:

1. Bob pede um certificado à CA, que confirma sua identidade, emite o certificado e o registra no banco de dados;
2. Bob usa o certificado ao se comunicar com Alice;
3. Alice confirma com a CA, usando a chave pública da CA, que o certificado de Bob é válido.

No navegador, isso acontece quando um site usa HTTPS: o navegador verifica se o certificado do site é válido e se foi emitido por uma CA confiável, guarda o certificado e usa a chave pública do site nas comunicações seguintes.

**Observação:** nem todo certificado vem direto de uma CA raiz. A **autoridade de registro (RA)** confere a identidade de quem pede o certificado e encaminha o pedido. Quem emite é sempre uma CA, que pode ser a raiz ou uma CA subordinada, certificada por ela, para usos específicos. Uma empresa também pode montar a própria PKI para uso interno, com Microsoft Server ou OpenSSL, e ser a sua própria CA.

### 7.6 Classes de Certificados

As CAs emitem certificados em **classes**, definidas pelo rigor da verificação de identidade feita na emissão. **Quanto maior a classe, mais confiável o certificado.**

| Classe | Uso |
| --- | --- |
| 0 | Testes, sem nenhuma verificação |
| 1 | Pessoas físicas, com verificação de e-mail |
| 2 | Organizações que precisam comprovar identidade |
| 3 | Servidores e assinatura de software, com verificação independente da identidade e da autoridade |
| 4 | Transações comerciais on-line entre empresas |
| 5 | Organizações privadas ou segurança do governo |

Na classe 1, basta responder a um e-mail, o que é uma autenticação fraca. Nas classes 3 e 4, o titular precisa comparecer pessoalmente com pelo menos dois documentos oficiais.

Os navegadores já vêm com as chaves públicas de várias CAs instaladas, na lista de **autoridades de certificação raiz confiáveis**. Qualquer certificado assinado por uma delas é aceito automaticamente.

### 7.7 Topologias de PKI

As CAs podem se organizar de formas diferentes para estabelecer confiança:

| Topologia | Como funciona | Vantagem | Desvantagem |
| --- | --- | --- | --- |
| Raiz única | Uma única CA raiz emite todos os certificados | Simplicidade | Difícil de crescer; ponto único de falha |
| Certificação cruzada | CAs de mesmo nível confiam umas nas outras | Redundância, sem ponto único de falha | Relações de confiança ponto a ponto para gerenciar |
| Hierárquica | A CA raiz emite certificados para CAs subordinadas, que atendem áreas ou domínios | Escala bem; ideal para grandes organizações | Difícil rastrear a cadeia de assinaturas |
| Híbrida | Hierarquias que se certificam entre si | Membros de comunidades diferentes confiam uns nos outros | Mais complexa |

O **ponto único de falha** é qualquer componente cuja falha derruba o sistema inteiro.

### 7.8 Padrão X.509

Como muitos fornecedores criaram soluções próprias, surgiram problemas de compatibilidade entre as PKIs e os serviços de diretório (LDAP e X.500, usados para consultar usuários e senhas em serviços como o Active Directory). Para resolver isso, o padrão **X.509 versão 3**, do ITU-T (órgão de padrões de telecomunicações), passou a definir o **formato dos certificados digitais**, e o IETF publicou documentos que mostram como usá-lo na internet, como a RFC 5280.

O X.509 v3 é usado em:

- **SSL/TLS**: servidores web autenticam o site, e navegadores usam certificados de cliente no HTTPS; é a autenticação por certificado mais usada;
- **IPsec**: as VPNs usam certificados quando a troca de chaves (IKE) é autenticada com RSA;
- **S/MIME**: programas de e-mail protegem mensagens com certificados;
- **EAP-TLS**: método de autenticação com certificado digital, usado pelos switches para autenticar os dispositivos que se conectam às portas da rede local.

### 7.9 Inscrição e Revogação de Certificados

O primeiro passo para usar uma PKI é obter, com segurança, a chave pública da CA, chamada de **certificado autoassinado**. Só uma CA raiz pode emitir um certificado autoassinado reconhecido pelas demais. Nos navegadores, isso já vem pronto, com os certificados raiz instalados.

No **registro** de um computador na PKI, os certificados da CA são obtidos pela rede, e a confirmação da impressão digital do certificado é feita **fora de banda** (por outro canal, como o telefone). Depois disso, os usuários trocam certificados entre si sem precisar da CA.

Um certificado pode precisar ser **revogado** antes do vencimento, por exemplo quando a chave é comprometida ou não é mais necessária. Os dois métodos mais comuns são:

| Método | Como funciona |
| --- | --- |
| CRL (*Certificate Revocation List* — Lista de Revogação de Certificados) | Lista dos números de série dos certificados invalidados; os sistemas consultam a lista periodicamente |
| OCSP (*Online Certificate Status Protocol* — Protocolo de Status de Certificado On-line) | Consulta um servidor sobre o status de um certificado específico; a informação é imediata |

### 7.10 Aplicações da PKI

A PKI está presente em muitos serviços da empresa:

- autenticação por certificado em SSL/TLS e tráfego web HTTPS;
- VPNs IPsec;
- controle de acesso à rede com 802.1X (padrão em que o dispositivo só usa a porta da rede depois de autenticado);
- e-mail seguro com S/MIME e mensagens instantâneas seguras;
- assinatura de código para aprovar aplicativos;
- criptografia de arquivos com o EFS (*Encrypting File System*);
- autenticação de dois fatores com cartões inteligentes;
- proteção de dispositivos de armazenamento USB.

Quando o navegador não consegue validar o certificado de um site, ele mostra um aviso de segurança. Os dois problemas mais comuns são:

- **validade fora do período**: o certificado tem datas “não antes de” e “não depois de”; um certificado vencido pode ser só um descuido do administrador ou sinal de algo mais grave;
- **erro de validação da assinatura**: o navegador não consegue confirmar a assinatura, geralmente porque o certificado raiz da CA não está no seu armazenamento; nesse caso, não há garantia de que a chave pública é autêntica.

O SSL/TLS é modular: ele usa um **conjunto de cifras** (*cipher suite*) formado por quatro algoritmos que podem ser trocados sem substituir o protocolo inteiro: o algoritmo de autenticação de mensagem (MAC), o de criptografia, o de troca de chaves e o de autenticação. Quando uma falha é descoberta em um algoritmo, basta atualizar o conjunto.

## 8. Ocultação de Dados

Além de criptografar, é possível proteger dados **escondendo ou disfarçando a informação**. As duas técnicas principais são o **mascaramento de dados** e a **esteganografia**.

### 8.1 Mascaramento de Dados

O **mascaramento de dados** **substitui a informação confidencial por uma versão não confidencial que parece e funciona como a original**. Assim, os sistemas continuam funcionando sem nenhuma mudança, mas sem expor os dados reais.

O uso mais comum é **criar conjuntos de dados substitutos para testes e análises**, evitando que dados reais se espalhem por ambientes que não são de produção. O mascaramento também pode ser dinâmico, aplicado na hora em que o sistema percebe que um pedido de informação é arriscado.

As principais técnicas de mascaramento são:

| Técnica | Como funciona | Exemplo |
| --- | --- | --- |
| Substituição | Troca os dados por valores que parecem autênticos, tornando os registros anônimos | Nomes reais trocados por nomes fictícios |
| Embaralhamento | Mistura os valores da própria coluna entre os registros | Salários trocados de lugar num banco de testes |
| Anulação | Coloca um valor nulo no campo, escondendo-o por completo | Campo de CPF deixado vazio |

### 8.2 Esteganografia

A **esteganografia** **esconde uma mensagem dentro de outro arquivo**, como uma imagem, um áudio ou um texto. Sua vantagem sobre a criptografia é que **a mensagem secreta não chama atenção**: quem vê a imagem não desconfia que ela carrega algo escondido.

Os componentes da esteganografia são:

- **dados embutidos**: a mensagem secreta;
- **capa**: o arquivo que esconde a mensagem (texto, imagem ou áudio de capa);
- **estego-arquivo**: o resultado, como a estego-imagem;
- **estego-chave**: o valor que controla o processo de esconder e recuperar.

A técnica mais usada em imagens é a dos **bits menos significativos (LSB**, *Least Significant Bits*). Cada pixel tem uma cor formada pela mistura de vermelho, verde e azul (RGB), com um byte para cada cor, ou 24 bits por pixel. O LSB troca o último bit de cada um desses bytes, o que permite guardar 3 bits por pixel.

Como o último bit quase não muda a cor, **o olho humano não percebe a alteração**. Exemplo: esconder a letra “T” em três pixels altera apenas dois bits.

A **esteganografia social** esconde a informação à vista de todos: a mensagem tem um sentido para o público e outro para quem conhece o código. Exemplo: entre amigos, “ir ao cinema” pode significar “ir à praia”. Pessoas em países com censura usam esse recurso, escrevendo palavras erradas de propósito ou fazendo referências indiretas.

### 8.3 Esteganoanálise

A **esteganoanálise** é a **descoberta de que existe informação escondida** e a tentativa de recuperá-la. Alguns sinais e métodos são:

- padrões estranhos na estego-imagem;
- áreas reservadas e não usadas em um disco, que podem estar escondendo dados;
- ferramentas de análise de disco que apontam informações em partes não utilizadas;
- filtros que capturam pacotes com dados escondidos nos cabeçalhos;
- comparação entre a imagem original e a estego-imagem, em busca de padrões repetidos.

| Característica | Criptografia | Esteganografia | Mascaramento |
| --- | --- | --- | --- |
| Objetivo | Tornar a mensagem ilegível | Esconder que a mensagem existe | Substituir dados reais por falsos realistas |
| Chama atenção? | Sim: o texto cifrado é visível | Não | Não |
| Uso típico | Proteger dados em trânsito e em repouso | Comunicação secreta | Ambientes de teste e análise |

## 9. Controle de Acesso e AAA

O **controle de acesso** é o conjunto de medidas que **define quem pode acessar cada recurso, o que pode fazer com ele e quando**. Ele responde a perguntas como: todo funcionário deve acessar tudo? Como saber o que cada usuário fez enquanto estava conectado?

### 9.1 Tipos de Controle de Acesso

De acordo com a forma como atuam, os controles de acesso podem ser classificados em **três tipos**:

| Tipo | O que são | Exemplos |
| --- | --- | --- |
| Físicos | Barreiras reais que impedem o contato direto com instalações e equipamentos | Guardas, cercas, portas trancadas, câmeras, alarmes |
| Lógicos | Soluções de hardware e software que gerenciam o acesso a sistemas | Senhas, criptografia, firewalls, cartões inteligentes |
| Administrativos | Políticas e procedimentos da organização | Políticas, treinamento, verificação de antecedentes |

Os **controles físicos** determinam quem pode entrar ou sair, por onde e quando. Exemplos:

- guardas que monitoram o local e cães de guarda;
- cercas que protegem o perímetro;
- detectores de movimento e alarmes;
- travas para notebooks e portas trancadas;
- cartões de acesso a áreas restritas;
- câmeras que gravam imagens do local;
- **mantrap** (eclusa): entrada com duas portas que controla o fluxo de pessoas e pode prender um visitante indesejado entre elas.

Os **controles lógicos** são usados pelos sistemas para identificação, autenticação, autorização e auditoria. Exemplos:

- criptografia;
- cartões inteligentes, com microchip embutido;
- senhas e biometria;
- listas de controle de acesso (ACLs), que definem o tipo de tráfego permitido na rede;
- firewalls, roteadores e sistemas de detecção de intrusão;
- **níveis de corte** (*clipping levels*): o limite de erros permitido antes de disparar um alerta.

Os **controles administrativos** focam nas práticas das pessoas e do negócio. Exemplos:

- políticas: declarações de intenção;
- procedimentos: os passos detalhados para realizar uma atividade;
- práticas de contratação e verificação de antecedentes (histórico profissional, de crédito e criminal);
- classificação de dados por confidencialidade;
- treinamento em segurança;
- avaliações de desempenho dos funcionários.

### 9.2 AAA: Autenticação, Autorização e Contabilidade

O **AAA** (*Authentication, Authorization and Accounting* — Autenticação, Autorização e Contabilidade) reúne os **três serviços de segurança que formam a estrutura principal do controle de acesso**:

| Serviço | Pergunta que responde | Exemplo |
| --- | --- | --- |
| Autenticação | Quem é você? | O usuário prova sua identidade com nome e senha |
| Autorização | O que você pode fazer? | Entrar na rede não dá direito de usar a impressora colorida |
| Contabilidade | O que você fez? | Registro de que o usuário acessou um servidor por 15 minutos |

O AAA funciona como um cartão de crédito: o cartão **identifica quem pode usá-lo**, define **quanto pode ser gasto** e registra **em que o dinheiro foi gasto**.

**Importante:** a “contabilidade” do AAA (*accounting*) não tem relação com finanças. Ela é o **registro do que o usuário fez**: o que acessou, por quanto tempo e quais alterações fez.

### 9.3 Identificação

A **identificação** é a etapa em que o usuário diz quem é. Ela aplica as regras definidas na política de autorização: sempre que alguém pede acesso a um recurso, o controle de acesso decide se concede ou nega.

O **identificador único** associa cada atividade a uma pessoa específica. O mais comum é o **nome de usuário**, mas também podem ser usados um PIN (número de identificação pessoal), um cartão inteligente ou a biometria.

**Importante:** identificar não é o mesmo que autenticar. Informar o nome de usuário é **identificação**; provar que se é realmente aquele usuário, com a senha, é **autenticação**.

### 9.4 Métodos de Autenticação

Para provar a identidade, o usuário apresenta pelo menos um de **três tipos de fator**:

| Fator | Exemplos |
| --- | --- |
| Algo que você sabe | Senha, frase secreta, PIN |
| Algo que você tem | Cartão inteligente, token (chaveiro de segurança) |
| Algo que você é | Impressão digital, íris, voz |

#### 9.4.1 Algo que Você Sabe

A **senha** é uma sequência de caracteres protegidos usada para comprovar a identidade, e é o **método de autenticação mais usado**. Frases secretas, códigos de acesso e PINs também são chamados genericamente de senhas.

As boas práticas para senhas são:

- não usar dados pessoais, como nome, data de nascimento ou endereço, que são fáceis de adivinhar;
- ter pelo menos oito caracteres, sem ser tão longa que fique impossível de memorizar;
- combinar letras maiúsculas e minúsculas, números e caracteres especiais;
- usar uma senha diferente para cada sistema, porque quem descobre uma senha repetida ganha acesso a todas as contas;
- usar um gerenciador de senhas para criar e guardar senhas fortes.

#### 9.4.2 Algo que Você Tem

O **cartão inteligente** (*smart card*) é um cartão plástico do tamanho de um cartão de crédito com um **chip que processa, armazena e protege dados** usando criptografia. Pode guardar números de contas, identificação pessoal, registros médicos e assinaturas digitais.

O **token** (ou chaveiro de segurança) é um pequeno dispositivo, do tamanho de um chaveiro, que exibe um número temporário. É usado principalmente como segundo fator de autenticação.

Exemplo: no banco on-line, o usuário informa o nome de usuário (identificação), digita a senha (primeiro fator) e, em seguida, o número exibido no token (segundo fator), que prova que ele tem o dispositivo emitido em seu nome.

#### 9.4.3 Algo que Você É

A **biometria** usa **características físicas ou comportamentais únicas** para identificar uma pessoa. O sistema compara a característica apresentada com um **perfil** guardado (um arquivo com as características conhecidas da pessoa) e libera o acesso se forem compatíveis.

Os identificadores biométricos podem ser classificados em dois tipos:

- **fisiológicos**: impressão digital, DNA, rosto, mãos, retina, orelha;
- **comportamentais**: gestos, voz, modo de andar, ritmo de digitação.

Um sistema biométrico tem três partes: o leitor, o software que converte a leitura em formato digital e o banco de dados com os perfis para comparação.

### 9.5 Autenticação Multifator (MFA)

A **autenticação multifator** (**MFA**, *Multi-Factor Authentication*) **usa pelo menos dois fatores de tipos diferentes** para verificar a identidade. Como saber a senha não basta, a MFA reduz muito o roubo de identidade on-line.

Exemplos:

- banco on-line que pede a senha e um PIN temporário enviado ao celular cadastrado;
- caixa eletrônico, que exige o cartão (algo que você tem) e o PIN (algo que você sabe).

A **autenticação de dois fatores** (**2FA**) é o caso da MFA com exatamente dois fatores. Na prática, os dois termos são usados como sinônimos.

**Importante:** duas senhas não formam autenticação multifator, porque são do mesmo tipo (“algo que você sabe”). Os fatores precisam ser de **tipos diferentes**.

### 9.6 Autorização

A **autorização** **controla o que o usuário pode e não pode fazer depois de autenticado**. Ela responde à pergunta: quais privilégios de ler, copiar, editar, criar e excluir este usuário tem?

O sistema compara os atributos do usuário com o banco de dados de autenticação, define as restrições e as entrega ao dispositivo onde ele está conectado. A autorização é **automática**: o usuário não precisa fazer nada além de se autenticar.

A autorização também pode controlar **quando** o acesso é permitido. Exemplo: o banco de dados de vendas só fica acessível no horário comercial.

Definir as regras de autorização é a **primeira etapa do controle de acesso**, e quem estabelece essas regras é a **política de autorização**. Os dois tipos mais comuns são:

- **política baseada em grupo**: a autorização depende de o usuário pertencer a um grupo; exemplo: todos os funcionários entram no prédio com o crachá, mas só a equipe de TI e os gestores entram na sala de servidores;
- **política de nível de autoridade**: as permissões dependem do cargo do funcionário na organização.

### 9.7 Auditabilidade

A **auditabilidade** (*accountability*) **rastreia cada ação até a pessoa ou o processo que a realizou**. Ela coleta essas informações e gera relatórios de uso, que podem servir para auditoria ou cobrança.

Os dados coletados podem incluir o horário de login, se o login teve sucesso ou falhou e quais recursos foram acessados. Falhas de login podem indicar que alguém tentou invadir uma conta; logins bem-sucedidos mostram quem usou o quê e quando.

A auditabilidade é implementada com tecnologias, políticas, procedimentos e educação. As políticas definem quais ações são registradas e como os logs são gerados, revisados e guardados. Leis de retenção de dados, de descarte de mídias e de conformidade também exigem auditabilidade.

### 9.8 Gerenciamento de Identidade Federada

O **gerenciamento de identidade federada** permite que **várias organizações aceitem as mesmas credenciais** para dar acesso às suas redes. Do ponto de vista do usuário, funciona como um login universal na web; exemplo: entrar em vários sites com a mesma conta de uma rede social.

O risco é o **efeito cascata**: se as credenciais forem comprometidas, o atacante ganha acesso a todos os sistemas da federação. Por isso, as organizações devem avaliar com cuidado quais dados de identidade compartilham com os parceiros, como CPF, nomes e endereços.

**Observação:** a forma mais comum de proteger identidades federadas é **vincular o login a um dispositivo autorizado**.

## 10. Modelos de Controle de Acesso e Confiança Zero

Um **modelo de controle de acesso** é a **regra geral que define quem decide sobre o acesso e com base em quê**. Conhecer os modelos ajuda o analista a entender como os atacantes tentam burlar os controles.

### 10.1 Modelos de Controle de Acesso

Os principais modelos são:

| Modelo | Quem decide / com base em quê | Característica marcante |
| --- | --- | --- |
| DAC (discricionário) | O **dono** dos dados | Menos restritivo |
| MAC (obrigatório) | Rótulos de segurança dos dados e autorização do usuário | Mais rígido; uso militar |
| RBAC (baseado em funções) | A **função** ou cargo do usuário | Prática recomendada em grandes organizações |
| ABAC (baseado em atributos) | Atributos do usuário, do recurso e do ambiente | Mais flexível |
| Baseado em regras | Regras definidas pela equipe de segurança | Usa ACLs; o usuário não altera |
| TAC (baseado em tempo) | Hora e dia | Acesso só em horários permitidos |

#### 10.1.1 Controle de Acesso Discricionário (DAC)

No **DAC** (*Discretionary Access Control*), **o dono do recurso decide quem pode acessá-lo** e com qual permissão. É o modelo **menos restritivo**. Exemplo: o dono de um arquivo define quem pode ler, gravar ou executar. O DAC pode usar permissões e ACLs.

#### 10.1.2 Controle de Acesso Obrigatório (MAC)

No **MAC** (*Mandatory Access Control*), cada recurso recebe um **rótulo de nível de segurança** e cada usuário recebe uma **autorização** (*clearance*). O sistema só libera o acesso se a autorização do usuário for compatível com o rótulo do recurso. É o modelo **mais rígido**, usado em aplicações militares ou de missão crítica, e o usuário não pode alterar as regras.

#### 10.1.3 Controle de Acesso Baseado em Funções (RBAC)

No **RBAC** (*Role-Based Access Control*), as permissões são atribuídas às **funções** (cargos, classes de cargo ou grupos), e cada pessoa recebe as permissões da função que ocupa. Quando alguém muda de cargo, basta trocar a função.

O RBAC facilita a administração em organizações com centenas de usuários e milhares de permissões e é considerado **prática recomendada**. Também é chamado de controle de acesso **não discricionário** e pode ser combinado com o DAC ou com o MAC.

#### 10.1.4 Controle de Acesso Baseado em Atributos (ABAC)

No **ABAC** (*Attribute-Based Access Control*), a decisão considera **atributos do recurso, do usuário e do ambiente**. Exemplo: um médico (atributo do usuário) pode ver prontuários (atributo do recurso) apenas no hospital e durante o plantão (atributos do ambiente).

#### 10.1.5 Controle de Acesso Baseado em Regras

No **controle de acesso baseado em regras** (*Rule-Based Access Control*), a equipe de segurança define **regras ou condições** que determinam o acesso, como endereços IP permitidos ou negados e protocolos aceitos. As regras ficam em listas de controle de acesso. Exemplo: nenhum funcionário acessa a folha de pagamento fora do expediente ou nos fins de semana.

**Importante:** a sigla **RBAC** é usada para dois modelos diferentes: o baseado em **funções** (*Role*) e o baseado em **regras** (*Rule*). Quando aparecer sozinha, normalmente se refere ao baseado em funções.

#### 10.1.6 Controle de Acesso Baseado em Tempo (TAC)

No **TAC** (*Time-based Access Control*), o acesso é liberado **conforme a hora e o dia**. Exemplo: o sistema de folha de pagamento só aceita logins de segunda a sexta, das 8h às 18h.

### 10.2 Privilégio Mínimo e Escalação de Privilégios

O **princípio do privilégio mínimo** determina que **usuários e processos recebam apenas o acesso mínimo necessário para fazer seu trabalho**. Ele está ligado ao conceito de **necessidade de saber** (*need to know*): só se acessa a informação de que realmente se precisa.

Um ataque comum contra os controles de acesso é a **escalação de privilégios**: o atacante explora uma vulnerabilidade para conseguir **um nível de privilégio maior do que deveria ter**. Com esse privilégio, pode acessar dados confidenciais ou assumir o controle do sistema.

### 10.3 Confiança Zero (Zero Trust)

A **confiança zero** (*zero trust*) é uma abordagem que **não confia automaticamente em ninguém nem em nada**, nem mesmo em usuários e dispositivos que já estão dentro da rede. Seu princípio é: “**nunca confie, sempre verifique**”.

Tradicionalmente, o **perímetro** (a borda da rede) separava o lado de dentro, confiável, do lado de fora, não confiável. O problema é que um usuário confiável podia circular pela rede inteira. Na confiança zero, **todo ponto em que há uma decisão de acesso passa a ser um perímetro**: quem já passou por um controle precisa se autenticar de novo para acessar outra área, às vezes mais de uma vez e de formas diferentes.

Com isso, a confiança zero impede acessos não autorizados, contém violações e reduz o **movimento lateral**, isto é, a circulação do atacante de um sistema para outro dentro da rede. Ela monitora constantemente todos os usuários, independentemente de cargo ou função.

A confiança zero se apoia em **três pilares**:

| Pilar | O que protege |
| --- | --- |
| Força de trabalho | Pessoas (funcionários, terceirizados, parceiros, fornecedores) que acessam aplicativos de trabalho com dispositivos pessoais ou da empresa, de qualquer lugar |
| Cargas de trabalho | Aplicativos na nuvem, em data centers e em ambientes virtualizados que conversam entre si, como uma API ou um contêiner acessando um banco de dados |
| Local de trabalho | Todos os dispositivos que se conectam à rede: servidores, impressoras, câmeras, sistemas de climatização, equipamentos médicos e industriais |

### 10.4 Controle de Acesso à Rede (NAC)

O **NAC** (*Network Access Control* — Controle de Acesso à Rede) é o sistema que **aplica as políticas da organização às pessoas e aos dispositivos que tentam entrar na rede**. Ele monitora quem está conectado e permite controlar o acesso de cada um.

Entre suas principais funções estão:

- aplicar rapidamente políticas de acesso criadas para diferentes situações;
- reconhecer e criar perfis dos usuários e dispositivos conectados;
- oferecer acesso seguro a visitantes, geralmente por um portal de cadastro;
- avaliar se o dispositivo cumpre as políticas de segurança (por tipo de usuário, tipo de dispositivo e sistema operacional) **antes** de liberar o acesso;
- conter incidentes, bloqueando, isolando ou corrigindo dispositivos fora das regras.

Com BYOD e Internet das Coisas, milhares de dispositivos podem tentar entrar na rede, e seria impossível avaliá-los manualmente. Por esse motivo, a automação do NAC é um **componente importante da confiança zero**.

## 11. Gerenciamento de Contas e Protocolos de Autenticação

O **gerenciamento de contas** garante que **cada usuário tenha o tipo de conta adequado à sua função** e só acesse e modifique o que for necessário. Ele é completado pelos **protocolos de autenticação**, que definem como a identidade é comprovada pela rede.

### 11.1 Tipos de Contas

Os tipos mais comuns de conta são:

| Tipo | Uso |
| --- | --- |
| Usuário | Uso diário dos recursos do sistema |
| Serviço | Interação de programas com o sistema operacional |
| Convidado | Usuários temporários |
| Administrador | Apenas para administrar o sistema |

**Importante:** a conta de administrador **só deve ser usada para administrar**. Se o administrador navegar na internet ou abrir e-mails com ela e cair em um site infectado, o malware ganha os mesmos privilégios de administrador.

Os sistemas operacionais criam contas padrão, como as de convidado e de administrador. Como os atacantes conhecem essas contas e suas configurações, a boa prática é **substituir ou desativar as contas padrão** e exigir senha em todas as contas. Contas também não devem ser compartilhadas entre pessoas.

### 11.2 Boas Práticas de Gerenciamento de Contas

As boas práticas acompanham todo o período em que a pessoa está na organização:

- na contratação, criar o perfil de identidade, registrar os computadores e celulares do funcionário e liberar o acesso; nesse papel, a empresa atua como **provedor de identidade (IdP)**, responsável por autenticar o funcionário;
- conceder apenas o acesso necessário às tarefas (privilégio mínimo);
- revisar periodicamente os acessos e ajustar o que for preciso;
- desativar as contas que não são mais necessárias e recuperar os dados da organização dos dispositivos do usuário;
- restringir **quando** o usuário pode fazer login, por horário;
- restringir **de onde** o usuário ou o dispositivo pode fazer login, por localização.

As restrições por localização usam três recursos:

| Recurso | O que faz | Exemplo |
| --- | --- | --- |
| Delimitação geográfica (*geofencing*) | Dispara uma ação quando o usuário entra ou sai de uma área | Bloquear o acesso fora do prédio da empresa |
| Geolocalização | Identifica onde o dispositivo está | Mostrar a posição do celular no mapa |
| Marcação geográfica (*geotagging*) | Acrescenta a localização a um arquivo | Foto que guarda as coordenadas de onde foi tirada |

### 11.3 Contas Privilegiadas

As **contas privilegiadas** são as mais poderosas da organização: têm **acesso elevado e sem restrição** e são usadas pelos administradores para implantar e gerenciar sistemas, aplicativos e dispositivos de rede. Por esse motivo, são o **alvo preferido dos criminosos digitais**.

As práticas para protegê-las são:

- identificar e reduzir o número de contas privilegiadas;
- aplicar o privilégio mínimo;
- revogar os acessos quando o funcionário sai ou muda de função;
- eliminar contas compartilhadas com senhas que nunca expiram e credenciais compartilhadas por vários administradores;
- proteger o armazenamento das senhas;
- trocar automaticamente as senhas privilegiadas **a cada 30 ou 60 dias**;
- criar um processo para trocar senhas embutidas em scripts e contas de serviço;
- registrar as sessões privilegiadas e toda a atividade dos usuários;
- gerar alertas para comportamentos incomuns;
- desativar contas privilegiadas inativas;
- exigir **autenticação multifator** para todo acesso administrativo;
- colocar um intermediário (*gateway*) entre o usuário e os ativos confidenciais, para reduzir a exposição a malware.

### 11.4 Permissões de Arquivos e Pastas

As **permissões** são **regras que limitam o acesso de uma pessoa ou de um grupo a pastas e arquivos**. Elas aplicam o privilégio mínimo: se o usuário só precisa de uma pasta, recebe acesso apenas a ela, e não ao disco inteiro. Assim, se o computador dele for infectado, o malware também não alcança o restante.

No Windows, os níveis de permissão são:

| Permissão | O que o usuário pode fazer |
| --- | --- |
| Controle total | Ver, alterar, excluir e criar arquivos e pastas e executar programas |
| Modificar | Alterar e excluir arquivos e pastas existentes |
| Ler e executar | Ver o conteúdo e executar programas |
| Gravar | Criar arquivos e pastas e alterar os existentes |
| Leitura | Ver o conteúdo e abrir arquivos e pastas |

**Observação:** no Windows, a permissão Modificar também inclui ler, executar e gravar; o que ela não permite, diferentemente do Controle total, é alterar as permissões nem tomar posse do arquivo.

**Importante:** a permissão **Negar substitui qualquer outra**. Se o administrador negar a alguém o acesso a um compartilhamento, essa pessoa não entra, mesmo que seja administradora ou faça parte do grupo de administradores.

Arquivos e pastas criados dentro de uma pasta **herdam as permissões da pasta-mãe**. Ao mover ou copiar dados, as permissões se comportam assim:

| Ação | Mesmo volume | Volume diferente |
| --- | --- | --- |
| Mover | Mantém as permissões originais | Herda novas permissões |
| Copiar | Herda novas permissões | Herda novas permissões |

Ou seja, **só mover dentro do mesmo volume mantém as permissões originais**.

### 11.5 Políticas de Conta no Windows

Nas redes Windows, o administrador costuma configurar o **Active Directory**, o serviço de diretório da Microsoft, com **domínios** em um servidor. Os computadores que entram no domínio recebem automaticamente a **política de segurança do domínio**.

Quando o computador não faz parte de um domínio, as políticas são configuradas pela **Política de Segurança Local**, aberta com o comando secpol.msc (disponível em todas as versões do Windows, exceto a Home).

As principais políticas são:

- **política de senhas**: exemplo: trocar a senha a cada 90 dias, usar cada senha por pelo menos um dia, ter oito caracteres com três de quatro categorias (maiúsculas, minúsculas, números e símbolos) e só repetir uma senha depois de 24 senhas diferentes;
- **política de bloqueio de conta**: bloqueia a conta por um tempo depois de muitas tentativas erradas; exemplo: depois de cinco tentativas, a conta fica bloqueada por 30 minutos, e então a contagem volta a zero;
- **política de auditoria**: cria um log de segurança que registra eventos de logon, gerenciamento de contas, acesso ao serviço de diretório e a objetos, mudanças de política, uso de privilégios, acompanhamento de processos e eventos do sistema.

### 11.6 Gerenciamento de Autenticação

O **gerenciamento de autenticação** busca **garantir uma entrada segura sem complicar a vida do usuário**. Os problemas mais comuns que ele resolve são credenciais sem criptografia, permissões incorretas e violações de acesso. As principais soluções são:

| Solução | Como funciona |
| --- | --- |
| SSO (*Single Sign-On* — logon único) | Um único conjunto de credenciais dá acesso a vários aplicativos; o usuário só precisa lembrar uma senha forte |
| OAuth | Padrão de autorização que permite que um serviço de terceiros acesse informações da conta do usuário sem receber a senha; o “entrar com Google” usa o OpenID Connect, construído sobre o OAuth 2.0 |
| Cofre de senhas | Guarda as credenciais protegidas por uma única senha forte |
| KBA (*Knowledge-Based Authentication* — autenticação baseada em conhecimento) | Redefine a senha esquecida com perguntas sobre informações pessoais do usuário |

### 11.7 Protocolos de Autenticação

Um **protocolo de autenticação** define **quais informações duas entidades trocam para se autenticar** antes de se conectarem. Uma entidade pode ser qualquer dispositivo ou sistema da organização.

| Protocolo | Como funciona | Segurança |
| --- | --- | --- |
| PAP (*Password Authentication Protocol*) | Envia nome de usuário e senha ao servidor em texto claro | Fraca |
| CHAP (*Challenge Handshake Authentication Protocol*) | O servidor envia um desafio; o cliente responde com um hash; o servidor compara com o valor esperado e repete a verificação durante a sessão | Melhor que o PAP |
| EAP (*Extensible Authentication Protocol*) | Estrutura que admite vários métodos de autenticação, muito usada em redes sem fio | Depende do método |
| 802.1X | Controle de acesso por porta: o dispositivo só usa a porta da rede depois de autenticado, com credenciais ou certificado conferidos por um servidor RADIUS | Alta |
| RADIUS | Servidor central de autenticação; criptografa só a senha | Média |
| TACACS+ | Servidor central de autenticação, sobre TCP; criptografa todos os dados | Alta |
| Kerberos | Autenticação mútua com tíquetes e criptografia forte | Alta |

#### 11.7.1 Kerberos

O **Kerberos** usa criptografia forte e faz uma **autenticação mútua**: o cliente prova sua identidade ao servidor, e o servidor prova a sua ao cliente. A base de tudo é o **tíquete**.

O servidor Kerberos guarda os nomes de usuário e os hashes das senhas, além de chaves secretas compartilhadas com os servidores da rede. De forma simplificada, o processo ocorre da seguinte maneira:

1. o cliente se autentica e recebe um **tíquete de concessão de tíquete** (TGT, *Ticket-Granting Ticket*);
2. o cliente apresenta o TGT ao servidor Kerberos e pede acesso a um servidor específico;
3. o cliente recebe um **tíquete de serviço** e o usa para acessar o serviço.

Como a sessão inteira pode ser criptografada, as senhas não trafegam de forma vulnerável. Além disso, os tíquetes têm **carimbo de hora e prazo de validade**, então uma tentativa de reutilizar um tíquete antigo falha.

## 12. Implementação do AAA

A política de segurança da rede define quem pode se conectar, o que cada um pode fazer e, muitas vezes, exige registrar **quem entrou, quando e o que fez**. Alguns regulamentos determinam até por quanto tempo esses registros devem ser guardados. O **AAA** oferece a estrutura para atender a essas exigências em redes de qualquer tamanho.

Relembrando: as três funções do AAA são independentes entre si:

- **autenticação**: o usuário prova quem é, com nome e senha, desafio e resposta ou token;
- **autorização**: define o que ele pode acessar; exemplo: “o usuário *aluno* pode acessar o servidor XYZ apenas por SSH”;
- **contabilidade** (*accounting*): registra o que ele fez; exemplo: “o usuário *aluno* acessou o servidor XYZ por SSH durante 15 minutos”.

### 12.1 AAA Local e AAA Baseado em Servidor

A Cisco oferece **duas formas de implementar o AAA**:

| Característica | AAA local | AAA baseado em servidor |
| --- | --- | --- |
| Onde ficam os usuários e senhas | No próprio roteador | Em um servidor AAA central |
| Outro nome | Autenticação autônoma | AAA centralizado |
| Indicado para | Redes pequenas | Redes médias e grandes |
| Escalabilidade | Baixa: cada roteador tem a sua lista | Alta: uma lista para todos |

No **AAA local**, o processo ocorre da seguinte maneira:

1. o cliente remoto se conecta ao roteador;
2. o roteador pede nome de usuário e senha;
3. o roteador confere as credenciais no seu banco de dados local e libera o acesso.

No **AAA baseado em servidor**, o terceiro passo muda: o roteador consulta o **servidor AAA**, e o usuário recebe acesso conforme as informações desse servidor.

O AAA centralizado é **mais escalável e mais fácil de gerenciar**, por isso é a forma preferida. Ele pode usar o Active Directory ou o **LDAP** (*Lightweight Directory Access Protocol*, protocolo de consulta a serviços de diretório) para autenticar os usuários e saber a que grupos pertencem, mantendo bancos próprios para autorização e contabilidade.

### 12.2 TACACS+ e RADIUS

Os dispositivos se comunicam com o servidor AAA central por meio de **dois protocolos**: o **TACACS+** (*Terminal Access Controller Access Control System Plus*) e o **RADIUS** (*Remote Authentication Dial-In User Service*).

| Característica | TACACS+ | RADIUS |
| --- | --- | --- |
| Funcionalidade | Separa autenticação, autorização e contabilidade | Combina autenticação e autorização; separa a contabilidade |
| Padrão | Principalmente Cisco | Padrão aberto (RFC) |
| Transporte | TCP, porta 49 | UDP, portas 1812 e 1813 (ou 1645 e 1646) |
| Desafio e resposta | Bidirecional, como no CHAP | Unidirecional, do servidor para o cliente |
| Confidencialidade | Criptografa todo o corpo do pacote | Criptografa só a senha |
| Autorização de comandos | Por usuário ou por grupo | Não tem |
| Contabilidade | Limitada | Abrangente |

**Importante:** a diferença mais cobrada é a criptografia. O **RADIUS criptografa só a senha**; nome de usuário, serviços autorizados e contabilidade trafegam em texto claro. O **TACACS+ criptografa todo o corpo do pacote**, mantendo apenas o cabeçalho padrão.

Por permitir definir ACLs, filtros e privilégios por usuário e controlar comandos, o TACACS+ é a melhor escolha para redes corporativas que exigem controle detalhado da autorização. Já o RADIUS, por ser padrão aberto e ter contabilidade abrangente, é muito usado com 802.1X e acesso remoto.

**Observação:** quando o RADIUS é usado, são necessárias medidas extras contra **ataques de repetição**, em que o atacante grava uma autenticação válida e a reenvia depois.

### 12.3 Contabilidade do AAA

O AAA centralizado também permite a **contabilidade**: os registros de todos os dispositivos são enviados a um repositório central, o que **facilita a auditoria das ações dos usuários**.

Os dados coletados podem incluir os horários de início e fim da conexão, os comandos executados e o número de pacotes e de bytes. O servidor guarda um registro detalhado do que o usuário autenticado fez no dispositivo, com nome de usuário, data, hora e o comando exato digitado. Isso ajuda a resolver problemas e **serve de prova contra quem realiza ações mal-intencionadas**.

Quando o usuário se autentica, o AAA gera uma mensagem de **início** (*start*); quando ele sai, gera uma mensagem de **parada** (*stop*), encerrando o registro.

Os tipos de informação de contabilidade que podem ser coletados são:

| Tipo | O que registra |
| --- | --- |
| De rede | Sessões PPP, com contagem de pacotes e bytes |
| De conexão | Conexões de saída feitas a partir do cliente AAA, como por SSH |
| EXEC | Sessões de terminal do usuário: nome, data, início, fim e IP do servidor de acesso |
| Do sistema | Eventos do sistema, como reinicializações e ativação ou desativação da contabilidade |
| De comandos | Comandos digitados em um nível de privilégio, com data, hora e usuário |
| De recursos | Registros de início e parada das conexões autenticadas e de parada das que falharam |

O **PPP** (*Point-to-Point Protocol*) é o protocolo usado em conexões ponto a ponto, como links seriais e acessos discados.

## 13. Segurança Física

A **segurança física** protege as instalações e os equipamentos da rede contra o acesso físico não autorizado. Ela é a **primeira linha de defesa**: de nada adianta uma senha forte se qualquer pessoa pode entrar na sala de servidores e levar um disco.

### 13.1 Barreiras Físicas e Cercas

As **barreiras físicas** são, em geral, a **camada mais externa e mais visível da defesa**. Todas devem atender aos requisitos do projeto e às especificações do fabricante. Seus principais componentes são:

- cerca de perímetro e portão de segurança;
- **cabeços de amarração** (*bollards*): postes curtos que impedem a invasão com veículos;
- barreiras de entrada de veículos;
- abrigos de proteção;
- cercamento.

A **cerca** protege áreas seguras e marca os limites da propriedade. A altura define o quanto ela atrasa um invasor:

| Altura | Efeito |
| --- | --- |
| 1 metro (3 a 4 pés) | Só detém invasores casuais |
| 2 metros (6 a 7 pés) | Alta demais para invasores casuais escalarem |
| 2,5 metros (8 pés) | Atrasa por pouco tempo um invasor determinado |

Áreas de alta segurança costumam exigir uma **proteção superior**, como arame farpado ou concertina, que funciona como impedimento extra. Mesmo assim, o invasor pode jogar um cobertor ou um colchão por cima para atravessar.

**Observação:** cercas exigem manutenção e inspeção regulares, porque animais cavam por baixo e a chuva leva a terra, deixando a cerca instável. Veículos nunca devem estacionar perto da cerca, porque ajudam o invasor a escalá-la. As regras locais também podem limitar o tipo de cerca permitido.

### 13.2 Biometria no Controle de Acesso Físico

Relembrando: a **biometria** identifica a pessoa por uma característica física ou comportamental, como rosto, digital, geometria da mão, íris, retina, assinatura ou voz. Ela é muito usada para liberar portas e áreas restritas.

Ao escolher um sistema biométrico, devem ser considerados os seguintes fatores:

- precisão;
- velocidade de leitura (taxa de transferência);
- aceitação pelos usuários;
- exclusividade da característica medida;
- resistência à falsificação;
- confiabilidade;
- espaço necessário para armazenar os dados;
- tempo de cadastro;
- o quanto a verificação é invasiva.

O fator mais importante é a **precisão**, medida pelos **tipos de erro** e suas taxas:

| Erro | Nome | O que acontece | Gravidade no controle de acesso |
| --- | --- | --- | --- |
| Tipo I | Falsa rejeição | Barra um usuário autorizado | Menos grave (incomoda, mas não deixa ninguém entrar) |
| Tipo II | Falsa aceitação | Deixa entrar quem não deveria | Mais grave (permite a entrada de invasores) |

**Importante:** no controle de acesso, o **erro tipo II (falsa aceitação) é o mais grave**, porque permite a entrada de um invasor. O tipo I é menos grave para a segurança, embora possa prejudicar o negócio.

A **taxa de aceitação**, em porcentagem, indica com que frequência o sistema aceita impostores ou pessoas descadastradas como se fossem usuários legítimos.

O método mais usado para comparar a precisão de sistemas biométricos é a **CER** (*Crossover Error Rate* — taxa de erro de cruzamento): o ponto em que a taxa de falsa rejeição e a taxa de falsa aceitação ficam iguais. **Quanto menor a CER, mais preciso é o sistema.**

### 13.3 Vigilância

Todos os controles físicos, sejam de impedimento ou de detecção, dependem, no fim, de **pessoas que intervenham para parar o ataque**. As principais formas de vigilância são:

| Forma | Vantagens | Desvantagens |
| --- | --- | --- |
| Guardas e escoltas | Resposta imediata; adaptam-se e decidem na hora | Custo, dificuldade de registrar grande movimento, erro humano |
| Vigilância eletrônica e por vídeo (CFTV) | Monitora sem pessoas presentes, grava por longos períodos, detecta movimento, cobre todo o perímetro a baixo custo | Depende de alguém que assista e reaja |
| Etiquetas RFID | Rastreiam ativos que saem da área segura, sem precisar vê-los | Exigem leitores instalados nas saídas |

Os **guardas** são a melhor solução quando a situação exige **resposta instantânea e adequada**. Em ambientes altamente seguros, controlam o acesso às áreas confidenciais.

A vigilância por vídeo (**CFTV**, circuito fechado de televisão, ou CCTV em inglês) complementa ou até substitui os guardas. Em ambientes altamente seguros, as câmeras devem cobrir **todas as entradas, saídas, áreas de carga, escadas e áreas de coleta de lixo**.

As etiquetas **RFID** (*Radio Frequency Identification* — Identificação por Radiofrequência) são lidas por ondas de rádio. Diferentemente do código de barras, **não precisam estar visíveis nem na linha de visão do leitor**, e os sistemas novos leem várias etiquetas ao mesmo tempo. Os leitores podem ficar escondidos nos batentes das portas.

Exemplo: um notebook da empresa com etiqueta RFID escondido na bolsa de alguém dispara um alerta ao passar pela porta, sem que a pessoa perceba que foi detectada.

### 13.4 Controle de Ameaças às Instalações

As organizações podem combinar várias medidas para controlar as ameaças às instalações físicas:

- controle de acesso e câmeras em todas as entradas;
- políticas e procedimentos para visitantes;
- testes de invasão do prédio, por meios físicos e digitais, feitos de forma secreta;
- crachás de acesso com criptografia;
- planos de recuperação de desastres e de continuidade dos negócios;
- treinamento e conscientização em segurança;
- sistema de etiquetagem de ativos.

## 14. Segurança de Aplicações

A **segurança de aplicações** protege os programas, sites e serviços on-line que a organização desenvolve e usa. A segurança precisa ser **prioridade em todas as etapas: desenvolvimento, testes e implantação**, e vale tanto para aplicativos locais quanto para os criados na nuvem.

### 14.1 Etapas do Desenvolvimento de Aplicações

Para manter a segurança do início ao fim, o desenvolvimento segue um processo com ambientes separados:

Desenvolvimento e teste → Preparação → Produção

| Ambiente ou etapa | O que acontece |
| --- | --- |
| Desenvolvimento e teste | O software é escrito, testado e corrigido; o ambiente é menos restritivo e tem segurança mais baixa; a garantia de qualidade (QA) encontra falhas, que são mais fáceis de corrigir nessa fase |
| Preparação (*staging*) | Ambiente idêntico ao de produção, onde se confirma que o software funciona com as configurações de segurança exigidas |
| Produção | O software é implantado para uso real |

No desenvolvimento, o **software de controle de versão** rastreia e gerencia as alterações no código, e o **sandbox** (ambiente isolado) permite trabalhar sem sobrescrever o código de outros.

O **provisionamento** é a criação ou atualização de um software no ambiente; o **desprovisionamento** é a sua remoção. Um portal de autoatendimento pode automatizar os dois.

### 14.2 Técnicas de Codificação Segura

Ao programar, os desenvolvedores usam técnicas que ajudam a cumprir os requisitos de segurança:

| Técnica | O que faz |
| --- | --- |
| Normalização | Organiza os dados no banco e converte cada entrada para a forma mais simples conhecida, o que ajuda a identificar entradas mal-intencionadas |
| Procedimento armazenado | Grupo de instruções SQL pré-compiladas, guardado no banco de dados, que executa uma tarefa; reduz o tráfego e acelera os resultados |
| Ofuscação | Esconde os dados originais com caracteres ou dados aleatórios |
| Camuflagem | Substitui dados confidenciais por dados fictícios realistas |
| Reutilização de código | Aproveita código existente para criar software novo, economizando tempo e dinheiro |
| SDKs e bibliotecas de terceiros | Repositórios de código pronto que aceleram e barateiam o desenvolvimento |

A ofuscação e a camuflagem **dificultam a engenharia reversa**, isto é, a tentativa de descobrir como o programa funciona a partir do arquivo pronto.

**Importante:** a reutilização de código e os **SDKs** (*Software Development Kits*, kits de desenvolvimento de software) têm um risco em comum: **uma vulnerabilidade no código reaproveitado passa para todos os aplicativos que o usam**.

### 14.3 Validação de Entrada

**Controlar o que entra no banco de dados é essencial para manter a integridade dos dados.** Muitos ataques enviam **dados malformados**, que podem confundir ou travar o aplicativo, ou fazê-lo revelar informações demais ao atacante.

Exemplo: um site envia um e-mail de confirmação com um link para quem assina sua newsletter. O atacante altera o link para mudar o nome, o e-mail ou o status da assinatura. Se o servidor não conferir os dados recebidos, aceita as informações falsas, e o atacante pode automatizar o processo para inundar o banco com milhares de assinantes inválidos.

A **regra de validação** verifica se os dados estão **dentro dos parâmetros definidos pelo projetista do banco de dados**, garantindo integridade, precisão e consistência. Os critérios usados são:

| Critério | O que verifica | Exemplo |
| --- | --- | --- |
| Tamanho | Número de caracteres | CEP com 8 dígitos |
| Formato | Se segue o formato definido | Data no formato DD/MM/AAAA |
| Consistência | Se códigos relacionados combinam entre si | Cidade compatível com o estado |
| Intervalo | Se o valor está entre um mínimo e um máximo | Idade entre 0 e 120 |
| Dígito verificador | Um cálculo extra para detectar erros | Último dígito do ISBN ou do CPF |

#### 14.3.1 Exemplo Resolvido: Dígito Verificador do ISBN-10

O ISBN-10 identifica um livro com 10 dígitos, e o último é o dígito verificador. Para os nove primeiros dígitos 1 5 8 7 1 4 3 7 3:

1. multiplica-se o primeiro dígito por 10, o segundo por 9, e assim por diante, até o nono por 2;
2. somam-se os resultados;
3. o dígito verificador é o número que, somado ao total, dá um múltiplo de 11.

| Dígito | 1 | 5 | 8 | 7 | 1 | 4 | 3 | 7 | 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Peso | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 |
| Produto | 10 | 45 | 64 | 49 | 6 | 20 | 12 | 21 | 6 |

Soma: 10 + 45 + 64 + 49 + 6 + 20 + 12 + 21 + 6 = 233.

O múltiplo de 11 seguinte é 242 (11 × 22). Como 242 − 233 = 9, o **dígito verificador é 9**. Se alguém digitar um dígito errado, a conta não fecha e o erro é detectado.

### 14.4 Integridade dos Dados no Aplicativo

A **verificação de integridade** mede a consistência dos dados de um arquivo, imagem ou registro para garantir que não foram corrompidos. Ela usa uma função hash, que gera um “instantâneo” de tamanho fixo dos dados; se o instantâneo mudar, os dados mudaram.

Além do hash e do checksum, outras práticas mantêm a integridade:

- **controle de versão**: dois usuários não podem alterar o mesmo arquivo ou registro ao mesmo tempo; o primeiro a abrir pode editar, e o segundo recebe uma cópia somente leitura;
- **backups**: cópias precisas permitem recuperar dados corrompidos, desde que a integridade do próprio backup seja verificada antes de ser necessária;
- **autorização**: permissões garantem que só determinados usuários possam modificar os dados; exemplo: um arquivo marcado como somente leitura.

### 14.5 Outras Práticas de Segurança de Aplicativos

Relembrando: a **assinatura de código** prova que um programa é autêntico e não foi alterado depois de assinado pelo autor.

Os **cookies** são pequenos arquivos que o navegador cria a pedido do servidor para guardar dados durante a navegação. Para protegê-los, os desenvolvedores devem usar **cookies seguros, enviados apenas por HTTPS**, nunca por HTTP sem criptografia.

### 14.6 Controle de Ameaças a Aplicativos

As organizações podem aplicar uma medida para cada ameaça:

| Ameaça | Medidas |
| --- | --- |
| Acesso não autorizado a data centers, salas de computadores e armários de cabos | Políticas, padrões e procedimentos para funcionários e visitantes |
| Inatividade do sistema | Plano de continuidade dos negócios e plano de recuperação de desastres |
| Vulnerabilidade no software do sistema operacional de rede | Política de atualizações e instalação regular de correções |
| Acesso não autorizado aos sistemas | Autenticação multifator e monitoramento dos logs |
| Perda de dados | Padrões de classificação de dados e procedimentos de backup |
| Vulnerabilidades no desenvolvimento | Testes antes do lançamento |

### 14.7 OWASP Top 10

A **OWASP** (*Open Web Application Security Project*) é uma organização sem fins lucrativos dedicada à segurança de aplicativos web. Ela publica, a cada três anos aproximadamente, a lista **OWASP Top 10**, com as **dez principais preocupações de segurança web** enfrentadas pelas empresas.

Para a OWASP, uma **vulnerabilidade** é uma falha no aplicativo que um agente de ameaça pode explorar, e um **ataque** é a técnica usada para explorar essa falha.

## 15. Fortalecimento de Serviços e Protocolos de Rede

O **fortalecimento da rede** (*network hardening*) consiste em **proteger os serviços e protocolos para que só o necessário fique exposto** e para que os protocolos inseguros sejam trocados por versões seguras. Os criminosos usam serviços vulneráveis tanto para atacar um dispositivo quanto para usá-lo como parte de um ataque maior.

### 15.1 Varredura de Portas

Um **scanner de portas** **envia uma mensagem a cada porta de um dispositivo e espera a resposta**, que indica se a porta está aberta e como é usada. A **porta** é o número que identifica um serviço em um computador; exemplo: a porta 80 corresponde ao HTTP.

O administrador usa o scanner para descobrir serviços desprotegidos, e o criminoso usa a mesma técnica para encontrar alvos. Por esse motivo, proteger os serviços significa garantir que **apenas as portas necessárias fiquem abertas**.

### 15.2 Serviços de Rede e de Roteamento

#### 15.2.1 DHCP

O **DHCP** (*Dynamic Host Configuration Protocol*) usa um servidor para **atribuir automaticamente endereço IP e outras configurações** aos dispositivos. Na prática, o dispositivo recebe do servidor uma permissão para usar a rede.

Os atacantes podem atacar o servidor DHCP para negar acesso aos dispositivos ou criar um servidor DHCP falso. O **DHCP snooping** (rastreamento de DHCP) **impede que servidores DHCP falsos entreguem endereços**, validando as mensagens que vêm de fontes não confiáveis.

Para proteger o DHCP:

- proteger fisicamente o servidor;
- aplicar as correções de software;
- deixar o servidor atrás de um firewall;
- monitorar a atividade analisando os registros do DHCP;
- manter um antivírus forte;
- desinstalar serviços e aplicativos não usados e fechar portas não usadas.

#### 15.2.2 DNS

O **DNS** (*Domain Name System*) **converte nomes, como www.cisco.com, em endereços IP**. Os atacantes podem atacar servidores DNS para negar acesso aos recursos ou **redirecionar o tráfego para sites falsos**.

As **DNSSEC** (*DNS Security Extensions*) usam **assinaturas digitais** para autenticar as respostas DNS e proteger contra essas ameaças.

Para proteger o DNS:

- manter o software DNS atualizado;
- impedir que a versão do software seja revelada;
- separar os servidores DNS internos dos externos;
- restringir as transações permitidas por endereço IP do cliente;
- usar assinaturas de transação para autenticar as trocas entre servidores;
- desativar ou restringir ao máximo as transferências de zona e as atualizações dinâmicas;
- ativar e analisar os logs;
- usar DNSSEC e assinar as zonas.

#### 15.2.3 ICMP

O **ICMP** (*Internet Control Message Protocol*) é usado pelos dispositivos para **enviar mensagens de erro e de controle**, como avisar que um serviço não está disponível ou que um destino não pode ser alcançado. O comando **ping** usa o ICMP para testar se um host responde.

Os criminosos podem usar o ICMP para reconhecimento da rede, ataques de negação de serviço (**DoS**, *Denial of Service*, que tiram um serviço do ar) e canais secretos de comunicação. Por isso, muitas redes filtram as solicitações ICMP.

#### 15.2.4 RIP

O **RIP** (*Routing Information Protocol*) é um protocolo de roteamento: os roteadores o usam para trocar informações sobre quais redes alcançam e a que distância. Ele escolhe a melhor rota pela **contagem de saltos**, com **máximo de 15 saltos**.

Ataques ao roteamento podem prejudicar o desempenho e a disponibilidade e até redirecionar o tráfego. Para proteger o RIP e outros protocolos de roteamento, usam-se **autenticação entre os roteadores** e correções e atualizações do sistema.

#### 15.2.5 NTP

O **NTP** (*Network Time Protocol*) **sincroniza os relógios dos dispositivos** com um servidor de tempo. A hora correta é essencial para rastrear eventos com precisão, interpretar os logs e validar certificados digitais, que têm prazo de validade.

Os criminosos atacam servidores de tempo para interromper comunicações que dependem de certificados e para esconder os horários do ataque. A proteção é a **autenticação NTP**, que confirma que o servidor de tempo é confiável.

### 15.3 Telnet, SSH e SCP

O **Telnet** e o **SSH** (*Secure Shell*) permitem acessar remotamente, por linha de comando, um dispositivo como um roteador. A diferença está na proteção:

| Característica | Telnet | SSH |
| --- | --- | --- |
| Criptografia | Nenhuma: usuário, senha e dados em texto claro | Forte: tudo criptografado |
| Porta | TCP 23 | TCP 22 |
| O que um sniffer vê | Usuário e senha legíveis | Apenas os endereços IP |
| Recomendação | Evitar | Usar sempre |

Exemplo: em uma captura com o Wireshark, a sessão Telnet mostra o nome de usuário e a senha do administrador por inteiro; na sessão SSH, o atacante só consegue ver o IP de quem acessou.

O **SCP** (*Secure Copy*) **transfere arquivos com segurança usando o SSH**, inclusive na autenticação, e garante a autenticidade e a confidencialidade dos dados em trânsito.

### 15.4 Protocolos Seguros

Protocolos antigos deixam a rede vulnerável, por isso os profissionais de segurança devem garantir que as **versões seguras** estejam em uso.

O **SNMP** (*Simple Network Management Protocol*) coleta estatísticas dos dispositivos para monitorar a rede. A versão atual, **SNMPv3**, usa criptografia para evitar espionagem e garante que os dados não foram alterados no caminho.

O **HTTP** (*Hypertext Transfer Protocol*), porta 80, oferece conectividade web básica, mas com pouca segurança: o conteúdo pode ser monitorado durante a transmissão. Para protegê-lo:

- o **SSL** (*Secure Sockets Layer*) negocia a criptografia em um processo inicial chamado **handshake**, no começo da sessão;
- o **TLS** (*Transport Layer Security*) é o **substituto atualizado e mais seguro do SSL**;
- quando o SSL/TLS protege a navegação, o endereço do site aparece com **HTTPS** em vez de HTTP.

O **FTP** (*File Transfer Protocol*) transfere arquivos, mas o cliente se conecta com usuário e senha em texto claro. O **FTPS** (*FTP Secure*) acrescenta SSL/TLS e evita interceptação, alteração e falsificação das mensagens.

No e-mail, o **POP** (*Post Office Protocol*), porta 110, e o **IMAP** (*Internet Message Access Protocol*), porta 143, baixam as mensagens, e o **MIME** (*Multipurpose Internet Mail Extensions*) permite anexar imagens e vídeos. Para protegê-los, usa-se SSL/TLS na transmissão. O **S/MIME** (*Secure/MIME*) envia mensagens **assinadas e criptografadas**, com autenticação, integridade e não repúdio.

### 15.5 Resumo de Protocolos Inseguros e Seguros

| Função | Protocolo inseguro | Alternativa segura |
| --- | --- | --- |
| Acesso remoto | Telnet (TCP 23) | SSH (TCP 22) |
| Cópia de arquivos | FTP | FTPS ou SCP |
| Navegação web | HTTP (porta 80) | HTTPS (SSL/TLS) |
| Gerenciamento | SNMPv1 e SNMPv2 | SNMPv3 |
| E-mail | POP (110), IMAP (143) sem criptografia | POP e IMAP com SSL/TLS; S/MIME |
| Resolução de nomes | DNS sem autenticação | DNSSEC |
| Tempo | NTP sem autenticação | NTP com autenticação |

## 16. Segmentação de Rede

A **segmentação** é a **divisão de uma rede em partes menores para melhorar o desempenho e a segurança**. Se um atacante entra em um segmento, ele não alcança automaticamente os outros.

### 16.1 VLANs

Uma **VLAN** (*Virtual Local Area Network* — rede local virtual) **agrupa dispositivos de forma lógica**, independentemente de onde estão ligados fisicamente. Os dispositivos de uma VLAN se comportam como se estivessem em uma rede própria, mesmo compartilhando a infraestrutura com outras VLANs.

**Importante:** VLAN não é o mesmo que LAN. A **LAN** é baseada em **conexões físicas**; a **VLAN**, em **conexões lógicas**.

Em um switch, cada porta pode ser atribuída a uma VLAN específica. Outras portas, chamadas de **troncos** (*trunks*), ligam os switches entre si e **transportam o tráfego de várias VLANs** ao mesmo tempo. Graças aos troncos, os funcionários de um mesmo setor podem estar em andares diferentes e ainda assim pertencer à mesma VLAN.

Os administradores criam VLANs por função, equipe ou aplicativo. Exemplo: o RH, que guarda dados confidenciais dos funcionários, fica em uma VLAN separada do resto da empresa, o que **reduz a chance de vazamento**.

As VLANs também limitam o tráfego de **broadcast** (mensagens enviadas a todos os dispositivos da rede), que fica restrito a cada VLAN. Como os atacantes também podem atacar o desempenho e a disponibilidade das VLANs, é preciso monitorá-las, usar configurações avançadas e aplicar correções regularmente.

### 16.2 Zona Desmilitarizada (DMZ)

A **DMZ** (*Demilitarized Zone* — zona desmilitarizada) é uma **pequena rede entre a rede privada confiável e a internet**. Nela ficam os servidores que precisam ser acessados de fora, como os **servidores web e de e-mail**. Assim, os visitantes da internet usam esses serviços sem chegar à rede interna.

A maioria das redes tem de **duas a quatro zonas de risco**:

| Zona | Risco | Confiança |
| --- | --- | --- |
| LAN privada | Baixo | Alta |
| Extranet (rede compartilhada com parceiros) | Médio-baixo | Médio-alta |
| DMZ | Médio-alto | Médio-baixa |
| Internet | Alto | Baixa |

Os firewalls controlam dois sentidos de tráfego:

- **leste-oeste**: tráfego entre os servidores dentro do data center da empresa;
- **norte-sul**: tráfego que entra e sai da rede da empresa.

### 16.3 Segmentação e Confiança Zero

Relembrando: na **confiança zero**, nenhum usuário ou dispositivo é confiável só por estar dentro da rede. A segmentação é a base técnica dessa abordagem: com a rede dividida, cada passagem de um segmento para outro é um ponto de controle, e um usuário confiável não circula livremente pela rede inteira.

| Característica | VLAN | DMZ |
| --- | --- | --- |
| O que separa | Grupos de usuários ou setores dentro da rede interna | Servidores públicos da rede interna |
| Onde fica | Dentro da LAN | Entre a LAN e a internet |
| Exemplo | VLAN do RH | Servidor web da empresa |

## 17. Segurança Sem Fio e de Dispositivos Móveis

Dispositivos sem fio e móveis são hoje a **maioria dos dispositivos nas redes**. Eles trazem mobilidade e conveniência, mas estão sujeitos a roubo, invasão, acesso remoto não autorizado, interceptação do tráfego (*sniffing*), ataques man-in-the-middle e ataques ao desempenho e à disponibilidade. A melhor forma de proteger uma rede sem fio é combinar **autenticação e criptografia**.

### 17.1 Padrões de Segurança Sem Fio

Os padrões de segurança das redes Wi-Fi evoluíram nesta ordem:

WEP → WPA → WPA2 → WPA3

| Padrão | Características | Situação |
| --- | --- | --- |
| WEP (*Wired Equivalent Privacy*) | Primeiro protocolo; chaves de 64 e 128 bits | Fraco, não usar |
| WPA (*Wi-Fi Protected Access*) | Chaves de 256 bits; MIC e TKIP | Substituiu o WEP |
| WPA2 | Lançado em 2004 (obrigatório na certificação Wi-Fi desde 2006); AES obrigatório; CCMP no lugar do TKIP | Seguro |
| WPA3 | Algoritmos mais robustos e troca de chaves melhorada | O mais atual |

O WPA trouxe duas melhorias importantes:

- **MIC** (*Message Integrity Check* — verificação de integridade da mensagem): detecta se um atacante capturou e alterou os dados entre o ponto de acesso e o cliente;
- **TKIP** (*Temporal Key Integrity Protocol*): melhorou a forma de tratar, proteger e trocar as chaves de criptografia.

No **WPA2**, o **AES** se tornou obrigatório, e o TKIP foi substituído pelo **CCMP** (*Counter Mode with Cipher Block Chaining Message Authentication Code Protocol*), com melhor gerenciamento de chaves e proteção. A configuração mais comum em casa é o **WPA-PSK** (*Pre-Shared Key*), em que todos usam a mesma senha da rede.

O **WPS** (*Wi-Fi Protected Setup*) foi criado para facilitar a conexão de dispositivos à rede doméstica, mas tem uma vulnerabilidade grave: o **PIN pode ser descoberto por força bruta**. Por isso, o WPS deve ser **desativado**.

### 17.2 Autenticação em Redes Sem Fio

O padrão sem fio original, 802.11, definiu **dois tipos de autenticação**:

- **sistema aberto**: qualquer dispositivo sem fio pode se conectar; só é usado quando a segurança não importa;
- **chave compartilhada**: oferece mecanismos para autenticar e criptografar os dados entre o cliente e o ponto de acesso.

O **ponto de acesso** (*access point*, AP) é o dispositivo que permite que os aparelhos sem fio se conectem à rede cabeada.

Relembrando: o **EAP** é uma estrutura de autenticação que admite vários métodos. Em uma rede sem fio, o processo ocorre da seguinte maneira:

1. o usuário pede para se conectar por meio do ponto de acesso;
2. o ponto de acesso pede o nome de usuário e o envia ao servidor de autenticação;
3. o servidor pede uma prova de que a identidade é válida;
4. o ponto de acesso pede ao usuário essa prova, na forma de senha;
5. o usuário envia a senha, que o ponto de acesso repassa ao servidor;
6. o servidor confirma que usuário e senha estão corretos e avisa o ponto de acesso e o usuário;
7. o usuário se conecta à rede sem fio.

Quatro métodos são usados com o EAP em redes sem fio:

| Método | Certificado no cliente | Certificado no servidor | Facilidade de implantação | Segurança |
| --- | --- | --- | --- | --- |
| EAP-TLS | Sim | Sim | Difícil | Alta |
| PEAP | Não | Sim | Moderada | Média |
| EAP-TTLS | Não | Sim | Moderada | Média |
| EAP-FAST | Não | Não | Fácil | Média |

**Importante:** o **EAP-TLS é o mais seguro e o mais difícil de implantar**, porque exige certificado tanto no cliente quanto no servidor.

### 17.3 Pontos de Acesso Não Autorizados e Autenticação Mútua

Qualquer dispositivo com uma interface sem fio e uma conexão à rede cabeada pode funcionar como ponto de acesso. Um **ponto de acesso não autorizado** (*rogue AP*) **imita um ponto de acesso legítimo** para que os usuários se conectem a ele.

Quando a vítima se conecta, o impostor pode copiar os dados do dispositivo e roubar credenciais. É um ataque man-in-the-middle **muito difícil de detectar**.

A proteção é a **autenticação mútua**, uma autenticação de duas vias em que **as duas pontas se autenticam antes de se conectar**. Assim, o cliente também confere o ponto de acesso e percebe quando ele é falso.

### 17.4 Comunicação dos Dispositivos Móveis

Os dispositivos móveis se conectam ao provedor de serviço pela rede celular (como LTE e 5G) e usam ainda outras formas de comunicação:

| Método | Como funciona | Exemplo |
| --- | --- | --- |
| Wi-Fi e Bluetooth | Sinais sem fio configurados no menu do aparelho | Fone de ouvido, som do carro |
| NFC (*Near-Field Communication* — comunicação por proximidade) | Campos eletromagnéticos de curtíssimo alcance | Pagamento por aproximação |
| Infravermelho (IR) | Comunicação de curto alcance com um receptor IR | Controlar a TV pelo celular |
| USB | O único com fio da lista | Armazenamento, modem, coleta forense |

### 17.5 Gerenciamento de Dispositivos Móveis

Um aparelho fornecido pela empresa pode guardar dados pessoais e da organização. No modelo **COPE** (*Corporate-Owned, Personally Enabled*), o aparelho é da empresa, mas o uso pessoal é permitido; no **BYOD**, o aparelho é do funcionário. Nos dois casos, as políticas de segurança precisam valer para os dados corporativos.

As principais formas de gerenciar dispositivos móveis são:

- **segmentação do armazenamento e conteinerização**: criam uma área autenticada e criptografada que **separa os dados da empresa dos dados pessoais**; permitem isolar aplicativos, controlar suas funções, apagar só o contêiner e bloquear ou limpar o aparelho remotamente;
- **gerenciamento de conteúdo**: controla o risco de aplicativos que compartilham dados, como Dropbox, Box, Google Drive e iCloud, com um sistema de gerenciamento de identidades que define o que cada usuário acessa;
- **gerenciamento de aplicativos**: a **lista de permissões** (*whitelisting*) autoriza, por assinatura digital, apenas os aplicativos que podem ser instalados, garantindo que venham de fontes confiáveis; aplicativos que pedem credenciais devem usar senhas fortes.

### 17.6 Ameaças e Proteções dos Dispositivos Móveis

As ameaças aos dispositivos móveis incluem roubo, perda, acesso não autorizado e riscos ligados ao sistema operacional, aos aplicativos e à rede.

Alguns usuários tentam **contornar as limitações do aparelho** para instalar aplicativos não autorizados:

| Técnica | Plataforma | O que faz | Risco |
| --- | --- | --- | --- |
| Jailbreak | Apple | Remove a restrição de só rodar aplicativos autorizados pela Apple | Alto |
| Root | Android | Ignora a arquitetura de segurança e dá acesso administrativo total | Alto |
| Sideloading | Ambas | Instala aplicativos fora da loja aprovada, como em lojas de terceiros | Menor, mas existe |

Existem soluções que detectam aparelhos com jailbreak ou root; o dispositivo é marcado como fora das regras e removido da rede ou impedido de acessar os aplicativos da organização.

As proteções para dispositivos móveis são:

- **bloqueio de tela** com senha, PIN ou padrão;
- **autenticação biométrica** (digital, rosto, íris ou voz);
- **autenticação com reconhecimento de contexto**: usa aprendizado de máquina para liberar o acesso com base no comportamento normal do usuário;
- **limpeza remota**: apaga os dados se o aparelho for roubado ou perdido;
- **criptografia completa do dispositivo**.

### 17.7 Rastreamento por GPS

O **GPS** (*Global Positioning System* — Sistema de Posicionamento Global) usa satélites para determinar a localização de um aparelho, com precisão de cerca de **5 metros**.

Muitos aplicativos usam o GPS, por exemplo para fazer check-in em lugares numa rede social. A delimitação geográfica permite que empresas da região enviem **notificações push** (mensagens que aparecem no aparelho sem que o usuário abra o aplicativo) com propaganda conforme a localização.

**Importante:** criminosos digitais passaram a usar **notificações push para capturar dados** dos usuários.

## 18. Resiliência e Alta Disponibilidade

A **resiliência** é o conjunto de métodos e configurações que tornam um sistema ou uma rede **tolerante a falhas**: capaz de continuar funcionando mesmo quando algo dá errado, inclusive durante um ataque. O objetivo é **reduzir ao mínimo o tempo de inatividade** dos processos críticos, que prejudica a produtividade e a receita.

### 18.1 Alta Disponibilidade

A **alta disponibilidade** descreve sistemas **projetados para evitar períodos de inatividade**. Esses sistemas seguem três princípios de projeto:

1. **eliminar os pontos únicos de falha**, com equipamentos de reserva prontos para assumir (*hot standby*), componentes redundantes e vários caminhos de conexão;
2. **garantir uma transição confiável**, com fontes de energia redundantes e sistemas de energia e de comunicação de reserva;
3. **detectar as falhas assim que ocorrem**, com monitoramento ativo que pode até acionar sozinho o sistema de reserva.

Relembrando: o **ponto único de falha** (*Single Point of Failure*, SPOF) é qualquer parte cuja falha derruba o sistema inteiro. Pode ser um equipamento, um processo, um dado específico, um serviço essencial ou até uma pessoa da equipe de TI que só ela sabe fazer algo. A solução é **não depender de um único elemento**, criando componentes redundantes que assumem quando um falha.

Três conceitos sustentam a alta disponibilidade:

| Conceito | Ideia | Exemplo |
| --- | --- | --- |
| Redução de pontos únicos de falha | Ter processos, recursos e componentes de reserva | Cluster de alta disponibilidade |
| Tolerância a falhas | Continuar funcionando quando um componente falha | Espelhamento de dados |
| Resiliência do sistema | Manter dados e processamento disponíveis mesmo sob ataque | Energia e processamento redundantes |

Em um **cluster de alta disponibilidade**, vários computadores com o mesmo armazenamento e configurações idênticas atendem o mesmo serviço ao mesmo tempo. Se um falha, os outros continuam.

### 18.2 Os Cinco Noves

Uma das metas mais conhecidas de alta disponibilidade são os **cinco noves**: **99,999% de disponibilidade**, o que significa **menos de 5,26 minutos de inatividade por ano**.

#### 18.2.1 Exemplo Resolvido: Tempo de Inatividade nos Cinco Noves

Um ano tem 365 × 24 × 60 = 525.600 minutos. A inatividade permitida é de 100% − 99,999% = 0,001%.

| Etapa | Cálculo | Resultado |
| --- | --- | --- |
| Minutos no ano | 365 × 24 × 60 | 525.600 min |
| Fração de inatividade | 0,001% = 0,00001 | 0,00001 |
| Inatividade máxima | 525.600 × 0,00001 | 5,256 min ≈ 5,26 min |

As medidas mais comuns para chegar aos cinco noves são:

- **sistemas padronizados**: usam os mesmos componentes, o que facilita o inventário de peças e a troca em emergências;
- **clustering**: vários dispositivos agrupados aparecem para o usuário como um só; se um falha, os outros seguem disponíveis;
- **sistemas de componentes compartilhados**: um sistema completo pode substituir outro que falhou.

### 18.3 Redundância N+1

Na **redundância N+1**, os componentes necessários (**N**) têm **pelo menos um componente de reserva (+1)**. A analogia é o carro: quatro pneus (N) e um estepe (+1) no porta-malas.

Em um data center, N+1 significa ter, por exemplo, um servidor, uma fonte de energia, um switch e um roteador de reserva, prontos para entrar em funcionamento se o principal falhar.

**Observação:** N+1 tem equipamento redundante, mas **não é um sistema totalmente redundante**: ele suporta a perda de um componente, não de todos.

### 18.4 RAID

O **RAID** (*Redundant Array of Independent Disks*) **distribui os dados entre vários discos**. Dependendo do tipo, permite recuperar os dados se um disco falhar e torna a leitura mais rápida, porque vários discos trabalham ao mesmo tempo. Pode ser feito por software ou por uma controladora de hardware dedicada.

O RAID combina três técnicas:

| Técnica | Como funciona | Protege contra falha de disco? |
| --- | --- | --- |
| Espelhamento | Grava os dados duplicados em um segundo disco | Sim |
| Distribuição (*striping*) | Espalha partes seguidas dos dados por discos diferentes | Não, sozinha |
| Paridade | Calcula somas de verificação dos dados distribuídos e as guarda em outro disco, para reconstruir o que se perder | Sim |

**Importante:** o **RAID 0 usa apenas distribuição e não tem redundância**: se um disco falhar, os dados se perdem. Quem protege contra falha de disco são os tipos com espelhamento (como o RAID 1) ou com paridade (como o RAID 5).

### 18.5 Spanning Tree Protocol (STP)

A redundância física entre switches, com mais de um cabo ligando os mesmos pontos, protege contra a falha de um cabo ou de um switch. Mas ela cria **loops**: os quadros ficam circulando sem parar e se duplicam, o que pode derrubar a rede.

O **STP** (*Spanning Tree Protocol*) **evita loops quando os switches se interligam por vários caminhos**. Ele **bloqueia de propósito os caminhos redundantes**, deixando apenas um caminho lógico ativo entre os destinos. Os cabos continuam ligados, prontos para uso.

Se um cabo ou um switch falha, o STP recalcula os caminhos e **desbloqueia a porta necessária** para que o caminho redundante assuma. Exemplo:

1. o PC1 envia uma mensagem de broadcast pela rede;
2. o tronco entre os switches S2 e S1 falha, interrompendo o caminho original;
3. o S2 desbloqueia a porta que estava bloqueada e o tráfego segue pelo caminho alternativo;
4. quando o link entre S2 e S1 volta, o STP bloqueia de novo o caminho alternativo.

### 18.6 Redundância de Roteador

O **gateway padrão** é o roteador que dá aos dispositivos acesso ao resto da rede e à internet. Se houver um único roteador nesse papel, ele é um ponto único de falha.

A solução é instalar um **roteador de reserva** (*standby*). Os dois roteadores usam um protocolo de redundância para decidir qual fica ativo:

- cada roteador tem o seu endereço IP físico e os dois compartilham um **endereço IP virtual**;
- os dispositivos usam o **IP virtual como gateway padrão**;
- os roteadores trocam mensagens periódicas pelos IPs físicos para confirmar que estão funcionando;
- se o roteador de reserva para de receber as mensagens do ativo, ele assume o encaminhamento.

Exemplo: os computadores usam o gateway virtual 192.0.2.100. Quando o roteador ativo cai, o de reserva assume o mesmo IP virtual, e os computadores continuam conectados sem mudar nada.

A capacidade de a rede se recuperar sozinha da falha do gateway padrão é chamada de **redundância de primeiro salto**. Exemplos de protocolos que fazem isso são o HSRP (da Cisco), o VRRP e o GLBP.

### 18.7 Redundância de Local

Dependendo das necessidades, a organização pode manter uma cópia dos dados em outro local:

| Tipo de replicação | Sincronização | Largura de banda | Distância entre os locais |
| --- | --- | --- | --- |
| Síncrona | Em tempo real | Alta | Pequena, para reduzir a latência |
| Assíncrona | Quase em tempo real | Menor | Pode ser maior |
| Ponto no tempo (*point-in-time*) | Atualizações periódicas | A menor, sem conexão constante | Qualquer |

A escolha depende do **equilíbrio entre custo e disponibilidade**.

### 18.8 Design Resiliente

O **design resiliente** é **mais do que adicionar redundância**: é entender as necessidades do negócio e ajustar a rede para que a recuperação seja rápida. Exemplo: com links redundantes e STP, a troca para o caminho alternativo pode demorar se a configuração não for ideal; ajustes testados em uma rede de testes podem tornar a transição imperceptível.

A **resiliência de aplicativos** é a capacidade de um aplicativo continuar funcionando quando um de seus componentes falha. Há três soluções, e **quanto maior a disponibilidade, maiores a complexidade e o custo**:

| Solução | Como funciona | Complexidade e custo |
| --- | --- | --- |
| Hardware tolerante a falhas | Vários componentes essenciais no mesmo computador | Os maiores |
| Arquitetura de cluster | Grupo de servidores que funciona como um só | Intermediários |
| Backup e restauração | Cópias dos arquivos para restaurar em caso de perda | Os menores |

Os roteadores e switches Cisco têm um recurso de **configuração resiliente do IOS** (o sistema operacional desses equipamentos). Ele guarda uma cópia segura da imagem do sistema e do arquivo de configuração em execução, chamada de **bootset primário**, que o usuário não consegue apagar. Assim, se alguém formatar a memória flash ou apagar a configuração, por acidente ou de propósito, a recuperação é rápida. Os comandos são secure boot-image e secure boot-config.

### 18.9 Backups

O **backup** guarda uma cópia das informações em uma mídia, geralmente removível, mantida em local seguro. É **uma das formas mais eficazes de proteger contra a perda de dados**, seja por roubo, falha de equipamento ou desastre. Uma boa política de segurança inclui backups regulares.

Ao planejar os backups, devem ser considerados:

- **frequência**: é comum fazer um backup completo semanal ou mensal e backups parciais frequentes do que mudou; muitos backups parciais, porém, aumentam o tempo de restauração;
- **armazenamento**: levar os backups para um local externo aprovado, em rodízio diário, semanal ou mensal, conforme a política;
- **segurança**: proteger os backups com senha;
- **validação**: sempre conferir os backups para garantir a integridade dos dados.

### 18.10 Energia

O fornecimento contínuo de energia elétrica é essencial para os data centers. As regras gerais para um bom sistema de energia são:

- alimentar o data center separadamente do resto do prédio;
- ter fontes redundantes, vindas de duas ou mais subestações;
- usar condicionamento de energia;
- ter sistemas de energia de reserva;
- ter um **nobreak** (UPS, *Uninterruptible Power Supply*) para desligar os sistemas corretamente.

Os principais eventos de energia são:

| Categoria | Evento | O que é |
| --- | --- | --- |
| Excesso | Pico (*spike*) | Alta tensão momentânea |
| Excesso | Sobretensão (*surge*) | Alta tensão prolongada |
| Perda | Falha (*fault*) | Perda momentânea de energia |
| Perda | Blecaute (*blackout*) | Perda completa de energia |
| Degradação | Afundamento (*sag* ou *dip*) | Baixa tensão momentânea |
| Degradação | Subtensão (*brownout*) | Baixa tensão prolongada |
| Degradação | Corrente de partida (*inrush*) | Pico inicial de corrente ao ligar um equipamento |

**Importante:** as palavras que mais confundem são as que indicam duração. **Pico** e **afundamento** são **momentâneos**; **sobretensão** e **subtensão** são **prolongadas**.

### 18.11 Climatização (HVAC)

Os sistemas de **HVAC** (*Heating, Ventilation and Air Conditioning* — aquecimento, ventilação e ar-condicionado) controlam a **temperatura, a umidade e a circulação do ar**, protegendo pessoas e equipamentos.

Quase todo equipamento de TI tem faixas aceitáveis de temperatura e umidade, informadas na especificação do produto ou no guia de planejamento físico. Respeitar essas faixas evita falhas e prolonga a vida útil dos sistemas.

**Observação:** os sistemas de HVAC modernos se conectam à internet para monitoramento remoto e costumam ser acessados por fornecedores terceirizados. Quanto mais pessoas têm as credenciais, menos seguro o sistema fica, e uma invasão pelo HVAC pode virar porta de entrada para a rede da empresa.

## 19. Sistemas Embarcados, IoT e Tecnologias de Dissimulação

Além de computadores e celulares, as redes ligam hoje **máquinas industriais, sensores, carros, equipamentos médicos e drones**. Esses sistemas têm fragilidades próprias e ampliam muito a superfície de ataque. Esta seção também apresenta as tecnologias que enganam o atacante de propósito.

### 19.1 Infraestruturas Críticas e SCADA

Setores como fabricação, energia, comunicações, transportes e serviços financeiros dependem de sistemas de controle. Um ataque a eles pode **derrubar usinas, telecomunicações ou sistemas de transporte**.

O **SCADA** (*Supervisory Control and Data Acquisition* — controle de supervisão e aquisição de dados) é usado para **controlar e monitorar processos industriais**. Ele faz parte dos **ICS** (*Industrial Control Systems* — sistemas de controle industrial), presentes na manufatura, na produção, na energia e nas comunicações.

O ataque **Stuxnet** mostrou, em 2010, que um ataque digital pode destruir ou interromper infraestruturas essenciais: ele mirou justamente sistemas SCADA.

Os ambientes SCADA são vulneráveis porque **foram projetados sem conexão com a rede corporativa e a internet**, e por isso a segurança digital não foi pensada desde o início. Hoje, as empresas querem coletar dados desses sistemas para melhorar as operações e conectam o SCADA à rede corporativa, o que aumenta o risco.

**Importante:** a principal proteção é **separar a rede SCADA da rede local da empresa**, segregando as redes internas e externas.

### 19.2 Internet das Coisas (IoT)

A **IoT** (*Internet of Things* — Internet das Coisas) é o conjunto de tecnologias que **conectam objetos variados à internet**: carros, máquinas industriais, robôs, fechaduras, motores, câmeras, lâmpadas e sensores.

Como esses dispositivos precisam ser acessados remotamente, eles ficam on-line e **aumentam o número de pontos de entrada na rede**. A IoT, a nuvem e a virtualização também fizeram crescer muito a quantidade de dados, dando origem ao **Big Data**.

Dispositivos IoT infectados com malware já foram usados em alguns dos maiores ataques de negação de serviço distribuído (**DDoS**, *Distributed Denial of Service*, em que muitos aparelhos atacam um alvo ao mesmo tempo) da história. Por esse motivo:

- avaliar se cada dispositivo IoT aceita atualização de firmware com correções de segurança, de preferência pela rede sem fio;
- **trocar sempre as credenciais padrão de administrador**, que são publicamente conhecidas.

Os dispositivos IoT costumam usar um **RTOS** (*Real-Time Operating System* — sistema operacional de tempo real): um sistema pequeno, que troca rapidamente de tarefa e prioriza o **tempo exato de resposta**, e não o volume de dados. Ele está em dispositivos vestíveis, equipamentos médicos, sistemas de veículos e automação residencial. Suas vulnerabilidades incluem:

- injeção de código;
- ataques de negação de serviço;
- inversão de prioridade: uma tarefa de prioridade alta fica esperando por uma de prioridade baixa.

Os dispositivos IoT se comunicam por métodos de curto, médio e longo alcance, como celular (4G e 5G), rádio e **Zigbee** (conjunto de protocolos sem fio para redes pessoais, as WPANs). O **Shodan** é um buscador de dispositivos IoT que mostra se um aparelho de automação residencial está exposto.

Para proteger dispositivos IoT:

- proteger a rede sem fio;
- saber exatamente quais dispositivos se comunicam na rede e o que cada um faz;
- instalar software de segurança nos dispositivos sempre que possível;
- proteger os celulares e aplicativos usados para controlar os dispositivos.

### 19.3 Sistemas Embarcados

Os **sistemas embarcados** (ou integrados) são computadores dedicados a uma função, dentro de outro equipamento, que **capturam, armazenam e acessam dados**. Estão em TVs inteligentes, climatização, equipamentos médicos e carros.

Eles são vulneráveis a **ataques de tempo**: o atacante descobre fraquezas medindo **quanto tempo o sistema leva para responder** a entradas diferentes. O ataque de tempo é um tipo de **ataque de canal lateral**, que não explora falhas do software, e sim informações que vazam do funcionamento físico: tempo, consumo de energia, emissões eletromagnéticas ou até som.

Muitos embarcados usam a tecnologia **SoC** (*System on Chip*), módulos de hardware pequenos (*Small Form Factor*, SFF), como o Raspberry Pi e o Arduino. Um SoC reúne microcontrolador, processador e periféricos, como placa gráfica e Wi-Fi, e pode rodar Windows, Linux ou Android. Alguns usam um **FPGA** (*Field-Programmable Gate Array*), um circuito que pode ser reprogramado depois de instalado.

**Importante:** muitos dispositivos SoC têm **autenticação fraca e não podem ser atualizados ou corrigidos**. Como não existe um programa formal para verificar sua segurança, é preciso confiar neles de forma implícita.

### 19.4 Voz sobre IP (VoIP)

O **VoIP** (*Voice over IP* — voz sobre IP) **usa redes de dados, como a internet, para fazer ligações telefônicas**. As opções de equipamento são:

- telefone tradicional com um adaptador, que liga o aparelho analógico à linha digital;
- telefone próprio para VoIP;
- software de VoIP instalado no computador.

A segurança do VoIP **depende da segurança da rede por baixo dele**: se a rede cai, a voz cai junto. Os criminosos atacam o VoIP para fazer ligações de graça, espionar conversas e prejudicar o serviço.

As medidas de proteção do VoIP são:

- criptografar os pacotes de voz contra espionagem;
- usar SSH para proteger gateways e switches;
- trocar todas as senhas padrão;
- usar um sistema de detecção de intrusão para identificar ataques como o envenenamento ARP;
- usar autenticação forte contra três ataques: falsificação de registro (o criminoso desvia para si as chamadas da vítima), personificação de proxy (a vítima conversa com um proxy falso) e sequestro de chamada (a chamada é interceptada e desviada no caminho);
- usar firewalls que reconheçam VoIP para monitorar o tráfego e filtrar sinais anormais.

### 19.5 Sistemas de Finalidade Específica

Os sistemas embarcados de finalidade específica aparecem em setores como saúde, indústria automotiva e aviação:

| Setor | Exemplos | Riscos | Proteções |
| --- | --- | --- | --- |
| Saúde | Marca-passos, bombas de insulina, implantes, desfibriladores, com conexão sem fio, monitoramento remoto e NFC | Segurança do paciente, vazamento de prontuários, porta de entrada para a rede | Atualização e isolamento dos dispositivos |
| Automotivo | Sistemas que registram velocidade, localização e frenagem e podem enviar os dados à seguradora | Rastreamento não autorizado, interferência sem fio, falsificação | Software projetado com segurança, criptografia entre os controladores, firewall |
| Aviação | Controle de voo e comunicação da aeronave | Credenciais fixas no código, protocolos inseguros, *backdoors* | Protocolos seguros e revisão do software |
| Drones (UAV) | Fotografia aérea, vigilância, agricultura, mapeamento | Sequestro, ataques ao Wi-Fi, falsificação de GPS, bloqueio de sinal, ataques de autenticação | Autenticação forte e proteção dos sinais |

Um **backdoor** (porta dos fundos) é um acesso escondido que contorna a autenticação normal.

### 19.6 Tecnologias de Dissimulação

As **tecnologias de dissimulação** (*deception*) acrescentam **uma camada falsa à infraestrutura** para enganar o atacante. Elas servem para distraí-lo das redes reais, aprender seus métodos e alertar sobre ataques que podem ser lançados contra a rede.

| Tecnologia | O que é |
| --- | --- |
| Honeypot | Sistema-isca que imita um servidor e fica exposto de propósito; as ações do atacante são registradas e analisadas |
| Honeynet | Conjunto de honeypots que imita uma rede inteira |
| Honey files | Arquivos falsos que atraem o atacante, mas não têm informações reais |
| DNS sinkhole | Impede a resolução de nomes de sites específicos, afastando os usuários de recursos mal-intencionados |

**Observação:** o honeypot não protege diretamente nenhum ativo. Seu valor está em **desviar o atacante dos recursos reais e revelar como ele age**.

## 20. Listas de Controle de Acesso (ACLs) e Máscaras Curinga

Um condomínio fechado tem um porteiro que só abre o portão para quem está na lista de visitantes. Na rede, o papel desse porteiro é feito pela **ACL**, que decide quais pacotes podem passar por um roteador.

### 20.1 O que é uma ACL

Relembrando: o roteador decide para onde encaminhar um pacote olhando o **endereço IP de destino** no cabeçalho e comparando-o com a tabela de roteamento. O mesmo hábito de olhar o cabeçalho também pode ser usado para **filtrar** pacotes.

A **ACL** (*Access Control List* — lista de controle de acesso) é uma **série de comandos que filtra pacotes de acordo com as informações do cabeçalho**. Cada linha da lista é uma instrução de permitir (*permit*) ou negar (*deny*), chamada de **ACE** (*Access Control Entry* — entrada de controle de acesso).

Por padrão, o roteador não tem nenhuma ACL. Quando uma ACL é aplicada a uma interface, o roteador **compara cada pacote que passa com as ACEs, em ordem**. Esse processo se chama **filtragem de pacotes** e atua nas **camadas 3 (rede) e 4 (transporte)** do modelo OSI.

As ACLs têm usos variados:

- limitar o tráfego para melhorar o desempenho: bloquear vídeo, por exemplo;
- controlar o fluxo de tráfego: aceitar atualizações de roteamento só de fontes conhecidas;
- dar segurança básica de acesso: permitir a rede do RH apenas para pessoas autorizadas;
- filtrar por tipo de tráfego: permitir e-mail e negar Telnet;
- escolher quais hosts usam um serviço: liberar FTP ou HTTP só para certos grupos;
- dar prioridade a certas classes de tráfego, como a voz.

### 20.2 Tipos de ACL

Os roteadores Cisco trabalham com dois tipos de ACL IPv4:

- **ACL padrão** (*standard*): filtra **apenas pelo endereço IPv4 de origem** (camada 3);
- **ACL estendida** (*extended*): filtra pelos endereços IPv4 de **origem e/ou destino** (camada 3), pelas **portas TCP e UDP** e pelo tipo de protocolo (camada 4).

Cada ACL é identificada por um número ou por um nome. Os números indicam o tipo:

- ACL padrão → 1 a 99 e 1300 a 1999;
- ACL estendida → 100 a 199 e 2000 a 2699.

As **ACLs nomeadas** são o **método preferido**, porque o nome mostra a finalidade da lista. Exemplo: FTP-FILTER diz muito mais do que o número 100. As regras para o nome são:

- indicar o objetivo da ACL;
- usar letras e números;
- não usar espaços nem pontuação;
- de preferência, escrever em MAIÚSCULAS.

Nas ACLs nomeadas também é possível incluir e excluir entradas individualmente.

| Característica | ACL padrão | ACL estendida |
| --- | --- | --- |
| Camadas analisadas | 3 | 3 e 4 |
| Endereço | Só origem | Origem e/ou destino |
| Portas e protocolo | Não | Sim |
| Números | 1–99 e 1300–1999 | 100–199 e 2000–2699 |

### 20.3 Como a ACL Processa os Pacotes

Uma ACL pode ser aplicada em dois sentidos de uma interface:

- **ACL de entrada** (*inbound*): filtra o pacote **antes** de ele ser roteado. É mais eficiente, porque o roteador não perde tempo procurando a rota de um pacote que vai ser descartado. É usada quando só a rede ligada àquela interface precisa ser examinada;
- **ACL de saída** (*outbound*): filtra o pacote **depois** de ele ser roteado, não importa por qual interface ele entrou. É usada quando o mesmo filtro vale para pacotes que chegam de várias interfaces e saem pela mesma.

De forma simplificada, o processo de uma ACL padrão de entrada ocorre da seguinte maneira:

1. o roteador extrai o endereço IPv4 de origem do pacote;
2. compara esse endereço com cada ACE, **de cima para baixo**;
3. na **primeira correspondência**, executa a ação (permite ou nega) e para de comparar;
4. se nenhuma ACE corresponder, o pacote é descartado.

O descarte do último passo acontece porque toda ACL termina com uma **negação implícita**: uma instrução oculta que **nega tudo o que não foi permitido**.

**Importante:** por causa da negação implícita, **toda ACL precisa ter pelo menos uma instrução de permitir**. Caso contrário, ela bloqueia todo o tráfego.

**Observação:** as ACLs **não filtram os pacotes criados pelo próprio roteador**, como as atualizações de roteamento que ele envia.

### 20.4 Máscaras Curinga

Para dizer à ACL quais endereços ela deve considerar, usa-se uma **máscara curinga** (*wildcard mask*), de 32 bits, que **indica quais bits do endereço devem ser verificados**. Ela também é usada em outros recursos, como o protocolo de roteamento OSPF.

Na máscara de sub-rede, que indica qual parte do endereço IP identifica a rede, o bit 1 marca a parte de rede e o bit 0 marca a parte de host. A máscara curinga segue a **lógica inversa**:

- bit **0** → o bit correspondente do endereço **precisa corresponder** (é verificado);
- bit **1** → o bit correspondente do endereço **é ignorado**.

A tabela mostra o efeito de algumas máscaras curinga no último octeto:

| Máscara curinga | Último octeto em binário | Efeito no último octeto |
| --- | --- | --- |
| 0.0.0.0 | 00000000 | Verifica todos os bits |
| 0.0.0.15 | 00001111 | Verifica os 4 primeiros bits e ignora os 4 últimos |
| 0.0.0.63 | 00111111 | Verifica os 2 primeiros bits e ignora os 6 últimos |
| 0.0.0.252 | 11111100 | Ignora os 6 primeiros bits e verifica os 2 últimos |
| 0.0.0.255 | 11111111 | Ignora o octeto inteiro |

Nos três primeiros octetos dessas máscaras, o valor 0 faz com que todos os bits sejam verificados.

Exemplos de uso:

- um único host: `access-list 10 permit 192.168.1.1 0.0.0.0`;
- uma sub-rede inteira: `access-list 10 permit 192.168.1.0 0.0.0.255`, que vale para os hosts de 192.168.1.0 a 192.168.1.255 (na prática, os hosts de .1 a .254);
- um intervalo de redes: `192.168.16.0 0.0.15.255`, que vale para as redes de 192.168.16.0/24 a 192.168.31.0/24.

### 20.5 Exemplo Resolvido: Cálculo de Máscaras Curinga

O atalho para calcular a máscara curinga é **subtrair a máscara de sub-rede de 255.255.255.255**, octeto por octeto.

| Situação | Máscara de sub-rede | Cálculo | Máscara curinga | Comando |
| --- | --- | --- | --- | --- |
| Rede 192.168.3.0/24 | 255.255.255.0 | 255 − 0 = 255 no último octeto | 0.0.0.255 | `permit 192.168.3.0 0.0.0.255` |
| Rede 192.168.3.32/28 (14 usuários) | 255.255.255.240 | 255 − 240 = 15 | 0.0.0.15 | `permit 192.168.3.32 0.0.0.15` |
| Redes 192.168.10.0 e 192.168.11.0, juntas como 192.168.10.0/23 | 255.255.254.0 | 255 − 254 = 1; 255 − 0 = 255 | 0.0.1.255 | `permit 192.168.10.0 0.0.1.255` |
| Redes 192.168.16.0 a 192.168.31.0, juntas como 192.168.16.0/20 | 255.255.240.0 | 255 − 240 = 15; 255 − 0 = 255 | 0.0.15.255 | `permit 192.168.16.0 0.0.15.255` |

A conferência em binário mostra por que o segundo caso funciona. No último octeto:

| Item | Binário | Decimal |
| --- | --- | --- |
| Endereço 192.168.3.**32** | 0010 0000 | 32 |
| Curinga 0.0.0.**15** | 0000 1111 | 15 |
| Bits verificados (os 4 primeiros) | 0010 xxxx | — |
| Menor endereço que corresponde | 0010 0000 | 32 |
| Maior endereço que corresponde | 0010 1111 | 47 |

Portanto, `192.168.3.32 0.0.0.15` corresponde aos endereços de **192.168.3.32 a 192.168.3.47**, que é exatamente a sub-rede /28.

O mesmo raciocínio vale para o quarto caso, aplicado ao terceiro octeto: 16 = 0001 0000 e 15 = 0000 1111. Os 4 primeiros bits (0001) são verificados, e os valores possíveis vão de 0001 0000 (16) a 0001 1111 (31).

**Observação:** no material do curso, os comandos do terceiro e do quarto caso aparecem trocados por `192.168.3.0 0.0.0.255`. Os comandos corretos são os da tabela.

### 20.6 Palavras-chave host e any

Duas palavras-chave substituem as máscaras curinga mais comuns:

- **host** → equivale à máscara **0.0.0.0** e indica **um único endereço**. Exemplo: `access-list 10 permit host 192.168.10.10`;
- **any** → equivale a 0.0.0.0 255.255.255.255 e indica **qualquer endereço**. Exemplo: `access-list 11 permit any`.

## 21. Configuração e Aplicação de ACLs

Depois de entender o que a ACL faz e como as máscaras curinga escolhem os endereços, o passo seguinte é escrever a lista no roteador, aplicá-la no lugar certo e corrigi-la quando necessário.

### 21.1 Planejamento

A Cisco recomenda preparar a ACL antes de digitá-la no equipamento, sobretudo quando ela tem muitas entradas. As etapas são:

1. escrever, em um editor de texto, o que a política deve fazer;
2. acrescentar os comandos correspondentes;
3. incluir comentários (*remarks*) para documentar a ACL;
4. copiar e colar os comandos no dispositivo;
5. testar a ACL com cuidado.

### 21.2 ACL Padrão

A ACL padrão numerada é criada com o comando:

`access-list número {deny | permit | remark texto} origem [curinga] [log]`

Seus parâmetros são:

- número: 1 a 99 ou 1300 a 1999;
- deny ou permit: nega ou permite;
- remark: comentário de até 100 caracteres;
- origem: um endereço, a palavra **host** com um endereço, ou **any**;
- curinga: se for omitida, vale 0.0.0.0;
- log: gera uma mensagem quando um pacote corresponde à ACE.

A mensagem do **log** informa o número da ACL, a condição, o endereço de origem e o número de pacotes. Como ele **consome muito processamento**, deve ser usado só para resolver problemas ou investigar ataques.

Para remover a ACL inteira, usa-se `no access-list número`.

A ACL padrão nomeada é criada com `ip access-list standard NOME`. O roteador entra em um modo próprio de configuração, e as ACEs são digitadas em seguida, sem repetir o comando a cada linha. O nome diferencia maiúsculas de minúsculas e precisa ser único. Para removê-la: `no ip access-list standard NOME`.

### 21.3 ACL Estendida

A ACL estendida numerada é criada com o comando:

`access-list número {deny | permit | remark texto} protocolo origem curinga [operador porta] destino curinga [operador porta] [established] [log]`

Seus parâmetros adicionais são:

- número: 100 a 199 ou 2000 a 2699;
- protocolo: **ip** (todos), **tcp**, **udp** ou **icmp**, que correspondem aos números de protocolo 1 (ICMP), 6 (TCP) e 17 (UDP);
- operador: **eq** (igual), **neq** (diferente), **lt** (menor que) e **gt** (maior que), usados com o número ou o nome da porta;
- established: só para TCP.

As portas podem ser escritas por número ou por nome:

| Nome | Porta | Serviço |
| --- | --- | --- |
| ftp-data | 20 | Dados do FTP |
| ftp | 21 | Controle do FTP |
| telnet | 23 | Telnet |
| smtp | 25 | Envio de e-mail |
| tacacs | 49 | TACACS+ |
| domain | 53 | DNS |
| www | 80 | HTTP |
| pop3 | 110 | Recebimento de e-mail |
| bgp | 179 | BGP |

**Importante:** o SSH (porta 22) e o HTTPS (porta 443) **não têm nome na lista** e precisam ser escritos pelo número.

A ACL estendida nomeada é criada com `ip access-list extended NOME`. Exemplo de uma ACL que só deixa a rede 192.168.10.0/24 navegar na web:

```
ip access-list extended SURFING
 permit tcp 192.168.10.0 0.0.0.255 any eq 80
 permit tcp 192.168.10.0 0.0.0.255 any eq 443
```

**Observação:** nas ACLs estendidas, as ACEs ficam **na ordem em que foram digitadas**. Nas ACLs padrão, o próprio sistema pode reorganizar as entradas de host.

### 21.4 A Palavra-chave established

A palavra-chave **established** permite que o tráfego da rede interna saia e que **apenas as respostas a esse tráfego voltem**. Ela funciona como uma forma simples de firewall.

Uma conexão TCP é aberta com o *three-way handshake* (troca de três mensagens: SYN, SYN-ACK e ACK), e depois disso os segmentos levam o sinalizador ACK ativado. O **established** considera correspondente o segmento que tem o sinalizador **ACK ou RST** ativado, ou seja, que pertence a uma conexão já existente. Uma conexão TCP iniciada de fora é negada.

Exemplo, que completa a ACL SURFING:

```
ip access-list extended BROWSING
 permit tcp any 192.168.10.0 0.0.0.255 established
interface g0/0/0
 ip access-group SURFING in
 ip access-group BROWSING out
```

Nesse exemplo, a rede 192.168.10.0/24 fica ligada à interface G0/0/0. A SURFING filtra o que entra no roteador vindo da rede, e a BROWSING filtra o que sai do roteador em direção à rede, deixando passar apenas as respostas das conexões abertas por ela.

### 21.5 Aplicação nas Interfaces e nas Linhas VTY

Depois de criada, a ACL só passa a funcionar quando é **aplicada**. Na interface, o comando é:

`ip access-group {número | nome} {in | out}`

Para tirar a ACL da interface, usa-se `no ip access-group`; para apagá-la do roteador, `no access-list`.

A ACL também pode controlar **quem acessa o roteador remotamente**, pelas linhas VTY (as linhas virtuais usadas pelo Telnet e pelo SSH). Nesse caso, o comando é `access-class`:

```
ip access-list standard VTY_ACCESS
 permit 192.168.10.10 log
 deny any
line vty 0 4
 access-class VTY_ACCESS in
```

Com essa configuração, só o computador 192.168.10.10 acessa o roteador remotamente, e cada acesso gera uma mensagem de log.

O comando `show access-lists` mostra as ACLs e um **contador de correspondências** (*matches*) em cada ACE, útil para conferir se elas estão funcionando.

### 21.6 Modificação de ACLs

Existem dois métodos para corrigir uma ACL:

- **editor de texto**: copiar a ACL da configuração em execução, corrigi-la, **apagar a ACL antiga** no roteador e colar a versão corrigida;
- **número de sequência**: cada ACE recebe automaticamente um número (10, 20, 30...), que aparece no `show access-lists`. Para corrigir, apaga-se a entrada pelo número e digita-se a nova com o mesmo número.

**Importante:** no método do editor, **a ACL antiga precisa ser apagada antes**. Se a versão corrigida for colada por cima, as linhas novas apenas se somam às antigas.

Exemplo do método do número de sequência, corrigindo uma entrada digitada com erro (19.168.10.10 em vez de 192.168.10.10):

```
ip access-list standard 1
 no 10
 10 deny host 192.168.10.10
```

Um número existente não pode ser simplesmente sobrescrito: a entrada antiga precisa ser apagada primeiro.

### 21.7 Diretrizes e Posicionamento

As principais diretrizes para trabalhar com ACLs são:

- a última instrução é sempre a negação implícita;
- a ordem importa: as ACEs são lidas de cima para baixo e a leitura para na primeira correspondência;
- organizar **do mais específico ao mais genérico**: primeiro negar um host, depois permitir o restante da rede;
- novas ACEs entram no final da lista;
- **uma ACL por interface, por protocolo e por direção**;
- os pacotes gerados pelo próprio roteador não são filtrados pelas ACLs de saída.

O lugar onde a ACL é aplicada também faz diferença:

- **ACL estendida** → o **mais perto possível da origem**, para que o tráfego indesejado não atravesse a rede à toa;
- **ACL padrão** → o **mais perto possível do destino**, porque ela só enxerga a origem: perto da origem, bloquearia aquela rede para todos os destinos.

A escolha também depende de até onde vai o controle da organização sobre os equipamentos, da largura de banda das redes envolvidas e da facilidade de configuração.

Exemplos:

- para impedir que a rede 192.168.10.0/24 alcance a rede 192.168.30.0/24 com uma ACL padrão, ela é aplicada **na saída da interface do roteador ligada à rede 192.168.30.0/24**. Se fosse aplicada na entrada do roteador, bloquearia também o acesso a outras redes atrás dele;
- para impedir que a rede 192.168.11.0/24 use Telnet e FTP com a rede 192.168.30.0/24, de outra empresa, a ACL estendida é aplicada **na entrada da interface do roteador ligada à rede 192.168.11.0/24**. Assim, só os pacotes dessa rede são examinados e o tráfego bloqueado nem chega a sair.

### 21.8 Resumo dos Comandos de ACL

| Comando | Função |
| --- | --- |
| `access-list 1–99` | Cria ACL padrão numerada |
| `access-list 100–199` | Cria ACL estendida numerada |
| `ip access-list standard NOME` | Cria ACL padrão nomeada |
| `ip access-list extended NOME` | Cria ACL estendida nomeada |
| `ip access-group ... in/out` | Aplica a ACL a uma interface |
| `access-class ... in` | Aplica a ACL às linhas VTY |
| `show access-lists` | Mostra as ACLs e os contadores |
| `no access-list` | Apaga a ACL |

## 22. Mitigação de Ataques com ACLs e ACLs IPv6

Além de organizar o tráfego, as ACLs são uma ferramenta de defesa: elas bloqueiam endereços falsificados, limitam os serviços expostos e controlam mensagens que os atacantes usam para reconhecimento. Esta seção também mostra como as ACLs funcionam no IPv6.

### 22.1 Bloqueio de Endereços Falsificados

Na **falsificação de IP** (*IP spoofing*), o atacante **coloca um endereço de origem falso no cabeçalho** para esconder sua identidade ou se passar por outro dispositivo.

Certos endereços nunca deveriam chegar da internet, porque não são usados nela. Por isso, a interface do roteador voltada para a internet **nunca deve aceitar pacotes com estes endereços de origem**:

- todos os bits em zero (0.0.0.0);
- endereço de broadcast (255.255.255.255);
- endereços de *loopback* (127.0.0.0/8), que são do próprio dispositivo;
- endereços APIPA (169.254.0.0/16), que o computador cria sozinho quando não recebe IP;
- endereços privados (10.0.0.0/8, 172.16.0.0/12 e 192.168.0.0/16);
- endereços de multicast (224.0.0.0/4).

Exemplo de ACL aplicada na entrada da interface ligada à internet:

```
access-list 150 deny ip host 0.0.0.0 any
access-list 150 deny ip 10.0.0.0 0.255.255.255 any
access-list 150 deny ip 127.0.0.0 0.255.255.255 any
access-list 150 deny ip 169.254.0.0 0.0.255.255 any
access-list 150 deny ip 172.16.0.0 0.15.255.255 any
access-list 150 deny ip 192.168.0.0 0.0.255.255 any
access-list 150 deny ip 224.0.0.0 15.255.255.255 any
access-list 150 deny ip host 255.255.255.255 any
access-list 150 permit ip any any
```

**Observação:** o exemplo do curso não tem a linha `permit ip any any` no final. Sem ela, a negação implícita bloquearia todo o tráfego vindo da internet. A linha do APIPA também foi acrescentada para cobrir a lista completa.

Na outra ponta, a interface ligada à rede local **só deve aceitar pacotes cuja origem seja a própria rede local**. Exemplo: `access-list 105 permit ip 192.168.1.0 0.0.0.255 any`. Assim, um dispositivo interno não consegue enviar pacotes com origem falsa.

### 22.2 Liberação Apenas dos Serviços Necessários

Uma ACL de entrada deve **deixar passar apenas o tráfego dos serviços que realmente são usados**. Os serviços que costumam ser liberados são:

- DNS, SMTP e FTP, para os servidores que atendem o público;
- SSH, syslog (envio de registros de eventos a um servidor) e SNMP, para a administração dos equipamentos.

Exemplo:

```
access-list 180 permit udp any host 192.168.20.2 eq domain
access-list 180 permit tcp any host 192.168.20.2 eq smtp
access-list 180 permit tcp any host 192.168.20.2 eq ftp
access-list 180 permit tcp host 200.5.5.5 host 10.0.1.1 eq 22
access-list 180 permit udp host 200.5.5.5 host 10.0.1.1 eq syslog
access-list 180 permit udp host 200.5.5.5 host 10.0.1.1 eq snmptrap
```

As três primeiras linhas liberam DNS, e-mail e FTP para o servidor 192.168.20.2. As três últimas liberam SSH, syslog e SNMP apenas da estação de administração 200.5.5.5 para o equipamento 10.0.1.1, porque a ACL filtra um único sentido. Todo o resto cai na negação implícita.

### 22.3 Controle do ICMP

Relembrando: o **ICMP** (*Internet Control Message Protocol* — protocolo de mensagens de controle da internet) é o protocolo das mensagens de erro e de teste, como as do comando ping. Os atacantes o usam de duas formas:

- o **echo** (ping) serve para descobrir sub-redes e hosts ativos e para ataques de negação de serviço por inundação;
- o **redirect** pode alterar a tabela de roteamento dos hosts.

Por esse motivo, **echo e redirect devem ser bloqueados na entrada**, e só algumas mensagens ICMP devem passar:

| Sentido | Mensagens permitidas | Finalidade |
| --- | --- | --- |
| Entrando na rede | echo-reply | Resposta aos pings feitos pelos usuários internos |
| Entrando na rede | source-quench | Pedido para diminuir a velocidade do envio |
| Entrando na rede | unreachable | Aviso de destino inalcançável |
| Saindo da rede | echo | Pings dos usuários internos |
| Saindo da rede | parameter-problem | Aviso de problema no cabeçalho |
| Saindo da rede | packet-too-big | Descoberta do tamanho máximo de pacote (MTU) |
| Saindo da rede | source-quench | Pedido para diminuir a velocidade do envio |

Exemplo da ACL de entrada:

```
access-list 112 permit icmp any any echo-reply
access-list 112 permit icmp any any source-quench
access-list 112 permit icmp any any unreachable
access-list 112 deny icmp any any
access-list 112 permit ip any any
```

A penúltima linha nega todas as outras mensagens ICMP, e a última libera o tráfego que não é ICMP.

### 22.4 Proteção do SNMP

O acesso ao **SNMP** (protocolo de gerenciamento dos equipamentos) pode ser filtrado com uma ACL na interface, mas pacotes com origem falsificada ainda podem passar. A forma mais eficaz é **desativar o SNMP quando ele não for necessário**, com o comando `no snmp-server`.

### 22.5 Riscos da Transição para o IPv6

Durante a transição do IPv4 para o IPv6, as duas versões convivem, e essa convivência cria brechas. Um dispositivo de **pilha dupla** (*dual stack*) tem **conectividade IPv4 e IPv6 ao mesmo tempo**, e um firewall configurado só para IPv4 não enxerga o que passa pelo IPv6.

Os principais ataques nesse cenário exploram:

- hosts de pilha dupla;
- mensagens falsas do **NDP** (*Neighbor Discovery Protocol* — protocolo de descoberta de vizinhos), que no IPv6 substitui o ARP;
- técnicas de tunelamento.

Um exemplo é o **Teredo**, uma técnica de transição que dá endereços IPv6 a hosts atrás de um NAT IPv4 (a tradução que faz vários endereços internos saírem para a internet com um único endereço público), **encapsulando o IPv6 dentro de pacotes UDP IPv4**. De forma simplificada, o ataque ocorre da seguinte maneira:

1. o atacante, na rede IPv4, envia anúncios de roteador IPv6 falsos (mensagens em que um roteador informa aos hosts o prefixo de rede e o gateway que devem usar);
2. os hosts se configuram com IPv6 em silêncio, sem que ninguém perceba;
3. o firewall IPv4 só vê tráfego UDP comum;
4. o atacante usa esse caminho para avançar sobre os hosts.

A defesa é **filtrar o tráfego IPv6 na borda da rede com ACLs IPv6**.

### 22.6 ACLs IPv6

As ACLs IPv6 funcionam como as estendidas do IPv4, com algumas diferenças:

- **não existe ACL IPv6 padrão**: toda ACL IPv6 é **nomeada** e filtra origem, destino, protocolo e portas;
- é criada com `ipv6 access-list NOME`;
- é aplicada à interface com `ipv6 traffic-filter NOME {in | out}`, e não com `ip access-group`;
- **any** equivale a ::/0, e os endereços são escritos com prefixo, como 2001:db8:1:1::/64.

Toda ACL IPv6 termina com três entradas implícitas:

- `permit icmp any any nd-na` (permite os anúncios de vizinho);
- `permit icmp any any nd-ns` (permite as solicitações de vizinho);
- `deny ipv6 any any` (nega todo o resto).

**Importante:** se o administrador escrever um `deny ipv6 any any` explícito sem antes permitir as mensagens de vizinho (nd-na e nd-ns), o **NDP para de funcionar**, e os dispositivos deixam de descobrir uns aos outros.

Exemplo, que também documenta as entradas implícitas (uma boa prática):

```
ipv6 access-list LAN_ONLY
 permit 2001:db8:1:1::/64 any
 permit icmp any any nd-na
 permit icmp any any nd-ns
 deny ipv6 any any
```

| Característica | ACL IPv4 | ACL IPv6 |
| --- | --- | --- |
| Tipos | Padrão e estendida | Apenas um tipo, semelhante à estendida |
| Identificação | Número ou nome | Apenas nome |
| Aplicação na interface | `ip access-group` | `ipv6 traffic-filter` |
| Entradas implícitas | Nega tudo | Permite nd-na e nd-ns e nega o resto |

## 23. Tecnologias de Firewall

As ACLs fazem uma filtragem básica, olhando pacote por pacote. O **firewall** vai além: ele é o equipamento ou programa dedicado a **controlar o tráfego entre redes com níveis de confiança diferentes**.

### 23.1 Características do Firewall

Todo firewall compartilha três propriedades:

- é resistente a ataques;
- é o **único ponto de trânsito** entre a rede interna e a externa, ou seja, todo o tráfego passa por ele;
- aplica a política de controle de acesso da organização.

Entre seus benefícios estão:

- impede que hosts, recursos e aplicações sensíveis fiquem expostos a usuários não confiáveis;
- "limpa" o fluxo dos protocolos, impedindo que falhas deles sejam exploradas;
- bloqueia dados maliciosos vindos de servidores e clientes;
- simplifica o gerenciamento, porque o controle de acesso fica concentrado em poucos equipamentos.

Suas limitações são:

- se estiver mal configurado, pode virar um **ponto único de falha**;
- os dados de muitos aplicativos não conseguem passar por ele com segurança;
- usuários podem tentar contorná-lo, expondo a rede;
- pode reduzir o desempenho da rede;
- tráfego não autorizado pode passar escondido dentro de tráfego legítimo.

### 23.2 Tipos de Firewall

De acordo com a forma de análise, os firewalls podem ser classificados em quatro tipos principais:

- **filtragem de pacotes** (*stateless*, sem estado): normalmente faz parte do roteador e atua nas camadas 3 e 4, consultando uma tabela de regras simples. Analisa o IP de origem e de destino, o protocolo, as portas de origem e de destino e o recebimento de pacotes SYN. Exemplo: bloquear a porta 25 (SMTP) de uma estação para que ela não espalhe vírus por e-mail;
- **com estado** (*stateful*): o tipo mais versátil e mais comum. Mantém uma **tabela de estado** com as conexões em andamento e analisa as camadas 3, 4 e 5;
- **gateway de aplicação** (*proxy*): atua nas camadas 3, 4, 5 e 7. O cliente se conecta ao proxy, e **o proxy se conecta ao servidor em nome do cliente**, de modo que o servidor só enxerga o proxy;
- **firewall de última geração** (**NGFW**, *Next-Generation Firewall*): faz tudo o que o firewall com estado faz e acrescenta prevenção de intrusão integrada, **reconhecimento e controle de aplicativos** (identifica e bloqueia aplicativos arriscados), atualização com informações sobre novas ameaças e técnicas contra ameaças em evolução.

Existem ainda outros tipos:

- **baseado em host**: programa instalado no próprio computador ou servidor;
- **transparente**: filtra o tráfego IP entre duas interfaces ligadas em ponte, sem precisar de endereço próprio no caminho;
- **híbrido**: combina tipos diferentes. Exemplo: a inspeção de aplicações, que une o firewall com estado ao gateway de aplicação.

| Tipo | Camadas analisadas | Como decide |
| --- | --- | --- |
| Filtragem de pacotes | 3 e 4 | Regras fixas, pacote por pacote |
| Com estado | 3, 4 e 5 | Regras + tabela de conexões |
| Gateway de aplicação | 3, 4, 5 e 7 | Intermedia a conexão e analisa a aplicação |
| NGFW | Até a 7 | Estado + aplicativos + prevenção de intrusão |

### 23.3 Firewall de Filtragem de Pacotes

As principais vantagens do filtro de pacotes são:

- regras simples de permitir e negar;
- **baixo impacto no desempenho**;
- fácil de implementar e disponível na maioria dos roteadores;
- oferece um nível inicial de segurança na camada de rede;
- entrega boa parte da proteção de um firewall caro, a um custo muito menor.

Suas desvantagens são:

- é suscetível à falsificação de IP: qualquer pacote que atenda às regras passa;
- não filtra bem pacotes fragmentados, porque só o primeiro fragmento leva o cabeçalho TCP e os demais passam sem verificação;
- ACLs complexas são difíceis de manter;
- não lida bem com serviços que negociam portas na hora, sendo preciso abrir faixas inteiras de portas;
- **não guarda estado**: examina cada pacote isoladamente, sem saber se ele faz parte de uma conexão.

**Observação:** o filtro de pacotes não é uma solução completa, mas continua sendo um elemento importante da defesa.

### 23.4 Firewall com Estado

O firewall com estado é o **principal meio de defesa** de muitas redes. Seus benefícios são:

- filtragem mais forte e controle mais rigoroso;
- desempenho melhor do que o dos filtros de pacotes e dos proxies;
- **defende contra falsificação e negação de serviço**, porque verifica se cada pacote pertence a uma conexão existente;
- registros (logs) mais ricos.

Suas limitações são:

- **não inspeciona a camada de aplicação**: não enxerga, por exemplo, o conteúdo de uma página HTTP;
- rastreia mal protocolos sem conexão, como UDP e ICMP, que não geram informações de conexão;
- tem dificuldade com aplicativos que abrem várias conexões em portas negociadas na hora;
- não faz autenticação de usuários.

### 23.5 Firewalls no Projeto de Rede

No projeto da rede, cada interface do firewall liga uma área com um nível de confiança, e as regras dizem que tráfego pode ir de uma área para outra.

No projeto mais simples, o firewall tem **duas interfaces**: a privada, confiável, e a pública, não confiável. A regra geral é:

- tráfego da rede privada para a pública → permitido e inspecionado, assim como suas respostas;
- tráfego que começa na rede pública em direção à privada → geralmente bloqueado.

Relembrando: a **DMZ** é a área intermediária onde ficam os servidores que atendem o público, como os de e-mail e da web. Com ela, o firewall passa a ter **três interfaces**: interna, externa e DMZ.

| Origem → Destino | Tratamento |
| --- | --- |
| Privada → pública ou DMZ | Inspecionado, com pouca ou nenhuma restrição; respostas permitidas |
| DMZ → privada | Geralmente bloqueado |
| DMZ → pública | Permitido seletivamente, conforme os serviços |
| Pública → DMZ | Permitido seletivamente e inspecionado (e-mail, DNS, HTTP, HTTPS) |
| Pública → privada | Bloqueado |

### 23.6 Defesa em Camadas com Firewalls

Relembrando: na defesa em profundidade, várias camadas de proteção se somam, para que a falha de uma não exponha tudo. Com firewalls, isso significa **combinar tipos diferentes de firewall**, cada um aplicando políticas em um ponto da rede.

Um exemplo clássico é a **sub-rede rastreada** (*screened subnet*), em que o tráfego vindo da internet passa por várias barreiras:

Rede não confiável → Filtro de pacotes no roteador de borda → Firewall ou host bastião → Roteador de triagem interno → Host de destino

O **host bastião** é um computador **reforçado para resistir a ataques**, normalmente instalado na DMZ.

As camadas dessa defesa, de dentro para fora, são:

- segurança do núcleo da rede: contra malware e anomalias de tráfego, garantindo que a rede continue funcionando;
- segurança do perímetro: nos limites entre as zonas;
- segurança das comunicações: garantia de que as informações trafegam protegidas;
- segurança do endpoint: identidade e conformidade de cada dispositivo.

### 23.7 Limites e Boas Práticas

**Importante:** o firewall **não resolve todos os problemas**. Ele:

- não impede invasões entre hosts da mesma rede ou zona;
- não protege contra um ponto de acesso sem fio não autorizado ligado à rede interna;
- não substitui o backup e a recuperação de desastres;
- não substitui administradores e usuários bem informados.

As boas práticas para a política de firewall são:

- posicionar firewalls nos limites de segurança, sem depender só deles;
- **negar todo o tráfego por padrão** e permitir apenas os serviços necessários;
- controlar o acesso físico ao firewall;
- monitorar os logs regularmente;
- controlar as mudanças na configuração;
- lembrar que o firewall protege principalmente contra ataques técnicos vindos de fora.

## 24. Firewall de Política Baseada em Zona (ZPF)

Os roteadores Cisco podem funcionar como firewall com estado. O **Cisco IOS Firewall** oferece dois modelos de configuração:

- **clássico**: a política é aplicada diretamente em cada interface;
- **ZPF** (*Zone-Based Policy Firewall* — firewall de política baseada em zona): as interfaces são agrupadas em zonas, e a política é aplicada **ao tráfego que passa de uma zona para outra**.

### 24.1 Zonas de Segurança

Uma **zona** é um **grupo de uma ou mais interfaces com funções e necessidades de segurança semelhantes**. Uma topologia básica tem três zonas: privada, pública (internet) e DMZ.

As regras básicas das zonas são:

- tráfego entre interfaces da **mesma zona** → passa livremente, sem política;
- tráfego entre **zonas diferentes** → **bloqueado**, a menos que uma política o permita ou inspecione.

A vantagem prática é que uma interface nova colocada na zona privada já se comunica com as outras da mesma zona e já segue as regras dessa zona, sem nenhuma configuração extra.

A exceção é a **zona self**, que representa **o próprio roteador**, com todos os endereços IP de suas interfaces. Ela reúne o tráfego de gerenciamento (como o SSH) e o de controle (como os protocolos de roteamento). Por padrão, **o tráfego que sai do roteador ou é destinado a ele passa**; só é filtrado se houver um par de zonas com a zona self e uma política específica.

### 24.2 Benefícios do ZPF

Entre os principais benefícios do ZPF estão:

- não depende de ACLs;
- a postura padrão é **bloquear tudo o que não for explicitamente permitido**;
- as políticas são fáceis de ler e de diagnosticar;
- interfaces físicas e virtuais podem ser agrupadas em zonas;
- as políticas valem para o tráfego em **um único sentido** entre duas zonas.

As políticas são escritas em **C3PL** (*Cisco Common Classification Policy Language*), uma forma estruturada de criar políticas a partir de eventos, condições e ações. Ela é escalável, porque uma única política alcança todo um tipo de tráfego, sem exigir várias ACLs.

**Importante:** os modelos clássico e ZPF podem existir no mesmo roteador, mas **não na mesma interface**.

### 24.3 Projeto do ZPF

O projeto de um ZPF segue estas etapas:

1. **determinar as zonas**, ou seja, as fronteiras de segurança (exemplo: zona pública e zona interna);
2. **estabelecer as políticas entre as zonas**: para cada par origem → destino, definir quais sessões (TCP, UDP, ICMP) os clientes da origem podem abrir com os servidores do destino. Como cada política vale em um sentido, ela é definida para um **par de zonas** (*zone pair*);
3. **projetar a infraestrutura física**, considerando segurança, disponibilidade, quantidade de equipamentos entre as zonas e redundância;
4. identificar subconjuntos dentro das zonas e juntar seus requisitos.

Os projetos variam do mais simples ao mais complexo: uma rede local ligada à internet; um firewall com servidores públicos em uma DMZ; servidores públicos entre dois firewalls; firewalls redundantes; e redes com várias VLANs, VPN e comércio eletrônico.

### 24.4 Ações do ZPF

O ZPF pode tomar três ações com o tráfego:

- **Inspect** (inspecionar): faz a inspeção com estado, guardando as informações da sessão TCP ou UDP e **permitindo automaticamente as respostas**;
- **Drop** (descartar): equivale a negar. É a **ação padrão**, e o descarte é silencioso;
- **Pass** (passar): equivale a permitir, mas **sem estado e em um único sentido**. Para que as respostas voltem, é preciso uma política no sentido contrário. É indicada para protocolos seguros e previsíveis, como o IPsec.

**Importante:** diferentemente da ACL, o Drop do ZPF descarta em silêncio, **sem enviar a mensagem ICMP de destino inalcançável** ao remetente. A opção log pode registrar os pacotes descartados.

**Observação:** para a maioria das aplicações, a ação recomendada é Inspect, e não Pass.

### 24.5 Regras para o Tráfego que Atravessa o Roteador

O resultado depende de as interfaces de origem e de destino pertencerem ou não a zonas:

| Interface de origem em zona? | Interface de destino em zona? | Situação | Resultado |
| --- | --- | --- | --- |
| Não | Não | Nenhuma das duas usa ZPF | Passa |
| Sim | Não | Uma só está em zona | Descarta |
| Não | Sim | Uma só está em zona | Descarta |
| Sim | Sim | Mesma zona | Passa |
| Sim | Sim | Zonas diferentes, sem par de zonas | Descarta |
| Sim | Sim | Zonas diferentes, com par de zonas e sem política | Descarta |
| Sim | Sim | Zonas diferentes, com par de zonas e política | Segue a política |

**Observação:** na tabela do curso, o caso "com par de zonas e sem política" aparece como "Passa". A documentação atual da Cisco informa que, sem política configurada no par de zonas, o tráfego é descartado.

**Importante:** o tráfego **nunca flui entre uma interface que está em zona e outra que não está**. Por isso, ao colocar a primeira interface em uma zona, a comunicação dela com as demais é interrompida até que as outras também sejam configuradas.

### 24.6 Configuração do ZPF

Antes de configurar, é preciso responder: quais interfaces participam, qual o nome de cada zona e que tráfego deve passar, em que sentido. A configuração segue cinco etapas:

Zonas → Classe de tráfego (class-map) → Política (policy-map) → Par de zonas (zone-pair) → Interfaces nas zonas

A ordem importa: o class-map precisa existir antes do policy-map, e o policy-map antes do zone-pair, ou o roteador mostra erro.

#### 24.6.1 Exemplo Resolvido: Rede Privada Acessando a Web

No exemplo, a interface GigabitEthernet0/0 fica na zona privada e a Serial0/0/0, na pública.

1. Criar as zonas:

```
zone security PRIVATE
zone security PUBLIC
```

2. Identificar o tráfego com um class-map. A opção **match-any** exige que o pacote atenda a **pelo menos um** critério; **match-all** exige que atenda a **todos**. Os critérios podem ser uma ACL (`match access-group`), um protocolo (`match protocol`) ou outro class-map. Ao permitir HTTP, recomenda-se incluir também HTTPS e DNS:

```
class-map type inspect match-any HTTP-TRAFFIC
 match protocol http
 match protocol https
 match protocol dns
```

3. Definir a ação com um policy-map:

```
policy-map type inspect PRIV-TO-PUB-POLICY
 class type inspect HTTP-TRAFFIC
  inspect
```

4. Criar o par de zonas e associar a política:

```
zone-pair security PRIV-PUB source PRIVATE destination PUBLIC
 service-policy type inspect PRIV-TO-PUB-POLICY
```

5. Colocar as interfaces nas zonas:

```
interface GigabitEthernet0/0
 zone-member security PRIVATE
interface Serial0/0/0
 zone-member security PUBLIC
```

O resultado é que o tráfego HTTP, HTTPS e DNS da zona privada para a pública é inspecionado, e da zona pública para a privada **só entram as respostas das sessões abertas pela zona privada**. Todo o resto cai na classe padrão (class-default), cuja ação é Drop.

### 24.7 Verificação e Cuidados

Os principais comandos de verificação são:

| Comando | O que mostra |
| --- | --- |
| `show run \| begin class-map` | A configuração do ZPF, a partir dos class-maps |
| `show policy-map type inspect zone-pair sessions` | As sessões inspecionadas e os contadores de cada classe |
| `show class-map type inspect` | Os class-maps |
| `show zone security` | As zonas, incluindo a self (“System Defined Zone”) |
| `show zone-pair security` | Os pares de zonas e suas políticas |
| `show policy-map type inspect` | Os policy-maps |

Ao usar o ZPF, alguns cuidados são necessários:

- o ZPF **nunca filtra o tráfego entre interfaces da mesma zona**;
- uma interface não pode pertencer a várias zonas;
- para usar o ZPF em uma interface que tem o modelo clássico, é preciso remover antes o comando `ip inspect`;
- a política padrão entre zonas é descartar tudo;
- o ZPF não protege o próprio roteador, a menos que sejam criados pares de zonas com a zona self.

| Característica | Firewall clássico | ZPF |
| --- | --- | --- |
| Onde a política é aplicada | Em cada interface | No tráfego entre zonas |
| Depende de ACLs | Sim | Não |
| Postura padrão | Depende da configuração | Bloquear o que não foi permitido |
| Interface nova | Precisa de configuração própria | Herda as regras da zona |

## 25. Virtualização e Computação em Nuvem

Boa parte dos servidores das empresas já não fica em máquinas físicas próprias, e sim em máquinas virtuais e na nuvem. Para proteger esse ambiente, é preciso primeiro entender como ele funciona.

### 25.1 Virtualização e Hypervisor

A **virtualização** permite **executar vários computadores virtuais em uma única máquina física**, reduzindo a quantidade de equipamentos. Cada computador virtual é uma **máquina virtual** (**VM**, *Virtual Machine*), com seu próprio sistema operacional.

O componente principal é o **hypervisor**: o software ou hardware que **executa vários sistemas operacionais independentes em um mesmo sistema físico**. Existem dois tipos:

- **tipo 1** (*bare metal*, "metal puro"): o hypervisor **roda diretamente sobre o hardware**, sem um sistema operacional por baixo. Exemplos: VMware ESXi e Microsoft Hyper-V;
- **tipo 2** (hospedado): o hypervisor é **um aplicativo instalado sobre um sistema operacional comum**, que cria as VMs em software. Exemplos: Oracle VirtualBox e VMware Workstation.

O tipo 1 é o usado nos data centers, por ser mais eficiente. O tipo 2 é comum em computadores pessoais, para testes e estudo.

**Importante:** como toda VM tem sistema operacional, ela **precisa de atualizações e correções como um computador físico**. Além disso, as VMs compartilham o hardware e rodam com privilégios altos, de modo que comprometer uma VM pode levar a comprometer o host.

### 25.2 Contêineres e Desktops Virtuais

O **contêiner** é uma forma mais leve de virtualização: em vez de um sistema operacional inteiro, ele leva **apenas o aplicativo e as dependências de que ele precisa**, e **compartilha o núcleo do sistema operacional do host**. As ferramentas mais conhecidas são:

- **Docker**: plataforma aberta que empacota o software em contêineres;
- **Kubernetes**: sistema que gerencia muitos contêineres ao mesmo tempo.

**Importante:** se um contêiner roda com privilégios elevados e é comprometido, o atacante pode alcançar o **sistema operacional por baixo dele**.

A **VDI** (*Virtual Desktop Infrastructure* — infraestrutura de desktops virtuais) guarda **o ambiente de trabalho do usuário em um servidor remoto**. O usuário acessa seu desktop por um equipamento simples, chamado *thin client*. Os desktops são fáceis de criar, apagar, copiar e arquivar, mas a VDI exige alta disponibilidade e muita capacidade de armazenamento.

| Característica | Máquina virtual | Contêiner |
| --- | --- | --- |
| O que leva | Sistema operacional completo | Só o aplicativo e suas dependências |
| Núcleo do sistema | Próprio | Compartilhado com o host |
| Peso | Maior | Menor |
| Gerenciador | Hypervisor | Docker, Kubernetes |

### 25.3 Riscos da Virtualização

Os dois riscos típicos da virtualização são:

- **expansão de VMs** (*VM sprawl*): como criar VMs é fácil, acumulam-se **VMs esquecidas ou subutilizadas**, que consomem recursos e ficam sem atualização;
- **fuga de VM** (*VM escape*): a VM **rompe o isolamento e passa a interagir com o sistema operacional do host**.

### 25.4 Modelos de Serviço em Nuvem

A **computação em nuvem** oferece **acesso a computação, armazenamento, software e servidores pela internet**. Os serviços são chamados de **XaaS** (*Anything as a Service* — qualquer coisa como serviço) e se dividem em três modelos principais:

- **SaaS** (*Software as a Service* — software como serviço): o provedor entrega o software pronto e gerencia toda a infraestrutura; o usuário guarda seus dados nos servidores do provedor. Exemplo: webmail;
- **PaaS** (*Platform as a Service* — plataforma como serviço): o provedor oferece, por assinatura, ferramentas e serviços para **desenvolver e publicar aplicativos**;
- **IaaS** (*Infrastructure as a Service* — infraestrutura como serviço): o provedor oferece **recursos de computação virtualizados**, como servidores, armazenamento e rede, e o cliente monta seu ambiente sobre eles.

### 25.5 Modelos de Implantação

De acordo com quem usa e quem controla a infraestrutura, as nuvens podem ser classificadas em quatro modelos:

| Modelo | Quem usa | Característica principal |
| --- | --- | --- |
| Privada | Uma única organização | Mais controle e mais custo |
| Pública | Qualquer cliente de um provedor externo | Mais barata, menos controle |
| Híbrida | Uma organização, combinando privada e pública | Dados sensíveis sob controle próprio e parte do serviço na nuvem pública |
| Comunitária | Várias empresas do mesmo setor | Plataforma compartilhada para necessidades comuns, como saúde ou energia |

### 25.6 Computação em Neblina e de Borda

Em algumas aplicações, mandar os dados até um data center distante e esperar a resposta demora demais. Duas abordagens aproximam o processamento de onde os dados nascem:

- **computação em neblina** (*fog computing*): os dados são processados **em um equipamento intermediário da rede local**, como um gateway IoT, entre o dispositivo e o data center;
- **computação de borda** (*edge computing*): os dados são processados **no próprio dispositivo ou sensor**, sem ir ao data center.

Elas são usadas onde milissegundos importam, como em veículos autônomos, aviação e manufatura.

## 26. Segurança na Nuvem

A nuvem traz vantagens, mas também concentra riscos: quando um recurso de nuvem é comprometido, o atacante pode usar a reputação do provedor a seu favor. Ele pode:

- atacar outras organizações a partir dali;
- hospedar malware em um provedor respeitado, o que faz o conteúdo parecer legítimo;
- lançar ataques DDoS e hospedar pirataria, spam e phishing.

### 26.1 Principais Ameaças

As principais ameaças à segurança na nuvem são:

- vazamento de dados;
- **configuração incorreta** dos serviços de nuvem;
- estratégia ruim de arquitetura de segurança;
- **credenciais de contas comprometidas**: a conta de serviço da nuvem pública tem o maior privilégio, e quem a sequestra controla tudo;
- ameaça interna, vinda de pessoas da própria organização;
- interfaces de usuário e **APIs inseguras**, que são os pontos mais expostos;
- pouca visibilidade sobre como a nuvem está sendo usada.

Uma **API** (*Application Programming Interface* — interface de programação de aplicações) é o conjunto de comandos pelo qual programas se comunicam com o serviço de nuvem.

### 26.2 Responsabilidade Compartilhada

Na nuvem privada, toda a segurança é responsabilidade da empresa. Nas nuvens pública, híbrida e comunitária, ela é **dividida entre o cliente e o provedor** (**CSP**, *Cloud Service Provider* — provedor de serviços de nuvem). Quanto mais pronto é o serviço, mais responsabilidades passam ao provedor:

| Responsabilidade | No local | IaaS | PaaS | SaaS |
| --- | --- | --- | --- | --- |
| Dados | Cliente | Cliente | Cliente | Cliente |
| Endpoints | Cliente | Cliente | Cliente | Compartilhada |
| Gerenciamento de identidades | Cliente | Cliente | Compartilhada | Compartilhada |
| Aplicação | Cliente | Cliente | Compartilhada | CSP |
| Controle de rede | Cliente | Cliente | Compartilhada | CSP |
| Sistema operacional | Cliente | Cliente | CSP | CSP |
| Infraestrutura física | Cliente | CSP | CSP | CSP |

**Importante:** em todos os modelos, **os dados continuam sendo responsabilidade do cliente**.

**Observação:** no curso, a penúltima linha aparece sem nome. Ela corresponde ao sistema operacional dos servidores, como no modelo de responsabilidade compartilhada da Microsoft, em que se baseia essa tabela.

### 26.3 Domínios da Segurança em Nuvem (CSA)

A **CSA** (*Cloud Security Alliance* — Aliança de Segurança na Nuvem) publica um guia com as áreas essenciais da segurança em nuvem, organizado em **14 domínios**:

1. conceitos e arquiteturas da computação em nuvem;
2. governança e gerenciamento de riscos corporativos;
3. questões jurídicas, contratos e descoberta eletrônica (localização de provas digitais);
4. gerenciamento de conformidade e auditoria;
5. governança da informação;
6. plano de gerenciamento e continuidade dos negócios;
7. segurança da infraestrutura;
8. virtualização e contêineres;
9. resposta a incidentes;
10. segurança das aplicações;
11. segurança e criptografia dos dados;
12. gerenciamento de identidade, direitos e acesso (IAM);
13. segurança como serviço;
14. tecnologias relacionadas.

No domínio 11, a CSA destaca que a proteção deve ser baseada no risco de cada dado e que a **criptografia é um dos controles mais importantes**.

### 26.4 Segurança da Infraestrutura em Nuvem

A **infraestrutura em nuvem** é a base dos recursos virtualizados (computação, rede e armazenamento). Ela tem duas camadas:

- a camada física e lógica do provedor (processadores, memória, redes e armazenamento), que forma a nuvem;
- a infraestrutura virtual que o cliente monta e gerencia com esses recursos.

Na nuvem, as medidas tradicionais, como controlar os cabos ou instalar um equipamento de segurança no caminho, **não funcionam**. Em seu lugar, usam-se equipamentos virtuais e agentes de software, que podem criar gargalos e sobrecarregar o processamento.

A **SDN** (*Software-Defined Networking* — rede definida por software) facilita o isolamento, porque **as redes são criadas e separadas por software**, sem depender do hardware. Os firewalls de SDN, chamados de **grupos de segurança**, usam critérios mais flexíveis do que os firewalls físicos.

Relembrando: na defesa em profundidade, várias camadas de proteção se somam. Na nuvem, os recursos formam quatro camadas (hardware, infraestrutura, plataforma e aplicações), e cada uma precisa da sua proteção. As opções mais usadas são:

- segurança integrada da plataforma: proteções que já vêm ativadas, como a defesa contra DDoS;
- **VPC** (*Virtual Private Cloud* — nuvem privada virtual): sub-redes privadas **isoladas da internet** dentro da nuvem pública;
- firewalls virtuais e grupos de segurança, com regras de permitir e negar;
- logs de fluxo, que registram o tráfego de cada interface;
- VPN, para acesso remoto e para ligar locais, nuvens diferentes ou a nuvem ao data center;
- **IAM** (*Identity and Access Management* — gerenciamento de identidade e acesso): controla credenciais, autenticação e autorização e é **essencial na nuvem**.

A **microssegmentação** (ou hipersegregação) divide a rede em **muitas redes menores e isoladas**, criadas em topologias virtuais, sem custo de hardware e com controle muito detalhado.

Outro cuidado é a **TI invisível** (*shadow IT*): aplicativos e serviços de nuvem que os usuários adotam por conta própria, sem autorização, e que criam pontos cegos. A resposta são políticas bem definidas e conscientização dos usuários.

### 26.5 Proteção dos Dados na Nuvem

Relembrando: os dados existem em três estados (em repouso, em trânsito e em processamento), e cada um exige proteção. Na nuvem, as ferramentas são as mesmas já usadas em qualquer rede:

- **criptografia** simétrica, como o AES, e assimétrica, como o RSA, para manter a **confidencialidade** dos dados guardados e transmitidos;
- **hash**, como o SHA-256, para garantir a **integridade**, isto é, que os dados continuam completos e inalterados.

A segurança dos aplicativos desenvolvidos na nuvem segue as mesmas práticas de desenvolvimento seguro, como validação das entradas, controle de versão e assinatura de código.

### 26.6 Proteção das Máquinas Virtuais

As VMs na nuvem precisam de correções, atualizações e antimalware como qualquer servidor. As principais medidas são:

- planejar em qual sub-rede cada VM fica, dando **só o acesso necessário**;
- desativar portas e serviços desnecessários;
- gerenciar as contas: desativar as contas padrão, exigir senhas complexas e aplicar o privilégio mínimo;
- manter antivírus e antimalware atualizados, no sistema da VM ou como serviço da plataforma;
- usar firewall de host e sistemas de detecção e de prevenção de intrusão (IDS/IPS).

Relembrando: na expansão de VMs, máquinas criadas para testes ficam esquecidas e rodando. Na nuvem, além de ficarem desatualizadas e vulneráveis, **elas continuam consumindo serviços pagos**, como instâncias, armazenamento e IPs públicos. Por esse motivo, são necessárias políticas para registrar e auditar os recursos e o monitoramento das VMs em execução.

## 27. Protocolos e Tecnologias no Monitoramento de Segurança

O **monitoramento de segurança** é a observação contínua do tráfego e dos registros da rede para **identificar ataques e comportamentos suspeitos**. Ele depende de protocolos e tecnologias que existem por bons motivos, mas que também podem ser mal usados. Esta seção mostra como cada um ajuda ou atrapalha quem monitora a rede.

### 27.1 Syslog e NTP

O **syslog** é o padrão para **registrar mensagens de eventos** de equipamentos de rede e computadores. Ele é neutro, isto é, funciona com equipamentos de vários fabricantes. As mensagens são enviadas a um **servidor central**, que as guarda, e é essa centralização que torna o monitoramento prático:

Dispositivos de rede → Mensagens de evento → Servidor syslog → Estação de monitoramento

Os servidores syslog escutam a **porta UDP 514**. Como os registros revelam o que o atacante fez, ele tenta:

- bloquear o envio das mensagens do equipamento para o servidor;
- adulterar ou destruir os logs ou o software que os gera e transmite;
- usar o próprio syslog para retirar dados aos poucos.

O **syslog-ng** (*next generation*, próxima geração) traz melhorias contra essas explorações.

Relembrando: o **NTP** sincroniza os relógios dos dispositivos com um servidor de tempo. As mensagens de syslog têm **carimbo de data e hora**, e só com relógios iguais é possível **juntar os rastros de um mesmo ataque registrados em equipamentos diferentes**. O NTP usa a porta UDP 123.

Os atacantes exploram o NTP de duas formas:

- corrompendo a hora para confundir os rastros;
- usando falhas de clientes e servidores NTP para ataques DDoS, que afetam a disponibilidade.

### 27.2 DNS

Como o DNS é usado o tempo todo, as políticas sobre ele costumam ser menos rigorosas. Os atacantes aproveitam isso para **esconder outros protocolos dentro do DNS** e passar pelos equipamentos de segurança. O malware usa o DNS para falar com seu servidor de **comando e controle** (**C&C** ou CNC, o computador que dá ordens ao malware) e para retirar dados disfarçados de consultas.

De forma simplificada, a retirada de dados pelo DNS ocorre da seguinte maneira:

1. o malware codifica os dados roubados (em Base64, hexadecimal ou binário), para escapar dos sistemas de **DLP** (*Data Loss Prevention* — prevenção de perda de dados);
2. coloca os dados no lugar do subdomínio de uma consulta, como em "dados-codificados.example.com";
3. a consulta chega ao servidor DNS controlado pelo atacante, que grava o subdomínio e responde normalmente;
4. o atacante junta os pedaços e decodifica os dados, como uma lista de usuários e senhas.

Os sinais de que isso está acontecendo são:

- **subdomínios muito mais longos que o normal**, detectáveis por um modelo estatístico do comprimento;
- consultas a domínios ou subdomínios aleatórios, como AW4GCGXHy2UGDG8GCHJVDGVJDC.example.com, sobretudo se a quantidade aumentar muito.

As defesas são analisar os logs dos servidores DNS e usar serviços como o **Cisco Umbrella**, que **bloqueia consultas a domínios de comando e controle**.

### 27.3 HTTP e HTTPS

O **HTTP** é a base da web e trafega **em texto claro**, sem proteção contra alteração ou interceptação. Um ataque comum é a **injeção de iFrame**:

1. o atacante invade um servidor web muito visitado;
2. planta um código que cria um **quadro invisível** (iFrame) na página;
3. quando o visitante abre a página, o quadro baixa malware, muitas vezes de outro endereço.

Serviços como o Cisco Web Reputation analisam a página e todos os seus quadros, detectando conteúdo vindo de sites não confiáveis.

O **HTTPS** acrescenta ao HTTP a criptografia **SSL/TLS**, que torna os dados ilegíveis entre o navegador e o servidor. Relembrando os conceitos de chave pública, chave simétrica e certificado digital, a conexão ocorre da seguinte maneira:

1. o navegador pede uma página https://;
2. o servidor envia seu certificado, que contém a chave pública;
3. o navegador verifica se o certificado não expirou, não foi revogado e foi emitido por uma autoridade confiável;
4. o navegador cria uma chave simétrica, cifra essa chave com a chave pública do servidor e a envia;
5. o servidor decifra a chave simétrica com sua chave privada;
6. o servidor cifra a página com a chave simétrica e a envia;
7. o navegador decifra e exibe a página.

**Importante:** o HTTPS **protege os dados apenas no caminho**. Ele não é uma proteção do servidor web, que pode continuar vulnerável.

Para quem monitora, o HTTPS complica o trabalho: decifrar o tráfego para inspecioná-lo exige muito processamento e levanta questões de privacidade.

**Observação:** as etapas acima são uma simplificação. Na prática, o navegador e o servidor combinam um segredo e derivam dele as chaves de sessão; nas versões atuais do TLS, essa combinação é sempre feita com o Diffie-Hellman.

### 27.4 E-mail e ICMP

No e-mail, cada protocolo tem um risco próprio:

- **SMTP** (envio): gera muito tráfego e nem sempre é monitorado, por isso é usado para retirar dados. No ataque à Sony Pictures, em 2014, os dados foram enviados por SMTP aos servidores dos criminosos;
- **POP3 e IMAP** (recebimento): **trazem o malware até o computador** do usuário. O monitoramento mostra quando o anexo entrou e qual computador foi infectado primeiro, e permite recuperar o anexo para análise.

O **ICMP** é usado para identificar computadores, a estrutura da rede e os sistemas operacionais, para negação de serviço e para retirar dados. O tráfego ICMP de dentro para fora muitas vezes é ignorado, o que permite o **tunelamento ICMP**: o malware **transfere arquivos escondidos em pacotes ICMP**. Exemplos de ferramentas são o LOKI e o Ping Tunnel.

### 27.5 ACLs, NAT e PAT

As ACLs podem dar uma **falsa sensação de segurança**. Uma ACL que deixa voltar mensagens ICMP de erro, por exemplo, também deixa passar um túnel ICMP. Os atacantes descobrem quais endereços, protocolos e portas são permitidos por varreduras e reconhecimento, falsificam o IP de origem, rodam aplicações em portas permitidas e manipulam recursos como o sinalizador de conexão estabelecida do TCP.

Por esse motivo, as regras fixas precisam ser complementadas por **medidas que analisam o comportamento e o contexto**, como firewalls de última geração e proteção avançada contra malware.

O **NAT** (*Network Address Translation*) e o **PAT** (*Port Address Translation*) fazem com que vários endereços internos saiam para a internet com um único endereço público (ou poucos). Os termos usados são:

| Termo | Significado | Exemplo |
| --- | --- | --- |
| Interno local | Endereço do dispositivo dentro da rede | 192.168.10.10 |
| Interno global | Endereço do mesmo dispositivo depois do NAT | 209.165.200.226 |
| Externo global | Endereço do destino na internet | 209.165.201.1 |

**Importante:** com o PAT, todos os dispositivos internos aparecem com o mesmo endereço público. Isso **dificulta saber qual dispositivo interno fez cada pedido**. O mesmo vale para os registros de fluxo, que são "quebrados" no ponto onde o NAT acontece e precisam ser reunidos por ferramentas próprias.

### 27.6 Criptografia e Tunelamento

Relembrando: a **VPN** usa um protocolo comum, como o IP, para levar tráfego cifrado por redes públicas, criando uma ligação privada virtual. O tráfego só é legível nas pontas. O malware pode usar a mesma técnica: **criar um túnel cifrado em um protocolo confiável** para retirar dados, como no caso do DNS.

O tráfego cifrado com SSL/TLS não pode ser inspecionado pelos meios normais e pode esconder malware, vazamento de dados, violações de conformidade e invasões. Os efeitos sobre o monitoramento e as investigações são:

- o comando e controle de uma botnet pode passar por TLS sem que o firewall veja;
- os dados retirados podem sair cifrados;
- detectar esses casos exige decifrar o tráfego e compará-lo com assinaturas, ou identificar um tráfego TLS fora do normal, o que é difícil e demorado;
- se um algoritmo de criptografia for quebrado, todo o tráfego já capturado com ele pode ser lido.

As medidas recomendadas são:

- em VPNs entre locais, **posicionar o IPS onde ele veja o tráfego já decifrado**;
- criar regras que distingam tráfego SSL de não SSL e HTTPS de não HTTPS;
- validar os certificados consultando a lista de revogação (CRL) ou o OCSP;
- usar antimalware e filtragem de URL para o HTTPS;
- usar equipamentos que decifram o tráfego e o entregam ao IPS para análise.

Os navegadores também mostram avisos que merecem atenção: certificado fora do prazo de validade (que pode ser descuido ou algo grave) e erro de validação da assinatura, que ocorre quando o certificado raiz não está entre os confiáveis do navegador e tira a garantia de que a chave é autêntica.

### 27.7 P2P e Tor

Nas redes **P2P** (*peer-to-peer*, ponto a ponto), **cada computador atua ao mesmo tempo como cliente e como servidor**. Existem três tipos:

- compartilhamento de arquivos: BitTorrent e similares; o Bitcoin compartilha um livro-razão distribuído;
- compartilhamento de processamento: computadores doam capacidade ociosa para pesquisas, como as de câncer;
- mensagens instantâneas: legítimas para equipes, sendo mais seguras as plataformas corporativas, como o Webex.

**Importante:** o **P2P de arquivos não deve ser permitido em redes corporativas**. Ele contorna o firewall, é uma via de entrada para malware, usa endereços e portas que mudam o tempo todo e espalha arquivos infectados.

O **Tor** é um software e uma rede P2P que permite **navegar de forma anônima**. O caminho é formado por vários retransmissores, e a mensagem recebe várias camadas de criptografia, uma para cada retransmissor (roteamento em cebola). De forma simplificada:

1. cada retransmissor retira uma camada e só descobre o próximo salto;
2. nenhum equipamento conhece o caminho inteiro;
3. do último retransmissor até o destino, o tráfego segue sem a criptografia do Tor;
4. a resposta volta por um caminho novo.

Para a segurança, o Tor é um desafio porque é usado por criminosos na *dark web*, pode servir de canal de comando e controle e esconde o endereço de destino, escapando das listas de bloqueio.

### 27.8 Balanceamento de Carga

O **balanceamento de carga** distribui o tráfego entre servidores ou caminhos redundantes. Ele pode confundir o analista de duas formas:

- no balanceamento por DNS, um mesmo nome tem vários endereços IP, às vezes em países diferentes, e **uma única transação pode aparecer com vários IPs** nas capturas;
- o gerenciador de balanceamento envia testes (*probes*) para verificar se servidores e caminhos estão funcionando, e esses testes podem parecer suspeitos.

No balanceamento por DNS, quando o usuário consulta www.example.com, o servidor responsável pelo domínio repassa a consulta ao balanceador, que devolve o IP do servidor menos ocupado naquele momento.

| Protocolo ou tecnologia | Mau uso ou dificuldade para o monitoramento |
| --- | --- |
| Syslog | Bloqueio, adulteração ou destruição dos logs |
| NTP | Hora corrompida e DDoS |
| DNS | Retirada de dados e comando e controle |
| HTTP | Injeção de iFrame |
| HTTPS e VPN | Tráfego cifrado não inspecionado |
| SMTP, POP3 e IMAP | Retirada de dados e entrada de malware |
| ICMP | Reconhecimento e tunelamento |
| NAT e PAT | Dispositivo interno escondido |
| P2P e Tor | Contorno do firewall e anonimato |
| Balanceamento de carga | Vários IPs e testes que parecem suspeitos |

## 28. Tipos de Dados de Segurança

O analista de segurança trabalha com dados de natureza diferente, do mais resumido ao mais detalhado. Muitos deles são reunidos pelo **Security Onion**, um conjunto gratuito e de código aberto de ferramentas de **NSM** (*Network Security Monitoring* — monitoramento de segurança de rede). De acordo com o que registram, os dados podem ser classificados em cinco tipos.

### 28.1 Dados de Alerta

Os **dados de alerta** são **mensagens geradas por um IDS ou IPS quando o tráfego viola uma regra** ou corresponde à assinatura de um ataque conhecido. O Snort é um IDS de rede gratuito que já vem com regras, e seus alertas são lidos em ferramentas como o Sguil e o Kibana.

Exemplo: um site de teste exibe o texto "uid=0(root) gid=0(root) groups=0(root)", que é a resposta típica de um sistema Linux quando alguém consegue acesso de administrador. Ao receber esse texto de fora, o Snort dispara um alerta com a mensagem "GPL ATTACK\_RESPONSE id check returned root".

### 28.2 Dados de Sessão

Os **dados de sessão** são o **registro de uma conversa entre dois endpoints**, como um cliente e um servidor. Eles registram **dados sobre a conversa, e não o conteúdo**: identificação, volume de dados de cada lado e duração.

Cada sessão é identificada pela **5-tupla**: IP de origem, IP de destino, porta de origem, porta de destino e protocolo. O **Zeek** (antigo Bro) gera esse registro no log de conexões:

| Campo | Significado | Exemplo |
| --- | --- | --- |
| ts | Início da sessão | 1320279567 |
| uid | Identificação única da sessão | CEV1Z545GT3PWJLog |
| id.orig\_h | IP de origem | 192.168.2.76 |
| id.orig\_p | Porta de origem | 52034 |
| id.resp\_h | IP de destino | 174.129.249.33 |
| id.resp\_p | Porta de destino | 80 |
| proto | Protocolo de transporte | tcp |
| service | Protocolo de aplicação | http |
| duration | Duração (segundos) | 0,082899 |
| orig\_bytes | Bytes enviados pela origem | 389 |
| resp\_bytes | Bytes enviados pelo destino | 1495 |

### 28.3 Dados de Transação

Os **dados de transação** são **as mensagens trocadas durante a sessão**. Eles aparecem nas capturas de pacotes, nos logs de acesso dos servidores e em ferramentas como o Zeek.

Exemplo: o pedido "GET /index.html HTTP/1.1" e a resposta "HTTP/1.1 200 OK", registrados no log do servidor como "192.168.1.10 - AnyUser \[10/Oct/2015:13:55:36 -0500\] GET /index.html HTTP/1.1 200 326".

**Importante:** a **sessão é todo o tráfego** necessário para fazer o pedido; a **transação é o próprio pedido** e sua resposta.

### 28.4 Capturas Completas de Pacotes

As **capturas completas de pacotes** são os dados mais detalhados: guardam **o conteúdo real** do que trafegou, como o texto dos e-mails, as páginas HTML e os arquivos que entraram e saíram. Esse conteúdo pode ser extraído e analisado em busca de malware ou de violações de política.

Em compensação, exigem **muito mais armazenamento** e mais esforço para recuperar as informações. Ferramentas comuns são o Wireshark e o Cisco Prime Infrastructure.

### 28.5 Dados Estatísticos

Os **dados estatísticos** são **criados a partir da análise dos outros dados** e servem para descrever ou prever o comportamento da rede. A técnica principal é a **linha de base**:

Comportamento normal registrado → Comparação com o atual → Diferença significativa → Alarme e investigação

A **NBA** (*Network Behavior Analysis* — análise de comportamento de rede) e a **NBAD** (*Network Behavior Anomaly Detection* — detecção de anomalias de comportamento de rede) analisam os registros de fluxo da rede com análise preditiva e inteligência artificial. Serviços como o Cisco Cognitive Threat Analytics usam aprendizado de máquina para descobrir comando e controle, retirada de dados e aplicativos indesejados que escaparam dos controles.

| Tipo de dado | O que registra | Nível de detalhe |
| --- | --- | --- |
| Alerta | Violação de uma regra ou assinatura | Resumido |
| Sessão | Quem conversou com quem, quanto e por quanto tempo | Sem conteúdo |
| Transação | Pedidos e respostas da conversa | Parte do conteúdo |
| Captura completa | Todo o conteúdo dos pacotes | Máximo |
| Estatístico | Comportamento calculado a partir dos outros | Derivado |

## 29. Logs de Hosts, Servidores e Rede, SIEM e SOAR

Um **log** é um **registro dos eventos que acontecem em um dispositivo ou serviço**. Cada equipamento gera seus próprios logs, e o analista precisa saber ler os principais e reuni-los em um só lugar.

### 29.1 Logs dos Hosts

Um **HIDS** (*Host-based Intrusion Detection System*) é um sistema de detecção de intrusão instalado no próprio computador. Além de detectar, ele pode impedir ataques, como um firewall de host. Seus logs ficam no computador e **devem ser enviados a servidores centrais**, por meio de agentes, para que as ferramentas de monitoramento consigam pesquisá-los. Exemplos são o **OSSEC**, HIDS de código aberto, e o **Tripwire**, para Linux.

No Windows, os logs são lidos no **Visualizador de Eventos**, que organiza cinco tipos de log:

- aplicativo: eventos dos aplicativos;
- sistema: eventos de drivers, processos e hardware;
- instalação: instalação de programas e atualizações do Windows;
- **segurança**: tentativas de logon e acesso a arquivos e objetos, com mensagens de sucesso ou falha de auditoria;
- eventos encaminhados: eventos recebidos de outros computadores. Os comandos executados, que podem revelar a ação de invasores e de malware, aparecem no log de segurança quando a auditoria de criação de processos está ativada.

O log de segurança é gerado pelo **LSASS** (*Local Security Authority Subsystem Service*, o arquivo lsass.exe), que também aplica as diretivas de segurança. Ele deve rodar a partir da pasta System32.

**Importante:** um lsass.exe em **outra pasta**, ou um nome disfarçado como **1sass.exe** (com o número 1 no lugar da letra L), **pode ser malware**.

Cada evento do Windows tem um tipo:

| Tipo de evento | Significado | Exemplo |
| --- | --- | --- |
| Erro | Problema significativo, com perda de dados ou de funcionalidade | Um serviço não consegue iniciar |
| Aviso | Sinal de possível problema futuro | Pouco espaço em disco |
| Informações | Operação bem-sucedida | Driver de rede carregado |
| Sucesso na auditoria | Acesso auditado que deu certo | Logon realizado |
| Falha na auditoria | Acesso auditado que falhou | Acesso a uma unidade de rede negado |

### 29.2 Formato do Syslog

Relembrando: o syslog envia as mensagens de evento a um servidor central. Ele é descrito na **RFC 3164** (formato tradicional, usado nesta seção) e na **RFC 5424** (formato atual) e envia mensagens pequenas, de menos de 1 KB no formato tradicional, ao servidor (chamado de *syslogd*), normalmente pela porta UDP 514, mas também pode usar TCP. As mensagens costumam viajar **em texto claro**.

Toda mensagem tem três partes:

PRI (prioridade) → HEADER (data, hora e nome ou IP do equipamento) → MSG (texto da mensagem)

A parte **MSG** é a mais útil para o analista e varia conforme o fabricante. A **PRI** combina dois valores:

- **facilidade**: a categoria da fonte da mensagem (sistema, processo ou aplicação), usada pelo servidor para guardar cada mensagem no arquivo certo. As facilidades de uso local, local0 a local7, têm os números 16 a 23;
- **gravidade**: de 0 a 7, em que **quanto menor o número, mais grave o evento**.

| Gravidade | Nome | Significado |
| --- | --- | --- |
| 0 | Emergência | Sistema inutilizável |
| 1 | Alerta | Ação imediata necessária |
| 2 | Crítico | Condição crítica, falha |
| 3 | Erro | Erro não urgente, a resolver em um prazo |
| 4 | Aviso | Erro futuro se nada for feito |
| 5 | Notificação | Evento normal, mas significativo |
| 6 | Informativo | Operação normal |
| 7 | Depuração | Mensagens para desenvolvedores |

O valor da prioridade é calculado assim e aparece entre os sinais < e >:

**Prioridade = Facilidade × 8 + Gravidade**

**Observação:** no curso, o texto da gravidade 5 aparece trocado por uma pergunta de exercício, e as facilidades locais aparecem como "15 a 23". Os valores corretos são os desta seção.

**Observação:** um ponto (.) ou um asterisco (\*) antes da data indica **problema com o NTP**, ou seja, a hora pode não ser confiável.

#### 29.2.1 Exemplo Resolvido: Cálculo da Prioridade do Syslog

Um firewall Cisco ASA envia mensagens com a facilidade local4 e gera um evento de gravidade 3 (erro).

| Etapa | Cálculo | Resultado |
| --- | --- | --- |
| Número da facilidade local4 | 16 + 4 | 20 |
| Facilidade × 8 | 20 × 8 | 160 |
| Soma da gravidade | 160 + 3 | 163 |
| Valor no início da mensagem | — | <163> |

Nos equipamentos Cisco, a parte MSG também segue um padrão próprio. Exemplo de mensagem de um roteador:

`*Sep 16 08:50:47.359 EDT: %SYS-5-CONFIG_I: Configured from console by con0`

| Trecho | Significado |
| --- | --- |
| \* | Aviso de problema com o NTP |
| Sep 16 08:50:47.359 EDT | Data e hora |
| SYS | Facilidade no padrão Cisco |
| 5 | Gravidade (notificação) |
| CONFIG\_I | Código da mensagem |
| Configured from console by con0 | Texto: a configuração foi alterada pelo console |

**Importante:** a palavra "facilidade" tem dois sentidos: a **facilidade do padrão syslog**, que entra no cálculo da PRI, e a **facilidade da Cisco**, escrita na parte MSG (como SYS ou ASA).

### 29.3 Logs dos Servidores

Os servidores de e-mail e web mantêm **logs de acesso e logs de erro**. Os **logs de proxy DNS** registram todas as consultas e respostas e ajudam a identificar computadores que visitaram sites perigosos, a retirada de dados pelo DNS e as conexões com servidores de comando e controle. Nos sistemas UNIX e Linux, os logs usam o syslog.

Exemplo de log de acesso do servidor web Apache:

`203.0.113.127 – dsmith [10/Oct/2016:10:26:57 -0500] "GET /logo_sm.gif HTTP/1.0" 200 2254`

Nesse registro aparecem o IP do cliente, o usuário, a data e a hora, o pedido feito, o código de resposta (200, sucesso) e o tamanho da resposta em bytes. O servidor Microsoft IIS registra informações parecidas, em outro formato.

### 29.4 Logs da Rede

Os equipamentos e serviços da rede geram vários tipos de registro:

- **tcpdump**: analisador de pacotes de linha de comando que captura o tráfego em tempo real ou o grava em arquivo. O Wireshark é uma interface gráfica construída sobre essa funcionalidade;
- **NetFlow**: tecnologia da Cisco que registra **informações sobre os fluxos de tráfego, sem o conteúdo**. O **IPFIX** é a versão padronizada pelo IETF, baseada no NetFlow versão 9;
- **AVC** (*Application Visibility and Control*): reconhece mais de mil aplicativos com o **NBAR2** e permite priorizar ou bloquear cada um;
- filtros de conteúdo: o **Cisco ESA**, para e-mail, e o **Cisco WSA**, para web, que age como proxy e registra todas as transações HTTP;
- **proxies web**: pedem os recursos em nome do cliente e registram todos os pedidos e respostas;
- **Cisco Umbrella**: registra os acessos DNS e mostra se cada consulta foi permitida ou bloqueada;
- **NGFW**: registra eventos de conexão, de intrusão, de hosts, de descoberta de rede e de fluxo.

Um **fluxo**, no NetFlow, é o conjunto de pacotes que seguem **em um único sentido** e têm os mesmos valores em até sete atributos:

- IP de origem;
- IP de destino;
- porta de origem;
- porta de destino;
- protocolo da camada 3;
- classe de serviço;
- interface do roteador ou switch.

Todo registro de fluxo tem os cinco primeiros atributos e os horários de início e de fim, além da contagem de pacotes e bytes. O **exportador** (o equipamento que observa o tráfego) cria os registros e os envia ao **coletor**, que os guarda. Ferramentas como o nfdump leem esses registros, que ajudam a montar a **linha do tempo de um ataque** e a ver o movimento do atacante dentro da rede.

Exemplo de registro: `2017-08-30 00:09:12.596 00.010 TCP 10.1.1.2:80 -> 13.1.1.2:8974 .AP.SF 0 62 3512 1`. Ele mostra o início e a duração do fluxo, o protocolo, a origem e o destino com as portas, os sinalizadores TCP, o número de pacotes e de bytes.

**Importante:** monitorar só pela porta dá pouca informação. O reconhecimento pela **assinatura do aplicativo**, como faz o AVC, mostra **o que o usuário está realmente fazendo**.

O proxy Squid gera registros como este:

| Trecho | Significado |
| --- | --- |
| 1265939281.764 | Data e hora em formato Unix |
| 19478 | Duração em milissegundos |
| 172.16.167.228 | IP do cliente |
| TCP\_MISS/200 | Resultado no Squid e código HTTP |
| 864 | Bytes entregues |
| GET | Método do pedido |
| http://www.example.com//images/home.png | Endereço pedido |
| image/png | Tipo de conteúdo |

**Observação:** os **proxies abertos**, que aceitam pedidos de qualquer pessoa, são usados por atacantes para esconder o próprio IP e por isso costumam entrar em listas de bloqueio.

### 29.5 SIEM

Com tantos logs espalhados, é preciso reuni-los. O **SIEM** (*Security Information and Event Management* — gerenciamento de informações e eventos de segurança) **coleta os logs de toda a rede e oferece relatórios em tempo real e análise de longo prazo**. Suas funções são:

| Função | O que faz |
| --- | --- |
| Coleta | Reúne os logs para investigações e conformidade |
| Normalização | Converte formatos diferentes para um modelo comum |
| Correlação | Liga eventos de sistemas diferentes, acelerando a detecção |
| Agregação | Junta eventos repetidos, reduzindo o volume |
| Relatórios | Mostra eventos em tempo real e resumos em painéis |
| Conformidade | Gera relatórios exigidos por normas |

Exemplos são o **Splunk**, muito usado em centros de operações de segurança, e o conjunto **ELK** (Elasticsearch, Logstash e Kibana), presente no Security Onion.

### 29.6 SOAR

O **SOAR** (*Security Orchestration, Automation and Response* — orquestração, automação e resposta de segurança) **vai além do SIEM: automatiza as etapas da resposta a incidentes**. Ele ajuda equipes com poucos profissionais e muitos painéis diferentes, unificando ferramentas de vários fabricantes. Exemplos são o Fortinet FortiSOAR e o Palo Alto Networks Cortex XSOAR. O curso também cita o Cisco SecureX, já descontinuado.

SIEM → reúne e correlaciona os eventos; SOAR → responde a eles de forma automatizada.

## 30. Avaliação de Alertas

É impossível evitar todos os ataques: muitas vezes eles só são detectados durante ou depois do acontecimento. Por isso, os alertas gerados pelas ferramentas de monitoramento precisam ser avaliados por analistas, que decidem o que é real e o que não é.

### 30.1 Security Onion

Relembrando: o **Security Onion** é um **conjunto gratuito e de código aberto de ferramentas de monitoramento de segurança** de rede. O curso descreve a versão legada, que rodava no Ubuntu Linux; a versão 2 usa outro sistema e trocou ferramentas como o Sguil e o CapMe por novas interfaces. Ele tem três funções:

- capturar pacotes e outros tipos de dados;
- detectar intrusões na rede e nos hosts;
- analisar os alertas.

Pode ser instalado em um único equipamento ou dividido entre sensores e um servidor. Sua arquitetura tem três níveis:

Dados (capturas, sessões, transações, logs, alertas) → Detecção (Snort, Zeek, OSSEC, Suricata, Wazuh, CapMe) → Análise (Sguil, Kibana, Wireshark)

**Observação:** o nome Security Onion não tem relação com a analogia da cebola usada na defesa em profundidade.

As ferramentas de detecção são:

| Ferramenta | Tipo | Função |
| --- | --- | --- |
| Snort | IDS de rede | Usa regras e assinaturas; é a principal fonte de alertas no Sguil |
| Suricata | IDS de rede | Usa assinaturas, como o Snort, e pode bloquear o tráfego; aproveita vários núcleos do processador |
| Zeek | IDS de rede | Analisa o comportamento, conforme políticas escritas em scripts |
| OSSEC | HIDS | Verifica a integridade de arquivos, logs locais, processos e rootkits |
| Wazuh | HIDS | Sucessor do OSSEC; acrescenta detecção de vulnerabilidades e resposta a incidentes |
| CapMe | Aplicação web | Mostra a transcrição de uma sessão capturada e a abre no Wireshark |

O **PulledPork** baixa automaticamente as regras novas do Snort.

As ferramentas de análise são:

- **Sguil**: console que reúne os alertas e é o **ponto de partida da investigação**, de onde o analista "pivota" para outras ferramentas;
- **Kibana**: painel interativo para consultar e visualizar os dados guardados no Elasticsearch;
- **Wireshark**: análise das capturas completas de pacotes;
- **Zeek**: também serve para análise, com logs precisos das transações e do conteúdo dos arquivos.

### 30.2 Alertas no Sguil

Os **alertas** são **mensagens de notificação geradas pelas ferramentas de monitoramento**. Eles são gerados por regras, assinaturas, anomalias ou comportamentos, sempre a partir de condições definidas antes. Suas fontes são:

- IDS de rede: Snort, Zeek e Suricata;
- HIDS: OSSEC e Wazuh;
- detecção passiva de ativos (**PADS**, *Passive Asset Detection System*);
- transações HTTP, DNS e TCP registradas pelo Zeek e pelas capturas;
- mensagens de syslog.

O Sguil organiza os alertas em uma fila, com data e hora, e o analista investiga, classifica, encaminha ou descarta cada um. Todo alerta traz a **5-tupla**, o horário e qual equipamento o gerou; alguns trazem também se o tráfego foi permitido ou negado, um trecho do conteúdo ou o hash de um arquivo.

| Campo do Sguil | Significado |
| --- | --- |
| ST | Status; a cor indica a prioridade, em quatro níveis, do amarelo claro ao vermelho |
| CNT | Quantidade de eventos agrupados com os mesmos IPs de origem e destino |
| Sensor | Agente que relatou o evento |
| Alert ID | Identificação no formato sensor.evento (exemplo: 1.24) |
| Date/Time | Data e hora do primeiro evento agrupado |
| Event Message | Texto da regra que gerou o alerta |

**Observação:** um CNT muito alto pode indicar um problema sério ou uma assinatura que precisa de ajuste.

### 30.3 Regras do Snort

Uma regra do Snort tem três partes:

- **cabeçalho**: ação, protocolo, endereços e portas de origem e de destino, e direção;
- **opções**: entre parênteses, com a mensagem, o conteúdo a procurar, a categoria e a identificação;
- **local da regra**: o arquivo e a linha onde ela está, acrescentados pelo Sguil.

Exemplo de regra:

`alert tcp $EXTERNAL_NET any -> $HOME_NET 21 (msg:"ET EXPLOIT VSFTPD backdoor user login smiley"; flow:established,to_server; content:"USER"; depth:5; content:"|3a 29|"; distance:0; classtype:attempted-admin; sid:2013188; rev:4;)`

| Trecho | Significado |
| --- | --- |
| alert | Ação: gerar um alerta (outras são log e pass) |
| tcp | Protocolo |
| $EXTERNAL\_NET any | Qualquer porta de qualquer endereço externo |
| -> | Direção do tráfego |
| $HOME\_NET 21 | Porta 21 (FTP) da rede interna |
| msg | Texto exibido no alerta |
| content | Conteúdo procurado no pacote |
| classtype | Categoria do ataque, ligada a um nível de prioridade |
| sid | Identificação única da regra |
| rev | Número da revisão da regra |

As variáveis $HOME\_NET e $EXTERNAL\_NET são definidas no arquivo de configuração do Snort (snort.conf). Essa regra detecta a tentativa de usar uma porta dos fundos conhecida do servidor FTP vsftpd, acionada por um nome de usuário com ":)" (em hexadecimal, 3a 29).

As regras têm três origens principais:

| Origem | Características |
| --- | --- |
| GPL | Regras antigas, da Sourcefire, sob licença GPLv2; identificações até 3464 |
| ET (Emerging Threats) | Mantidas pela Proofpoint, sob licença BSD |
| VRT | Mantidas pelo Cisco Talos; assinantes recebem na hora, usuários registrados após 30 dias |

Também existem regras locais, criadas pela própria organização.

### 30.4 Classificação dos Alertas

As regras de detecção devem ser **propositalmente conservadoras**: é melhor gerar alertas para tráfego inocente do que deixar passar um ataque. Por isso, cada alerta precisa ser avaliado. O analista de **nível 1** trabalha a fila do Sguil e consulta o Zeek, o Wireshark e o Kibana.

A classificação é emprestada do diagnóstico médico. "Positivo" e "negativo" dizem se houve alerta; "verdadeiro" e "falso" dizem se o alerta (ou a ausência dele) estava certo:

|  | Verdadeiro | Falso |
| --- | --- | --- |
| Positivo (houve alerta) | Ocorreu um incidente | Não ocorreu incidente |
| Negativo (não houve alerta) | Não ocorreu incidente | Ocorreu um incidente |

Cada caso tem uma consequência:

- **verdadeiro positivo**: a regra funcionou e o incidente precisa ser tratado;
- **falso positivo**: o alerta foi gerado por atividade inofensiva (um **gatilho benigno**). É indesejável e custa tempo dos analistas, mas é inevitável;
- **verdadeiro negativo**: tráfego inofensivo ignorado corretamente; é o desejável;
- **falso negativo**: **um ataque aconteceu e nenhum alerta foi gerado**. É o caso **mais perigoso**, porque o ataque pode continuar sem ser visto por muito tempo.

O que fazer em cada situação:

- verdadeiro positivo suspeito → **encaminhar para o nível superior**, que confirma o incidente, avalia o dano e coordena isolamento, correção e relato;
- excesso de falsos positivos → informar para que as regras sejam ajustadas. Mudanças na rede ou regras novas costumam provocar picos de falsos positivos;
- falso negativo descoberto depois → usar a **RSA** (*Retrospective Security Analysis* — análise de segurança retrospectiva): **aplicar regras e informações novas aos dados guardados**, para descobrir se a rede esteve exposta e qual foi o dano.

### 30.5 Análise Determinística e Probabilística

Há duas formas de raciocinar sobre um possível ataque:

- **análise determinística**: parte do princípio de que, para o ataque dar certo, **todas as etapas anteriores precisam ter dado certo**. O analista conhece as etapas e suas características, como as portas padrão usadas. Ela descreve o pior caso, e como o atacante pode falhar em alguma etapa, existe a chance de detectá-lo no caminho;
- **análise probabilística**: usa **estatística para estimar a probabilidade** de cada etapa seguinte, dado que a anterior deu certo. É útil em tempo real, com muitas variáveis e decisões do atacante desconhecidas, e é necessária contra ataques que usam **portas dinâmicas** para escapar de firewalls com regras fixas.

| Característica | Determinística | Probabilística |
| --- | --- | --- |
| Base | Etapas conhecidas do ataque | Estatística |
| Resultado | Pior caso | Caminhos mais prováveis |
| Melhor uso | Ataques com etapas e portas conhecidas | Tempo real, portas dinâmicas e muitas incógnitas |

## Glossário de Siglas

| Sigla | Nome completo | Significado |
| --- | --- | --- |
| AAA | Authentication, Authorization and Accounting | Autenticação, autorização e contabilidade dos acessos |
| ABAC | Attribute-Based Access Control | Controle de acesso baseado em atributos |
| ACE | Access Control Entry | Cada linha de permitir ou negar de uma ACL |
| ACL | Access Control List | Lista de controle de acesso que filtra pacotes |
| AES | Advanced Encryption Standard | Algoritmo simétrico recomendado, com bloco de 128 bits |
| AMP | Advanced Malware Protection | Proteção avançada contra malware da Cisco |
| AP | Access Point | Ponto de acesso sem fio |
| API | Application Programming Interface | Conjunto de comandos pelo qual programas se comunicam |
| APIPA | Automatic Private IP Addressing | Endereço 169.254.x.x criado pelo computador sem DHCP |
| ARP | Address Resolution Protocol | Descobre o endereço MAC a partir do IP |
| ASA | Adaptive Security Appliance | Firewall da Cisco |
| AUP | Acceptable Use Policy | Política de uso aceitável |
| AVC | Application Visibility and Control | Reconhece e controla aplicativos na rede |
| BGP | Border Gateway Protocol | Protocolo de roteamento entre redes da internet |
| BYOD | Bring Your Own Device | Uso de aparelhos pessoais no trabalho |
| C&C (CNC) | Command and Control | Servidor que dá ordens a um malware |
| C3PL | Cisco Common Classification Policy Language | Linguagem usada para escrever as políticas do ZPF |
| CA | Certificate Authority | Autoridade que emite certificados digitais |
| CCMP | Counter Mode with CBC-MAC Protocol | Protocolo de criptografia do WPA2, baseado no AES |
| CER | Crossover Error Rate | Taxa de erro de cruzamento dos sistemas biométricos |
| CFTV (CCTV) | Circuito Fechado de Televisão (Closed-Circuit Television) | Vigilância por câmeras |
| CHAP | Challenge Handshake Authentication Protocol | Autenticação por desafio e resposta com hash |
| CIA (CID) | Confidentiality, Integrity, Availability | Tríade confidencialidade, integridade e disponibilidade |
| COPE | Corporate-Owned, Personally Enabled | Aparelho da empresa com uso pessoal permitido |
| CRL | Certificate Revocation List | Lista de certificados revogados |
| CSA | Cloud Security Alliance | Aliança de Segurança na Nuvem |
| CSP | Cloud Service Provider | Provedor de serviços de nuvem |
| CSPRNG | Cryptographically Secure Pseudo-Random Number Generator | Gerador de números aleatórios seguro para criptografia |
| DAC | Discretionary Access Control | Controle de acesso discricionário, definido pelo dono |
| DDoS | Distributed Denial of Service | Negação de serviço com muitos atacantes ao mesmo tempo |
| DES | Data Encryption Standard | Algoritmo simétrico antigo, com bloco de 64 bits |
| DH | Diffie-Hellman | Algoritmo para combinar uma chave secreta pela rede |
| DHCP | Dynamic Host Configuration Protocol | Atribui endereços IP automaticamente |
| DLP | Data Loss Prevention | Prevenção de perda (vazamento) de dados |
| DMZ | Demilitarized Zone | Zona desmilitarizada, onde ficam os servidores públicos |
| DNS | Domain Name System | Converte nomes em endereços IP |
| DNSSEC | DNS Security Extensions | Extensões que autenticam as respostas DNS |
| DoS | Denial of Service | Negação de serviço |
| DSA | Digital Signature Algorithm | Algoritmo de assinatura digital |
| DSS | Digital Signature Standard | Padrão de assinatura digital que usa o DSA |
| EAP | Extensible Authentication Protocol | Estrutura de autenticação usada em redes sem fio e 802.1X |
| ECC | Elliptic Curve Cryptography | Criptografia de curvas elípticas |
| ECDSA | Elliptic Curve Digital Signature Algorithm | Assinatura digital com curvas elípticas |
| EFS | Encrypting File System | Criptografia de arquivos do Windows |
| ELK | Elasticsearch, Logstash, Kibana | Conjunto de ferramentas para guardar e analisar logs |
| ESA | Email Security Appliance | Filtro de conteúdo de e-mail da Cisco |
| ET | Emerging Threats | Fonte de regras do Snort mantida pela Proofpoint |
| FIPS | Federal Information Processing Standards | Padrões de segurança do governo dos EUA |
| FPGA | Field-Programmable Gate Array | Circuito reprogramável depois de instalado |
| FTP | File Transfer Protocol | Transferência de arquivos, em texto claro |
| FTPS | FTP Secure | FTP protegido por SSL/TLS |
| GLBP | Gateway Load Balancing Protocol | Protocolo de redundância de gateway da Cisco |
| GPL | GNU General Public License | Licença de software livre; também nome de regras antigas do Snort |
| GPS | Global Positioning System | Sistema de posicionamento global por satélites |
| HIDS | Host-based Intrusion Detection System | Detecção de intrusão instalada no host |
| HMAC | Hash-based Message Authentication Code | Hash com chave secreta, que garante integridade e autenticidade |
| HSRP | Hot Standby Router Protocol | Protocolo de redundância de roteador da Cisco |
| HTTP | Hypertext Transfer Protocol | Protocolo da web, em texto claro |
| HTTPS | HTTP Secure | HTTP protegido por SSL/TLS |
| HVAC | Heating, Ventilation and Air Conditioning | Aquecimento, ventilação e ar-condicionado |
| IaaS | Infrastructure as a Service | Infraestrutura como serviço |
| IAM | Identity and Access Management | Gerenciamento de identidade e acesso |
| ICMP | Internet Control Message Protocol | Mensagens de erro e de teste, como o ping |
| ICS | Industrial Control Systems | Sistemas de controle industrial |
| IDS | Intrusion Detection System | Sistema de detecção de intrusão |
| IETF | Internet Engineering Task Force | Organização que cria os padrões da internet |
| IIS | Internet Information Services | Servidor web da Microsoft |
| IKE | Internet Key Exchange | Troca de chaves nas VPNs IPsec |
| IMAP | Internet Message Access Protocol | Protocolo de recebimento de e-mail |
| IoT | Internet of Things | Internet das Coisas |
| IP | Internet Protocol | Protocolo de endereçamento e roteamento da internet |
| IPFIX | IP Flow Information Export | Padrão do IETF para registros de fluxo, baseado no NetFlow v9 |
| IPS | Intrusion Prevention System | Sistema de prevenção de intrusão |
| IPsec | IP Security | Conjunto de protocolos que protege o tráfego IP, usado em VPNs |
| KBA | Knowledge-Based Authentication | Autenticação baseada em conhecimento |
| LAN | Local Area Network | Rede local |
| LDAP | Lightweight Directory Access Protocol | Protocolo de consulta a serviços de diretório |
| LGPD | Lei Geral de Proteção de Dados | Lei brasileira de proteção de dados pessoais |
| LSASS | Local Security Authority Subsystem Service | Serviço do Windows que gera o log de segurança |
| LSB | Least Significant Bits | Bits menos significativos, usados na esteganografia |
| MAC | Mandatory Access Control | Controle de acesso obrigatório (também: código de autenticação de mensagem; endereço físico) |
| MD5 | Message Digest 5 | Algoritmo de hash de 128 bits, inseguro |
| MDM | Mobile Device Management | Gerenciamento de dispositivos móveis |
| MFA | Multi-Factor Authentication | Autenticação multifator |
| MitM | Man-in-the-Middle | Ataque em que o criminoso se coloca entre as duas partes |
| MTU | Maximum Transmission Unit | Tamanho máximo de pacote |
| NAC | Network Access Control | Controle de acesso à rede |
| NAT | Network Address Translation | Tradução de endereços de rede |
| NBA | Network Behavior Analysis | Análise de comportamento de rede |
| NBAD | Network Behavior Anomaly Detection | Detecção de anomalias de comportamento de rede |
| NBAR2 | Network-Based Application Recognition 2 | Reconhecimento de aplicativos da Cisco |
| NDP | Neighbor Discovery Protocol | Descoberta de vizinhos no IPv6 |
| NFC | Near-Field Communication | Comunicação por proximidade |
| NGFW | Next-Generation Firewall | Firewall de última geração |
| NIST | National Institute of Standards and Technology | Instituto de padrões dos EUA |
| NSA | National Security Agency | Agência de segurança nacional dos EUA |
| NSM | Network Security Monitoring | Monitoramento de segurança de rede |
| NTP | Network Time Protocol | Sincroniza os relógios dos dispositivos |
| OCSP | Online Certificate Status Protocol | Consulta on-line do status de um certificado |
| OSI | Open Systems Interconnection | Modelo de referência em sete camadas |
| OSPF | Open Shortest Path First | Protocolo de roteamento |
| OWASP | Open Web Application Security Project | Organização dedicada à segurança de aplicações web |
| P2P | Peer-to-Peer | Rede em que cada computador é cliente e servidor |
| PaaS | Platform as a Service | Plataforma como serviço |
| PADS | Passive Asset Detection System | Sistema de detecção passiva de ativos |
| PAP | Password Authentication Protocol | Autenticação com senha em texto claro |
| PAT | Port Address Translation | NAT com sobrecarga, que usa portas para muitos hosts |
| PEAP | Protected EAP | EAP protegido por túnel TLS |
| PGP | Pretty Good Privacy | Privacidade e autenticação em e-mails |
| PIN | Personal Identification Number | Senha numérica pessoal |
| PKCS | Public Key Cryptography Standards | Padrões de criptografia de chave pública |
| PKI | Public Key Infrastructure | Infraestrutura de chave pública |
| POP3 | Post Office Protocol 3 | Protocolo de recebimento de e-mail |
| PPP | Point-to-Point Protocol | Protocolo de enlace ponto a ponto |
| PRI | Priority | Parte da mensagem syslog com facilidade e gravidade |
| QA | Quality Assurance | Garantia de qualidade |
| RA | Registration Authority | Autoridade de registro, que confere a identidade antes de a CA emitir o certificado |
| RADIUS | Remote Authentication Dial-In User Service | Servidor de autenticação AAA, padrão aberto |
| RAID | Redundant Array of Independent Disks | Conjunto de discos com distribuição e redundância |
| RBAC | Role-Based Access Control | Controle de acesso baseado em funções |
| RFC | Request for Comments | Documento que define padrões da internet |
| RFID | Radio-Frequency Identification | Identificação por radiofrequência |
| RIP | Routing Information Protocol | Protocolo de roteamento |
| RSA | Rivest, Shamir, Adleman | Algoritmo assimétrico (também: análise de segurança retrospectiva) |
| RTOS | Real-Time Operating System | Sistema operacional de tempo real |
| SaaS | Software as a Service | Software como serviço |
| SCADA | Supervisory Control and Data Acquisition | Controle de supervisão e aquisição de dados industriais |
| SCP | Secure Copy Protocol | Cópia segura de arquivos sobre SSH |
| SDN | Software-Defined Networking | Rede definida por software |
| SEAL | Software-Optimized Encryption Algorithm | Cifra de fluxo com chave de 160 bits |
| SFF | Small Form Factor | Hardware de tamanho reduzido |
| SHA | Secure Hash Algorithm | Família de algoritmos de hash |
| SIEM | Security Information and Event Management | Gerenciamento de informações e eventos de segurança |
| SMTP | Simple Mail Transfer Protocol | Protocolo de envio de e-mail |
| SNMP | Simple Network Management Protocol | Gerenciamento e monitoramento de equipamentos de rede |
| SOAR | Security Orchestration, Automation and Response | Orquestração, automação e resposta de segurança |
| SoC | System on Chip | Sistema completo em um único chip |
| SPOF | Single Point of Failure | Ponto único de falha |
| SQL | Structured Query Language | Linguagem de consulta a bancos de dados |
| SSH | Secure Shell | Acesso remoto seguro por linha de comando |
| SSL | Secure Sockets Layer | Protocolo de criptografia antecessor do TLS |
| SSO | Single Sign-On | Logon único |
| STP | Spanning Tree Protocol | Evita loops bloqueando caminhos redundantes entre switches |
| TACACS+ | Terminal Access Controller Access-Control System Plus | Servidor de autenticação AAA da Cisco |
| TCP | Transmission Control Protocol | Protocolo de transporte orientado à conexão |
| TGT | Ticket-Granting Ticket | Tíquete de concessão de tíquete do Kerberos |
| TI | Tecnologia da Informação | Área responsável pelos sistemas e redes |
| TKIP | Temporal Key Integrity Protocol | Protocolo de criptografia do WPA |
| TLS | Transport Layer Security | Protocolo de criptografia das conexões, sucessor do SSL |
| UAV | Unmanned Aerial Vehicle | Veículo aéreo não tripulado (drone) |
| UDP | User Datagram Protocol | Protocolo de transporte sem conexão |
| UPS | Uninterruptible Power Supply | Nobreak |
| URL | Uniform Resource Locator | Endereço de um recurso na web |
| USB | Universal Serial Bus | Padrão de conexão de dispositivos |
| VDI | Virtual Desktop Infrastructure | Infraestrutura de desktops virtuais |
| VLAN | Virtual Local Area Network | Rede local virtual |
| VM | Virtual Machine | Máquina virtual |
| VoIP | Voice over IP | Voz sobre IP |
| VPC | Virtual Private Cloud | Nuvem privada virtual |
| VPN | Virtual Private Network | Rede privada virtual |
| VRRP | Virtual Router Redundancy Protocol | Protocolo aberto de redundância de roteador |
| VRT | Vulnerability Research Team | Regras do Snort mantidas pelo Cisco Talos |
| VTY | Virtual Teletype | Linhas virtuais de acesso remoto ao roteador |
| WEP | Wired Equivalent Privacy | Primeiro padrão de segurança Wi-Fi, inseguro |
| WPA | Wi-Fi Protected Access | Padrões de segurança Wi-Fi (WPA, WPA2, WPA3) |
| WPS | Wi-Fi Protected Setup | Conexão simplificada ao Wi-Fi, vulnerável |
| WSA | Web Security Appliance | Proxy e filtro de conteúdo web da Cisco |
| XaaS | Anything as a Service | Qualquer coisa como serviço |
| ZPF | Zone-Based Policy Firewall | Firewall de política baseada em zona |

## Exercícios

### A. Cálculo de Disponibilidade (ver item 18.2)

Considere um ano de 365 dias.

1. Calcule o tempo máximo de inatividade por ano, em minutos, de um sistema com 99,9% de disponibilidade.
2. Calcule o tempo máximo de inatividade por ano de um sistema com 99,99% de disponibilidade.
3. Calcule o tempo máximo de inatividade por ano de um sistema com 99,95% de disponibilidade e converta o resultado em horas e minutos.
4. Um servidor ficou fora do ar por 30 minutos em um ano. Calcule sua disponibilidade e informe se ele atingiu os cinco noves.

### B. Dígito Verificador do ISBN-10 (ver item 14.3)

1. Calcule o dígito verificador do ISBN-10 cujos nove primeiros dígitos são 0 3 0 6 4 0 6 1 5.
2. Calcule o dígito verificador do ISBN-10 cujos nove primeiros dígitos são 8 5 7 5 2 2 0 0 3.
3. Um usuário digitou o ISBN 0-306-40615-7. Indique se a validação aceita ou rejeita esse número e por quê.

### C. Máscaras Curinga (ver item 20.5)

1. Informe a máscara curinga para a rede 192.168.50.0/24.
2. Informe a máscara curinga para a rede 172.16.8.64/26 e o comando `permit` correspondente.
3. Informe a máscara curinga que reúne as redes 10.1.4.0/24 a 10.1.7.0/24 em uma única entrada.
4. Indique o primeiro e o último endereço que correspondem a `192.168.5.16 0.0.0.15`, mostrando o último octeto em binário.
5. Indique a faixa de endereços que corresponde a `172.16.32.0 0.0.7.255`.
6. Escreva a entrada que permite apenas o host 192.168.1.20 de duas formas: com máscara curinga e com a palavra-chave correspondente.

### D. Prioridade do Syslog (ver item 29.2)

1. Calcule a prioridade de uma mensagem com facilidade local7 e gravidade 6.
2. Calcule a prioridade de uma mensagem com facilidade local0 e gravidade 4.
3. Uma mensagem começa com <165>. Informe o número da facilidade, o nome da facilidade local e o nome da gravidade.
4. Uma mensagem começa com <11>. Informe o número da facilidade e o nome da gravidade.
5. Na mensagem `%SYS-5-CONFIG_I: Configured from console by con0`, indique a facilidade Cisco, a gravidade e o código da mensagem.

### E. Posicionamento de ACLs e Firewalls (ver itens 21.7, 23.5 e 24.5)

1. Indique onde aplicar uma ACL padrão que impede a rede 192.168.10.0/24 de acessar a rede 192.168.30.0/24 e justifique.
2. Indique onde aplicar uma ACL estendida que impede a rede 192.168.11.0/24 de usar Telnet com a rede 192.168.30.0/24 e justifique.
3. Classifique cada tráfego, em um firewall com DMZ, como bloqueado, permitido seletivamente ou permitido com inspeção: a) da rede pública para a privada; b) da rede pública para o servidor web da DMZ; c) da rede privada para a internet; d) da DMZ para a rede privada.
4. Em um roteador com ZPF, a interface G0/0 está na zona PRIVATE e a interface G0/1 não pertence a nenhuma zona. Indique o que acontece com o tráfego entre elas.

### F. Classificação de Alertas (ver item 30.4)

Classifique cada situação como verdadeiro positivo, falso positivo, verdadeiro negativo ou falso negativo.

1. O IDS gerou um alerta de exploração do FTP, e a investigação confirmou que um atacante entrou no servidor.
2. O IDS gerou um alerta porque um administrador fez uma varredura autorizada na rede.
3. Um malware retirou dados por DNS durante meses sem que nenhum alerta fosse gerado.
4. Um usuário navegou normalmente na web, e nenhum alerta foi gerado.
5. Indique qual dos quatro casos é o mais perigoso e por quê.

### G. Questões Conceituais: Fundamentos e Criptografia (ver itens 1 a 8)

1. Explique a diferença entre confidencialidade, integridade e disponibilidade, com um exemplo de cada.
2. Diferencie a analogia da cebola da analogia da alcachofra na defesa em profundidade.
3. Indique por que a criptografia simétrica é usada para grandes volumes de dados e a assimétrica para trocar chaves.
4. Explique por que o hash sozinho não protege contra o ataque man-in-the-middle e qual recurso resolve esse problema.
5. Informe o que é criptografado em uma assinatura digital e se ela, sozinha, garante confidencialidade.
6. Diferencie mascaramento de dados de esteganografia.

### H. Questões Conceituais: Controle de Acesso (ver itens 9 a 12)

1. Cite os três fatores de autenticação e dê um exemplo de cada.
2. Diferencie os modelos DAC, MAC e RBAC.
3. Explique o princípio da confiança zero.
4. Compare o TACACS+ e o RADIUS quanto ao transporte e à criptografia.

### I. Questões Conceituais: Proteção de Sistemas e da Rede (ver itens 13 a 19)

1. Explique a função da CER na escolha de um sistema biométrico.
2. Indique por que o Telnet deve ser substituído pelo SSH.
3. Explique a função da DMZ.
4. Indique por que o WEP e o WPS não devem ser usados.
5. Explique por que o RAID 0 não protege contra a falha de um disco.
6. Explique por que os sistemas SCADA são vulneráveis e qual é a principal medida de proteção.
7. Indique a finalidade de um honeypot.

### J. Questões Conceituais: Filtragem de Tráfego (ver itens 20 a 24)

1. Diferencie a ACL padrão da ACL estendida.
2. Explique a negação implícita e sua consequência para uma ACL que só tem instruções deny.
3. Explique o efeito da palavra-chave established.
4. Indique os cuidados com o deny ipv6 any any explícito em uma ACL IPv6.
5. Diferencie o firewall de filtragem de pacotes do firewall com estado.
6. Diferencie as ações Inspect, Pass e Drop do ZPF.

### K. Questões Conceituais: Nuvem (ver itens 25 e 26)

1. Diferencie o hypervisor tipo 1 do tipo 2.
2. Diferencie a máquina virtual do contêiner.
3. Diferencie SaaS, PaaS e IaaS.
4. Indique qual responsabilidade é sempre do cliente no modelo de responsabilidade compartilhada.
5. Explique a expansão de VMs e a fuga de VM.

### L. Questões Conceituais: Monitoramento (ver itens 27 a 30)

1. Explique por que o NTP é importante para a análise dos logs.
2. Indique dois sinais de retirada de dados pelo DNS.
3. Explique por que o PAT dificulta a investigação.
4. Diferencie dados de sessão de dados de transação.
5. Diferencie o SIEM do SOAR.
6. Diferencie a análise determinística da análise probabilística.

## Gabarito

### A. Cálculo de Disponibilidade

1. 525.600 × 0,001 = **525,6 minutos** (cerca de 8 horas e 46 minutos).
2. 525.600 × 0,0001 = **52,56 minutos**.
3. 525.600 × 0,0005 = **262,8 minutos**, ou **4 horas e 22,8 minutos**.
4. Disponibilidade = (525.600 − 30) ÷ 525.600 = **99,9943%**. **Não** atingiu os cinco noves, que permitem no máximo 5,26 minutos por ano.

### B. Dígito Verificador do ISBN-10

1. Produtos: 0, 27, 0, 42, 24, 0, 24, 3, 10; soma = 130. Múltiplo de 11 seguinte: 132. Dígito verificador = **2**.
2. Produtos: 80, 45, 56, 35, 12, 10, 0, 0, 6; soma = 244. Múltiplo de 11 seguinte: 253. Dígito verificador = **9**.
3. A validação **rejeita** o número: o dígito verificador correto é 2 (questão 1), e com 7 a soma total (130 + 7 = 137) não é múltipla de 11.

### C. Máscaras Curinga

1. 255.255.255.255 − 255.255.255.0 = **0.0.0.255**.
2. /26 = 255.255.255.192; 255 − 192 = 63 → **0.0.0.63**; comando: `permit 172.16.8.64 0.0.0.63`.
3. As quatro redes formam 10.1.4.0/22 (255.255.252.0); 255 − 252 = 3 → **0.0.3.255** (`10.1.4.0 0.0.3.255`).
4. 16 = 0001 0000 e 15 = 0000 1111; os 4 primeiros bits (0001) são verificados. Primeiro: 0001 0000 = **192.168.5.16**; último: 0001 1111 = **192.168.5.31**.
5. No terceiro octeto, 32 = 0010 0000 e 7 = 0000 0111; os 5 primeiros bits (00100) são verificados, de 32 a 39. Faixa: **172.16.32.0 a 172.16.39.255**.
6. `permit 192.168.1.20 0.0.0.0` e `permit host 192.168.1.20`.

### D. Prioridade do Syslog

1. local7 = 23; 23 × 8 + 6 = **190** (<190>).
2. local0 = 16; 16 × 8 + 4 = **132** (<132>).
3. 165 ÷ 8 = 20, resto 5 → facilidade **20 (local4)**, gravidade **5 (Notificação)**.
4. 11 ÷ 8 = 1, resto 3 → facilidade **1**, gravidade **3 (Erro)**.
5. Facilidade Cisco **SYS**, gravidade **5 (Notificação)**, código **CONFIG\_I**.

### E. Posicionamento de ACLs e Firewalls

1. Na **saída da interface do roteador ligada à rede 192.168.30.0/24**, isto é, perto do destino, porque a ACL padrão só enxerga a origem; perto da origem, bloquearia a rede 192.168.10.0/24 para todos os destinos.
2. Na **entrada da interface do roteador ligada à rede 192.168.11.0/24**, isto é, perto da origem, para que o tráfego bloqueado não atravesse a rede.
3. a) bloqueado; b) permitido seletivamente e inspecionado; c) permitido com inspeção; d) geralmente bloqueado.
4. O tráfego **é descartado**: ele nunca flui entre uma interface que está em zona e outra que não está.

### F. Classificação de Alertas

1. Verdadeiro positivo.
2. Falso positivo (gatilho benigno).
3. Falso negativo.
4. Verdadeiro negativo.
5. O **falso negativo**, porque o ataque acontece sem ser detectado e pode continuar causando dano por muito tempo.

### G. Questões Conceituais: Fundamentos e Criptografia

1. Confidencialidade: só pessoas autorizadas leem a informação (exemplo: folha de pagamento restrita ao RH). Integridade: a informação está completa e não foi alterada (exemplo: valor de uma transferência). Disponibilidade: a informação está acessível quando necessária (exemplo: site do banco no ar).
2. Na cebola, o atacante precisa atravessar todas as camadas, uma a uma; na alcachofra, que representa as redes sem fronteiras, basta remover algumas "folhas" para chegar aos dados.
3. A simétrica é muito mais rápida e por isso serve para grandes volumes; a assimétrica é lenta, mas não exige segredo combinado antes, por isso é usada para trocar chaves e assinar.
4. O atacante pode alterar a mensagem e calcular um novo hash, que vai bater. O **HMAC** resolve, porque o hash depende de uma chave secreta que o atacante não tem.
5. Criptografa-se o **hash** do documento com a chave privada do autor. Sozinha, ela **não** garante confidencialidade, porque o documento continua legível.
6. O mascaramento substitui os dados confidenciais por uma versão não confidencial que parece e funciona como a original, sobretudo para testes; a esteganografia esconde uma mensagem dentro de outro arquivo, sem chamar atenção.

### H. Questões Conceituais: Controle de Acesso

1. Algo que a pessoa sabe (senha), algo que ela tem (cartão inteligente ou token) e algo que ela é (impressão digital).
2. DAC: o dono dos dados decide quem acessa. MAC: o acesso depende de rótulos de segurança dos dados e da autorização do usuário, de forma rígida. RBAC: o acesso depende da função ou do cargo.
3. "Nunca confie, sempre verifique": ninguém é confiável automaticamente, nem dentro da rede, e cada acesso precisa ser verificado.
4. TACACS+: usa TCP (porta 49) e criptografa todos os dados. RADIUS: usa UDP e criptografa apenas a senha.

### I. Questões Conceituais: Proteção de Sistemas e da Rede

1. A CER é o ponto em que a taxa de falsa rejeição e a de falsa aceitação se igualam; quanto menor a CER, mais preciso o sistema.
2. O Telnet envia tudo em texto claro, inclusive usuário e senha; o SSH criptografa a sessão.
3. A DMZ é uma rede intermediária que abriga os servidores acessados pelo público, separando-os da rede interna.
4. O WEP é fraco e fácil de quebrar; no WPS, o PIN pode ser descoberto por força bruta.
5. Porque o RAID 0 só distribui os dados entre os discos, sem espelhamento nem paridade; se um disco falhar, os dados se perdem.
6. Foram projetados sem conexão com a rede corporativa e a internet, sem pensar em segurança digital; a principal proteção é separar a rede SCADA da rede da empresa.
7. Atrair o atacante para um sistema-isca, desviando-o dos recursos reais e revelando como ele age.

### J. Questões Conceituais: Filtragem de Tráfego

1. A padrão filtra só pelo IPv4 de origem; a estendida filtra por origem, destino, protocolo e portas.
2. Toda ACL termina com uma instrução oculta que nega tudo o que não foi permitido; uma ACL só com deny bloqueia todo o tráfego.
3. Permite apenas os segmentos TCP com ACK ou RST ativados, ou seja, as respostas de conexões abertas de dentro; conexões iniciadas de fora são negadas.
4. Antes dele, é preciso permitir as mensagens nd-na e nd-ns; caso contrário, o NDP para de funcionar.
5. O filtro de pacotes analisa cada pacote isoladamente, com regras fixas; o firewall com estado acompanha as conexões em uma tabela de estado e verifica se cada pacote pertence a uma conexão existente.
6. Inspect: inspeção com estado, permitindo as respostas automaticamente. Pass: permite sem estado e em um único sentido. Drop: descarta em silêncio, e é a ação padrão.

### K. Questões Conceituais: Nuvem

1. O tipo 1 roda diretamente sobre o hardware; o tipo 2 é um aplicativo instalado sobre um sistema operacional comum.
2. A VM tem sistema operacional completo; o contêiner leva só o aplicativo e as dependências e compartilha o núcleo do host.
3. SaaS: software pronto. PaaS: plataforma para desenvolver e publicar aplicativos. IaaS: recursos de computação virtualizados.
4. Os **dados**.
5. Expansão de VMs: acúmulo de VMs esquecidas ou subutilizadas, que consomem recursos e ficam desatualizadas. Fuga de VM: a VM rompe o isolamento e interage com o sistema do host.

### L. Questões Conceituais: Monitoramento

1. Os logs têm carimbo de data e hora; só com relógios sincronizados é possível juntar os rastros de um mesmo ataque registrados em equipamentos diferentes.
2. Subdomínios muito mais longos que o normal e consultas a domínios ou subdomínios aleatórios, sobretudo se a quantidade aumentar muito.
3. Todos os dispositivos internos saem com o mesmo endereço público, o que dificulta saber qual deles fez cada pedido.
4. A sessão é todo o tráfego da conversa, registrado sem o conteúdo; a transação é o próprio pedido e sua resposta.
5. O SIEM reúne, normaliza e correlaciona os eventos; o SOAR automatiza a resposta a eles.
6. A determinística parte das etapas conhecidas do ataque e descreve o pior caso; a probabilística usa estatística para estimar os caminhos mais prováveis, sendo útil em tempo real e contra portas dinâmicas.
