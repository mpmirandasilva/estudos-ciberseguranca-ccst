# Defesa de Rede

Nov 4, 2026 · Maria Paula

## 1. Fundamentos da Defesa de Redes

A **defesa de rede** é o conjunto de medidas, tecnologias e processos que **protegem os recursos de uma organização contra ataques**.

Antes de escolher qualquer ferramenta, é preciso saber o que proteger, quais são os pontos fracos e quais perigos existem.

### 1.1 Tríade CIA: Confidencialidade, Integridade e Disponibilidade

A **tríade CIA** (*Confidentiality, Integrity, Availability* — Confidencialidade, Integridade e Disponibilidade) reúne os **três objetivos principais da segurança da informação**. Toda medida de defesa protege pelo menos um deles.

| Objetivo | O que garante | Exemplo de ameaça |
| --- | --- | --- |
| Confidencialidade | Só pessoas autorizadas leem a informação | Funcionário de fora do RH (recursos humanos) abrindo a folha de pagamento |
| Integridade | A informação está completa e não foi alterada | Valor de uma transferência modificado no caminho |
| Disponibilidade | A informação e os serviços funcionam quando necessários | Servidor do site fora do ar por um ataque |

Em português, também se usa **tríade CID**.

### 1.2 Ativos, Vulnerabilidades e Ameaças

Para se preparar contra ataques, o analista identifica três elementos:

- **ativos**: tudo o que tem valor e deve ser protegido, como servidores, dispositivos e, principalmente, os **dados**;
- **vulnerabilidades**: uma fraqueza em um sistema ou no seu projeto que pode ser explorada;
- **ameaças**: qualquer perigo potencial para um ativo.

Quem explora uma vulnerabilidade é o **agente de ameaça** (também chamado de ator de ameaça): a pessoa ou o grupo por trás do ataque, como um criminoso digital, um funcionário mal-intencionado ou um grupo organizado.

O conjunto dos ativos forma a **superfície de ataque**, isto é, tudo o que pode ser atingido. Ela cresce junto com a organização, inclusive por fusões com outras empresas. Por isso, muitas organizações têm só uma ideia geral do que precisam proteger.

**Importante:** a vulnerabilidade é o **ponto fraco** (uma senha padrão nunca trocada); a ameaça é o **perigo** que se aproveita dele (alguém que tenta entrar com essa senha).

### 1.3 Gerenciamento de Ativos

O **gerenciamento de ativos** consiste em **inventariar todos os ativos e, em seguida, criar e aplicar políticas e procedimentos para protegê-los**.

A tarefa é grande: é preciso proteger usuários e recursos internos, trabalhadores móveis e serviços virtuais e na nuvem. Também é preciso saber **onde estão guardados os ativos de informação essenciais e como se chega a eles**.

Cada negócio guarda ativos diferentes, que atraem agentes de ameaça com habilidades e motivações diferentes. Exemplos:

- uma loja guarda dados de cartão de crédito;
- uma empresa de engenharia guarda projetos e softwares que interessam à concorrência;
- um banco guarda dados de clientes, de contas e outras informações financeiras.

### 1.4 Classificação de Ativos

A **classificação de ativos** distribui os recursos em **grupos com características comuns**. As informações mais importantes recebem o nível mais alto de proteção e podem exigir tratamento especial.

A empresa pode adotar um **sistema de rotulagem** de acordo com o valor, a confidencialidade e a importância das informações.

O processo ocorre em quatro etapas:

1. determinar a categoria de cada ativo: informação, software, físico ou serviço;
2. identificar o **proprietário** de cada ativo de informação e de cada software, para estabelecer a responsabilização;
3. definir os critérios: confidencialidade, valor, tempo, direitos de acesso e destruição;
4. aplicar um esquema uniforme de classificação para assegurar a proteção.

### 1.5 Padronização de Ativos

Os **padrões de ativos** definem **quais produtos de hardware e software a organização usa e dá suporte**.

Sem padronização, é difícil achar peças de reposição, e o ambiente exige mais conhecimento para ser gerenciado e custa mais em contratos de manutenção e em inventário. Com ela, a ação diante de uma falha é imediata, e o acesso e a segurança se mantêm.

### 1.6 Ciclo de Vida dos Ativos

Todo ativo passa por um **ciclo de vida**, e precisa ser protegido em todas as etapas:

Aquisição → Implantação → Utilização → Manutenção → Descarte

| Etapa | O que acontece |
| --- | --- |
| Aquisição | O ativo é comprado conforme as necessidades levantadas e entra no inventário |
| Implantação | É montado, inspecionado em busca de falhas, testado e recebe etiquetas ou códigos de barras para rastreamento |
| Utilização | Fase mais longa: o desempenho é verificado continuamente; recebe atualizações, correções (*patches*), novas licenças e auditorias de conformidade |
| Manutenção | É modificado ou atualizado para prolongar a vida produtiva |
| Descarte | Os dados são apagados, o ativo pode ser desmontado para peças, e as peças com risco ambiental seguem as regras locais |

### 1.7 Identificação de Ameaças e de Vulnerabilidades

A **identificação de ameaças** produz uma **lista das ameaças prováveis para um ambiente específico**. Ela responde a três perguntas:

- quais são as vulnerabilidades do sistema?
- quem pode explorá-las, e para chegar a quais ativos?
- quais são as consequências se as vulnerabilidades forem exploradas e os ativos forem perdidos?

A **identificação de vulnerabilidades** exige conhecer os aplicativos importantes da rede e as fraquezas deles e do hardware, o que pode exigir bastante pesquisa do administrador de rede.

#### 1.7.1 Exemplo Resolvido: Ameaças a um Sistema de Banco On-line

Para um banco pela internet, a lista de ameaças incluiria:

- invasão do sistema interno a partir dos servidores expostos à internet;
- roubo de dados de clientes;
- transações falsas, com código alterado ou com PIN e cartão roubados;
- ataque interno (*insider*), feito por um funcionário;
- erros de entrada de dados: o usuário digita dados ou pede transações incorretas;
- destruição do data center (o prédio ou a sala onde ficam os servidores) por um evento catastrófico, como incêndio ou enchente.

**Observação:** nem toda ameaça é um ataque. Erros e desastres naturais também afetam a integridade e a disponibilidade.

## 2. Defesa em Profundidade

A **defesa em profundidade** é a abordagem que **usa várias camadas de segurança na borda da rede, dentro da rede e nos dispositivos finais**. Assim, a falha de uma proteção não compromete as outras.

### 2.1 Camadas de uma Rede Protegida

Na topologia mais simples (o desenho de como os equipamentos estão ligados), o tráfego da internet atravessa três linhas de defesa até a rede interna da empresa, a **LAN** (*Local Area Network* — rede local):

Internet → Roteador de borda → Firewall → Roteador interno → Rede interna

![O tráfego da internet atravessa três linhas de defesa até chegar à rede interna](img/defesa/def_camadas.png){width=6in}

| Linha de defesa | Função |
| --- | --- |
| Roteador de borda | Primeira linha: é o roteador (equipamento que encaminha os pacotes entre redes) que liga a empresa à internet; segue regras que permitem ou negam o tráfego e repassa ao firewall o que vai para a rede interna |
| Firewall | Segunda linha: funciona como um posto de controle; faz uma filtragem adicional e acompanha o estado das conexões, isto é, lembra quem abriu cada conversa para só deixar voltar as respostas esperadas |
| Roteador interno | Aplica as regras finais de filtragem antes de encaminhar o tráfego ao destino |

O **firewall** fica entre redes e decide qual tráfego pode passar. Ele **nega conexões iniciadas na rede externa (não confiável) em direção à rede interna (confiável)**, mas deixa os usuários internos estabelecerem conexões nos dois sentidos com as redes externas. Ele também pode **autenticar usuários**, ou seja, pedir que provem quem são (com usuário e senha, por exemplo) antes de liberar o acesso. Esse recurso se chama **proxy de autenticação** e é usado para dar a usuários remotos acesso aos recursos internos.

Outras camadas comuns são:

- o **IPS** (*Intrusion Prevention System* — sistema de prevenção de intrusão), que identifica e bloqueia ataques no tráfego;
- a **AMP** (*Advanced Malware Protection*), proteção avançada da Cisco contra malware (programas maliciosos, como vírus);
- os filtros de conteúdo web e de e-mail;
- os serviços de identidade e de controle de acesso à rede, que verificam quem é cada usuário e cada aparelho antes de deixá-los entrar.

### 2.2 A Cebola e a Alcachofra da Segurança

Duas analogias descrevem a defesa em profundidade.

Na **cebola de segurança**, o atacante precisa **descascar as defesas camada por camada** até chegar aos dados, no centro.

Nas **redes sem fronteiras**, acessadas de celulares, de casa e da nuvem, vale a **alcachofra de segurança**: o atacante **não precisa remover todas as camadas, basta arrancar algumas folhas**. Exemplos de folhas: senhas, bancos de dados e aplicativos web.

Cada folha protege, mas também abre um caminho para o ataque; folha após folha, o atacante chega a mais dados, até o **coração**, onde ficam os mais confidenciais. Os sistemas voltados para a internet costumam ser bem protegidos, mas um atacante persistente acaba achando uma brecha nesse exterior e, a partir dela, vai aonde quiser.

| Característica | Cebola | Alcachofra |
| --- | --- | --- |
| Cenário | Rede com perímetro bem definido | Rede sem fronteiras |
| Caminho do atacante | Atravessar todas as camadas | Remover só algumas folhas |

**Observação:** a cebola de segurança é só uma figura de linguagem. Não tem relação com o **Security Onion**, um conjunto gratuito de ferramentas de monitoramento de rede visto no fim desta trilha.

### 2.3 Estratégias de Defesa em Profundidade

A defesa em profundidade não cria um escudo impenetrável, mas **minimiza os riscos**: mesmo que o atacante passe por uma camada, ainda encontra as outras. Ela funciona melhor com cinco estratégias:

| Estratégia | Ideia central | Exemplo |
| --- | --- | --- |
| Sobreposição (camadas) | Várias defesas seguidas | Servidor com senha, em prédio trancado e cercado |
| Limitação | Só o acesso necessário ao trabalho, com ferramentas (permissões de arquivo) e procedimentos definidos | Documentos sigilosos consultados em sala com câmeras |
| Diversidade | Camadas diferentes entre si | Crachá de um fabricante e leitor de digital de outro; algoritmos de criptografia diferentes para dados em estados diferentes |
| Ofuscação | Não revelar detalhes úteis ao atacante | Mensagem de erro sem a versão do sistema nem o tipo de equipamento |
| Simplicidade | Simples por dentro, complexo por fora | Configuração que a equipe entende e mantém; um sistema complexo mal configurado é tão fácil de invadir quanto um simples |

Na diversidade, a ideia é que a técnica que vence uma camada não vença as outras.

## 3. Gerenciamento de Operações de Segurança

O **gerenciamento de operações de segurança** reúne os processos do dia a dia que mantêm a rede segura: **controlar as configurações, registrar os eventos e observar o tráfego**.

### 3.1 Gerenciamento de Configuração

O **gerenciamento de configuração** é a **identificação, o controle e a auditoria da implantação de um sistema e de qualquer alteração feita na sua linha de base**.

A **linha de base** (*baseline*) é o conjunto de configurações que serve de **modelo para todos os sistemas semelhantes**. Exemplo: quem implanta as estações Windows instala os aplicativos necessários e define as configurações conforme um padrão documentado.

Devem ser documentados, entre outros:

- mapas de rede, diagramas de cabeamento e especificações de configuração dos aplicativos;
- convenções de nomes dos computadores;
- esquema de endereçamento IP, para rastrear os endereços (o endereço IP é o número que identifica cada equipamento na rede, como 192.168.1.10).

### 3.2 Reforço do Sistema Operacional

O **reforço** (*hardening*) do sistema operacional consiste em **configurá-lo de forma segura, reduzindo as brechas que um atacante poderia usar**. As principais medidas são:

- configurar logs (registros de eventos, explicados no próximo item) e auditoria;
- trocar nomes de conta e senhas padrão (as que vêm de fábrica, como admin/admin, que qualquer atacante conhece);
- aplicar políticas de conta, como tamanho mínimo da senha e bloqueio depois de várias tentativas erradas;
- controlar o acesso aos arquivos.

### 3.3 Arquivos de Log

Um **log** é o **registro dos eventos que ocorrem em um sistema**. Cada evento vira uma **entrada de log**, com todas as informações dele, e o conjunto delas forma o **arquivo de log**. Registros precisos e completos são essenciais. Exemplos: o log de auditoria, com as tentativas de autenticação, e o log de acesso, com os pedidos a arquivos.

Pelos logs, descobre-se **como um ataque aconteceu e se as defesas funcionaram**. Como o número de logs cresce, a empresa precisa de um **processo de gerenciamento de logs**, com procedimentos para cada etapa:

Gerar → Transmitir → Armazenar → Analisar → Descartar

| Fonte | O que registra | Para que serve |
| --- | --- | --- |
| Sistema operacional | Pedidos dos clientes e respostas dos servidores (como logins bem-sucedidos) e informações de uso (número e tamanho das transações em um período) | Acompanhar a operação do sistema |
| Software de segurança (de rede ou do sistema) | Atividades mal-intencionadas detectadas | Análise de auditoria, identificação de tendências e de problemas de longo prazo e comprovação documental da conformidade com as leis e os requisitos regulatórios |

### 3.4 Analisadores de Pacotes

Um **analisador de pacotes** (*sniffer*) **intercepta e registra o tráfego da rede**. Na rede, toda informação viaja dividida em pequenos blocos, os **pacotes**; o analisador captura cada pacote, mostra os valores dos campos (como os endereços de origem e de destino) e analisa o conteúdo, em redes com e sem fio. Exemplos: o Wireshark, com interface gráfica, e o tcpdump, usado pela linha de comando.

Ele serve para:

- registrar o tráfego;
- analisar problemas de rede;
- detectar uso indevido e tentativas de invasão;
- isolar um sistema explorado.

A mesma ferramenta ajuda o atacante: com um sniffer, ele lê tudo o que trafega sem criptografia, inclusive senhas.

## 4. Políticas, Regulamentos e Padrões

As **políticas** são regras criadas pela própria organização; os **regulamentos** são regras externas, como leis, que ela precisa cumprir. Juntos, **definem o que é permitido e o que é proibido** na rede e nos dados.

### 4.1 Políticas de Negócios

As **políticas de negócios** são diretrizes que governam as ações da organização. Na rede, elas formam uma **linha de base de uso aceitável**.

Por esse motivo, um comportamento que viola a política pode indicar que **ocorreu uma violação de segurança**.

| Política | O que define | Exemplos |
| --- | --- | --- |
| Da empresa | Regras de conduta e responsabilidades dos funcionários e dos empregadores; protegem os direitos dos funcionários e os interesses comerciais dos empregadores | Conduta dos funcionários, assiduidade, vestimenta, privacidade |
| De funcionários | Criadas e mantidas pela equipe de recursos humanos; fornecidas e assinadas na contratação | Salário, cronograma de pagamento, horário de trabalho, benefícios, férias |
| De segurança | Objetivos de segurança, regras de comportamento para usuários e administradores e requisitos do sistema, que juntos garantem a segurança da rede e dos sistemas; como o plano de continuidade, é um documento em constante evolução | Senhas, acesso remoto, uso aceitável; evoluem conforme o cenário de ameaças, as vulnerabilidades e os requisitos do negócio e dos funcionários |

### 4.2 Política de Segurança

A **política de segurança** informa a todos os requisitos para proteger os ativos de tecnologia e de informação. Ela serve de linha de base para comprar, configurar e auditar sistemas.

Seus principais benefícios são:

- dar ao pessoal de segurança o apoio da gestão;
- demonstrar o compromisso da organização com a segurança;
- definir o comportamento esperado;
- garantir a consistência nas operações, na aquisição e no uso de hardware e software;
- definir as consequências das violações.

Ela reúne políticas menores:

| Política | O que especifica |
| --- | --- |
| Identificação e autenticação | Quem acessa os recursos e como a identidade é verificada |
| Senhas | Requisitos mínimos e troca regular |
| Uso aceitável (AUP) | Usos da rede permitidos e consequências da violação |
| Acesso remoto | Como usuários remotos acessam a rede e o que fica acessível remotamente |
| Manutenção de rede | Procedimentos de atualização dos sistemas operacionais dos dispositivos de rede (o software que controla roteadores e switches) e dos aplicativos dos usuários |
| Tratamento de incidentes | Descreve como os incidentes são tratados |

### 4.3 Política de Uso Aceitável (AUP)

A **AUP** (*Acceptable Use Policy* — Política de Uso Aceitável) define **o que os usuários podem ou não fazer nos sistemas**. Também é chamada de **política de uso apropriado**. Ela deve ser o mais explícita possível, para evitar mal-entendidos. Exemplo: listar os sites, fóruns ou aplicativos que consomem muita largura de banda (a capacidade de transmissão da conexão) e que não podem ser acessados pela rede da empresa.

Todo funcionário assina a AUP, e a cópia assinada é guardada durante todo o emprego.

### 4.4 Políticas de BYOD

O **BYOD** (*Bring Your Own Device* — Traga seu Próprio Dispositivo) permite que os funcionários usem **seus próprios aparelhos para acessar sistemas, redes e informações da empresa**.

Ele traz produtividade, mobilidade, menos custos operacionais e de TI (tecnologia da informação) e mais atração na hora de contratar e reter funcionários, mas aumenta o risco de **vazamento de dados**. Por isso, a política de BYOD define:

- os objetivos do programa BYOD;
- quem pode trazer dispositivos e quais são aceitos;
- o nível de acesso dos dispositivos pessoais;
- o que a equipe de segurança pode fazer no aparelho;
- as medidas de proteção a aplicar se um dispositivo for comprometido.

| Práticas recomendadas | O que fazer |
| --- | --- |
| Acesso protegido por senha | Usar uma senha diferente para cada dispositivo e conta |
| Controle manualmente a conectividade sem fio | Desligar o Wi-Fi e o Bluetooth quando não estiverem em uso e conectar-se apenas a redes confiáveis |
| Mantenha-se atualizado | Manter o sistema e os aplicativos atualizados, porque as atualizações trazem correções contra as ameaças mais recentes |
| Dados de backup | Ativar o backup para o caso de perda ou roubo |
| Ativar "localizar meu dispositivo" | Usar um serviço de localização do dispositivo com apagamento remoto, que apaga os dados à distância se o aparelho for roubado |
| Forneça software antivírus | Instalar antivírus nos dispositivos BYOD aprovados |

O **MDM** (*Mobile Device Management* — Gerenciamento de Dispositivos Móveis) permite à TI **aplicar configurações de segurança e de software em todos os dispositivos que se conectam à rede da empresa**.

### 4.5 Conformidade com Regulamentos e Padrões

Há também regulamentos externos ligados à segurança da rede. Os profissionais da área precisam conhecer as leis e os códigos de ética que se aplicam aos profissionais de **INFOSEC** (*Information Systems Security* — Segurança de Sistemas de Informação).

Os **regulamentos de conformidade** definem **pelo que a organização é responsável e quais são as consequências se ela não cumprir**. Eles variam conforme o tipo de organização e de dado. No Brasil, por exemplo, quem trata dados pessoais segue a LGPD (Lei Geral de Proteção de Dados).

## 5. Criptografia e Confidencialidade

A **criptografia** é a ciência de criar e quebrar códigos. Ela **embaralha os dados para que só quem conhece o segredo certo consiga lê-los** e é a principal ferramenta da confidencialidade.

### 5.1 Conceitos Básicos de Criptografia

Os dados legíveis são o **texto claro** (ou texto simples); criptografados, viram **texto cifrado**, uma mensagem ilegível e disfarçada. O caminho de volta é a **descriptografia**.

Texto claro → Criptografia → Texto cifrado → Descriptografia → Texto claro

![A chave transforma o texto claro em texto cifrado e, do outro lado, o texto cifrado de volta em texto claro](img/defesa/def_cripto.png){width=6in}

A **chave** é o valor secreto que o algoritmo usa nas duas operações. **Quem tem a chave consegue descriptografar o texto cifrado**. Quanto maior a chave, mais tempo alguém leva para descobri-la por tentativa.

Existem duas classes de criptografia, que diferem na maneira de usar as chaves:

- **simétrica**: a mesma chave criptografa e descriptografa;
- **assimétrica**: um par de chaves diferentes, uma para cada operação.

### 5.2 Estados dos Dados

Os dados precisam de proteção em **três estados**:

| Estado | Situação | Exemplo |
| --- | --- | --- |
| Em repouso (inativos) | Armazenados, sem nenhum usuário ou processo acessando, pedindo ou alterando | Disco do computador ou servidor central da empresa |
| Em trânsito | Sendo transmitidos: entre as peças do próprio computador (pelos barramentos, as "vias" da placa-mãe), dentro de uma rede ou entre redes, pela internet | Mensagem viajando pela internet |
| Em processamento | Na entrada, na modificação, no cálculo ou na saída | Planilha aberta sendo editada |

Todo dado que não está em trânsito nem em processamento está em repouso.

### 5.3 Criptografia Simétrica

Na **criptografia simétrica**, **as duas partes usam a mesma chave**, chamada de **chave pré-compartilhada** ou **chave secreta**. Ela precisa ser conhecida pelo remetente e pelo receptor **antes** da comunicação.

É como um cadeado com duas cópias da chave: Alice tranca a caixa, e só Bob, com a outra cópia, abre.

Os algoritmos simétricos usam **menos processamento** do processador (a CPU, o "cérebro" do computador) que os assimétricos. Por isso são rápidos e usados para **grandes volumes de dados**, como o tráfego de uma **VPN** (*Virtual Private Network* — rede privada virtual, que cria um túnel protegido pela internet entre dois pontos). O tamanho da chave é medido em **bits** (cada bit é um 0 ou um 1): as chaves simétricas têm de 40 a 256 bits, e para ser segura a chave deve ter **no mínimo 128 bits**.

Os algoritmos simétricos funcionam de duas formas:

- **cifra de bloco**: divide os dados em pedaços de tamanho fixo e transforma cada pedaço em um bloco cifrado de 64 ou 128 bits; exemplos: DES (bloco de 64 bits) e AES (bloco de 128 bits), descritos na tabela abaixo;
- **cifra de fluxo**: criptografa um byte (8 bits) ou um bit de cada vez, de forma contínua, e por isso costuma ser mais rápida; exemplos: o RC4 e o A5, usado na antiga telefonia celular GSM (a rede 2G).

| Algoritmo | Características | Situação |
| --- | --- | --- |
| DES (*Data Encryption Standard*) | Padrão antigo dos anos 1970; chave de só 56 bits, curta demais para os computadores de hoje | Inseguro, não usar |
| 3DES (*Triple DES*) | Substituto do DES; repete o DES três vezes | Evitar (aposentadoria prevista para 2023); se usar, trocar as chaves com frequência |
| AES (*Advanced Encryption Standard*) | Bloco de 128 bits; chaves de 128, 192 ou 256 bits; adotado pelo governo dos EUA e usado no Wi-Fi, nas VPNs e na criptografia de discos | Popular e recomendado |
| SEAL (*Software-Optimized Encryption Algorithm*) | Cifra de fluxo, chave de 160 bits, menor impacto na CPU | Alternativa mais rápida ao AES |
| Série RC (*Rivest ciphers*) | Criada pelo criptógrafo Ron Rivest; o RC4 é uma cifra de fluxo que já protegeu o tráfego dos sites e o Wi-Fi antigo | RC4 vulnerável, não usar |

**Observação:** no AES, só o tamanho da **chave** varia; o **bloco** é sempre de 128 bits.

### 5.4 Criptografia Assimétrica

Na **criptografia assimétrica**, ou **de chave pública**, cada um tem **um par de chaves**: a **pública**, que pode ser divulgada, e a **privada**, que só o dono conhece.

As duas se completam: **o que uma chave criptografa, só a outra do mesmo par descriptografa**. Funciona como uma caixa de correio: qualquer pessoa pode pôr uma carta pela fenda (a chave pública), mas só o dono, com a chave da portinhola (a privada), consegue tirá-la.

A privada não pode ser calculada a partir da pública. Isso porque esses algoritmos se baseiam em contas fáceis de fazer em um sentido e quase impossíveis de desfazer, como **descobrir quais números primos foram multiplicados** para gerar um número enorme (a fatoração) ou descobrir a qual potência um número foi elevado (o logaritmo discreto).

Como as partes não têm um segredo compartilhado, as chaves precisam ser **muito longas**, de 512 a 4.096 bits; hoje, **2.048 bits ou mais** são confiáveis, e 1.024 ou menos são insuficientes. Por isso esses algoritmos são **lentos** e ficam com tarefas de pouco volume: **troca de chaves e assinaturas digitais**. Em compensação, o gerenciamento das chaves é mais simples, porque uma delas pode ser pública.

Os **protocolos** (conjuntos de regras que os equipamentos seguem para conversar) que usam criptografia assimétrica são, em geral, os que precisam combinar uma chave com um desconhecido ou provar a identidade de alguém. Os principais são:

- **SSL** (*Secure Sockets Layer*) e seu sucessor, o **TLS** (*Transport Layer Security*): protegem a comunicação entre o navegador e o site. São eles que fazem o **cadeado** aparecer no navegador e o endereço começar com **https**. O SSL é a versão antiga, hoje considerada insegura; o que se usa de fato é o TLS, embora muita gente ainda diga "SSL";
- **SSH** (*Secure Shell*): permite **acessar e administrar à distância** um servidor ou um equipamento de rede (roteador, switch), digitando comandos como se estivesse na frente dele, com tudo criptografado. Substitui o Telnet, que enviava tudo, inclusive a senha, sem proteção;
- **IKE** (*Internet Key Exchange*): é a parte que **negocia e troca as chaves** nas VPNs **IPsec** (*IP Security*), o conjunto de protocolos que cria túneis seguros entre redes, por exemplo entre a matriz e uma filial;
- **PGP** (*Pretty Good Privacy*): criptografa e assina **e-mails e arquivos**, garantindo que só o destinatário leia e que a mensagem venha mesmo do remetente.

Os algoritmos assimétricos mais conhecidos são:

| Algoritmo | Tamanho de chave (bits) | Características |
| --- | --- | --- |
| Diffie-Hellman (DH), nome dos seus criadores | 512, 1.024, 2.048, 3.072 e 4.096 | Não criptografa mensagens: serve para **duas partes combinarem uma chave secreta** pela internet sem enviá-la (explicado no item 5.6); a segurança vem de que é fácil elevar um número a uma potência, mas difícil descobrir qual potência foi usada |
| DSS (*Digital Signature Standard*) e DSA (*Digital Signature Algorithm*) | 512 a 1.024 | O DSS é o padrão do governo dos EUA para **assinaturas digitais** (a "assinatura" eletrônica que prova quem enviou um documento, vista na seção 7), e o DSA é o algoritmo que ele define; baseado no ElGamal (abaixo); assina na mesma velocidade do RSA, mas verifica de 10 a 40 vezes mais devagar |
| RSA (iniciais de Rivest, Shamir e Adleman, seus criadores) | 512 a 2.048 | Baseado na dificuldade de fatorar números grandes; o primeiro que serve tanto para assinatura quanto para criptografia; muito usado no comércio eletrônico e nos certificados dos sites |
| ElGamal (nome do criador) | 512 a 1.024 | Derivado do Diffie-Hellman; a mensagem cifrada fica com o dobro do tamanho, por isso só serve para mensagens pequenas, como chaves |
| Curvas elípticas (ECC, *Elliptic Curve Cryptography*) | 224 ou mais | Usa uma matemática diferente (curvas elípticas) para adaptar algoritmos como DH e ElGamal; vantagem: **chaves muito menores com a mesma segurança**, o que poupa bateria e processamento em celulares |

### 5.5 Confidencialidade e Autenticação com Chaves Assimétricas

O resultado depende da chave usada para criptografar:

- chave **pública** do destinatário → só ele lê → **confidencialidade**, sem precisar combinar uma senha antes;
- chave **privada** do remetente → só ele poderia ter enviado → **autenticação**; como a chave pública não é sigilosa, qualquer um consegue ler.

![A chave usada para criptografar define o resultado: a pública do destinatário dá confidencialidade; a privada do remetente, autenticação](img/defesa/def_assim.png){width=6in}

#### 5.5.1 Exemplo Resolvido: Alice Envia uma Mensagem Sigilosa a Bob

1. Alice pede e recebe a chave pública de Bob;
2. Alice criptografa a mensagem com essa chave, usando um algoritmo combinado, e a envia;
3. Bob descriptografa com a própria chave privada; só ele consegue ler.

Se uma chave privada for comprometida, é preciso gerar outro par para substituí-la.

#### 5.5.2 Exemplo Resolvido: Bob Confere que a Mensagem Veio de Alice

1. Alice criptografa a mensagem com a própria chave privada e a envia;
2. Bob pede a chave pública de Alice;
3. Bob descriptografa com essa chave; se der certo, a mensagem só pode ter vindo de Alice.

#### 5.5.3 Exemplo Resolvido: Confidencialidade, Integridade e Autenticação Juntas

1. Alice criptografa a mensagem com a chave **pública de Bob** (confidencialidade);
2. Alice calcula um **hash** da mensagem (um resumo dela, explicado logo abaixo) e o criptografa com a própria chave **privada** (autenticação e integridade); depois envia os dois;
3. Bob descriptografa o hash com a chave pública de Alice e o compara com o hash que ele mesmo calcula; se forem iguais, a mensagem não foi alterada e veio de Alice;
4. Bob descriptografa a mensagem com a própria chave privada.

O **hash** é um resumo de tamanho fixo calculado a partir dos dados, que muda se qualquer parte deles mudar.

### 5.6 Diffie-Hellman

O **Diffie-Hellman (DH)** permite que **dois computadores gerem o mesmo segredo compartilhado sem nunca terem se comunicado antes**. A nova chave **nunca é trocada** entre eles: cada lado a calcula sozinho. Ela depois é usada por um algoritmo simétrico, como o AES. Usos comuns: as **VPNs IPsec** e o **SSH**, descritos no item 5.4.

#### 5.6.1 Exemplo Resolvido: a Analogia das Cores

1. Alice e Bob combinam uma cor pública: amarelo;
2. cada um escolhe uma cor secreta, que nunca é compartilhada: Alice, vermelho; Bob, azul;
3. cada um mistura o amarelo com a sua cor e envia o resultado: Alice envia laranja; Bob, verde;
4. cada um mistura a cor recebida com a própria cor secreta;
5. os dois chegam ao mesmo marrom, que é a chave compartilhada.

Quem intercepta só vê amarelo, laranja e verde, e não chega ao marrom.

A segurança do DH vem dos **números enormes** usados nos cálculos: um número DH de 1.024 bits tem cerca de **309 dígitos decimais** (um bilhão tem só 10). A força é definida pelo **grupo DH**, um número que indica o tamanho dos valores usados: quanto maior, **mais seguro e mais lento** para calcular a chave. Grupos aceitos pelo Cisco IOS, o sistema operacional dos roteadores e switches da Cisco:

| Grupo DH | Tamanho |
| --- | --- |
| 1, 2 e 5 | 768, 1.024 e 1.536 bits |
| 14, 15 e 16 | 2.048, 3.072 e 4.096 bits |
| 19, 20 e 24 | Curvas elípticas |

### 5.7 Resumo de Criptografia Simétrica e Assimétrica

| Característica | Simétrica | Assimétrica |
| --- | --- | --- |
| Chaves | A mesma nas duas operações | Par: pública e privada |
| Tamanho da chave | 40 a 256 bits | 512 a 4.096 bits |
| Velocidade | Rápida | Lenta |
| Uso típico | Grandes volumes, como VPN | Troca de chaves e assinaturas |
| Exemplos | AES, SEAL, 3DES | RSA, DH, DSA, ElGamal, ECC |

As duas trabalham juntas. Os sistemas assimétricos são lentos demais para criptografia em massa. Por isso, o **DH cria as chaves, e um algoritmo simétrico (como o AES ou o 3DES) criptografa o grande volume de dados**.

## 6. Hash, Integridade e Autenticidade

A criptografia impede a leitura dos dados, mas não garante que eles chegaram sem alteração nem quem os enviou. Para isso existem o **hash** e o **HMAC**.

### 6.1 Elementos das Comunicações Seguras

As organizações precisam proteger os dados que viajam pelos links (as conexões entre redes), principalmente os que saem para filiais, trabalho remoto e parceiros. A criptografia pode ser usada em praticamente qualquer comunicação, e **a tendência é que toda comunicação seja criptografada**. As comunicações seguras se apoiam em **quatro elementos**:

| Elemento | O que garante | Como é obtido |
| --- | --- | --- |
| Integridade dos dados | A mensagem não foi alterada; qualquer alteração em trânsito é detectada | Hash, com algoritmos como SHA-2 ou SHA-3; o MD5 ainda é muito usado, mas é inseguro (todos explicados nos itens 6.2 e 6.3) |
| Autenticação de origem | A mensagem não é falsificada e vem de quem diz ter enviado | HMAC, um hash calculado com uma chave secreta (ver item 6.6) |
| Confidencialidade | Só autorizados leem; se interceptada, a mensagem não é decifrada em tempo razoável | Criptografia simétrica e assimétrica |
| Não repúdio | O remetente não pode negar o envio, porque só ele tem a característica ou a assinatura exclusiva | Assinatura digital |

### 6.2 Funções Hash

Uma **função hash** recebe dados de qualquer tamanho e produz uma **representação de tamanho fixo**, chamada de **hash** (ou *digest*).

Ela é **unidirecional**: calcular o hash é fácil, mas voltar aos dados é praticamente impossível. É como moer café: ninguém reconstrói os grãos a partir do pó.

Suas características são:

- a entrada pode ter qualquer tamanho, e a saída tem sempre o mesmo;
- o cálculo é rápido;
- não pode ser revertida;
- duas entradas diferentes **praticamente nunca geram o mesmo hash**.

Por esse motivo, **qualquer alteração nos dados, por menor que seja, muda o hash**. Os hashes funcionam como **impressões digitais** dos dados e também servem para detectar arquivos duplicados e mudanças de versão.

### 6.3 Algoritmos de Hash

| Algoritmo | Tamanho do hash | Situação |
| --- | --- | --- |
| MD5 (*Message Digest 5*) | 128 bits | Criado por Ron Rivest; legado e inseguro; só usar sem alternativa melhor |
| SHA-1 | 160 bits | Criado pela NSA (*National Security Agency*, a agência de segurança nacional dos EUA) e publicado pelo NIST nos anos 1990; um pouco mais lento que o MD5; com falhas conhecidas |
| SHA-2 | SHA-224, SHA-256, SHA-384 e SHA-512 | Criado pela NSA; preferir SHA-256, SHA-384 e SHA-512 |
| SHA-3 | SHA3-224, SHA3-256, SHA3-384 e SHA3-512 | O mais novo, do NIST, para substituir o SHA-2; usar sempre que possível |

A sigla **SHA** significa *Secure Hash Algorithm*. O **NIST** (*National Institute of Standards and Technology*, instituto de padrões dos EUA) o especificou no padrão de hash seguro (SHS).

### 6.4 Verificação de Integridade com Hash

A verificação compara o hash calculado antes e depois da transmissão:

1. o remetente calcula o hash da mensagem e o envia junto;
2. o destinatário calcula de novo o hash da mensagem recebida;
3. hashes iguais → mensagem intacta; hashes diferentes → mensagem alterada.

Exemplo: “Pagar a Alex US$ 100” gera um hash. Se a mensagem virar “Pagar a Jeremy US$ 1.000” no caminho, o hash muda e a mensagem é descartada.

Usos comuns:

- **downloads**: comparar o hash publicado pelo fabricante com o do arquivo baixado; a Cisco, por exemplo, publica os hashes (também chamados de *checksums*) MD5 e SHA dos arquivos do IOS, para que se confira se o sistema instalado no equipamento é original;
- **perícia forense**: o perito faz uma **cópia bit a bit** (clone) da mídia e compara o hash dela com o da original. Hashes iguais provam a **invariabilidade**: os dados não foram corrompidos nem alterados. O perito então examina a cópia e deixa o original intacto.

### 6.5 Limitação do Hash

O hash detecta alterações acidentais, mas **não protege contra alterações deliberadas**: ele não traz nenhuma identificação do remetente, e qualquer pessoa com a função certa consegue calculá-lo.

Um atacante no meio do caminho pode alterar a mensagem, calcular um novo hash e anexá-lo; o receptor só confere o hash que veio junto. Esse é o **ataque *man-in-the-middle* (MitM)**, em que o criminoso se coloca entre as duas partes.

### 6.6 HMAC

O **HMAC** (*Hash-based Message Authentication Code*) é um hash calculado **a partir da mensagem e de uma chave secreta que só o remetente e o destinatário conhecem**.

Sem a chave, o atacante não gera um HMAC válido. Por isso, o HMAC garante a **integridade e a autenticação da origem**.

1. o remetente calcula o HMAC da mensagem com a chave e o envia junto;
2. o destinatário calcula o HMAC com a mesma chave;
3. valores iguais → mensagem íntegra e de origem confiável.

Existem outros métodos de **MAC** (*Message Authentication Code* — código de autenticação de mensagem; não confundir com o endereço MAC das placas de rede), mas o HMAC é o usado no SSL/TLS (ver item 5.4), no IPsec, no SSH e na autenticação entre roteadores que usam o **OSPF** (*Open Shortest Path First*, um protocolo com que os roteadores trocam informações sobre os caminhos da rede).

O HMAC também autentica usuários da web. Muitos serviços usam a **autenticação básica** do HTTP (o protocolo das páginas web), que **não criptografa** o usuário e a senha. Com o HMAC, o usuário envia um identificador e um HMAC calculado com a chave privada dele; o servidor busca essa chave, calcula o HMAC e confere se os dois batem. As VPNs IPsec usam o HMAC para autenticar a origem de cada pacote e conferir a integridade.

Resumindo, as funções hash servem para:

- provar a **autenticidade**, com uma chave secreta simétrica, no IPsec e na autenticação de protocolos de roteamento (os roteadores Cisco IOS fazem isso);
- gerar respostas únicas e unidirecionais a **desafios** nos protocolos de autenticação;
- provar a **integridade**, como nos contratos assinados digitalmente e nos certificados digitais da PKI (a infraestrutura de chave pública, vista na seção 7).

Ao escolher um algoritmo de hash, use o **SHA-256 ou superior** e evite o SHA-1 e o MD5.

#### 6.6.1 Exemplo Resolvido: HMAC entre Roteadores OSPF

O roteador R1 avisa o roteador vizinho R2 sobre um caminho para a rede 10.2.0.0/16, enviando uma atualização de estado do link (**LSU**, *Link-State Update*, a mensagem do OSPF que informa as rotas):

1. R1 calcula o hash da LSU com a chave secreta;
2. R1 envia o hash junto com a LSU;
3. R2 calcula o hash da LSU com a mesma chave; se os valores baterem, aceita a atualização; se não, a descarta.

| Característica | Hash | HMAC |
| --- | --- | --- |
| Entrada | Só a mensagem | Mensagem + chave secreta |
| Quem calcula | Qualquer pessoa | Só quem tem a chave |
| Resiste ao man-in-the-middle | Não | Sim |

### 6.7 Hash de Senhas

Os sistemas não guardam as senhas: **guardam apenas o hash da senha**. No login, comparam o hash da senha digitada com o guardado. Assim, a senha fica protegida e ainda pode ser verificada.

Quem rouba os hashes precisa adivinhar as senhas, por dois ataques:

- **dicionário**: compara os hashes roubados com os de um arquivo de palavras, frases e senhas comuns; cada hash que bate revela uma senha;
- **força bruta**: testa todas as combinações; consome muito tempo e processamento e, em teoria, sempre acaba achando a senha, por isso a senha precisa ser longa o bastante para o ataque não valer a pena.

O **alongamento de chave** (*key stretching*) deixa cada tentativa muito lenta, o que reduz a eficácia de equipamentos capazes de calcular bilhões de hashes por segundo.

#### 6.7.1 Salt

O **salt** é uma **sequência aleatória acrescentada à senha antes do cálculo do hash**. Assim, senhas iguais geram hashes diferentes.

O salt é guardado junto com o hash e não precisa ser secreto. As boas práticas são:

- um salt exclusivo para cada senha, nunca reutilizado;
- salt do mesmo tamanho da saída da função hash;
- gerado por um **CSPRNG** (*Cryptographically Secure Pseudo-Random Number Generator* — gerador de números aleatórios seguro para criptografia), que produz números imprevisíveis;
- hash calculado sempre no servidor, nos aplicativos web.

Para **guardar** a senha: gerar um salt longo com o CSPRNG → colocá-lo no começo da senha → calcular o hash (SHA-256) → salvar o salt e o hash no registro do usuário.

Para **validar** a senha: buscar o salt e o hash do usuário → juntar o salt à senha digitada e calcular o hash com a mesma função → comparar com o hash guardado; se forem diferentes, a senha está errada.

O salt impede o ataque de dicionário e inutiliza as tabelas que os atacantes preparam com antecedência:

| Tabela | Como funciona |
| --- | --- |
| Tabela de pesquisa | Hashes pré-calculados de um dicionário, com a senha de cada um; processa centenas de pesquisas por segundo |
| Tabela de pesquisa reversa | Liga cada hash roubado a todos os usuários que o usam, para atacar vários hashes sem tabela pré-calculada |
| Tabela rainbow | Sacrifica a velocidade para ocupar menos espaço e guardar soluções para mais hashes |

## 7. Assinaturas Digitais e Infraestrutura de Chave Pública (PKI)

A **assinatura digital** combina o hash (ver item 6.2) e a criptografia assimétrica para provar quem enviou uma mensagem. Para confiar nas chaves públicas usadas nessa prova, existe a **PKI**.

### 7.1 Assinatura Digital

A **assinatura digital** é uma técnica matemática que garante **autenticidade, integridade e não repúdio**. O **não repúdio** significa que quem assinou não pode depois negar que assinou. Ela vale como **prova legal** de que a troca de dados ocorreu.

Suas características são:

- autêntica: não pode ser falsificada e prova que o signatário, e ninguém mais, assinou;
- inalterável: o documento assinado não pode ser modificado;
- não reutilizável: não pode ser transferida para outro documento;
- não repudiável: o documento assinado vale como um documento físico, e o signatário não pode negar a assinatura.

Os dois usos mais comuns são a **assinatura de código** (ver item 7.3) e os **certificados digitais** (ver item 7.4), uma espécie de carteira de identidade virtual que prova quem é um site ou um sistema e permite abrir uma conexão criptografada com ele.

O padrão **DSS** (*Digital Signature Standard*), já citado no item 5.4, admite três algoritmos:

- **DSA**: o padrão original, com chaves de 512 a 1.024 bits;
- **RSA** (ver item 5.4): assimétrico, muito usado para gerar e verificar assinaturas;
- **ECDSA** (*Elliptic Curve DSA*): variante mais recente do DSA, com curvas elípticas (ECC); mais eficiente, com assinaturas menores e menos dados trafegando na rede.

Nos anos 1990, a empresa RSA Security começou a publicar os **PKCS** (*Public-Key Cryptography Standards*), padrões de criptografia de chave pública. Eram 15, um deles retirado. Não são padrões oficiais do setor, mas são bem reconhecidos e passaram a interessar a organizações como a **IETF** (*Internet Engineering Task Force*), a entidade que publica os padrões técnicos da internet.

### 7.2 Como a Assinatura É Criada e Verificada

A assinatura usa a chave **privada** do remetente para assinar e a chave **pública** dele para conferir.

#### 7.2.1 Exemplo Resolvido: Bob Confirma um Pedido de Alice

Bob confirma um pedido de Alice. Para assinar:

1. o computador de Bob calcula o hash da confirmação;
2. criptografa o hash com a própria chave privada: essa é a assinatura;
3. envia o documento com a assinatura.

Para verificar:

1. Alice descriptografa a assinatura com a chave pública de Bob e recupera o hash enviado;
2. calcula o hash do documento recebido;
3. hashes iguais → a confirmação foi enviada por Bob e não mudou desde que foi assinada.

![Bob assina com a própria chave privada; Alice confere com a chave pública de Bob e compara os hashes](img/defesa/def_assinatura.png){width=6in}

**Importante:** o que se criptografa na assinatura é o **hash** do documento. Por isso, a assinatura não dá confidencialidade: o documento continua legível.

### 7.3 Assinatura de Código

A **assinatura de código** aplica a assinatura digital a programas: o executável vem em um **envelope assinado digitalmente**, e o usuário confere a assinatura antes de instalar. Ela garante que:

- o código veio realmente da editora;
- não foi modificado desde a publicação;
- a editora não pode negar que o publicou;
- nenhum código malicioso foi inserido por terceiros.

O padrão **FIPS 140-3** (*Federal Information Processing Standard*, norma de segurança do governo dos EUA para módulos de criptografia) exige que o software disponível para download seja assinado e verificado digitalmente.

No Windows, nas propriedades de um programa baixado (botão direito → Propriedades), a aba Assinaturas Digitais mostra quem assinou (por exemplo, a Cisco Systems Inc.), o algoritmo do *digest*, isto é, do hash (por exemplo, sha256), e a data da assinatura.

### 7.4 Certificados Digitais

Um **certificado digital** funciona como um **passaporte eletrônico**: ele **associa uma chave pública a uma identidade confirmada**, de um site, de uma pessoa ou de uma organização. Ele informa para quem foi emitido, quem o emitiu e até quando vale. Serve para **autenticar quem envia** uma mensagem e também para dar ao receptor um meio de **criptografar a resposta**.

**Importante:** o **certificado verifica a identidade**; a **assinatura verifica que algo veio dessa identidade**.

### 7.5 Infraestrutura de Chave Pública (PKI)

Ao abrir uma conexão assimétrica, dois hosts trocam suas chaves públicas. Para confiar nelas, um **terceiro confiável** precisa confirmar a quem pertencem, como o órgão que emite a carteira de motorista: ele faz uma investigação aprofundada e emite credenciais difíceis de falsificar, que todos os que confiam nele aceitam.

Na prática, para um site usar HTTPS (o SSL/TLS do item 5.4), o dono obtém um certificado para o seu domínio (o nome do site, como exemplo.com.br) junto a um provedor de certificados. Quando alguém acessa o site, o navegador recebe esse certificado, e a chave pública do site, que vem nele, protege as comunicações seguintes.

A **PKI** (*Public Key Infrastructure* — Infraestrutura de Chave Pública) é o conjunto de especificações, hardware, software, pessoas, políticas e procedimentos que **criam, gerenciam, distribuem, armazenam e revogam certificados digitais**. Ela permite distribuir e identificar chaves públicas em grande escala, com uma relação de confiança muito escalável, e foi projetada para proteger identidades digitais até de atacantes sofisticados e de Estados.

A **autoridade de certificação** (**CA**, *Certificate Authority*) é quem **emite os certificados, vinculando uma chave pública a uma identidade confirmada**. Ela os assina com a própria chave privada. Exemplos: IdenTrust, DigiCert, Sectigo, GlobalSign, GoDaddy e Let's Encrypt, sem fins lucrativos e gratuita.

Nem todo certificado vem diretamente de uma CA pública: fornecedores oferecem servidores de CA como serviço, e a organização pode montar uma **PKI privada** com o Windows Server ou com o OpenSSL (programa gratuito de criptografia). Nesse caso, a empresa é a própria CA e pode autenticar os funcionários que acessam a rede.

| Elemento | Função |
| --- | --- |
| Certificado | Chave pública, finalidade, CA emissora, período de validade e algoritmo da assinatura |
| Armazenamento de certificados | Guarda certificados e chaves privadas no computador |
| CA | Verifica a identidade e emite os certificados |
| Banco de dados de certificados | Guarda os certificados aprovados |

De forma simplificada:

1. Bob pede um certificado à CA, que confirma sua identidade e o emite;
2. Bob apresenta o certificado a Alice;
3. Alice confere com a chave pública da CA que o certificado é válido.

![A CA confirma a identidade de Bob e emite o certificado; Alice confia nele porque confere a assinatura da CA](img/defesa/def_pki.png){width=6in}

A **autoridade de registro** (**RA**, *Registration Authority*) confere a identidade de quem pede o certificado e encaminha o pedido; quem emite é sempre uma CA.

### 7.6 Classes de Certificados

As CAs, principalmente as terceirizadas, emitem certificados em classes. O número depende do **rigor da verificação de identidade** na emissão: **quanto maior a classe, mais confiável o certificado**.

| Classe | Uso |
| --- | --- |
| 0 | Testes, sem nenhuma verificação |
| 1 | Pessoas, com verificação de e-mail |
| 2 | Organizações que precisam provar a identidade |
| 3 | Servidores e assinatura de software, com verificação independente da identidade e da autoridade |
| 4 | Transações comerciais on-line entre empresas |
| 5 | Organizações privadas e segurança do governo |

Na classe 1, basta responder a um e-mail, o que é uma autenticação fraca. Nas classes 3 e 4, o titular comparece **pessoalmente com pelo menos dois documentos oficiais** de identificação.

Os navegadores já trazem a lista de **autoridades de certificação raiz confiáveis**, as CAs do topo, em quem todos confiam (ver item 7.7).

### 7.7 Topologias de PKI

| Topologia | Como funciona | Vantagem | Desvantagem |
| --- | --- | --- | --- |
| Raiz única | Uma CA emite todos os certificados | Simplicidade | Ponto único de falha |
| Certificação cruzada | CAs do mesmo nível confiam umas nas outras | Sem ponto único de falha | Muitas relações para gerenciar |
| Hierárquica | A CA raiz (a do topo) certifica CAs subordinadas, que emitem os certificados finais | Escala bem | Cadeia difícil de rastrear |
| Híbrida | Hierarquias que se certificam entre si | Une comunidades diferentes | Mais complexa |

O **ponto único de falha** é qualquer componente cuja falha derruba o sistema inteiro. Em redes maiores, as CAs se ligam por duas arquiteturas básicas: certificação cruzada e hierárquica. A híbrida serve, por exemplo, quando duas comunidades hierárquicas querem que seus membros confiem uns nos outros.

A interoperabilidade é um problema, porque muitos fornecedores criaram soluções próprias para a PKI e seus serviços de diretório, como o **LDAP** (*Lightweight Directory Access Protocol*) e o **X.500**, usados para consultar um diretório (um cadastro central de usuários e equipamentos, como o Active Directory da Microsoft) e conferir usuário e senha. Para resolver isso, a IETF publicou a RFC 2527 (os padrões da internet são publicados em documentos numerados chamados RFC, *Request for Comments*), um modelo de políticas para a PKI X.509.

### 7.8 Padrão X.509

O padrão **X.509 versão 3**, do **ITU-T** (o setor de telecomunicações da União Internacional de Telecomunicações, órgão da ONU), define o **formato dos certificados digitais**: que campos o certificado tem e em que ordem. Ele é usado em:

- **SSL/TLS**: os servidores web autenticam o site, e os navegadores usam certificados de cliente no HTTPS; é a autenticação por certificado mais usada;
- **IPsec**: VPNs em que os equipamentos provam a identidade com certificados RSA durante a troca de chaves (IKE);
- **S/MIME** (*Secure/Multipurpose Internet Mail Extensions*): padrão que programas de e-mail usam para assinar e criptografar as mensagens;
- **EAP-TLS**: método de autenticação do padrão **802.1X**, em que o switch só libera a porta da rede depois que o dispositivo conectado prova a identidade com um certificado; o switch repassa essa verificação a um servidor central de autenticação (na Cisco, o ACS, *Access Control Server*).

### 7.9 Inscrição e Revogação de Certificados

O primeiro passo é obter com segurança a chave pública da CA, o **certificado autoassinado**, que verifica todos os certificados que ela emite. **Só uma CA raiz** pode emitir um certificado autoassinado reconhecido pelas outras CAs. Nos navegadores, os certificados raiz públicos já vêm instalados.

Na **inscrição**, o host pede à CA um certificado de identidade para si e obtém o certificado da CA pela própria rede (**em banda**). A autenticidade do certificado da CA é conferida **fora de banda**, isto é, por outro canal, por exemplo por telefone, comparando a **impressão digital** do certificado (o hash dele, uma sequência que o identifica de forma única). Depois disso, a CA não precisa mais estar presente: os usuários trocam diretamente seus certificados com as chaves públicas.

Um certificado pode ser **revogado**, por exemplo quando a chave é comprometida ou quando ele não é mais necessário:

| Método | Como funciona |
| --- | --- |
| CRL (*Certificate Revocation List*) | Lista dos números de série dos certificados revogados; as entidades da PKI consultam o repositório regularmente |
| OCSP (*Online Certificate Status Protocol*) | Consulta a um servidor OCSP sobre um certificado X.509; as revogações vão imediatamente para um banco de dados on-line |

### 7.10 Aplicações da PKI

A PKI está em:

- autenticação entre pontos com certificados SSL/TLS e tráfego web HTTPS;
- VPNs IPsec;
- controle de acesso à rede com 802.1X (padrão em que o dispositivo só usa a porta da rede depois de autenticado);
- e-mail seguro (S/MIME) e mensagens instantâneas seguras;
- assinatura de código, para aprovar e autorizar aplicativos;
- **EFS** (*Encrypting File System*), que criptografa os arquivos do usuário;
- autenticação de dois fatores com cartões inteligentes (*smart cards*, cartões com chip que guardam o certificado do usuário);
- proteção de dispositivos de armazenamento USB.

O navegador mostra um aviso de segurança em dois casos:

- **validade**: o certificado X.509v3 traz datas de "não antes" e "não depois"; um certificado vencido pode ser só descuido do administrador ou algo mais grave;
- **erro de validação da assinatura**: sem validar a assinatura, não há garantia de que a chave pública é autêntica; isso acontece quando o certificado raiz da CA não está no armazenamento do navegador.

O SSL/TLS é modular: o **conjunto de cifras** (*cipher suite*) reúne o algoritmo de MAC (o HMAC (ver item 6.6) do item 6.6), o de criptografia (como o AES), o de troca de chaves (como o DH) e o de autenticação (como o RSA). Cada um pode ser trocado sem mudar o protocolo inteiro, o que permite corrigir falhas que a **criptoanálise** (o estudo de como quebrar cifras) descobre. Quando as versões do conjunto mudam, muda também o número de versão do SSL/TLS.

A criptografia afeta as investigações de duas formas:

- o ataque pode mirar o próprio algoritmo; quebrado o algoritmo e obtidas as chaves, todos os dados capturados podem ser lidos;
- os dados ficam **escondidos à vista**: o criminoso também usa criptografia. Os comandos que ele envia às máquinas infectadas (o chamado **comando e controle**) vão cifrados, e assim ele pode infectar mais computadores e formar uma **botnet** (rede de computadores infectados comandados à distância) sem que o conteúdo seja lido; achá-los é demorado, muitas vezes por tentativa e erro.

## 8. Ocultação de Dados

Além de criptografar, é possível proteger dados **escondendo ou disfarçando a informação**, com o mascaramento e a esteganografia.

### 8.1 Mascaramento de Dados

O **mascaramento de dados** **substitui a informação confidencial por uma versão não confidencial que parece e funciona como a original**. Assim, os processos da organização usam os dados sem nenhuma mudança nos aplicativos ou no armazenamento.

O uso mais comum é **distribuir conjuntos de dados substitutos para testes e análises** fora da produção (os sistemas reais que atendem os clientes), o que limita a circulação dos dados reais. O mascaramento também pode ser **dinâmico**: o sistema mascara a informação quando julga arriscado o pedido do usuário.

Todas as técnicas mantêm os dados significativos, mas alterados o bastante para protegê-los:

| Técnica | Como funciona | Exemplo |
| --- | --- | --- |
| Substituição | Troca os dados por valores fictícios | Nomes reais trocados por nomes inventados |
| Embaralhamento | Mistura os valores da própria coluna entre os registros | Dados financeiros em um banco de testes |
| Anulação | Aplica um valor nulo ao campo, que fica totalmente invisível | CPF apagado |

### 8.2 Esteganografia

A **esteganografia** **esconde uma mensagem dentro de outro arquivo**, como uma imagem, um áudio ou um texto. Sua vantagem sobre a criptografia é que **a mensagem secreta não chama atenção**: quem vê a imagem, na tela ou impressa, não sabe que ela guarda uma mensagem.

Seus componentes são a mensagem escondida, a **capa** (o arquivo que a esconde), o **estego-arquivo** (o resultado) e a **estego-chave**, que controla o processo.

A técnica mais usada em imagens é a dos **bits menos significativos (LSB**, *Least Significant Bits*), que usa os bits de cada pixel:

- o **pixel** é a unidade básica de cor de uma imagem;
- a cor de um pixel mistura vermelho, verde e azul (**RGB**), com um byte para cada cor; um sistema de cores de 24 bits usa os três bytes;
- a técnica troca o último bit de cada byte de cor; como esse bit quase não muda a cor, **o olho humano não percebe a alteração**.

Em média, basta alterar no máximo **metade dos bits** de uma imagem para esconder uma mensagem.

Na **esteganografia social**, a mensagem tem um sentido para o público e outro para quem conhece o código, como duas mensagens ao mesmo tempo: a aparente e a secreta. Exemplos:

- adolescentes nas redes sociais combinam que "ir ao cinema" significa "ir à praia", para os pais não entenderem;
- em países com censura, as pessoas erram palavras de propósito ou fazem referências imprecisas.

### 8.3 Esteganoanálise

A **esteganoanálise** é a **descoberta de que existe informação escondida**. Os padrões da estego-imagem levantam suspeita:

- **imagens**: comparando a original com a estego-imagem, o analista procura padrões de repetição visual;
- **disco**: áreas reservadas e ainda não usadas podem esconder informação, e utilitários de análise de disco apontam dados em *clusters* (os pequenos blocos em que o disco é dividido) que deveriam estar vazios;
- **rede**: filtros capturam pacotes com informação escondida nos cabeçalhos (a parte do pacote com os dados de controle, como os endereços).

Os dois últimos métodos usam **assinaturas de esteganografia**.

| Característica | Criptografia | Esteganografia | Mascaramento |
| --- | --- | --- | --- |
| Objetivo | Tornar a mensagem ilegível | Esconder que ela existe | Trocar dados reais por falsos realistas |
| Chama atenção? | Sim | Não | Não |
| Uso típico | Dados em trânsito e em repouso | Comunicação secreta | Testes e análises |

## 9. Controle de Acesso e AAA

O **controle de acesso** é o conjunto de medidas que **define quem pode acessar cada recurso, o que pode fazer com ele e quando**.

### 9.1 Tipos de Controle de Acesso

Os controles de acesso são de **três tipos**:

| Tipo | O que são | Exemplos |
| --- | --- | --- |
| Físicos | Barreiras reais que impedem o contato direto com os sistemas; definem quem entra ou sai, onde e quando | Guardas, cercas, detectores de movimento, travas de notebook, portas trancadas, cartões de acesso, cães de guarda, câmeras, alarmes |
| Lógicos (técnicos) | Hardware e software para identificar, autenticar, autorizar e auditar | Criptografia, cartões inteligentes, senhas, biometria, ACLs, protocolos, firewalls, roteadores, sistemas de detecção de intrusão |
| Administrativos | Políticas e procedimentos da empresa, focados em práticas pessoais e de negócios | Políticas, procedimentos, práticas de contratação, verificação de antecedentes, classificação de dados, treinamento, avaliações de desempenho |

Alguns itens merecem uma explicação:

- **mantrap** (eclusa): entrada com duas portas que controla o fluxo de pessoas e pode prender um visitante indesejado entre elas;
- **níveis de corte** (*clipping levels*): limite de erros permitido antes de disparar um alerta;
- **ACL** (*Access Control List* — lista de controle de acesso): lista de regras, configurada em roteadores, firewalls ou arquivos, que define o que é permitido e o que é bloqueado (detalhada na seção 20);
- **política**: declaração de intenções; **procedimento**: os passos detalhados para realizar uma atividade;
- **verificação de antecedentes**: triagem na admissão, com histórico profissional, de crédito e criminal.

### 9.2 AAA: Autenticação, Autorização e Contabilidade

O **AAA** (*Authentication, Authorization and Accounting*) reúne os **três serviços de segurança que formam a estrutura principal do controle de acesso**:

| Serviço | Pergunta que responde | Exemplo |
| --- | --- | --- |
| Autenticação | Quem é você? | Nome de usuário e senha |
| Autorização | O que você pode fazer? | Entrar na rede não dá direito à impressora colorida; o banco de dados de vendas fica bloqueado fora do horário comercial |
| Contabilidade | O que você fez? | Acesso a um servidor por 15 minutos |

A contabilidade (*accounting*) não tem relação com finanças. Ela é o **registro do que o usuário fez**: o que acessou, por quanto tempo e o que alterou. Funciona como a auditoria de um banco, que mostra a hora, o valor e o autor de cada transação. O administrador ativa a auditoria nas políticas do computador, e o sistema controla cada transação em tempo real.

O AAA se parece com um **cartão de crédito**: ele identifica quem pode usá-lo, define quanto pode ser gasto e registra o que foi comprado.

### 9.3 Identificação

Na **identificação**, o usuário diz quem é, normalmente pelo **nome de usuário**. Sempre que alguém pede acesso a um recurso, os controles decidem se concedem ou negam, conforme a política de autorização.

O **identificador único** liga cada atividade permitida a uma pessoa e permite que o sistema reconheça cada usuário individualmente. As políticas de segurança e a sensibilidade das informações definem quais controles de identificação usar e quão rigorosos eles devem ser.

**Importante:** informar o nome de usuário é **identificação**; provar que se é aquele usuário, com a senha, é **autenticação**.

### 9.4 Métodos de Autenticação

Para provar a identidade, o usuário apresenta pelo menos um de **três tipos de fator**:

| Fator | Exemplos |
| --- | --- |
| Algo que você sabe | Senha, frase secreta, PIN (*Personal Identification Number*, a senha numérica curta, como a do cartão do banco) |
| Algo que você tem | Cartão inteligente, chaveiro de segurança (*token*), aplicativo autenticador no celular |
| Algo que você é | Impressão digital, retina, voz |

#### 9.4.1 Algo que Você Sabe

A **senha** é uma **sequência de caracteres protegida que comprova a identidade** e o **método de autenticação mais usado**. Frase secreta, código de acesso e PIN também são chamados genericamente de senha. As boas práticas são:

- não usar dados pessoais, como nome, data de nascimento ou endereço, que facilitam adivinhar;
- ter pelo menos oito caracteres, nem tão longa que não dê para lembrar, nem tão curta que seja fácil de quebrar;
- combinar maiúsculas, minúsculas, números e símbolos;
- usar uma senha diferente para cada sistema, porque uma senha quebrada abriria todas as contas;
- guardar as senhas em um **gerenciador de senhas**, que também ajuda a criá-las.

#### 9.4.2 Algo que Você Tem

O **cartão inteligente** é um cartão de plástico do tamanho de um cartão de crédito, com um **chip que guarda e protege dados** com criptografia, como contas bancárias, identificação, registros médicos e assinaturas digitais.

O **chaveiro de segurança** (*security key fob*, também chamado de *token*) é um dispositivo pequeno, preso a um chaveiro, que **mostra um número temporário**, trocado a cada minuto, e usado como segundo fator. Os aplicativos autenticadores do celular fazem a mesma coisa.

#### 9.4.3 Algo que Você É

A **biometria** usa **características físicas ou comportamentais únicas** e as compara com um **perfil**, um arquivo com as características conhecidas da pessoa. O acesso é liberado se elas baterem. Ela pode ser:

- **fisiológica**: digital, DNA, rosto, mãos, retina, orelha;
- **comportamental**: gestos, voz, modo de andar, ritmo de digitação.

A biometria cresce na segurança pública, nos eletrônicos e nos pontos de venda. Ela precisa de um leitor, de um software que converte a leitura para o formato digital e de um banco de dados com os perfis.

### 9.5 Autenticação Multifator (MFA)

A **MFA** (*Multi-Factor Authentication* — autenticação multifator) **usa pelo menos dois fatores de tipos diferentes**. Ela reduz o roubo de identidade on-line, porque saber a senha não basta para entrar na conta. Exemplos:

- o banco on-line pede a senha e um PIN enviado ao celular;
- o caixa eletrônico exige o cartão (tem) e o PIN (sabe).

Com exatamente dois fatores, chama-se **2FA** (*Two-Factor Authentication*, autenticação de dois fatores), mas os dois termos costumam ser usados como sinônimos.

**Importante:** duas senhas não formam MFA, porque são do mesmo tipo de fator.

### 9.6 Autorização

A **autorização** **controla o que o usuário pode e não pode fazer depois de autenticado**. Ela responde: "quais privilégios de leitura, cópia, edição, criação e exclusão esse usuário tem?". Alguns sistemas usam uma ACL para isso. Ela também pode limitar **quando** o acesso vale, como só no horário comercial.

O sistema compara os atributos do usuário com o banco de dados de autenticação, define as restrições e as entrega ao dispositivo em que ele está conectado. A autorização é **automática**, logo após a autenticação, sem nenhum passo extra do usuário.

Definir as regras é o primeiro passo do controle de acesso. Elas vêm da **política de autorização**, que pode ser:

- **baseada em grupo**: todos têm cartão para entrar no prédio, mas só a equipe de tecnologia (TI) e os funcionários seniores entram na sala de servidores;
- **por nível de autoridade**: as permissões dependem do cargo.

### 9.7 Auditabilidade

A **auditabilidade** (*accountability*) **rastreia cada ação até a pessoa ou o processo que a realizou** e relata os dados de uso, para auditoria ou cobrança. Ela registra, por exemplo:

- horários de login, com sucesso ou falha;
- recursos de rede acessados.

Falhas de login podem indicar que um criminoso tentou invadir uma conta; sucessos mostram quem usa cada recurso e quando. Assim, a empresa rastreia ações e erros em uma auditoria ou investigação.

A auditabilidade se implementa com **tecnologias, políticas, procedimentos e educação**:

- os arquivos de log trazem os detalhes, conforme os parâmetros escolhidos;
- as políticas definem o que registrar e como os logs são gerados, revisados e guardados;
- a retenção de dados, o descarte de mídias e as leis que exigem proteger certos dados também a exigem;
- a conscientização sobre as políticas e as leis completa o processo.

### 9.8 Gerenciamento de Identidade Federada

O **gerenciamento de identidade federada** permite que **várias organizações aceitem as mesmas credenciais** para acessar as redes de todas as empresas do grupo. O objetivo é compartilhar a identidade automaticamente entre organizações diferentes; para o usuário, é um **login único na web** (o chamado *single sign-on*). Exemplo: entrar em vários sites com o botão "Entrar com Google" ou com a mesma conta de rede social.

O risco é o **efeito cascata**: o escopo aumenta, e credenciais roubadas abrem todos os sistemas da federação. Por isso, as organizações precisam examinar o que compartilham com os parceiros, mesmo dentro do mesmo grupo: CPF, nomes e endereços roubados de um parceiro servem para fraudes. A proteção mais comum é **vincular o login a um dispositivo autorizado**.

## 10. Modelos de Controle de Acesso e Confiança Zero

Um **modelo de controle de acesso** define **quem decide sobre o acesso e com base em quê**. A organização precisa de controles adequados para proteger seus recursos de rede, sistemas e informações, e o analista precisa conhecer os modelos para entender como os atacantes os quebram.

### 10.1 Modelos de Controle de Acesso

| Modelo | Quem decide / com base em quê | Característica marcante |
| --- | --- | --- |
| DAC (*Discretionary Access Control* — discricionário, isto é, a critério do dono) | O **dono** dos dados | Menos restritivo |
| MAC (*Mandatory Access Control* — obrigatório; não confundir com o endereço MAC) | Rótulos de segurança e autorização do usuário | Mais rígido; uso militar |
| RBAC (*Role-Based Access Control* — baseado em funções) | A **função** ou cargo | Recomendado para grandes organizações |
| ABAC (*Attribute-Based Access Control* — baseado em atributos) | Atributos do usuário, do recurso e do ambiente | Mais flexível |
| Baseado em regras | Regras da equipe de segurança | Usa ACLs; o usuário não altera |
| TAC (*Time-based Access Control* — baseado em tempo) | Hora e dia | Acesso só em horários permitidos |

#### 10.1.1 Controle de Acesso Discricionário (DAC)

No **DAC**, **o dono do recurso decide quem pode acessá-lo**. É o modelo **menos restritivo** e pode usar ACLs ou outros métodos para indicar quais usuários ou grupos têm acesso. Exemplo: o dono de um arquivo define quem pode ler, gravar ou executar.

#### 10.1.2 Controle de Acesso Obrigatório (MAC)

No **MAC**, cada recurso tem um **rótulo de nível de segurança** (como "confidencial", "secreto" e "ultrassecreto") e cada usuário, uma **autorização** (*clearance*), o nível máximo que ele pode ver. O acesso só é liberado se os dois forem compatíveis, e o usuário não muda as regras. Ele restringe as ações sobre cada objeto (um arquivo, uma porta, um dispositivo) onde existem vários níveis de classificação. É o controle **mais rigoroso**, usado em aplicações militares e de missão crítica.

#### 10.1.3 Controle de Acesso Baseado em Funções (RBAC)

No **RBAC**, as decisões se baseiam nas **funções e responsabilidades** de cada pessoa. As permissões pertencem às funções (cargos, classificações de cargo ou grupos delas), e cada pessoa recebe o perfil da função que ocupa. Quando alguém muda de cargo, basta trocar a função. É um tipo de **controle não discricionário**. Facilita a administração em organizações com centenas de usuários e milhares de permissões e é amplamente aceito como **boa prática**.

#### 10.1.4 Controle de Acesso Baseado em Atributos (ABAC)

No **ABAC**, a decisão considera atributos do **objeto** (o recurso), do **sujeito** (o usuário) e do **ambiente**, como a hora do dia. Exemplo: o médico vê prontuários só no hospital e durante o plantão.

#### 10.1.5 Controle de Acesso Baseado em Regras

No **controle baseado em regras**, a equipe de segurança de rede define regras ou condições de acesso, como endereços IP permitidos ou negados e protocolos, em listas de controle de acesso. Exemplo: nenhum funcionário acessa a folha de pagamento fora do expediente ou nos fins de semana. Como no MAC, o usuário não altera as regras. Esse modelo pode ser combinado com outros; o MAC, por exemplo, pode ser implementado com regras.

**Importante:** a sigla **RBAC** serve para os dois modelos: funções (*Role*) e regras (*Rule*). Sozinha, normalmente indica o de funções.

#### 10.1.6 Controle de Acesso Baseado em Tempo (TAC)

No **TAC**, o acesso depende da **hora e do dia**. Exemplo: a folha de pagamento só aceita logins em dias úteis, das 8h às 18h.

### 10.2 Privilégio Mínimo e Escalação de Privilégios

O **privilégio mínimo** é também um modelo de controle de acesso: **usuários e processos recebem apenas o acesso mínimo necessário** às informações e ferramentas, conforme a necessidade.

Na **escalação de privilégios**, uma exploração comum, o atacante aproveita falhas em servidores ou em sistemas de controle de acesso para dar a um usuário ou processo não autorizado **um nível de privilégio maior do que deveria ter**. Com esse privilégio, ele acessa informações confidenciais ou assume o controle do sistema.

### 10.3 Confiança Zero (Zero Trust)

A **confiança zero** (*zero trust*) é uma abordagem para proteger todo o acesso em redes, aplicativos e ambientes: de usuários, dispositivos e também de programas que conversam entre si, como **APIs** (*Application Programming Interfaces*, as "portas" pelas quais um programa pede dados a outro), equipamentos de **IoT** (*Internet of Things* — internet das coisas: câmeras, sensores, eletrodomésticos conectados), **microsserviços** (aplicativos divididos em pequenas partes independentes) e **contêineres** (pacotes leves que levam um aplicativo com tudo de que ele precisa para rodar). Ela **não confia automaticamente em ninguém**, nem em quem já está dentro da rede. Seu princípio é “**nunca confie, sempre verifique**”: assumir confiança zero sempre que alguém ou algo pedir acesso. Ela impede acessos não autorizados e **contém as violações**.

No modelo antigo, o perímetro (a borda) separava o lado de dentro, confiável, do de fora, e quem passava por ele circulava pela rede inteira. Na confiança zero, **todo ponto em que há uma decisão de acesso passa a ser um perímetro**: quem já passou por um controle não é confiável em outra área até se autenticar de novo, às vezes várias vezes e de formas diferentes. Isso reduz o **movimento lateral**, a passagem do atacante de um sistema para outro.

| Pilar | O que protege |
| --- | --- |
| Força de trabalho | Funcionários, prestadores, parceiros e fornecedores que usam dispositivos pessoais ou da empresa; só usuários certos e dispositivos seguros acessam, de qualquer lugar |
| Cargas de trabalho | Aplicativos na nuvem, no data center e em ambientes virtualizados (máquinas simuladas por software) que interagem entre si; por exemplo, uma API, um microsserviço ou um contêiner acessando um banco de dados |
| Local de trabalho | Todos os dispositivos ligados à rede, inclusive IoT: computadores, servidores físicos e virtuais, impressoras, câmeras, ar-condicionado, quiosques, bombas de infusão, sistemas de controle industrial |

### 10.4 Controle de Acesso à Rede (NAC)

O **NAC** (*Network Access Control*) **aplica as políticas da organização às pessoas e aos dispositivos que tentam entrar na rede**. Ele permite monitorar quem está conectado e controlar o acesso manualmente quando necessário. Suas funções são:

- aplicar rapidamente políticas criadas para diferentes condições de operação;
- reconhecer e criar perfis de usuários e dispositivos, para que malware em sistemas fora das regras não cause danos;
- oferecer acesso seguro a visitantes, geralmente por portais de registro (a página que aparece pedindo cadastro, como no Wi-Fi de hotéis);
- verificar, **antes** de liberar o acesso, se o dispositivo cumpre as políticas conforme o tipo de usuário, o tipo de dispositivo e o sistema operacional;
- bloquear, isolar ou corrigir dispositivos fora das regras.

O BYOD (uso de aparelhos pessoais no trabalho, visto no item 4.4) e a IoT ampliam muito a **superfície de ataque**, o conjunto de pontos por onde um atacante pode entrar. Sem a automação do NAC, seria impossível avaliar os milhares de dispositivos que tentam entrar, e ele é parte importante da confiança zero.

## 11. Gerenciamento de Contas e Protocolos de Autenticação

O **gerenciamento de contas** garante que **cada usuário tenha a conta adequada à sua função** e só acesse o necessário. Os **protocolos de autenticação** definem como a identidade é comprovada pela rede.

### 11.1 Tipos de Contas

| Tipo | Uso |
| --- | --- |
| Usuário | Uso diário dos recursos do sistema |
| Serviço | Usada por programas que rodam em segundo plano (os serviços), e não por pessoas, para interagir com o sistema operacional |
| Convidado | Usuários temporários que precisam acessar aplicativos instalados |
| Administrador | Apenas administrar o sistema |

O administrador de rede tem papel importante na segurança. A conta de administrador **só deve ser usada para administrar**: se ele abrir um site infectado ou um e-mail mal-intencionado com ela, coloca a empresa em risco, porque o malware ganha os mesmos privilégios.

Os sistemas operacionais instalam grupos e contas padrão, como convidado e administrador, que os atacantes conhecem bem, principalmente em sistemas mais antigos. O administrador precisa conhecê-las para decidir quais manter e quais desativar. A boa prática é **substituir ou desativar as contas padrão** e nunca compartilhar contas.

### 11.2 Boas Práticas de Gerenciamento de Contas

As boas práticas são:

- ao contratar, criar o perfil de identidade, registrar o computador e os celulares e liberar o acesso; como **provedor de identidade (IdP)**, a empresa é responsável por autenticar o funcionário;
- liberar só o acesso necessário às tarefas (privilégio mínimo (ver item 10.2));
- revisar os acessos periodicamente para ajustar os controles;
- desativar as contas que não são mais usadas e recuperar dados e aplicativos da empresa dos dispositivos do usuário;
- limitar **quando** (restrições de horário) e **de onde** (restrições de local) cada usuário pode fazer login.

| Recurso | O que faz | Exemplo |
| --- | --- | --- |
| Delimitação geográfica (*geofencing*) | Dispara uma ação quando o usuário entra ou sai de uma área | Bloquear o acesso fora do prédio |
| Geolocalização | Identifica onde o dispositivo está | Posição do celular no mapa |
| Marcação geográfica (*geotagging*) | Acrescenta a localização a um arquivo | Foto com as coordenadas |

### 11.3 Contas Privilegiadas

As **contas privilegiadas** têm **acesso elevado e sem restrição** e são o **alvo preferido dos criminosos digitais**. Para protegê-las:

- identificar e reduzir o número de contas privilegiadas;
- aplicar o privilégio mínimo a usuários, sistemas e processos;
- revogar os acessos quando o funcionário sai ou muda de função;
- eliminar contas compartilhadas com senhas que não expiram e credenciais usadas por vários administradores;
- proteger o armazenamento das senhas;
- trocar as senhas automaticamente a cada 30 ou 60 dias e ter um processo para trocar as senhas embutidas em scripts (pequenos programas que automatizam tarefas) e contas de serviço;
- registrar as sessões privilegiadas e todas as atividades, e gerar alertas para comportamentos incomuns;
- desativar as contas privilegiadas inativas;
- exigir **autenticação multifator** em todo acesso administrativo;
- colocar um *gateway* (um ponto de passagem obrigatório e controlado) entre o usuário e os ativos confidenciais, para limitar a exposição a malware.

Esse processo deve ser avaliado e ajustado regularmente.

### 11.4 Permissões de Arquivos e Pastas

As **permissões** são regras que **limitam o acesso de uma pessoa ou de um grupo a pastas e arquivos**. Elas aplicam o privilégio mínimo, ligado ao acesso por **necessidade de saber**: cada um acessa e altera só o necessário, o que ajuda a controlar os riscos de segurança e de conformidade.

| Permissão | O que o usuário pode fazer |
| --- | --- |
| Controle total | Ver o conteúdo, alterar e excluir, criar arquivos e pastas e executar programas |
| Modificar | Alterar e excluir os existentes, mas não criar novos |
| Ler e executar | Ver o conteúdo e executar programas da pasta |
| Gravar | Criar arquivos e pastas e alterar os existentes |
| Leitura | Ver o conteúdo da pasta e abrir arquivos e pastas |

**Importante:** a permissão **Negar substitui qualquer outra**, mesmo para administradores.

Arquivos novos **herdam as permissões da pasta-mãe**. Ao mover ou copiar:

| Ação | Mesmo volume | Volume diferente |
| --- | --- | --- |
| Mover | Mantém as permissões | Herda novas |
| Copiar | Herda novas | Herda novas |

Ou seja, **só mover dentro do mesmo volume mantém as permissões originais**.

### 11.5 Políticas de Conta no Windows

Em empresas, os computadores Windows costumam fazer parte de um **domínio**, um grupo de computadores administrado de forma central pelo **Active Directory** (o cadastro central de usuários e computadores da Microsoft). Esses computadores recebem a política de segurança do domínio. Fora dele, usa-se a **Política de Segurança Local**, aberta pelo comando `secpol.msc`.

As principais políticas são:

- **senhas**: exemplo: trocar a cada 90 dias e usar cada nova senha por pelo menos um dia; oito caracteres com três das quatro categorias (maiúsculas, minúsculas, números e símbolos); só repetir uma senha depois de 24 senhas diferentes;
- **bloqueio de conta**: exemplo: depois de cinco tentativas erradas, bloquear por 30 minutos; passado esse tempo, o contador volta a zero;
- **auditoria** (em Políticas Locais): cria um log de segurança com eventos de login, gerenciamento de contas, acesso ao serviço de diretório, acesso a objetos, mudanças de política, uso de privilégios, acompanhamento de processos e eventos do sistema.

Os valores são só exemplos; cada empresa define os seus.

### 11.6 Gerenciamento de Autenticação

O **gerenciamento de autenticação** busca **garantir uma entrada segura sem complicar a vida do usuário**. Os problemas mais comuns de autenticação e autorização são credenciais não criptografadas, permissões incorretas e violações de acesso.

| Solução | Como funciona |
| --- | --- |
| SSO (*Single Sign-On*) | Um conjunto de credenciais dá acesso a vários aplicativos; basta lembrar uma senha forte |
| OAuth (*Open Authorization*) | Permite que um site use uma conta de outro serviço, como Google ou Facebook, sem receber a senha; é o que acontece no botão "Entrar com Google" |
| Cofre de senhas | Guarda as credenciais sob uma única senha forte |
| KBA (*Knowledge-Based Authentication*) | Redefine a senha esquecida com informações pessoais ou uma série de perguntas |

### 11.7 Protocolos de Autenticação

Um **protocolo de autenticação** autentica os dados entre duas **entidades** (qualquer dispositivo ou sistema da empresa) e define **o que elas trocam para se autenticar**.

| Protocolo | Como funciona | Segurança |
| --- | --- | --- |
| PAP (*Password Authentication Protocol*) | Envia usuário e senha a um servidor de acesso remoto (o equipamento que recebe as conexões de quem está fora) em **texto claro**, ou seja, sem criptografia; aceito pela maioria dos servidores | Fraca |
| CHAP (*Challenge-Handshake Authentication Protocol*) | Desafio e resposta: o servidor manda um número aleatório (o desafio), o cliente calcula um hash juntando esse número e a senha e devolve o resultado; o servidor faz a mesma conta e compara. A senha nunca viaja pela rede. A identidade é conferida de novo de tempos em tempos | Melhor que o PAP |
| EAP (*Extensible Authentication Protocol*) | Não é um método único, e sim uma estrutura que aceita vários métodos (por isso "extensível"); em geral, a senha vai protegida até o servidor de autenticação, que apresenta um certificado (o cliente não precisa ter um); comum no Wi-Fi corporativo | Depende do método |
| 802.1X | Padrão de controle de acesso por porta: o switch ou o ponto de acesso Wi-Fi só libera a conexão depois que o dispositivo se autentica com a credencial ou com um certificado, confirmado por um servidor RADIUS | Alta |
| RADIUS (*Remote Authentication Dial-In User Service*) | Servidor central que confere usuário e senha para vários equipamentos; criptografa só a senha, e o resto vai em texto claro; precisa de proteção contra **ataques de repetição** (o atacante grava uma autenticação válida e a reenvia depois) | Média |
| TACACS+ (*Terminal Access Controller Access-Control System Plus*) | Servidor central semelhante ao RADIUS, criado pela Cisco; usa o TCP (o protocolo de transporte que confirma a entrega) e criptografa tudo; permite ACLs, filtros e privilégios; melhor para redes corporativas que exigem controle da autorização | Alta |
| Kerberos | Autenticação mútua com tíquetes (ver item 11.7.1); é o método usado nos domínios Windows | Alta |

#### 11.7.1 Kerberos

O **Kerberos** usa criptografia forte e faz **autenticação mútua**: o cliente prova a identidade ao servidor, e o servidor se autentica ao cliente, com base em **tíquetes**. O tíquete funciona como uma pulseira de evento: depois de provar a identidade na entrada, o usuário a mostra em cada área sem precisar se identificar de novo. O servidor Kerberos guarda a identificação (ID) e o hash da senha de cada usuário, além de chaves secretas compartilhadas com os servidores para os quais emite tíquetes.

1. o cliente se autentica e recebe um **TGT** (*Ticket-Granting Ticket*, tíquete de concessão de tíquete);
2. apresenta o TGT e pede acesso a um serviço;
3. recebe um **tíquete de serviço** e acessa o serviço.

![No Kerberos, o cliente se autentica uma vez e depois usa tíquetes para acessar os serviços](img/defesa/def_kerberos.png){width=6in}

Como toda a sessão pode ser criptografada, as senhas não trafegam de forma insegura. Os tíquetes têm **carimbo de hora e prazo de validade**, o que impede reutilizar um tíquete antigo.

## 12. Implementação do AAA

A rede deve ser projetada para controlar **quem pode se conectar e o que pode fazer** depois de conectado. Esses requisitos ficam na **política de segurança de rede**, que define como administradores, usuários corporativos e remotos, parceiros e clientes acessam os recursos. Ela também pode exigir um sistema de contabilidade que registre **quem entrou, quando e o que fez**, e alguns regulamentos exigem guardar esses logs por um período definido.

O **AAA** (ver item 9.2) é a estrutura que permite essa segurança de acesso de forma **escalável**, com três funções independentes:

- **autenticação**: por usuário e senha, desafio e resposta (como no CHAP, item 11.7), tokens e outros métodos; o AAA a centraliza;
- **autorização**: define os recursos e as operações permitidas; exemplo: "o usuário 'aluno' pode acessar o servidor XYZ só por SSH";
- **contabilidade** (*accounting*): registra como os recursos são usados; exemplo: "o usuário 'aluno' acessou o servidor XYZ por SSH durante 15 minutos".

### 12.1 AAA Local e AAA Baseado em Servidor

A Cisco oferece **duas formas de implementar o AAA**:

| Característica | AAA local | AAA baseado em servidor |
| --- | --- | --- |
| Onde ficam os usuários | No próprio roteador | Em um servidor AAA central |
| Indicado para | Redes pequenas | Redes médias e grandes |
| Escalabilidade | Baixa | Alta |

No **AAA local**, também chamado de **autenticação autônoma**, o cliente remoto se conecta ao roteador, informa usuário e senha, e o roteador confere no próprio banco de dados. No **AAA baseado em servidor**, o roteador confere as credenciais em um servidor AAA central.

O AAA centralizado é **mais escalável e mais fácil de gerenciar** e, por isso, é a implementação preferida. Ele pode usar o Active Directory ou o **LDAP** (protocolo de consulta a serviços de diretório) para autenticar e saber os grupos do usuário, mantendo os próprios bancos de autorização e contabilidade.

### 12.2 TACACS+ e RADIUS

Os dispositivos falam com o servidor AAA pelo **TACACS+** ou pelo **RADIUS**:

| Característica | TACACS+ | RADIUS |
| --- | --- | --- |
| Funções | Separa as três funções do AAA, o que dá modularidade | Junta autenticação e autorização e separa só a contabilidade; menos flexível |
| Padrão | Principalmente Cisco | Aberto (RFC) |
| Transporte (protocolo e porta, o número que identifica o serviço) | TCP, que confirma a entrega; porta 49 | UDP, mais simples e sem confirmação; portas 1812 e 1813 (ou 1645 e 1646) |
| CHAP | Desafio e resposta nos dois sentidos | Desafio e resposta em um só sentido, do servidor para o cliente |
| Criptografia | Todo o corpo do pacote, deixando só um cabeçalho TACACS+ padrão | Só a senha no pedido de acesso; usuário, serviços autorizados e contabilidade ficam desprotegidos |
| Autorização de comandos | Por usuário ou por grupo | Não tem |
| Contabilidade | Limitada | Abrangente |

**Importante:** o **RADIUS criptografa só a senha**; o **TACACS+ criptografa todo o corpo do pacote**.

O TACACS+ é a melhor escolha quando se precisa controlar os comandos de cada administrador. O RADIUS é muito usado com 802.1X (ver item 11.7) e acesso remoto.

### 12.3 Contabilidade do AAA

Com o AAA centralizado, os registros de todos os dispositivos vão para um só lugar, o que **facilita a auditoria das ações dos usuários**. Eles incluem horários de início e fim da conexão, comandos executados, número de pacotes e de bytes, e servem para auditorias de segurança e como prova contra ações mal-intencionadas.

Quando o usuário se autentica, o AAA gera uma **mensagem de início** da contabilidade; quando ele termina, uma **mensagem de parada** encerra o registro.

| Tipo | O que registra |
| --- | --- |
| De rede | Todas as sessões PPP (*Point-to-Point Protocol*, usado em conexões diretas entre dois pontos, como acessos remotos), com contagem de pacotes e bytes |
| De conexão | Conexões de saída feitas a partir do cliente AAA, como por SSH |
| EXEC | Sessões de terminal do usuário, isto é, as conexões à linha de comando do roteador (o modo EXEC): nome, data, horas de início e fim e IP do servidor de acesso |
| Do sistema | Eventos do sistema, como reinicializações ou a contabilidade ligada e desligada |
| De comandos | Comandos digitados na linha de comando em um nível de privilégio, com data, hora e usuário |
| De recursos | Registros de início e de parada das conexões autenticadas, e de parada também para as que falharam na autenticação |

## 13. Segurança Física

A **segurança física** protege instalações e equipamentos contra o acesso físico não autorizado. De nada adianta uma senha forte se qualquer pessoa pode entrar na sala de servidores.

### 13.1 Barreiras Físicas e Cercas

As **barreiras físicas** são a **camada mais externa e mais visível da defesa** e devem seguir os requisitos do projeto e as especificações do fabricante. Seus componentes são:

- sistema de cerca de perímetro e cercamento;
- sistema de portão de segurança;
- **cabeços de amarração** (*bollards*), postes curtos que impedem a invasão com veículos;
- barreiras de entrada de veículos;
- abrigos de proteção.

A **cerca** protege as áreas seguras e marca os limites da propriedade.

A altura da cerca define o quanto ela atrasa um invasor:

| Altura | Efeito |
| --- | --- |
| 1 metro (3 a 4 pés) | Só detém invasores casuais |
| 2 metros (6 a 7 pés) | Alta demais para invasores casuais escalarem |
| 2,5 metros (8 pés) | Atrasa por pouco tempo um invasor determinado |

Áreas de alta segurança acrescentam uma **proteção superior**, como arame farpado ou concertina (a espiral de arame com lâminas), que atrasa o invasor e pode feri-lo; ainda assim, ele pode usar um cobertor ou colchão para passar.

Cuidados com as cercas:

- as regras locais podem restringir o tipo de cerca;
- elas exigem manutenção: animais cavam por baixo e a erosão deixa a cerca instável, por isso precisam de inspeção regular;
- nunca estacionar veículos perto da cerca, porque ajudam o invasor a escalar ou danificam a cerca.

### 13.2 Biometria no Controle de Acesso Físico

A biometria usa características fisiológicas ou comportamentais e é muito usada para liberar portas e áreas restritas. Os sistemas medem rosto, impressão digital, geometria da mão, íris, retina, assinatura e voz. O uso cresceu com o aumento de falhas de segurança e de fraudes; um exemplo conhecido é o celular com leitor de digital, que libera aplicativos de banco e de pagamento.

Na escolha do sistema, pesam:

- precisão;
- velocidade de atendimento (*throughput*);
- aceitação pelos usuários;
- exclusividade do órgão ou da ação medidos;
- resistência à falsificação;
- confiabilidade;
- espaço para armazenar os dados;
- tempo de cadastro;
- grau de intrusão da verificação.

O fator mais importante é a **precisão**, expressa em tipos e taxas de erro:

| Erro | Nome | O que acontece |
| --- | --- | --- |
| Tipo I | Falsa rejeição | Barra um usuário autorizado |
| Tipo II | Falsa aceitação | Deixa entrar quem não deveria |

**Importante:** no controle de acesso, o **erro tipo II (falsa aceitação) é o mais grave**, porque deixa um invasor entrar. A falsa rejeição é o menos importante, embora possa prejudicar muito o negócio.

A **taxa de aceitação**, em porcentagem, é a frequência com que o sistema aceita impostores ou pessoas descadastradas como usuários autênticos.

A **CER** (*Crossover Error Rate* — taxa de erro de cruzamento) é o ponto em que as taxas de falsa rejeição e de falsa aceitação se igualam. **Quanto menor a CER, mais preciso é o sistema.**

### 13.3 Vigilância

Todos os controles físicos, de dissuasão e de detecção, dependem, no fim, de **pessoas que intervenham** para parar o ataque:

| Forma | Vantagens | Desvantagens |
| --- | --- | --- |
| Guardas e escoltas | Resposta imediata; se adaptam, distinguem situações e decidem na hora | Custo, dificuldade de monitorar e registrar muito movimento e erro humano |
| Vigilância eletrônica e por vídeo (CFTV, circuito fechado de TV, as câmeras de segurança) | Monitora sem ninguém presente, grava por longos períodos e detecta e avisa sobre movimento | Depende de alguém que assista e reaja |
| Etiquetas RFID (*Radio-Frequency Identification*) | Pequenas etiquetas com chip lidas por ondas de rádio, como as de pedágio automático; rastreiam ativos que saem da área segura e permitem ler várias etiquetas ao mesmo tempo | Exigem leitores nas saídas |

Os **guardas** são a melhor solução quando é preciso **resposta instantânea e adequada**. Em ambientes de alta segurança, a vigilância eletrônica e por vídeo complementa ou substitui os guardas e deve cobrir todas as entradas, saídas, locais de carga, escadas e áreas de coleta de lixo.

Localizar os ativos importantes é um desafio, ainda maior com celulares e IoT, e procurar um equipamento crítico pode causar atrasos e paradas caras. As etiquetas **RFID** (identificação por radiofrequência) resolvem isso: os leitores ficam escondidos nos batentes das portas, e as etiquetas, diferentemente dos códigos de barras, **não precisam estar visíveis nem na linha de visão do leitor**. Exemplo: um notebook da empresa escondido em uma bolsa dispara o alerta ao passar pela porta.

### 13.4 Controle de Ameaças às Instalações

As principais medidas são:

- controle de acesso e circuito fechado de TV (CFTV) em todas as entradas;
- políticas e procedimentos para os visitantes;
- testes da segurança do prédio, tentando entrar às escondidas por meios cibernéticos e físicos;
- crachás com criptografia;
- planos de recuperação de desastres e de continuidade dos negócios;
- treinamento e conscientização em segurança;
- sistema de marcação (etiquetagem) de ativos.

Nas instalações de alta segurança, os guardas controlam o acesso às áreas confidenciais, porque se adaptam melhor que os sistemas automáticos.

## 14. Segurança de Aplicações

A **segurança de aplicações** protege os programas, sites e serviços que a organização desenvolve e usa. Ela deve ser **prioridade em todas as etapas: desenvolvimento, testes e implantação**.

### 14.1 Etapas do Desenvolvimento de Aplicações

O desenvolvimento usa ambientes separados:

Desenvolvimento e teste → Preparação → Produção

| Ambiente | O que acontece |
| --- | --- |
| Desenvolvimento e teste | O software é escrito, testado e depurado; o ambiente é menos restritivo e tem segurança mais baixa que o real; nos testes, a equipe de garantia de qualidade (QA, *Quality Assurance*) analisa como o código interage com o ambiente e encontra falhas, que são **muito mais fáceis de corrigir nessa fase** |
| Preparação (*staging*) | Ambiente que deve corresponder ao de produção, para confirmar que o software roda com as configurações de segurança necessárias |
| Produção | Depois dos testes de segurança, o software entra em uso real, atendendo usuários e clientes de verdade |

O software de **controle de versão** (como o Git) rastreia e gerencia as alterações no código, guardando cada versão, e o **sandbox** ("caixa de areia") é um ambiente isolado em que o desenvolvedor trabalha sem afetar o sistema real e sem que seu código seja sobrescrito por outros.

O **provisionamento** é a criação ou atualização do software; o **desprovisionamento**, a remoção. Um **portal de autoatendimento** pode automatizar os dois.

### 14.2 Técnicas de Codificação Segura

| Técnica | O que faz |
| --- | --- |
| Normalização | Organiza os dados no banco e mantém a integridade; converte cada entrada para a forma mais simples, com uma representação binária única, o que ajuda a achar entradas maliciosas |
| Procedimento armazenado | Grupo de comandos em SQL (*Structured Query Language*, a linguagem usada para consultar e alterar bancos de dados) já preparados e guardados no próprio banco, que executam uma tarefa; o aplicativo só chama o procedimento, sem montar comandos com o que o usuário digitou, o que reduz o tráfego, dá resultados mais rápidos e dificulta ataques de injeção de SQL |
| Ofuscação | Esconde os dados originais com caracteres aleatórios |
| Camuflagem | Troca dados confidenciais por dados fictícios realistas |
| Reutilização de código e SDKs | Aproveitam código pronto para desenvolver mais rápido e mais barato |

A ofuscação e a camuflagem dificultam a **engenharia reversa**, a tentativa de descobrir como o programa funciona.

Na reutilização de código e nos **SDKs** (*Software Development Kits* — kits de desenvolvimento de software, pacotes de código pronto oferecidos por fabricantes), **uma vulnerabilidade no código reaproveitado passa para todos os aplicativos que o usam**.

### 14.3 Validação de Entrada

**Controlar o que entra no banco de dados é essencial para manter a integridade dos dados.** Os criminosos miram as informações confidenciais dos bancos de dados, e muitos ataques enviam dados malformados para confundir, travar o aplicativo ou fazê-lo revelar informações.

Exemplo: os usuários assinam uma newsletter (boletim enviado por e-mail) por um formulário web, e o sistema envia um e-mail com um link de confirmação. O atacante altera o link, mudando o nome, o e-mail ou o status da assinatura. Se o servidor não conferir cada endereço com os dados da assinatura, recebe informações falsas. O ataque pode ser automatizado para encher o banco com milhares de assinantes inválidos.

A **regra de validação** confere se os dados estão **dentro dos parâmetros definidos pelo projetista do banco de dados**:

| Critério | O que verifica | Exemplo |
| --- | --- | --- |
| Tamanho | Número de caracteres | CEP com 8 dígitos |
| Formato | Formato definido | Data DD/MM/AAAA |
| Consistência | Dados que combinam entre si | Cidade compatível com o estado |
| Intervalo | Valor entre um mínimo e um máximo | Idade entre 0 e 120 |
| Dígito verificador | Cálculo extra para detectar erros de digitação | Último dígito do ISBN (o número que identifica cada livro) ou os dois últimos do CPF |

#### 14.3.1 Exemplo Resolvido: Dígito Verificador do ISBN-10

O ISBN-10 tem 10 dígitos, e o último é o verificador. Para os nove primeiros dígitos 1 5 8 7 1 4 3 7 3:

1. multiplica-se o primeiro dígito por 10, o segundo por 9, e assim por diante, até o nono por 2;
2. somam-se os resultados;
3. o dígito verificador é o que falta para chegar a um múltiplo de 11.

| Dígito | 1 | 5 | 8 | 7 | 1 | 4 | 3 | 7 | 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Peso | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 |
| Produto | 10 | 45 | 64 | 49 | 6 | 20 | 12 | 21 | 6 |

Soma: 233. O múltiplo de 11 seguinte é 242, e 242 − 233 = 9. O **dígito verificador é 9**.

### 14.4 Integridade dos Dados no Aplicativo

Dados comprometidos ameaçam os dispositivos e sistemas. A **verificação de integridade** mede a consistência dos dados de um arquivo, imagem ou registro: uma função hash tira um **instantâneo** dos dados, que depois confirma que eles não mudaram.

- **checksum** (soma de verificação): confere arquivos ou textos antes e depois da transferência; converte cada conjunto de informações em um valor e soma tudo; o receptor repete a conta, e somas iguais indicam dados válidos;
- **funções hash** (MD5, SHA-1, SHA-256, SHA-512): depois de baixar um arquivo, compara-se o hash da fonte com o calculado por uma calculadora de hash;
- **controle de versão**: evita alterações acidentais; duas pessoas não alteram o mesmo arquivo, registro ou transação ao mesmo tempo; a primeira que abre o documento pode alterá-lo, e a segunda recebe uma versão somente leitura;
- **backups precisos**: recuperam dados corrompidos; a integridade do backup deve ser conferida antes de qualquer perda;
- **autorização**: controles de acesso e permissões garantem que só certos usuários modifiquem os dados; um arquivo somente leitura não aceita alterações.

### 14.5 Outras Práticas de Segurança de Aplicativos

Duas práticas garantem que o software é autêntico e que a navegação é segura:

- **assinatura de código**: o executável é assinado digitalmente para validar a identidade do autor e garantir que o código não mudou desde a assinatura;
- **cookies seguros**: o **cookie** é um pequeno arquivo que o site pede ao navegador para guardar, com dados como o login e o carrinho de compras, e que o navegador devolve ao site a cada novo acesso; por isso, quem rouba um cookie pode se passar pelo usuário. Os desenvolvedores devem marcar os cookies para trafegar **só por HTTPS** (a versão criptografada do HTTP, o protocolo das páginas web), nunca por HTTP sem criptografia.

### 14.6 Controle de Ameaças a Aplicativos

| Ameaça | Medidas |
| --- | --- |
| Acesso não autorizado a data centers, salas de computadores e armários de cabos | Políticas, padrões e procedimentos para funcionários e visitantes |
| Sistema fora do ar | Plano de continuidade de negócios para os aplicativos essenciais e plano de recuperação de desastres para aplicativos e dados |
| Vulnerabilidade no sistema operacional de rede | Política de atualizações de aplicativos e do sistema; correções (*patches*) instaladas regularmente |
| Acesso não autorizado aos sistemas | MFA e monitoramento dos logs |
| Perda de dados | Padrões de classificação de dados e procedimentos de backup |
| Vulnerabilidades no desenvolvimento | Testes antes do lançamento |

Além disso, a empresa deve seguir as boas práticas de segurança de rede, que protegem os sistemas contra ameaças e acessos não autorizados.

### 14.7 OWASP Top 10

A **OWASP** (*Open Web Application Security Project*) é uma organização sem fins lucrativos que publica a cada três anos o **OWASP Top 10**, a lista das **dez principais preocupações de segurança web** das empresas. Suas páginas da comunidade reúnem os ataques e as vulnerabilidades relatados pelos colaboradores.

## 15. Fortalecimento de Serviços e Protocolos de Rede

O **fortalecimento da rede** (*network hardening*) consiste em **proteger os serviços e protocolos para que só o necessário fique exposto**, trocando os protocolos inseguros por versões seguras. Os invasores entram na infraestrutura por serviços, protocolos e portas abertas, e protocolos antigos deixam a rede vulnerável.

### 15.1 Varredura de Portas

Um **scanner de portas** envia uma mensagem a cada porta de um dispositivo e espera a resposta, para saber quais estão abertas e como são usadas. A **porta** é o número que identifica um serviço; exemplo: a 80 é do HTTP.

O administrador usa o scanner para achar serviços desprotegidos, e o atacante também. Por isso, o ideal é que **apenas as portas necessárias fiquem abertas**.

### 15.2 Serviços de Rede e de Roteamento

#### 15.2.1 DHCP

O **DHCP** (*Dynamic Host Configuration Protocol*) usa um servidor para **atribuir automaticamente endereço IP** e outras configurações aos dispositivos; é o que permite conectar o celular ao Wi-Fi sem configurar nada; na prática, o dispositivo ganha do servidor a permissão para usar a rede. O atacante pode mirar o servidor DHCP para negar o acesso à rede ou criar um servidor falso, que entrega configurações erradas e faz o tráfego das vítimas passar pela máquina dele.

O **DHCP snooping** (rastreamento de DHCP) **impede que servidores DHCP falsos entreguem endereços**, porque valida as mensagens vindas de fontes não confiáveis. A lista de verificação do DHCP é:

- proteger fisicamente o servidor;
- aplicar as correções de software;
- deixar o servidor atrás de um firewall;
- monitorar os registros do DHCP;
- manter um antivírus forte;
- desinstalar serviços e aplicativos não usados;
- fechar as portas não usadas.

#### 15.2.2 DNS

O **DNS** (*Domain Name System* — sistema de nomes de domínio) **converte nomes, como www.cisco.com, em endereços IP**, funcionando como a agenda de contatos da internet. Atacando o DNS, o criminoso pode negar o acesso aos recursos ou **redirecionar o tráfego para sites falsos**.

As **DNSSEC** (*DNS Security Extensions*) usam **assinaturas digitais** para fortalecer a autenticação das respostas DNS. A lista de verificação do DNS é:

- manter o software DNS atualizado;
- impedir que o servidor informe a versão do programa DNS que usa, o que ajudaria o atacante a procurar falhas conhecidas;
- separar os servidores DNS internos dos externos;
- restringir as transações pelo endereço IP do cliente;
- autenticar as transações com assinaturas de transação (TSIG, um código calculado com uma chave secreta compartilhada entre os servidores);
- desativar ou restringir ao máximo as **transferências de zona** (a cópia da lista completa de nomes de um domínio para outro servidor, que entregaria ao atacante o mapa da rede) e as **atualizações dinâmicas** (alterações de registros feitas automaticamente pela rede);
- ativar e analisar os logs;
- usar DNSSEC e assinar as zonas (zona é o conjunto de registros de um domínio, como todos os nomes de exemplo.com.br).

#### 15.2.3 ICMP

O **ICMP** (*Internet Control Message Protocol*) **envia mensagens de erro e de controle**, como serviço indisponível ou host (computador) inalcançável. O comando **ping** usa o ICMP para testar se um host responde. Os atacantes o usam como **canal secreto** (escondendo dados dentro de mensagens de ping, que parecem inofensivas), para reconhecimento da rede (descobrir quais máquinas estão ligadas) e para ataques de negação de serviço (**DoS**, *Denial of Service*, que tiram um serviço do ar). Por isso, muitas redes filtram o ICMP.

#### 15.2.4 RIP

O **RIP** (*Routing Information Protocol*) é um protocolo de roteamento, isto é, uma linguagem com que os roteadores trocam informações sobre as redes que cada um alcança. Ele escolhe a rota pela contagem de **saltos** (cada roteador atravessado no caminho conta um salto), com **máximo de 15 saltos**. Ataques ao roteamento afetam o desempenho e a disponibilidade e podem até redirecionar o tráfego. A proteção é usar **serviços seguros com autenticação** e aplicar correções e atualizações.

#### 15.2.5 NTP

O **NTP** (*Network Time Protocol*) **sincroniza os relógios dos dispositivos** com um servidor NTP. Carimbos de hora corretos são essenciais para rastrear eventos como violações, interpretar os logs syslog (o padrão de envio de logs pela rede, visto na seção 29) e validar certificados, que têm data de validade. Os criminosos atacam os servidores de tempo para interromper a comunicação que depende de certificados e esconder os carimbos de hora do ataque. A proteção é a **autenticação NTP**.

### 15.3 Telnet, SSH e SCP

O **Telnet** e o **SSH** (*Secure Shell*) dão acesso remoto, por linha de comando, a dispositivos como roteadores:

| Característica | Telnet | SSH |
| --- | --- | --- |
| Criptografia | Nenhuma | Tudo criptografado |
| Porta | TCP 23 | TCP 22 |
| O que um sniffer (como o Wireshark) vê | Usuário e senha do administrador em texto claro | Apenas os endereços IP; usuário e senha vão criptografados |
| Recomendação | Evitar | Usar sempre |

O **SCP** (*Secure Copy*) **transfere arquivos entre dois sistemas remotos usando o SSH**, inclusive na autenticação, o que garante a autenticidade e a confidencialidade dos dados em trânsito.

### 15.4 Protocolos Seguros

Os principais protocolos têm versões seguras:

- **SNMPv3**: o **SNMP** (*Simple Network Management Protocol*) coleta estatísticas dos dispositivos, como uso de processador e de tráfego, para monitorar a rede; a versão 3, padrão atual, usa criptografia contra espionagem e alteração dos dados;
- **SSL e TLS**: o HTTP (porta 80) tem segurança limitada e pode ser monitorado; o SSL criptografa a sessão com um *handshake* (a "apresentação" inicial em que os dois lados combinam os algoritmos e as chaves) no início, e o **TLS** é o **substituto atualizado e mais seguro do SSL**; com eles, o navegador mostra **HTTPS**;
- **FTPS**: no **FTP** (*File Transfer Protocol*, protocolo de transferência de arquivos), o cliente se conecta com usuário e senha em texto claro; o FTPS acrescenta TLS e SSL contra interceptação, alteração e falsificação;
- **e-mail**: o **POP** (*Post Office Protocol*, porta 110), que baixa as mensagens para o computador, e o **IMAP** (*Internet Message Access Protocol*, porta 143), que as mantém no servidor e sincroniza vários aparelhos, recebem as mensagens; o **MIME** (*Multipurpose Internet Mail Extensions*) permite anexar dados que não são texto, como imagens e vídeos; POP e IMAP devem usar SSL/TLS, e o **S/MIME** envia e-mails **assinados e criptografados**, com autenticação, integridade e não repúdio.

### 15.5 Resumo de Protocolos Inseguros e Seguros

| Função | Protocolo inseguro | Alternativa segura |
| --- | --- | --- |
| Acesso remoto | Telnet (TCP 23) | SSH (TCP 22) |
| Cópia de arquivos | FTP | FTPS ou SCP |
| Navegação web | HTTP (porta 80) | HTTPS (porta 443) |
| Gerenciamento | SNMPv1 e SNMPv2 | SNMPv3 |
| E-mail | POP (110) e IMAP (143) sem criptografia | POP e IMAP com SSL/TLS; S/MIME |
| Resolução de nomes | DNS sem autenticação | DNSSEC |
| Tempo | NTP sem autenticação | NTP com autenticação |

## 16. Segmentação de Rede

A **segmentação** é a **divisão de uma rede em partes menores para melhorar o desempenho e a segurança**. Quem invade um segmento não alcança automaticamente os outros.

### 16.1 VLANs

Uma **VLAN** (*Virtual Local Area Network* — rede local virtual) **agrupa dispositivos de forma lógica**, em uma LAN e em switches individuais, não importa onde estejam ligados. Cada porta do switch (o equipamento que liga os computadores de uma rede local) pode ser atribuída a uma VLAN.

**Importante:** a **LAN** se baseia em **conexões físicas**; a **VLAN**, em **conexões lógicas**.

Os **troncos** (*trunks*) são portas que ligam os switches e **transportam o tráfego de várias VLANs**. Assim, pessoas do mesmo setor podem estar em andares diferentes e na mesma VLAN.

Os administradores segmentam a rede por **função, equipe ou aplicativo**. Os dispositivos de uma VLAN funcionam como uma **rede independente**, mesmo dividindo a infraestrutura com outras VLANs. Exemplo: o RH fica em uma VLAN própria, separando os dados confidenciais do resto da rede, o que **reduz a chance de vazamento**. As VLANs também limitam o **broadcast** (mensagens para todos os dispositivos) a cada VLAN.

Para proteger a VLAN: monitorar o desempenho, usar configurações avançadas e instalar correções e atualizações regularmente.

### 16.2 Zona Desmilitarizada (DMZ)

A **DMZ** (*Demilitarized Zone* — zona desmilitarizada) é uma **pequena rede entre a rede privada confiável e a internet**. Nela ficam os servidores acessados de fora, como os **servidores web e de e-mail**, para que os usuários usem uma rede não confiável, como a internet, sem comprometer a rede interna.

A maioria das redes tem de **duas a quatro zonas de risco**:

| Zona | Risco | Confiança |
| --- | --- | --- |
| LAN privada | Baixo | Alta |
| Extranet (rede com parceiros) | Médio-baixo | Médio-alta |
| DMZ | Médio-alto | Médio-baixa |
| Internet | Alto | Baixa |

Os firewalls controlam o tráfego **leste-oeste** (que circula dentro da rede, entre servidores do data center) e **norte-sul** (que entra e sai da rede). Os nomes vêm do desenho tradicional das redes, com a internet no alto e os servidores lado a lado.

### 16.3 Segmentação e Confiança Zero

A segmentação é a base técnica da confiança zero (ver item 10.3): cada passagem entre segmentos vira um ponto de controle. A rede de confiança zero **monitora constantemente todos os usuários**, qualquer que seja o status ou a função.

| Característica | VLAN | DMZ |
| --- | --- | --- |
| O que separa | Setores dentro da rede interna | Servidores públicos da rede interna |
| Onde fica | Dentro da LAN | Entre a LAN e a internet |
| Exemplo | VLAN do RH | Servidor web da empresa |

## 17. Segurança Sem Fio e de Dispositivos Móveis

Os dispositivos sem fio e móveis, de celulares e computadores a roteadores e câmeras IP, são hoje a **maioria dos dispositivos nas redes**. Eles trazem mobilidade e conveniência, mas estão sujeitos a roubo, invasão e acesso remoto não autorizado, interceptação do tráfego (*sniffing*), ataques *man-in-the-middle* (o atacante se coloca no meio da conversa e lê ou altera o que passa) e ataques ao desempenho e à disponibilidade. A melhor proteção combina **autenticação e criptografia**.

### 17.1 Padrões de Segurança Sem Fio

Os padrões de segurança do Wi-Fi definem como a rede sem fio autentica os aparelhos e criptografa o que trafega pelo ar. Eles evoluíram nesta ordem:

WEP → WPA → WPA2 → WPA3

| Padrão | Características | Situação |
| --- | --- | --- |
| WEP (*Wired Equivalent Privacy*) | Primeiro padrão; chaves de 64 e 128 bits; quebrado em poucos minutos com ferramentas gratuitas | Fraco, não usar |
| WPA (*Wi-Fi Protected Access*) | Resposta às fraquezas do WEP; chaves de 256 bits; **MIC** (*Message Integrity Check*), que detecta dados capturados e alterados entre o roteador Wi-Fi (o ponto de acesso, ou AP) e o aparelho do usuário; **TKIP** (*Temporal Key Integrity Protocol*), que trata, protege e troca melhor as chaves | Substituiu o WEP |
| WPA2 (2006) | **AES** (a cifra simétrica do item 5.3) obrigatório, com melhor gerenciamento de chaves; **CCMP** (o modo de uso do AES no Wi-Fi) no lugar do TKIP | Seguro |
| WPA3 | Acrescenta ao WPA2 algoritmos criptográficos robustos e uma troca de chaves melhor | O mais atual |

Em casa, o mais comum é o **WPA-PSK** (*Pre-Shared Key* — chave pré-compartilhada), em que todos usam a mesma senha do Wi-Fi. Nas empresas, usa-se o modo **Enterprise**, em que cada pessoa entra com o próprio usuário e senha, conferidos por um servidor (o EAP, no item 17.2).

O **WPS** (*Wi-Fi Protected Setup*) facilita configurar a rede de casa e conectar dispositivos IoT, mas o **PIN pode ser descoberto por força bruta** (testando todas as combinações possíveis, o que no WPS leva poucas horas). Por isso, não deve ser usado e deve ser **desativado**.

### 17.2 Autenticação em Redes Sem Fio

O **802.11** é o nome técnico do padrão Wi-Fi. Na versão original, ele tem **dois tipos de autenticação**:

- **sistema aberto**: qualquer dispositivo se conecta; só para situações em que a segurança não importa;
- **chave compartilhada**: autentica e criptografa entre o cliente e o ponto de acesso.

O **ponto de acesso** (*access point*, AP) é o equipamento que liga os aparelhos sem fio à rede cabeada.

O **EAP** (*Extensible Authentication Protocol*) é a estrutura de autenticação usada nas redes sem fio:

1. o usuário pede a conexão ao AP;
2. o AP pede a identificação (nome de usuário) e a envia ao servidor de autenticação;
3. o servidor pede a prova de que a identidade é válida;
4. o AP pede a senha ao usuário, que a fornece, e o AP a repassa ao servidor;
5. o servidor confirma que usuário e senha estão corretos e avisa o AP e o usuário;
6. o usuário se conecta à rede sem fio.

Quatro protocolos são usados com o EAP:

| Método | Certificado no cliente | Certificado no servidor | Implantação | Segurança |
| --- | --- | --- | --- | --- |
| EAP-TLS (usa o TLS do item 5.4) | Sim | Sim | Difícil | Alta |
| PEAP (*Protected EAP*: cria primeiro um túnel TLS e depois envia usuário e senha dentro dele) | Não | Sim | Moderada | Média |
| EAP-TTLS (*Tunneled TLS*: ideia parecida com a do PEAP) | Não | Sim | Moderada | Média |
| EAP-FAST (criado pela Cisco; usa uma credencial própria em vez de certificado) | Não | Não | Fácil | Média |

O **EAP-TLS é o mais seguro e o mais difícil de implantar**, porque exige certificado nas duas pontas.

### 17.3 Pontos de Acesso Não Autorizados e Autenticação Mútua

Qualquer dispositivo com interface sem fio e cabeada ligado à rede pode agir como **ponto de acesso não autorizado** (*rogue AP*). Ele **imita um ponto de acesso legítimo** para que as vítimas se conectem; o impostor então pede e copia dados dos dispositivos. Esse ataque man-in-the-middle é **muito difícil de detectar** e pode roubar credenciais de login e dados.

A proteção é a **autenticação mútua** (de duas vias): **as duas pontas se autenticam antes de se conectar**, e o cliente percebe quando o ponto de acesso é falso.

Para a internet, os celulares também usam as redes de telefonia móvel da operadora, como o **LTE** (*Long Term Evolution*, o 4G) e o **5G**.

### 17.4 Comunicação dos Dispositivos Móveis

| Método | Como funciona | Exemplo |
| --- | --- | --- |
| Wi-Fi e Bluetooth | Sinais sem fio, configurados no menu do aparelho | Fone de ouvido; som do carro |
| NFC (*Near-Field Communication*) | Comunicação sem contato por campos eletromagnéticos | Pagamento por aproximação |
| Infravermelho (IR) | Curto alcance, com um receptor de IR | Controlar a TV pelo celular |
| USB | O único com fio | Armazenamento e áudio; celular compartilhando a internet com o computador (como um modem); ligar o aparelho a equipamentos de **aquisição forense** (que copiam o conteúdo do aparelho como prova) em uma investigação |

### 17.5 Gerenciamento de Dispositivos Móveis

No **COPE** (*Corporate-Owned, Personally Enabled*), o aparelho é da empresa e o uso pessoal é permitido, por isso guarda dados pessoais e da organização; no BYOD (ver item 4.4), o aparelho é do funcionário. Nos dois casos, valem as políticas de segurança e proteção de dados quando há informação confidencial no aparelho.

As principais formas de gerenciamento são:

- **segmentação do armazenamento e conteinerização**: cria uma área autenticada e criptografada que **separa os dados da empresa dos dados pessoais**; permite isolar os aplicativos, controlar as funções deles, apagar o contêiner e bloquear ou limpar o aparelho à distância;
- **gerenciamento de conteúdo**: avalia o risco de aplicativos que compartilham dados, como Dropbox, Box, Google Drive e iCloud; um sistema de gerenciamento de identidades controla o que cada usuário acessa;
- **gerenciamento de aplicativos**: a **lista de permissões** (*whitelisting*) assina digitalmente os aplicativos autorizados, para garantir que venham de fontes confiáveis; os aplicativos que pedem credenciais devem usar senhas fortes.

### 17.6 Ameaças e Proteções dos Dispositivos Móveis

Seja da empresa ou pessoal, o aparelho precisa de proteção contra roubo, perda, acesso não autorizado e riscos do sistema operacional, dos aplicativos e da rede. Alguns usuários **contornam as limitações do aparelho** para rodar aplicativos não autorizados ou fora da loja:

| Técnica | Plataforma | O que faz | Risco |
| --- | --- | --- | --- |
| Jailbreak | Apple | Remove a restrição de só rodar aplicativos autorizados pela Apple | Alto |
| Root | Android | Ignora a arquitetura de segurança e dá acesso administrativo total | Alto |
| Sideloading | Ambas | Contorna as configurações para instalar aplicativos não aprovados, como os de lojas de terceiros, não avaliados | Menor, mas ainda é um risco |

Há soluções que detectam aparelhos com jailbreak ou root: eles são marcados como **não conformes** e removidos da rede ou bloqueados nos aplicativos da organização.

As proteções são:

- bloqueio de tela, com senha, PIN ou padrão;
- biometria: impressão digital, rosto, íris ou voz;
- **autenticação com reconhecimento de contexto**, que usa aprendizado de máquina (programas que aprendem padrões a partir de dados) para liberar o acesso conforme o comportamento normal do usuário, como o local e o horário de costume;
- **limpeza remota**, se o aparelho for perdido ou roubado;
- criptografia completa do dispositivo.

### 17.7 Rastreamento por GPS

O **GPS** (*Global Positioning System*) usa satélites e computadores para localizar o aparelho em tempo real, com precisão de cerca de **5 metros**. Muitos aplicativos rastreiam o celular; o Facebook, por exemplo, permite fazer **check-in** em um local, visível para os contatos. Alguns aplicativos usam a **delimitação geográfica** ou a geolocalização para definir uma área.

As **notificações push** (mensagens que aparecem sem abrir o aplicativo) também usam a localização, e comércios locais enviam propagandas conforme as configurações do usuário.

Criminosos também usam **notificações push para capturar dados** dos usuários.

## 18. Resiliência e Alta Disponibilidade

A **resiliência** torna um sistema **tolerante a falhas**: ele continua funcionando quando algo dá errado, inclusive durante um ataque. O objetivo é **reduzir ao mínimo o tempo de inatividade**. A disponibilidade contínua é essencial não só para as empresas, mas para a vida moderna, que depende cada vez mais dos sistemas de informação.

### 18.1 Alta Disponibilidade

A **alta disponibilidade** descreve **sistemas concebidos para evitar períodos de inatividade**, com acesso ininterrupto aos dados e serviços. Eles seguem três princípios:

1. **eliminar ou reduzir os pontos únicos de falha** (definidos logo abaixo), com dispositivos em espera ativa (*hot standby*, ligados e prontos para assumir), componentes redundantes (duplicados) e várias conexões ou caminhos;
2. **garantir uma transição confiável**, com fontes de alimentação redundantes e sistemas de energia e de comunicação de reserva;
3. **detectar as falhas assim que ocorrem**, com monitoramento ativo, que pode até acionar o sistema de reserva.

O **ponto único de falha** (*Single Point of Failure*, SPOF) é o elo fraco: **qualquer parte cuja falha derruba o sistema inteiro**. Pode ser um equipamento (roteadores ou switches centrais), um processo, um dado, um serviço de rede, um utilitário essencial ou até uma equipe de TI altamente qualificada. A solução é mudar a operação crítica para que não dependa de um único elemento, ou criar componentes redundantes que assumam o processo.

Em um **cluster de alta disponibilidade**, vários computadores com acesso ao mesmo armazenamento e configurações de rede idênticas processam o mesmo serviço ao mesmo tempo; se um falha, os outros continuam.

- **tolerância a falhas**: o sistema segue funcionando se um ou mais componentes falharem; exemplo: com o espelhamento de dados, se o controlador de disco falha, o sistema espelhado entrega os dados sem interrupção aparente;
- **resiliência do sistema**: manter os dados e o processamento disponíveis mesmo sob ataque ou interrupção, com energia e processamento redundantes; vai além de blindar os dispositivos.

### 18.2 Os Cinco Noves

Toda empresa quer operar sem parar, mesmo em condições extremas, como um ataque. Uma das práticas mais conhecidas são os **cinco noves**: **99,999% de disponibilidade**, ou **menos de 5,26 minutos de inatividade por ano**.

#### 18.2.1 Exemplo Resolvido: Tempo de Inatividade nos Cinco Noves

| Etapa | Cálculo | Resultado |
| --- | --- | --- |
| Minutos no ano | 365 × 24 × 60 | 525.600 min |
| Fração de inatividade | 100% − 99,999% = 0,001% | 0,00001 |
| Inatividade máxima | 525.600 × 0,00001 | 5,256 ≈ 5,26 min |

Para chegar aos cinco noves, usam-se:

- **sistemas padronizados**: com os mesmos componentes, o estoque de peças é mais fácil de manter e é possível trocar componentes em uma emergência;
- **clustering**: vários dispositivos agrupados parecem uma única entidade para o usuário;
- **sistemas de componentes compartilhados**: um sistema completo pode substituir o que falhou.

### 18.3 Redundância N+1

Na **redundância N+1**, os componentes necessários (N) têm **pelo menos um componente de reserva (+1)**, em espera e pronto para entrar em ação, como os quatro pneus e o estepe de um carro. Em um data center, isso significa ter um servidor, uma fonte de alimentação, um switch e um roteador de reserva.

**Observação:** o N+1 tem equipamento redundante, mas **não é totalmente redundante**: suporta a perda de um componente, não de todos.

### 18.4 RAID

O **RAID** (*Redundant Array of Independent Disks*) **distribui os dados entre vários discos**. Se um disco é perdido, os dados são recuperados dos outros, e a leitura fica mais rápida, porque vários discos trabalham juntos. Pode ser feito por software ou por hardware, com um controlador especializado. Combina três técnicas:

| Técnica | Como funciona | Protege contra falha de disco? |
| --- | --- | --- |
| Espelhamento | Grava os dados duplicados em outro disco | Sim |
| Distribuição (*striping*) | Espalha os dados por vários discos | Não, sozinha |
| Paridade | Depois da distribuição, gera somas de verificação, guardadas em uma terceira unidade, para conferir e reconstruir os dados | Sim |

**Importante:** o **RAID 0 usa apenas distribuição e não tem redundância**. Quem protege contra falha de disco são o RAID 1 (espelhamento) e o RAID 5 (paridade).

### 18.5 Spanning Tree Protocol (STP)

A redundância protege a rede de pontos únicos de falha, como um cabo ou um switch. Mas cabos redundantes entre switches criam **loops** (caminhos em círculo) e **quadros duplicados** (o quadro é o nome do bloco de dados na rede local): os quadros circulam sem parar, multiplicando-se, e derrubam a rede comutada (a rede formada por switches).

O **STP** (*Spanning Tree Protocol*) **bloqueia de propósito os caminhos redundantes**, deixando um só caminho lógico entre todos os destinos. Os caminhos físicos continuam existindo para dar redundância. Se um cabo ou switch falha, o STP recalcula os caminhos e desbloqueia as portas necessárias.

#### 18.5.1 Exemplo Resolvido: o STP Diante de uma Falha

Três switches, S1, S2 e S3, estão ligados em triângulo. Para evitar o loop, o STP deixa bloqueada a porta de S2 que leva a S3 (o Tronco2), e o tráfego de S2 vai direto a S1.

1. o tronco entre S2 e S1 falha e interrompe o caminho original;
2. S2 desbloqueia a porta do Tronco2, e o tráfego segue pelo caminho alternativo, S2 → S3 → S1;
3. quando o link entre S2 e S1 volta, o STP bloqueia de novo o link entre S2 e S3.

### 18.6 Redundância de Roteador

O **gateway padrão** é o roteador que dá acesso às outras redes. Sozinho, ele é um ponto único de falha.

Com um roteador de reserva (*standby*), os dois usam um **protocolo de redundância** para decidir qual fica ativo e compartilham um **endereço IP virtual**; os dispositivos usam esse **IP virtual como gateway padrão**. Pelos IPs físicos, os dois trocam mensagens periódicas para confirmar que estão on-line. Se o de reserva deixa de receber essas mensagens, assume o encaminhamento. Os computadores continuam falando com o IP virtual (por exemplo, 192.0.2.100) e permanecem on-line.

Essa recuperação automática é a **redundância de primeiro salto** (o gateway é o primeiro roteador no caminho do computador). Protocolos que a oferecem: **HSRP** (*Hot Standby Router Protocol*, da Cisco), **VRRP** (*Virtual Router Redundancy Protocol*, padrão aberto) e **GLBP** (*Gateway Load Balancing Protocol*, da Cisco, que também divide a carga entre os roteadores).

### 18.7 Redundância de Local

Conforme as necessidades, a empresa pode precisar de redundância de local:

| Replicação | Sincronização | Largura de banda | Distância entre locais |
| --- | --- | --- | --- |
| Síncrona | Em tempo real | Alta | Pequena, para reduzir a latência (o atraso da comunicação) |
| Assíncrona | Quase em tempo real | Menor | Maior, porque a latência pesa menos |
| Ponto no tempo | Atualiza periodicamente o local de backup | A menor, sem conexão constante | Qualquer |

O equilíbrio entre custo e disponibilidade define a melhor escolha.

### 18.8 Design Resiliente

O **design resiliente** é **mais do que adicionar redundância**: é entender as necessidades do negócio e incorporar a redundância de modo que a recuperação seja rápida. Exemplos:

- o STP dá um caminho alternativo, mas a transição pode não ser imediata se a configuração não for ideal;
- os protocolos de roteamento dão resiliência, e o ajuste fino deixa a transição imperceptível;
- o administrador deve testar configurações não padrão em uma rede de testes para melhorar o tempo de recuperação.

A **resiliência de aplicativos** é a capacidade de o aplicativo reagir a problemas em um componente sem parar de funcionar. Ela evita perder clientes, funcionários ou negócios por falha de aplicativo, lembrando que o administrador às vezes precisa desligar aplicativos para correções, atualizações ou novas funções.

Na resiliência de aplicativos, **quanto maior a disponibilidade, maiores a complexidade e o custo**:

| Solução | Complexidade e custo |
| --- | --- |
| Hardware tolerante a falhas: vários componentes essenciais no mesmo computador | Os maiores |
| Arquitetura de cluster: servidores que funcionam como um único sistema | Intermediários |
| Backup e restauração: cópias dos arquivos para restaurar se houver perda | Os menores |

Nos roteadores e switches Cisco, a **configuração resiliente do IOS** acelera a recuperação se alguém, de propósito ou não, formatar a memória flash (onde fica o sistema) ou apagar a configuração de inicialização. Ela guarda uma cópia protegida do arquivo do sistema IOS e da configuração em uso, o **bootset primário**, que o usuário não consegue apagar (comandos `secure boot-image` e `secure boot-config`).

### 18.9 Backups

Os dados podem ser perdidos por roubo, falha de equipamento, desastre ou erro. O **backup** guarda uma cópia das informações em uma mídia, de preferência removível e guardada em local seguro, e é **uma das formas mais eficazes de proteger contra a perda de dados**. Uma boa política de segurança exige backups regulares, normalmente guardados em outro local. Ao planejá-lo, considera-se:

- **frequência**: é comum fazer um backup completo mensal ou semanal e backups parciais frequentes do que mudou desde então; muitos backups parciais aumentam o tempo de restauração;
- **armazenamento**: levar as cópias a um local externo aprovado, em rodízio diário, semanal ou mensal, conforme a política;
- **segurança**: proteger os backups com senha, digitada antes de restaurar;
- **validação**: conferir sempre os backups, para garantir a integridade dos dados.

### 18.10 Energia

O fornecimento contínuo de energia é crítico. As regras gerais são:

- o data center fica em uma fonte de alimentação separada do resto do prédio;
- fontes redundantes: duas ou mais alimentações vindas de duas ou mais subestações;
- condicionamento da energia (equipamentos que filtram oscilações e entregam tensão estável);
- sistemas de energia de reserva, muitas vezes necessários;
- **nobreak** (UPS, *Uninterruptible Power Supply*) para desligar os sistemas normalmente.

| Categoria | Evento | O que é |
| --- | --- | --- |
| Excesso | Pico (*spike*) | Alta tensão momentânea |
| Excesso | Sobretensão (*surge*) | Alta tensão prolongada |
| Perda | Falha (*fault*) | Perda momentânea |
| Perda | Blecaute | Perda completa |
| Degradação | Afundamento (*sag*) | Baixa tensão momentânea |
| Degradação | Subtensão (*brownout*) | Baixa tensão prolongada |
| Degradação | Corrente de partida (*inrush*) | Sobrecarga inicial de energia |

**Importante:** **pico** e **afundamento** são **momentâneos**; **sobretensão** e **subtensão** são **prolongadas**.

### 18.11 Climatização (HVAC)

O **HVAC** (*Heating, Ventilation and Air Conditioning*) controla **temperatura, umidade e circulação do ar** e é crítico para a segurança das pessoas e dos equipamentos. Ele deve ser planejado junto com o hardware, o cabeamento, o armazenamento, a proteção contra incêndio, a segurança física e a energia.

Quase todo equipamento vem com **requisitos ambientais**, faixas aceitáveis de temperatura e umidade, no documento de especificações ou no guia de planejamento físico. Respeitá-los evita falhas e prolonga a vida dos sistemas.

Os sistemas modernos de HVAC ficam conectados à internet para monitoramento remoto e são acessados por fornecedores e terceiros. Como os técnicos precisam achar informações rápido, as credenciais ficam espalhadas e acessíveis a muita gente, inclusive a funcionários das empreiteiras. Quanto mais gente tem acesso, menos seguro é o sistema, e sua interrupção é um risco considerável para a empresa.

## 19. Sistemas Embarcados, IoT e Tecnologias de Dissimulação

As redes ligam hoje **máquinas industriais, sensores, carros e equipamentos médicos**. Esses sistemas têm fragilidades próprias e ampliam a superfície de ataque.

### 19.1 Infraestruturas Críticas e SCADA

Setores como manufatura, energia, comunicação e transporte mantêm a infraestrutura de que o país depende, e protegê-los é fundamental para a economia.

O **SCADA** (*Supervisory Control and Data Acquisition* — controle de supervisão e aquisição de dados) serve para **controlar e monitorar processos industriais**. Ele faz parte dos **ICS** (*Industrial Control Systems* — sistemas de controle industrial), usados na manufatura, na produção, na energia e na comunicação.

O **Stuxnet**, um vírus descoberto em 2010 que danificou centrífugas de enriquecimento de urânio no Irã, mirou sistemas SCADA e mostrou que um ataque digital pode **destruir ou interromper infraestruturas essenciais**, como telecomunicações, transportes e usinas de energia, e até o setor financeiro.

Os sistemas SCADA são vulneráveis porque **foram projetados sem conexão com a rede corporativa e a internet**, e a segurança não foi pensada no desenvolvimento. Hoje, as empresas querem coletar dados para melhorar as operações e reduzir custos e ligam o SCADA à rede da empresa, o que aumenta o risco.

A principal proteção é **separar as redes internas das externas e a rede SCADA da rede local da empresa**.

### 19.2 Internet das Coisas (IoT)

A **IoT** (*Internet of Things* — Internet das Coisas) é o conjunto de tecnologias que **conectam objetos variados à internet**: bilhões de carros, máquinas industriais, robôs, fechaduras, motores e aparelhos de entretenimento. Como os usuários precisam acessá-los à distância, ficam on-line e **aumentam o número de pontos de entrada na rede**.

A IoT, a virtualização e o armazenamento na nuvem (assuntos das seções 25 e 26) fizeram os dados crescerem de forma exponencial, o que criou a área de **Big Data**, que estuda como guardar e analisar volumes enormes de dados. Há muito mais dados a gerenciar e proteger.

Os dispositivos IoT expandem muito a superfície de ataque: milhares de aparelhos precisam de acesso à rede para enviar dados e ser gerenciados. Aparelhos inteligentes infectados já foram usados em alguns dos maiores ataques **DDoS** (*Distributed Denial of Service*, em que muitos aparelhos atacam um alvo ao mesmo tempo) da história. Por isso:

- verificar se o dispositivo aceita atualizações de **firmware** (o software gravado no próprio aparelho, que o faz funcionar) com correções, de preferência pela rede sem fio;
- **trocar sempre as credenciais padrão de administrador**, que são públicas.

Empresas e consumidores usam a IoT para automatizar processos, monitorar o ambiente e alertar sobre condições adversas. A maioria se conecta **sem fio**: câmeras, fechaduras, sensores de proximidade, luzes e outros sensores. Fabricantes avisam quando é preciso trocar peças ou repor suprimentos, e as empresas controlam estoque, veículos e pessoal. Com **sensores geoespaciais**, dá para localizar e controlar à distância temperatura, umidade e iluminação.

Muitos dispositivos IoT usam um **RTOS** (*Real-Time Operating System* — sistema operacional de tempo real), um sistema pequeno que troca de tarefa rapidamente e prioriza o tempo exato, não o volume, com alta confiabilidade. Ele está em vestíveis (relógios e pulseiras inteligentes), equipamentos médicos, carros e automação residencial e é vulnerável a **injeção de código** (o atacante insere comandos próprios no sistema), **negação de serviço** e **inversão de prioridade** (uma tarefa de prioridade baixa passa na frente de uma de prioridade alta).

O **Shodan** é um buscador que mostra dispositivos IoT expostos e vulneráveis na internet. A IoT se comunica por métodos de curto, médio ou longo alcance, como celular (4G, 5G), rádio e **Zigbee**, um conjunto de protocolos sem fio de baixo consumo para **WPANs** (*Wireless Personal Area Networks*, redes pessoais de curto alcance, como as de lâmpadas e sensores de uma casa).

Para proteger os dispositivos IoT:

- proteger a rede sem fio;
- saber exatamente quais dispositivos se comunicam na rede e o que cada um faz;
- instalar software de segurança sempre que possível;
- proteger os celulares e aplicativos usados para controlá-los.

### 19.3 Sistemas Embarcados

Os **sistemas embarcados** são computadores dedicados a uma função dentro de outro equipamento, como TVs inteligentes e carros. Eles capturam, guardam e acessam dados e trazem desafios próprios por serem muito usados por empresas e consumidores.

Os ataques exploram falhas de software e de hardware. Eles sofrem **ataques de tempo**: o atacante mede **quanto tempo o sistema leva para responder** a entradas diferentes para descobrir fraquezas. É um **ataque de canal lateral**, baseado em informações da implementação do sistema, e não em falhas do software.

Uma técnica de proteção é o **SoC** (*System on Chip*), um módulo de hardware de formato reduzido, como o **Raspberry Pi** e o **Arduino**. São computadores de placa única, que podem usar um **FPGA** (*Field-Programmable Gate Array*), circuito que pode ser reprogramado depois de instalado. Têm bom processamento em pouco espaço, gastam menos energia, custam menos e rendem mais que componentes maiores. O SoC reúne em um só chip o microcontrolador, o processador e periféricos como a GPU (*Graphics Processing Unit*, o processador de vídeo), o Wi-Fi ou um coprocessador, e pode rodar Windows, Linux ou Android.

Muitos dispositivos SoC têm **autenticação fraca e não podem ser atualizados ou corrigidos**. Como não existe programa formal para verificar seus controles de segurança, é preciso ter neles uma **confiança implícita**.

### 19.4 Voz sobre IP (VoIP)

O **VoIP** (*Voice over IP* — voz sobre IP) **usa redes de dados para fazer ligações telefônicas**. Precisa de uma conexão com a internet e de um destes:

- telefone tradicional com adaptador, que liga o aparelho analógico à linha digital VoIP;
- telefone próprio para VoIP;
- software VoIP no computador.

O VoIP doméstico usa a internet, mas muitas organizações usam redes privadas, mais seguras e com melhor qualidade. Sua segurança **depende da segurança da rede por baixo dele**: quando a rede cai, a voz cai junto. Os criminosos o atacam para usar o telefone de graça, espionar ligações ou afetar o desempenho e a disponibilidade.

As medidas de proteção são:

- criptografar os pacotes de voz contra espionagem;
- usar SSH (ver item 15.3) para administrar os gateways de voz (que ligam a rede VoIP à telefonia comum) e os switches;
- trocar todas as senhas padrão;
- usar um sistema de detecção de intrusão contra ataques como o **envenenamento ARP** (o atacante engana os aparelhos da rede local para que enviem a ele o tráfego destinado a outro equipamento);
- usar autenticação forte contra o **spoofing de registro** (o criminoso desvia para si as chamadas da vítima), a **representação de proxy** (a vítima fala com um proxy falso) e o **sequestro de chamadas** (a chamada é interceptada e desviada);
- usar firewalls que reconheçam o VoIP, monitorem os fluxos e filtrem sinais anormais.

### 19.5 Sistemas de Finalidade Específica

| Setor | Exemplos | Riscos | Proteções |
| --- | --- | --- | --- |
| Saúde | Marca-passos, bombas de insulina, implantes e desfibriladores, com conexão sem fio, monitoramento remoto e NFC (a comunicação por aproximação, item 17.4) | Segurança do paciente, vazamento de prontuários e porta de entrada para a rede | — |
| Automotivo | Sistemas que guardam dados de operação, manutenção e emergência; muitos registram velocidade, localização e frenagem e os enviam à seguradora | Rastreamento não autorizado, interferência sem fio e falsificação | Software projetado com segurança, criptografia entre os controladores e firewall |
| Aviação | Controle de voo e comunicação | Credenciais fixas no código, protocolos inseguros e *backdoors* | — |
| Drones (UAV, *Unmanned Aerial Vehicle*, veículo aéreo não tripulado) | Uso militar, agrícola e de cartografia; foto aérea, vigilância e topografia | Sequestro, ataques de Wi-Fi, falsificação de GPS, bloqueio e ataques de autenticação | — |

Um **backdoor** (porta dos fundos) é um acesso escondido que contorna a autenticação.

### 19.6 Tecnologias de Dissimulação

As **tecnologias de dissimulação** (*deception*) acrescentam **uma camada falsa à infraestrutura**. Elas distraem o atacante das redes de produção, ensinam os métodos dele e alertam sobre possíveis ataques.

| Tecnologia | O que é |
| --- | --- |
| Honeypot | Sistema-isca que imita um servidor da empresa, exposto de propósito; registra e monitora as ações do atacante para análise |
| Honeynet | Conjunto de honeypots que imita a rede da empresa |
| Honey files | Arquivos falsos, que atraem o atacante mas não têm informação real |
| DNS sinkhole ("ralo" de DNS) | O servidor DNS responde com um endereço falso e inofensivo quando alguém tenta acessar um site malicioso conhecido; assim, o usuário (ou o malware instalado na máquina) não chega ao destino |

O objetivo do honeypot é **desviar o atacante dos recursos reais e revelar como ele age**.

## 20. Listas de Controle de Acesso (ACLs) e Máscaras Curinga

Um condomínio fechado tem um porteiro que só abre o portão para quem está na lista. Na rede, esse porteiro é a **ACL**, que decide quais pacotes passam por um roteador.

### 20.1 O que é uma ACL

O roteador decide o caminho de cada pacote pelo cabeçalho: compara o IP de destino com as rotas da **tabela de roteamento** (a lista de redes que ele conhece e de por onde chegar a cada uma) e encaminha pela melhor correspondência.

A **ACL** (*Access Control List* — lista de controle de acesso) é uma **série de comandos que filtra pacotes de acordo com as informações do cabeçalho**. Cada linha é uma instrução de permitir (*permit*) ou negar (*deny*), chamada de **ACE** (*Access Control Entry*) ou **declaração da ACL**.

Por padrão, o roteador não tem nenhuma ACL. Com a ACL aplicada a uma **interface** (cada porta física do roteador onde um cabo se liga a uma rede), ele passa a **comparar cada pacote que passa com as ACEs, em ordem**, para decidir se o encaminha. Essa é a **filtragem de pacotes**: analisar os pacotes que entram ou saem e encaminhá-los ou descartá-los conforme os critérios. Ela atua nas **camadas 3 e 4** do modelo OSI, o modelo que divide a comunicação em sete camadas: a **camada 3** (rede) cuida dos endereços IP, e a **camada 4** (transporte) cuida das portas e dos protocolos TCP e UDP.

Usos comuns:

- limitar o tráfego e melhorar o desempenho, bloqueando vídeo, por exemplo;
- controlar o fluxo, aceitando atualizações de roteamento só de fontes conhecidas e em certos links;
- dar segurança básica, liberando a rede do RH só para pessoas autorizadas;
- filtrar por tipo de tráfego: permitir e-mail e negar Telnet;
- liberar serviços só para certos grupos, como o acesso por FTP ou HTTP;
- dar prioridade a certas classes de tráfego, como a voz, junto com a **QoS** (qualidade de serviço).

### 20.2 Tipos de ACL

Os roteadores Cisco têm dois tipos de ACL IPv4:

- **ACL padrão**: filtra **apenas pelo endereço IPv4 de origem**;
- **ACL estendida**: filtra pelos endereços de **origem e/ou destino** (camada 3) e, na camada 4, pelas portas TCP e UDP (que indicam o serviço, como a 80 do HTTP) e pelo tipo de protocolo, para um controle mais fino.

As **ACLs nomeadas** são o **método preferido** e são criadas com o comando `ip access-list` no modo de configuração global (o modo da linha de comando do roteador em que se alteram as configurações gerais). Suas regras:

- o nome identifica a finalidade da ACL; exemplo: FTP-FILTER;
- pode ter letras e números, mas não espaços nem pontuação;
- recomenda-se escrevê-lo em MAIÚSCULAS;
- é possível acrescentar ou excluir entradas na ACL.

| Característica | ACL padrão | ACL estendida |
| --- | --- | --- |
| Camadas analisadas | 3 | 3 e 4 |
| Endereço | Só origem | Origem e/ou destino |
| Portas e protocolo | Não | Sim |
| Números | 1–99 e 1300–1999 | 100–199 e 2000–2699 |

### 20.3 Como a ACL Processa os Pacotes

As ACLs controlam os pacotes que chegam às interfaces, os que passam pelo roteador e os que saem dele. Elas podem filtrar em dois sentidos:

- **de entrada** (*inbound*): antes do roteamento; é mais eficiente, porque o pacote descartado nem é roteado;
- **de saída** (*outbound*): depois do roteamento, para pacotes que saem pela interface.

O processo de uma ACL padrão aplicada na entrada de uma interface é:

1. o roteador lê o endereço IPv4 de origem do pacote;
2. começa pelo topo da ACL e compara com cada ACE, **de cima para baixo**;
3. **na primeira correspondência**, permite ou nega e para de comparar;
4. se nada corresponder, descarta o pacote.

![A ACL é lida de cima para baixo e para na primeira correspondência; o que não corresponde a nada é descartado](img/defesa/def_acl.png){width=6in}

Toda ACL termina com uma **negação implícita**, que **nega tudo o que não foi permitido**.

**Importante:** por isso, **toda ACL precisa ter pelo menos uma instrução de permitir**.

**Observação:** as ACLs não filtram os pacotes criados pelo próprio roteador.

### 20.4 Máscaras Curinga

A **máscara curinga** (*wildcard mask*) **indica quais bits do endereço devem ser verificados**. Ela também é usada pelo protocolo de roteamento OSPF. Tem 32 bits, como a máscara de sub-rede, mas combina os 0 e os 1 de outra forma.

Na máscara de sub-rede, que indica qual parte do endereço IP identifica a rede, o bit 1 marca a rede. O endereço IPv4 tem 32 bits, escritos em quatro blocos de 8 bits, os **octetos**, cada um com valor de 0 a 255. A máscara curinga segue a **lógica inversa**:

- bit **0** → o bit do endereço **precisa corresponder**;
- bit **1** → o bit do endereço é ignorado.

| Máscara curinga | Último octeto em binário | Efeito no último octeto |
| --- | --- | --- |
| 0.0.0.0 | 00000000 | Verifica todos os bits |
| 0.0.0.15 | 00001111 | Verifica os 4 primeiros e ignora os 4 últimos |
| 0.0.0.63 | 00111111 | Verifica os 2 primeiros e ignora os 6 últimos |
| 0.0.0.252 | 11111100 | Ignora os 6 primeiros e verifica os 2 últimos |
| 0.0.0.255 | 11111111 | Ignora o octeto inteiro |

Nos quatro primeiros casos, os três primeiros octetos são sempre verificados.

Exemplos:

- um host: `access-list 10 permit 192.168.1.1 0.0.0.0`; todos os bits precisam corresponder;
- uma sub-rede: `access-list 10 permit 192.168.1.0 0.0.0.255`, que vale para os hosts de 192.168.1.1 a 192.168.1.254;
- um intervalo: `access-list 10 permit 192.168.16.0 0.0.15.255`, que vale para os hosts de 192.168.16.1 a 192.168.31.254.

### 20.5 Exemplo Resolvido: Cálculo de Máscaras Curinga

O atalho é **subtrair a máscara de sub-rede de 255.255.255.255**, octeto por octeto. A notação /24, /28 etc. (o prefixo) indica quantos bits da máscara de sub-rede valem 1: /24 equivale a 255.255.255.0.

| Situação | Máscara de sub-rede | Máscara curinga | Comando |
| --- | --- | --- | --- |
| Rede 192.168.3.0/24 | 255.255.255.0 | 0.0.0.255 | `permit 192.168.3.0 0.0.0.255` |
| Rede 192.168.3.32/28 | 255.255.255.240 | 0.0.0.15 | `permit 192.168.3.32 0.0.0.15` |
| Redes 192.168.10.0 e .11.0 (/23) | 255.255.254.0 | 0.0.1.255 | `permit 192.168.10.0 0.0.1.255` |
| Redes 192.168.16.0 a .31.0 (/20) | 255.255.240.0 | 0.0.15.255 | `permit 192.168.16.0 0.0.15.255` |

Conferência em binário do segundo caso, no último octeto:

| Item | Binário | Decimal |
| --- | --- | --- |
| Endereço | 0010 0000 | 32 |
| Curinga | 0000 1111 | 15 |
| Menor endereço que corresponde | 0010 0000 | 32 |
| Maior endereço que corresponde | 0010 1111 | 47 |

Portanto, `192.168.3.32 0.0.0.15` vale para **192.168.3.32 a 192.168.3.47**.

**Observação:** no curso, os comandos dos dois últimos casos estão errados; os corretos são os da tabela.

### 20.6 Palavras-chave host e any

Escrever as máscaras em decimal pode ser cansativo. O Cisco IOS tem duas palavras-chave para os casos mais comuns, que reduzem a digitação e, principalmente, **facilitam a leitura** da ACE:

- **host** → equivale à máscara **0.0.0.0**: **um único endereço**. Exemplo: `access-list 10 permit host 192.168.10.10`, em vez de `192.168.10.10 0.0.0.0`;
- **any** → **qualquer endereço**, o mesmo que `0.0.0.0 255.255.255.255`. Exemplo: `access-list 11 permit any`.

## 21. Configuração e Aplicação de ACLs

Com a lógica da ACL (ver item 20.1) e das máscaras curinga entendida, falta escrever a lista no roteador, aplicá-la no lugar certo e corrigi-la quando preciso.

### 21.1 Planejamento

A ACL deve ser preparada antes de ser digitada:

1. escrever em um editor de texto o que a política deve fazer;
2. acrescentar os comandos de configuração do IOS (o sistema dos equipamentos Cisco) e comentários (*remarks*);
3. copiar e colar os comandos no dispositivo;
4. **testar com cuidado** se a ACL aplica a política desejada.

Assim, a ACL é criada sem afetar o tráfego da rede.

### 21.2 ACL Padrão

A ACL padrão numerada é criada com:

`access-list número {deny | permit | remark texto} origem [curinga] [log]`

| Parâmetro | Função |
| --- | --- |
| número | 1 a 99 ou 1300 a 1999 |
| deny / permit | Nega ou permite se as condições corresponderem |
| remark | Comentário opcional para documentação, de até 100 caracteres; muito útil em ACLs longas |
| origem | Endereço de host ou de rede; **host** com um endereço, só o endereço, ou **any** para todas as redes |
| curinga | Opcional; se omitida, vale 0.0.0.0 |
| log | Opcional; gera uma mensagem no primeiro pacote que corresponde, com o número da ACL, a condição (permitido ou negado), a origem e o número de pacotes |

O **log** usa muito a CPU e prejudica o desempenho do equipamento. Por isso, só deve ser usado na solução de problemas ou por segurança, por exemplo para descobrir quem é o invasor durante um ataque.

Para remover a ACL numerada, usa-se `no access-list número`.

A ACL padrão nomeada é criada com `ip access-list standard NOME`. O *prompt* (o texto que aparece antes do cursor na linha de comando) muda para o modo de configuração da ACL nomeada, e as ACEs são digitadas em seguida, **sem repetir o comando para cada ACE**. Os nomes têm letras e números, diferenciam maiúsculas de minúsculas e precisam ser únicos. Não é obrigatório usar MAIÚSCULAS, mas elas destacam a ACL na **running-config** (a configuração em uso no roteador, exibida com `show running-config`) e evitam criar, sem querer, duas ACLs com o mesmo nome escrito de formas diferentes. Exemplo: `ip access-list standard NO-ACCESS`. Para removê-la: `no ip access-list standard NOME`.

### 21.3 ACL Estendida

A ACL estendida numerada é criada com:

`access-list número {deny | permit} protocolo origem curinga [operador porta] destino curinga [operador porta] [established]`

Os passos são os mesmos da ACL padrão, mas a sintaxe é mais complexa; não é preciso usar todas as palavras-chave. A faixa de números é de 100 a 199 e de 2000 a 2699.

- **protocolo**: nome ou número de um protocolo; os mais usados são **ip** (todos os protocolos IP), **tcp**, **udp** e **icmp**; o `?` mostra a ajuda;
- **destino**: como a origem, com **host**, só o endereço ou **any**, seguido da curinga;
- **operador e porta**: comparam as portas de origem ou de destino; os operadores são **eq** (igual), **neq** (diferente), **lt** (menor) e **gt** (maior), e a porta pode ser o número ou o nome;
- **established**: só para TCP; deixa passar apenas respostas de conexões já abertas (ver item 21.4); é um recurso de firewall de primeira geração.

O protocolo escolhido define as opções de porta: tcp mostra as portas TCP; udp, as UDP; icmp, os tipos de mensagem. Os **nomes das portas facilitam entender a finalidade** da ACE; `eq 23` e `eq telnet` dão o mesmo resultado.

| Nome | Porta | Serviço |
| --- | --- | --- |
| ftp-data / ftp | 20 / 21 | FTP |
| telnet | 23 | Telnet |
| smtp | 25 | Envio de e-mail |
| domain | 53 | DNS |
| www | 80 | HTTP |
| pop3 | 110 | Recebimento de e-mail |

O SSH (22) e o HTTPS (443) **não têm nome na lista** e precisam ser escritos pelo número.

Para remover a ACL estendida numerada, usa-se `no access-list número`. A nomeada é criada com `ip access-list extended NOME` (por exemplo, NO-FTP-ACCESS), e as ACEs vão no modo de configuração da ACL estendida nomeada. Exemplo que deixa a rede 192.168.10.0/24 navegar na web por HTTP e HTTPS:

```
ip access-list extended SURFING
 permit tcp 192.168.10.0 0.0.0.255 any eq 80
 permit tcp 192.168.10.0 0.0.0.255 any eq 443
```

### 21.4 A Palavra-chave established

A palavra-chave **established** deixa o tráfego interno sair e **apenas as respostas a esse tráfego voltem**.

Uma conexão TCP é aberta com o *three-way handshake*, uma troca de três mensagens: quem quer conversar envia um **SYN** ("vamos sincronizar?"), o outro lado responde **SYN-ACK** ("sim, e confirmo") e o primeiro fecha com **ACK** ("confirmado"). Depois disso, todos os segmentos (o nome dos blocos de dados do TCP) levam o sinalizador ACK. O established aceita os segmentos com **ACK ou RST** (*reset*, a mensagem que encerra uma conexão à força) ativado, ou seja, de conexões já abertas. Assim, só as respostas ao tráfego que saiu de 192.168.10.0/24 voltam, e o tráfego TCP iniciado por um host externo é negado. Sem o established, o servidor web externo também poderia iniciar conexões.

No exemplo, a SURFING deixa sair o HTTP e o HTTPS dos usuários internos, e a BROWSING deixa voltar só o tráfego web de retorno; todo o resto que sai pela G0/0/0 (a interface Gigabit Ethernet 0/0/0 do roteador, voltada para a LAN) rumo à LAN é negado pela negação implícita. Depois que os hosts internos acessam sites seguros, o `show access-lists` mostra os contadores do `eq 443` da SURFING e do established da BROWSING aumentando. O mesmo vale com ACLs numeradas, como a 110 (saída) e a 120 (retorno, com established).

```
ip access-list extended BROWSING
 permit tcp any 192.168.10.0 0.0.0.255 established
interface g0/0/0
 ip access-group SURFING in
 ip access-group BROWSING out
```

### 21.5 Aplicação nas Interfaces e nas Linhas VTY

A ACL só funciona depois de **aplicada**. Na interface:

`ip access-group {número | nome} {in | out}`

Nas linhas **VTY** (*Virtual Teletype*, as "portas" virtuais por onde entram as conexões remotas de Telnet e SSH ao roteador), usa-se `access-class`:

```
ip access-list standard VTY_ACCESS
 permit 192.168.10.10
 deny any
line vty 0 4
 access-class VTY_ACCESS in
```

O comando `show access-lists` mostra as ACLs e quantas vezes cada ACE foi usada.

Para tirar a ACL da interface, usa-se `no ip access-group`; ela continua configurada no roteador até o comando `no access-list`. As ACLs também fazem parte de outras configurações de segurança, como o NAT (a tradução de endereços privados em públicos), os firewalls baseados em zona (ver seção 24) e as VPNs.

### 21.6 Modificação de ACLs

ACLs com várias ACEs são complexas, e às vezes uma ACE não produz o efeito esperado; no começo, pode ser preciso um pouco de tentativa e erro. Há dois métodos para corrigir uma ACL:

- **editor de texto**: as ACLs com várias ACEs devem ser criadas em um editor, o que facilita planejar e corrigir; copiar a ACL da running-config para o editor, corrigi-la, **apagar a antiga no roteador** e colar a nova; sem apagar, as linhas novas só se somam às antigas;
- **número de sequência**: entrar na ACL com `ip access-list standard` e apagar a entrada errada pelo número (10, 20, 30...), com `no 10`, porque **não dá para sobrescrever** um número que já existe; depois, digitá-la de novo com o mesmo número e conferir com `show access-lists`.

Exemplo: a primeira ACE deveria negar o host 192.168.10.10, mas foi digitada errada com o número 10; apaga-se a 10 e digita-se a correta.

### 21.7 Diretrizes e Posicionamento

As diretrizes principais são:

- a última instrução é sempre a negação implícita `deny any` ou `deny ip any any`;
- a ordem importa: a leitura é de cima para baixo e para na primeira correspondência;
- organizar **do mais específico ao mais genérico**, por exemplo negando um host e permitindo todos os outros;
- novas ACEs entram no final da lista;
- os pacotes gerados pelo roteador não passam pelas ACLs de saída;
- **uma ACL por interface, por protocolo e por direção**.

O posicionamento segue a regra:

- **ACL estendida** → o **mais perto possível da origem**, para o tráfego indesejado não atravessar a rede;
- **ACL padrão** → o **mais perto possível do destino**, porque ela só enxerga a origem e, perto dela, bloquearia todos os destinos.

Uma ACL padrão perto da origem permitiria ou negaria pelo endereço de origem, **qualquer que fosse o destino**. Já a estendida perto da origem evita que o tráfego indesejado atravesse várias redes só para ser recusado no fim.

Outros fatores também pesam:

| Fator | Explicação |
| --- | --- |
| Alcance do controle da organização | A organização só coloca ACLs nos equipamentos que controla, na origem ou no destino |
| Largura de banda | Filtrar na origem evita transmitir tráfego indesejado que consome banda |
| Facilidade de configuração | No destino é mais fácil, mas desperdiça banda; na origem economiza banda, mas exige ACLs estendidas em vários roteadores |

#### 21.7.1 Exemplo Resolvido: Onde Colocar Cada ACL

A rede 192.168.10.0/24 não pode alcançar 192.168.30.0/24 (ACL padrão no R3):

Na topologia do exemplo, três roteadores (R1, R2 e R3) estão ligados entre si por interfaces seriais (as S, de *serial*), e cada um tem redes locais nas interfaces G (Gigabit Ethernet). As redes 192.168.10.0 e 192.168.11.0 ficam no R1; as redes 192.168.30.0 e 192.168.31.0, no R3.

- na entrada da S0/1/1 do R3, também bloquearia a .10 rumo à rede 192.168.31.0/24, o que não se quer;
- na **saída da G0/0/0 do R3**, ligada à rede .30, não afeta as outras redes, e a .10 continua alcançando a .31; **é a melhor escolha**.

A rede 192.168.11.0/24 não pode usar Telnet com 192.168.30.0/24 (ACL estendida). O administrador não controla o R3, então a ACL vai no R1, com origem e destino:

- na saída da S0/1/0 do R1, processaria todos os pacotes que saem do R1, inclusive os da rede .10;
- na **entrada da G0/0/1 do R1**, só os pacotes da rede .11 passam pela ACL; **é a melhor escolha**.

### 21.8 Resumo dos Comandos de ACL

| Comando | Função |
| --- | --- |
| `access-list 1–99` | ACL padrão numerada |
| `access-list 100–199` | ACL estendida numerada |
| `ip access-list standard NOME` | ACL padrão nomeada |
| `ip access-list extended NOME` | ACL estendida nomeada |
| `ip access-group ... in/out` | Aplica na interface |
| `access-class ... in` | Aplica nas linhas VTY |
| `show access-lists` | Mostra as ACLs e os contadores |

## 22. Mitigação de Ataques com ACLs e ACLs IPv6

As ACLs também são ferramentas de defesa: bloqueiam endereços falsificados, limitam os serviços expostos e controlam o ICMP.

### 22.1 Bloqueio de Endereços Falsificados

A maioria dos ataques usa algum tipo de falsificação. Na **falsificação de IP** (*IP spoofing*), o atacante foge do processo normal de criação dos pacotes e **coloca um cabeçalho IP com um endereço de origem falso**, o que esconde sua identidade.

A interface voltada para a internet **nunca deve aceitar pacotes com estes endereços de origem**:

- todos zeros (0.0.0.0) e broadcast (255.255.255.255, o endereço de "todos");
- host local, o *loopback* (127.0.0.0/8, endereço que o computador usa para falar consigo mesmo);
- APIPA (169.254.0.0/16), criado pelo computador quando não recebe IP;
- privados reservados pela RFC 1918 (10.0.0.0/8, 172.16.0.0/12 e 192.168.0.0/16);
- multicast (224.0.0.0/4, endereços de grupo, usados para enviar a vários destinos ao mesmo tempo).

Nenhum desses endereços pode ser a origem legítima de um pacote vindo da internet; se aparecer, é falsificação.

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

**Observação:** o exemplo do curso não tem a última linha, sem a qual todo o tráfego seria bloqueado.

A interface da rede local **só deve aceitar pacotes cuja origem seja a própria rede local**. Exemplo: `access-list 105 permit ip 192.168.1.0 0.0.0.255 any`.

### 22.2 Liberação Apenas dos Serviços Necessários

Uma estratégia eficaz é **permitir explicitamente só alguns tipos de tráfego** pelo firewall, aqueles dos serviços que realmente são usados: DNS, **SMTP** (*Simple Mail Transfer Protocol*, o envio de e-mails) e FTP para os servidores públicos. Também é comum liberar o acesso remoto dos administradores, e o roteador pode precisar de SSH, syslog (envio de registros de eventos a um servidor) e SNMP (ver item 15.4). Esses serviços são úteis, mas **precisam ser controlados e monitorados**, porque sua exploração abre vulnerabilidades.

```
access-list 180 permit udp any host 192.168.20.2 eq domain
access-list 180 permit tcp any host 192.168.20.2 eq smtp
access-list 180 permit tcp any host 192.168.20.2 eq ftp
access-list 180 permit tcp host 200.5.5.5 host 10.0.1.1 eq 22
```

### 22.3 Controle do ICMP

O **ICMP** envia mensagens de erro e de teste, como as do ping. Os atacantes usam o **echo** (a mensagem enviada pelo ping) para descobrir hosts e para inundações (enviar tantos pings que o alvo não dá conta), e o **redirect** (mensagem que manda o host usar outro roteador) para alterar a tabela de roteamento dos hosts. Por isso, **echo e redirect devem ser bloqueados na entrada**.

Algumas mensagens ICMP são necessárias para a rede funcionar:

| Sentido | Mensagem | Para que serve |
| --- | --- | --- |
| Entrando na rede | echo-reply | Deixa os usuários pingarem hosts externos |
| Entrando na rede | source-quench | Pede ao remetente que diminua a taxa de tráfego |
| Entrando na rede | unreachable | Gerada para pacotes negados por uma ACL |
| Saindo da rede | echo | Deixa os usuários pingarem hosts externos |
| Saindo da rede | parameter-problem | Avisa o host sobre problemas no cabeçalho do pacote |
| Saindo da rede | packet-too-big | Permite descobrir a **MTU** (*Maximum Transmission Unit*, o maior tamanho de pacote que um caminho aceita) |
| Saindo da rede | source-quench | Reduz o tráfego quando necessário |

Como regra, **todos os outros tipos de ICMP de saída são bloqueados**.

```
access-list 112 permit icmp any any echo-reply
access-list 112 permit icmp any any source-quench
access-list 112 permit icmp any any unreachable
access-list 112 deny icmp any any
access-list 112 permit ip any any
```

### 22.4 Proteção do SNMP

O **SNMP** e outros protocolos de gerenciamento são úteis para monitorar e gerenciar os equipamentos à distância. Se ele for necessário, ACLs nas interfaces filtram os pacotes SNMP de sistemas não autorizados, mas um pacote com endereço falsificado e permitido pela ACL ainda passa. O mais eficaz é **desativar o SNMP quando ele não for necessário**, com `no snmp-server`.

### 22.5 Riscos da Transição para o IPv6

Muitas redes estão migrando para o **IPv6**, a versão nova do protocolo IP, com endereços de 128 bits escritos em hexadecimal (como 2001:db8::1), em parte porque os endereços IPv4 se esgotaram e pelas fraquezas do IPv4, e os ataques ao IPv6 crescem junto. O IPv4 não vai sumir de uma hora para outra: os dois vão coexistir até o IPv6 substituí-lo aos poucos, e essa convivência abre brechas de segurança.

Na **pilha dupla** (*dual stack*), o dispositivo tem **conectividade IPv4 e IPv6 ao mesmo tempo**. Os atacantes usam o IPv4 para explorar o IPv6, e um firewall só de IPv4 não enxerga o tráfego IPv6.

Um exemplo de ataque usa o **Teredo**, técnica que dá IPv6 a hosts atrás de um NAT IPv4 (a tradução que faz vários endereços internos saírem com um único endereço público), **encapsulando o IPv6 dentro de pacotes UDP IPv4**:

1. o atacante envia anúncios de roteador IPv6 falsos (mensagens que informam aos hosts o prefixo e o gateway);
2. os hosts se configuram com IPv6 sem ninguém perceber;
3. o firewall IPv4 só vê UDP comum, e o atacante avança.

É preciso uma estratégia contra os ataques à infraestrutura e aos protocolos IPv6, que inclua **filtrar na borda** com técnicas como as ACLs IPv6.

### 22.6 ACLs IPv6

As ACLs IPv6 têm diferenças importantes:

- **não existe ACL IPv6 padrão**: todas são nomeadas e parecidas com a estendida;
- são criadas com `ipv6 access-list NOME`;
- são aplicadas com `ipv6 traffic-filter NOME {in | out}`.

| Parâmetro | Função |
| --- | --- |
| deny / permit | Recusa ou permite o pacote |
| prefixo/tamanho de origem e de destino | A rede IPv6 ou a classe de redes a filtrar |
| any | Abreviação de ::/0; corresponde a todos os endereços |
| host | Um único endereço IPv6 de origem ou destino |
| operador e porta | Opcional; compara portas com lt, gt, eq, neq e **range** (intervalo); porta pelo número ou nome |
| dscp | Opcional; compara o valor DSCP (*Differentiated Services Code Point*, a marcação de prioridade do pacote, usada pela QoS) com o campo Traffic Class do cabeçalho |
| fragments | Opcional; vale para pacotes grandes que foram divididos em pedaços (fragmentos): corresponde aos fragmentos que não são o primeiro e aos primeiros fragmentos sem informação da camada 4; só vale sem operador e porta |
| log / log-input | Opcional; envia uma mensagem ao console (a tela de administração do roteador); o log-input inclui a interface de entrada |
| sequence | Opcional; número de sequência da instrução, de 1 a 4.294.967.295 |
| time-range | Opcional; período em que a instrução vale, definido pelos comandos time-range e absolute ou periodic |

Elas terminam com três entradas implícitas: `permit icmp any any nd-na`, `permit icmp any any nd-ns` e `deny ipv6 any any`. As duas primeiras permitem as mensagens de vizinho do **NDP** (*Neighbor Discovery Protocol*), que no IPv6 faz o papel do **ARP** do IPv4: descobrir o endereço físico (MAC) de um vizinho a partir do endereço IP. O **nd-ns** (*neighbor solicitation*) é a pergunta "quem tem este IP?", e o **nd-na** (*neighbor advertisement*) é a resposta.

**Importante:** um `deny ipv6 any any` escrito sem antes permitir nd-na e nd-ns faz o **NDP parar de funcionar**.

| Característica | ACL IPv4 | ACL IPv6 |
| --- | --- | --- |
| Tipos | Padrão e estendida | Só um tipo |
| Identificação | Número ou nome | Só nome |
| Aplicação | `ip access-group` | `ipv6 traffic-filter` |
| Final implícito | Nega tudo | Permite nd-na e nd-ns e nega o resto |

## 23. Tecnologias de Firewall

A ACL filtra pacote por pacote. O **firewall** vai além: é um sistema ou grupo de sistemas que **aplica uma política de controle de acesso entre redes** com níveis de confiança diferentes.

Exemplo de operação: o firewall deixa chegar da internet o tráfego para os servidores web, FTP, SMTP e IMAP, mas nega o tráfego de entrada com endereços iguais aos internos (sinal de falsificação, item 22.1), o *echo request* do ICMP (o ping), as consultas ao Active Directory e ao SQL Server (o banco de dados da Microsoft) e as mensagens de broadcast da rede Windows interna, que só devem circular dentro da empresa.

### 23.1 Características do Firewall

Todo firewall:

- é resistente a ataques de rede;
- é o **único ponto de trânsito** entre a rede interna e a externa, porque todo o tráfego passa por ele;
- aplica a política de controle de acesso.

Seus benefícios são:

- não expor hosts, recursos e aplicativos sensíveis a usuários não confiáveis;
- sanear o fluxo dos protocolos, impedindo que suas falhas sejam exploradas;
- bloquear dados maliciosos de servidores e clientes;
- simplificar o gerenciamento, concentrando o controle de acesso em poucos equipamentos.

Suas limitações são:

- mal configurado, tem consequências graves, como virar um **ponto único de falha** (ver item 18.1);
- os dados de muitos aplicativos não passam por ele com segurança;
- usuários podem procurar formas de contorná-lo para receber material bloqueado, o que expõe a rede;
- pode reduzir o desempenho;
- tráfego não autorizado pode passar encapsulado ou escondido em tráfego legítimo.

Conhecer os tipos e as capacidades de cada um permite usar o firewall certo em cada situação.

### 23.2 Tipos de Firewall

Os firewalls se dividem em quatro tipos principais:

- **filtragem de pacotes** (sem estado): normalmente parte de um firewall de roteador; analisa IPs, portas e protocolo nas camadas 3 e 4, com uma consulta simples a uma tabela de políticas; exemplo: bloquear a porta 25 (SMTP) de uma estação para que ela não espalhe um vírus de e-mail;
- **com estado** (*stateful*): **o mais versátil e o mais comum**; filtra com as informações de conexão de uma **tabela de estado**, onde anota cada conversa aberta de dentro para fora (quem, com quem, por qual porta) e só deixa voltar o que corresponde a uma delas; analisa as camadas 3, 4 e 5 (a camada 5, de sessão, controla o início e o fim das conversas);
- **gateway de aplicação** (*proxy*): filtra nas camadas 3, 4, 5 e 7 (a camada de aplicação, onde estão o conteúdo do HTTP, do e-mail etc.), quase todo em software; o cliente se conecta ao proxy, e **o proxy se conecta ao servidor em nome do cliente**, de modo que o servidor só enxerga o proxy;
- **NGFW** (*Next-Generation Firewall* — firewall de última geração): vai além do com estado, com prevenção de intrusão integrada (o IPS, que detecta e bloqueia ataques conhecidos), **reconhecimento e controle de aplicativos** para ver e bloquear os arriscados (por exemplo, liberar o WhatsApp e bloquear jogos), atualização constante com informações sobre novas ameaças e técnicas contra ameaças em evolução.

Também existem o firewall **baseado em host**, um PC ou servidor com software de firewall; o **transparente**, que fica no meio do cabo, de forma invisível para a rede, e filtra o tráfego que passa entre duas interfaces sem ter endereço IP próprio; e o **híbrido**, que combina tipos, como o firewall de inspeção de aplicativos, que une o com estado e o gateway de aplicação.

| Tipo | Camadas analisadas | Como decide |
| --- | --- | --- |
| Filtragem de pacotes | 3 e 4 | Regras fixas, pacote por pacote |
| Com estado | 3, 4 e 5 | Regras + tabela de conexões |
| Gateway de aplicação | 3, 4, 5 e 7 | Intermedia a conexão |
| NGFW | Até a 7 | Estado + aplicativos + prevenção de intrusão |

### 23.3 Firewall de Filtragem de Pacotes

Vantagens:

- regras simples de permitir ou negar;
- **baixo impacto no desempenho**;
- fácil de implementar e disponível na maioria dos roteadores;
- dá um nível inicial de segurança na camada de rede;
- faz quase tudo o que um firewall caro faz, a um custo muito menor.

Não é uma solução completa, mas é parte importante da política de firewall.

Desvantagens:

- é enganado pela falsificação de IP: o atacante envia pacotes que atendem aos critérios da ACL;
- filtra mal pacotes fragmentados (divididos em pedaços): o cabeçalho TCP, com as portas, vai só no primeiro fragmento, e os seguintes passam sem condição;
- ACLs complexas são difíceis de implementar e manter;
- não filtra bem serviços com **negociação dinâmica de portas** (aplicativos, como o FTP e as chamadas de vídeo, que combinam na hora uma porta nova para cada conexão) sem abrir toda uma faixa de portas;
- **não guarda estado**: analisa cada pacote isoladamente, sem o contexto da conexão.

### 23.4 Firewall com Estado

| Benefícios | Limitações |
| --- | --- |
| **Principal meio de defesa**, filtrando o tráfego indesejado | **Não inspeciona a camada de aplicação**, como o conteúdo de uma conexão HTTP |
| Filtragem mais rigorosa que a de pacotes | Acompanha mal o UDP e o ICMP, que não geram informações de conexão |
| Desempenho melhor que o do filtro de pacotes e do proxy | Tem dificuldade com a negociação dinâmica de portas, quando um aplicativo abre várias conexões |
| **Defende contra falsificação e DoS**, conferindo se o pacote pertence a uma conexão existente | Não autentica usuários |
| Logs mais ricos |  |

### 23.5 Firewalls no Projeto de Rede

As arquiteturas de segurança definem os limites do tráfego que entra e sai. Três projetos são comuns: privado e público, DMZ (ver item 16.2) e firewall de política baseada em zona (ZPF), visto na próxima seção.

Com **duas interfaces**, o firewall separa a rede privada, confiável, da pública, não confiável:

- privada → pública: permitido e inspecionado, e as respostas associadas voltam;
- pública → privada: geralmente bloqueado.

Com a DMZ, o firewall passa a ter **três interfaces**:

| Origem → Destino | Tratamento |
| --- | --- |
| Privada → pública ou DMZ | Inspecionado, com pouca ou nenhuma restrição; as respostas voltam |
| DMZ → privada | Bloqueado |
| DMZ → pública | Permitido seletivamente |
| Pública → DMZ | Permitido seletivamente e inspecionado (e-mail, DNS, HTTP, HTTPS); as respostas da DMZ voltam dinamicamente |
| Pública → privada | Bloqueado |

![Com a DMZ, o firewall tem três interfaces e trata de forma diferente cada sentido do tráfego](img/defesa/def_dmz.png){width=6in}

### 23.6 Defesa em Camadas com Firewalls

A defesa em camadas combina **tipos diferentes de firewall** para dar profundidade à segurança. Ela cobre quatro áreas:

- **núcleo da rede**: protege contra malware e anomalias de tráfego, impõe as políticas e garante a sobrevivência da rede;
- **perímetro**: protege os limites entre as zonas;
- **comunicações**: protege a informação enquanto ela trafega, com criptografia e VPNs;
- **endpoints** (os aparelhos dos usuários, como computadores e celulares): identidade e conformidade dos dispositivos com a política.

As políticas valem entre as camadas e dentro delas, e esses **pontos de aplicação da política** decidem se o tráfego segue ou é descartado. Na **sub-rede rastreada** (*screened subnet*), o tráfego da rede não confiável passa por várias barreiras:

Internet → Roteador de borda → Firewall ou host bastião → Roteador interno → Host de destino

Primeiro, encontra o filtro de pacotes do roteador de borda; se permitido, vai ao firewall ou ao **host bastião**, que aplica mais regras e descarta pacotes suspeitos; depois, passa pelo roteador interno. Só chega ao host interno quem passa por todos os pontos. O host bastião é um computador **reforçado para resistir a ataques**, normalmente na DMZ.

### 23.7 Limites e Boas Práticas

A defesa em camadas sozinha não basta. O firewall:

- normalmente não impede intrusões de hosts da mesma rede ou zona;
- não protege contra pontos de acesso sem fio não autorizados;
- não substitui o backup e a recuperação de desastres;
- não substitui administradores e usuários bem informados.

As boas práticas, ponto de partida para a política de firewall, são:

- posicionar firewalls nos limites de segurança, sem depender só deles;
- **negar todo o tráfego por padrão** e permitir só os serviços necessários;
- controlar o acesso físico ao firewall;
- monitorar os logs regularmente;
- fazer gerenciamento de mudanças na configuração (toda alteração é registrada, aprovada e testada antes de entrar em vigor);
- lembrar que o firewall protege principalmente contra ataques técnicos vindos de fora.

## 24. Firewall de Política Baseada em Zona (ZPF)

Os roteadores Cisco também funcionam como firewall com estado (ver item 23.2), em dois modelos:

- **clássico**: a política é aplicada em cada interface, com o comando `ip inspect`;
- **ZPF** (*Zone-Based Policy Firewall*): as interfaces formam zonas de segurança, e a política é aplicada **ao tráfego que passa de uma zona para outra**; é o substituto flexível e poderoso do clássico.

As principais motivações para migrar ao ZPF são a **estrutura**, útil para documentar e comunicar, e a **facilidade de uso**, que aproxima a segurança de mais profissionais.

### 24.1 Zonas de Segurança

Uma **zona** é um **grupo de uma ou mais interfaces com funções e necessidades de segurança semelhantes**, como privada, pública e DMZ.

As regras básicas são:

- **mesma zona** → o tráfego passa livremente;
- **zonas diferentes** → o tráfego é **bloqueado**, a menos que uma política o permita.

Uma interface nova colocada em uma zona já segue as regras dela: os hosts ligados a ela trocam tráfego livremente com os das outras interfaces da mesma zona. Uma rede simples tem três zonas: privada, pública e DMZ.

A **zona self** é **o próprio roteador**, com todos os endereços IP das suas interfaces. Ela trata o tráfego que nasce no roteador ou é endereçado a ele, como o de gerenciamento (SSH, SNMP) e o de controle (protocolos de roteamento). Por padrão, esse tráfego passa; só é filtrado se houver um par de zonas com a self **e** uma política:

| Origem | Destino | Par de zonas? | Política? | Resultado |
| --- | --- | --- | --- | --- |
| Zona self | Outra zona | Não | — | Passa |
| Zona self | Outra zona | Sim | Não | Passa |
| Zona self | Outra zona | Sim | Sim | Inspeciona |
| Outra zona | Zona self | Não | — | Passa |
| Outra zona | Zona self | Sim | Não | Passa |
| Outra zona | Zona self | Sim | Sim | Inspeciona |

### 24.2 Benefícios do ZPF

Seus benefícios são:

- não depende de ACLs;
- a postura padrão é **bloquear tudo o que não for explicitamente permitido**;
- as políticas são fáceis de ler e de corrigir com a **C3PL** (*Cisco Common Classification Policy Language*), um método estruturado de criar políticas por eventos, condições e ações; isso dá escalabilidade, porque uma política vale para todo um tipo de tráfego, sem várias ACLs e inspeções;
- interfaces físicas e virtuais podem ser agrupadas em zonas;
- cada política vale em **um único sentido** entre duas zonas.

Os dois modelos podem estar ativos no mesmo roteador, mas **não na mesma interface**: uma interface não pode ser membro de zona e ter a inspeção do modelo clássico (`ip inspect`) ao mesmo tempo.

### 24.3 Projeto do ZPF

1. **determinar as zonas**: separar a rede em zonas, que são as **fronteiras de segurança**; ao cruzar para outra zona, o tráfego passa pelas restrições da política; exemplo: a rede pública é uma zona, e a interna, outra;
2. **estabelecer as políticas entre as zonas**: para cada **par de zonas** (*zone pair*), origem → destino, definir as sessões que os clientes da origem podem pedir aos servidores do destino, em geral TCP e UDP, mas também ICMP, como o echo; para tráfego sem sessão, definir os fluxos de ida e de volta; as políticas são unidirecionais;
3. **projetar a infraestrutura física**, considerando segurança e disponibilidade: quantos equipamentos entre as zonas mais e menos seguras e quais redundantes;
4. **identificar subconjuntos nas zonas e juntar os requisitos de tráfego** de cada firewall, já que várias zonas podem chegar indiretamente a uma só interface (tema fora do escopo do curso).

Exemplos de projeto: LAN para a internet, firewall com servidores públicos, firewalls redundantes e firewall complexo.

### 24.4 Ações do ZPF

As políticas definidas pelo usuário agem sobre o tráfego que vai de uma zona de origem a uma de destino:

- **Inspect**: inspeção com estado do Cisco IOS; para o TCP e o UDP que vai da privada à pública, o roteador guarda as informações da sessão e **permite automaticamente as respostas**;
- **Drop**: como o deny de uma ACL; é a ação padrão, e a opção log registra os pacotes descartados;
- **Pass**: como o permit de uma ACL, **sem estado e em um único sentido**; o retorno exige outra política; é ideal para protocolos seguros e previsíveis, como o IPsec, mas a maior parte do tráfego de aplicativos fica melhor com o inspect.

O Drop descarta em silêncio, **sem enviar a mensagem ICMP de destino inalcançável**, diferentemente da ACL.

### 24.5 Regras para o Tráfego que Atravessa o Roteador

| Interface de origem em zona? | Interface de destino em zona? | Situação | Resultado |
| --- | --- | --- | --- |
| Não | Não | Nenhuma usa ZPF | Passa |
| Sim | Não | Uma só está em zona | Descarta |
| Não | Sim | Uma só está em zona | Descarta |
| Sim | Sim | Mesma zona | Passa |
| Sim | Sim | Zonas diferentes, sem par ou sem política | Descarta |
| Sim | Sim | Zonas diferentes, com par e política | Inspeciona, permite ou descarta conforme a política |

**Observação:** no curso, o caso "par sem política" aparece como "Passa"; segundo a documentação da Cisco, o tráfego é descartado.

**Importante:** o tráfego **nunca flui entre uma interface que está em zona e outra que não está**.

### 24.6 Configuração do ZPF

A configuração tem cinco etapas. A sequência não é obrigatória, mas algumas dependem de outras: o class-map vem antes do policy-map, e o policy-map antes do zone-pair:

Zonas → class-map → policy-map → zone-pair → Interfaces nas zonas

#### 24.6.1 Exemplo Resolvido: Rede Privada Acessando a Web

A interface GigabitEthernet0/0 fica na zona privada e a Serial0/0/0, na pública.

1. Criar as zonas. Antes, responder: quais interfaces entram nas zonas, qual o nome de cada zona e que tráfego é necessário entre elas, em que sentido. No exemplo, há duas interfaces, duas zonas e tráfego em um só sentido; o que vem da zona pública não é permitido.

```
zone security PRIVATE
zone security PUBLIC
```

2. Identificar o tráfego com um **class-map** (mapa de classe, a "lista" que diz qual tráfego interessa), que separa um conjunto de pacotes pelo conteúdo, com condições de correspondência, para depois aplicar uma ação. **match-any** exige **pelo menos um** critério; **match-all**, **todos**. Os critérios podem ser `match access-group` (uma ACL, pelo número ou nome), `match protocol` (um protocolo) ou `match class-map` (outro class-map). Ao permitir o HTTP, recomenda-se incluir também o HTTPS e o DNS:

```
class-map type inspect match-any HTTP-TRAFFIC
 match protocol http
 match protocol https
 match protocol dns
```

3. Definir a ação com um **policy-map** (mapa de política, que diz o que fazer com esse tráfego), associado a uma classe de tráfego. O `inspect` faz o R1 guardar o estado de todo o tráfego da classe:

```
policy-map type inspect PRIV-TO-PUB-POLICY
 class type inspect HTTP-TRAFFIC
  inspect
```

4. Criar o par de zonas, com `source` (zona de origem), `destination` (zona de destino) ou `self` (o próprio roteador), e anexar o policy-map com `service-policy type inspect`:

```
zone-pair security PRIV-PUB source PRIVATE destination PUBLIC
 service-policy type inspect PRIV-TO-PUB-POLICY
```

5. Colocar as interfaces nas zonas. A política associada vale **imediatamente**; se ainda não houver política para a zona, **todo o tráfego de trânsito é descartado**:

```
interface GigabitEthernet0/0
 zone-member security PRIVATE
interface Serial0/0/0
 zone-member security PUBLIC
```

Resultado: o tráfego web da zona privada é inspecionado, e da pública **só entram as respostas das sessões abertas pela zona privada**.

### 24.7 Verificação e Cuidados

Ao final de todo policy-map, o IOS aplica um **drop explícito** na `class class-default`, como a negação implícita das ACLs; outros class-maps também podem descartar tráfego indesejado.

Na running-config, aparece primeiro o class-map, depois o policy-map que o usa, a `class class-default` que descarta o resto, as zonas, o par com a service-policy e, por fim, as interfaces nas zonas.

Os comandos `show zone security`, `show zone-pair security` e `show policy-map type inspect zone-pair sessions` mostram as zonas, os pares e as sessões inspecionadas. No teste do exemplo, o host 192.168.1.3 da zona privada abriu uma sessão HTTPS com o servidor 10.1.1.2, e um ping do mesmo host gerou quatro pacotes na `class-default`.

Cuidados:

- verificar a conectividade entre os dispositivos **antes** de configurar o firewall e testar depois com ping, Telnet e navegador;
- o ZPF **nunca filtra o tráfego entre interfaces da mesma zona**;
- uma interface pertence a uma única zona; para unir zonas, cria-se uma nova zona com seu policy-map e seus pares;
- para usar o ZPF em uma interface com o firewall clássico, remove-se antes o `ip inspect`;
- o `zone-member` sempre causa uma **interrupção temporária** até o outro membro da zona ser configurado;
- a política padrão entre zonas é descartar tudo o que a service-policy do par não permitir;
- o ZPF só protege o próprio roteador se houver pares com a zona self.

| Característica | Firewall clássico | ZPF |
| --- | --- | --- |
| Onde a política é aplicada | Em cada interface | Entre zonas |
| Depende de ACLs | Sim | Não |
| Interface nova | Precisa de configuração | Herda as regras da zona |

## 25. Virtualização e Computação em Nuvem

Boa parte dos servidores das empresas hoje é virtual ou fica na nuvem. Para proteger esse ambiente, é preciso entender como ele funciona.

### 25.1 Virtualização e Hypervisor

A **virtualização** permite **executar vários computadores virtuais em uma única máquina física**. Cada um é uma **máquina virtual** (**VM**, *Virtual Machine*), com o próprio sistema operacional. Ela reduz o número de máquinas físicas, servidores e estações, necessárias na TI.

O **hypervisor** é o software ou hardware que permite executar vários sistemas operacionais independentes em um sistema físico; é o componente-chave da virtualização. Existem dois métodos:

- **virtualização de hardware** (hypervisor **tipo 1**, *bare metal*): o sistema convidado **roda diretamente sobre o hardware**; exemplos: VMware ESXi e Hyper-V, usados nos data centers;
- **virtualização hospedada** (hypervisor **tipo 2**): **um aplicativo no computador host** (o computador físico, com seu sistema operacional normal, que "hospeda" as VMs) cria VMs feitas só de software; exemplos: VirtualBox e VMware Workstation, usados em computadores pessoais.

A VM **precisa de atualizações e correções como um computador físico**, porque usa um sistema operacional. As VMs compartilham o hardware e rodam com **privilégios muito altos**: comprometer uma VM pode levar a comprometer o host.

### 25.2 Contêineres e Desktops Virtuais

O **contêiner** leva **só o aplicativo e as dependências** (bibliotecas e arquivos de que ele precisa) e, em vez de ter um sistema operacional próprio, **compartilha o núcleo do host**. O núcleo (*kernel*) é a parte central do sistema operacional, que controla o hardware. O **Docker** é uma plataforma aberta que distribui software em contêineres, fáceis de mover, e o **Kubernetes** gerencia muitos ao mesmo tempo. Se um usuário ou aplicativo tiver privilégios elevados no contêiner, o sistema do host pode ser comprometido.

A **VDI** (*Virtual Desktop Infrastructure*) guarda **o ambiente de trabalho do usuário em um servidor remoto**, acessado por um equipamento simples (*thin client*) ou por desktops virtuais. Fica fácil criar, excluir, copiar, arquivar ou baixar configurações pela rede, mas a VDI exige **alta disponibilidade e capacidade de armazenamento**.

| Característica | Máquina virtual | Contêiner |
| --- | --- | --- |
| O que leva | Sistema operacional completo | Só o aplicativo e as dependências |
| Núcleo do sistema | Próprio | Compartilhado com o host |
| Peso | Maior | Menor |

### 25.3 Riscos da Virtualização

- **expansão de VMs** (*VM sprawl*): acúmulo de **VMs esquecidas ou subutilizadas**, sem atualização, que consomem mais recursos e espaço do que o trabalho exige;
- **fuga de VM** (*VM escape*): a VM **rompe o isolamento e passa a interagir com o sistema operacional do host**.

### 25.4 Modelos de Serviço em Nuvem

A **computação em nuvem** oferece **computação, armazenamento, software e servidores pela internet** e leva a parte tecnológica da organização para o provedor. Os modelos de serviço formam o **XaaS** (*Anything as a Service*):

- **SaaS** (*Software as a Service* — software como serviço): acesso a aplicativos e bancos de dados prontos, usados pelo navegador, como o Gmail e o Microsoft 365; o provedor gerencia a infraestrutura, e os dados ficam nos servidores dele;
- **PaaS** (*Platform as a Service* — plataforma como serviço): acesso remoto, por assinatura, às ferramentas e serviços para **desenvolver e publicar aplicativos**;
- **IaaS** (*Infrastructure as a Service* — infraestrutura como serviço): **recursos de computação virtualizados**, como VMs e discos alugados; o provedor hospeda hardware, software, servidores e armazenamento, e o usuário paga uma assinatura.

### 25.5 Modelos de Implantação

| Modelo | Quem usa | Característica principal |
| --- | --- | --- |
| Privada (interna, corporativa) | Uma organização, em plataforma privada | Mais controle dos dados; mais cara pela infraestrutura, manutenção e administração |
| Pública | Clientes de um provedor, em instalação externa | Taxa mensal ou anual; mais barata, mas com menos controle dos dados |
| Híbrida | Uma organização, combinando as duas | Controle dos dados da organização, ainda que hospedados em nuvem pública |
| Comunitária | Mais de uma empresa do mesmo setor, como saúde ou energia | Plataforma compartilhada para as necessidades do setor |

As classificações da nuvem se baseiam na forma de implantação.

### 25.6 Computação em Neblina e de Borda

A explosão da IoT levou às computações em neblina e de borda. Quando milissegundos importam, como em carros autônomos, companhias aéreas e manufatura, o processamento fica perto dos dados:

- **neblina** (*fog*): distribui a computação entre o dispositivo e o data center; os dados são processados em um equipamento intermediário na rede local, o **fog node** (nó de neblina), que recebe os dados dos sensores antes de enviá-los à nuvem;
- **borda** (*edge*): **no próprio dispositivo ou sensor**, sem ir ao data center.

## 26. Segurança na Nuvem

A nuvem sofre as mesmas ameaças das redes físicas e ainda tem ameaças próprias. Com um recurso de nuvem comprometido, o atacante pode:

- usar a capacidade da nuvem para atacar outras organizações;
- hospedar malware em um provedor respeitado, o que faz o conteúdo parecer inofensivo ou legítimo;
- abusar dos serviços para lançar ataques DDoS, hospedar conteúdo pirata, enviar spam (e-mails em massa não solicitados) e fazer campanhas de phishing (mensagens falsas que tentam roubar senhas e dados).

### 26.1 Principais Ameaças

As principais ameaças são:

- **vazamento de dados**: dados confidenciais acessados por alguém não autorizado;
- **configuração incorreta** dos recursos, que os deixa vulneráveis;
- **arquitetura de segurança mal planejada**: a segurança da nuvem privada é da empresa, mas a das nuvens pública, híbrida e comunitária é compartilhada com o provedor, o que gera brechas quando não é bem entendida ou implementada;
- **credenciais de contas comprometidas**: contas e privilégios mal protegidos; na nuvem pública, a **conta de serviço** tem o maior privilégio, e quem a sequestra controla todos os recursos;
- **ameaça interna**: funcionário, prestador ou parceiro que compromete o serviço, por má intenção ou não;
- **interfaces e APIs inseguras**: são os pontos mais expostos à internet e alvo dos atacantes;
- **visibilidade limitada** do uso da nuvem, que dificulta identificar arquivos seguros ou maliciosos.

Uma **API** (*Application Programming Interface*) é o conjunto de comandos pelo qual programas se comunicam com o serviço.

### 26.2 Responsabilidade Compartilhada

Na nuvem pública, a segurança é **dividida entre o cliente e o provedor** (**CSP**, *Cloud Service Provider*). O CSP responde pelos serviços que presta, e o cliente, pelo resto; a divisão varia com o modelo. Quanto mais pronto o serviço, mais responsabilidade fica com o provedor:

| Responsabilidade | No local | IaaS | PaaS | SaaS |
| --- | --- | --- | --- | --- |
| Dados | Cliente | Cliente | Cliente | Cliente |
| Endpoints | Cliente | Cliente | Cliente | Compartilhada |
| Identidades | Cliente | Cliente | Compartilhada | Compartilhada |
| Aplicação | Cliente | Cliente | Compartilhada | CSP |
| Controle de rede | Cliente | Cliente | Compartilhada | CSP |
| Sistema operacional | Cliente | Cliente | CSP | CSP |
| Infraestrutura física | Cliente | CSP | CSP | CSP |

**Importante:** em todos os modelos, **os dados continuam sendo responsabilidade do cliente**.

### 26.3 Domínios da Segurança em Nuvem (CSA)

A **CSA** (*Cloud Security Alliance*) publica o **Guia de Segurança para Áreas de Foco Essenciais na Computação em Nuvem v4**, com boas práticas organizadas em **14 domínios**:

| Domínio | O que trata |
| --- | --- |
| Conceitos e arquiteturas | Terminologia e estruturas lógicas e de arquitetura da nuvem |
| Governança e riscos corporativos | Governança, riscos empresariais, riscos de informação e segurança da informação |
| Questões jurídicas, contratos e descoberta eletrônica | Transferência de dados para a nuvem, contratação de provedores e pedidos de descoberta eletrônica (a entrega de dados digitais exigida pela Justiça em processos) |
| Conformidade e auditoria | Manter, medir e comunicar a conformidade ao migrar do data center para a nuvem |
| Governança da informação | Uso dos dados de acordo com as políticas, os padrões e os objetivos regulatórios, contratuais e comerciais |
| Plano de gerenciamento e continuidade | Proteger o plano de gerenciamento (protocolos e recursos que administram a nuvem) e a continuidade e recuperação de desastres do provedor e do cliente |
| Segurança de infraestrutura | Aspectos próprios da nuvem e a base para operar com segurança |
| Virtualização e contêineres | Proteger a virtualização e os ativos virtuais, base da nuvem |
| Resposta a incidentes | Ciclo de vida da resposta a incidentes (**IR**, *Incident Response*) em ambiente de nuvem |
| Segurança de aplicações | Criar e implantar aplicativos com segurança, principalmente em PaaS e IaaS |
| Segurança e criptografia de dados | Controles de proteção dos dados, baseados em risco, porque não é adequado proteger tudo igual |
| Identidade, direitos e acesso (IAM) | Diferenças entre a identidade na nuvem e a tradicional |
| Segurança como serviço | Serviços de segurança oferecidos pela própria nuvem |
| Tecnologias relacionadas | Tecnologias que dependem da nuvem ou que aparecem muito junto com ela |

Para a CSA, a **criptografia é um dos controles mais importantes** dos dados.

### 26.4 Segurança da Infraestrutura em Nuvem

A infraestrutura é a base sobre a qual os recursos virtualizados (computação, rede e armazenamento) são construídos. Ela tem duas camadas:

- a computação física e lógica (CPU, memória), as redes e o armazenamento que formam a nuvem;
- a infraestrutura virtual que o cliente gerencia, com os recursos que ele usa dos *pools* (os "reservatórios" de processamento, memória e disco que o provedor divide entre os clientes).

Na nuvem, não é possível instalar um equipamento de segurança no meio do cabo. Usam-se **equipamentos virtuais e agentes de software** (pequenos programas de segurança instalados em cada servidor), que precisam ser avaliados com cuidado, porque podem criar gargalos (pontos que deixam tudo lento) e sobrecarregar o processador.

A **SDN** (*Software-Defined Networking* — rede definida por software) traz novos controles de segurança:

- **isolamento fácil**, sem as restrições do hardware, porque **as redes são criadas e separadas por software**;
- firewalls de SDN, chamados de **grupos de segurança**, aplicados com critérios mais flexíveis que os firewalls de hardware.

Os recursos de nuvem formam quatro camadas, **hardware, infraestrutura, plataforma e aplicações**, e cada uma pode receber defesa em profundidade (ver item 2.3). As proteções mais usadas são:

- **segurança integrada** à plataforma; alguns CSPs, por exemplo, já trazem proteção contra DDoS;
- **VPC** (*Virtual Private Cloud* — nuvem privada virtual): sub-redes privadas **isoladas logicamente da internet**;
- **firewalls virtuais**, com regras de permitir e negar e grupos de segurança de host, já que o cliente não configura os firewalls físicos;
- **logs de fluxo**, que monitoram o tráfego de cada interface de rede;
- **VPNs** para o acesso remoto dos usuários e para ligar nuvens entre si ou a nuvem ao data center local;
- **IAM** (*Identity and Access Management* — gerenciamento de identidade e acesso), que gerencia credenciais, autenticação e autorização e é **fundamental contra abusos**.

A **microssegmentação** (ou hipersegregação) usa redes virtuais para criar **muitas redes menores e isoladas**, sem custo de hardware. Como tudo é definido por software, sem os problemas tradicionais de endereçamento, fica viável ter vários ambientes, com controle mais fino do tráfego e dos fluxos.

A **TI invisível** (*shadow IT*) são aplicativos baixados e usados sem autorização. Eles aumentam a produtividade, mas criam brechas e pontos cegos. A resposta são **políticas de segurança claras e conscientização** dos usuários.

### 26.5 Proteção dos Dados na Nuvem

Os dados do cliente precisam de proteção nos três estados: em repouso, em trânsito e em processamento. Os controles mais importantes são a **criptografia** (AES, simétrica, usada pelo governo dos EUA; RSA, Diffie-Hellman (ver item 5.6), ElGamal e ECC, assimétricas) para a confidencialidade e o **hash** (família SHA-2: SHA-224, SHA-256, SHA-384 e SHA-512) para a integridade e a autenticação.

### 26.6 Proteção das Máquinas Virtuais

As VMs, ou instâncias, precisam de correções, atualizações e antimalware como um computador físico, e a nuvem oferece opções extras conforme a plataforma. As medidas principais são:

- **planejar a sub-rede** de cada instância, para que ela tenha só o acesso necessário ao exterior;
- desativar portas e serviços desnecessários;
- desativar as contas padrão e criar contas com boas práticas, como senhas complexas e privilégio mínimo;
- instalar e manter atualizado o antivírus/antimalware;
- instalar firewall de host e sistemas de detecção e de prevenção de intrusão (**IDS**, *Intrusion Detection System*, que alerta, e **IPS**, *Intrusion Prevention System*, que também bloqueia).

Os dois últimos podem ser feitos pelo sistema da VM ou contratados como serviço da plataforma.

Criar instâncias na nuvem é fácil, e é comum criar várias no início de um projeto para testar opções. Sem acompanhamento, elas ficam desatualizadas e vulneráveis, a **expansão de VMs**, e ainda **consomem serviços pagos**, como instâncias, armazenamento e IPs públicos não usados. Por isso, os recursos precisam ser **registrados, monitorados e auditados**.

## 27. Protocolos e Tecnologias no Monitoramento de Segurança

O **monitoramento de segurança** observa o tráfego e os registros da rede para **identificar ataques e comportamentos suspeitos**. Vários protocolos comuns têm recursos que interessam especialmente ao monitoramento, e eles também podem ser mal usados.

### 27.1 Syslog e NTP

O **syslog** é o padrão para **registrar mensagens de eventos** dos equipamentos e enviá-las a um servidor central, na **porta UDP 514**:

Dispositivos → Mensagens de evento → Servidor syslog → Estação de monitoramento

Por ser tão importante, o servidor syslog é alvo dos atacantes. Algumas explorações, como a **retirada de dados** (também chamada de exfiltração: copiar dados da empresa para fora, às escondidas), levam muito tempo, porque o roubo secreto é lento. Para esconder que ela está acontecendo, o atacante ataca o servidor syslog: **adultera ou destrói os logs** ou o software que cria e envia as mensagens. O **syslog-ng** (próxima geração) traz melhorias que evitam algumas dessas explorações.

O **NTP (ver item 15.2.5)** (porta UDP 123) mantém os relógios iguais. Como um ataque deixa rastros em todos os equipamentos do caminho até o alvo, os carimbos de hora são essenciais: só assim é possível **juntar os rastros de um mesmo ataque registrados em equipamentos diferentes**. O atacante pode corromper a hora para esconder os vestígios. Os sistemas NTP também já foram usados para **direcionar ataques DDoS**, explorando falhas de clientes e servidores, o que pode derrubar a disponibilidade da rede.

### 27.2 DNS

O DNS é usado por milhões de pessoas todos os dias, e por isso muitas organizações o protegem menos que outros serviços. Os atacantes aproveitam isso para **esconder outros protocolos dentro do DNS** e escapar dos dispositivos de segurança, falar com o servidor de **comando e controle** (**C&C** ou CnC, o computador que dá ordens ao malware) e retirar dados disfarçados de consultas normais.

Na retirada de dados pelo DNS:

1. o malware codifica os dados roubados, isto é, reescreve-os com outro conjunto de caracteres, em **Base64** (letras, números e alguns símbolos), binário de 8 bits ou hexadecimal, para escapar do **DLP** (*Data Loss Prevention* — prevenção de perda de dados, ferramenta que procura dados confidenciais saindo da rede);
2. coloca os dados no lugar do **subdomínio** (a parte que vem antes do nome principal, como o "www" em www.example.com) de uma consulta a um domínio cujo servidor DNS o atacante controla, como em "dados-codificados.example.com";
3. a consulta chega ao servidor DNS do atacante, que grava o subdomínio e reúne os dados.

O sinal mais claro são **subdomínios muito mais longos que o normal** ou aleatórios, como AW4GCGXHy2UGDG8GCHJVDGVJDC.example.com, principalmente se aumentarem muito na rede. O analista pode montar um modelo matemático do comprimento normal dos subdomínios e comparar com o que observa. Os **logs de proxy DNS** (registros de todas as consultas DNS feitas pela rede) revelam essas consultas, e serviços como o **Cisco Umbrella**, que guarda o histórico das respostas DNS da internet (o DNS passivo), bloqueiam domínios de comando e controle e de exploração.

### 27.3 HTTP e HTTPS

O **HTTP** é o protocolo base da web e trafega **em texto claro**, sem proteção contra alteração ou interceptação, o que ameaça a privacidade, a identidade e a segurança; toda navegação deve ser considerada em risco.

Um ataque comum é a **injeção de iFrame** (quadro em linha). O **iFrame** é um recurso do HTML (a linguagem das páginas web) que exibe uma página dentro de outra, como uma janela. A maioria das ameaças web são scripts (pequenos programas) de malware plantados em servidores, que fazem os navegadores carregar quadros de servidores infectados. O atacante invade um site muito visitado e planta um **quadro invisível**; ao carregar, ele baixa malware, muitas vezes de outro endereço. A filtragem de reputação web da Cisco detecta quando um site tenta entregar conteúdo de um site não confiável, mesmo dentro de um iFrame.

Por isso, muitas empresas adotaram o **HTTPS** ou políticas só de HTTPS. Ele acrescenta a criptografia **SSL/TLS**, que deixa os dados ilegíveis do computador de origem até o servidor. Usando a chave pública, a chave simétrica e o certificado, a conexão ocorre assim:

1. o navegador pede a página com https://;
2. o servidor envia sua chave pública junto com o certificado;
3. o navegador confere se o certificado não venceu, não foi revogado e foi emitido por uma parte confiável;
4. o navegador cria uma chave simétrica e a envia ao servidor, que a descriptografa com a própria chave privada;
5. o servidor criptografa a página com a chave simétrica, e o navegador a descriptografa e mostra ao usuário.

![No HTTPS, a criptografia assimétrica protege a troca da chave simétrica, que depois cifra a página](img/defesa/def_https.png){width=6in}

O HTTPS **protege os dados apenas no caminho**, não o servidor. Para quem monitora, ele complica a inspeção: alguns equipamentos decifram e inspecionam o SSL, mas isso traz problemas de processamento e de privacidade, e as mensagens extras do estabelecimento da conexão complicam as capturas de pacotes.

### 27.4 E-mail e ICMP

- **SMTP** (envio, de um host ao servidor e entre servidores): pouco monitorado, já foi usado por malware para retirar dados; no ataque à **Sony Pictures** em 2014, uma das explorações enviou por SMTP dados de usuários para servidores de comando e controle; o monitoramento detecta esse tráfego pelas características das mensagens;
- **POP3 e IMAP** (recebimento, do servidor ao computador): **trazem o malware até o computador** do usuário; o monitoramento identifica quando um anexo malicioso entrou e qual host foi infectado primeiro, a **análise retrospectiva** acompanha o comportamento do malware a partir daí, e os anexos podem ser recuperados para análise em uma caixa de proteção (*sandbox (ver item 14.1)*).

O ICMP tem usos legítimos, mas também serve para identificar os hosts, a estrutura da rede e os sistemas operacionais. Como a preocupação maior é com o ICMP vindo de fora, o tráfego ICMP de dentro da rede às vezes é ignorado. No **tunelamento ICMP**, o malware **transfere arquivos escondidos em pacotes ICMP** criados de propósito (o pacote parece um ping comum, mas carrega dados); a exploração **LOKI** é um exemplo conhecido, e ferramentas como o Ping Tunnel criam esses túneis.

### 27.5 ACLs, NAT e PAT

Algumas tecnologias de segurança dificultam o próprio monitoramento. As ACLs podem dar uma **falsa sensação de segurança** se houver confiança demais nelas:

- o atacante descobre quais IPs, protocolos e portas a ACL permite, por varredura de portas (ver item 15.1), testes de penetração (ataques simulados) ou outro reconhecimento;
- cria pacotes com IP de origem falsificado;
- os aplicativos podem abrir conexões em portas arbitrárias;
- outros recursos do tráfego podem ser manipulados, como o sinalizador established do TCP;
- uma ACL que deixa voltar mensagens ICMP também deixa passar um túnel ICMP.

Como as regras não antecipam todas as técnicas novas de manipulação, é preciso reforço com análise de comportamento e de contexto, como a dos **firewalls de última geração**, do **AMP** e dos equipamentos de conteúdo de e-mail e web da Cisco.

O **NAT** (*Network Address Translation*) e o **PAT** (*Port Address Translation*) fazem vários endereços internos saírem com um ou mais endereços públicos.

Com o PAT, todos os dispositivos internos aparecem com o mesmo endereço, o que **dificulta saber qual dispositivo interno fez cada pedido**. O problema pesa no **NetFlow**, tecnologia da Cisco que registra os **fluxos** da rede (resumos de quem conversou com quem, por qual porta e quanto): os fluxos são unidirecionais e definidos pelos endereços e portas, e o NAT os **quebra** no gateway, deixando sem informação o que vem depois. A Cisco tem produtos que "costuram" os fluxos mesmo depois da troca de endereços.

### 27.6 Criptografia e Tunelamento

A **VPN** cria um túnel cifrado: um protocolo comum, como o IP, transporta o tráfego criptografado e forma uma conexão virtual ponto a ponto entre redes, ilegível para todos, menos para as pontas da VPN. O malware usa a mesma técnica: um túnel cifrado em um protocolo comum e confiável, entre um host interno e o atacante, para retirar dados, como no caso do DNS.

O tráfego TLS não é inspecionado pelos meios normais e pode esconder malware e comando e controle. As medidas são:

- **posicionar o IPS onde ele veja o tráfego já decifrado**, como depois do ponto em que termina uma VPN site a site (a VPN que liga duas redes, como matriz e filial);
- criar regras que distingam o tráfego SSL do não SSL, e o HTTPS do não HTTPS;
- validar os certificados dos servidores (CRL ou OCSP);
- usar antimalware e filtragem de URL (o endereço de uma página, como https://www.exemplo.com/pagina) no conteúdo HTTPS;
- usar equipamentos que decifram o tráfego e o enviam ao IPS, como o Cisco SSL Appliance.

### 27.7 P2P e Tor

Nas redes **P2P** (*peer-to-peer*), **cada computador atua ao mesmo tempo como cliente e como servidor**. Dar acesso a usuários desconhecidos é sempre uma preocupação. São três tipos:

- **compartilhamento de arquivos**: os arquivos de cada participante ficam disponíveis aos outros; exemplos: Napster, Gnutella e BitTorrent;
- **compartilhamento de processadores**: os participantes doam ciclos de processador para tarefas distribuídas, como pesquisa de câncer e de vida extraterrestre;
- **mensagens instantâneas**: úteis para equipes distribuídas, de preferência em plataformas corporativas, como o Webex Teams, mais seguras que as públicas.

O **Bitcoin** também é P2P: compartilha um banco de dados distribuído (o livro-razão) com os saldos e as transações.

O **P2P de arquivos não deve ser permitido em redes corporativas**: contorna o firewall, conecta-se a vários IPs com portas dinâmicas e espalha malware, porque os arquivos costumam estar infectados e os atacantes colocam malware nos clientes P2P.

O **Tor** é uma plataforma e uma rede de hosts P2P que funcionam como roteadores e permitem **navegar de forma anônima**, com um navegador especial. Ele monta um caminho criptografado em camadas: cada retransmissor "descasca" uma camada, como uma cebola (*onion routing*), e só lê o **próximo salto**. Assim, nenhum dispositivo conhece o caminho inteiro. O Tor é muito usado por criminosos na *dark net* e como canal de comando e controle. Como o destino fica oculto, o tráfego **escapa das listas negras** dos equipamentos de segurança.

### 27.8 Balanceamento de Carga

O **balanceamento de carga** distribui o tráfego entre vários servidores ou caminhos. Na internet, técnicas de DNS mandam o tráfego para recursos com o mesmo nome e vários IPs, às vezes em servidores espalhados geograficamente. Por isso, **uma única transação pode aparecer com vários IPs** nas capturas. Os gerenciadores de balanceamento (**LBM**, *Load Balancing Manager*) também enviam testes de desempenho e de disponibilidade dos caminhos e equipamentos, que podem parecer suspeitos para um analista que não os conheça.

| Protocolo ou tecnologia | Mau uso ou dificuldade |
| --- | --- |
| Syslog e NTP | Logs apagados, hora corrompida e DDoS |
| DNS | Retirada de dados e comando e controle |
| HTTP | Injeção de iFrame |
| HTTPS e VPN | Tráfego cifrado não inspecionado |
| E-mail | Retirada de dados e entrada de malware |
| ICMP | Reconhecimento e tunelamento |
| ACLs | Falsa sensação de segurança |
| NAT e PAT | Dispositivo interno escondido e fluxos quebrados |
| P2P e Tor | Contorno do firewall e anonimato |
| Balanceamento de carga | Vários IPs para a mesma transação |

## 28. Tipos de Dados de Segurança

O analista trabalha com dados do mais resumido ao mais detalhado. Muitos são reunidos pelo **Security Onion**, um conjunto gratuito de ferramentas de **NSM** (*Network Security Monitoring* — monitoramento de segurança de rede). Os dados são de cinco tipos.

### 28.1 Dados de Alerta

Os **dados de alerta** são **mensagens geradas por um IDS (ver item 26.6) ou IPS quando o tráfego viola uma regra** ou corresponde à assinatura de um ataque conhecido. Um IDS de rede (**NIDS**, *Network IDS*, que analisa o tráfego da rede inteira, e não de um só computador), como o **Snort**, vem configurado com regras para explorações conhecidas, e seus alertas podem ser lidos e pesquisados no **Sguil** e no **Squert**, ferramentas do Security Onion.

Exemplo: uma regra do Snort alerta quando qualquer IP da rede recebe de fora um conteúdo com o texto **uid=0 (root)**, a resposta típica de um acesso de administrador em um Linux (no Linux, o administrador se chama root e tem o número de usuário 0). O alerta traz a mensagem "GPL ATTACK\_RESPONSE id check returned root" e o ID da regra, 2100498.

### 28.2 Dados de Sessão

Os **dados de sessão** são o **registro de uma conversa entre dois endpoints**, normalmente um cliente e um servidor, dentro da rede ou na internet. Eles guardam **dados sobre a conversa, e não o conteúdo**: quem falou com quem, quanto e por quanto tempo.

Cada sessão é identificada pela **5-tupla** (um conjunto de cinco informações): IP de origem, IP de destino, porta de origem, porta de destino e protocolo. Os dados também trazem um ID da sessão, a quantidade de dados enviada por cada lado e a duração.

O **Zeek** (antigo Bro) registra esses dados no log de conexões:

| Campo | Significado |
| --- | --- |
| ts | Carimbo de data e hora |
| uid | ID único da sessão |
| id.orig\_h / id.orig\_p | IP e porta do host que iniciou a sessão (origem) |
| id.resp\_h / id.resp\_p | IP e porta do host que respondeu (destino) |
| proto | Protocolo da camada de transporte |
| service | Protocolo da camada de aplicação |
| duration | Duração da sessão |
| orig\_bytes / resp\_bytes | Bytes enviados pela origem e pelo destino |
| orig\_packets / resp\_packets | Pacotes enviados pela origem e pelo destino |

### 28.3 Dados de Transação

Os **dados de transação** são **as mensagens trocadas durante a sessão**, que aparecem nas transcrições das capturas de pacotes e nos logs dos servidores. Exemplo: no download de uma página, o pedido "GET /index.html" e a resposta "200 OK" ficam no log de acesso do servidor ou são registrados por um NIDS como o Zeek.

**Importante:** a **sessão é todo o tráfego** da conversa; a **transação é o próprio pedido** e sua resposta.

### 28.4 Capturas Completas de Pacotes

As **capturas completas de pacotes** guardam **o conteúdo real** do que trafegou: o texto dos e-mails, o HTML das páginas e os arquivos que entram ou saem da rede. O conteúdo extraído pode ser analisado em busca de malware ou de comportamento que viole as políticas. São as mais detalhadas e, por isso, **as que mais exigem armazenamento e recuperação**. Exemplos de ferramentas: **Wireshark** (o analisador de pacotes do item 3.4) e o módulo de análise de rede do **Cisco Prime**, ferramenta de gerenciamento de redes da Cisco.

### 28.5 Dados Estatísticos

Os **dados estatísticos** também tratam do tráfego, mas são **criados a partir da análise dos outros dados**. Deles saem conclusões que descrevem ou preveem o comportamento da rede. A técnica principal é a **linha de base**: as estatísticas definem a variação normal do tráfego, e **diferenças estatisticamente significativas** geram alarme e investigação imediata:

Comportamento normal → Comparação com o atual → Diferença significativa → Alarme

A **NBA** (*Network Behavior Analysis* — análise de comportamento de rede) e a **NBAD** (*Network Behavior Anomaly Detection*) usam essa ideia: analisam a telemetria (dados coletados automaticamente dos equipamentos) **NetFlow** ou **IPFIX** (*IP Flow Information Export*, a versão padrão da IETF do NetFlow 9) com análise preditiva e inteligência artificial para achar incidentes nos dados de sessão.

Um exemplo é o **Cisco Cognitive Threat Analytics**, serviço na nuvem com aprendizado de máquina e modelagem estatística. Ele cria a linha de base do tráfego e encontra atividades maliciosas que passaram pelos controles ou entraram por canais não monitorados, como mídias removíveis, analisando o comportamento de usuários e dispositivos e o tráfego web para descobrir comando e controle e retirada de dados.

| Tipo de dado | O que registra | Nível de detalhe |
| --- | --- | --- |
| Alerta | Violação de uma regra | Resumido |
| Sessão | Quem conversou com quem | Sem conteúdo |
| Transação | Pedidos e respostas | Parte do conteúdo |
| Captura completa | Todo o conteúdo | Máximo |
| Estatístico | Comportamento calculado | Derivado |

## 29. Logs de Hosts, Servidores e Rede, SIEM e SOAR

Um **log** é um **registro dos eventos que acontecem em um dispositivo ou serviço**. O analista precisa ler os principais e reuni-los em um só lugar.

### 29.1 Logs dos Hosts

Um **HIDS** (*Host-based Intrusion Detection System*) é um sistema de detecção de intrusão instalado no próprio computador. Ele detecta intrusões e, na forma de firewall de host, também as impede. Seus logs ficam no host, o que dificulta ver o que acontece na empresa; por isso, devem ir para **servidores centrais de gerenciamento de logs**, por meio de agentes, para serem pesquisados com as ferramentas de NSM. Exemplos: **OSSEC**, de código aberto, com coleta e análise robustas de logs, e **Tripwire**, para Linux. O Windows também tem métodos próprios de coleta, e todos funcionam em empresas grandes.

No Windows, o **Visualizador de Eventos** mostra cinco logs:

- **aplicativos**: eventos registrados pelos programas;
- **sistema**: funcionamento de drivers (os programas que fazem o Windows conversar com cada peça de hardware), processos e hardware;
- **instalação**: instalação de software, inclusive as atualizações do Windows;
- **segurança**: tentativas de logon (a entrada do usuário no sistema) e operações de gerenciamento e acesso a arquivos e objetos; só tem mensagens de **sucesso ou falha de auditoria**;
- **linha de comando**: atacantes e alguns malwares executam comandos na linha de comando em vez da interface gráfica, e esse log dá visibilidade a isso.

O log de segurança é gerado pelo **LSASS** (*Local Security Authority Subsystem Service*, lsass.exe), que também aplica as políticas de segurança do Windows e deve rodar da pasta **System32**.

Um lsass.exe em **outra pasta**, ou disfarçado como **1sass.exe**, **pode ser malware**.

Os eventos do Windows são identificados por **números de ID** e descrições curtas; o site Ultimate Windows Security traz uma enciclopédia desses IDs.

| Tipo de evento | Significado | Exemplo |
| --- | --- | --- |
| Erro | Problema significativo, como perda de dados ou de funções | Um serviço não inicia |
| Aviso | Não é necessariamente grave, mas pode indicar problema futuro; usado quando o aplicativo se recupera sem perda | Pouco espaço em disco |
| Informações | Operação bem-sucedida de um aplicativo, driver ou serviço | Driver de rede carregado |
| Sucesso na auditoria | Acesso de segurança auditado que deu certo | Logon realizado |
| Falha na auditoria | Acesso de segurança auditado que falhou | Acesso negado a uma unidade de rede |

### 29.2 Formato do Syslog

O syslog (ver item 27.1) é um protocolo **cliente/servidor**, definido pela IETF (**RFC 5424**) e aceito por muitos equipamentos. O remetente envia uma mensagem de texto curta, **de menos de 1 KB** (cerca de mil caracteres), ao receptor, chamado de **syslogd**, *syslog daemon* (no Linux, *daemon* é o nome dos programas que rodam em segundo plano) ou servidor syslog, pela **porta UDP 514** ou TCP (normalmente 5000). Salvo quando se acrescenta uma camada de TLS, as mensagens trafegam **em texto claro**.

Toda mensagem syslog tem três partes:

PRI (prioridade) → HEADER (data, hora e equipamento) → MSG (texto)

A **PRI** combina dois valores inteiros:

- **facilidade**: a categoria da fonte que gerou a mensagem (sistema, processo ou aplicativo), que os servidores usam para mandar a mensagem ao arquivo de log certo; as facilidades locais, local0 a local7, têm os números 16 a 23, não têm nome e mudam de sentido conforme o uso; vários sistemas usam as facilidades 9 e 15 para mensagens de relógio;
- **gravidade**: de 0 a 7, e **quanto menor o número, mais grave o evento**.

| Gravidade | Nome | Significado |
| --- | --- | --- |
| 0 | Emergência | Sistema inutilizável |
| 1 | Alerta | Ação imediata necessária |
| 2 | Crítico | Condição crítica, a corrigir imediatamente; falha em um sistema |
| 3 | Erro | Falha não urgente, a resolver em certo prazo |
| 4 | Aviso | Ainda não há erro, mas haverá se nada for feito |
| 5 | Notificação | Evento normal, mas significativo |
| 6 | Informativo | Operação normal |
| 7 | Depuração | Mensagens para desenvolvedores |

**Prioridade = Facilidade × 8 + Gravidade**

O valor da prioridade é o **primeiro do pacote**, entre os sinais < e >.

O **HEADER** traz a data e a hora no formato MMM DD HH:MM:SS e o nome ou IP do equipamento de origem.

**Observação:** um asterisco (\*) ou um ponto antes da data indica **problema com o NTP**.

A **MSG** traz o significado da mensagem. Ela varia entre fabricantes e pode ser personalizada, por isso é **a parte mais útil para o analista**.

#### 29.2.1 Exemplo Resolvido: Cálculo da Prioridade do Syslog

Um firewall envia uma mensagem com a facilidade local4 e gravidade 3 (erro):

| Etapa | Cálculo | Resultado |
| --- | --- | --- |
| Número da local4 | 16 + 4 | 20 |
| Facilidade × 8 | 20 × 8 | 160 |
| Mais a gravidade | 160 + 3 | 163 |
| Início da mensagem | — | <163> |

Nos equipamentos Cisco, a palavra "facilidade" tem dois sentidos: o valor padrão do syslog, usado na PRI (a Cisco usa alguns entre 15 e 23 conforme a plataforma), e a **facilidade da Cisco**, que aparece na parte MSG. Os equipamentos de segurança Cisco enviam eventos e alertas às plataformas de gerenciamento por SNMP ou syslog, e os formatos variam um pouco; o IOS usa **mnemônicos** em vez de IDs de mensagem:

`*Sep 16 08:50:47.359 EDT: %SYS-5-CONFIG_I: Configured from console by con0`

| Trecho | Significado |
| --- | --- |
| SYS | Facilidade no padrão Cisco |
| 5 | Gravidade (notificação) |
| CONFIG\_I | Mnemônico da mensagem |
| Configured from console by con0 | A configuração foi alterada pelo console |

Em um Cisco **ASA** (*Adaptive Security Appliance*, o firewall da Cisco), a mensagem `*Mar 19 11:22:07.289 EDT: %ASA-3-201008: Disallowing new connections` traz a facilidade ASA, a gravidade 3 e o ID 201008. A Cisco publica um dicionário das mensagens syslog do ASA.

### 29.3 Logs dos Servidores

Os servidores de aplicativos, como os de e-mail e web, mantêm **logs de acesso e de erro**, essenciais para o monitoramento. Muitos servidores UNIX e Linux (o UNIX é o sistema que deu origem ao Linux) usam o syslog; outros têm registro próprio, e o conteúdo depende do tipo de servidor. Os **logs de proxy DNS**, que documentam todas as consultas e respostas, são especialmente importantes: mostram quem visitou sites perigosos, a retirada de dados pelo DNS e as conexões com comando e controle.

Dois logs importantes são o de acesso do **Apache** (o servidor web gratuito mais usado no Linux) e o do **IIS** (*Internet Information Services*, o servidor web da Microsoft). Exemplo de log do Apache: `203.0.113.127 – dsmith [10/Oct/2016:10:26:57 -0500] "GET /logo_sm.gif HTTP/1.0" 200 2254`. Ele mostra o IP do cliente, o usuário, a data, o pedido, o código de resposta (200, sucesso) e o tamanho.

### 29.4 Logs da Rede

As principais fontes de registro da rede são:

- **tcpdump**: analisador de pacotes de linha de comando, muito popular; mostra as capturas em tempo real ou as grava em arquivo, com detalhes dos protocolos e do conteúdo; o **Wireshark** é uma interface gráfica construída sobre ele;
- **NetFlow**: protocolo criado pela Cisco para solução de problemas e contabilidade por sessão; registra **informações sobre os fluxos de tráfego, sem o conteúdo**; serve para contabilizar o tráfego, cobrar pelo uso, planejar a rede, segurança, monitoramento e roteamento, e mostra usuários, aplicativos, horários de pico e rotas; o **IPFIX** é a versão padronizada pela IETF; o **nfdump** mostra os dados pela linha de comando, a partir do coletor **nfcapd**;
- **AVC** (*Application Visibility and Control*): reconhece, analisa e controla **mais de mil aplicativos**, como voz e vídeo, e-mail, compartilhamento de arquivos, jogos, P2P e nuvem, usando o **NBAR2** (*Next-Generation Network-Based Application Recognition*); o Cisco Prime apresenta os dados em painéis, e o uso dos aplicativos pode ser controlado por políticas e QoS;
- **filtros de conteúdo** de e-mail e de web: o **Cisco ESA** (*Email Security Appliance*) tem mais de 30 logs (entrega, sistema, antivírus, antispam, listas negras e brancas), guardados em texto e enviados a servidores syslog, FTP ou SCP, além de alertas por e-mail sobre o próprio equipamento; o **Cisco WSA** (*Web Security Appliance*) age como proxy web e registra todas as transações HTTP, com logs detalhados de decisão de ACL, varredura de malware e reputação web;
- **proxies web**, que registram todos os pedidos dos usuários;
- **Cisco Umbrella** (antigo OpenDNS), um DNS hospedado com proteções de segurança;
- **NGFW**, que registra conexões e intrusões.

Um **fluxo** é o conjunto de pacotes em um único sentido com os mesmos atributos, tradicionalmente de 5 a 7: IPs e portas de origem e destino, protocolo, interface e classe de serviço. O fluxo inclui todos os pacotes até a conversa TCP terminar, e os pacotes e bytes são contados. Essas informações ficam condensadas no **cache do NetFlow** (uma área de memória do roteador), o que torna o método escalável; a **IANA** (*Internet Assigned Numbers Authority*, a entidade que controla os números e nomes da internet) lista centenas de atributos de IPFIX, e os 128 primeiros são os mais comuns.

O NetFlow não foi criado para segurança, mas é muito útil na análise de incidentes: monta a **linha do tempo de um ataque**, mostra o comportamento de cada host e acompanha o movimento do atacante de host em host. O **Cisco Stealthwatch** (da Lancope) melhora seu uso no NSM.

Monitorar só pela porta dá pouca informação. O reconhecimento pelo aplicativo mostra **o que o usuário está realmente fazendo**.

#### 29.4.1 Proxies Web e DNS

O **servidor proxy** é um intermediário: o cliente envia o pedido ao proxy, que busca o recurso e o devolve. Os logs dos proxies web e DNS são uma **fonte primária** do monitoramento e mostram:

- quais hosts fazem os pedidos e se os destinos são seguros ou maliciosos;
- que tipo de recurso foi baixado;
- se as respostas vieram de pedidos legítimos ou são explorações disfarçadas de resposta.

O proxy web também inspeciona o tráfego de saída para **DLP**, conferindo se os dados que saem contêm informações confidenciais ou secretas. Exemplos: Squid, CCProxy, Apache Traffic Server e WinGate.

| Campo do log do Squid | Significado |
| --- | --- |
| 1265939281.764 | Hora no formato Unix epoch: segundos contados desde 1º de janeiro de 1970, com os milissegundos depois do ponto |
| 19478 | Duração do pedido e da resposta |
| 172.16.167.228 | IP do cliente |
| TCP\_MISS/200 | Código de resultado do Squid (MISS: o recurso não estava guardado no proxy e foi buscado na internet) e código de status HTTP (200: sucesso) |
| 864 | Bytes entregues |
| GET | Pedido HTTP do cliente |
| http://www.example.com//images/home.png | Endereço do recurso pedido |
| - | Identidade do cliente (RFC 1413), não usada por padrão |
| NONE/- | Consulta ao servidor de cache vizinho |
| image/png | Tipo de conteúdo da resposta, no padrão MIME (aqui, uma imagem PNG) |

Os **proxies abertos**, disponíveis para qualquer usuário da internet, servem para esconder o IP dos atacantes; seus endereços podem entrar em listas negras.

O **Cisco Umbrella** oferece **listas negras, proteção contra phishing e outras proteções de DNS** no próprio serviço, com mais recursos do que a maioria das organizações conseguiria pagar, funcionando como um **superproxy DNS**. A organização assina o serviço em vez de usar os servidores DNS locais ou do provedor, e recebe os logs de acesso DNS:

| Campo | Exemplo | Significado |
| --- | --- | --- |
| Timestamp | 2015-01-16 17:48:41 | Hora do pedido, em UTC (o horário universal, 3 horas à frente de Brasília) |
| Policy Identity | ActiveDirectoryUserName | Primeira identidade que correspondeu ao pedido |
| Identities | ActiveDirectoryUserName, ADSite, Network | Todas as identidades do pedido |
| Internal Ip / External Ip | 10.10.1.100 / 24.123.132.133 | IPs interno e externo que fizeram o pedido |
| Action | Allowed | Se o pedido foi permitido ou bloqueado |
| QueryType | 1 (A) | Tipo de consulta DNS (o tipo A pede o endereço IPv4 de um nome) |
| ResponseCode | NOERROR | Código de retorno do DNS |
| Domain | domain-visited.com. | Domínio pedido |
| Categories | Chat, Photo Sharing, Social Networking | Categorias de segurança ou de conteúdo do destino |

#### 29.4.2 Firewalls de Última Geração

Os **NGFW** levam a segurança além dos IPs e das portas, até a camada de aplicação, e têm **painéis interativos** com relatórios por apontar e clicar, sem precisar de SIEM. A linha da Cisco usa os **Firepower Services**, que reúnem em uma plataforma controle de aplicativos, **NGIPS** (IPS de última geração), filtragem de URL por categoria e reputação e **AMP**, o que reduz custos e simplifica o gerenciamento. O monitoramento é feito no **Visualizador de Eventos**:

| Evento | O que registra |
| --- | --- |
| Conexão | Sessões detectadas pelo NGIPS: hora, IPs de origem e destino e por que foi registrada, como a regra de controle que a tratou |
| Intrusão | Atividades maliciosas nos pacotes que afetem a disponibilidade, a integridade e a confidencialidade de um host |
| Host ou endpoint | Hardware, IP e última presença de um host detectado na rede |
| Descoberta de rede | Mudanças detectadas na rede, conforme as políticas de descoberta |
| Fluxo de rede | Novos eventos de hosts e servidores gerados a partir de registros NetFlow |

### 29.5 SIEM

O **SIEM** (*Security Information and Event Management* — gerenciamento de informações e eventos de segurança) **coleta os logs de toda a rede** e oferece relatórios em tempo real e análises de longo prazo. Ele combina o **SEM** (gerenciamento de eventos de segurança) e o **SIM** (gerenciamento de informações de segurança).

| Função | O que faz |
| --- | --- |
| Coleta | Reúne os logs da organização, com informações forenses e para conformidade |
| Normalização | Converte formatos diferentes para um modelo comum, para analisar eventos relacionados |
| Correlação | Liga eventos de sistemas diferentes e acelera a detecção e a reação |
| Agregação | Junta eventos repetidos e reduz o volume |
| Relatórios | Mostra painéis em tempo real e resumos de longo prazo |
| Conformidade | Gera os relatórios exigidos pelas normas |

Exemplos: **Splunk**, de um parceiro da Cisco, muito usado nos **SOCs** (*Security Operations Centers*, os centros de operações de segurança, onde as equipes monitoram a rede o tempo todo), e o Security Onion com **ELK** (Elasticsearch, Logstash e Kibana).

### 29.6 SOAR

O **SOAR** (*Security Orchestration, Automation and Response*) vai além do SIEM e **automatiza as etapas da resposta a incidentes**. Há muitos bons produtos de segurança, mas eles não conversam entre si e exigem vários painéis para tratar seus muitos alertas. Como faltam profissionais para analisar tanto dado, o SOAR une ferramentas de vários fabricantes. Exemplos: FortiSOAR e Cortex XSOAR.

As **plataformas de segurança integradas** vão além do SIEM e do SOAR e unem tecnologias, processos e pessoas em uma equipe só. Exemplos: Cisco SecureX, Fortinet Security Fabric e Palo Alto Networks Cortex XDR.

SIEM → reúne e correlaciona os eventos; SOAR → responde a eles de forma automatizada.

## 30. Avaliação de Alertas

O cenário de ameaças muda o tempo todo, e os atacantes variam rapidamente suas explorações para escapar da detecção. É impossível prever todas: muitos ataques só são detectados durante ou depois. Por isso, os alertas precisam ser avaliados por analistas, que decidem o que é real.

### 30.1 Security Onion

O **Security Onion** é um pacote gratuito, de código aberto, de ferramentas de NSM que roda em **Ubuntu Linux**. Ele oferece três funções principais: **captura completa de pacotes e tipos de dados, detecção de intrusão de rede e de host, e ferramentas de análise de alertas**. Pode ser instalado de forma autônoma ou como sensor e servidor. Alguns componentes são mantidos por empresas, como a Cisco e a Riverbed, mas distribuídos como código aberto. Às vezes é abreviado como **SO**.

O curso descreve a versão antiga, que usava o Sguil, o CapMe e o ELSA; a versão atual trocou essas ferramentas por novas interfaces.

Dados → Detecção → Análise

- **dados**: pcaps (arquivos de captura de pacotes), dados de conteúdo e de transação, dados de sessão, logs de host, dados de alerta, syslog e metadados;
- **detecção**: as ferramentas da tabela abaixo;
- **análise**: Sguil, com Wireshark e ELSA.

| Ferramenta | Tipo | Função |
| --- | --- | --- |
| CapMe | Aplicativo web | Mostra transcrições pcap geradas pelo tcpflow ou pelo Zeek, uma sessão inteira da camada 4; acessado pelo **ELSA** (*Enterprise Log Search and Archive*) e abre os pcaps no Wireshark |
| Snort | IDS de rede | Detecta ataques por regras e assinaturas; principal fonte de alertas do Sguil; baixa regras novas com o **PulledPork**; os dois são patrocinados pela Cisco |
| Suricata | IDS de rede | Usa assinaturas, como o Snort, e pode bloquear o tráfego em linha (posicionado no caminho dos pacotes); usa **multithreading** (executa várias tarefas em paralelo) em vários núcleos do processador e na GPU e faz bloqueio por reputação |
| Zeek (antigo Bro) | IDS de rede | Analisa o comportamento; em vez de assinaturas, usa **políticas em scripts** que definem o que registrar e quando alertar; pode enviar anexos para análise de malware, bloquear sites maliciosos e desligar um computador que viole as políticas |
| OSSEC | HIDS | Monitora integridade de arquivos, logs, processos e rootkits (malware que se esconde dentro do sistema operacional) do host; exige agente nos computadores Windows; seus alertas aparecem no Sguil e no Kibana |
| Wazuh | HIDS | Substitui o OSSEC; analisa logs, integridade de arquivos, vulnerabilidades e configurações, também com agentes |

Na análise, o **Sguil** é o **ponto de partida da investigação**, um console de alto nível para alertas de várias fontes. Dele, o analista "gira" (*pivot*) para:

- **Kibana**: painel interativo sobre o **Elasticsearch**, para consultar e visualizar os dados de NSM;
- **Wireshark**: abre as capturas completas de pacotes relevantes;
- **Zeek**: inspeciona todo o tráfego de um segmento e permite análise aprofundada.

### 30.2 Alertas no Sguil

Os **alertas** são **mensagens geradas pelas ferramentas de monitoramento** a partir de regras, assinaturas ou anomalias, em várias formas; o syslog, por exemplo, tem classificações de gravidade. O Sguil reúne alertas de várias fontes em uma **fila com carimbo de hora**, onde o analista investiga, classifica, escala (repassa a um analista mais experiente) ou retira cada alerta, em vez de usar um sistema de fluxo de trabalho dedicado como o **RTIR** (*Request Tracker for Incident Response*).

Todo alerta traz, quando disponível, a **5-tupla** (SrcIP, SPort, DstIP, DPort e Pr, o número do protocolo IP), o horário e o equipamento que o gerou. Pode trazer também a decisão de permitir ou negar, dados da carga útil (o conteúdo do pacote, sem os cabeçalhos) ou o hash de um arquivo baixado.

| Campo do Sguil | Significado |
| --- | --- |
| ST | Status; RT é tempo real; a cor indica a prioridade, baseada na categoria do alerta, em quatro níveis (muito baixa, baixa, média e alta), do amarelo-claro ao vermelho |
| CNT | Quantas vezes o evento correlacionado foi detectado para os mesmos IPs de origem e destino; números altos indicam problema ou necessidade de ajustar as assinaturas |
| Sensor | Agente que relatou o evento; os sensores aparecem na aba Agent Status (por exemplo, OSSEC, pcap e Snort, com a interface de monitoramento) |
| Alert ID | Número do sensor e número do evento nesse sensor |
| Date/Time | Horário do evento; nos correlacionados, o do primeiro |
| Event Message | Texto da regra que gerou o alerta; a regra aparece no painel direito com a opção Show Rule |

As condições que disparam um alerta precisam ser predefinidas. Os alertas vêm de:

- **NIDS**: Snort, Zeek e Suricata;
- **HIDS**: OSSEC e Wazuh;
- **gerenciamento e monitoramento de ativos**: **PADS** (*Passive Asset Detection System*);
- **transações HTTP, DNS e TCP**: registradas pelo Zeek e nos pcaps;
- **mensagens syslog**: várias fontes, por isso os formatos variam.

### 30.3 Regras do Snort

O analista precisa entender as regras do Snort, uma das principais fontes de alertas. Uma regra tem **cabeçalho** (ação, protocolo, origem, destino e direção) e **opções** (entre parênteses); o Sguil acrescenta a **localização da regra** (/nsm/server\_data/securityonion/rules/…). Exemplo do curso:

`alert tcp $EXTERNAL_NET any -> $HOME_NET 21 (msg:"ET EXPLOIT VSFTPD backdoor user login smiley"; content:"USER"; sid:2013188; rev:4;)`

| Trecho | Significado |
| --- | --- |
| alert | Ação: gerar um alerta; outras ações são registrar (*log*) e deixar passar (*pass*) |
| tcp | Protocolo |
| `$EXTERNAL_NET any -> $HOME_NET 21` | De qualquer endereço externo para a porta 21 da rede interna; a seta indica a direção |
| msg | Texto do alerta |
| content | Conteúdo procurado no pacote |
| reference | Link opcional com mais informações sobre a regra |
| classtype | Categoria do ataque, com um dos quatro valores de prioridade |
| sid | Identificação única da regra |
| rev | Número da revisão |

As variáveis `$HOME_NET` e `$EXTERNAL_NET`, definidas no arquivo **snort.conf**, representam os endereços internos e externos e dispensam escrever endereços e máscaras em cada regra. A regra também aceita IPs, blocos ou listas, e intervalos de portas com dois-pontos (como 1:1024).

Outro exemplo, do alerta de acesso de administrador: `alert ip any any -> any any (msg:"GPL ATTACK_RESPONSE id check returned root"; content:"uid=0(root)"; … sid:2100498;)`, que alerta quando o texto **uid=0(root)** aparece em qualquer parte do pacote.

As regras vêm de três fontes principais:

- **GPL**: regras antigas, criadas pela Sourcefire (a empresa que criou o Snort, depois comprada pela Cisco) sob a licença de software livre GPLv2, com SIDs até 3464, não certificadas pelo Cisco Talos;
- **ET** (*Emerging Threats*): regras de várias fontes, de código aberto (licença BSD), da Proofpoint;
- **VRT** (*Vulnerability Research Team*): liberadas na hora para assinantes e, 30 dias depois, para usuários registrados; hoje mantidas pelo **Cisco Talos**, a equipe de inteligência de ameaças da Cisco.

O PulledPork baixa as regras do Snort.org automaticamente. Alertas que não vêm do Snort são marcados com tags como OSSEC ou PADS, e é possível criar **regras locais** personalizadas.

### 30.4 Classificação dos Alertas

As regras são **propositalmente conservadoras**: é melhor alertar à toa do que deixar passar um ataque. Os analistas de **nível 1** trabalham nas filas de alertas do Sguil e giram para o Zeek, o Wireshark e o Kibana para confirmar se houve uma exploração.

A classificação vem do **diagnóstico médico**: o médico pode acertar ou errar ao dizer se o paciente está doente, e diagnósticos falsos são caros ou perigosos. O alerta é como o paciente que diz "estou doente", e o analista precisa confirmar se é verdade.

"Positivo" e "negativo" dizem se houve alerta; "verdadeiro" e "falso" dizem se ele estava certo:

|  | Verdadeiro | Falso |
| --- | --- | --- |
| Positivo (houve alerta) | Ocorreu um incidente | Não ocorreu incidente |
| Negativo (não houve alerta) | Não ocorreu incidente | Ocorreu um incidente |

Eventos "verdadeiros" são desejáveis; "falsos" são indesejáveis e potencialmente perigosos.

- **verdadeiro positivo**: a regra funcionou; é o alerta desejado;
- **falso positivo**: alerta por atividade inofensiva (**gatilho benigno**); não esconde ataque, mas custa caro, porque o analista perde tempo investigando alarmes falsos;
- **verdadeiro negativo**: tráfego normal, corretamente ignorado, sem alerta;
- **falso negativo**: **um ataque aconteceu e nenhum alerta foi gerado**; é o caso **mais perigoso**, porque pode passar despercebido por muito tempo, com perdas e danos contínuos.

O que fazer:

- verdadeiro positivo → **encaminhar para o nível superior**, que confirma o incidente e identifica os danos; o pessoal sênior isola os danos, corrige as vulnerabilidades, mitiga a ameaça e cuida dos relatórios;
- excesso de falsos positivos → informar a equipe e **ajustar as regras**; picos também surgem depois de mudanças legítimas na rede ou de regras novas;
- falso negativo descoberto depois → **RSA** (*Retrospective Security Analysis* — análise retrospectiva): **aplicar regras e informações novas aos dados guardados**. Por isso, é importante acompanhar as informações sobre ameaças, avaliar se a rede esteve vulnerável e qual o dano possível, e decidir se bastam novas mitigações ou se é preciso uma análise mais profunda.

### 30.5 Análise Determinística e Probabilística

Técnicas estatísticas avaliam o risco de uma exploração dar certo e ajudam a comparar o custo de mitigar a ameaça com o dano que ela causaria:

- **determinística**: avalia o risco pelo que se sabe da vulnerabilidade; para o ataque dar certo, **todas as etapas anteriores precisam ter dado certo**; toda a informação é conhecida, como as portas padrão; descreve o pior caso; muitos atacantes conhecem o processo, mas não têm habilidade para cumprir cada etapa, o que dá ao analista a chance de detectá-los;
- **probabilística**: usa **estatística para estimar a probabilidade** de a próxima etapa dar certo; as portas só podem ser previstas com certo grau de confiança, como nas explorações com portas dinâmicas, feitas para escapar de firewalls com regras fixas; serve na análise em tempo real, com muitas variáveis, e mostra os caminhos mais prováveis, onde concentrar a atenção.

| Característica | Determinística | Probabilística |
| --- | --- | --- |
| Base | Etapas conhecidas | Estatística |
| Portas | Conhecidas | Previstas com certa confiança |
| Resultado | Pior caso | Caminhos mais prováveis |

## Glossário de Siglas

| Sigla | Nome completo | Significado |
| --- | --- | --- |
| 2FA | Two-Factor Authentication | Autenticação com exatamente dois fatores |
| AAA | Authentication, Authorization and Accounting | Autenticação, autorização e contabilidade dos acessos |
| ABAC | Attribute-Based Access Control | Controle de acesso baseado em atributos |
| ACE | Access Control Entry | Cada linha de permitir ou negar de uma ACL |
| ACK | Acknowledgment | Sinalizador TCP de confirmação de recebimento |
| ACL | Access Control List | Lista de controle de acesso que filtra pacotes |
| ACS | Access Control Server | Servidor central de controle de acesso da Cisco |
| AES | Advanced Encryption Standard | Algoritmo simétrico recomendado, com bloco de 128 bits |
| AMP | Advanced Malware Protection | Proteção avançada contra malware da Cisco |
| AP | Access Point | Ponto de acesso sem fio |
| API | Application Programming Interface | Conjunto de comandos pelo qual programas se comunicam |
| APIPA | Automatic Private IP Addressing | Endereço 169.254.x.x criado pelo computador sem DHCP |
| ARP | Address Resolution Protocol | Descobre o endereço MAC a partir do IP |
| ASA | Adaptive Security Appliance | Firewall da Cisco |
| AUP | Acceptable Use Policy | Política de uso aceitável |
| AVC | Application Visibility and Control | Reconhece e controla aplicativos na rede |
| BYOD | Bring Your Own Device | Uso de aparelhos pessoais no trabalho |
| C&C (CNC) | Command and Control | Servidor que dá ordens a um malware |
| C3PL | Cisco Common Classification Policy Language | Linguagem estruturada de políticas do ZPF |
| CA | Certificate Authority | Autoridade que emite certificados digitais |
| CCMP | Counter Mode with CBC-MAC Protocol | Protocolo de criptografia do WPA2, baseado no AES |
| CER | Crossover Error Rate | Taxa de erro de cruzamento dos sistemas biométricos |
| CFTV | Circuito Fechado de TV | Vigilância por câmeras |
| CFTV (CCTV) | Circuito Fechado de Televisão (Closed-Circuit Television) | Vigilância por câmeras |
| CHAP | Challenge Handshake Authentication Protocol | Autenticação por desafio e resposta com hash |
| CIA (CID) | Confidentiality, Integrity, Availability | Tríade confidencialidade, integridade e disponibilidade |
| COPE | Corporate-Owned, Personally Enabled | Aparelho da empresa com uso pessoal permitido |
| CPU | Central Processing Unit | Processador do equipamento |
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
| DSCP | Differentiated Services Code Point | Valor de classe de tráfego no cabeçalho IP |
| DSS | Digital Signature Standard | Padrão de assinatura digital que usa o DSA |
| EAP | Extensible Authentication Protocol | Estrutura de autenticação usada em redes sem fio e 802.1X |
| ECC | Elliptic Curve Cryptography | Criptografia de curvas elípticas |
| ECDSA | Elliptic Curve Digital Signature Algorithm | Assinatura digital com curvas elípticas |
| EFS | Encrypting File System | Sistema de criptografia de arquivos do Windows |
| ELK | Elasticsearch, Logstash, Kibana | Conjunto de ferramentas para guardar e analisar logs |
| ELSA | Enterprise Log Search and Archive | Busca e arquivo de logs do Security Onion antigo |
| ESA | Email Security Appliance | Filtro de conteúdo de e-mail da Cisco |
| ET | Emerging Threats | Fonte de regras do Snort mantida pela Proofpoint |
| FIPS | Federal Information Processing Standard | Padrão do governo dos EUA para processamento de informações |
| FPGA | Field-Programmable Gate Array | Circuito reprogramável depois de instalado |
| FTP | File Transfer Protocol | Transferência de arquivos, em texto claro |
| FTPS | FTP Secure | FTP protegido por SSL/TLS |
| GLBP | Gateway Load Balancing Protocol | Protocolo de redundância de gateway da Cisco |
| GPL | GNU General Public License | Licença de software livre; também nome de regras antigas do Snort |
| GPS | Global Positioning System | Sistema de posicionamento global por satélites |
| GPU | Graphics Processing Unit | Processador gráfico |
| GSM | Global System for Mobile Communications | Padrão de telefonia celular |
| HIDS | Host-based Intrusion Detection System | Detecção de intrusão instalada no host |
| HMAC | Hash-based Message Authentication Code | Hash com chave secreta, que garante integridade e autenticidade |
| HSRP | Hot Standby Router Protocol | Protocolo de redundância de roteador da Cisco |
| HTTP | Hypertext Transfer Protocol | Protocolo da web, em texto claro |
| HTTPS | HTTP Secure | HTTP protegido por SSL/TLS |
| HVAC | Heating, Ventilation and Air Conditioning | Aquecimento, ventilação e ar-condicionado |
| IaaS | Infrastructure as a Service | Infraestrutura como serviço |
| IAM | Identity and Access Management | Gerenciamento de identidade e acesso |
| IANA | Internet Assigned Numbers Authority | Órgão que registra números e parâmetros da internet |
| ICMP | Internet Control Message Protocol | Mensagens de erro e de teste, como o ping |
| ICS | Industrial Control Systems | Sistemas de controle industrial |
| IdP | Identity Provider | Provedor de identidade, quem autentica o usuário |
| IDS | Intrusion Detection System | Sistema de detecção de intrusão |
| IETF | Internet Engineering Task Force | Órgão que cria os padrões da internet |
| IIS | Internet Information Services | Servidor web da Microsoft |
| IKE | Internet Key Exchange | Troca de chaves nas VPNs IPsec |
| IMAP | Internet Message Access Protocol | Protocolo de recebimento de e-mail |
| INFOSEC | Information Systems Security | Segurança de sistemas de informação |
| IOS | Internetwork Operating System | Sistema operacional dos roteadores e switches Cisco |
| IoT | Internet of Things | Internet das Coisas |
| IP | Internet Protocol | Protocolo de endereçamento e roteamento da internet |
| IPFIX | IP Flow Information Export | Padrão do IETF para registros de fluxo, baseado no NetFlow v9 |
| IPS | Intrusion Prevention System | Sistema de prevenção de intrusão |
| IPsec | IP Security | Conjunto de protocolos que protege o tráfego IP, usado em VPNs |
| IR | Infrared / Incident Response | Infravermelho, comunicação de curto alcance; também, resposta a incidentes |
| ISBN | International Standard Book Number | Número que identifica um livro |
| ITU-T | International Telecommunication Union – Telecommunication Standardization Sector | Órgão de padrões de telecomunicações, autor do X.509 |
| KBA | Knowledge-Based Authentication | Autenticação baseada em conhecimento |
| LAN | Local Area Network | Rede local |
| LBM | Load Balancing Manager | Gerenciador de balanceamento de carga |
| LDAP | Lightweight Directory Access Protocol | Protocolo de consulta a serviços de diretório |
| LGPD | Lei Geral de Proteção de Dados | Lei brasileira de proteção de dados pessoais |
| LSASS | Local Security Authority Subsystem Service | Serviço do Windows que gera o log de segurança |
| LSB | Least Significant Bits | Bits menos significativos, usados na esteganografia |
| LSU | Link-State Update | Atualização de estado do link do OSPF |
| LTE | Long Term Evolution | Padrão de rede celular 4G |
| MAC | Mandatory Access Control | Controle de acesso obrigatório (também: código de autenticação de mensagem; endereço físico) |
| MD5 | Message Digest 5 | Algoritmo de hash de 128 bits, inseguro |
| MDM | Mobile Device Management | Gerenciamento de dispositivos móveis |
| MFA | Multi-Factor Authentication | Autenticação multifator |
| MIC | Message Integrity Check | Verificação de integridade das mensagens no WPA |
| MIME | Multipurpose Internet Mail Extensions | Anexa dados que não são texto ao e-mail |
| MitM | Man-in-the-Middle | Ataque em que o criminoso se coloca entre as duas partes |
| MTU | Maximum Transmission Unit | Maior tamanho de pacote que um link transmite |
| NAC | Network Access Control | Controle de acesso à rede |
| NAT | Network Address Translation | Tradução de endereços de rede |
| NBA | Network Behavior Analysis | Análise de comportamento de rede |
| NBAD | Network Behavior Anomaly Detection | Detecção de anomalias de comportamento de rede |
| NBAR2 | Next-Generation Network-Based Application Recognition | Reconhecimento de aplicativos da Cisco |
| NDP | Neighbor Discovery Protocol | Descoberta de vizinhos no IPv6 |
| NFC | Near-Field Communication | Comunicação por proximidade |
| NGFW | Next-Generation Firewall | Firewall de última geração |
| NGIPS | Next-Generation Intrusion Prevention System | IPS de última geração |
| NIDS | Network-based Intrusion Detection System | Detecção de intrusão na rede |
| NIST | National Institute of Standards and Technology | Instituto de padrões dos EUA |
| NSA | National Security Agency | Agência de segurança nacional dos EUA |
| NSM | Network Security Monitoring | Monitoramento de segurança de rede |
| NTP | Network Time Protocol | Sincroniza os relógios dos dispositivos |
| OAuth | Open Authorization | Permite entrar em um site com a conta de outro serviço, sem entregar a senha |
| OCSP | Online Certificate Status Protocol | Consulta on-line do status de um certificado |
| OSI | Open Systems Interconnection | Modelo de referência em sete camadas |
| OSPF | Open Shortest Path First | Protocolo de roteamento |
| OWASP | Open Web Application Security Project | Organização dedicada à segurança de aplicações web |
| P2P | Peer-to-Peer | Rede em que cada computador é cliente e servidor |
| PaaS | Platform as a Service | Plataforma como serviço |
| PADS | Passive Asset Detection System | Detecção passiva de ativos |
| PAP | Password Authentication Protocol | Autenticação com senha em texto claro |
| PAT | Port Address Translation | NAT com sobrecarga, que usa portas para muitos hosts |
| PEAP | Protected EAP | EAP protegido por túnel TLS |
| PGP | Pretty Good Privacy | Privacidade e autenticação em e-mails |
| PIN | Personal Identification Number | Senha numérica pessoal |
| PKCS | Public-Key Cryptography Standards | Padrões de criptografia de chave pública da RSA Security |
| PKI | Public Key Infrastructure | Infraestrutura de chave pública |
| POP3 | Post Office Protocol 3 | Protocolo de recebimento de e-mail |
| PPP | Point-to-Point Protocol | Protocolo de enlace ponto a ponto |
| PRI | Priority | Parte da mensagem syslog com facilidade e gravidade |
| PSK | Pre-Shared Key | Chave pré-compartilhada |
| QA | Quality Assurance | Garantia de qualidade |
| QoS | Quality of Service | Qualidade de serviço: prioriza certos tipos de tráfego, como a voz |
| RA | Registration Authority | Autoridade de registro, que confere a identidade antes de a CA emitir o certificado |
| RADIUS | Remote Authentication Dial-In User Service | Servidor de autenticação AAA, padrão aberto |
| RAID | Redundant Array of Independent Disks | Conjunto de discos com distribuição e redundância |
| RBAC | Role-Based Access Control | Controle de acesso baseado em funções |
| RC4 | Rivest Cipher 4 | Cifra de fluxo antiga e vulnerável |
| RFC | Request for Comments | Documento que define padrões da internet |
| RFID | Radio-Frequency Identification | Identificação por radiofrequência |
| RGB | Red, Green, Blue | Vermelho, verde e azul, as cores de um pixel |
| RIP | Routing Information Protocol | Protocolo de roteamento |
| RSA | Rivest, Shamir, Adleman | Algoritmo assimétrico (também: análise de segurança retrospectiva) |
| RST | Reset | Sinalizador TCP que encerra uma conexão |
| RTIR | Request Tracker for Incident Response | Sistema de fluxo de trabalho para resposta a incidentes |
| RTOS | Real-Time Operating System | Sistema operacional de tempo real |
| S/MIME | Secure/Multipurpose Internet Mail Extensions | Padrão para assinar e criptografar e-mails |
| SaaS | Software as a Service | Software como serviço |
| SCADA | Supervisory Control and Data Acquisition | Controle de supervisão e aquisição de dados industriais |
| SCP | Secure Copy Protocol | Cópia segura de arquivos sobre SSH |
| SDK | Software Development Kit | Kit de código pronto para desenvolver aplicativos |
| SDN | Software-Defined Networking | Rede definida por software |
| SEAL | Software-Optimized Encryption Algorithm | Cifra de fluxo com chave de 160 bits |
| SEM | Security Event Management | Gerenciamento de eventos de segurança |
| SHA | Secure Hash Algorithm | Família de algoritmos de hash |
| SHS | Secure Hash Standard | Padrão de hash seguro do NIST |
| SIEM | Security Information and Event Management | Gerenciamento de informações e eventos de segurança |
| SIM | Security Information Management | Gerenciamento de informações de segurança |
| SMTP | Simple Mail Transfer Protocol | Protocolo de envio de e-mail |
| SNMP | Simple Network Management Protocol | Gerenciamento e monitoramento de equipamentos de rede |
| SOAR | Security Orchestration, Automation and Response | Orquestração, automação e resposta de segurança |
| SoC | System on Chip | Sistema completo em um único chip |
| SOC | Security Operations Center | Centro de operações de segurança, que monitora a rede o tempo todo |
| SPOF | Single Point of Failure | Ponto único de falha |
| SQL | Structured Query Language | Linguagem de consulta a bancos de dados |
| SSH | Secure Shell | Acesso remoto seguro por linha de comando |
| SSL | Secure Sockets Layer | Protocolo de criptografia antecessor do TLS |
| SSO | Single Sign-On | Logon único |
| STP | Spanning Tree Protocol | Evita loops bloqueando caminhos redundantes entre switches |
| SYN | Synchronize | Sinalizador TCP que inicia uma conexão |
| TAC | Time-based Access Control | Controle de acesso baseado em tempo |
| TACACS+ | Terminal Access Controller Access-Control System Plus | Servidor de autenticação AAA da Cisco |
| TCP | Transmission Control Protocol | Protocolo de transporte orientado à conexão |
| TGT | Ticket-Granting Ticket | Tíquete de concessão de tíquete do Kerberos |
| TI | Tecnologia da Informação | Área responsável pelos sistemas e redes |
| TKIP | Temporal Key Integrity Protocol | Protocolo de criptografia do WPA |
| TLS | Transport Layer Security | Protocolo de criptografia das conexões, sucessor do SSL |
| TSIG | Transaction Signature | Assinatura que autentica as transações entre servidores DNS |
| UAV | Unmanned Aerial Vehicle | Veículo aéreo não tripulado (drone) |
| UDP | User Datagram Protocol | Protocolo de transporte sem conexão |
| UPS | Uninterruptible Power Supply | Nobreak |
| URL | Uniform Resource Locator | Endereço de um recurso na web |
| USB | Universal Serial Bus | Padrão de conexão de dispositivos |
| UTC | Coordinated Universal Time | Tempo universal coordenado |
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
| WPAN | Wireless Personal Area Network | Rede pessoal sem fio |
| WPS | Wi-Fi Protected Setup | Conexão simplificada ao Wi-Fi, vulnerável |
| WSA | Web Security Appliance | Proxy e filtro de conteúdo web da Cisco |
| XaaS | Anything as a Service | Qualquer coisa como serviço |
| XDR | Extended Detection and Response | Detecção e resposta estendidas |
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
