# Defesa de Rede

Nov 4, 2026 · Maria Paula

## 1. Fundamentos da Defesa de Redes

A **defesa de rede** é o conjunto de medidas, tecnologias e processos que **protegem os recursos de uma organização contra ataques**.

Antes de escolher qualquer ferramenta, é preciso saber o que proteger, quais são os pontos fracos e quais perigos existem.

### 1.1 Tríade CIA: Confidencialidade, Integridade e Disponibilidade

A **tríade CIA** (*Confidentiality, Integrity, Availability* — Confidencialidade, Integridade e Disponibilidade) reúne os **três objetivos principais da segurança da informação**. Toda medida de defesa protege pelo menos um deles.

| Objetivo | O que garante | Exemplo de ameaça |
| --- | --- | --- |
| Confidencialidade | Só pessoas autorizadas leem a informação | Funcionário de fora do RH abrindo a folha de pagamento |
| Integridade | A informação está completa e não foi alterada | Valor de uma transferência modificado no caminho |
| Disponibilidade | A informação e os serviços funcionam quando necessários | Servidor do site fora do ar por um ataque |

Em português, também se usa **tríade CID**.

### 1.2 Ativos, Vulnerabilidades e Ameaças

Para se preparar contra ataques, o analista identifica três elementos:

- **ativos**: tudo o que tem valor e deve ser protegido, como servidores, dispositivos e, principalmente, os **dados**;
- **vulnerabilidades**: uma fraqueza em um sistema ou no seu projeto que pode ser explorada;
- **ameaças**: qualquer perigo potencial para um ativo.

Quem explora uma vulnerabilidade é o **agente de ameaça**: um criminoso digital, um funcionário mal-intencionado ou um grupo organizado.

O conjunto dos ativos forma a **superfície de ataque**, isto é, tudo o que pode ser atingido. Ela cresce junto com a organização.

**Importante:** a vulnerabilidade é o **ponto fraco** (uma senha padrão nunca trocada); a ameaça é o **perigo** que se aproveita dele (alguém que tenta entrar com essa senha).

### 1.3 Gerenciamento de Ativos

O **gerenciamento de ativos** consiste em **inventariar todos os ativos e, em seguida, criar e aplicar políticas e procedimentos para protegê-los**.

Cada negócio guarda ativos diferentes, que atraem agentes de ameaça diferentes. Exemplos:

- uma loja guarda dados de cartão de crédito;
- uma empresa de engenharia guarda projetos que interessam à concorrência;
- um banco guarda dados de contas.

### 1.4 Classificação de Ativos

A **classificação de ativos** distribui os recursos em **grupos com características comuns**. As informações mais importantes recebem o nível mais alto de proteção.

O processo ocorre em quatro etapas:

1. determinar a categoria de cada ativo: informação, software, físico ou serviço;
2. identificar o **proprietário** de cada ativo;
3. definir os critérios: confidencialidade, valor, tempo, direitos de acesso e destruição;
4. aplicar um esquema uniforme de classificação.

### 1.5 Padronização de Ativos

Os **padrões de ativos** definem **quais produtos de hardware e software a organização usa e dá suporte**.

Sem padronização, é difícil achar peças de reposição e os custos de manutenção aumentam. Com ela, a troca é rápida e a segurança se mantém.

### 1.6 Ciclo de Vida dos Ativos

Todo ativo passa por um **ciclo de vida**, e precisa ser protegido em todas as etapas:

Aquisição → Implantação → Utilização → Manutenção → Descarte

| Etapa | O que acontece |
| --- | --- |
| Aquisição | O ativo é comprado e entra no inventário |
| Implantação | É montado, testado e etiquetado para rastreamento |
| Utilização | Fase mais longa: recebe atualizações, correções e auditorias |
| Manutenção | É ajustado para prolongar a vida útil |
| Descarte | Os dados são apagados e as peças seguem as regras ambientais |

### 1.7 Identificação de Ameaças e de Vulnerabilidades

A **identificação de ameaças** produz uma **lista das ameaças prováveis para um ambiente específico**. Ela responde a três perguntas:

- quais são as vulnerabilidades do sistema?
- quem pode explorá-las, e para chegar a quais ativos?
- quais são as consequências se isso acontecer?

A **identificação de vulnerabilidades** exige conhecer os aplicativos importantes da rede e as fraquezas deles e do hardware.

#### 1.7.1 Exemplo Resolvido: Ameaças a um Sistema de Banco On-line

Para um banco pela internet, a lista de ameaças incluiria:

- invasão do sistema interno a partir dos servidores expostos à internet;
- roubo de dados de clientes;
- transações falsas, com código alterado ou com PIN e cartão roubados;
- ataque interno (*insider*), feito por um funcionário;
- erros de digitação dos usuários;
- destruição do data center por incêndio ou enchente.

**Observação:** nem toda ameaça é um ataque. Erros e desastres naturais também afetam a integridade e a disponibilidade.

## 2. Defesa em Profundidade

A **defesa em profundidade** é a abordagem que **usa várias camadas de segurança na borda da rede, dentro da rede e nos dispositivos finais**. Assim, a falha de uma proteção não compromete as outras.

### 2.1 Camadas de uma Rede Protegida

Na topologia mais simples, o tráfego da internet atravessa três linhas de defesa até a rede interna (LAN):

Internet → Roteador de borda → Firewall → Roteador interno → Rede interna

| Linha de defesa | Função |
| --- | --- |
| Roteador de borda | Permite ou nega o tráfego e repassa ao firewall o que vai para a rede interna |
| Firewall | Faz uma filtragem adicional e acompanha o estado das conexões |
| Roteador interno | Aplica as regras finais antes de entregar o tráfego |

O **firewall** fica entre redes e decide qual tráfego pode passar. Ele **nega conexões iniciadas na rede externa (não confiável) em direção à rede interna (confiável)**, mas deixa os usuários internos acessarem a internet e receberem as respostas.

Outras camadas comuns são:

- o **IPS** (*Intrusion Prevention System* — sistema de prevenção de intrusão), que identifica e bloqueia ataques no tráfego;
- a **AMP** (*Advanced Malware Protection*), proteção avançada contra malware;
- os filtros de conteúdo web e de e-mail;
- os serviços de identidade e de controle de acesso à rede.

### 2.2 A Cebola e a Alcachofra da Segurança

Duas analogias descrevem a defesa em profundidade.

Na **cebola de segurança**, o atacante precisa **descascar as defesas camada por camada** até chegar aos dados, no centro.

Nas **redes sem fronteiras**, acessadas de celulares, de casa e da nuvem, vale a **alcachofra de segurança**: o atacante **não precisa remover todas as camadas, basta arrancar algumas folhas**. Exemplos de folhas: senhas, bancos de dados e aplicativos web.

| Característica | Cebola | Alcachofra |
| --- | --- | --- |
| Cenário | Rede com perímetro bem definido | Rede sem fronteiras |
| Caminho do atacante | Atravessar todas as camadas | Remover só algumas folhas |

**Observação:** a cebola de segurança é só uma imagem. Não tem relação com o **Security Onion**, um conjunto de ferramentas de monitoramento.

### 2.3 Estratégias de Defesa em Profundidade

As camadas funcionam melhor com cinco estratégias:

| Estratégia | Ideia central | Exemplo |
| --- | --- | --- |
| Sobreposição (camadas) | Várias defesas seguidas | Servidor com senha, em prédio trancado e cercado |
| Limitação | Só o acesso necessário ao trabalho | Documentos sigilosos consultados em sala com câmeras |
| Diversidade | Camadas diferentes entre si | Crachá de um fabricante e leitor de digital de outro |
| Ofuscação | Não revelar detalhes úteis ao atacante | Mensagem de erro sem a versão do sistema |
| Simplicidade | Simples por dentro, complexo por fora | Configuração que a equipe entende e mantém |

Na diversidade, a ideia é que a técnica que vence uma camada não vença as outras.

## 3. Gerenciamento de Operações de Segurança

O **gerenciamento de operações de segurança** reúne os processos do dia a dia que mantêm a rede segura: **controlar as configurações, registrar os eventos e observar o tráfego**.

### 3.1 Gerenciamento de Configuração

O **gerenciamento de configuração** é a **identificação, o controle e a auditoria da implantação de um sistema e de qualquer alteração feita na sua linha de base**.

A **linha de base** (*baseline*) é o conjunto de configurações que serve de **modelo para todos os sistemas semelhantes**. Exemplo: todas as estações Windows saem com os mesmos aplicativos e configurações.

Devem ser documentados, entre outros:

- mapas de rede e diagramas de cabeamento;
- convenções de nomes dos computadores;
- esquema de endereçamento IP.

### 3.2 Reforço do Sistema Operacional

O **reforço** (*hardening*) do sistema operacional é **configurá-lo de forma segura, reduzindo as brechas que um atacante poderia usar**. As principais medidas são:

- configurar logs e auditoria;
- trocar nomes de conta e senhas padrão;
- aplicar políticas de conta;
- controlar o acesso aos arquivos.

### 3.3 Arquivos de Log

Um **log** é o **registro dos eventos que ocorrem em um sistema**. Cada evento vira uma **entrada de log**, e o conjunto delas forma o **arquivo de log**. Exemplos: o log de auditoria, com as tentativas de autenticação, e o log de acesso, com os pedidos a arquivos.

Pelos logs, descobre-se **como um ataque aconteceu e se as defesas funcionaram**. O gerenciamento de logs define o que fazer em cada etapa:

Gerar → Transmitir → Armazenar → Analisar → Descartar

| Fonte | O que registra | Para que serve |
| --- | --- | --- |
| Sistema operacional | Pedidos, respostas e informações de uso | Acompanhar a operação do sistema |
| Software de segurança | Atividades mal-intencionadas detectadas | Auditoria, tendências e cumprimento de leis |

### 3.4 Analisadores de Pacotes

Um **analisador de pacotes** (*sniffer*) **intercepta e registra o tráfego da rede** e mostra o conteúdo de cada pacote. Exemplos: Wireshark e tcpdump.

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
| Da empresa | Regras de conduta | Assiduidade, vestimenta, privacidade |
| De funcionários | Itens do RH, assinados na contratação | Salário, benefícios, férias |
| De segurança | Objetivos e regras de segurança | Senhas, acesso remoto, uso aceitável |

### 4.2 Política de Segurança

A **política de segurança** informa a todos os requisitos para proteger os ativos de tecnologia e de informação. Ela serve de linha de base para comprar, configurar e auditar sistemas.

Seus principais benefícios são:

- mostrar o compromisso da organização com a segurança;
- definir o comportamento esperado;
- dar consistência à compra e ao uso de hardware e software;
- definir as consequências das violações.

Ela reúne políticas menores:

| Política | O que especifica |
| --- | --- |
| Identificação e autenticação | Quem acessa os recursos e como a identidade é verificada |
| Senhas | Requisitos mínimos e troca regular |
| Uso aceitável (AUP) | Usos da rede permitidos e consequências da violação |
| Acesso remoto | Como usuários remotos acessam a rede |
| Manutenção de rede | Como atualizar sistemas e aplicativos |
| Tratamento de incidentes | Como os incidentes são tratados |

### 4.3 Política de Uso Aceitável (AUP)

A **AUP** (*Acceptable Use Policy* — Política de Uso Aceitável) define **o que os usuários podem ou não fazer nos sistemas**. Ela deve ser o mais explícita possível. Exemplo: listar os sites que não podem ser acessados pelos computadores da empresa.

Todo funcionário assina a AUP, e a cópia assinada é guardada durante todo o emprego.

### 4.4 Políticas de BYOD

O **BYOD** (*Bring Your Own Device* — Traga seu Próprio Dispositivo) permite que os funcionários usem **seus próprios aparelhos para acessar sistemas, redes e informações da empresa**.

Ele traz produtividade, mobilidade e menos custos de TI, mas aumenta o risco de **vazamento de dados**. Por isso, a política de BYOD define:

- quem pode trazer dispositivos e quais são aceitos;
- o nível de acesso dos dispositivos pessoais;
- o que a equipe de segurança pode fazer no aparelho;
- o que fazer se um dispositivo for comprometido.

| Prática | O que fazer |
| --- | --- |
| Senha | Uma senha diferente para cada dispositivo e conta |
| Sem fio | Desligar Wi-Fi e Bluetooth quando não estiverem em uso |
| Atualização | Manter sistema e aplicativos atualizados |
| Backup | Ativar o backup para o caso de perda ou roubo |
| Localização | Usar localização com apagamento remoto |
| Antivírus | Instalar antivírus nos dispositivos aprovados |

O **MDM** (*Mobile Device Management* — Gerenciamento de Dispositivos Móveis) permite à TI **aplicar configurações de segurança e de software em todos os dispositivos que se conectam à rede da empresa**.

### 4.5 Conformidade com Regulamentos e Padrões

Os **regulamentos de conformidade** definem **pelo que a organização é responsável e quais são as consequências se ela não cumprir**. Eles variam conforme o tipo de organização e de dado. No Brasil, por exemplo, quem trata dados pessoais segue a LGPD (Lei Geral de Proteção de Dados).

## 5. Criptografia e Confidencialidade

A **criptografia** é a técnica de **embaralhar os dados para que só quem conhece o segredo certo consiga lê-los**. É a principal ferramenta da confidencialidade.

### 5.1 Conceitos Básicos de Criptografia

Os dados legíveis são o **texto claro**; criptografados, viram **texto cifrado**. O caminho de volta é a **descriptografia**.

Texto claro → Criptografia → Texto cifrado → Descriptografia → Texto claro

A **chave** é o valor secreto que o algoritmo usa nas duas operações. Quanto maior a chave, mais difícil descobri-la por tentativa.

Os algoritmos se dividem em duas categorias:

- **simétricos**: a mesma chave criptografa e descriptografa;
- **assimétricos**: um par de chaves diferentes, uma para cada operação.

### 5.2 Estados dos Dados

Os dados precisam de proteção em **três estados**:

| Estado | Situação | Exemplo |
| --- | --- | --- |
| Em repouso | Armazenados | Arquivo no disco ou na nuvem |
| Em trânsito | Sendo transmitidos | Mensagem viajando pela internet |
| Em processamento | Sendo usados ou alterados | Planilha aberta sendo editada |

### 5.3 Criptografia Simétrica

Na **criptografia simétrica**, **as duas partes usam a mesma chave**, chamada de **chave pré-compartilhada**. Ela precisa ser combinada **antes** da comunicação.

É como um cadeado com duas cópias da chave: Alice tranca a caixa, e só Bob, com a outra cópia, abre.

Por ser rápida, a criptografia simétrica é usada para **grandes volumes de dados**, como o tráfego de uma VPN (rede privada virtual, que cria um túnel protegido pela internet).

Para ser segura, a chave simétrica deve ter **no mínimo 128 bits**.

Os algoritmos simétricos funcionam de duas formas:

- **cifra de bloco**: criptografa blocos de tamanho fixo; exemplos: DES (64 bits) e AES (128 bits);
- **cifra de fluxo**: criptografa um bit ou byte de cada vez; exemplo: RC4.

| Algoritmo | Características | Situação |
| --- | --- | --- |
| DES | Chave curta | Inseguro, não usar |
| 3DES | Repete o DES três vezes | Descontinuado desde 2023 |
| AES | Bloco de 128 bits; chaves de 128, 192 ou 256 bits | Recomendado |
| SEAL | Cifra de fluxo, chave de 160 bits | Alternativa mais rápida ao AES |
| RC4 | Cifra de fluxo | Vulnerável, não usar |

**Observação:** no AES, só o tamanho da **chave** varia; o **bloco** é sempre de 128 bits.

### 5.4 Criptografia Assimétrica

Na **criptografia assimétrica**, ou **de chave pública**, cada um tem **um par de chaves**: a **pública**, que pode ser divulgada, e a **privada**, que só o dono conhece.

As duas se completam: **o que uma chave criptografa, só a outra do mesmo par descriptografa**. A privada não pode ser calculada a partir da pública.

As chaves são longas, de 512 a 4.096 bits; hoje, o seguro é usar **2.048 bits ou mais**. Por isso esses algoritmos são **lentos** e ficam com tarefas de pouco volume: **troca de chaves e assinaturas digitais**.

Exemplos de protocolos que os usam: IKE (troca de chaves das VPNs IPsec), SSL/TLS (HTTPS), SSH e PGP (e-mail).

| Algoritmo | Tamanho de chave (bits) | Uso |
| --- | --- | --- |
| Diffie-Hellman (DH) | 512 a 4.096 | Combinar uma chave secreta |
| DSA | 512 a 1.024 | Assinatura digital |
| RSA | 2.048 ou mais | Assinatura e criptografia |
| ElGamal | 512 a 1.024 | Mensagens pequenas, como chaves |
| Curvas elípticas (ECC) | 224 ou mais | Mesma segurança com chaves menores |

### 5.5 Confidencialidade e Autenticação com Chaves Assimétricas

O resultado depende da chave usada para criptografar:

- chave **pública** do destinatário → só ele lê → **confidencialidade**;
- chave **privada** do remetente → só ele poderia ter enviado → **autenticação**.

#### 5.5.1 Exemplo Resolvido: Alice Envia uma Mensagem Sigilosa a Bob

1. Alice recebe a chave pública de Bob;
2. Alice criptografa a mensagem com essa chave e a envia;
3. Bob descriptografa com a própria chave privada; só ele consegue ler.

Se uma chave privada for comprometida, o par inteiro deve ser trocado.

### 5.6 Diffie-Hellman

O **Diffie-Hellman (DH)** permite que **dois computadores gerem o mesmo segredo compartilhado sem nunca terem se comunicado antes**, sem enviar esse segredo pela rede. É usado nas VPNs IPsec e no SSH.

#### 5.6.1 Exemplo Resolvido: a Analogia das Cores

1. Alice e Bob combinam uma cor pública: amarelo;
2. cada um escolhe uma cor secreta: Alice, vermelho; Bob, azul;
3. cada um mistura o amarelo com a sua cor e envia o resultado: Alice envia laranja; Bob, verde;
4. cada um mistura a cor recebida com a própria cor secreta;
5. os dois chegam ao mesmo marrom, que é a chave compartilhada.

Quem intercepta só vê amarelo, laranja e verde, e não chega ao marrom.

A força do DH é definida pelo **grupo DH**: quanto maior, mais seguro e mais lento.

| Grupo DH | Tamanho |
| --- | --- |
| 1, 2 e 5 | 768, 1.024 e 1.536 bits |
| 14, 15 e 16 | 2.048, 3.072 e 4.096 bits |
| 19 e 20 | Curvas elípticas |

### 5.7 Resumo de Criptografia Simétrica e Assimétrica

| Característica | Simétrica | Assimétrica |
| --- | --- | --- |
| Chaves | A mesma nas duas operações | Par: pública e privada |
| Tamanho da chave | 40 a 256 bits | 512 a 4.096 bits |
| Velocidade | Rápida | Lenta |
| Uso típico | Grandes volumes, como VPN | Troca de chaves e assinaturas |
| Exemplos | AES, SEAL | RSA, DH, DSA, ECC |

As duas trabalham juntas. O assimétrico troca a chave com segurança, e o **algoritmo simétrico (como o AES) criptografa o grande volume de dados**.

## 6. Hash, Integridade e Autenticidade

A criptografia impede a leitura dos dados, mas não garante que eles chegaram sem alteração nem quem os enviou. Para isso existem o **hash** e o **HMAC**.

### 6.1 Elementos das Comunicações Seguras

As comunicações seguras se apoiam em **quatro elementos**:

| Elemento | O que garante | Como é obtido |
| --- | --- | --- |
| Integridade dos dados | A mensagem não foi alterada | Hash (SHA-2 ou SHA-3) |
| Autenticação de origem | A mensagem vem de quem diz ter enviado | HMAC |
| Confidencialidade | Só autorizados leem a mensagem | Criptografia |
| Não repúdio | O remetente não pode negar o envio | Assinatura digital |

### 6.2 Funções Hash

Uma **função hash** recebe dados de qualquer tamanho e produz uma **representação de tamanho fixo**, chamada de **hash** (ou *digest*).

Ela é **unidirecional**: calcular o hash é fácil, mas voltar aos dados é praticamente impossível. É como moer café: ninguém reconstrói os grãos a partir do pó.

Suas características são:

- a entrada pode ter qualquer tamanho, e a saída tem sempre o mesmo;
- o cálculo é rápido;
- não pode ser revertida;
- duas entradas diferentes **praticamente nunca geram o mesmo hash**.

Por esse motivo, **qualquer alteração nos dados, por menor que seja, muda o hash**.

### 6.3 Algoritmos de Hash

| Algoritmo | Tamanho do hash | Situação |
| --- | --- | --- |
| MD5 | 128 bits | Inseguro; evitar |
| SHA-1 | 160 bits | Com falhas conhecidas; evitar |
| SHA-2 | SHA-224, SHA-256, SHA-384 e SHA-512 | Seguro; preferir SHA-256 ou maior |
| SHA-3 | SHA3-224 a SHA3-512 | O mais novo; usar sempre que possível |

A sigla **SHA** significa *Secure Hash Algorithm*.

### 6.4 Verificação de Integridade com Hash

A verificação compara o hash calculado antes e depois da transmissão:

1. o remetente calcula o hash da mensagem e o envia junto;
2. o destinatário calcula de novo o hash da mensagem recebida;
3. hashes iguais → mensagem intacta; hashes diferentes → mensagem alterada.

Exemplo: “Pagar a Alex US$ 100” gera um hash. Se a mensagem virar “Pagar a Jeremy US$ 1.000” no caminho, o hash muda e a mensagem é descartada.

Usos comuns:

- **downloads**: comparar o hash publicado pelo fabricante com o do arquivo baixado;
- **perícia forense**: hashes iguais provam que a cópia de um disco é idêntica ao original.

### 6.5 Limitação do Hash

O hash detecta alterações acidentais, mas **não protege contra alterações deliberadas**: qualquer pessoa consegue calculá-lo.

Um atacante no meio do caminho pode alterar a mensagem, calcular um novo hash e enviá-lo. Esse é o **ataque *man-in-the-middle* (MitM)**, em que o criminoso se coloca entre as duas partes.

### 6.6 HMAC

O **HMAC** (*Hash-based Message Authentication Code*) é um hash calculado **a partir da mensagem e de uma chave secreta que só o remetente e o destinatário conhecem**.

Sem a chave, o atacante não gera um HMAC válido. Por isso, o HMAC garante a **integridade e a autenticação da origem**.

1. o remetente calcula o HMAC da mensagem com a chave e o envia junto;
2. o destinatário calcula o HMAC com a mesma chave;
3. valores iguais → mensagem íntegra e de origem confiável.

O HMAC é usado no SSL/TLS, no IPsec, no SSH e na autenticação entre roteadores (OSPF).

| Característica | Hash | HMAC |
| --- | --- | --- |
| Entrada | Só a mensagem | Mensagem + chave secreta |
| Quem calcula | Qualquer pessoa | Só quem tem a chave |
| Resiste ao man-in-the-middle | Não | Sim |

### 6.7 Hash de Senhas

Os sistemas não guardam as senhas: **guardam apenas o hash da senha**. No login, comparam o hash da senha digitada com o guardado.

Quem rouba os hashes precisa adivinhar as senhas, por dois ataques:

- **dicionário**: compara os hashes roubados com os de senhas comuns;
- **força bruta**: testa todas as combinações; por isso a senha precisa ser longa.

#### 6.7.1 Salt

O **salt** é uma **sequência aleatória acrescentada à senha antes do cálculo do hash**. Assim, senhas iguais geram hashes diferentes.

O salt é guardado junto com o hash e não precisa ser secreto. As boas práticas são:

- um salt exclusivo para cada senha, nunca reutilizado;
- gerado por um **CSPRNG** (gerador de números aleatórios seguro para criptografia);
- calculado sempre no servidor.

O salt inutiliza as tabelas que os atacantes preparam com antecedência:

| Tabela | Como funciona |
| --- | --- |
| Tabela de pesquisa | Hashes pré-calculados de um dicionário, com a senha de cada um |
| Tabela de pesquisa reversa | Liga cada hash roubado a todos os usuários que o usam |
| Tabela rainbow | Ocupa menos espaço, mas quebra as senhas mais devagar |

## 7. Assinaturas Digitais e Infraestrutura de Chave Pública (PKI)

A **assinatura digital** combina o hash e a criptografia assimétrica para provar quem enviou uma mensagem. Para confiar nas chaves públicas usadas nessa prova, existe a **PKI**.

### 7.1 Assinatura Digital

A **assinatura digital** garante **autenticidade, integridade e não repúdio**, e vale como prova legal.

Suas características são:

- autêntica: prova quem assinou;
- inalterável: o documento assinado não pode ser modificado;
- não reutilizável: não pode ser transferida para outro documento;
- não repudiável: o signatário não pode negar a assinatura.

O padrão **DSS** (*Digital Signature Standard*) admite três algoritmos: DSA, RSA e **ECDSA**, que usa curvas elípticas e gera assinaturas menores.

### 7.2 Como a Assinatura É Criada e Verificada

A assinatura usa a chave **privada** do remetente para assinar e a chave **pública** dele para conferir.

#### 7.2.1 Exemplo Resolvido: Bob Confirma um Pedido de Alice

Para assinar:

1. Bob calcula o hash do documento;
2. criptografa o hash com a própria chave privada: essa é a assinatura;
3. envia o documento com a assinatura.

Para verificar:

1. Alice descriptografa a assinatura com a chave pública de Bob e recupera o hash;
2. calcula o hash do documento recebido;
3. hashes iguais → documento autêntico e inalterado.

**Importante:** o que se criptografa na assinatura é o **hash** do documento. Por isso, a assinatura não dá confidencialidade: o documento continua legível.

### 7.3 Assinatura de Código

A **assinatura de código** aplica a assinatura digital a programas. Ela garante que:

- o código veio realmente da editora;
- não foi modificado desde a publicação;
- a editora não pode negar que o publicou.

Nas propriedades de um programa baixado, a aba de assinaturas digitais mostra quem assinou, o algoritmo usado e a data.

### 7.4 Certificados Digitais

Um **certificado digital** funciona como um **passaporte eletrônico**: ele **associa uma chave pública a uma identidade confirmada**, de um site, de uma pessoa ou de uma organização. Ele informa para quem foi emitido, quem o emitiu e até quando vale.

**Importante:** o **certificado verifica a identidade**; a **assinatura verifica que algo veio dessa identidade**.

### 7.5 Infraestrutura de Chave Pública (PKI)

Para confiar na chave pública de um site, um terceiro confiável precisa confirmar a quem ela pertence, como o órgão que emite a carteira de motorista.

A **PKI** (*Public Key Infrastructure* — Infraestrutura de Chave Pública) é o conjunto de sistemas, pessoas e procedimentos que **criam, distribuem, armazenam e revogam certificados digitais**.

A **autoridade de certificação (CA)** é quem **emite os certificados, vinculando uma chave pública a uma identidade confirmada**. Exemplos: DigiCert, GlobalSign e Let's Encrypt, que é gratuita.

| Elemento | Função |
| --- | --- |
| Certificado | Chave pública, finalidade, CA emissora e validade |
| Armazenamento de certificados | Guarda certificados e chaves privadas no computador |
| CA | Verifica a identidade e emite os certificados |
| Banco de dados de certificados | Guarda os certificados aprovados |

De forma simplificada:

1. Bob pede um certificado à CA, que confirma sua identidade e o emite;
2. Bob apresenta o certificado a Alice;
3. Alice confere com a chave pública da CA que o certificado é válido.

A **autoridade de registro (RA)** confere a identidade de quem pede o certificado e encaminha o pedido; quem emite é sempre uma CA.

### 7.6 Classes de Certificados

As classes vão de 0 (testes, sem verificação) a 5 (governo e organizações privadas), conforme o rigor da verificação de identidade. **Quanto maior a classe, mais confiável o certificado.**

| Classe | Uso |
| --- | --- |
| 0 | Testes |
| 1 | Pessoas, com verificação de e-mail |
| 2 | Organizações |
| 3 | Servidores e assinatura de software |
| 4 | Transações entre empresas |
| 5 | Governo e organizações privadas |

Os navegadores já trazem a lista de **autoridades de certificação raiz confiáveis**.

### 7.7 Topologias de PKI

| Topologia | Como funciona | Vantagem | Desvantagem |
| --- | --- | --- | --- |
| Raiz única | Uma CA emite todos os certificados | Simplicidade | Ponto único de falha |
| Certificação cruzada | CAs do mesmo nível confiam umas nas outras | Sem ponto único de falha | Muitas relações para gerenciar |
| Hierárquica | A CA raiz certifica CAs subordinadas | Escala bem | Cadeia difícil de rastrear |
| Híbrida | Hierarquias que se certificam entre si | Une comunidades diferentes | Mais complexa |

O **ponto único de falha** é qualquer componente cuja falha derruba o sistema inteiro.

### 7.8 Padrão X.509

O padrão **X.509 versão 3**, do ITU-T, define o **formato dos certificados digitais**. Ele é usado em:

- **SSL/TLS**: certificados dos sites no HTTPS;
- **IPsec**: autenticação nas VPNs;
- **S/MIME**: e-mail protegido;
- **EAP-TLS**: autenticação com certificado digital dos dispositivos que se conectam à rede.

### 7.9 Inscrição e Revogação de Certificados

O primeiro passo é obter o certificado da CA raiz, que é **autoassinado**. Nos navegadores, ele já vem instalado.

Um certificado pode ser **revogado** antes do vencimento, por exemplo quando a chave é comprometida:

| Método | Como funciona |
| --- | --- |
| CRL (*Certificate Revocation List*) | Lista dos certificados revogados, consultada periodicamente |
| OCSP (*Online Certificate Status Protocol*) | Consulta imediata a um servidor sobre um certificado |

### 7.10 Aplicações da PKI

A PKI está em:

- HTTPS e VPNs IPsec;
- controle de acesso à rede com 802.1X (padrão em que o dispositivo só usa a porta da rede depois de autenticado);
- e-mail seguro (S/MIME);
- assinatura de código e criptografia de arquivos;
- autenticação com cartões inteligentes.

O navegador mostra um aviso quando o certificado está **vencido** ou quando **não consegue validar a assinatura**, geralmente porque a CA raiz não está entre as confiáveis.

## 8. Ocultação de Dados

Além de criptografar, é possível proteger dados **escondendo ou disfarçando a informação**, com o mascaramento e a esteganografia.

### 8.1 Mascaramento de Dados

O **mascaramento de dados** **substitui a informação confidencial por uma versão não confidencial que parece e funciona como a original**. O uso mais comum é criar dados de teste sem expor os dados reais.

| Técnica | Como funciona | Exemplo |
| --- | --- | --- |
| Substituição | Troca os dados por valores fictícios | Nomes reais trocados por nomes inventados |
| Embaralhamento | Mistura os valores da coluna entre os registros | Salários trocados de lugar |
| Anulação | Deixa o campo vazio | CPF apagado |

### 8.2 Esteganografia

A **esteganografia** **esconde uma mensagem dentro de outro arquivo**, como uma imagem ou um áudio. Sua vantagem é que **a mensagem secreta não chama atenção**.

Seus componentes são a mensagem escondida, a **capa** (o arquivo que a esconde), o **estego-arquivo** (o resultado) e a **estego-chave**, que controla o processo.

A técnica mais usada em imagens é a dos **bits menos significativos (LSB**, *Least Significant Bits*): ela troca o último bit de cada byte de cor dos pixels. Como esse bit quase não muda a cor, **o olho humano não percebe a alteração**.

Na **esteganografia social**, a mensagem tem um sentido para o público e outro para quem conhece o código.

### 8.3 Esteganoanálise

A **esteganoanálise** é a **descoberta de que existe informação escondida**. Ela procura padrões estranhos nas imagens, dados em áreas não usadas do disco e informações escondidas em cabeçalhos de pacotes.

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
| Físicos | Barreiras reais | Guardas, cercas, portas trancadas, câmeras |
| Lógicos | Hardware e software | Senhas, criptografia, firewalls, cartões inteligentes |
| Administrativos | Políticas e procedimentos | Treinamento, verificação de antecedentes |

Dois exemplos merecem destaque:

- **mantrap** (eclusa): entrada com duas portas que pode prender um visitante indesejado entre elas;
- **níveis de corte** (*clipping levels*): limite de erros permitido antes de disparar um alerta.

### 9.2 AAA: Autenticação, Autorização e Contabilidade

O **AAA** (*Authentication, Authorization and Accounting*) reúne os **três serviços de segurança que formam a estrutura principal do controle de acesso**:

| Serviço | Pergunta que responde | Exemplo |
| --- | --- | --- |
| Autenticação | Quem é você? | Nome de usuário e senha |
| Autorização | O que você pode fazer? | Entrar na rede não dá direito à impressora colorida |
| Contabilidade | O que você fez? | Acesso a um servidor por 15 minutos |

A contabilidade (*accounting*) não tem relação com finanças. Ela é o **registro do que o usuário fez**.

### 9.3 Identificação

Na **identificação**, o usuário diz quem é, normalmente pelo **nome de usuário**.

**Importante:** informar o nome de usuário é **identificação**; provar que se é aquele usuário, com a senha, é **autenticação**.

### 9.4 Métodos de Autenticação

Para provar a identidade, o usuário apresenta pelo menos um de **três tipos de fator**:

| Fator | Exemplos |
| --- | --- |
| Algo que você sabe | Senha, PIN |
| Algo que você tem | Cartão inteligente, token |
| Algo que você é | Impressão digital, íris, voz |

#### 9.4.1 Algo que Você Sabe

A **senha** é o **método de autenticação mais usado**. As boas práticas são:

- não usar dados pessoais, fáceis de adivinhar;
- ter pelo menos oito caracteres;
- combinar maiúsculas, minúsculas, números e símbolos;
- usar uma senha diferente para cada sistema;
- guardar as senhas em um gerenciador.

#### 9.4.2 Algo que Você Tem

O **cartão inteligente** tem um **chip que guarda e protege dados** com criptografia. O **token** é um pequeno dispositivo que mostra um número temporário, usado como segundo fator.

#### 9.4.3 Algo que Você É

A **biometria** usa **características físicas ou comportamentais únicas** e as compara com um perfil guardado. Ela pode ser:

- **fisiológica**: digital, rosto, retina;
- **comportamental**: voz, modo de andar, ritmo de digitação.

### 9.5 Autenticação Multifator (MFA)

A **MFA** (*Multi-Factor Authentication* — autenticação multifator) **usa pelo menos dois fatores de tipos diferentes**. Exemplo: o caixa eletrônico exige o cartão (tem) e o PIN (sabe). Com dois fatores, também se chama **2FA**.

**Importante:** duas senhas não formam MFA, porque são do mesmo tipo de fator.

### 9.6 Autorização

A **autorização** **controla o que o usuário pode e não pode fazer depois de autenticado**: ler, editar, criar ou excluir. Ela é automática e pode limitar também **quando** o acesso vale, como só no horário comercial.

As regras vêm da **política de autorização**, que pode ser:

- **baseada em grupo**: só a equipe de TI entra na sala de servidores;
- **por nível de autoridade**: as permissões dependem do cargo.

### 9.7 Auditabilidade

A **auditabilidade** **rastreia cada ação até a pessoa ou o processo que a realizou**. Ela registra, por exemplo, horários de login, falhas de login e recursos acessados. Várias falhas seguidas podem indicar uma tentativa de invasão.

### 9.8 Gerenciamento de Identidade Federada

O **gerenciamento de identidade federada** permite que **várias organizações aceitem as mesmas credenciais**. Exemplo: entrar em vários sites com a mesma conta de rede social.

O risco é o **efeito cascata**: credenciais roubadas abrem todos os sistemas da federação. A proteção mais comum é **vincular o login a um dispositivo autorizado**.

## 10. Modelos de Controle de Acesso e Confiança Zero

Um **modelo de controle de acesso** define **quem decide sobre o acesso e com base em quê**.

### 10.1 Modelos de Controle de Acesso

| Modelo | Quem decide / com base em quê | Característica marcante |
| --- | --- | --- |
| DAC (discricionário) | O **dono** dos dados | Menos restritivo |
| MAC (obrigatório) | Rótulos de segurança e autorização do usuário | Mais rígido; uso militar |
| RBAC (baseado em funções) | A **função** ou cargo | Recomendado para grandes organizações |
| ABAC (baseado em atributos) | Atributos do usuário, do recurso e do ambiente | Mais flexível |
| Baseado em regras | Regras da equipe de segurança | Usa ACLs; o usuário não altera |
| TAC (baseado em tempo) | Hora e dia | Acesso só em horários permitidos |

#### 10.1.1 Controle de Acesso Discricionário (DAC)

No **DAC**, **o dono do recurso decide quem pode acessá-lo**. Exemplo: o dono de um arquivo define quem lê ou altera.

#### 10.1.2 Controle de Acesso Obrigatório (MAC)

No **MAC**, cada recurso tem um **rótulo de segurança** e cada usuário, uma **autorização** (*clearance*). O acesso só é liberado se os dois forem compatíveis, e o usuário não muda as regras.

#### 10.1.3 Controle de Acesso Baseado em Funções (RBAC)

No **RBAC**, as permissões pertencem às **funções**, e cada pessoa recebe as da função que ocupa. Quando alguém muda de cargo, basta trocar a função.

#### 10.1.4 Controle de Acesso Baseado em Atributos (ABAC)

No **ABAC**, a decisão considera **atributos do usuário, do recurso e do ambiente**. Exemplo: o médico vê prontuários só no hospital e durante o plantão.

#### 10.1.5 Controle de Acesso Baseado em Regras

No **controle baseado em regras**, a equipe de segurança define condições, como IPs e protocolos permitidos, em listas de controle de acesso.

**Importante:** a sigla **RBAC** serve para os dois modelos: funções (*Role*) e regras (*Rule*). Sozinha, normalmente indica o de funções.

#### 10.1.6 Controle de Acesso Baseado em Tempo (TAC)

No **TAC**, o acesso depende da **hora e do dia**. Exemplo: a folha de pagamento só aceita logins em dias úteis, das 8h às 18h.

### 10.2 Privilégio Mínimo e Escalação de Privilégios

O **privilégio mínimo** determina que **usuários e processos recebam apenas o acesso mínimo necessário para fazer seu trabalho**.

Na **escalação de privilégios**, o atacante explora uma falha para obter **um nível de privilégio maior do que deveria ter**.

### 10.3 Confiança Zero (Zero Trust)

A **confiança zero** (*zero trust*) **não confia automaticamente em ninguém**, nem em quem já está dentro da rede. Seu princípio é “**nunca confie, sempre verifique**”.

No modelo antigo, quem passava pelo perímetro circulava pela rede inteira. Na confiança zero, **todo ponto em que há uma decisão de acesso passa a ser um perímetro**. Isso reduz o **movimento lateral**, a passagem do atacante de um sistema para outro.

| Pilar | O que protege |
| --- | --- |
| Força de trabalho | Pessoas que acessam aplicativos de trabalho de qualquer lugar |
| Cargas de trabalho | Aplicativos que conversam entre si, na nuvem ou no data center |
| Local de trabalho | Dispositivos ligados à rede: servidores, impressoras, câmeras |

### 10.4 Controle de Acesso à Rede (NAC)

O **NAC** (*Network Access Control*) **aplica as políticas da organização às pessoas e aos dispositivos que tentam entrar na rede**. Suas funções são:

- identificar usuários e dispositivos conectados;
- oferecer acesso seguro a visitantes;
- verificar se o dispositivo cumpre as políticas **antes** de liberar o acesso;
- bloquear ou isolar dispositivos fora das regras.

Com BYOD e IoT, a automação do NAC é parte importante da confiança zero.

## 11. Gerenciamento de Contas e Protocolos de Autenticação

O **gerenciamento de contas** garante que **cada usuário tenha a conta adequada à sua função** e só acesse o necessário. Os **protocolos de autenticação** definem como a identidade é comprovada pela rede.

### 11.1 Tipos de Contas

| Tipo | Uso |
| --- | --- |
| Usuário | Uso diário |
| Serviço | Programas interagindo com o sistema |
| Convidado | Usuários temporários |
| Administrador | Apenas administrar o sistema |

A conta de administrador **só deve ser usada para administrar**. Se o administrador abrir um site infectado com ela, o malware ganha os mesmos privilégios.

Os atacantes conhecem as contas padrão dos sistemas. Por isso, a boa prática é **substituir ou desativar as contas padrão** e nunca compartilhar contas.

### 11.2 Boas Práticas de Gerenciamento de Contas

As boas práticas são:

- liberar só o acesso necessário às tarefas;
- revisar os acessos periodicamente;
- desativar as contas que não são mais usadas;
- limitar **quando** e **de onde** cada usuário pode fazer login.

| Recurso | O que faz | Exemplo |
| --- | --- | --- |
| Delimitação geográfica (*geofencing*) | Dispara uma ação quando o usuário entra ou sai de uma área | Bloquear o acesso fora do prédio |
| Geolocalização | Identifica onde o dispositivo está | Posição do celular no mapa |
| Marcação geográfica (*geotagging*) | Acrescenta a localização a um arquivo | Foto com as coordenadas |

### 11.3 Contas Privilegiadas

As **contas privilegiadas** têm **acesso elevado e sem restrição** e são o **alvo preferido dos criminosos digitais**. Para protegê-las:

- reduzir o número de contas privilegiadas;
- trocar as senhas automaticamente a cada 30 ou 60 dias;
- eliminar credenciais compartilhadas;
- registrar as sessões e gerar alertas para comportamentos incomuns;
- exigir **autenticação multifator** em todo acesso administrativo.

### 11.4 Permissões de Arquivos e Pastas

As **permissões** **limitam o acesso de uma pessoa ou de um grupo a pastas e arquivos**, aplicando o privilégio mínimo.

| Permissão | O que o usuário pode fazer |
| --- | --- |
| Controle total | Tudo, inclusive alterar as permissões |
| Modificar | Ler, alterar e excluir |
| Ler e executar | Ver e executar programas |
| Gravar | Criar e alterar arquivos |
| Leitura | Ver e abrir |

**Importante:** a permissão **Negar substitui qualquer outra**, mesmo para administradores.

Arquivos novos **herdam as permissões da pasta-mãe**. Ao mover ou copiar:

| Ação | Mesmo volume | Volume diferente |
| --- | --- | --- |
| Mover | Mantém as permissões | Herda novas |
| Copiar | Herda novas | Herda novas |

Ou seja, **só mover dentro do mesmo volume mantém as permissões originais**.

### 11.5 Políticas de Conta no Windows

Em redes com **Active Directory**, os computadores do domínio recebem a política de segurança do domínio. Fora dele, usa-se a **Política de Segurança Local** (secpol.msc).

As principais políticas são:

- **senhas**: exemplo: trocar a cada 90 dias, com oito caracteres e três tipos diferentes;
- **bloqueio de conta**: exemplo: bloquear por 30 minutos depois de cinco tentativas erradas;
- **auditoria**: registrar logons, uso de privilégios e mudanças de política.

### 11.6 Gerenciamento de Autenticação

O **gerenciamento de autenticação** busca **garantir uma entrada segura sem complicar a vida do usuário**.

| Solução | Como funciona |
| --- | --- |
| SSO (*Single Sign-On*) | Um login dá acesso a vários aplicativos |
| OAuth | Um serviço de terceiros acessa dados da conta sem receber a senha |
| Cofre de senhas | Guarda as credenciais sob uma única senha forte |
| KBA (*Knowledge-Based Authentication*) | Redefine a senha com perguntas pessoais |

### 11.7 Protocolos de Autenticação

Um **protocolo de autenticação** define **o que duas entidades trocam para se autenticar**.

| Protocolo | Como funciona | Segurança |
| --- | --- | --- |
| PAP | Envia usuário e senha em texto claro | Fraca |
| CHAP | Desafio e resposta com hash | Melhor que o PAP |
| EAP | Estrutura com vários métodos, comum no sem fio | Depende do método |
| 802.1X | O dispositivo só usa a porta da rede depois de autenticado | Alta |
| RADIUS | Servidor central; criptografa só a senha | Média |
| TACACS+ | Servidor central; criptografa tudo | Alta |
| Kerberos | Autenticação mútua com tíquetes | Alta |

#### 11.7.1 Kerberos

O **Kerberos** faz **autenticação mútua**: cliente e servidor provam a identidade um ao outro, com base em **tíquetes**.

1. o cliente se autentica e recebe um **TGT** (*Ticket-Granting Ticket*, tíquete de concessão de tíquete);
2. apresenta o TGT e pede acesso a um serviço;
3. recebe um **tíquete de serviço** e acessa o serviço.

Os tíquetes têm **carimbo de hora e prazo de validade**, o que impede reutilizar um tíquete antigo.

## 12. Implementação do AAA

A política de segurança costuma exigir o registro de **quem entrou, quando e o que fez**. O **AAA** é a estrutura que atende a isso em redes de qualquer tamanho.

### 12.1 AAA Local e AAA Baseado em Servidor

A Cisco oferece **duas formas de implementar o AAA**:

| Característica | AAA local | AAA baseado em servidor |
| --- | --- | --- |
| Onde ficam os usuários | No próprio roteador | Em um servidor AAA central |
| Indicado para | Redes pequenas | Redes médias e grandes |
| Escalabilidade | Baixa | Alta |

No AAA local, o roteador confere as credenciais no próprio banco de dados. No AAA baseado em servidor, ele consulta o servidor central.

O AAA centralizado é **mais escalável e mais fácil de gerenciar**. Ele pode usar o Active Directory ou o **LDAP** (protocolo de consulta a serviços de diretório).

### 12.2 TACACS+ e RADIUS

Os dispositivos falam com o servidor AAA pelo **TACACS+** ou pelo **RADIUS**:

| Característica | TACACS+ | RADIUS |
| --- | --- | --- |
| Funções | Separa as três funções do AAA | Junta autenticação e autorização |
| Padrão | Principalmente Cisco | Aberto (RFC) |
| Transporte | TCP, porta 49 | UDP, portas 1812 e 1813 |
| Criptografia | Todo o corpo do pacote | Só a senha |
| Autorização de comandos | Sim | Não |
| Contabilidade | Limitada | Abrangente |

**Importante:** o **RADIUS criptografa só a senha**; o **TACACS+ criptografa todo o corpo do pacote**.

O TACACS+ é a melhor escolha quando se precisa controlar os comandos de cada administrador. O RADIUS é muito usado com 802.1X e acesso remoto.

### 12.3 Contabilidade do AAA

Com o AAA centralizado, os registros de todos os dispositivos vão para um só lugar, o que **facilita a auditoria das ações dos usuários**. Eles incluem horários de início e fim, comandos executados e volume de dados, e servem de prova contra ações mal-intencionadas.

| Tipo | O que registra |
| --- | --- |
| De rede | Sessões de rede, com pacotes e bytes |
| De conexão | Conexões de saída, como por SSH |
| EXEC | Sessões de terminal do usuário |
| Do sistema | Eventos como reinicializações |
| De comandos | Comandos digitados, com data, hora e usuário |
| De recursos | Início e fim das conexões autenticadas |

## 13. Segurança Física

A **segurança física** protege instalações e equipamentos contra o acesso físico não autorizado. De nada adianta uma senha forte se qualquer pessoa pode entrar na sala de servidores.

### 13.1 Barreiras Físicas e Cercas

As **barreiras físicas** são a **camada mais externa e mais visível da defesa**. Exemplos: cerca de perímetro, portões e **cabeços de amarração** (*bollards*), postes que impedem a invasão com veículos.

A altura da cerca define o quanto ela atrasa um invasor:

| Altura | Efeito |
| --- | --- |
| 1 metro | Só detém invasores casuais |
| 2 metros | Alta demais para invasores casuais |
| 2,5 metros | Atrasa por pouco tempo um invasor determinado |

Áreas de alta segurança acrescentam arame farpado ou concertina no topo.

### 13.2 Biometria no Controle de Acesso Físico

A biometria é muito usada para liberar portas e áreas restritas. Na escolha do sistema, pesam a velocidade, a aceitação pelos usuários e a resistência à falsificação, mas o fator mais importante é a **precisão**:

| Erro | Nome | O que acontece |
| --- | --- | --- |
| Tipo I | Falsa rejeição | Barra um usuário autorizado |
| Tipo II | Falsa aceitação | Deixa entrar quem não deveria |

**Importante:** no controle de acesso, o **erro tipo II (falsa aceitação) é o mais grave**, porque deixa um invasor entrar.

A **CER** (*Crossover Error Rate* — taxa de erro de cruzamento) é o ponto em que as taxas de falsa rejeição e de falsa aceitação se igualam. **Quanto menor a CER, mais preciso é o sistema.**

### 13.3 Vigilância

Os controles físicos dependem, no fim, de pessoas que reajam ao ataque:

| Forma | Vantagens | Desvantagens |
| --- | --- | --- |
| Guardas | Resposta imediata | Custo e erro humano |
| Vídeo (CFTV) | Grava por longos períodos e cobre todo o perímetro | Depende de alguém que assista |
| Etiquetas RFID | Rastreiam ativos que saem da área segura | Exigem leitores nas saídas |

Os **guardas** são a melhor solução quando é preciso **resposta instantânea e adequada**.

As etiquetas **RFID** (identificação por radiofrequência) **não precisam estar visíveis nem na linha de visão do leitor**. Exemplo: um notebook da empresa escondido em uma bolsa dispara o alerta ao passar pela porta.

### 13.4 Controle de Ameaças às Instalações

As principais medidas são:

- câmeras e controle de acesso em todas as entradas;
- regras para visitantes;
- crachás com criptografia;
- planos de recuperação de desastres;
- treinamento em segurança.

## 14. Segurança de Aplicações

A **segurança de aplicações** protege os programas, sites e serviços que a organização desenvolve e usa. Ela deve ser **prioridade em todas as etapas: desenvolvimento, testes e implantação**.

### 14.1 Etapas do Desenvolvimento de Aplicações

O desenvolvimento usa ambientes separados:

Desenvolvimento e teste → Preparação → Produção

| Ambiente | O que acontece |
| --- | --- |
| Desenvolvimento e teste | O código é escrito e corrigido; a garantia de qualidade (QA) encontra as falhas |
| Preparação (*staging*) | Ambiente idêntico ao de produção, para confirmar as configurações de segurança |
| Produção | O software entra em uso real |

O **controle de versão** rastreia as alterações no código, e o **sandbox** é um ambiente isolado para testes.

### 14.2 Técnicas de Codificação Segura

| Técnica | O que faz |
| --- | --- |
| Normalização | Converte cada entrada para a forma mais simples, o que ajuda a achar entradas maliciosas |
| Procedimento armazenado | Instruções SQL prontas, guardadas no banco de dados |
| Ofuscação | Esconde os dados originais com caracteres aleatórios |
| Camuflagem | Troca dados confidenciais por dados fictícios realistas |
| Reutilização de código e SDKs | Aproveitam código pronto para economizar tempo |

A ofuscação e a camuflagem dificultam a **engenharia reversa**, a tentativa de descobrir como o programa funciona.

Na reutilização de código e nos **SDKs** (kits de desenvolvimento de software), **uma vulnerabilidade no código reaproveitado passa para todos os aplicativos que o usam**.

### 14.3 Validação de Entrada

**Controlar o que entra no banco de dados é essencial para manter a integridade dos dados.** Muitos ataques enviam dados malformados para travar o aplicativo ou fazê-lo revelar informações.

A **regra de validação** confere se os dados estão **dentro dos parâmetros definidos pelo projetista do banco de dados**:

| Critério | O que verifica | Exemplo |
| --- | --- | --- |
| Tamanho | Número de caracteres | CEP com 8 dígitos |
| Formato | Formato definido | Data DD/MM/AAAA |
| Consistência | Dados que combinam entre si | Cidade compatível com o estado |
| Intervalo | Valor entre um mínimo e um máximo | Idade entre 0 e 120 |
| Dígito verificador | Cálculo extra para detectar erros | Último dígito do ISBN ou do CPF |

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

Além do hash, três práticas mantêm a integridade:

- **controle de versão**: duas pessoas não alteram o mesmo registro ao mesmo tempo;
- **backups**: permitem recuperar dados corrompidos;
- **autorização**: só certos usuários podem modificar os dados.

### 14.5 Outras Práticas de Segurança de Aplicativos

Os **cookies** guardam dados da navegação no computador do usuário. Devem ser **cookies seguros, enviados apenas por HTTPS**.

### 14.6 Controle de Ameaças a Aplicativos

| Ameaça | Medidas |
| --- | --- |
| Acesso não autorizado a salas de equipamentos | Políticas para funcionários e visitantes |
| Sistema fora do ar | Planos de continuidade e de recuperação de desastres |
| Falhas no sistema operacional | Correções regulares |
| Acesso não autorizado aos sistemas | MFA e monitoramento dos logs |
| Perda de dados | Classificação de dados e backup |
| Falhas no desenvolvimento | Testes antes do lançamento |

### 14.7 OWASP Top 10

A **OWASP** (*Open Web Application Security Project*) é uma organização sem fins lucrativos que publica o **OWASP Top 10**, a lista das **dez principais preocupações de segurança web**.

## 15. Fortalecimento de Serviços e Protocolos de Rede

O **fortalecimento da rede** (*network hardening*) consiste em **proteger os serviços e protocolos para que só o necessário fique exposto**, trocando os protocolos inseguros por versões seguras.

### 15.1 Varredura de Portas

Um **scanner de portas** testa cada porta de um dispositivo para saber quais estão abertas. A **porta** é o número que identifica um serviço; exemplo: a 80 é do HTTP.

O administrador usa o scanner para achar serviços desprotegidos, e o atacante também. Por isso, o ideal é que **apenas as portas necessárias fiquem abertas**.

### 15.2 Serviços de Rede e de Roteamento

#### 15.2.1 DHCP

O **DHCP** **atribui automaticamente endereço IP** e outras configurações aos dispositivos. Um atacante pode criar um servidor DHCP falso.

O **DHCP snooping** **impede que servidores DHCP falsos entreguem endereços**. Também é preciso proteger fisicamente o servidor, mantê-lo atrás de um firewall e aplicar as correções.

#### 15.2.2 DNS

O **DNS** **converte nomes, como www.cisco.com, em endereços IP**. Atacando o DNS, o criminoso pode **redirecionar o tráfego para sites falsos**.

As **DNSSEC** (*DNS Security Extensions*) usam **assinaturas digitais** para autenticar as respostas DNS. Outras medidas são manter o software atualizado, separar os servidores internos dos externos e restringir as transferências de zona.

#### 15.2.3 ICMP

O **ICMP** **envia mensagens de erro e de controle**, como as do comando **ping**. Os atacantes o usam para reconhecimento da rede e para ataques de negação de serviço (**DoS**, *Denial of Service*, que tiram um serviço do ar). Por isso, muitas redes filtram o ICMP.

#### 15.2.4 RIP

O **RIP** é um protocolo de roteamento que escolhe a rota pela contagem de saltos, com **máximo de 15 saltos**. Para proteger o roteamento, usa-se **autenticação entre os roteadores**.

#### 15.2.5 NTP

O **NTP** (*Network Time Protocol*) **sincroniza os relógios dos dispositivos**. A hora certa é essencial para os logs e para validar certificados. A proteção é a **autenticação NTP**.

### 15.3 Telnet, SSH e SCP

O **Telnet** e o **SSH** (*Secure Shell*) dão acesso remoto, por linha de comando, a dispositivos como roteadores:

| Característica | Telnet | SSH |
| --- | --- | --- |
| Criptografia | Nenhuma | Tudo criptografado |
| Porta | TCP 23 | TCP 22 |
| O que um sniffer vê | Usuário e senha | Apenas os endereços IP |
| Recomendação | Evitar | Usar sempre |

O **SCP** (*Secure Copy*) **transfere arquivos com segurança usando o SSH**.

### 15.4 Protocolos Seguros

Os principais protocolos têm versões seguras:

- **SNMPv3**: versão do SNMP (gerenciamento de equipamentos) com criptografia;
- **TLS**: o **substituto atualizado e mais seguro do SSL**; protege o HTTP, que vira **HTTPS**;
- **FTPS**: o FTP com SSL/TLS;
- **S/MIME**: e-mails **assinados e criptografados**.

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

Uma **VLAN** (*Virtual Local Area Network* — rede local virtual) **agrupa dispositivos de forma lógica**, não importa onde estejam ligados.

**Importante:** a **LAN** se baseia em **conexões físicas**; a **VLAN**, em **conexões lógicas**.

Os **troncos** (*trunks*) são portas que ligam os switches e **transportam o tráfego de várias VLANs**. Assim, pessoas do mesmo setor podem estar em andares diferentes e na mesma VLAN.

Exemplo: o RH fica em uma VLAN própria, o que **reduz a chance de vazamento**. As VLANs também limitam o **broadcast** (mensagens para todos os dispositivos) a cada VLAN.

### 16.2 Zona Desmilitarizada (DMZ)

A **DMZ** (*Demilitarized Zone* — zona desmilitarizada) é uma **pequena rede entre a rede privada confiável e a internet**. Nela ficam os servidores acessados de fora, como os **servidores web e de e-mail**.

A maioria das redes tem de **duas a quatro zonas de risco**:

| Zona | Risco | Confiança |
| --- | --- | --- |
| LAN privada | Baixo | Alta |
| Extranet (rede com parceiros) | Médio-baixo | Médio-alta |
| DMZ | Médio-alto | Médio-baixa |
| Internet | Alto | Baixa |

Os firewalls controlam o tráfego **leste-oeste** (entre servidores do data center) e **norte-sul** (que entra e sai da rede).

### 16.3 Segmentação e Confiança Zero

A segmentação é a base técnica da confiança zero: cada passagem entre segmentos vira um ponto de controle.

| Característica | VLAN | DMZ |
| --- | --- | --- |
| O que separa | Setores dentro da rede interna | Servidores públicos da rede interna |
| Onde fica | Dentro da LAN | Entre a LAN e a internet |
| Exemplo | VLAN do RH | Servidor web da empresa |

## 17. Segurança Sem Fio e de Dispositivos Móveis

Os dispositivos sem fio e móveis são hoje a **maioria dos dispositivos nas redes**. Eles estão sujeitos a roubo, interceptação do tráfego e ataques man-in-the-middle. A melhor proteção combina **autenticação e criptografia**.

### 17.1 Padrões de Segurança Sem Fio

Os padrões Wi-Fi evoluíram nesta ordem:

WEP → WPA → WPA2 → WPA3

| Padrão | Características | Situação |
| --- | --- | --- |
| WEP | Primeiro padrão; chaves de 64 e 128 bits | Fraco, não usar |
| WPA | MIC (integridade) e TKIP (troca de chaves) | Substituiu o WEP |
| WPA2 | AES obrigatório; CCMP no lugar do TKIP | Seguro |
| WPA3 | Algoritmos e troca de chaves mais robustos | O mais atual |

Em casa, o mais comum é o **WPA-PSK** (*Pre-Shared Key*), em que todos usam a mesma senha.

O **WPS** (*Wi-Fi Protected Setup*) facilita a conexão, mas o **PIN pode ser descoberto por força bruta**. Por isso, deve ser **desativado**.

### 17.2 Autenticação em Redes Sem Fio

O padrão 802.11 original tem **dois tipos de autenticação**:

- **sistema aberto**: qualquer dispositivo se conecta;
- **chave compartilhada**: autentica e criptografa entre o cliente e o ponto de acesso.

O **ponto de acesso** (*access point*, AP) liga os aparelhos sem fio à rede cabeada.

Com o EAP, o ponto de acesso repassa as credenciais do usuário a um servidor de autenticação, que libera ou não a conexão. Os métodos usados são:

| Método | Certificado no cliente | Certificado no servidor | Implantação | Segurança |
| --- | --- | --- | --- | --- |
| EAP-TLS | Sim | Sim | Difícil | Alta |
| PEAP | Não | Sim | Moderada | Média |
| EAP-TTLS | Não | Sim | Moderada | Média |
| EAP-FAST | Não | Não | Fácil | Média |

O **EAP-TLS é o mais seguro e o mais difícil de implantar**, porque exige certificado nas duas pontas.

### 17.3 Pontos de Acesso Não Autorizados e Autenticação Mútua

Um **ponto de acesso não autorizado** (*rogue AP*) **imita um ponto de acesso legítimo** para que as vítimas se conectem a ele e tenham os dados roubados.

A proteção é a **autenticação mútua**: **as duas pontas se autenticam antes de se conectar**, e o cliente percebe quando o ponto de acesso é falso.

### 17.4 Comunicação dos Dispositivos Móveis

| Método | Como funciona | Exemplo |
| --- | --- | --- |
| Wi-Fi e Bluetooth | Sinais sem fio | Fone de ouvido |
| NFC (*Near-Field Communication*) | Curtíssimo alcance | Pagamento por aproximação |
| Infravermelho (IR) | Curto alcance | Controlar a TV |
| USB | Com fio | Armazenamento |

### 17.5 Gerenciamento de Dispositivos Móveis

No **COPE** (*Corporate-Owned, Personally Enabled*), o aparelho é da empresa e o uso pessoal é permitido; no BYOD, o aparelho é do funcionário.

As principais formas de gerenciamento são:

- **conteinerização**: cria uma área criptografada que **separa os dados da empresa dos dados pessoais** e pode ser apagada à distância;
- **gerenciamento de conteúdo**: controla o que cada usuário acessa em serviços como Google Drive e Dropbox;
- **lista de permissões** (*whitelisting*): só deixa instalar aplicativos autorizados.

### 17.6 Ameaças e Proteções dos Dispositivos Móveis

Alguns usuários **contornam as limitações do aparelho**:

| Técnica | Plataforma | O que faz | Risco |
| --- | --- | --- | --- |
| Jailbreak | Apple | Permite rodar aplicativos não autorizados | Alto |
| Root | Android | Dá acesso administrativo total | Alto |
| Sideloading | Ambas | Instala aplicativos fora da loja oficial | Menor |

As proteções são:

- bloqueio de tela e biometria;
- **limpeza remota**, se o aparelho for perdido ou roubado;
- criptografia completa do dispositivo.

### 17.7 Rastreamento por GPS

O **GPS** (*Global Positioning System*) localiza o aparelho com precisão de cerca de **5 metros**. Com ele, empresas enviam **notificações push** (mensagens que aparecem sem abrir o aplicativo) conforme a localização.

Criminosos também usam **notificações push para capturar dados** dos usuários.

## 18. Resiliência e Alta Disponibilidade

A **resiliência** torna um sistema **tolerante a falhas**: ele continua funcionando quando algo dá errado, inclusive durante um ataque. O objetivo é **reduzir ao mínimo o tempo de inatividade**.

### 18.1 Alta Disponibilidade

Os sistemas de **alta disponibilidade** seguem três princípios:

1. **eliminar os pontos únicos de falha**, com componentes e caminhos redundantes;
2. **garantir uma transição confiável** para os sistemas de reserva;
3. **detectar as falhas assim que ocorrem**.

O **ponto único de falha** (*Single Point of Failure*, SPOF) pode ser um equipamento, um serviço ou até uma pessoa que só ela sabe fazer algo.

Em um **cluster de alta disponibilidade**, vários computadores atendem o mesmo serviço; se um falha, os outros continuam.

### 18.2 Os Cinco Noves

Os **cinco noves** são **99,999% de disponibilidade**, ou **menos de 5,26 minutos de inatividade por ano**.

#### 18.2.1 Exemplo Resolvido: Tempo de Inatividade nos Cinco Noves

| Etapa | Cálculo | Resultado |
| --- | --- | --- |
| Minutos no ano | 365 × 24 × 60 | 525.600 min |
| Fração de inatividade | 100% − 99,999% = 0,001% | 0,00001 |
| Inatividade máxima | 525.600 × 0,00001 | 5,256 ≈ 5,26 min |

Para chegar aos cinco noves, usam-se sistemas padronizados, **clustering** e componentes que substituem uns aos outros.

### 18.3 Redundância N+1

Na **redundância N+1**, os componentes necessários (N) têm **pelo menos um componente de reserva (+1)**, como os quatro pneus e o estepe de um carro.

**Observação:** o N+1 suporta a perda de um componente, não de todos.

### 18.4 RAID

O **RAID** (*Redundant Array of Independent Disks*) **distribui os dados entre vários discos**, combinando três técnicas:

| Técnica | Como funciona | Protege contra falha de disco? |
| --- | --- | --- |
| Espelhamento | Grava os dados duplicados em outro disco | Sim |
| Distribuição (*striping*) | Espalha os dados por vários discos | Não, sozinha |
| Paridade | Guarda somas de verificação para reconstruir os dados | Sim |

**Importante:** o **RAID 0 usa apenas distribuição e não tem redundância**. Quem protege contra falha de disco são o RAID 1 (espelhamento) e o RAID 5 (paridade).

### 18.5 Spanning Tree Protocol (STP)

Cabos redundantes entre switches protegem contra falhas, mas criam **loops**: os quadros circulam sem parar e derrubam a rede.

O **STP** (*Spanning Tree Protocol*) **bloqueia de propósito os caminhos redundantes**, deixando um só caminho ativo. Se o caminho ativo falha, o STP libera o bloqueado.

### 18.6 Redundância de Roteador

O **gateway padrão** é o roteador que dá acesso às outras redes. Sozinho, ele é um ponto único de falha.

Com um roteador de reserva, os dois compartilham um **endereço IP virtual**, e os dispositivos usam esse **IP virtual como gateway padrão**. Se o ativo cai, o de reserva assume o mesmo IP, sem mudar nada nos computadores.

Essa recuperação automática é a **redundância de primeiro salto**. Protocolos que a oferecem: HSRP (Cisco), VRRP e GLBP.

### 18.7 Redundância de Local

| Replicação | Sincronização | Largura de banda | Distância entre locais |
| --- | --- | --- | --- |
| Síncrona | Em tempo real | Alta | Pequena |
| Assíncrona | Quase em tempo real | Menor | Maior |
| Ponto no tempo | Periódica | A menor | Qualquer |

### 18.8 Design Resiliente

O **design resiliente** é **mais do que adicionar redundância**: é ajustar a rede às necessidades do negócio para que a recuperação seja rápida.

Na resiliência de aplicativos, **quanto maior a disponibilidade, maiores a complexidade e o custo**:

| Solução | Complexidade e custo |
| --- | --- |
| Hardware tolerante a falhas | Os maiores |
| Arquitetura de cluster | Intermediários |
| Backup e restauração | Os menores |

Nos equipamentos Cisco, a **configuração resiliente do IOS** guarda uma cópia protegida do sistema e da configuração, que o usuário não consegue apagar (comandos secure boot-image e secure boot-config).

### 18.9 Backups

O **backup** é **uma das formas mais eficazes de proteger contra a perda de dados**. Ao planejá-lo, considera-se:

- a frequência dos backups completos e parciais;
- a guarda das cópias em local externo;
- a proteção com senha;
- a verificação regular da integridade.

### 18.10 Energia

Um data center precisa de fontes redundantes, energia de reserva e **nobreak** (UPS, *Uninterruptible Power Supply*).

| Categoria | Evento | O que é |
| --- | --- | --- |
| Excesso | Pico (*spike*) | Alta tensão momentânea |
| Excesso | Sobretensão (*surge*) | Alta tensão prolongada |
| Perda | Falha (*fault*) | Perda momentânea |
| Perda | Blecaute | Perda completa |
| Degradação | Afundamento (*sag*) | Baixa tensão momentânea |
| Degradação | Subtensão (*brownout*) | Baixa tensão prolongada |

**Importante:** **pico** e **afundamento** são **momentâneos**; **sobretensão** e **subtensão** são **prolongadas**.

### 18.11 Climatização (HVAC)

O **HVAC** (*Heating, Ventilation and Air Conditioning*) controla **temperatura, umidade e circulação do ar** dos equipamentos.

Os sistemas modernos de HVAC ficam conectados à internet e são acessados por terceiros, o que pode abrir uma porta de entrada para a rede.

## 19. Sistemas Embarcados, IoT e Tecnologias de Dissimulação

As redes ligam hoje **máquinas industriais, sensores, carros e equipamentos médicos**. Esses sistemas têm fragilidades próprias e ampliam a superfície de ataque.

### 19.1 Infraestruturas Críticas e SCADA

O **SCADA** (*Supervisory Control and Data Acquisition* — controle de supervisão e aquisição de dados) serve para **controlar e monitorar processos industriais**. Ele faz parte dos **ICS** (*Industrial Control Systems* — sistemas de controle industrial), usados em energia, manufatura e transportes.

O ataque **Stuxnet**, em 2010, mirou sistemas SCADA e mostrou que um ataque digital pode destruir infraestruturas.

Os sistemas SCADA são vulneráveis porque **foram projetados sem conexão com a rede corporativa e a internet**. Hoje, ao serem ligados à rede da empresa, o risco aumenta.

A principal proteção é **separar a rede SCADA da rede local da empresa**.

### 19.2 Internet das Coisas (IoT)

A **IoT** (*Internet of Things* — Internet das Coisas) **conecta objetos variados à internet**, como câmeras, fechaduras, lâmpadas e sensores. Esses dispositivos **aumentam o número de pontos de entrada na rede**.

Aparelhos IoT infectados já foram usados em grandes ataques **DDoS** (*Distributed Denial of Service*, em que muitos aparelhos atacam um alvo ao mesmo tempo). Por isso:

- verificar se o dispositivo aceita atualizações de firmware;
- **trocar sempre as credenciais padrão de administrador**.

Muitos dispositivos IoT usam um **RTOS** (*Real-Time Operating System* — sistema operacional de tempo real), que prioriza o tempo exato de resposta. Ele é vulnerável a injeção de código e a negação de serviço.

O **Shodan** é um buscador que mostra dispositivos IoT expostos na internet.

### 19.3 Sistemas Embarcados

Os **sistemas embarcados** são computadores dedicados a uma função dentro de outro equipamento, como TVs inteligentes e carros.

Eles sofrem **ataques de tempo**: o atacante mede **quanto tempo o sistema leva para responder** para descobrir fraquezas. É um **ataque de canal lateral**, que explora informações que vazam do funcionamento físico, como tempo e consumo de energia.

Muitos usam **SoC** (*System on Chip*), placas pequenas como o Raspberry Pi e o Arduino, ou **FPGA**, circuitos reprogramáveis.

Muitos dispositivos SoC têm **autenticação fraca e não podem ser atualizados ou corrigidos**.

### 19.4 Voz sobre IP (VoIP)

O **VoIP** (*Voice over IP* — voz sobre IP) **usa redes de dados para fazer ligações telefônicas**. Sua segurança **depende da segurança da rede por baixo dele**.

As medidas de proteção são:

- criptografar os pacotes de voz;
- trocar todas as senhas padrão;
- usar autenticação forte contra o sequestro e o desvio de chamadas;
- usar firewalls que reconheçam o tráfego de VoIP.

### 19.5 Sistemas de Finalidade Específica

| Setor | Exemplos | Riscos |
| --- | --- | --- |
| Saúde | Marca-passos e bombas de insulina conectados | Segurança do paciente e vazamento de prontuários |
| Automotivo | Sistemas que registram velocidade e localização | Rastreamento e falsificação |
| Aviação | Controle de voo | Credenciais fixas no código e *backdoors* |
| Drones (UAV) | Vigilância e mapeamento | Sequestro e falsificação de GPS |

Um **backdoor** (porta dos fundos) é um acesso escondido que contorna a autenticação.

### 19.6 Tecnologias de Dissimulação

As **tecnologias de dissimulação** (*deception*) acrescentam **uma camada falsa à infraestrutura** para enganar o atacante.

| Tecnologia | O que é |
| --- | --- |
| Honeypot | Sistema-isca exposto de propósito, que registra as ações do atacante |
| Honeynet | Conjunto de honeypots que imita uma rede |
| Honey files | Arquivos falsos, sem informação real |
| DNS sinkhole | Impede o acesso a sites maliciosos pelo nome |

O objetivo do honeypot é **desviar o atacante dos recursos reais e revelar como ele age**.

## 20. Listas de Controle de Acesso (ACLs) e Máscaras Curinga

Um condomínio fechado tem um porteiro que só abre o portão para quem está na lista. Na rede, esse porteiro é a **ACL**, que decide quais pacotes passam por um roteador.

### 20.1 O que é uma ACL

A **ACL** (*Access Control List* — lista de controle de acesso) é uma **série de comandos que filtra pacotes de acordo com as informações do cabeçalho**. Cada linha é uma instrução de permitir (*permit*) ou negar (*deny*), chamada de **ACE** (*Access Control Entry*).

Com a ACL aplicada a uma interface, o roteador **compara cada pacote que passa com as ACEs, em ordem**. Essa é a **filtragem de pacotes**, que atua nas **camadas 3 e 4** do modelo OSI.

Usos comuns:

- limitar o tráfego, bloqueando vídeo, por exemplo;
- dar segurança básica, liberando a rede do RH só para pessoas autorizadas;
- permitir e-mail e negar Telnet;
- dar prioridade ao tráfego de voz.

### 20.2 Tipos de ACL

Os roteadores Cisco têm dois tipos de ACL IPv4:

- **ACL padrão**: filtra **apenas pelo endereço IPv4 de origem**;
- **ACL estendida**: filtra pelos endereços de **origem e/ou destino**, pelas portas e pelo protocolo.

As **ACLs nomeadas** são o **método preferido**, porque o nome mostra a finalidade. Exemplo: FTP-FILTER. Os nomes não têm espaços e costumam ser escritos em MAIÚSCULAS.

| Característica | ACL padrão | ACL estendida |
| --- | --- | --- |
| Camadas analisadas | 3 | 3 e 4 |
| Endereço | Só origem | Origem e/ou destino |
| Portas e protocolo | Não | Sim |
| Números | 1–99 e 1300–1999 | 100–199 e 2000–2699 |

### 20.3 Como a ACL Processa os Pacotes

A ACL pode filtrar em dois sentidos:

- **de entrada** (*inbound*): antes do roteamento; é mais eficiente, porque o pacote descartado nem é roteado;
- **de saída** (*outbound*): depois do roteamento, para pacotes que saem pela interface.

O processo de uma ACL padrão é:

1. o roteador lê o endereço de origem do pacote;
2. compara com cada ACE, **de cima para baixo**;
3. **na primeira correspondência**, permite ou nega e para de comparar;
4. se nada corresponder, descarta o pacote.

Toda ACL termina com uma **negação implícita**, que **nega tudo o que não foi permitido**.

**Importante:** por isso, **toda ACL precisa ter pelo menos uma instrução de permitir**.

**Observação:** as ACLs não filtram os pacotes criados pelo próprio roteador.

### 20.4 Máscaras Curinga

A **máscara curinga** (*wildcard mask*) **indica quais bits do endereço devem ser verificados**.

Na máscara de sub-rede, que indica qual parte do endereço IP identifica a rede, o bit 1 marca a rede. A máscara curinga segue a **lógica inversa**:

- bit **0** → o bit do endereço **precisa corresponder**;
- bit **1** → o bit do endereço é ignorado.

| Máscara curinga | Último octeto em binário | Efeito no último octeto |
| --- | --- | --- |
| 0.0.0.0 | 00000000 | Verifica todos os bits |
| 0.0.0.15 | 00001111 | Verifica os 4 primeiros e ignora os 4 últimos |
| 0.0.0.63 | 00111111 | Verifica os 2 primeiros e ignora os 6 últimos |
| 0.0.0.255 | 11111111 | Ignora o octeto inteiro |

Exemplos:

- um host: `access-list 10 permit 192.168.1.1 0.0.0.0`;
- uma sub-rede: `access-list 10 permit 192.168.1.0 0.0.0.255`, de 192.168.1.0 a 192.168.1.255.

### 20.5 Exemplo Resolvido: Cálculo de Máscaras Curinga

O atalho é **subtrair a máscara de sub-rede de 255.255.255.255**, octeto por octeto.

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

- **host** → equivale à máscara **0.0.0.0**: **um único endereço**. Exemplo: `permit host 192.168.10.10`;
- **any** → **qualquer endereço**. Exemplo: `permit any`.

## 21. Configuração e Aplicação de ACLs

Com a lógica da ACL e das máscaras curinga entendida, falta escrever a lista no roteador, aplicá-la no lugar certo e corrigi-la quando preciso.

### 21.1 Planejamento

A ACL deve ser preparada antes de ser digitada:

1. escrever em um editor de texto o que a política deve fazer;
2. acrescentar os comandos e comentários (*remarks*);
3. colar os comandos no dispositivo;
4. testar com cuidado.

### 21.2 ACL Padrão

A ACL padrão numerada é criada com:

`access-list número {deny | permit | remark texto} origem [curinga] [log]`

A origem pode ser um endereço, **host** com um endereço, ou **any**. Sem curinga, vale 0.0.0.0. A opção **log** registra cada correspondência, mas **consome muito processamento**.

A ACL padrão nomeada é criada com `ip access-list standard NOME`, e as ACEs são digitadas em seguida.

### 21.3 ACL Estendida

A ACL estendida numerada é criada com:

`access-list número {deny | permit} protocolo origem curinga [operador porta] destino curinga [operador porta] [established]`

O protocolo pode ser **ip** (todos), **tcp**, **udp** ou **icmp**. Os operadores são **eq** (igual), **neq** (diferente), **lt** (menor) e **gt** (maior).

| Nome | Porta | Serviço |
| --- | --- | --- |
| ftp-data / ftp | 20 / 21 | FTP |
| telnet | 23 | Telnet |
| smtp | 25 | Envio de e-mail |
| domain | 53 | DNS |
| www | 80 | HTTP |
| pop3 | 110 | Recebimento de e-mail |

O SSH (22) e o HTTPS (443) **não têm nome na lista** e precisam ser escritos pelo número.

A ACL estendida nomeada é criada com `ip access-list extended NOME`. Exemplo que só deixa a rede 192.168.10.0/24 navegar na web:

```
ip access-list extended SURFING
 permit tcp 192.168.10.0 0.0.0.255 any eq 80
 permit tcp 192.168.10.0 0.0.0.255 any eq 443
```

### 21.4 A Palavra-chave established

A palavra-chave **established** deixa o tráfego interno sair e **apenas as respostas a esse tráfego voltem**.

Uma conexão TCP é aberta com o *three-way handshake* (troca de três mensagens: SYN, SYN-ACK e ACK). Depois disso, os segmentos levam o sinalizador ACK. O established aceita os segmentos com **ACK ou RST** ativado, ou seja, de conexões já abertas. Conexões iniciadas de fora são negadas.

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

Nas linhas VTY, que controlam o acesso remoto ao roteador, usa-se `access-class`:

```
ip access-list standard VTY_ACCESS
 permit 192.168.10.10
 deny any
line vty 0 4
 access-class VTY_ACCESS in
```

O comando `show access-lists` mostra as ACLs e quantas vezes cada ACE foi usada.

### 21.6 Modificação de ACLs

Há dois métodos para corrigir uma ACL:

- **editor de texto**: copiar a ACL, corrigi-la, apagar a antiga no roteador e colar a nova;
- **número de sequência**: apagar a entrada pelo número (10, 20, 30...) e digitá-la de novo com o mesmo número.

No método do editor, **a ACL antiga precisa ser apagada antes**; senão, as linhas novas só se somam às antigas.

### 21.7 Diretrizes e Posicionamento

As diretrizes principais são:

- a ordem importa: a leitura para na primeira correspondência;
- organizar **do mais específico ao mais genérico**;
- novas ACEs entram no final da lista;
- **uma ACL por interface, por protocolo e por direção**.

O posicionamento segue a regra:

- **ACL estendida** → o **mais perto possível da origem**, para o tráfego indesejado não atravessar a rede;
- **ACL padrão** → o **mais perto possível do destino**, porque ela só enxerga a origem e, perto dela, bloquearia todos os destinos.

Exemplos:

- ACL padrão que impede 192.168.10.0/24 de alcançar 192.168.30.0/24 → na saída da interface ligada à rede 192.168.30.0/24;
- ACL estendida que impede 192.168.11.0/24 de usar Telnet com 192.168.30.0/24 → na entrada da interface ligada à rede 192.168.11.0/24.

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

Na **falsificação de IP** (*IP spoofing*), o atacante **coloca um endereço de origem falso no cabeçalho**.

A interface voltada para a internet **nunca deve aceitar pacotes com estes endereços de origem**:

- 0.0.0.0 e 255.255.255.255;
- *loopback* (127.0.0.0/8);
- APIPA (169.254.0.0/16), criado pelo computador quando não recebe IP;
- privados (10.0.0.0/8, 172.16.0.0/12 e 192.168.0.0/16);
- multicast (224.0.0.0/4).

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

A ACL de entrada deve **deixar passar apenas o tráfego dos serviços que realmente são usados**: DNS, SMTP e FTP para os servidores públicos e SSH, syslog (envio de registros de eventos a um servidor) e SNMP para a administração.

```
access-list 180 permit udp any host 192.168.20.2 eq domain
access-list 180 permit tcp any host 192.168.20.2 eq smtp
access-list 180 permit tcp any host 192.168.20.2 eq ftp
access-list 180 permit tcp host 200.5.5.5 host 10.0.1.1 eq 22
```

### 22.3 Controle do ICMP

O **ICMP** envia mensagens de erro e de teste, como as do ping. Os atacantes usam o **echo** para descobrir hosts e para inundações, e o **redirect** para alterar a tabela de roteamento dos hosts. Por isso, **echo e redirect devem ser bloqueados na entrada**.

| Sentido | Mensagens permitidas |
| --- | --- |
| Entrando na rede | echo-reply, source-quench, unreachable |
| Saindo da rede | echo, parameter-problem, packet-too-big, source-quench |

```
access-list 112 permit icmp any any echo-reply
access-list 112 permit icmp any any source-quench
access-list 112 permit icmp any any unreachable
access-list 112 deny icmp any any
access-list 112 permit ip any any
```

### 22.4 Proteção do SNMP

Uma ACL pode filtrar o **SNMP**, mas pacotes falsificados ainda passam. O mais eficaz é **desativar o SNMP quando ele não for necessário**, com `no snmp-server`.

### 22.5 Riscos da Transição para o IPv6

Na **pilha dupla** (*dual stack*), o dispositivo tem **conectividade IPv4 e IPv6 ao mesmo tempo**, e um firewall só de IPv4 não enxerga o tráfego IPv6.

Um exemplo de ataque usa o **Teredo**, técnica que dá IPv6 a hosts atrás de um NAT IPv4 (a tradução que faz vários endereços internos saírem com um único endereço público), **encapsulando o IPv6 dentro de pacotes UDP IPv4**:

1. o atacante envia anúncios de roteador IPv6 falsos (mensagens que informam aos hosts o prefixo e o gateway);
2. os hosts se configuram com IPv6 sem ninguém perceber;
3. o firewall IPv4 só vê UDP comum, e o atacante avança.

A defesa é filtrar o IPv6 na borda com ACLs IPv6.

### 22.6 ACLs IPv6

As ACLs IPv6 têm diferenças importantes:

- **não existe ACL IPv6 padrão**: todas são nomeadas e parecidas com a estendida;
- são criadas com `ipv6 access-list NOME`;
- são aplicadas com `ipv6 traffic-filter NOME {in | out}`.

Elas terminam com três entradas implícitas: `permit icmp any any nd-na`, `permit icmp any any nd-ns` e `deny ipv6 any any`. As duas primeiras permitem as mensagens de vizinho do **NDP** (*Neighbor Discovery Protocol*), que no IPv6 faz o papel do ARP.

**Importante:** um `deny ipv6 any any` escrito sem antes permitir nd-na e nd-ns faz o **NDP para de funcionar**.

| Característica | ACL IPv4 | ACL IPv6 |
| --- | --- | --- |
| Tipos | Padrão e estendida | Só um tipo |
| Identificação | Número ou nome | Só nome |
| Aplicação | `ip access-group` | `ipv6 traffic-filter` |
| Final implícito | Nega tudo | Permite nd-na e nd-ns e nega o resto |

## 23. Tecnologias de Firewall

A ACL filtra pacote por pacote. O **firewall** vai além: ele serve para **controlar o tráfego entre redes com níveis de confiança diferentes**.

### 23.1 Características do Firewall

Todo firewall:

- é resistente a ataques;
- é o **único ponto de trânsito** entre a rede interna e a externa;
- aplica a política de acesso da organização.

Seus benefícios são:

- não expor recursos sensíveis a usuários não confiáveis;
- impedir que falhas dos protocolos sejam exploradas;
- concentrar o controle de acesso em poucos equipamentos.

Suas limitações são:

- mal configurado, vira um **ponto único de falha**;
- pode reduzir o desempenho;
- tráfego malicioso pode passar escondido em tráfego legítimo.

### 23.2 Tipos de Firewall

Os firewalls se dividem em quatro tipos principais:

- **filtragem de pacotes** (sem estado): analisa IPs, portas e protocolo nas camadas 3 e 4, com regras fixas;
- **com estado** (*stateful*): o mais comum; mantém uma **tabela de estado** com as conexões em andamento;
- **gateway de aplicação** (*proxy*): **o proxy se conecta ao servidor em nome do cliente**, e o servidor só enxerga o proxy;
- **NGFW** (*Next-Generation Firewall* — firewall de última geração): acrescenta prevenção de intrusão e **reconhecimento e controle de aplicativos**.

Também existem o firewall **baseado em host**, instalado no próprio computador, o **transparente** e o **híbrido**, que combina tipos.

| Tipo | Camadas analisadas | Como decide |
| --- | --- | --- |
| Filtragem de pacotes | 3 e 4 | Regras fixas, pacote por pacote |
| Com estado | 3, 4 e 5 | Regras + tabela de conexões |
| Gateway de aplicação | 3, 4, 5 e 7 | Intermedia a conexão |
| NGFW | Até a 7 | Estado + aplicativos + prevenção de intrusão |

### 23.3 Firewall de Filtragem de Pacotes

Vantagens:

- regras simples;
- **baixo impacto no desempenho**;
- disponível na maioria dos roteadores, a baixo custo.

Desvantagens:

- é enganado pela falsificação de IP;
- filtra mal pacotes fragmentados;
- ACLs complexas são difíceis de manter;
- **não guarda estado**: analisa cada pacote isoladamente.

### 23.4 Firewall com Estado

O firewall com estado é o **principal meio de defesa** de muitas redes.

Benefícios:

- filtragem mais rigorosa e bom desempenho;
- **defende contra falsificação e negação de serviço**, porque confere se o pacote pertence a uma conexão;
- logs mais ricos.

Limitações:

- **não inspeciona a camada de aplicação**, como o conteúdo de uma página;
- acompanha mal o UDP e o ICMP, que não têm conexão;
- não autentica usuários.

### 23.5 Firewalls no Projeto de Rede

Com **duas interfaces**, o firewall separa a rede privada, confiável, da pública:

- privada → pública: permitido e inspecionado, com as respostas;
- pública → privada: bloqueado.

Com a DMZ, o firewall passa a ter **três interfaces**:

| Origem → Destino | Tratamento |
| --- | --- |
| Privada → pública ou DMZ | Inspecionado, com pouca restrição |
| DMZ → privada | Bloqueado |
| DMZ → pública | Permitido seletivamente |
| Pública → DMZ | Permitido seletivamente (e-mail, DNS, HTTP, HTTPS) |
| Pública → privada | Bloqueado |

### 23.6 Defesa em Camadas com Firewalls

A defesa em camadas combina **tipos diferentes de firewall**. Na **sub-rede rastreada** (*screened subnet*), o tráfego passa por várias barreiras:

Internet → Roteador de borda → Firewall ou host bastião → Roteador interno → Host de destino

O **host bastião** é um computador **reforçado para resistir a ataques**, normalmente na DMZ.

### 23.7 Limites e Boas Práticas

O firewall não impede ataques entre hosts da mesma rede, não detecta pontos de acesso sem fio não autorizados e não substitui o backup nem usuários bem informados.

As boas práticas são:

- **negar todo o tráfego por padrão** e liberar só o necessário;
- controlar o acesso físico ao firewall;
- monitorar os logs;
- controlar as mudanças na configuração.

## 24. Firewall de Política Baseada em Zona (ZPF)

Os roteadores Cisco também funcionam como firewall com estado, em dois modelos:

- **clássico**: a política é aplicada em cada interface;
- **ZPF** (*Zone-Based Policy Firewall*): as interfaces formam zonas, e a política é aplicada **ao tráfego que passa de uma zona para outra**.

### 24.1 Zonas de Segurança

Uma **zona** é um **grupo de uma ou mais interfaces com funções e necessidades de segurança semelhantes**, como privada, pública e DMZ.

As regras básicas são:

- **mesma zona** → o tráfego passa livremente;
- **zonas diferentes** → o tráfego é **bloqueado**, a menos que uma política o permita.

Uma interface nova colocada em uma zona já segue as regras dela.

A **zona self** é **o próprio roteador**. Por padrão, o tráfego de e para o roteador passa; só é filtrado se houver um par de zonas com a self.

### 24.2 Benefícios do ZPF

Seus benefícios são:

- não depende de ACLs;
- a postura padrão é **bloquear tudo o que não for explicitamente permitido**;
- as políticas são fáceis de ler;
- cada política vale em **um único sentido** entre duas zonas.

Os dois modelos podem existir no mesmo roteador, mas **não na mesma interface**.

### 24.3 Projeto do ZPF

1. determinar as zonas;
2. definir as políticas para cada **par de zonas** (*zone pair*), origem → destino;
3. projetar a infraestrutura física, com redundância.

### 24.4 Ações do ZPF

- **Inspect**: inspeção com estado, **permitindo automaticamente as respostas**;
- **Drop**: descarta; é a ação padrão;
- **Pass**: permite **sem estado e em um único sentido**; o retorno exige outra política.

O Drop descarta em silêncio, **sem enviar a mensagem ICMP de destino inalcançável**, diferentemente da ACL.

### 24.5 Regras para o Tráfego que Atravessa o Roteador

| Interface de origem em zona? | Interface de destino em zona? | Situação | Resultado |
| --- | --- | --- | --- |
| Não | Não | Nenhuma usa ZPF | Passa |
| Sim | Não | Uma só está em zona | Descarta |
| Não | Sim | Uma só está em zona | Descarta |
| Sim | Sim | Mesma zona | Passa |
| Sim | Sim | Zonas diferentes, sem par ou sem política | Descarta |
| Sim | Sim | Zonas diferentes, com par e política | Segue a política |

**Observação:** no curso, o caso "par sem política" aparece como "Passa"; segundo a documentação da Cisco, o tráfego é descartado.

**Importante:** o tráfego **nunca flui entre uma interface que está em zona e outra que não está**.

### 24.6 Configuração do ZPF

A configuração segue cinco etapas, nesta ordem:

Zonas → class-map → policy-map → zone-pair → Interfaces nas zonas

#### 24.6.1 Exemplo Resolvido: Rede Privada Acessando a Web

A interface GigabitEthernet0/0 fica na zona privada e a Serial0/0/0, na pública.

1. Criar as zonas:

```
zone security PRIVATE
zone security PUBLIC
```

2. Identificar o tráfego. **match-any** exige **pelo menos um** critério; **match-all**, **todos**:

```
class-map type inspect match-any HTTP-TRAFFIC
 match protocol http
 match protocol https
 match protocol dns
```

3. Definir a ação:

```
policy-map type inspect PRIV-TO-PUB-POLICY
 class type inspect HTTP-TRAFFIC
  inspect
```

4. Criar o par de zonas:

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

Resultado: o tráfego web da zona privada é inspecionado, e da pública **só entram as respostas das sessões abertas pela zona privada**.

### 24.7 Verificação e Cuidados

Os comandos `show zone security`, `show zone-pair security` e `show policy-map type inspect zone-pair sessions` mostram as zonas, os pares e as sessões inspecionadas.

Cuidados:

- o ZPF **nunca filtra o tráfego entre interfaces da mesma zona**;
- uma interface pertence a uma única zona;
- o ZPF só protege o próprio roteador se houver pares com a zona self.

| Característica | Firewall clássico | ZPF |
| --- | --- | --- |
| Onde a política é aplicada | Em cada interface | Entre zonas |
| Depende de ACLs | Sim | Não |
| Interface nova | Precisa de configuração | Herda as regras da zona |

## 25. Virtualização e Computação em Nuvem

Boa parte dos servidores das empresas hoje é virtual ou fica na nuvem. Para proteger esse ambiente, é preciso entender como ele funciona.

### 25.1 Virtualização e Hypervisor

A **virtualização** permite **executar vários computadores virtuais em uma única máquina física**. Cada um é uma **máquina virtual** (**VM**, *Virtual Machine*), com o próprio sistema operacional.

O **hypervisor** é o software que executa as VMs. Existem dois tipos:

- **tipo 1** (*bare metal*): **roda diretamente sobre o hardware**; exemplos: VMware ESXi e Hyper-V, usados nos data centers;
- **tipo 2** (hospedado): é **um aplicativo instalado sobre um sistema operacional comum**; exemplos: VirtualBox e VMware Workstation.

A VM **precisa de atualizações e correções como um computador físico**. Comprometer uma VM pode levar a comprometer o host.

### 25.2 Contêineres e Desktops Virtuais

O **contêiner** leva **só o aplicativo e as dependências** e **compartilha o núcleo do sistema operacional do host**. O **Docker** cria contêineres, e o **Kubernetes** gerencia muitos ao mesmo tempo.

A **VDI** (*Virtual Desktop Infrastructure*) guarda **o ambiente de trabalho do usuário em um servidor remoto**, acessado por um equipamento simples (*thin client*).

| Característica | Máquina virtual | Contêiner |
| --- | --- | --- |
| O que leva | Sistema operacional completo | Só o aplicativo e as dependências |
| Núcleo do sistema | Próprio | Compartilhado com o host |
| Peso | Maior | Menor |

### 25.3 Riscos da Virtualização

- **expansão de VMs** (*VM sprawl*): acúmulo de **VMs esquecidas ou subutilizadas**, sem atualização;
- **fuga de VM** (*VM escape*): a VM **rompe o isolamento e passa a interagir com o sistema operacional do host**.

### 25.4 Modelos de Serviço em Nuvem

A **computação em nuvem** oferece **computação, armazenamento e software pela internet**, nos modelos **XaaS** (*Anything as a Service*):

- **SaaS** (*Software as a Service*): software pronto, como o webmail;
- **PaaS** (*Platform as a Service*): ferramentas para **desenvolver e publicar aplicativos**;
- **IaaS** (*Infrastructure as a Service*): **recursos de computação virtualizados**, como servidores e armazenamento.

### 25.5 Modelos de Implantação

| Modelo | Quem usa | Característica principal |
| --- | --- | --- |
| Privada | Uma organização | Mais controle e mais custo |
| Pública | Clientes de um provedor | Mais barata, menos controle |
| Híbrida | Uma organização, combinando as duas | Dados sensíveis sob controle próprio |
| Comunitária | Empresas do mesmo setor | Plataforma compartilhada |

### 25.6 Computação em Neblina e de Borda

Quando milissegundos importam, como em carros autônomos, o processamento fica perto dos dados:

- **neblina** (*fog*): em um equipamento da rede local, como um gateway IoT;
- **borda** (*edge*): **no próprio dispositivo ou sensor**.

## 26. Segurança na Nuvem

Um recurso de nuvem comprometido permite ao atacante atacar outras organizações e hospedar malware em um provedor respeitado, o que faz o conteúdo parecer legítimo.

### 26.1 Principais Ameaças

As principais ameaças são:

- vazamento de dados;
- **configuração incorreta** dos serviços;
- **credenciais de contas comprometidas**: quem sequestra a conta de serviço controla tudo;
- ameaça interna;
- **APIs inseguras**, que são os pontos mais expostos.

Uma **API** (*Application Programming Interface*) é o conjunto de comandos pelo qual programas se comunicam com o serviço.

### 26.2 Responsabilidade Compartilhada

Na nuvem pública, a segurança é **dividida entre o cliente e o provedor** (**CSP**, *Cloud Service Provider*). Quanto mais pronto o serviço, mais responsabilidade fica com o provedor:

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

A **CSA** (*Cloud Security Alliance*) organiza a segurança em nuvem em 14 domínios, como governança, conformidade, resposta a incidentes e identidade e acesso. Para a CSA, a **criptografia é um dos controles mais importantes**.

### 26.4 Segurança da Infraestrutura em Nuvem

Na nuvem, não é possível instalar um equipamento de segurança no meio do cabo. Usam-se equipamentos virtuais e agentes de software.

A **SDN** (*Software-Defined Networking* — rede definida por software) facilita o isolamento, porque **as redes são criadas e separadas por software**. Os firewalls de SDN se chamam **grupos de segurança**.

As proteções mais usadas são:

- **VPC** (*Virtual Private Cloud* — nuvem privada virtual): sub-redes **isoladas da internet** dentro da nuvem pública;
- firewalls virtuais e logs de fluxo;
- VPN entre a nuvem, os escritórios e o data center;
- **IAM** (*Identity and Access Management* — gerenciamento de identidade e acesso), essencial na nuvem.

A **microssegmentação** divide a rede em **muitas redes menores e isoladas**, sem custo de hardware.

A **TI invisível** (*shadow IT*) são serviços adotados pelos usuários sem autorização. A resposta são políticas claras e conscientização.

### 26.5 Proteção dos Dados na Nuvem

Na nuvem, valem as mesmas ferramentas: **criptografia** (AES, RSA) para a confidencialidade e **hash** (SHA-256) para a integridade.

### 26.6 Proteção das Máquinas Virtuais

As medidas principais são:

- dar a cada VM **só o acesso necessário**;
- desativar portas, serviços e contas padrão;
- manter o antimalware atualizado;
- usar firewall de host e sistemas de detecção e de prevenção de intrusão (IDS/IPS).

Além de ficarem vulneráveis, as VMs esquecidas **continuam consumindo serviços pagos**. Por isso, os recursos precisam ser registrados e auditados.

## 27. Protocolos e Tecnologias no Monitoramento de Segurança

O **monitoramento de segurança** observa o tráfego e os registros da rede para **identificar ataques e comportamentos suspeitos**. Os protocolos que ele usa também podem ser mal usados.

### 27.1 Syslog e NTP

O **syslog** é o padrão para **registrar mensagens de eventos** dos equipamentos e enviá-las a um servidor central, na **porta UDP 514**:

Dispositivos → Mensagens de evento → Servidor syslog → Estação de monitoramento

O atacante tenta bloquear o envio, apagar ou adulterar os logs para esconder seus rastros.

O **NTP** (porta UDP 123) mantém os relógios iguais. Só assim é possível **juntar os rastros de um mesmo ataque registrados em equipamentos diferentes**. O atacante pode corromper a hora para confundir a investigação.

### 27.2 DNS

Como o DNS é usado o tempo todo, é pouco vigiado. Os atacantes aproveitam isso para **esconder outros protocolos dentro do DNS**, falar com o servidor de **comando e controle** (**C&C**, o computador que dá ordens ao malware) e retirar dados.

Na retirada de dados pelo DNS:

1. o malware codifica os dados roubados para escapar do **DLP** (*Data Loss Prevention* — prevenção de perda de dados);
2. coloca os dados no lugar do subdomínio, como em "dados-codificados.example.com";
3. o servidor DNS do atacante grava o subdomínio e reúne os dados.

O sinal mais claro são **subdomínios muito mais longos que o normal** ou aleatórios. Serviços como o **Cisco Umbrella** bloqueiam domínios de comando e controle.

### 27.3 HTTP e HTTPS

O **HTTP** trafega **em texto claro**. Um ataque comum é a **injeção de iFrame**: o atacante invade um site e planta um **quadro invisível** que baixa malware para quem visita a página.

O **HTTPS** acrescenta a criptografia **SSL/TLS**. Usando a chave pública, a chave simétrica e o certificado, a conexão ocorre assim:

1. o navegador pede a página;
2. o servidor envia seu certificado, que contém a chave pública;
3. o navegador confere se o certificado é válido e confiável;
4. os dois combinam uma chave simétrica;
5. a página trafega criptografada com essa chave.

O HTTPS **protege os dados apenas no caminho**, não o servidor. Para quem monitora, ele dificulta a inspeção do tráfego.

### 27.4 E-mail e ICMP

- **SMTP** (envio): pouco monitorado, é usado para retirar dados;
- **POP3 e IMAP** (recebimento): **trazem o malware até o computador** do usuário.

No **tunelamento ICMP**, o malware **transfere arquivos escondidos em pacotes ICMP**, aproveitando que esse tráfego costuma ser ignorado.

### 27.5 ACLs, NAT e PAT

As ACLs podem dar uma **falsa sensação de segurança**: uma ACL que deixa voltar mensagens ICMP também deixa passar um túnel ICMP. Por isso, as regras fixas precisam de reforço com análise de comportamento, como a dos firewalls de última geração.

O **NAT** (*Network Address Translation*) e o **PAT** (*Port Address Translation*) fazem vários endereços internos saírem com um único endereço público.

Com o PAT, todos os dispositivos internos aparecem com o mesmo endereço, o que **dificulta saber qual dispositivo interno fez cada pedido**.

### 27.6 Criptografia e Tunelamento

A **VPN** cria um túnel cifrado pela internet. O malware usa a mesma técnica: um túnel cifrado em um protocolo confiável para retirar dados.

O tráfego TLS não é inspecionado pelos meios normais e pode esconder malware e comando e controle. As medidas são:

- **posicionar o IPS onde ele veja o tráfego já decifrado**;
- validar os certificados (CRL ou OCSP);
- usar equipamentos que decifram o tráfego para inspeção.

### 27.7 P2P e Tor

Nas redes **P2P** (*peer-to-peer*), **cada computador atua ao mesmo tempo como cliente e como servidor**.

O **P2P de arquivos não deve ser permitido em redes corporativas**: contorna o firewall e espalha malware.

O **Tor** permite **navegar de forma anônima**: a mensagem passa por vários retransmissores, e cada um só conhece o próximo salto. Os criminosos o usam como canal de comando e controle e para esconder o destino.

### 27.8 Balanceamento de Carga

O **balanceamento de carga** distribui o tráfego entre vários servidores. Por isso, **uma única transação pode aparecer com vários IPs** nas capturas, e os testes do balanceador podem parecer suspeitos.

| Protocolo ou tecnologia | Mau uso ou dificuldade |
| --- | --- |
| Syslog e NTP | Logs apagados e hora corrompida |
| DNS | Retirada de dados e comando e controle |
| HTTP | Injeção de iFrame |
| HTTPS e VPN | Tráfego cifrado não inspecionado |
| E-mail | Retirada de dados e entrada de malware |
| ICMP | Reconhecimento e tunelamento |
| NAT e PAT | Dispositivo interno escondido |
| P2P e Tor | Contorno do firewall e anonimato |
| Balanceamento de carga | Vários IPs para a mesma transação |

## 28. Tipos de Dados de Segurança

O analista trabalha com dados do mais resumido ao mais detalhado. Muitos são reunidos pelo **Security Onion**, um conjunto gratuito de ferramentas de **NSM** (*Network Security Monitoring* — monitoramento de segurança de rede). Os dados são de cinco tipos.

### 28.1 Dados de Alerta

Os **dados de alerta** são **mensagens geradas por um IDS ou IPS quando o tráfego viola uma regra** ou corresponde a um ataque conhecido. Exemplo: o **Snort**, um IDS de rede gratuito, alerta quando recebe de fora a resposta típica de um acesso de administrador em um Linux.

### 28.2 Dados de Sessão

Os **dados de sessão** são o **registro de uma conversa entre dois endpoints**. Eles guardam **dados sobre a conversa, e não o conteúdo**: quem falou com quem, quanto e por quanto tempo.

Cada sessão é identificada pela **5-tupla**: IP de origem, IP de destino, porta de origem, porta de destino e protocolo. O **Zeek** registra esses dados no log de conexões.

### 28.3 Dados de Transação

Os **dados de transação** são **as mensagens trocadas durante a sessão**. Exemplo: o pedido "GET /index.html" e a resposta "200 OK", gravados no log do servidor.

**Importante:** a **sessão é todo o tráfego** da conversa; a **transação é o próprio pedido** e sua resposta.

### 28.4 Capturas Completas de Pacotes

As **capturas completas de pacotes** guardam **o conteúdo real** do que trafegou, como e-mails e arquivos. São as mais detalhadas, mas exigem **muito mais armazenamento**. Exemplo de ferramenta: Wireshark.

### 28.5 Dados Estatísticos

Os **dados estatísticos** são **criados a partir da análise dos outros dados**. A técnica principal é a **linha de base**:

Comportamento normal → Comparação com o atual → Diferença significativa → Alarme

A **NBA** (*Network Behavior Analysis* — análise de comportamento de rede) e a **NBAD** (*Network Behavior Anomaly Detection*) usam essa ideia, com inteligência artificial, para achar comando e controle e retirada de dados.

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

Um **HIDS** (*Host-based Intrusion Detection System*) é um sistema de detecção de intrusão instalado no próprio computador. Seus logs devem ir para servidores centrais. Exemplos: **OSSEC** e **Tripwire**.

No Windows, o **Visualizador de Eventos** organiza cinco logs:

- aplicativo;
- sistema;
- instalação;
- **segurança**: logons e acessos, com sucesso ou falha de auditoria;
- eventos encaminhados de outros computadores.

O log de segurança é gerado pelo **LSASS** (lsass.exe), que deve rodar da pasta System32.

Um lsass.exe em **outra pasta**, ou disfarçado como **1sass.exe**, **pode ser malware**.

| Tipo de evento | Significado | Exemplo |
| --- | --- | --- |
| Erro | Problema significativo | Um serviço não inicia |
| Aviso | Possível problema futuro | Pouco espaço em disco |
| Informações | Operação bem-sucedida | Driver carregado |
| Sucesso na auditoria | Acesso auditado que deu certo | Logon realizado |
| Falha na auditoria | Acesso auditado que falhou | Acesso negado |

### 29.2 Formato do Syslog

Toda mensagem syslog tem três partes:

PRI (prioridade) → HEADER (data, hora e equipamento) → MSG (texto)

A **PRI** combina dois valores:

- **facilidade**: a categoria da fonte; as facilidades locais, local0 a local7, têm os números 16 a 23;
- **gravidade**: de 0 a 7, e **quanto menor o número, mais grave o evento**.

| Gravidade | Nome | Significado |
| --- | --- | --- |
| 0 | Emergência | Sistema inutilizável |
| 1 | Alerta | Ação imediata necessária |
| 2 | Crítico | Condição crítica |
| 3 | Erro | Erro a resolver |
| 4 | Aviso | Erro futuro se nada for feito |
| 5 | Notificação | Evento normal, mas significativo |
| 6 | Informativo | Operação normal |
| 7 | Depuração | Mensagens para desenvolvedores |

**Prioridade = Facilidade × 8 + Gravidade**

**Observação:** um asterisco (\*) ou um ponto antes da data indica **problema com o NTP**.

#### 29.2.1 Exemplo Resolvido: Cálculo da Prioridade do Syslog

Um firewall envia uma mensagem com a facilidade local4 e gravidade 3 (erro):

| Etapa | Cálculo | Resultado |
| --- | --- | --- |
| Número da local4 | 16 + 4 | 20 |
| Facilidade × 8 | 20 × 8 | 160 |
| Mais a gravidade | 160 + 3 | 163 |
| Início da mensagem | — | <163> |

Nos equipamentos Cisco, a parte MSG tem um padrão próprio:

`*Sep 16 08:50:47.359 EDT: %SYS-5-CONFIG_I: Configured from console by con0`

| Trecho | Significado |
| --- | --- |
| SYS | Facilidade no padrão Cisco |
| 5 | Gravidade (notificação) |
| CONFIG\_I | Código da mensagem |
| Configured from console by con0 | A configuração foi alterada pelo console |

### 29.3 Logs dos Servidores

Os servidores web e de e-mail mantêm **logs de acesso e de erro**. Os logs de proxy DNS mostram quem visitou sites perigosos e as conexões com comando e controle.

Exemplo de log do servidor Apache: `203.0.113.127 – dsmith [10/Oct/2016:10:26:57 -0500] "GET /logo_sm.gif HTTP/1.0" 200 2254`. Ele mostra o IP do cliente, o usuário, a data, o pedido, o código de resposta (200, sucesso) e o tamanho.

### 29.4 Logs da Rede

As principais fontes de registro da rede são:

- **tcpdump**: captura de pacotes por linha de comando;
- **NetFlow**: registra **informações sobre os fluxos de tráfego, sem o conteúdo**; o **IPFIX** é a versão padronizada;
- **AVC** (*Application Visibility and Control*): reconhece e controla mais de mil aplicativos;
- filtros de conteúdo de e-mail e de web, como o Cisco ESA e o Cisco WSA;
- **proxies web**, que registram todos os pedidos dos usuários;
- **NGFW**, que registra conexões e intrusões.

Um **fluxo** é o conjunto de pacotes em um único sentido com os mesmos IPs, portas e protocolo. Os registros de fluxo ajudam a montar a linha do tempo de um ataque.

Monitorar só pela porta dá pouca informação. O reconhecimento pelo aplicativo mostra **o que o usuário está realmente fazendo**.

### 29.5 SIEM

O **SIEM** (*Security Information and Event Management* — gerenciamento de informações e eventos de segurança) **coleta os logs de toda a rede** e os analisa em tempo real.

| Função | O que faz |
| --- | --- |
| Coleta | Reúne os logs |
| Normalização | Converte formatos diferentes para um modelo comum |
| Correlação | Liga eventos de sistemas diferentes |
| Agregação | Junta eventos repetidos |
| Relatórios | Mostra painéis e resumos |
| Conformidade | Gera os relatórios exigidos por normas |

Exemplos: **Splunk** e **ELK** (Elasticsearch, Logstash e Kibana).

### 29.6 SOAR

O **SOAR** (*Security Orchestration, Automation and Response*) **automatiza as etapas da resposta a incidentes**, unindo ferramentas de vários fabricantes. Exemplos: FortiSOAR e Cortex XSOAR.

SIEM → reúne e correlaciona os eventos; SOAR → responde a eles de forma automatizada.

## 30. Avaliação de Alertas

Nem todo ataque pode ser evitado; muitos só são detectados durante ou depois. Por isso, os alertas precisam ser avaliados por analistas, que decidem o que é real.

### 30.1 Security Onion

O **Security Onion** reúne ferramentas gratuitas para capturar dados, detectar intrusões e analisar alertas. O curso descreve a versão antiga, que usava o Sguil e o CapMe; a versão atual trocou essas ferramentas por novas interfaces.

Dados → Detecção → Análise

| Ferramenta | Tipo | Função |
| --- | --- | --- |
| Snort | IDS de rede | Detecta ataques por regras e assinaturas |
| Suricata | IDS de rede | Usa assinaturas, como o Snort, e pode bloquear o tráfego |
| Zeek | IDS de rede | Analisa o comportamento do tráfego |
| OSSEC | HIDS | Verifica arquivos, logs e processos do host |
| Wazuh | HIDS | Sucessor do OSSEC |

Na análise, o **Sguil** é o **ponto de partida da investigação**; dele, o analista passa para o **Kibana** (painéis) e o **Wireshark** (pacotes).

### 30.2 Alertas no Sguil

Os **alertas** são **mensagens geradas pelas ferramentas de monitoramento** a partir de regras, assinaturas ou anomalias. Todo alerta traz a **5-tupla**, o horário e o equipamento que o gerou.

| Campo do Sguil | Significado |
| --- | --- |
| ST | Status; a cor indica a prioridade |
| CNT | Quantidade de eventos agrupados |
| Sensor | Agente que relatou o evento |
| Event Message | Texto da regra que gerou o alerta |

### 30.3 Regras do Snort

Uma regra do Snort tem **cabeçalho** (ação, protocolo, origem, destino e direção) e **opções** (entre parênteses):

`alert tcp $EXTERNAL_NET any -> $HOME_NET 21 (msg:"ET EXPLOIT VSFTPD backdoor user login smiley"; content:"USER"; sid:2013188; rev:4;)`

| Trecho | Significado |
| --- | --- |
| alert | Ação: gerar um alerta |
| tcp | Protocolo |
| $EXTERNAL\_NET any -> $HOME\_NET 21 | De qualquer endereço externo para a porta 21 da rede interna |
| msg | Texto do alerta |
| content | Conteúdo procurado no pacote |
| sid | Identificação única da regra |
| rev | Número da revisão |

As regras vêm de três fontes principais: GPL (antigas), ET (Emerging Threats) e VRT (Cisco Talos).

### 30.4 Classificação dos Alertas

As regras são **propositalmente conservadoras**: é melhor alertar à toa do que deixar passar um ataque.

"Positivo" e "negativo" dizem se houve alerta; "verdadeiro" e "falso" dizem se ele estava certo:

|  | Verdadeiro | Falso |
| --- | --- | --- |
| Positivo (houve alerta) | Ocorreu um incidente | Não ocorreu incidente |
| Negativo (não houve alerta) | Não ocorreu incidente | Ocorreu um incidente |

- **verdadeiro positivo**: a regra funcionou;
- **falso positivo**: alerta por atividade inofensiva (**gatilho benigno**); custa tempo, mas é inevitável;
- **verdadeiro negativo**: tráfego normal, sem alerta;
- **falso negativo**: **um ataque aconteceu e nenhum alerta foi gerado**; é o caso **mais perigoso**.

O que fazer:

- verdadeiro positivo → **encaminhar para o nível superior**;
- excesso de falsos positivos → ajustar as regras;
- falso negativo descoberto depois → **RSA** (*Retrospective Security Analysis* — análise retrospectiva): **aplicar regras e informações novas aos dados guardados**.

### 30.5 Análise Determinística e Probabilística

- **determinística**: para o ataque dar certo, **todas as etapas anteriores precisam ter dado certo**; descreve o pior caso;
- **probabilística**: usa **estatística para estimar a probabilidade** de cada etapa; serve em tempo real e contra ataques com portas dinâmicas.

| Característica | Determinística | Probabilística |
| --- | --- | --- |
| Base | Etapas conhecidas | Estatística |
| Resultado | Pior caso | Caminhos mais prováveis |

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

## Glossário de Siglas

| Sigla | Nome completo | Significado |
| --- | --- | --- |
| AAA | Authentication, Authorization and Accounting | Autenticação, autorização e contabilidade dos acessos |
| ABAC | Attribute-Based Access Control | Controle de acesso baseado em atributos |
| ACE | Access Control Entry | Cada linha de permitir ou negar de uma ACL |
| ACK | Acknowledgment | Sinalizador TCP de confirmação de recebimento |
| ACL | Access Control List | Lista de controle de acesso que filtra pacotes |
| AES | Advanced Encryption Standard | Algoritmo simétrico recomendado, com bloco de 128 bits |
| AMP | Advanced Malware Protection | Proteção avançada contra malware da Cisco |
| AP | Access Point | Ponto de acesso sem fio |
| API | Application Programming Interface | Conjunto de comandos pelo qual programas se comunicam |
| APIPA | Automatic Private IP Addressing | Endereço 169.254.x.x criado pelo computador sem DHCP |
| ARP | Address Resolution Protocol | Descobre o endereço MAC a partir do IP |
| AUP | Acceptable Use Policy | Política de uso aceitável |
| AVC | Application Visibility and Control | Reconhece e controla aplicativos na rede |
| BYOD | Bring Your Own Device | Uso de aparelhos pessoais no trabalho |
| C&C (CNC) | Command and Control | Servidor que dá ordens a um malware |
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
| ELK | Elasticsearch, Logstash, Kibana | Conjunto de ferramentas para guardar e analisar logs |
| ESA | Email Security Appliance | Filtro de conteúdo de e-mail da Cisco |
| ET | Emerging Threats | Fonte de regras do Snort mantida pela Proofpoint |
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
| IKE | Internet Key Exchange | Troca de chaves nas VPNs IPsec |
| IMAP | Internet Message Access Protocol | Protocolo de recebimento de e-mail |
| IOS | Internetwork Operating System | Sistema operacional dos roteadores e switches Cisco |
| IoT | Internet of Things | Internet das Coisas |
| IP | Internet Protocol | Protocolo de endereçamento e roteamento da internet |
| IPFIX | IP Flow Information Export | Padrão do IETF para registros de fluxo, baseado no NetFlow v9 |
| IPS | Intrusion Prevention System | Sistema de prevenção de intrusão |
| IPsec | IP Security | Conjunto de protocolos que protege o tráfego IP, usado em VPNs |
| IR | Infrared | Infravermelho, comunicação de curto alcance |
| ISBN | International Standard Book Number | Número que identifica um livro |
| ITU-T | International Telecommunication Union – Telecommunication Standardization Sector | Órgão de padrões de telecomunicações, autor do X.509 |
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
| MIC | Message Integrity Check | Verificação de integridade das mensagens no WPA |
| MitM | Man-in-the-Middle | Ataque em que o criminoso se coloca entre as duas partes |
| NAC | Network Access Control | Controle de acesso à rede |
| NAT | Network Address Translation | Tradução de endereços de rede |
| NBA | Network Behavior Analysis | Análise de comportamento de rede |
| NBAD | Network Behavior Anomaly Detection | Detecção de anomalias de comportamento de rede |
| NDP | Neighbor Discovery Protocol | Descoberta de vizinhos no IPv6 |
| NFC | Near-Field Communication | Comunicação por proximidade |
| NGFW | Next-Generation Firewall | Firewall de última geração |
| NSM | Network Security Monitoring | Monitoramento de segurança de rede |
| NTP | Network Time Protocol | Sincroniza os relógios dos dispositivos |
| OCSP | Online Certificate Status Protocol | Consulta on-line do status de um certificado |
| OSI | Open Systems Interconnection | Modelo de referência em sete camadas |
| OSPF | Open Shortest Path First | Protocolo de roteamento |
| OWASP | Open Web Application Security Project | Organização dedicada à segurança de aplicações web |
| P2P | Peer-to-Peer | Rede em que cada computador é cliente e servidor |
| PaaS | Platform as a Service | Plataforma como serviço |
| PAP | Password Authentication Protocol | Autenticação com senha em texto claro |
| PAT | Port Address Translation | NAT com sobrecarga, que usa portas para muitos hosts |
| PEAP | Protected EAP | EAP protegido por túnel TLS |
| PGP | Pretty Good Privacy | Privacidade e autenticação em e-mails |
| PIN | Personal Identification Number | Senha numérica pessoal |
| PKI | Public Key Infrastructure | Infraestrutura de chave pública |
| POP3 | Post Office Protocol 3 | Protocolo de recebimento de e-mail |
| PRI | Priority | Parte da mensagem syslog com facilidade e gravidade |
| QA | Quality Assurance | Garantia de qualidade |
| RA | Registration Authority | Autoridade de registro, que confere a identidade antes de a CA emitir o certificado |
| RADIUS | Remote Authentication Dial-In User Service | Servidor de autenticação AAA, padrão aberto |
| RAID | Redundant Array of Independent Disks | Conjunto de discos com distribuição e redundância |
| RBAC | Role-Based Access Control | Controle de acesso baseado em funções |
| RC4 | Rivest Cipher 4 | Cifra de fluxo antiga e vulnerável |
| RFC | Request for Comments | Documento que define padrões da internet |
| RFID | Radio-Frequency Identification | Identificação por radiofrequência |
| RIP | Routing Information Protocol | Protocolo de roteamento |
| RSA | Rivest, Shamir, Adleman | Algoritmo assimétrico (também: análise de segurança retrospectiva) |
| RST | Reset | Sinalizador TCP que encerra uma conexão |
| RTOS | Real-Time Operating System | Sistema operacional de tempo real |
| SaaS | Software as a Service | Software como serviço |
| SCADA | Supervisory Control and Data Acquisition | Controle de supervisão e aquisição de dados industriais |
| SCP | Secure Copy Protocol | Cópia segura de arquivos sobre SSH |
| SDN | Software-Defined Networking | Rede definida por software |
| SEAL | Software-Optimized Encryption Algorithm | Cifra de fluxo com chave de 160 bits |
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
| SYN | Synchronize | Sinalizador TCP que inicia uma conexão |
| TAC | Time-based Access Control | Controle de acesso baseado em tempo |
| TACACS+ | Terminal Access Controller Access-Control System Plus | Servidor de autenticação AAA da Cisco |
| TCP | Transmission Control Protocol | Protocolo de transporte orientado à conexão |
| TGT | Ticket-Granting Ticket | Tíquete de concessão de tíquete do Kerberos |
| TI | Tecnologia da Informação | Área responsável pelos sistemas e redes |
| TKIP | Temporal Key Integrity Protocol | Protocolo de criptografia do WPA |
| TLS | Transport Layer Security | Protocolo de criptografia das conexões, sucessor do SSL |
| UAV | Unmanned Aerial Vehicle | Veículo aéreo não tripulado (drone) |
| UDP | User Datagram Protocol | Protocolo de transporte sem conexão |
| UPS | Uninterruptible Power Supply | Nobreak |
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
