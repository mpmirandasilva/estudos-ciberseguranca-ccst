# Defesa de Rede

Nov 4, 2026 · Maria Paula

## 1. Fundamentos da Defesa de Redes

A **defesa de rede** é o conjunto de medidas, tecnologias e processos que **protegem os recursos de uma organização contra ataques**.

### 1.1 Tríade CIA: Confidencialidade, Integridade e Disponibilidade

A **tríade CIA** (*Confidentiality, Integrity, Availability*) reúne os **três objetivos principais da segurança da informação**. Em português, também se usa **tríade CID**.

| Objetivo | O que garante | Exemplo de ameaça |
| --- | --- | --- |
| Confidencialidade | Só pessoas autorizadas leem a informação | Funcionário de fora do RH abrindo a folha de pagamento |
| Integridade | A informação não foi alterada | Valor de uma transferência modificado no caminho |
| Disponibilidade | A informação e os serviços funcionam quando necessários | Site fora do ar por um ataque |

### 1.2 Ativos, Vulnerabilidades e Ameaças

O analista identifica três elementos:

- **ativos**: tudo o que tem valor e deve ser protegido, principalmente os **dados**;
- **vulnerabilidades**: uma fraqueza em um sistema ou no seu projeto que pode ser explorada;
- **ameaças**: qualquer perigo potencial para um ativo.

O **agente de ameaça** (ou ator de ameaça) é quem explora a vulnerabilidade: um criminoso, um funcionário mal-intencionado ou um grupo organizado.

A **superfície de ataque** é tudo o que pode ser atingido. Ela cresce junto com a organização.

**Importante:** a vulnerabilidade é o **ponto fraco** (uma senha padrão nunca trocada); a ameaça é o **perigo** que se aproveita dele.

### 1.3 Gerenciamento de Ativos

O **gerenciamento de ativos** consiste em **inventariar todos os ativos e criar políticas e procedimentos para protegê-los**.

É preciso saber onde estão os ativos de informação essenciais e como se chega a eles.

Cada negócio guarda ativos diferentes. Exemplos:

- loja: dados de cartão de crédito;
- empresa de engenharia: projetos e softwares;
- banco: dados de clientes e de contas.

### 1.4 Classificação de Ativos

A **classificação de ativos** distribui os recursos em **grupos com características comuns**. As informações mais importantes recebem o nível mais alto de proteção.

O processo ocorre em quatro etapas:

1. determinar a categoria de cada ativo: informação, software, físico ou serviço;
2. identificar o **proprietário** de cada ativo, para estabelecer a responsabilização;
3. definir os critérios: confidencialidade, valor, tempo, direitos de acesso e destruição;
4. aplicar um esquema uniforme de classificação.

### 1.5 Padronização de Ativos

Os **padrões de ativos** definem **quais produtos de hardware e software a organização usa e dá suporte**.

Com padronização, a reposição é rápida e a gestão custa menos.

### 1.6 Ciclo de Vida dos Ativos

Todo ativo precisa ser protegido em todas as etapas do **ciclo de vida**:

Aquisição → Implantação → Utilização → Manutenção → Descarte

| Etapa | O que acontece |
| --- | --- |
| Aquisição | Compra e entrada no inventário |
| Implantação | Inspeção, testes e etiquetas para rastreamento |
| Utilização | Fase mais longa: atualizações, correções (*patches*), licenças e auditorias |
| Manutenção | Modificações para prolongar a vida útil |
| Descarte | Os dados são apagados e as peças seguem as regras ambientais |

### 1.7 Identificação de Ameaças e de Vulnerabilidades

A **identificação de ameaças** produz uma **lista das ameaças prováveis para um ambiente específico**. Ela responde a:

- quais são as vulnerabilidades do sistema?
- quem pode explorá-las, e para chegar a quais ativos?
- quais são as consequências?

A **identificação de vulnerabilidades** exige conhecer os aplicativos e o hardware da rede e suas fraquezas.

#### 1.7.1 Exemplo Resolvido: Ameaças a um Sistema de Banco On-line

Para um banco pela internet, as ameaças incluem:

- invasão a partir dos servidores expostos à internet;
- roubo de dados de clientes;
- transações falsas, com PIN e cartão roubados;
- ataque interno (*insider*), feito por um funcionário;
- erros de entrada de dados;
- destruição do data center por incêndio ou enchente.

**Observação:** nem toda ameaça é um ataque. Erros e desastres naturais também afetam a integridade e a disponibilidade.

## 2. Políticas, Regulamentos e Padrões

As **políticas** são regras da própria organização; os **regulamentos** são regras externas, como leis. Juntos, **definem o que é permitido e o que é proibido** na rede e nos dados.

### 2.1 Políticas de Negócios

As **políticas de negócios** governam as ações da organização. Na rede, elas formam uma **linha de base de uso aceitável**.

Por isso, um comportamento que viola a política pode indicar uma violação de segurança.

| Política | O que define | Exemplos |
| --- | --- | --- |
| Da empresa | Conduta e responsabilidades de funcionários e empregadores | Assiduidade, vestimenta, privacidade |
| De funcionários | Regras do RH, assinadas na contratação | Salário, horário, benefícios, férias |
| De segurança | Objetivos de segurança, regras de comportamento e requisitos do sistema; documento em constante evolução | Senhas, acesso remoto, uso aceitável |

### 2.2 Política de Segurança

A **política de segurança** informa a todos os requisitos para proteger os ativos de tecnologia e de informação. Serve de base para comprar, configurar e auditar sistemas.

Seus principais benefícios são:

- dar à segurança o apoio da gestão;
- demonstrar o compromisso da organização;
- definir o comportamento esperado;
- garantir consistência nas operações;
- definir as consequências das violações.

Ela reúne políticas menores:

| Política | O que especifica |
| --- | --- |
| Identificação e autenticação | Quem acessa e como a identidade é verificada |
| Senhas | Requisitos mínimos e troca regular |
| Uso aceitável (AUP) | Usos permitidos e consequências da violação |
| Acesso remoto | Como usuários remotos acessam a rede |
| Manutenção de rede | Como atualizar dispositivos de rede e aplicativos |
| Tratamento de incidentes | Como os incidentes são tratados |

### 2.3 Política de Uso Aceitável (AUP)

A **AUP** (*Acceptable Use Policy* — Política de Uso Aceitável) define **o que os usuários podem ou não fazer nos sistemas**. Deve ser o mais explícita possível. Exemplo: listar os sites e aplicativos proibidos na rede da empresa.

Todo funcionário assina a AUP, e a cópia fica guardada durante todo o emprego.

### 2.4 Políticas de BYOD

O **BYOD** (*Bring Your Own Device* — Traga seu Próprio Dispositivo) permite usar **aparelhos pessoais para acessar sistemas, redes e informações da empresa**.

Traz produtividade e mobilidade, mas aumenta o risco de **vazamento de dados**. A política de BYOD define:

- os objetivos do programa;
- quem pode trazer dispositivos e quais são aceitos;
- o nível de acesso dos dispositivos pessoais;
- o que a segurança pode fazer no aparelho;
- as medidas se um dispositivo for comprometido.

| Prática recomendada | O que fazer |
| --- | --- |
| Senha | Uma senha diferente para cada dispositivo e conta |
| Conectividade sem fio | Desligar Wi-Fi e Bluetooth sem uso; só redes confiáveis |
| Atualizações | Sistema e aplicativos sempre atualizados |
| Backup | Ativar o backup para perda ou roubo |
| Localizar o dispositivo | Localização com apagamento remoto |
| Antivírus | Instalar nos dispositivos aprovados |

O **MDM** (*Mobile Device Management* — Gerenciamento de Dispositivos Móveis) **aplica configurações de segurança em todos os dispositivos que se conectam à rede da empresa**.

### 2.5 Conformidade com Regulamentos e Padrões

Os **regulamentos de conformidade** definem **pelo que a organização é responsável e quais são as consequências se ela não cumprir**. Variam conforme o tipo de organização e de dado.

Exemplo: no Brasil, quem trata dados pessoais segue a **LGPD** (Lei Geral de Proteção de Dados).

## 3. Defesa em Profundidade

A **defesa em profundidade** **usa várias camadas de segurança na borda da rede, dentro da rede e nos dispositivos finais**. Assim, a falha de uma proteção não compromete as outras.

### 3.1 Camadas de uma Rede Protegida

Na topologia mais simples, o tráfego da internet atravessa três linhas de defesa até a **LAN** (*Local Area Network* — rede local):

Internet → Roteador de borda → Firewall → Roteador interno → Rede interna

![O tráfego da internet atravessa três linhas de defesa até chegar à rede interna](img/defesa/def_camadas.png){width=6in}

| Linha de defesa | Função |
| --- | --- |
| Roteador de borda | Primeira linha: liga a empresa à internet e segue regras que permitem ou negam o tráfego |
| Firewall | Segunda linha: filtragem adicional e acompanhamento do estado das conexões |
| Roteador interno | Regras finais de filtragem antes do destino |

O **firewall** decide qual tráfego passa entre redes:

- **nega conexões iniciadas na rede externa** (não confiável) **em direção à interna** (confiável);
- deixa os usuários internos abrirem conexões para fora;
- pode **autenticar usuários** antes de liberar o acesso (**proxy de autenticação**).

Outras camadas comuns:

- **IPS** (*Intrusion Prevention System* — sistema de prevenção de intrusão): identifica e bloqueia ataques no tráfego;
- **AMP** (*Advanced Malware Protection*): proteção da Cisco contra malware (programas maliciosos);
- filtros de conteúdo web e de e-mail;
- controle de acesso à rede, que verifica usuários e aparelhos antes de deixá-los entrar.

### 3.2 A Cebola e a Alcachofra da Segurança

Duas analogias descrevem a defesa em profundidade:

- **cebola**: o atacante precisa **descascar as defesas camada por camada** até os dados, no centro;
- **alcachofra**: nas **redes sem fronteiras** (celulares, casa, nuvem), o atacante **não precisa remover todas as camadas, basta arrancar algumas folhas**, como senhas, bancos de dados e aplicativos web.

| Característica | Cebola | Alcachofra |
| --- | --- | --- |
| Cenário | Perímetro bem definido | Rede sem fronteiras |
| Caminho do atacante | Todas as camadas | Só algumas folhas |

### 3.3 Estratégias de Defesa em Profundidade

A defesa em profundidade não é impenetrável, mas **minimiza os riscos**. Ela usa cinco estratégias:

| Estratégia | Ideia central | Exemplo |
| --- | --- | --- |
| Sobreposição | Várias defesas seguidas | Servidor com senha, em prédio trancado |
| Limitação | Só o acesso necessário ao trabalho | Documentos sigilosos em sala com câmeras |
| Diversidade | Camadas diferentes entre si | Firewall de um fabricante e antivírus de outro |
| Ofuscação | Não revelar detalhes úteis ao atacante | Mensagem de erro sem a versão do sistema |
| Simplicidade | Simples por dentro, complexo por fora | Configuração que a equipe entende e mantém |

**Observação:** na diversidade, a técnica que vence uma camada não vence as outras.

## 4. Criptografia e Confidencialidade

A **criptografia** é a ciência de criar e quebrar códigos. Ela **embaralha os dados para que só quem tem a chave consiga lê-los** e é a principal ferramenta da confidencialidade.

### 4.1 Conceitos Básicos de Criptografia

O **texto claro** é o dado legível. O **texto cifrado** é o dado criptografado, ilegível.

Texto claro → Criptografia → Texto cifrado → Descriptografia → Texto claro

![A chave transforma o texto claro em texto cifrado e, do outro lado, o texto cifrado de volta em texto claro](img/defesa/def_cripto.png){width=6in}

A **chave** é o valor secreto usado nas duas operações. **Quem tem a chave descriptografa o texto cifrado.**

Quanto maior a chave, mais difícil descobri-la por tentativa.

De acordo com o uso das chaves, a criptografia pode ser:

- **simétrica**: a mesma chave criptografa e descriptografa;
- **assimétrica**: um par de chaves, uma para cada operação.

### 4.2 Estados dos Dados

Os dados precisam de proteção em **três estados**:

| Estado | Situação | Exemplo |
| --- | --- | --- |
| Em repouso | Armazenados, sem acesso no momento | Disco do servidor |
| Em trânsito | Sendo transmitidos, dentro do computador ou pela rede | Mensagem pela internet |
| Em processamento | Na entrada, na modificação, no cálculo ou na saída | Planilha sendo editada |

**Observação:** todo dado que não está em trânsito nem em processamento está em repouso.

### 4.3 Criptografia Simétrica

Na **criptografia simétrica**, **as duas partes usam a mesma chave**, chamada **chave pré-compartilhada** ou **chave secreta**. Ela precisa ser combinada **antes** da comunicação.

Entre suas principais características estão:

- **pouco processamento** e, por isso, **alta velocidade**;
- uso em **grandes volumes de dados**, como o tráfego de uma **VPN** (*Virtual Private Network* — rede privada virtual, um túnel protegido pela internet);
- chaves de **40 a 256 bits**, com **mínimo de 128 bits** para ser segura.

Os algoritmos simétricos podem ser:

- **cifra de bloco**: cifra os dados em blocos de tamanho fixo, de 64 ou 128 bits; exemplos: DES e AES;
- **cifra de fluxo**: cifra um byte ou um bit de cada vez, e costuma ser mais rápida; exemplos: RC4 e A5 (telefonia GSM, o 2G).

| Algoritmo | Características | Situação |
| --- | --- | --- |
| DES (*Data Encryption Standard*) | Anos 1970; chave de 56 bits | Inseguro |
| 3DES (*Triple DES*) | Aplica o DES três vezes | Evitar |
| AES (*Advanced Encryption Standard*) | Bloco de 128 bits; chaves de 128, 192 ou 256 bits; usado no Wi-Fi, em VPNs e em discos | **Recomendado** |
| SEAL (*Software-Optimized Encryption Algorithm*) | Cifra de fluxo; chave de 160 bits; pouco uso de CPU | Alternativa ao AES |
| Série RC (*Rivest ciphers*) | RC4 é cifra de fluxo, usada no Wi-Fi antigo | RC4 vulnerável |

**Observação:** no AES, só o tamanho da **chave** varia; o **bloco** é sempre de 128 bits.

### 4.4 Criptografia Assimétrica

Na **criptografia assimétrica**, ou **de chave pública**, cada um tem **um par de chaves**:

- **pública**: pode ser divulgada;
- **privada**: só o dono conhece.

**O que uma chave do par criptografa, só a outra descriptografa.** A privada não pode ser calculada a partir da pública.

Entre suas principais características estão:

- chaves **longas**, de 512 a 4.096 bits; hoje, **2.048 bits ou mais**;
- **lentidão**, por isso é usada em tarefas de pouco volume: **troca de chaves e assinaturas digitais**;
- gerenciamento de chaves mais simples, porque uma delas é pública.

Os principais protocolos que a usam são:

- **SSL** (*Secure Sockets Layer*) e **TLS** (*Transport Layer Security*): protegem a comunicação entre navegador e site (o **cadeado** e o **https**); o SSL é antigo e inseguro, e o que se usa é o TLS;
- **SSH** (*Secure Shell*): **acesso remoto criptografado** a servidores e equipamentos de rede; substitui o Telnet;
- **IKE** (*Internet Key Exchange*): **negocia as chaves** nas VPNs **IPsec** (*IP Security*);
- **PGP** (*Pretty Good Privacy*): criptografa e assina **e-mails e arquivos**.

| Algoritmo | Chave (bits) | Características |
| --- | --- | --- |
| Diffie-Hellman (DH) | 512 a 4.096 | Não cifra mensagens: **combina uma chave secreta** sem enviá-la |
| DSS / DSA (*Digital Signature Standard / Algorithm*) | 512 a 1.024 | Padrão dos EUA para **assinaturas digitais**; verifica de 10 a 40 vezes mais devagar que o RSA |
| RSA (Rivest, Shamir e Adleman) | 512 a 2.048 | Serve para **assinatura e criptografia**; usado nos certificados dos sites |
| ElGamal | 512 a 1.024 | Derivado do DH; a mensagem cifrada dobra de tamanho |
| ECC (*Elliptic Curve Cryptography*) | 224 ou mais | **Chaves menores com a mesma segurança**; poupa bateria em celulares |

### 4.5 Confidencialidade e Autenticação com Chaves Assimétricas

O resultado depende da chave usada para criptografar:

- chave **pública** do destinatário → só ele lê → **confidencialidade**;
- chave **privada** do remetente → só ele poderia ter enviado → **autenticação**.

![A chave usada para criptografar define o resultado: a pública do destinatário dá confidencialidade; a privada do remetente, autenticação](img/defesa/def_assim.png){width=6in}

#### 4.5.1 Exemplo Resolvido: Alice Envia uma Mensagem Sigilosa a Bob

1. Alice recebe a chave pública de Bob;
2. Alice criptografa a mensagem com ela e a envia;
3. Bob descriptografa com a própria chave privada.

#### 4.5.2 Exemplo Resolvido: Bob Confere que a Mensagem Veio de Alice

1. Alice criptografa a mensagem com a própria chave privada e a envia;
2. Bob descriptografa com a chave pública de Alice;
3. se der certo, a mensagem só pode ter vindo de Alice.

#### 4.5.3 Exemplo Resolvido: Confidencialidade, Integridade e Autenticação Juntas

O **hash** é um resumo de tamanho fixo dos dados, que muda se qualquer parte deles mudar.

1. Alice criptografa a mensagem com a chave **pública de Bob** (confidencialidade);
2. Alice criptografa o **hash** da mensagem com a própria chave **privada** (autenticação e integridade) e envia os dois;
3. Bob descriptografa o hash com a chave pública de Alice e o compara com o hash que ele calcula;
4. Bob descriptografa a mensagem com a própria chave privada.

**Observação:** se uma chave privada for comprometida, é preciso gerar um novo par.

### 4.6 Diffie-Hellman

O **Diffie-Hellman (DH)** permite que **dois computadores gerem o mesmo segredo sem nunca tê-lo transmitido**. Cada lado calcula a chave sozinho, e ela depois é usada por um algoritmo simétrico, como o AES.

Exemplos de uso: **VPNs IPsec** e **SSH**.

#### 4.6.1 Exemplo Resolvido: a Analogia das Cores

1. Alice e Bob combinam uma cor pública: amarelo;
2. cada um escolhe uma cor secreta: Alice, vermelho; Bob, azul;
3. cada um mistura o amarelo com a sua cor e envia: Alice envia laranja; Bob, verde;
4. cada um mistura a cor recebida com a própria cor secreta;
5. os dois chegam ao mesmo marrom, a chave compartilhada.

Quem intercepta só vê amarelo, laranja e verde.

A força do DH é definida pelo **grupo DH**: **quanto maior, mais seguro e mais lento**.

### 4.7 Resumo de Criptografia Simétrica e Assimétrica

| Característica | Simétrica | Assimétrica |
| --- | --- | --- |
| Chaves | A mesma nas duas operações | Par: pública e privada |
| Tamanho da chave | 40 a 256 bits | 512 a 4.096 bits |
| Velocidade | Rápida | Lenta |
| Uso típico | Grandes volumes, como VPN | Troca de chaves e assinaturas |
| Exemplos | AES, SEAL, 3DES | RSA, DH, DSA, ElGamal, ECC |

**Importante:** as duas trabalham juntas: o **DH cria as chaves, e um algoritmo simétrico, como o AES, criptografa o grande volume de dados**.

## 5. Hash, Integridade e Autenticidade

A criptografia impede a leitura, mas não garante que os dados chegaram sem alteração nem quem os enviou. Para isso existem o **hash** e o **HMAC**.

### 5.1 Elementos das Comunicações Seguras

A tendência é que **toda comunicação seja criptografada**. As comunicações seguras se apoiam em **quatro elementos**:

| Elemento | O que garante | Como é obtido |
| --- | --- | --- |
| Integridade dos dados | A mensagem não foi alterada | Hash (SHA-2, SHA-3) |
| Autenticação de origem | A mensagem vem de quem diz ter enviado | HMAC |
| Confidencialidade | Só autorizados leem | Criptografia simétrica e assimétrica |
| Não repúdio | O remetente não pode negar o envio | Assinatura digital |

### 5.2 Funções Hash

Uma **função hash** recebe dados de qualquer tamanho e produz uma **representação de tamanho fixo**, chamada **hash** (ou *digest*).

Entre suas principais características estão:

- **unidirecional**: não pode ser revertida;
- saída sempre do mesmo tamanho;
- cálculo rápido;
- duas entradas diferentes praticamente nunca geram o mesmo hash.

Por isso, **qualquer alteração nos dados, por menor que seja, muda o hash**. O hash funciona como uma **impressão digital** dos dados.

### 5.3 Algoritmos de Hash

| Algoritmo | Tamanho do hash | Situação |
| --- | --- | --- |
| MD5 (*Message Digest 5*) | 128 bits | Legado e inseguro |
| SHA-1 | 160 bits | Com falhas conhecidas |
| SHA-2 | SHA-224, SHA-256, SHA-384 e SHA-512 | Preferir SHA-256 ou superior |
| SHA-3 | SHA3-224 a SHA3-512 | O mais novo; usar sempre que possível |

A sigla **SHA** significa *Secure Hash Algorithm*, padronizado pelo **NIST** (*National Institute of Standards and Technology*, instituto de padrões dos EUA).

### 5.4 Verificação de Integridade com Hash

De forma simplificada, o processo ocorre da seguinte maneira:

1. o remetente calcula o hash e o envia junto com a mensagem;
2. o destinatário calcula de novo o hash da mensagem recebida;
3. hashes iguais → mensagem intacta; hashes diferentes → mensagem alterada.

Usos comuns:

- **downloads**: comparar o hash publicado pelo fabricante com o do arquivo baixado;
- **perícia forense**: o perito faz uma **cópia bit a bit** da mídia e compara os hashes; hashes iguais provam que os dados não foram alterados.

### 5.5 Limitação do Hash

O hash **não protege contra alterações deliberadas**: ele não identifica o remetente, e qualquer pessoa consegue calculá-lo.

Um atacante no meio do caminho altera a mensagem, calcula um novo hash e o anexa. Esse é o **ataque *man-in-the-middle* (MitM)**, em que o criminoso se coloca entre as duas partes.

### 5.6 HMAC

O **HMAC** (*Hash-based Message Authentication Code*) é um hash calculado **a partir da mensagem e de uma chave secreta** que só o remetente e o destinatário conhecem.

Sem a chave, o atacante não gera um HMAC válido. Por isso, o HMAC garante **integridade e autenticação da origem**.

1. o remetente calcula o HMAC com a chave e o envia junto;
2. o destinatário calcula o HMAC com a mesma chave;
3. valores iguais → mensagem íntegra e de origem confiável.

Exemplos de uso: **SSL/TLS**, **IPsec**, **SSH** e autenticação entre roteadores.

**Observação:** ao escolher um algoritmo de hash, usar **SHA-256 ou superior** e evitar SHA-1 e MD5.

#### 5.6.1 Exemplo Resolvido: HMAC entre Roteadores OSPF

O roteador R1 envia ao vizinho R2 uma atualização de rotas pelo **OSPF** (*Open Shortest Path First*, protocolo com que os roteadores trocam rotas):

1. R1 calcula o hash da atualização com a chave secreta;
2. R1 envia o hash junto;
3. R2 calcula o hash com a mesma chave; se bater, aceita; se não, descarta.

| Característica | Hash | HMAC |
| --- | --- | --- |
| Entrada | Só a mensagem | Mensagem + chave secreta |
| Quem calcula | Qualquer pessoa | Só quem tem a chave |
| Resiste ao MitM | Não | Sim |

### 5.7 Hash de Senhas

Os sistemas **guardam apenas o hash da senha**. No login, comparam o hash da senha digitada com o guardado.

Quem rouba os hashes tenta adivinhar as senhas por dois ataques:

- **dicionário**: compara os hashes roubados com os de uma lista de senhas comuns;
- **força bruta**: testa todas as combinações; por isso a senha precisa ser longa.

O **alongamento de chave** (*key stretching*) deixa cada tentativa muito lenta.

#### 5.7.1 Salt

O **salt** é uma **sequência aleatória acrescentada à senha antes do cálculo do hash**. Assim, senhas iguais geram hashes diferentes.

O salt é guardado junto com o hash e não precisa ser secreto. As boas práticas são:

- um salt exclusivo para cada senha;
- gerado por um **CSPRNG** (*Cryptographically Secure Pseudo-Random Number Generator* — gerador de números aleatórios seguro);
- hash calculado sempre no servidor.

Para guardar: gerar o salt → juntar à senha → calcular o hash → salvar salt e hash.

Para validar: buscar o salt → juntar à senha digitada → calcular o hash → comparar com o guardado.

O salt inutiliza as tabelas que os atacantes preparam com antecedência:

| Tabela | Como funciona |
| --- | --- |
| De pesquisa | Hashes pré-calculados de um dicionário |
| De pesquisa reversa | Liga cada hash roubado a todos os usuários que o usam |
| Rainbow | Ocupa menos espaço e cobre mais hashes |

## 6. Assinaturas Digitais e Infraestrutura de Chave Pública (PKI)

A **assinatura digital** combina o hash e a criptografia assimétrica para provar quem enviou uma mensagem. A **PKI** garante que as chaves públicas usadas nessa prova são confiáveis.

### 6.1 Assinatura Digital

A **assinatura digital** garante **autenticidade, integridade e não repúdio**. O **não repúdio** significa que quem assinou não pode negar que assinou.

Entre suas principais características estão:

- **autêntica**: não pode ser falsificada;
- **inalterável**: o documento assinado não pode ser modificado;
- **não reutilizável**: não passa para outro documento;
- **não repudiável**: vale como prova legal.

Os dois usos mais comuns são a **assinatura de código** e os **certificados digitais**.

O padrão **DSS** (*Digital Signature Standard*) admite três algoritmos:

- **DSA**: o original, com chaves de 512 a 1.024 bits;
- **RSA**: muito usado para assinar e verificar;
- **ECDSA** (*Elliptic Curve DSA*): com curvas elípticas, mais eficiente e com assinaturas menores.

### 6.2 Como a Assinatura É Criada e Verificada

A assinatura usa a chave **privada** do remetente para assinar e a chave **pública** dele para conferir.

#### 6.2.1 Exemplo Resolvido: Bob Confirma um Pedido de Alice

Para assinar:

1. Bob calcula o hash da confirmação;
2. criptografa o hash com a própria chave privada: essa é a assinatura;
3. envia o documento com a assinatura.

Para verificar:

1. Alice descriptografa a assinatura com a chave pública de Bob e recupera o hash;
2. calcula o hash do documento recebido;
3. hashes iguais → foi Bob quem enviou, e o documento não mudou.

![Bob assina com a própria chave privada; Alice confere com a chave pública de Bob e compara os hashes](img/defesa/def_assinatura.png){width=6in}

**Importante:** o que se criptografa é o **hash** do documento. Por isso, a assinatura não dá confidencialidade: o documento continua legível.

### 6.3 Assinatura de Código

A **assinatura de código** aplica a assinatura digital a programas. Ela garante que:

- o código veio realmente da editora;
- não foi modificado desde a publicação;
- a editora não pode negar que o publicou;
- nenhum código malicioso foi inserido por terceiros.

Exemplo: no Windows, Propriedades → Assinaturas Digitais mostra quem assinou o programa, o algoritmo de hash e a data.

### 6.4 Certificados Digitais

Um **certificado digital** funciona como um **passaporte eletrônico**: **associa uma chave pública a uma identidade confirmada** (site, pessoa ou organização). Informa para quem foi emitido, quem o emitiu e até quando vale.

**Importante:** o **certificado verifica a identidade**; a **assinatura verifica que algo veio dessa identidade**.

### 6.5 Infraestrutura de Chave Pública (PKI)

Para confiar em uma chave pública, um **terceiro confiável** precisa confirmar a quem ela pertence, como o órgão que emite a carteira de motorista.

A **PKI** (*Public Key Infrastructure* — Infraestrutura de Chave Pública) é o conjunto de hardware, software, pessoas, políticas e procedimentos que **criam, gerenciam, distribuem, armazenam e revogam certificados digitais**.

A **autoridade de certificação** (**CA**, *Certificate Authority*) **emite os certificados, vinculando uma chave pública a uma identidade confirmada**, e os assina com a própria chave privada. Exemplos: DigiCert, GlobalSign e Let's Encrypt (gratuita).

A empresa também pode montar uma **PKI privada** e ser a própria CA, por exemplo com o Windows Server.

| Elemento | Função |
| --- | --- |
| Certificado | Chave pública, finalidade, CA emissora, validade |
| Armazenamento de certificados | Guarda certificados e chaves privadas no computador |
| CA | Verifica a identidade e emite os certificados |
| Banco de dados de certificados | Guarda os certificados aprovados |

De forma simplificada:

1. Bob pede um certificado à CA, que confirma sua identidade e o emite;
2. Bob apresenta o certificado a Alice;
3. Alice confere com a chave pública da CA que o certificado é válido.

![A CA confirma a identidade de Bob e emite o certificado; Alice confia nele porque confere a assinatura da CA](img/defesa/def_pki.png){width=6in}

A **autoridade de registro** (**RA**, *Registration Authority*) confere a identidade de quem pede o certificado; quem emite é sempre a CA.

### 6.6 Classes de Certificados

A classe depende do rigor da verificação de identidade: **quanto maior a classe, mais confiável o certificado**.

| Classe | Uso |
| --- | --- |
| 0 | Testes, sem verificação |
| 1 | Pessoas, só verificação de e-mail |
| 2 | Organizações que precisam provar a identidade |
| 3 | Servidores e software, com verificação independente |
| 4 | Transações on-line entre empresas |
| 5 | Organizações privadas e governo |

Os navegadores já trazem a lista de **CAs raiz confiáveis**, as do topo, em quem todos confiam.

### 6.7 Topologias de PKI

| Topologia | Como funciona | Vantagem | Desvantagem |
| --- | --- | --- | --- |
| Raiz única | Uma CA emite tudo | Simplicidade | Ponto único de falha |
| Certificação cruzada | CAs do mesmo nível confiam umas nas outras | Sem ponto único de falha | Muitas relações |
| Hierárquica | A CA raiz certifica CAs subordinadas | Escala bem | Cadeia difícil de rastrear |
| Híbrida | Hierarquias que se certificam entre si | Une comunidades | Mais complexa |

O **ponto único de falha** é qualquer componente cuja falha derruba o sistema inteiro.

### 6.8 Padrão X.509

O **X.509 versão 3** define **o formato dos certificados digitais**. É usado em:

- **SSL/TLS**: autenticação de sites no HTTPS;
- **IPsec**: VPNs autenticadas com certificados;
- **S/MIME** (*Secure/Multipurpose Internet Mail Extensions*): assina e criptografa e-mails;
- **EAP-TLS**: autenticação **802.1X**, em que o dispositivo prova a identidade com certificado antes de usar a porta da rede.

### 6.9 Inscrição e Revogação de Certificados

O certificado da CA raiz é **autoassinado**: **só uma CA raiz** emite certificado autoassinado reconhecido. Nos navegadores, eles já vêm instalados.

Na **inscrição**, o host pede seu certificado à CA. A autenticidade do certificado da CA é conferida **fora de banda** (por outro canal, como telefone), pela **impressão digital** (o hash do certificado).

Um certificado é **revogado** quando a chave é comprometida ou ele não é mais necessário:

| Método | Como funciona |
| --- | --- |
| CRL (*Certificate Revocation List*) | Lista dos certificados revogados, consultada periodicamente |
| OCSP (*Online Certificate Status Protocol*) | Consulta on-line, em tempo real, sobre um certificado |

### 6.10 Aplicações da PKI

A PKI está em:

- certificados SSL/TLS e HTTPS;
- VPNs IPsec;
- controle de acesso com 802.1X;
- e-mail seguro (S/MIME);
- assinatura de código;
- **EFS** (*Encrypting File System*), que criptografa arquivos;
- autenticação de dois fatores com cartões inteligentes (*smart cards*).

O navegador mostra aviso de segurança em dois casos:

- **certificado vencido**;
- **assinatura não validada**, quando a CA raiz não está no navegador.

O **conjunto de cifras** (*cipher suite*) do TLS reúne os algoritmos de MAC (HMAC), criptografia (AES), troca de chaves (DH) e autenticação (RSA). Cada um pode ser trocado sem mudar o protocolo.

**Importante:** o criminoso também usa criptografia. Os comandos que ele envia às máquinas infectadas (**comando e controle**) vão cifrados, o que esconde o ataque do monitoramento.

## 7. Protocolos Seguros

Os **protocolos seguros** são as versões protegidas dos protocolos do dia a dia. Neles, a criptografia assimétrica e os certificados provam a identidade e combinam uma chave; a simétrica e o HMAC protegem o resto da conversa.

### 7.1 Telnet, SSH e SCP

O **Telnet** e o **SSH** (*Secure Shell*) dão acesso remoto, por linha de comando, a equipamentos como roteadores:

| Característica | Telnet | SSH |
| --- | --- | --- |
| Criptografia | Nenhuma | Tudo criptografado |
| Porta | TCP 23 | TCP 22 |
| O que um sniffer (como o Wireshark) vê | Usuário e senha em texto claro | Só os endereços IP |
| Recomendação | Evitar | Usar sempre |

O **SCP** (*Secure Copy*) **transfere arquivos usando o SSH**.

### 7.2 SNMP, SSL/TLS, FTPS e E-mail Seguro

Os principais protocolos têm versões seguras:

- **SNMPv3**: o **SNMP** (*Simple Network Management Protocol*) coleta estatísticas dos dispositivos para monitorar a rede; a versão 3 usa criptografia;
- **TLS** (*Transport Layer Security*): **substituto atualizado e mais seguro do SSL**; combina algoritmos e chaves em um *handshake* (a apresentação inicial) e protege o **HTTPS**;
- **FTPS**: o **FTP** (*File Transfer Protocol*) envia usuário e senha em texto claro; o FTPS acrescenta TLS;
- **e-mail**: **POP** (porta 110) baixa as mensagens, **IMAP** (porta 143) as mantém no servidor; ambos devem usar SSL/TLS. O **S/MIME** envia e-mails **assinados e criptografados**.

### 7.3 HTTP e HTTPS

O **HTTP** (*HyperText Transfer Protocol*) trafega **em texto claro**: qualquer pessoa no caminho lê e altera. O **HTTPS** acrescenta **a criptografia SSL/TLS** e faz aparecer o cadeado no navegador.

De forma simplificada, a conexão ocorre da seguinte maneira:

1. o navegador pede a página com https://;
2. o servidor envia sua chave pública no certificado;
3. o navegador confere se o certificado não venceu, não foi revogado e foi emitido por uma CA confiável;
4. o navegador cria uma chave simétrica e a envia cifrada com a chave pública do servidor;
5. a página passa a ser cifrada com a chave simétrica.

![No HTTPS, a criptografia assimétrica protege a troca da chave simétrica, que depois cifra a página](img/defesa/def_https.png){width=6in}

**Importante:** o HTTPS **protege os dados apenas no caminho**, não o servidor: um site com cadeado pode ser malicioso.

### 7.4 Resumo de Protocolos Inseguros e Seguros

| Função | Protocolo inseguro | Alternativa segura |
| --- | --- | --- |
| Acesso remoto | Telnet (TCP 23) | SSH (TCP 22) |
| Cópia de arquivos | FTP | FTPS ou SCP |
| Navegação web | HTTP (porta 80) | HTTPS (porta 443) |
| Gerenciamento | SNMPv1 e SNMPv2 | SNMPv3 |
| E-mail | POP (110) e IMAP (143) sem criptografia | POP e IMAP com SSL/TLS; S/MIME |
| Resolução de nomes | DNS sem autenticação | DNSSEC |
| Tempo | NTP sem autenticação | NTP com autenticação |

## 8. Ocultação de Dados

Além de criptografar, é possível proteger dados **escondendo ou disfarçando a informação**.

### 8.1 Mascaramento de Dados

O **mascaramento de dados** **substitui a informação confidencial por uma versão não confidencial que parece e funciona como a original**.

Uso mais comum: dados substitutos para **testes e análises**, sem expor os dados reais.

| Técnica | Como funciona | Exemplo |
| --- | --- | --- |
| Substituição | Troca por valores fictícios | Nomes reais por nomes inventados |
| Embaralhamento | Mistura os valores da coluna entre os registros | Dados financeiros em banco de testes |
| Anulação | Aplica valor nulo ao campo | CPF apagado |

### 8.2 Esteganografia

A **esteganografia** **esconde uma mensagem dentro de outro arquivo**, como uma imagem ou um áudio. Vantagem: a mensagem secreta não chama atenção.

A técnica mais usada em imagens é a dos **bits menos significativos** (**LSB**, *Least Significant Bits*): troca o último bit de cada cor dos pixels, mudança que o olho humano não percebe.

Na **esteganografia social**, a mensagem tem um sentido para o público e outro para quem conhece o código. Exemplo: combinar que "ir ao cinema" significa "ir à praia".

### 8.3 Esteganoanálise

A **esteganoanálise** é **a descoberta de que existe informação escondida**. O analista procura padrões em imagens, em áreas do disco que deveriam estar vazias e em cabeçalhos de pacotes.

| Característica | Criptografia | Esteganografia | Mascaramento |
| --- | --- | --- | --- |
| Objetivo | Tornar a mensagem ilegível | Esconder que ela existe | Trocar dados reais por falsos realistas |
| Chama atenção? | Sim | Não | Não |
| Uso típico | Dados em trânsito e em repouso | Comunicação secreta | Testes e análises |

## 9. Controle de Acesso e Autenticação

O **controle de acesso** **define quem pode acessar cada recurso, o que pode fazer com ele e quando**.

### 9.1 Tipos de Controle de Acesso

Os controles de acesso são de **três tipos**:

| Tipo | O que são | Exemplos |
| --- | --- | --- |
| Físicos | Barreiras reais que impedem o contato com os sistemas | Guardas, cercas, portas trancadas, câmeras, alarmes |
| Lógicos (técnicos) | Hardware e software para identificar, autenticar, autorizar e auditar | Criptografia, senhas, biometria, ACLs, firewalls |
| Administrativos | Políticas e procedimentos da empresa | Contratação, verificação de antecedentes, treinamento |

Alguns termos:

- **mantrap** (eclusa): entrada com duas portas que pode prender um visitante indesejado entre elas;
- **níveis de corte** (*clipping levels*): limite de erros antes de disparar um alerta;
- **ACL** (*Access Control List* — lista de controle de acesso): lista de regras que define o que é permitido e o que é bloqueado.

### 9.2 AAA: Autenticação, Autorização e Contabilidade

O **AAA** (*Authentication, Authorization and Accounting*) reúne os **três serviços que formam a estrutura do controle de acesso**:

| Serviço | Pergunta que responde | Exemplo |
| --- | --- | --- |
| Autenticação | Quem é você? | Usuário e senha |
| Autorização | O que você pode fazer? | Acesso ao banco de vendas só no horário comercial |
| Contabilidade | O que você fez? | Acesso a um servidor por 15 minutos |

**Importante:** a contabilidade (*accounting*) não tem relação com finanças: é o **registro do que o usuário fez**.

### 9.3 Identificação

Na **identificação**, o usuário diz quem é, normalmente pelo **nome de usuário**. O **identificador único** liga cada ação a uma pessoa.

**Importante:** informar o usuário é **identificação**; provar que é ele, com a senha, é **autenticação**.

### 9.4 Métodos de Autenticação

A autenticação usa pelo menos um de **três tipos de fator**:

| Fator | Exemplos |
| --- | --- |
| Algo que você sabe | Senha, frase secreta, PIN |
| Algo que você tem | Cartão inteligente, *token*, aplicativo autenticador |
| Algo que você é | Digital, retina, voz |

#### 9.4.1 Algo que Você Sabe

A **senha** é o **método de autenticação mais usado**. As boas práticas são:

- não usar dados pessoais;
- pelo menos oito caracteres;
- combinar maiúsculas, minúsculas, números e símbolos;
- uma senha diferente para cada sistema;
- usar um **gerenciador de senhas**.

#### 9.4.2 Algo que Você Tem

O **cartão inteligente** tem um **chip que guarda e protege dados** com criptografia.

O **chaveiro de segurança** (*security key fob* ou *token*) **mostra um número temporário**, trocado a cada minuto. Aplicativos autenticadores fazem o mesmo.

#### 9.4.3 Algo que Você É

A **biometria** usa **características físicas ou comportamentais únicas**, comparadas com um perfil guardado. Pode ser:

- **fisiológica**: digital, rosto, retina, mãos;
- **comportamental**: voz, modo de andar, ritmo de digitação.

### 9.5 Autenticação Multifator (MFA)

A **MFA** (*Multi-Factor Authentication* — autenticação multifator) **usa pelo menos dois fatores de tipos diferentes**. Saber a senha não basta para entrar. Exemplos:

- senha e código enviado ao celular;
- cartão (tem) e PIN (sabe) no caixa eletrônico.

Com exatamente dois fatores, chama-se **2FA** (*Two-Factor Authentication*).

**Importante:** duas senhas não formam MFA, porque são do mesmo tipo de fator.

### 9.6 Autorização

A **autorização** **controla o que o usuário pode fazer depois de autenticado**: ler, copiar, editar, criar, excluir, e em que horário. É **automática**, logo após a autenticação.

A **política de autorização** pode ser:

- **baseada em grupo**: só a equipe de TI entra na sala de servidores;
- **por nível de autoridade**: as permissões dependem do cargo.

### 9.7 Auditabilidade

A **auditabilidade** (*accountability*) **rastreia cada ação até a pessoa ou o processo que a realizou**. Registra, por exemplo:

- logins com sucesso ou falha;
- recursos acessados.

**Observação:** falhas de login podem indicar tentativa de invasão.

### 9.8 Gerenciamento de Identidade Federada

O **gerenciamento de identidade federada** permite que **várias organizações aceitem as mesmas credenciais**. Para o usuário, é um **login único** (*single sign-on*). Exemplo: "Entrar com Google".

O risco é o **efeito cascata**: credenciais roubadas abrem todos os sistemas da federação. Proteção comum: vincular o login a um dispositivo autorizado.

## 10. Modelos de Controle de Acesso e Confiança Zero

Um **modelo de controle de acesso** define **quem decide sobre o acesso e com base em quê**.

### 10.1 Modelos de Controle de Acesso

| Modelo | Quem decide / com base em quê | Característica marcante |
| --- | --- | --- |
| DAC (*Discretionary Access Control* — discricionário) | O **dono** dos dados | Menos restritivo |
| MAC (*Mandatory Access Control* — obrigatório) | Rótulos de segurança e autorização do usuário | Mais rígido; uso militar |
| RBAC (*Role-Based Access Control* — baseado em funções) | A **função** ou cargo | Recomendado para grandes organizações |
| ABAC (*Attribute-Based Access Control* — baseado em atributos) | Atributos do usuário, do recurso e do ambiente | Mais flexível |
| Baseado em regras | Regras da equipe de segurança | Usa ACLs; o usuário não altera |
| TAC (*Time-based Access Control* — baseado em tempo) | Hora e dia | Acesso só em horários permitidos |

#### 10.1.1 Controle de Acesso Discricionário (DAC)

No **DAC**, **o dono do recurso decide quem pode acessá-lo**. Exemplo: o dono de um arquivo define quem lê, grava ou executa.

#### 10.1.2 Controle de Acesso Obrigatório (MAC)

No **MAC**, cada recurso tem um **rótulo de nível de segurança** ("confidencial", "secreto", "ultrassecreto") e cada usuário uma **autorização** (*clearance*). O acesso só é liberado se forem compatíveis, e o usuário não muda as regras.

#### 10.1.3 Controle de Acesso Baseado em Funções (RBAC)

No **RBAC**, as permissões pertencem às **funções**, e cada pessoa recebe o perfil da função que ocupa. Quando alguém muda de cargo, basta trocar a função. É considerado **boa prática**.

#### 10.1.4 Controle de Acesso Baseado em Atributos (ABAC)

No **ABAC**, a decisão considera atributos do **objeto**, do **sujeito** e do **ambiente**. Exemplo: o médico vê prontuários só no hospital e durante o plantão.

#### 10.1.5 Controle de Acesso Baseado em Regras

No **controle baseado em regras**, a equipe de segurança define as condições de acesso em ACLs, como IPs permitidos. Exemplo: ninguém acessa a folha de pagamento no fim de semana.

**Importante:** a sigla **RBAC** serve para funções (*Role*) e para regras (*Rule*). Sozinha, normalmente indica funções.

#### 10.1.6 Controle de Acesso Baseado em Tempo (TAC)

No **TAC**, o acesso depende da **hora e do dia**. Exemplo: logins só em dias úteis, das 8h às 18h.

### 10.2 Privilégio Mínimo e Escalação de Privilégios

O **privilégio mínimo** dá a usuários e processos **apenas o acesso mínimo necessário**.

Na **escalação de privilégios**, o atacante explora falhas para ganhar **um nível de privilégio maior do que deveria ter** e assumir o controle do sistema.

### 10.3 Confiança Zero (Zero Trust)

A **confiança zero** (*zero trust*) **não confia automaticamente em ninguém**, nem em quem já está dentro da rede. Seu princípio é “**nunca confie, sempre verifique**”.

No modelo antigo, quem passava pelo perímetro circulava pela rede inteira. Na confiança zero, **todo ponto de decisão de acesso é um perímetro**, o que reduz o **movimento lateral** (a passagem do atacante de um sistema para outro).

| Pilar | O que protege |
| --- | --- |
| Força de trabalho | Usuários e seus dispositivos, de qualquer lugar |
| Cargas de trabalho | Aplicativos, **APIs** (*Application Programming Interfaces*), microsserviços e contêineres |
| Local de trabalho | Todos os dispositivos da rede, inclusive **IoT** (*Internet of Things* — internet das coisas) |

### 10.4 Controle de Acesso à Rede (NAC)

O **NAC** (*Network Access Control*) **aplica as políticas da organização às pessoas e aos dispositivos que tentam entrar na rede**. Suas funções são:

- verificar, **antes** de liberar o acesso, se o dispositivo cumpre as políticas;
- criar perfis de usuários e dispositivos;
- dar acesso seguro a visitantes, por portais de registro;
- bloquear, isolar ou corrigir dispositivos fora das regras.

**Observação:** o BYOD e a IoT ampliam a superfície de ataque, e o NAC é parte importante da confiança zero.

## 11. Contas e Permissões

O **gerenciamento de contas** garante que **cada usuário tenha a conta adequada à sua função** e só acesse o necessário.

### 11.1 Tipos de Contas

| Tipo | Uso |
| --- | --- |
| Usuário | Uso diário |
| Serviço | Programas em segundo plano, não pessoas |
| Convidado | Usuários temporários |
| Administrador | Apenas administrar o sistema |

**Importante:** se o administrador abrir um site infectado com a conta de administrador, o malware ganha os mesmos privilégios.

A boa prática é **substituir ou desativar as contas padrão** e nunca compartilhar contas.

### 11.2 Boas Práticas de Gerenciamento de Contas

As boas práticas são:

- liberar só o acesso necessário (privilégio mínimo);
- revisar os acessos periodicamente;
- desativar as contas que não são mais usadas;
- limitar **quando** e **de onde** cada usuário faz login.

| Recurso | O que faz | Exemplo |
| --- | --- | --- |
| Delimitação geográfica (*geofencing*) | Dispara uma ação quando o usuário entra ou sai de uma área | Bloquear acesso fora do prédio |
| Geolocalização | Identifica onde o dispositivo está | Celular no mapa |
| Marcação geográfica (*geotagging*) | Acrescenta a localização a um arquivo | Foto com coordenadas |

### 11.3 Contas Privilegiadas

As **contas privilegiadas** têm acesso elevado e são o **alvo preferido dos criminosos**. Para protegê-las:

- reduzir o número de contas privilegiadas;
- revogar os acessos quando o funcionário sai ou muda de função;
- eliminar contas compartilhadas;
- trocar as senhas automaticamente;
- registrar as sessões privilegiadas e alertar sobre comportamento incomum;
- exigir **MFA** em todo acesso administrativo.

### 11.4 Permissões de Arquivos e Pastas

As **permissões** **limitam o acesso de pessoas e grupos a pastas e arquivos**, conforme a **necessidade de saber**.

| Permissão | O que o usuário pode fazer |
| --- | --- |
| Controle total | Tudo: ver, alterar, excluir, criar e executar |
| Modificar | Alterar e excluir, mas não criar |
| Ler e executar | Ver e executar programas |
| Gravar | Criar e alterar |
| Leitura | Ver e abrir |

**Importante:** a permissão **Negar substitui qualquer outra**, mesmo para administradores.

Arquivos novos **herdam as permissões da pasta-mãe**:

| Ação | Mesmo volume | Volume diferente |
| --- | --- | --- |
| Mover | Mantém as permissões | Herda novas |
| Copiar | Herda novas | Herda novas |

Ou seja, **só mover dentro do mesmo volume mantém as permissões**.

### 11.5 Políticas de Conta no Windows

Em empresas, os computadores Windows fazem parte de um **domínio**, administrado pelo **Active Directory**. Fora dele, usa-se a **Política de Segurança Local** (`secpol.msc`).

As principais políticas são:

- **senhas**: validade, tamanho mínimo, complexidade e histórico;
- **bloqueio de conta**: bloquear depois de várias tentativas erradas;
- **auditoria**: registra eventos de login, contas, acessos e mudanças de política.

### 11.6 Gerenciamento de Autenticação

O **gerenciamento de autenticação** busca **entrada segura sem complicar a vida do usuário**.

| Solução | Como funciona |
| --- | --- |
| SSO (*Single Sign-On*) | Um conjunto de credenciais dá acesso a vários aplicativos |
| OAuth (*Open Authorization*) | Usa uma conta de outro serviço sem entregar a senha ("Entrar com Google") |
| Cofre de senhas | Guarda as credenciais sob uma senha forte |
| KBA (*Knowledge-Based Authentication*) | Redefine a senha com perguntas pessoais |

## 12. AAA na Rede: Servidores e Protocolos de Autenticação

Este módulo mostra **como o AAA é implementado na rede**: onde ficam as contas, quais protocolos comprovam a identidade e como os servidores RADIUS e TACACS+ se comparam.

### 12.1 AAA Local e AAA Baseado em Servidor

Há **duas formas de implementar o AAA**:

| Característica | AAA local | AAA baseado em servidor |
| --- | --- | --- |
| Onde ficam os usuários | No próprio roteador | Em um servidor AAA central |
| Indicado para | Redes pequenas | Redes médias e grandes |
| Escalabilidade | Baixa | Alta |

O AAA centralizado é **mais escalável e mais fácil de gerenciar** e pode usar o Active Directory ou o **LDAP** (protocolo de consulta a diretórios).

### 12.2 Protocolos de Autenticação

Um **protocolo de autenticação** define **o que as partes trocam para se autenticar**.

| Protocolo | Como funciona | Segurança |
| --- | --- | --- |
| PAP (*Password Authentication Protocol*) | Envia usuário e senha em **texto claro** | Fraca |
| CHAP (*Challenge-Handshake Authentication Protocol*) | Desafio e resposta: a senha nunca viaja pela rede | Melhor que o PAP |
| EAP (*Extensible Authentication Protocol*) | Estrutura que aceita vários métodos; comum no Wi-Fi corporativo | Depende do método |
| 802.1X | Controle de acesso por porta: só libera a conexão depois da autenticação, confirmada por um servidor RADIUS | Alta |
| Kerberos | Autenticação mútua com tíquetes; usado nos domínios Windows | Alta |

### 12.3 Servidores RADIUS e TACACS+

Os dispositivos falam com o servidor AAA central pelo **RADIUS** (*Remote Authentication Dial-In User Service*), padrão aberto, ou pelo **TACACS+** (*Terminal Access Controller Access-Control System Plus*), da Cisco.

| Característica | TACACS+ | RADIUS |
| --- | --- | --- |
| Funções | Separa as três funções do AAA | Junta autenticação e autorização |
| Padrão | Principalmente Cisco | Aberto (RFC) |
| Transporte | TCP, porta 49 | UDP, portas 1812 e 1813 |
| Criptografia | Todo o corpo do pacote | Só a senha |
| Autorização de comandos | Por usuário ou grupo | Não tem |
| Contabilidade | Limitada | Abrangente |

**Importante:** o **RADIUS criptografa só a senha**; o **TACACS+ criptografa todo o corpo do pacote**.

O TACACS+ é a melhor escolha para controlar os comandos de cada administrador. O RADIUS é muito usado com 802.1X e acesso remoto.

### 12.4 Kerberos

O **Kerberos** faz **autenticação mútua** (cliente e servidor provam a identidade) com base em **tíquetes**. O tíquete funciona como uma pulseira de evento: o usuário se identifica uma vez e mostra a pulseira em cada área.

1. o cliente se autentica e recebe um **TGT** (*Ticket-Granting Ticket*);
2. apresenta o TGT e pede acesso a um serviço;
3. recebe um **tíquete de serviço** e acessa o serviço.

![No Kerberos, o cliente se autentica uma vez e depois usa tíquetes para acessar os serviços](img/defesa/def_kerberos.png){width=6in}

Os tíquetes têm **carimbo de hora e prazo de validade**, o que impede reutilizar um tíquete antigo.

### 12.5 Contabilidade do AAA

Com o AAA centralizado, os registros de todos os dispositivos vão para um só lugar, o que **facilita a auditoria**. Incluem início e fim da conexão, comandos executados e volume de dados.

| Tipo | O que registra |
| --- | --- |
| De rede | Sessões PPP (*Point-to-Point Protocol*) com pacotes e bytes |
| De conexão | Conexões de saída, como por SSH |
| EXEC | Sessões na linha de comando do roteador |
| Do sistema | Eventos como reinicializações |
| De comandos | Comandos digitados, com data, hora e usuário |
| De recursos | Início e fim das conexões autenticadas |

## 13. Segurança Física

A **segurança física** **protege instalações e equipamentos contra o acesso físico não autorizado**.

### 13.1 Barreiras Físicas e Cercas

As **barreiras físicas** são a **camada mais externa e mais visível da defesa**. Exemplos:

- cercas e portões;
- **cabeços de amarração** (*bollards*): postes curtos que impedem a invasão com veículos;
- barreiras de entrada de veículos.

| Altura da cerca | Efeito |
| --- | --- |
| 1 metro | Só detém invasores casuais |
| 2 metros | Alta demais para invasores casuais |
| 2,5 metros | Atrasa por pouco tempo um invasor determinado |

Áreas de alta segurança acrescentam arame farpado ou concertina no topo.

### 13.2 Biometria no Controle de Acesso Físico

A biometria libera portas e áreas restritas por rosto, digital, mão, íris, retina, assinatura ou voz.

O fator mais importante na escolha é a **precisão**:

| Erro | Nome | O que acontece |
| --- | --- | --- |
| Tipo I | Falsa rejeição | Barra um usuário autorizado |
| Tipo II | Falsa aceitação | Deixa entrar quem não deveria |

**Importante:** o **erro tipo II (falsa aceitação) é o mais grave**, porque deixa um invasor entrar.

A **CER** (*Crossover Error Rate* — taxa de erro de cruzamento) é o ponto em que as duas taxas se igualam. **Quanto menor a CER, mais preciso o sistema.**

### 13.3 Vigilância

| Forma | Vantagens | Desvantagens |
| --- | --- | --- |
| Guardas | Resposta imediata e adaptação | Custo e erro humano |
| Câmeras (CFTV, circuito fechado de TV) | Monitoram e gravam sem ninguém presente | Dependem de alguém que reaja |
| Etiquetas RFID (*Radio-Frequency Identification*) | Rastreiam ativos que saem da área segura | Exigem leitores nas saídas |

Os **guardas** são a melhor solução quando é preciso **resposta instantânea**.

As etiquetas **RFID** **não precisam estar visíveis** nem na linha de visão do leitor. Exemplo: um notebook escondido em uma bolsa dispara o alerta na porta.

### 13.4 Controle de Ameaças às Instalações

As principais medidas são:

- controle de acesso e CFTV em todas as entradas;
- políticas para visitantes;
- testes de invasão física e cibernética;
- crachás com criptografia;
- treinamento e conscientização;
- etiquetagem de ativos.

## 14. Fortalecimento de Dispositivos e Serviços de Rede

O **fortalecimento** (*hardening*) consiste em **deixar exposto só o necessário**. Os invasores entram por serviços, portas abertas e configurações padrão.

### 14.1 Gerenciamento de Configuração

O **gerenciamento de configuração** é **a identificação, o controle e a auditoria de um sistema e de qualquer alteração na sua linha de base**.

A **linha de base** (*baseline*) é o **modelo de configuração para todos os sistemas semelhantes**.

Devem ser documentados:

- mapas de rede e diagramas de cabeamento;
- convenções de nomes dos computadores;
- esquema de endereçamento IP.

### 14.2 Reforço do Sistema Operacional

O **reforço** do sistema operacional consiste em **configurá-lo de forma segura, reduzindo as brechas**. As principais medidas são:

- configurar logs e auditoria;
- trocar nomes de conta e senhas padrão;
- aplicar políticas de conta;
- controlar o acesso aos arquivos.

### 14.3 Varredura de Portas

Um **scanner de portas** **descobre quais portas de um dispositivo estão abertas**. A **porta** é o número que identifica um serviço (exemplo: 80 é o HTTP).

Administradores e atacantes usam scanners. Por isso, **apenas as portas necessárias devem ficar abertas**.

### 14.4 DHCP

O **DHCP** (*Dynamic Host Configuration Protocol*) **atribui automaticamente endereço IP** e outras configurações aos dispositivos.

O atacante pode derrubar o servidor DHCP ou criar um **servidor falso**, que desvia o tráfego das vítimas.

O **DHCP snooping** **impede que servidores DHCP falsos entreguem endereços**.

Outras medidas: proteger fisicamente o servidor, aplicar correções, deixá-lo atrás de um firewall e monitorar os registros.

### 14.5 DNS

O **DNS** (*Domain Name System*) **converte nomes, como www.cisco.com, em endereços IP**. Atacando o DNS, o criminoso **redireciona o tráfego para sites falsos**.

As **DNSSEC** (*DNS Security Extensions*) usam **assinaturas digitais** para autenticar as respostas DNS. Outras medidas:

- manter o software atualizado;
- não informar a versão do programa DNS;
- separar servidores internos e externos;
- restringir as **transferências de zona** (cópia da lista completa de nomes de um domínio, que entregaria o mapa da rede);
- analisar os logs.

### 14.6 ICMP

O **ICMP** (*Internet Control Message Protocol*) **envia mensagens de erro e de controle**. O comando **ping** o usa para testar se um host responde.

Os atacantes usam o ICMP para:

- **reconhecimento** (descobrir quais máquinas estão ligadas);
- **canal secreto** (dados escondidos em mensagens de ping);
- **DoS** (*Denial of Service* — negação de serviço, que tira um serviço do ar).

Por isso, muitas redes filtram o ICMP.

### 14.7 RIP

O **RIP** (*Routing Information Protocol*) é um protocolo de roteamento que escolhe a rota pela contagem de **saltos**, com **máximo de 15 saltos**. Ataques ao roteamento podem redirecionar o tráfego. Proteção: **autenticação** entre roteadores e atualizações.

### 14.8 NTP

O **NTP** (*Network Time Protocol*) **sincroniza os relógios dos dispositivos**. A hora correta é essencial para:

- rastrear eventos nos logs;
- validar certificados, que têm data de validade.

Os criminosos atacam o NTP para esconder os carimbos de hora do ataque. Proteção: **autenticação NTP**.

## 15. Segmentação de Rede

A **segmentação** é a **divisão de uma rede em partes menores para melhorar o desempenho e a segurança**. Quem invade um segmento não alcança automaticamente os outros.

### 15.1 VLANs

Uma **VLAN** (*Virtual Local Area Network* — rede local virtual) **agrupa dispositivos de forma lógica**, não importa em que switch estejam ligados.

**Importante:** a **LAN** se baseia em **conexões físicas**; a **VLAN**, em **conexões lógicas**.

Os **troncos** (*trunks*) são portas entre switches que **transportam o tráfego de várias VLANs**.

Entre suas principais vantagens estão:

- segmentar por função, equipe ou aplicativo;
- isolar dados confidenciais, como a VLAN do RH;
- limitar o **broadcast** (mensagens para todos) a cada VLAN.

### 15.2 Zona Desmilitarizada (DMZ)

A **DMZ** (*Demilitarized Zone* — zona desmilitarizada) é uma **pequena rede entre a rede privada e a internet**. Nela ficam os servidores acessados de fora, como **servidores web e de e-mail**.

A maioria das redes tem de **duas a quatro zonas de risco**:

| Zona | Risco | Confiança |
| --- | --- | --- |
| LAN privada | Baixo | Alta |
| Extranet (rede com parceiros) | Médio-baixo | Médio-alta |
| DMZ | Médio-alto | Médio-baixa |
| Internet | Alto | Baixa |

Os firewalls controlam o tráfego:

- **leste-oeste**: dentro da rede, entre servidores;
- **norte-sul**: que entra e sai da rede.

| Característica | VLAN | DMZ |
| --- | --- | --- |
| O que separa | Setores da rede interna | Servidores públicos da rede interna |
| Onde fica | Dentro da LAN | Entre a LAN e a internet |
| Exemplo | VLAN do RH | Servidor web da empresa |

## 16. Listas de Controle de Acesso (ACLs)

A **ACL** funciona como o porteiro de um condomínio: decide quais pacotes passam por um roteador.

### 16.1 O que é uma ACL

A **ACL** (*Access Control List* — lista de controle de acesso) é uma **série de comandos que filtra pacotes de acordo com as informações do cabeçalho**. Cada linha é uma **ACE** (*Access Control Entry*): permitir (*permit*) ou negar (*deny*).

Aplicada a uma **interface** do roteador, a ACL compara cada pacote com as ACEs, em ordem. Essa é a **filtragem de pacotes**, que atua nas **camadas 3 (endereços IP) e 4 (portas TCP e UDP)** do modelo OSI.

Usos comuns:

- limitar o tráfego, como bloquear vídeo;
- aceitar atualizações de roteamento só de fontes conhecidas;
- dar segurança básica, liberando a rede do RH só a autorizados;
- filtrar por tipo de tráfego: permitir e-mail e negar Telnet;
- priorizar tráfego, como a voz, com a **QoS** (qualidade de serviço).

### 16.2 Tipos de ACL

Há dois tipos de ACL IPv4:

- **padrão**: filtra **apenas pelo endereço IPv4 de origem**;
- **estendida**: filtra por **origem, destino, portas e protocolo**.

As **ACLs nomeadas** são o **método preferido**. Exemplo de nome: FTP-FILTER.

| Característica | ACL padrão | ACL estendida |
| --- | --- | --- |
| Camadas analisadas | 3 | 3 e 4 |
| Endereço | Só origem | Origem e/ou destino |
| Portas e protocolo | Não | Sim |
| Números | 1–99 e 1300–1999 | 100–199 e 2000–2699 |

### 16.3 Como a ACL Processa os Pacotes

A ACL filtra em dois sentidos:

- **de entrada** (*inbound*): antes do roteamento; mais eficiente;
- **de saída** (*outbound*): depois do roteamento.

De forma simplificada, o processo ocorre da seguinte maneira:

1. o roteador lê o endereço do pacote;
2. compara com cada ACE, **de cima para baixo**;
3. **na primeira correspondência**, permite ou nega e para;
4. se nada corresponder, descarta.

![A ACL é lida de cima para baixo e para na primeira correspondência; o que não corresponde a nada é descartado](img/defesa/def_acl.png){width=6in}

Toda ACL termina com uma **negação implícita**, que nega tudo o que não foi permitido.

**Importante:** por isso, **toda ACL precisa ter pelo menos uma instrução de permitir**.

### 16.4 Máscaras Curinga

A **máscara curinga** (*wildcard mask*) **indica quais bits do endereço devem ser verificados**. Segue a lógica inversa da máscara de sub-rede:

- bit **0** → precisa corresponder;
- bit **1** → é ignorado.

| Máscara curinga | Efeito |
| --- | --- |
| 0.0.0.0 | Verifica todos os bits (um host) |
| 0.0.0.255 | Ignora o último octeto (uma rede /24) |
| 0.0.0.15 | Ignora os 4 últimos bits |

Exemplos:

- um host: `permit 192.168.1.1 0.0.0.0`;
- uma rede: `permit 192.168.1.0 0.0.0.255`.

### 16.5 Exemplo Resolvido: Cálculo de Máscaras Curinga

Atalho: **subtrair a máscara de sub-rede de 255.255.255.255**.

| Situação | Máscara de sub-rede | Máscara curinga |
| --- | --- | --- |
| Rede 192.168.3.0/24 | 255.255.255.0 | 0.0.0.255 |
| Rede 192.168.3.32/28 | 255.255.255.240 | 0.0.0.15 |
| Redes 192.168.10.0 e .11.0 (/23) | 255.255.254.0 | 0.0.1.255 |
| Redes 192.168.16.0 a .31.0 (/20) | 255.255.240.0 | 0.0.15.255 |

Conferência do segundo caso, no último octeto:

| Item | Binário | Decimal |
| --- | --- | --- |
| Endereço | 0010 0000 | 32 |
| Curinga | 0000 1111 | 15 |
| Menor endereço | 0010 0000 | 32 |
| Maior endereço | 0010 1111 | 47 |

Portanto, `192.168.3.32 0.0.0.15` vale para **192.168.3.32 a 192.168.3.47**.

### 16.6 Palavras-chave host e any

- **host** → um único endereço (máscara 0.0.0.0);
- **any** → qualquer endereço (0.0.0.0 255.255.255.255).

### 16.7 Planejamento

A ACL deve ser escrita antes em um editor de texto, colada no equipamento e **testada com cuidado**.

### 16.8 ACL Padrão

Sintaxe: `access-list número {deny | permit | remark} origem [curinga] [log]`

- **remark**: comentário para documentação;
- **log**: registra os pacotes que correspondem, mas usa muita CPU.

ACL nomeada: `ip access-list standard NOME`.

### 16.9 ACL Estendida

Sintaxe: `access-list número {deny | permit} protocolo origem curinga destino curinga [operador porta]`

- **protocolo**: ip, tcp, udp ou icmp;
- **operador**: eq (igual), neq (diferente), lt (menor), gt (maior).

| Nome | Porta | Serviço |
| --- | --- | --- |
| ftp-data / ftp | 20 / 21 | FTP |
| telnet | 23 | Telnet |
| smtp | 25 | Envio de e-mail |
| domain | 53 | DNS |
| www | 80 | HTTP |
| pop3 | 110 | Recebimento de e-mail |

Exemplo que libera a navegação web da rede 192.168.10.0/24:

```
ip access-list extended SURFING
 permit tcp 192.168.10.0 0.0.0.255 any eq 80
 permit tcp 192.168.10.0 0.0.0.255 any eq 443
```

### 16.10 A Palavra-chave established

A palavra-chave **established** deixa voltar **apenas as respostas** a conexões abertas de dentro. O tráfego TCP iniciado de fora é negado.

```
ip access-list extended BROWSING
 permit tcp any 192.168.10.0 0.0.0.255 established
```

### 16.11 Aplicação nas Interfaces e nas Linhas VTY

A ACL só funciona depois de **aplicada**:

- interface: `ip access-group NOME {in | out}`;
- linhas **VTY** (acesso remoto por Telnet e SSH): `access-class NOME in`.

O comando `show access-lists` mostra as ACLs e quantas vezes cada ACE foi usada.

### 16.12 Modificação de ACLs

Há dois métodos:

- **editor de texto**: copiar, corrigir, apagar a antiga e colar a nova;
- **número de sequência**: apagar a linha errada (`no 10`) e digitá-la de novo, porque não dá para sobrescrever um número existente.

### 16.13 Diretrizes e Posicionamento

As diretrizes principais são:

- organizar **do mais específico ao mais genérico**;
- novas ACEs entram no final;
- **uma ACL por interface, por protocolo e por direção**.

O posicionamento segue a regra:

- **ACL estendida** → o **mais perto possível da origem**;
- **ACL padrão** → o **mais perto possível do destino**, porque só enxerga a origem.

#### 16.13.1 Exemplo Resolvido: Onde Colocar Cada ACL

Três roteadores (R1, R2 e R3) em linha; as redes 192.168.10.0 e .11.0 ficam no R1, e as redes .30.0 e .31.0 no R3.

- **Bloquear a rede .10 rumo à .30 (ACL padrão)**: na **saída da G0/0/0 do R3**, ligada à rede .30; assim a .10 continua alcançando a .31.
- **Impedir Telnet da rede .11 para a .30 (ACL estendida)**: na **entrada da G0/0/1 do R1**, onde só passa o tráfego da rede .11.

### 16.14 Resumo dos Comandos de ACL

| Comando | Função |
| --- | --- |
| `access-list 1–99` | ACL padrão numerada |
| `access-list 100–199` | ACL estendida numerada |
| `ip access-list standard NOME` | ACL padrão nomeada |
| `ip access-list extended NOME` | ACL estendida nomeada |
| `ip access-group ... in/out` | Aplica na interface |
| `access-class ... in` | Aplica nas linhas VTY |
| `show access-lists` | Mostra as ACLs e os contadores |

### 16.15 Bloqueio de Endereços Falsificados

Na **falsificação de IP** (*IP spoofing*), o atacante **coloca um endereço de origem falso** no pacote.

A interface voltada para a internet **nunca deve aceitar pacotes com estes endereços de origem**:

- 0.0.0.0 e 255.255.255.255 (broadcast);
- *loopback* (127.0.0.0/8);
- APIPA (169.254.0.0/16);
- privados (10.0.0.0/8, 172.16.0.0/12 e 192.168.0.0/16);
- multicast (224.0.0.0/4).

A interface da rede local **só deve aceitar origem da própria rede local**.

### 16.16 Liberação Apenas dos Serviços Necessários

Uma estratégia eficaz é **permitir explicitamente só os serviços usados**, como DNS, **SMTP** (*Simple Mail Transfer Protocol*, envio de e-mail) e FTP nos servidores públicos, e SSH para os administradores.

### 16.17 Controle do ICMP

Os atacantes usam o **echo** (ping) para descobrir hosts e o **redirect** para alterar rotas. Por isso, **echo e redirect devem ser bloqueados na entrada**.

Mensagens ICMP necessárias:

| Sentido | Mensagem | Para que serve |
| --- | --- | --- |
| Entrando | echo-reply | Resposta aos pings dos usuários |
| Entrando | source-quench | Reduzir a taxa de tráfego |
| Entrando | unreachable | Aviso de pacote negado |
| Saindo | echo | Pings dos usuários |
| Saindo | parameter-problem | Problema no cabeçalho |
| Saindo | packet-too-big | Descobrir a **MTU** (maior tamanho de pacote) |

### 16.18 Proteção do SNMP

O mais eficaz é **desativar o SNMP quando ele não for necessário** (`no snmp-server`).

### 16.19 Riscos da Transição para o IPv6

Na **pilha dupla** (*dual stack*), o dispositivo tem **IPv4 e IPv6 ao mesmo tempo**. Um firewall só de IPv4 não enxerga o tráfego IPv6.

O **Teredo** **encapsula IPv6 dentro de pacotes UDP IPv4**: o firewall vê só UDP comum, e o atacante passa.

Proteção: **filtrar o IPv6 na borda**, com ACLs IPv6.

### 16.20 ACLs IPv6

Diferenças das ACLs IPv6:

- **não existe ACL IPv6 padrão**: todas são nomeadas e parecidas com a estendida;
- criadas com `ipv6 access-list NOME`;
- aplicadas com `ipv6 traffic-filter NOME {in | out}`.

Terminam com três entradas implícitas: permitir **nd-na** e **nd-ns** (mensagens do **NDP**, *Neighbor Discovery Protocol*, que faz o papel do ARP no IPv6) e negar o resto.

**Importante:** um `deny ipv6 any any` sem antes permitir nd-na e nd-ns faz o **NDP parar de funcionar**.

| Característica | ACL IPv4 | ACL IPv6 |
| --- | --- | --- |
| Tipos | Padrão e estendida | Só um tipo |
| Identificação | Número ou nome | Só nome |
| Aplicação | `ip access-group` | `ipv6 traffic-filter` |
| Final implícito | Nega tudo | Permite nd-na e nd-ns e nega o resto |

## 17. Firewalls

O **firewall** é um sistema que **aplica uma política de controle de acesso entre redes** com níveis de confiança diferentes. Vai além da ACL, que filtra pacote por pacote.

### 17.1 Características do Firewall

Todo firewall:

- é resistente a ataques;
- é o **único ponto de trânsito** entre a rede interna e a externa;
- aplica a política de controle de acesso.

Seus benefícios são:

- não expor hosts e aplicativos sensíveis a usuários não confiáveis;
- bloquear dados maliciosos;
- concentrar o controle de acesso em poucos equipamentos.

Suas limitações são:

- mal configurado, vira um **ponto único de falha**;
- usuários podem tentar contorná-lo;
- pode reduzir o desempenho;
- tráfego não autorizado pode passar escondido em tráfego legítimo.

### 17.2 Tipos de Firewall

| Tipo | Camadas analisadas | Como decide |
| --- | --- | --- |
| Filtragem de pacotes (sem estado) | 3 e 4 | Regras fixas, pacote por pacote |
| Com estado (*stateful*) | 3, 4 e 5 | Regras + tabela de conexões |
| Gateway de aplicação (*proxy*) | 3, 4, 5 e 7 | Conecta-se ao servidor em nome do cliente |
| NGFW (*Next-Generation Firewall*) | Até a 7 | Estado + controle de aplicativos + prevenção de intrusão |

Detalhes de cada tipo:

- **filtragem de pacotes**: analisa IPs, portas e protocolo; exemplo: bloquear a porta 25 (SMTP);
- **com estado**: **o mais versátil e o mais comum**; anota cada conversa aberta de dentro na **tabela de estado** e só deixa voltar o que corresponde a uma delas;
- **gateway de aplicação**: o servidor só enxerga o proxy;
- **NGFW**: inclui IPS e **reconhecimento e controle de aplicativos** (liberar o WhatsApp e bloquear jogos, por exemplo).

Outros tipos:

- **baseado em host**: software de firewall no próprio computador;
- **transparente**: filtra entre duas interfaces sem ter endereço IP próprio;
- **híbrido**: combina tipos.

### 17.3 Firewall de Filtragem de Pacotes

| Vantagens | Desvantagens |
| --- | --- |
| Regras simples | Enganado pela falsificação de IP |
| Baixo impacto no desempenho | Filtra mal pacotes fragmentados |
| Disponível na maioria dos roteadores | ACLs complexas são difíceis de manter |
| Baixo custo | Não lida bem com portas negociadas na hora (FTP, vídeo) |
| | **Não guarda estado**: analisa cada pacote isoladamente |

### 17.4 Firewall com Estado

| Benefícios | Limitações |
| --- | --- |
| **Principal meio de defesa** | **Não inspeciona a camada de aplicação** |
| Filtragem mais rigorosa que a de pacotes | Acompanha mal o UDP e o ICMP |
| Bom desempenho | Dificuldade com portas negociadas na hora |
| **Defende contra falsificação e DoS** | Não autentica usuários |
| Logs mais ricos | |

### 17.5 Firewalls no Projeto de Rede

Com **duas interfaces**, o firewall separa a rede privada da pública:

- privada → pública: permitido e inspecionado; as respostas voltam;
- pública → privada: bloqueado.

Com a DMZ, o firewall tem **três interfaces**:

| Origem → Destino | Tratamento |
| --- | --- |
| Privada → pública ou DMZ | Inspecionado, com pouca restrição |
| DMZ → privada | Bloqueado |
| DMZ → pública | Permitido seletivamente |
| Pública → DMZ | Permitido seletivamente (e-mail, DNS, HTTP, HTTPS) |
| Pública → privada | Bloqueado |

![Com a DMZ, o firewall tem três interfaces e trata de forma diferente cada sentido do tráfego](img/defesa/def_dmz.png){width=6in}

### 17.6 Defesa em Camadas com Firewalls

A defesa em camadas combina **tipos diferentes de firewall**. Cobre quatro áreas:

- **núcleo da rede**: malware e anomalias;
- **perímetro**: limites entre zonas;
- **comunicações**: criptografia e VPNs;
- **endpoints**: identidade e conformidade dos aparelhos.

Na **sub-rede rastreada** (*screened subnet*), o tráfego passa por várias barreiras:

Internet → Roteador de borda → Firewall ou host bastião → Roteador interno → Host de destino

O **host bastião** é um computador **reforçado para resistir a ataques**, normalmente na DMZ.

### 17.7 Limites e Boas Práticas

O firewall **não**:

- impede intrusões entre hosts da mesma rede;
- protege contra pontos de acesso sem fio não autorizados;
- substitui o backup;
- substitui usuários bem informados.

As boas práticas são:

- **negar todo o tráfego por padrão** e permitir só o necessário;
- controlar o acesso físico ao firewall;
- monitorar os logs;
- registrar e testar toda mudança de configuração.

### 17.8 Firewall de Política Baseada em Zona (ZPF) e Zonas de Segurança

Os roteadores Cisco funcionam como firewall com estado em dois modelos:

- **clássico**: política em cada interface (`ip inspect`);
- **ZPF** (*Zone-Based Policy Firewall*): a política vale **para o tráfego que passa de uma zona para outra**.

Uma **zona** é um **grupo de interfaces com necessidades de segurança semelhantes**, como privada, pública e DMZ.

As regras básicas são:

- **mesma zona** → o tráfego passa livremente;
- **zonas diferentes** → bloqueado, a menos que uma política permita.

A **zona self** é **o próprio roteador**. Seu tráfego (SSH, SNMP, roteamento) passa, a menos que haja um par de zonas com a self **e** uma política.

### 17.9 Benefícios do ZPF

Seus benefícios são:

- não depende de ACLs;
- bloqueia tudo o que não for explicitamente permitido;
- políticas fáceis de ler;
- cada política vale em **um único sentido**.

**Importante:** uma interface não pode estar em zona e usar o `ip inspect` ao mesmo tempo.

### 17.10 Projeto do ZPF

1. determinar as zonas;
2. definir as políticas entre cada **par de zonas** (origem → destino);
3. projetar a infraestrutura física, com redundância;
4. identificar subconjuntos dentro das zonas.

### 17.11 Ações do ZPF

- **Inspect**: inspeção com estado; **permite automaticamente as respostas**;
- **Drop**: como o deny; é a ação padrão;
- **Pass**: como o permit, **sem estado e em um único sentido**.

**Observação:** o Drop descarta em silêncio, sem enviar mensagem ICMP.

### 17.12 Regras para o Tráfego que Atravessa o Roteador

| Situação | Resultado |
| --- | --- |
| Nenhuma interface em zona | Passa |
| Só uma interface em zona | Descarta |
| Mesma zona | Passa |
| Zonas diferentes, sem par ou sem política | Descarta |
| Zonas diferentes, com par e política | Conforme a política |

**Importante:** o tráfego **nunca flui entre uma interface em zona e outra fora de zona**.

### 17.13 Configuração do ZPF

A configuração tem cinco etapas:

Zonas → class-map → policy-map → zone-pair → Interfaces nas zonas

#### 17.13.1 Exemplo Resolvido: Rede Privada Acessando a Web

A G0/0 fica na zona privada e a S0/0/0, na pública.

```
zone security PRIVATE
zone security PUBLIC
class-map type inspect match-any HTTP-TRAFFIC
 match protocol http
 match protocol https
 match protocol dns
policy-map type inspect PRIV-TO-PUB-POLICY
 class type inspect HTTP-TRAFFIC
  inspect
zone-pair security PRIV-PUB source PRIVATE destination PUBLIC
 service-policy type inspect PRIV-TO-PUB-POLICY
interface GigabitEthernet0/0
 zone-member security PRIVATE
interface Serial0/0/0
 zone-member security PUBLIC
```

- **class-map** identifica o tráfego (**match-any**: pelo menos um critério; **match-all**: todos);
- **policy-map** define a ação;
- **zone-pair** liga as zonas e aplica a política.

Resultado: da zona pública só entram as respostas das sessões abertas pela privada.

### 17.14 Verificação e Cuidados

Todo policy-map termina com um **drop** na `class class-default`, como a negação implícita das ACLs.

Comandos de verificação: `show zone security`, `show zone-pair security` e `show policy-map type inspect zone-pair sessions`.

Cuidados:

- testar a conectividade **antes** e depois de configurar;
- uma interface pertence a uma única zona;
- o `zone-member` causa interrupção temporária até a outra zona ser configurada.

| Característica | Firewall clássico | ZPF |
| --- | --- | --- |
| Onde a política é aplicada | Em cada interface | Entre zonas |
| Depende de ACLs | Sim | Não |
| Interface nova | Precisa de configuração | Herda as regras da zona |

## 18. Segurança Sem Fio e de Dispositivos Móveis

Os dispositivos sem fio e móveis são hoje a **maioria dos dispositivos nas redes**. Estão sujeitos a roubo, interceptação (*sniffing*) e ataques *man-in-the-middle*. A melhor proteção combina **autenticação e criptografia**.

### 18.1 Padrões de Segurança Sem Fio

Os padrões de segurança do Wi-Fi evoluíram nesta ordem:

WEP → WPA → WPA2 → WPA3

| Padrão | Características | Situação |
| --- | --- | --- |
| WEP (*Wired Equivalent Privacy*) | Primeiro padrão; quebrado em minutos | Fraco, não usar |
| WPA (*Wi-Fi Protected Access*) | **TKIP** (*Temporal Key Integrity Protocol*) e **MIC** (*Message Integrity Check*), que detecta dados alterados | Substituiu o WEP |
| WPA2 | **AES** obrigatório, com **CCMP** no lugar do TKIP | Seguro |
| WPA3 | Criptografia mais robusta e troca de chaves melhor | O mais atual |

Modos de uso:

- **Personal (PSK, *Pre-Shared Key*)**: todos usam a mesma senha do Wi-Fi; comum em casa;
- **Enterprise**: cada pessoa entra com o próprio usuário e senha, conferidos por um servidor.

O **WPS** (*Wi-Fi Protected Setup*) facilita conectar dispositivos, mas o **PIN pode ser descoberto por força bruta**. Deve ser **desativado**.

### 18.2 Autenticação em Redes Sem Fio

O **802.11** (padrão Wi-Fi) original tem **dois tipos de autenticação**:

- **sistema aberto**: qualquer dispositivo se conecta;
- **chave compartilhada**: autentica e criptografa entre cliente e **ponto de acesso** (*access point*, AP).

O **EAP** (*Extensible Authentication Protocol*) é a estrutura de autenticação das redes corporativas. De forma simplificada:

1. o usuário pede a conexão ao AP;
2. o AP repassa a identificação e a senha ao **servidor de autenticação**;
3. o servidor confirma as credenciais;
4. o usuário se conecta.

| Método | Certificado no cliente | Certificado no servidor | Implantação | Segurança |
| --- | --- | --- | --- | --- |
| EAP-TLS | Sim | Sim | Difícil | Alta |
| PEAP (*Protected EAP*: túnel TLS com usuário e senha dentro) | Não | Sim | Moderada | Média |
| EAP-TTLS (*Tunneled TLS*) | Não | Sim | Moderada | Média |
| EAP-FAST (Cisco; credencial própria) | Não | Não | Fácil | Média |

**Importante:** o **EAP-TLS é o mais seguro e o mais difícil de implantar**, porque exige certificado nas duas pontas.

### 18.3 Pontos de Acesso Não Autorizados e Autenticação Mútua

O **ponto de acesso não autorizado** (*rogue AP*) **imita um ponto de acesso legítimo** para as vítimas se conectarem a ele. É um ataque man-in-the-middle **muito difícil de detectar**.

A proteção é a **autenticação mútua**: **as duas pontas se autenticam antes de se conectar**.

### 18.4 Comunicação dos Dispositivos Móveis

| Método | Como funciona | Exemplo |
| --- | --- | --- |
| Wi-Fi e Bluetooth | Sinais sem fio | Fone de ouvido |
| NFC (*Near-Field Communication*) | Comunicação sem contato a curtíssima distância | Pagamento por aproximação |
| Infravermelho (IR) | Curto alcance | Controle da TV |
| USB | O único com fio | Carregar, transferir dados, perícia forense |

Os celulares também usam a rede da operadora: **LTE** (4G) e **5G**.

### 18.5 Gerenciamento de Dispositivos Móveis

Dois modelos de aparelho:

- **COPE** (*Corporate-Owned, Personally Enabled*): aparelho da empresa com uso pessoal permitido;
- **BYOD**: aparelho do funcionário.

As principais formas de gerenciamento são:

- **conteinerização**: área criptografada que **separa os dados da empresa dos dados pessoais**;
- **gerenciamento de conteúdo**: controla aplicativos de compartilhamento, como Dropbox e Google Drive;
- **gerenciamento de aplicativos**: a **lista de permissões** (*whitelisting*) só libera aplicativos autorizados.

### 18.6 Ameaças e Proteções dos Dispositivos Móveis

| Técnica | Plataforma | O que faz | Risco |
| --- | --- | --- | --- |
| Jailbreak | Apple | Remove a restrição de só rodar aplicativos autorizados | Alto |
| Root | Android | Dá acesso administrativo total | Alto |
| Sideloading | Ambas | Instala aplicativos de fora da loja oficial | Menor, mas existe |

Aparelhos com jailbreak ou root são marcados como **não conformes** e bloqueados.

As proteções são:

- bloqueio de tela (senha, PIN ou padrão);
- biometria;
- **autenticação com reconhecimento de contexto**: libera conforme o comportamento normal (local, horário);
- **limpeza remota** em caso de perda ou roubo;
- criptografia completa do dispositivo.

### 18.7 Rastreamento por GPS

O **GPS** (*Global Positioning System*) localiza o aparelho com precisão de cerca de **5 metros**. Aplicativos o usam para check-in, delimitação geográfica e **notificações push**.

**Observação:** criminosos também usam notificações push para capturar dados.

## 19. Resiliência e Alta Disponibilidade

A **resiliência** torna um sistema **tolerante a falhas**: ele continua funcionando quando algo dá errado. O objetivo é **reduzir ao mínimo o tempo de inatividade**.

### 19.1 Alta Disponibilidade

A **alta disponibilidade** descreve **sistemas concebidos para evitar períodos de inatividade**. Segue três princípios:

1. **eliminar os pontos únicos de falha**, com componentes redundantes e espera ativa (*hot standby*);
2. **garantir uma transição confiável**, com energia e comunicação de reserva;
3. **detectar as falhas assim que ocorrem**.

O **ponto único de falha** (*SPOF*, *Single Point of Failure*) é **qualquer parte cuja falha derruba o sistema inteiro**: um equipamento, um processo ou até uma pessoa.

Termos relacionados:

- **cluster de alta disponibilidade**: vários computadores processam o mesmo serviço; se um falha, os outros continuam;
- **tolerância a falhas**: o sistema segue funcionando se componentes falharem;
- **resiliência do sistema**: manter dados e processamento disponíveis mesmo sob ataque.

### 19.2 Os Cinco Noves

Os **cinco noves** significam **99,999% de disponibilidade**, ou **menos de 5,26 minutos de inatividade por ano**.

#### 19.2.1 Exemplo Resolvido: Tempo de Inatividade nos Cinco Noves

| Etapa | Cálculo | Resultado |
| --- | --- | --- |
| Minutos no ano | 365 × 24 × 60 | 525.600 min |
| Fração de inatividade | 100% − 99,999% | 0,00001 |
| Inatividade máxima | 525.600 × 0,00001 | 5,256 ≈ 5,26 min |

Para chegar aos cinco noves, usam-se:

- sistemas padronizados;
- **clustering**: vários dispositivos parecem um só;
- componentes compartilhados.

### 19.3 Redundância N+1

Na **redundância N+1**, os componentes necessários (N) têm **pelo menos um de reserva (+1)**, como o estepe de um carro.

**Observação:** o N+1 suporta a perda de um componente, não de todos.

### 19.4 RAID

O **RAID** (*Redundant Array of Independent Disks*) **distribui os dados entre vários discos**. Se um disco falha, os dados são recuperados dos outros.

| Técnica | Como funciona | Protege contra falha de disco? |
| --- | --- | --- |
| Espelhamento | Grava os dados duplicados em outro disco | Sim |
| Distribuição (*striping*) | Espalha os dados por vários discos | Não, sozinha |
| Paridade | Somas de verificação que permitem reconstruir os dados | Sim |

**Importante:** o **RAID 0 usa apenas distribuição e não tem redundância**. Protegem contra falha o **RAID 1** (espelhamento) e o **RAID 5** (paridade).

### 19.5 Spanning Tree Protocol (STP)

Cabos redundantes entre switches criam **loops**: os quadros circulam sem parar e derrubam a rede.

O **STP** (*Spanning Tree Protocol*) **bloqueia de propósito os caminhos redundantes**, deixando um só caminho lógico. Se um cabo falha, o STP desbloqueia o caminho alternativo.

#### 19.5.1 Exemplo Resolvido: o STP Diante de uma Falha

Três switches (S1, S2 e S3) em triângulo; a porta de S2 para S3 está bloqueada.

1. o link S2–S1 falha;
2. S2 desbloqueia a porta para S3, e o tráfego segue S2 → S3 → S1;
3. quando o link volta, o STP bloqueia de novo S2–S3.

### 19.6 Redundância de Roteador

O **gateway padrão** sozinho é um ponto único de falha. Com um roteador de reserva, os dois compartilham um **endereço IP virtual**, usado pelos computadores como gateway. Se o ativo falha, o de reserva assume.

Essa é a **redundância de primeiro salto**. Protocolos:

- **HSRP** (*Hot Standby Router Protocol*, da Cisco);
- **VRRP** (*Virtual Router Redundancy Protocol*, padrão aberto);
- **GLBP** (*Gateway Load Balancing Protocol*, da Cisco), que também divide a carga.

### 19.7 Redundância de Local

| Replicação | Sincronização | Largura de banda | Distância entre locais |
| --- | --- | --- | --- |
| Síncrona | Em tempo real | Alta | Pequena |
| Assíncrona | Quase em tempo real | Menor | Maior |
| Ponto no tempo | Periódica | A menor | Qualquer |

### 19.8 Design Resiliente

O **design resiliente** é **mais do que adicionar redundância**: é planejar para que a recuperação seja rápida e testar as configurações.

A **resiliência de aplicativos** é a capacidade de o aplicativo continuar funcionando quando um componente falha. Quanto maior a disponibilidade, maiores a complexidade e o custo:

| Solução | Complexidade e custo |
| --- | --- |
| Hardware tolerante a falhas | Os maiores |
| Arquitetura de cluster | Intermediários |
| Backup e restauração | Os menores |

Nos equipamentos Cisco, a **configuração resiliente do IOS** guarda uma cópia protegida do sistema e da configuração, que o usuário não consegue apagar.

### 19.9 Backups

O **backup** é **uma das formas mais eficazes de proteger contra a perda de dados**. Ao planejá-lo, considera-se:

- **frequência**: backup completo periódico e parciais frequentes;
- **armazenamento**: cópias em local externo;
- **segurança**: backups protegidos por senha;
- **validação**: conferir sempre os backups.

### 19.10 Energia

As regras gerais são:

- fonte de alimentação separada para o data center;
- alimentação redundante;
- condicionamento da energia;
- **nobreak** (UPS, *Uninterruptible Power Supply*) para desligar os sistemas normalmente.

| Categoria | Evento | O que é |
| --- | --- | --- |
| Excesso | Pico (*spike*) | Alta tensão momentânea |
| Excesso | Sobretensão (*surge*) | Alta tensão prolongada |
| Perda | Falha (*fault*) | Perda momentânea |
| Perda | Blecaute | Perda completa |
| Degradação | Afundamento (*sag*) | Baixa tensão momentânea |
| Degradação | Subtensão (*brownout*) | Baixa tensão prolongada |
| Degradação | Corrente de partida (*inrush*) | Sobrecarga inicial |

### 19.11 Climatização (HVAC)

O **HVAC** (*Heating, Ventilation and Air Conditioning*) controla **temperatura, umidade e circulação do ar**. Todo equipamento tem faixas aceitáveis de temperatura e umidade.

**Observação:** sistemas de HVAC conectados à internet e acessados por terceiros são um risco de segurança.

## 20. Segurança de Aplicações

A **segurança de aplicações** protege os programas, sites e serviços da organização. Deve ser **prioridade em todas as etapas: desenvolvimento, testes e implantação**.

### 20.1 Etapas do Desenvolvimento de Aplicações

Desenvolvimento e teste → Preparação → Produção

| Ambiente | O que acontece |
| --- | --- |
| Desenvolvimento e teste | Código escrito e testado; falhas são **muito mais fáceis de corrigir nessa fase** |
| Preparação (*staging*) | Ambiente igual ao de produção, para confirmar as configurações de segurança |
| Produção | Uso real, com clientes de verdade |

Ferramentas e termos:

- **controle de versão** (como o Git): rastreia as alterações no código;
- **sandbox**: ambiente isolado para trabalhar sem afetar o sistema real;
- **provisionamento** e **desprovisionamento**: criação e remoção do software.

### 20.2 Técnicas de Codificação Segura

| Técnica | O que faz |
| --- | --- |
| Normalização | Converte cada entrada para a forma mais simples, o que ajuda a achar entradas maliciosas |
| Procedimento armazenado | Comandos SQL prontos, guardados no banco, que dificultam a injeção de SQL |
| Ofuscação | Esconde os dados com caracteres aleatórios |
| Camuflagem | Troca dados confidenciais por fictícios realistas |
| Reutilização de código e SDKs | Código pronto, mais rápido e barato |

A ofuscação e a camuflagem dificultam a **engenharia reversa**.

**Importante:** uma vulnerabilidade no código reaproveitado passa para todos os aplicativos que o usam.

### 20.3 Validação de Entrada

**Controlar o que entra no banco de dados é essencial para a integridade dos dados.** Muitos ataques enviam dados malformados para travar o aplicativo ou fazê-lo revelar informações.

A **regra de validação** confere se os dados estão **dentro dos parâmetros definidos**:

| Critério | O que verifica | Exemplo |
| --- | --- | --- |
| Tamanho | Número de caracteres | CEP com 8 dígitos |
| Formato | Formato definido | Data DD/MM/AAAA |
| Consistência | Dados que combinam entre si | Cidade compatível com o estado |
| Intervalo | Valor entre mínimo e máximo | Idade entre 0 e 120 |
| Dígito verificador | Cálculo extra que detecta erros de digitação | Últimos dígitos do CPF |

#### 20.3.1 Exemplo Resolvido: Dígito Verificador do ISBN-10

Para os nove primeiros dígitos 1 5 8 7 1 4 3 7 3, multiplica-se cada dígito por um peso de 10 a 2 e somam-se os resultados:

| Dígito | 1 | 5 | 8 | 7 | 1 | 4 | 3 | 7 | 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Peso | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 |
| Produto | 10 | 45 | 64 | 49 | 6 | 20 | 12 | 21 | 6 |

Soma: 233. O múltiplo de 11 seguinte é 242, e 242 − 233 = 9. O **dígito verificador é 9**.

### 20.4 Integridade dos Dados no Aplicativo

A **verificação de integridade** tira um **instantâneo** dos dados que depois confirma que eles não mudaram. Ferramentas:

- **checksum** (soma de verificação): compara valores antes e depois da transferência;
- **hash** (MD5, SHA-256): compara o hash da fonte com o do arquivo baixado;
- **controle de versão**: duas pessoas não alteram o mesmo arquivo ao mesmo tempo;
- **backups**: recuperam dados corrompidos;
- **autorização**: só certos usuários modificam os dados.

### 20.5 Outras Práticas de Segurança de Aplicativos

- **assinatura de código**: valida o autor e garante que o código não mudou;
- **cookies seguros**: o **cookie** guarda dados como o login, e quem o rouba pode se passar pelo usuário; por isso, deve trafegar **só por HTTPS**.

### 20.6 Controle de Ameaças a Aplicativos

| Ameaça | Medidas |
| --- | --- |
| Acesso físico não autorizado | Políticas para funcionários e visitantes |
| Sistema fora do ar | Planos de continuidade e de recuperação de desastres |
| Vulnerabilidade no sistema | Correções (*patches*) instaladas regularmente |
| Acesso não autorizado | MFA e monitoramento dos logs |
| Perda de dados | Classificação de dados e backup |
| Falhas no desenvolvimento | Testes antes do lançamento |

### 20.7 OWASP Top 10

A **OWASP** (*Open Web Application Security Project*) publica o **OWASP Top 10**, a lista das **dez principais preocupações de segurança web**.

## 21. Sistemas Embarcados, IoT e Tecnologias de Dissimulação

As redes ligam hoje **máquinas industriais, sensores, carros e equipamentos médicos**, que têm fragilidades próprias e ampliam a superfície de ataque.

### 21.1 Infraestruturas Críticas e SCADA

O **SCADA** (*Supervisory Control and Data Acquisition* — controle de supervisão e aquisição de dados) **controla e monitora processos industriais**. Faz parte dos **ICS** (*Industrial Control Systems* — sistemas de controle industrial).

O **Stuxnet** (2010) mirou sistemas SCADA e mostrou que um ataque digital pode **destruir infraestruturas essenciais**.

O SCADA é vulnerável porque **foi projetado sem conexão com a rede corporativa e a internet**.

A principal proteção é **separar a rede SCADA da rede da empresa e da internet**.

### 21.2 Internet das Coisas (IoT)

A **IoT** (*Internet of Things* — Internet das Coisas) **conecta objetos variados à internet**: carros, máquinas, fechaduras, câmeras e sensores. Cada um **aumenta os pontos de entrada na rede**.

Aparelhos IoT infectados já foram usados em grandes ataques **DDoS** (*Distributed Denial of Service*, muitos aparelhos atacando um alvo ao mesmo tempo).

Muitos dispositivos IoT usam um **RTOS** (*Real-Time Operating System* — sistema operacional de tempo real), vulnerável a injeção de código e negação de serviço.

O **Shodan** é um buscador que mostra dispositivos IoT expostos na internet. O **Zigbee** é um protocolo sem fio de baixo consumo, comum em casas inteligentes.

Para proteger a IoT:

- **trocar sempre as credenciais padrão**;
- atualizar o **firmware** (o software gravado no aparelho);
- proteger a rede sem fio;
- saber quais dispositivos estão na rede e o que cada um faz;
- proteger os aplicativos que os controlam.

### 21.3 Sistemas Embarcados

Os **sistemas embarcados** são **computadores dedicados a uma função dentro de outro equipamento**, como TVs e carros.

Eles sofrem **ataques de tempo**: o atacante mede **quanto tempo o sistema leva para responder** para descobrir fraquezas. É um **ataque de canal lateral**.

O **SoC** (*System on Chip*) reúne processador e periféricos em um só chip, como no **Raspberry Pi** e no **Arduino**. Pode usar um **FPGA** (*Field-Programmable Gate Array*), circuito reprogramável.

**Importante:** muitos SoCs têm **autenticação fraca e não podem ser atualizados**.

### 21.4 Voz sobre IP (VoIP)

O **VoIP** (*Voice over IP*) **usa redes de dados para fazer ligações telefônicas**. Sua segurança **depende da segurança da rede por baixo dele**.

As medidas de proteção são:

- criptografar os pacotes de voz;
- usar SSH para administrar os equipamentos;
- trocar as senhas padrão;
- usar detecção de intrusão contra o **envenenamento ARP**;
- usar autenticação forte contra o **spoofing de registro** (desvio das chamadas da vítima) e o **sequestro de chamadas**;
- usar firewalls que reconheçam o VoIP.

### 21.5 Sistemas de Finalidade Específica

| Setor | Exemplos | Riscos |
| --- | --- | --- |
| Saúde | Marca-passos e bombas de insulina conectados | Segurança do paciente e vazamento de prontuários |
| Automotivo | Sistemas que registram velocidade, localização e frenagem | Rastreamento e interferência sem fio |
| Aviação | Controle de voo | Credenciais fixas no código e *backdoors* |
| Drones (UAV, *Unmanned Aerial Vehicle*) | Uso militar, agrícola e de vigilância | Sequestro e falsificação de GPS |

Um **backdoor** (porta dos fundos) é um acesso escondido que contorna a autenticação.

### 21.6 Tecnologias de Dissimulação

As **tecnologias de dissimulação** (*deception*) acrescentam **uma camada falsa à infraestrutura** para distrair o atacante e estudar seus métodos.

| Tecnologia | O que é |
| --- | --- |
| Honeypot | Sistema-isca exposto de propósito, que registra as ações do atacante |
| Honeynet | Conjunto de honeypots que imita a rede |
| Honey files | Arquivos falsos que atraem o atacante |
| DNS sinkhole | O DNS responde com endereço falso e inofensivo para sites maliciosos conhecidos |

O objetivo do honeypot é **desviar o atacante dos recursos reais e revelar como ele age**.

## 22. Virtualização e Computação em Nuvem

Boa parte dos servidores das empresas hoje é **virtual ou fica na nuvem**.

### 22.1 Virtualização e Hypervisor

A **virtualização** permite **executar vários computadores virtuais em uma única máquina física**. Cada um é uma **máquina virtual** (**VM**, *Virtual Machine*), com o próprio sistema operacional.

O **hypervisor** é o software que permite executar vários sistemas operacionais em um sistema físico. Há dois tipos:

- **tipo 1** (*bare metal*): **roda diretamente sobre o hardware**; exemplos: VMware ESXi e Hyper-V, nos data centers;
- **tipo 2** (hospedado): **um aplicativo no sistema operacional do computador**; exemplos: VirtualBox e VMware Workstation.

**Importante:** a VM **precisa de atualizações e correções como um computador físico**. Comprometer uma VM pode levar a comprometer o host.

### 22.2 Contêineres e Desktops Virtuais

O **contêiner** leva **só o aplicativo e as dependências** e **compartilha o núcleo (*kernel*) do host**. O **Docker** distribui contêineres, e o **Kubernetes** gerencia muitos ao mesmo tempo.

A **VDI** (*Virtual Desktop Infrastructure*) guarda **o ambiente de trabalho do usuário em um servidor remoto**. Exige alta disponibilidade e muito armazenamento.

| Característica | Máquina virtual | Contêiner |
| --- | --- | --- |
| O que leva | Sistema operacional completo | Só o aplicativo e as dependências |
| Núcleo do sistema | Próprio | Compartilhado com o host |
| Peso | Maior | Menor |

### 22.3 Riscos da Virtualização

- **expansão de VMs** (*VM sprawl*): acúmulo de **VMs esquecidas**, sem atualização;
- **fuga de VM** (*VM escape*): a VM **rompe o isolamento e alcança o host**.

### 22.4 Modelos de Serviço em Nuvem

A **computação em nuvem** oferece **computação, armazenamento, software e servidores pela internet**. Os modelos de serviço são:

- **SaaS** (*Software as a Service*): aplicativos prontos, usados pelo navegador, como Gmail e Microsoft 365;
- **PaaS** (*Platform as a Service*): ferramentas para **desenvolver e publicar aplicativos**;
- **IaaS** (*Infrastructure as a Service*): **recursos de computação virtualizados**, como VMs e discos alugados.

### 22.5 Modelos de Implantação

| Modelo | Quem usa | Característica principal |
| --- | --- | --- |
| Privada | Uma organização | Mais controle, mais cara |
| Pública | Clientes de um provedor | Mais barata, menos controle |
| Híbrida | Combina privada e pública | Controle dos dados com a flexibilidade da pública |
| Comunitária | Empresas do mesmo setor | Plataforma compartilhada |

### 22.6 Computação em Neblina e de Borda

Quando milissegundos importam (carros autônomos, manufatura), o processamento fica perto dos dados:

- **neblina** (*fog*): processamento em um equipamento intermediário da rede local, o **fog node**;
- **borda** (*edge*): **no próprio dispositivo ou sensor**.

## 23. Segurança na Nuvem

A nuvem sofre as mesmas ameaças das redes físicas e tem ameaças próprias. Com um recurso de nuvem comprometido, o atacante pode:

- usar a capacidade da nuvem para atacar outras organizações;
- hospedar malware em um provedor respeitado;
- lançar DDoS, enviar spam e fazer phishing.

### 23.1 Principais Ameaças

As principais ameaças são:

- **vazamento de dados**;
- **configuração incorreta** dos recursos;
- arquitetura de segurança mal planejada;
- **credenciais comprometidas**: quem sequestra a **conta de serviço** controla todos os recursos;
- ameaça interna;
- **interfaces e APIs inseguras**, os pontos mais expostos;
- visibilidade limitada do uso da nuvem.

### 23.2 Responsabilidade Compartilhada

Na nuvem pública, a segurança é **dividida entre o cliente e o provedor** (**CSP**, *Cloud Service Provider*). Quanto mais pronto o serviço, mais responsabilidade fica com o provedor.

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

### 23.3 Domínios da Segurança em Nuvem (CSA)

A **CSA** (*Cloud Security Alliance*) organiza as boas práticas de segurança em nuvem em **14 domínios**, entre eles governança e riscos, conformidade, segurança de infraestrutura, virtualização e contêineres, resposta a incidentes, criptografia de dados e **IAM** (identidade e acesso).

Para a CSA, a **criptografia é um dos controles mais importantes** dos dados.

### 23.4 Segurança da Infraestrutura em Nuvem

Na nuvem, não é possível instalar um equipamento de segurança no cabo. Usam-se **equipamentos virtuais e agentes de software**.

A **SDN** (*Software-Defined Networking* — rede definida por software) **cria e separa redes por software**. Seus firewalls se chamam **grupos de segurança**.

As proteções mais usadas são:

- segurança integrada à plataforma, como proteção contra DDoS;
- **VPC** (*Virtual Private Cloud* — nuvem privada virtual): sub-redes privadas **isoladas logicamente da internet**;
- firewalls virtuais;
- **logs de fluxo**, que monitoram o tráfego;
- VPNs para acesso remoto e entre nuvens;
- **IAM** (*Identity and Access Management*): gerencia credenciais, autenticação e autorização.

A **microssegmentação** cria **muitas redes menores e isoladas** por software.

A **TI invisível** (*shadow IT*) são **aplicativos usados sem autorização**. A resposta são políticas claras e conscientização.

### 23.5 Proteção dos Dados na Nuvem

Os dados precisam de proteção nos três estados. Os controles mais importantes são:

- **criptografia** para a confidencialidade (AES, RSA, DH, ECC);
- **hash** para a integridade (família SHA-2).

### 23.6 Proteção das Máquinas Virtuais

As medidas principais para as VMs (instâncias) são:

- planejar a sub-rede de cada instância;
- desativar portas e serviços desnecessários;
- desativar as contas padrão;
- manter o antimalware atualizado;
- instalar firewall de host, **IDS** (*Intrusion Detection System*, que alerta) e **IPS** (*Intrusion Prevention System*, que também bloqueia).

**Observação:** instâncias esquecidas ficam vulneráveis e **consomem serviços pagos**. Os recursos precisam ser registrados, monitorados e auditados.

## 24. IDS, IPS e Tipos de Dados de Segurança

Muitos ataques só são percebidos durante ou depois. Por isso, a rede precisa ser **monitorada**. Muitos desses dados são reunidos pelo **Security Onion**, um conjunto gratuito de ferramentas de **NSM** (*Network Security Monitoring* — monitoramento de segurança de rede).

### 24.1 IDS e IPS

Um **IDS** (*Intrusion Detection System* — sistema de detecção de intrusão) **analisa o tráfego e gera um alerta**. Fica **fora do caminho**, com uma cópia do tráfego: não atrasa a rede, mas não impede o ataque.

Um **IPS** (*Intrusion Prevention System* — sistema de prevenção de intrusão) fica **no caminho** dos pacotes e **pode bloquear** o ataque. Em troca, acrescenta atraso.

| Característica | IDS | IPS |
| --- | --- | --- |
| Posição | Fora do caminho (cópia do tráfego) | No caminho (em linha) |
| Ação | Alerta | Alerta e bloqueia |
| Efeito na rede | Nenhum | Atraso; uma falha afeta o tráfego |

Formas de detecção:

- **por assinatura**: compara com regras de ataques conhecidos; precisa, mas não reconhece ataques novos;
- **por anomalia**: compara com o comportamento normal (linha de base); percebe ataques novos, mas gera mais alarmes falsos.

Conforme o lugar:

- **de rede** (**NIDS**/**NIPS**): analisam o tráfego de um segmento inteiro; exemplos: Snort, Suricata e Zeek;
- **de host** (**HIDS**/**HIPS**): instalados no próprio computador; exemplos: OSSEC e Wazuh.

### 24.2 Dados de Alerta

Os **dados de alerta** são **mensagens geradas por um IDS ou IPS quando o tráfego viola uma regra**.

Exemplo: uma regra do **Snort** alerta quando chega de fora o texto **uid=0 (root)**, resposta típica de um acesso de administrador no Linux.

### 24.3 Dados de Sessão

Os **dados de sessão** são o **registro de uma conversa entre dois endpoints**: quem falou com quem, quanto e por quanto tempo, **sem o conteúdo**.

Cada sessão é identificada pela **5-tupla**: IP de origem, IP de destino, porta de origem, porta de destino e protocolo. O **Zeek** registra esses dados no log de conexões.

### 24.4 Dados de Transação

Os **dados de transação** são **as mensagens trocadas durante a sessão**. Exemplo: o pedido "GET /index.html" e a resposta "200 OK".

**Importante:** a **sessão é todo o tráfego** da conversa; a **transação é o pedido** e sua resposta.

### 24.5 Analisadores de Pacotes

Um **analisador de pacotes** (*sniffer*) **intercepta e registra o tráfego da rede**. Exemplos: **Wireshark** (gráfico) e **tcpdump** (linha de comando).

Usos:

- analisar problemas de rede;
- detectar uso indevido e tentativas de invasão;
- isolar um sistema explorado.

**Importante:** com um sniffer, o atacante lê tudo o que trafega sem criptografia, inclusive senhas.

### 24.6 Capturas Completas de Pacotes

As **capturas completas de pacotes** guardam **o conteúdo real** do que trafegou: e-mails, páginas e arquivos. São as mais detalhadas e **as que mais exigem armazenamento**.

### 24.7 Dados Estatísticos

Os **dados estatísticos** são **criados a partir da análise dos outros dados**. A técnica principal é a **linha de base**:

Comportamento normal → Comparação com o atual → Diferença significativa → Alarme

A **NBA** (*Network Behavior Analysis* — análise de comportamento de rede) usa essa ideia com dados **NetFlow** ou **IPFIX**.

| Tipo de dado | O que registra | Nível de detalhe |
| --- | --- | --- |
| Alerta | Violação de uma regra | Resumido |
| Sessão | Quem conversou com quem | Sem conteúdo |
| Transação | Pedidos e respostas | Parte do conteúdo |
| Captura completa | Todo o conteúdo | Máximo |
| Estatístico | Comportamento calculado | Derivado |

## 25. Fontes de Dados do Monitoramento: Logs e Fluxos

Este módulo reúne **as fontes de dados do monitoramento**: os logs dos hosts e dos servidores, o syslog e os registros de fluxos da rede.

### 25.1 Arquivos de Log

Um **log** é o **registro dos eventos que ocorrem em um sistema**. Cada evento vira uma **entrada de log**.

Pelos logs, descobre-se **como um ataque aconteceu e se as defesas funcionaram**. O **gerenciamento de logs** tem as etapas:

Gerar → Transmitir → Armazenar → Analisar → Descartar

| Fonte | O que registra |
| --- | --- |
| Sistema operacional | Logins, pedidos e uso do sistema |
| Software de segurança | Atividades maliciosas detectadas |

### 25.2 Logs dos Hosts

Um **HIDS** (*Host-based Intrusion Detection System*) é instalado no próprio computador. Seus logs devem ir para **servidores centrais de gerenciamento de logs**. Exemplos: **OSSEC** e **Tripwire**.

No Windows, o **Visualizador de Eventos** mostra cinco logs:

- **aplicativos**: eventos dos programas;
- **sistema**: drivers, processos e hardware;
- **instalação**: instalação de software e atualizações;
- **segurança**: tentativas de logon e acesso a arquivos; só **sucesso ou falha de auditoria**;
- **linha de comando**: comandos executados, muito usados por atacantes.

O log de segurança é gerado pelo **LSASS** (lsass.exe), que deve rodar da pasta **System32**.

**Importante:** um lsass.exe em **outra pasta**, ou disfarçado como **1sass.exe**, **pode ser malware**.

| Tipo de evento | Significado | Exemplo |
| --- | --- | --- |
| Erro | Problema significativo | Um serviço não inicia |
| Aviso | Pode indicar problema futuro | Pouco espaço em disco |
| Informações | Operação bem-sucedida | Driver carregado |
| Sucesso na auditoria | Acesso auditado que deu certo | Logon realizado |
| Falha na auditoria | Acesso auditado que falhou | Acesso negado |

### 25.3 Formato do Syslog

O **syslog** é o padrão para **enviar mensagens de eventos dos equipamentos a um servidor central**. Usa a **porta UDP 514** e, sem TLS, trafega **em texto claro**.

Toda mensagem tem três partes:

PRI (prioridade) → HEADER (data, hora e equipamento) → MSG (texto)

A **PRI** combina:

- **facilidade**: a categoria da fonte (local0 a local7 = 16 a 23);
- **gravidade**: de 0 a 7, e **quanto menor o número, mais grave o evento**.

| Gravidade | Nome | Significado |
| --- | --- | --- |
| 0 | Emergência | Sistema inutilizável |
| 1 | Alerta | Ação imediata necessária |
| 2 | Crítico | Condição crítica |
| 3 | Erro | Falha não urgente |
| 4 | Aviso | Haverá erro se nada for feito |
| 5 | Notificação | Evento normal, mas significativo |
| 6 | Informativo | Operação normal |
| 7 | Depuração | Mensagens para desenvolvedores |

**Prioridade = Facilidade × 8 + Gravidade**

**Observação:** um asterisco (\*) antes da data indica **problema com o NTP**.

A **MSG** é **a parte mais útil para o analista**.

#### 25.3.1 Exemplo Resolvido: Cálculo da Prioridade do Syslog

Facilidade local4 e gravidade 3 (erro):

| Etapa | Cálculo | Resultado |
| --- | --- | --- |
| Número da local4 | 16 + 4 | 20 |
| Facilidade × 8 | 20 × 8 | 160 |
| Mais a gravidade | 160 + 3 | 163 |
| Início da mensagem | — | <163> |

Exemplo de mensagem Cisco: `%SYS-5-CONFIG_I: Configured from console by con0`

| Trecho | Significado |
| --- | --- |
| SYS | Facilidade |
| 5 | Gravidade (notificação) |
| CONFIG\_I | Mnemônico da mensagem |
| Configured from console by con0 | A configuração foi alterada pelo console |

### 25.4 Proteção do Syslog e da Hora (NTP)

O servidor syslog é alvo dos atacantes. Para esconder a **retirada de dados** (exfiltração), o atacante **adultera ou destrói os logs**. O **syslog-ng** traz melhorias contra isso.

O **NTP** (porta UDP 123) mantém os relógios iguais. Só com a hora certa é possível **juntar os rastros de um mesmo ataque registrados em equipamentos diferentes**.

### 25.5 Logs dos Servidores

Os servidores mantêm **logs de acesso e de erro**. Os **logs de proxy DNS** mostram visitas a sites perigosos e conexões com comando e controle.

Exemplo de log do **Apache**: `203.0.113.127 – dsmith [10/Oct/2016:10:26:57 -0500] "GET /logo_sm.gif HTTP/1.0" 200 2254` (IP do cliente, usuário, data, pedido, código 200 e tamanho).

### 25.6 Logs da Rede

As principais fontes da rede são:

- **tcpdump** e **Wireshark**: capturas de pacotes;
- **NetFlow**: registra **os fluxos de tráfego, sem o conteúdo**; o **IPFIX** é a versão padronizada;
- **AVC** (*Application Visibility and Control*): reconhece e controla mais de mil aplicativos;
- **filtros de conteúdo** de e-mail e de web;
- **proxies web**, que registram todos os pedidos;
- **NGFW**, que registra conexões e intrusões.

Um **fluxo** é o conjunto de pacotes de uma conversa, em um sentido, com os mesmos atributos (IPs, portas e protocolo).

O NetFlow monta a **linha do tempo de um ataque** e mostra o movimento do atacante de host em host.

**Observação:** monitorar só pela porta dá pouca informação; o reconhecimento pelo aplicativo mostra **o que o usuário está realmente fazendo**.

#### 25.6.1 Proxies Web e DNS

O **servidor proxy** busca o recurso em nome do cliente. Seus logs são uma **fonte primária** e mostram:

- quais hosts fazem os pedidos e se os destinos são maliciosos;
- que tipo de recurso foi baixado.

O proxy também inspeciona o tráfego de saída para **DLP** (*Data Loss Prevention*), conferindo se saem dados confidenciais.

Exemplo de log do proxy **Squid**: hora, duração, IP do cliente, código de resultado (como TCP\_MISS/200), bytes, método (GET), endereço do recurso e tipo de conteúdo.

Os **proxies abertos** servem para esconder o IP dos atacantes.

O **Cisco Umbrella** é um **DNS hospedado com listas negras e proteção contra phishing**. Seus logs mostram hora, IPs, ação (permitido ou bloqueado), domínio e categoria do destino.

#### 25.6.2 Firewalls de Última Geração

Os **NGFW** monitoram até a camada de aplicação e têm painéis próprios. Eventos registrados:

| Evento | O que registra |
| --- | --- |
| Conexão | Sessões detectadas, com IPs e a regra aplicada |
| Intrusão | Atividades maliciosas nos pacotes |
| Host ou endpoint | Hosts detectados na rede |
| Descoberta de rede | Mudanças na rede |
| Fluxo de rede | Eventos gerados a partir do NetFlow |

## 26. Tecnologias que Dificultam o Monitoramento

O **monitoramento de segurança** observa o tráfego e os registros para **identificar ataques e comportamentos suspeitos**. Vários protocolos comuns podem ser mal usados para escapar dele.

### 26.1 DNS

Muitas organizações protegem pouco o DNS. Os atacantes o usam para **esconder outros protocolos dentro do DNS**, falar com o servidor de **comando e controle** (**C&C**, o computador que dá ordens ao malware) e retirar dados disfarçados de consultas.

Na retirada de dados pelo DNS:

1. o malware codifica os dados (em **Base64** ou hexadecimal) para escapar do **DLP** (*Data Loss Prevention*);
2. coloca os dados no **subdomínio** de uma consulta, como "dados-codificados.example.com";
3. o servidor DNS do atacante grava o subdomínio e reúne os dados.

O sinal mais claro são **subdomínios muito mais longos que o normal** ou aleatórios. Os **logs de proxy DNS** revelam essas consultas.

### 26.2 HTTP e HTTPS

O **HTTP** trafega **em texto claro**.

Na **injeção de iFrame**, o atacante invade um site e planta um **quadro invisível** que baixa malware no navegador de quem visita.

O **HTTPS** protege a navegação, mas **dificulta a inspeção** do tráfego: decifrá-lo exige processamento e levanta questões de privacidade.

### 26.3 E-mail e ICMP

- **SMTP** (envio): já foi usado por malware para retirar dados;
- **POP3 e IMAP** (recebimento): **trazem o malware até o computador**; a **análise retrospectiva** acompanha o malware a partir do primeiro host infectado.

No **tunelamento ICMP**, o malware **transfere dados escondidos em pacotes que parecem pings**. Exemplo: a exploração **LOKI**.

### 26.4 ACLs, NAT e PAT

As ACLs podem dar uma **falsa sensação de segurança**:

- o atacante descobre o que a ACL permite por varredura de portas;
- falsifica o IP de origem;
- manipula sinalizadores como o established;
- uma ACL que deixa voltar ICMP também deixa passar um túnel ICMP.

O **NAT** (*Network Address Translation*) e o **PAT** (*Port Address Translation*) fazem vários endereços internos saírem com um endereço público. Isso **dificulta saber qual dispositivo interno fez cada pedido** e **quebra os fluxos** do NetFlow.

### 26.5 Criptografia e Tunelamento

A **VPN** cria um túnel cifrado. O malware usa a mesma técnica: um túnel cifrado em protocolo confiável para retirar dados.

O tráfego TLS esconde malware. As medidas são:

- **posicionar o IPS onde ele veja o tráfego já decifrado**;
- validar os certificados (CRL ou OCSP);
- filtrar URLs e usar antimalware no conteúdo HTTPS;
- usar equipamentos que decifram o tráfego e o enviam ao IPS.

### 26.6 P2P e Tor

Nas redes **P2P** (*peer-to-peer*), **cada computador é ao mesmo tempo cliente e servidor**. Tipos:

- compartilhamento de arquivos (BitTorrent);
- compartilhamento de processadores;
- mensagens instantâneas.

**Importante:** o **P2P de arquivos não deve ser permitido em redes corporativas**: contorna o firewall e espalha malware.

O **Tor** permite **navegar de forma anônima**. Cada retransmissor só conhece o **próximo salto** (*onion routing*). Muito usado por criminosos, o tráfego **escapa das listas negras**.

### 26.7 Balanceamento de Carga

O **balanceamento de carga** distribui o tráfego entre vários servidores. Por isso, **uma única transação pode aparecer com vários IPs** nas capturas.

| Protocolo ou tecnologia | Mau uso ou dificuldade |
| --- | --- |
| Syslog e NTP | Logs apagados e hora corrompida |
| DNS | Retirada de dados e comando e controle |
| HTTP | Injeção de iFrame |
| HTTPS e VPN | Tráfego cifrado não inspecionado |
| E-mail | Retirada de dados e entrada de malware |
| ICMP | Reconhecimento e tunelamento |
| ACLs | Falsa sensação de segurança |
| NAT e PAT | Dispositivo interno escondido |
| P2P e Tor | Contorno do firewall e anonimato |
| Balanceamento de carga | Vários IPs para a mesma transação |

## 27. SIEM, SOAR e Avaliação de Alertas

Com tantas fontes de dados, o analista precisa de ferramentas que **reúnam tudo em um só lugar** e o ajudem a decidir o que é real.

### 27.1 SIEM

O **SIEM** (*Security Information and Event Management* — gerenciamento de informações e eventos de segurança) **coleta os logs de toda a rede** e oferece relatórios em tempo real e análises de longo prazo.

| Função | O que faz |
| --- | --- |
| Coleta | Reúne os logs da organização |
| Normalização | Converte formatos diferentes para um modelo comum |
| Correlação | Liga eventos de sistemas diferentes e acelera a detecção |
| Agregação | Junta eventos repetidos e reduz o volume |
| Relatórios | Painéis em tempo real e resumos |
| Conformidade | Relatórios exigidos pelas normas |

Exemplos: **Splunk**, muito usado nos **SOCs** (*Security Operations Centers*, centros de operações de segurança), e **ELK** (Elasticsearch, Logstash e Kibana).

### 27.2 SOAR

O **SOAR** (*Security Orchestration, Automation and Response*) **automatiza as etapas da resposta a incidentes** e integra ferramentas de vários fabricantes.

SIEM → reúne e correlaciona os eventos; SOAR → responde a eles de forma automatizada.

### 27.3 Security Onion

O **Security Onion** é um pacote **gratuito de ferramentas de monitoramento de segurança** que roda em Ubuntu Linux.

Dados → Detecção → Análise

| Ferramenta | Tipo | Função |
| --- | --- | --- |
| Snort | IDS de rede | Detecta ataques por regras e assinaturas |
| Suricata | IDS de rede | Usa assinaturas e pode bloquear em linha |
| Zeek | IDS de rede | Analisa o comportamento com políticas em scripts |
| OSSEC / Wazuh | HIDS | Integridade de arquivos, logs e rootkits do host |

Na análise, o **Sguil** é o **ponto de partida da investigação**. Dele, o analista "gira" (*pivot*) para:

- **Kibana**: painel para consultar os dados;
- **Wireshark**: abre as capturas de pacotes;
- **Zeek**: análise aprofundada do tráfego.

### 27.4 Alertas no Sguil

Os **alertas** são **mensagens geradas pelas ferramentas de monitoramento** a partir de regras, assinaturas ou anomalias. O Sguil os reúne em uma **fila**, onde o analista investiga, classifica, escala ou retira cada alerta.

Todo alerta traz, quando disponível, a **5-tupla**, o horário e o equipamento que o gerou.

| Campo do Sguil | Significado |
| --- | --- |
| ST | Status; a cor indica a prioridade |
| CNT | Quantas vezes o evento foi detectado para os mesmos IPs |
| Sensor | Agente que relatou o evento |
| Alert ID | Sensor e número do evento |
| Date/Time | Horário do evento |
| Event Message | Texto da regra que gerou o alerta |

### 27.5 Regras do Snort

Uma regra do Snort tem **cabeçalho** (ação, protocolo, origem, destino e direção) e **opções** (entre parênteses):

`alert tcp $EXTERNAL_NET any -> $HOME_NET 21 (msg:"ET EXPLOIT VSFTPD backdoor user login smiley"; content:"USER"; sid:2013188; rev:4;)`

| Trecho | Significado |
| --- | --- |
| alert | Ação: gerar um alerta |
| tcp | Protocolo |
| `$EXTERNAL_NET any -> $HOME_NET 21` | De qualquer endereço externo para a porta 21 da rede interna |
| msg | Texto do alerta |
| content | Conteúdo procurado no pacote |
| sid | Identificação única da regra |
| rev | Número da revisão |

As regras vêm de três fontes: **GPL** (antigas), **ET** (*Emerging Threats*, código aberto) e **VRT** (mantidas pelo **Cisco Talos**).

### 27.6 Classificação dos Alertas

As regras são **propositalmente conservadoras**: é melhor alertar à toa do que deixar passar um ataque.

|  | Verdadeiro | Falso |
| --- | --- | --- |
| Positivo (houve alerta) | Ocorreu um incidente | Não ocorreu incidente |
| Negativo (não houve alerta) | Não ocorreu incidente | Ocorreu um incidente |

- **verdadeiro positivo**: a regra funcionou;
- **falso positivo**: alerta por atividade inofensiva; custa tempo do analista;
- **verdadeiro negativo**: tráfego normal, sem alerta;
- **falso negativo**: **um ataque aconteceu e nenhum alerta foi gerado**; é o caso **mais perigoso**.

O que fazer:

- verdadeiro positivo → **encaminhar para o nível superior**;
- excesso de falsos positivos → **ajustar as regras**;
- falso negativo descoberto depois → **RSA** (*Retrospective Security Analysis* — análise retrospectiva): **aplicar regras novas aos dados guardados**.

### 27.7 Análise Determinística e Probabilística

- **determinística**: **todas as etapas anteriores precisam ter dado certo** para o ataque funcionar; usa informações conhecidas e descreve o pior caso;
- **probabilística**: **usa estatística para estimar a probabilidade** de a próxima etapa dar certo; útil com portas dinâmicas e muitas variáveis.

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

### A. Cálculo de Disponibilidade (ver item 19.2)

Considere um ano de 365 dias.

1. Calcule o tempo máximo de inatividade por ano, em minutos, de um sistema com 99,9% de disponibilidade.
2. Calcule o tempo máximo de inatividade por ano de um sistema com 99,99% de disponibilidade.
3. Calcule o tempo máximo de inatividade por ano de um sistema com 99,95% de disponibilidade e converta o resultado em horas e minutos.
4. Um servidor ficou fora do ar por 30 minutos em um ano. Calcule sua disponibilidade e informe se ele atingiu os cinco noves.

### B. Dígito Verificador do ISBN-10 (ver item 20.3)

1. Calcule o dígito verificador do ISBN-10 cujos nove primeiros dígitos são 0 3 0 6 4 0 6 1 5.
2. Calcule o dígito verificador do ISBN-10 cujos nove primeiros dígitos são 8 5 7 5 2 2 0 0 3.
3. Um usuário digitou o ISBN 0-306-40615-7. Indique se a validação aceita ou rejeita esse número e por quê.

### C. Máscaras Curinga (ver item 16.5)

1. Informe a máscara curinga para a rede 192.168.50.0/24.
2. Informe a máscara curinga para a rede 172.16.8.64/26 e o comando `permit` correspondente.
3. Informe a máscara curinga que reúne as redes 10.1.4.0/24 a 10.1.7.0/24 em uma única entrada.
4. Indique o primeiro e o último endereço que correspondem a `192.168.5.16 0.0.0.15`, mostrando o último octeto em binário.
5. Indique a faixa de endereços que corresponde a `172.16.32.0 0.0.7.255`.
6. Escreva a entrada que permite apenas o host 192.168.1.20 de duas formas: com máscara curinga e com a palavra-chave correspondente.

### D. Prioridade do Syslog (ver item 25.3)

1. Calcule a prioridade de uma mensagem com facilidade local7 e gravidade 6.
2. Calcule a prioridade de uma mensagem com facilidade local0 e gravidade 4.
3. Uma mensagem começa com <165>. Informe o número da facilidade, o nome da facilidade local e o nome da gravidade.
4. Uma mensagem começa com <11>. Informe o número da facilidade e o nome da gravidade.
5. Na mensagem `%SYS-5-CONFIG_I: Configured from console by con0`, indique a facilidade Cisco, a gravidade e o código da mensagem.

### E. Posicionamento de ACLs e Firewalls (ver itens 16.13, 17.5 e 17.12)

1. Indique onde aplicar uma ACL padrão que impede a rede 192.168.10.0/24 de acessar a rede 192.168.30.0/24 e justifique.
2. Indique onde aplicar uma ACL estendida que impede a rede 192.168.11.0/24 de usar Telnet com a rede 192.168.30.0/24 e justifique.
3. Classifique cada tráfego, em um firewall com DMZ, como bloqueado, permitido seletivamente ou permitido com inspeção: a) da rede pública para a privada; b) da rede pública para o servidor web da DMZ; c) da rede privada para a internet; d) da DMZ para a rede privada.
4. Em um roteador com ZPF, a interface G0/0 está na zona PRIVATE e a interface G0/1 não pertence a nenhuma zona. Indique o que acontece com o tráfego entre elas.

### F. Classificação de Alertas (ver item 27.6)

Classifique cada situação como verdadeiro positivo, falso positivo, verdadeiro negativo ou falso negativo.

1. O IDS gerou um alerta de exploração do FTP, e a investigação confirmou que um atacante entrou no servidor.
2. O IDS gerou um alerta porque um administrador fez uma varredura autorizada na rede.
3. Um malware retirou dados por DNS durante meses sem que nenhum alerta fosse gerado.
4. Um usuário navegou normalmente na web, e nenhum alerta foi gerado.
5. Indique qual dos quatro casos é o mais perigoso e por quê.

### G. Questões Conceituais: Fundamentos e Criptografia (ver seções 1 a 8)

1. Explique a diferença entre confidencialidade, integridade e disponibilidade, com um exemplo de cada.
2. Diferencie a analogia da cebola da analogia da alcachofra na defesa em profundidade.
3. Indique por que a criptografia simétrica é usada para grandes volumes de dados e a assimétrica para trocar chaves.
4. Explique por que o hash sozinho não protege contra o ataque man-in-the-middle e qual recurso resolve esse problema.
5. Informe o que é criptografado em uma assinatura digital e se ela, sozinha, garante confidencialidade.
6. Diferencie mascaramento de dados de esteganografia.

### H. Questões Conceituais: Controle de Acesso (ver seções 9 a 12)

1. Cite os três fatores de autenticação e dê um exemplo de cada.
2. Diferencie os modelos DAC, MAC e RBAC.
3. Explique o princípio da confiança zero.
4. Compare o TACACS+ e o RADIUS quanto ao transporte e à criptografia.

### I. Questões Conceituais: Proteção de Sistemas e da Rede (ver seções 13 a 15 e 18 a 21)

1. Explique a função da CER na escolha de um sistema biométrico.
2. Indique por que o Telnet deve ser substituído pelo SSH.
3. Explique a função da DMZ.
4. Indique por que o WEP e o WPS não devem ser usados.
5. Explique por que o RAID 0 não protege contra a falha de um disco.
6. Explique por que os sistemas SCADA são vulneráveis e qual é a principal medida de proteção.
7. Indique a finalidade de um honeypot.

### J. Questões Conceituais: Filtragem de Tráfego (ver seções 16 e 17)

1. Diferencie a ACL padrão da ACL estendida.
2. Explique a negação implícita e sua consequência para uma ACL que só tem instruções deny.
3. Explique o efeito da palavra-chave established.
4. Indique os cuidados com o deny ipv6 any any explícito em uma ACL IPv6.
5. Diferencie o firewall de filtragem de pacotes do firewall com estado.
6. Diferencie as ações Inspect, Pass e Drop do ZPF.

### K. Questões Conceituais: Nuvem (ver seções 22 e 23)

1. Diferencie o hypervisor tipo 1 do tipo 2.
2. Diferencie a máquina virtual do contêiner.
3. Diferencie SaaS, PaaS e IaaS.
4. Indique qual responsabilidade é sempre do cliente no modelo de responsabilidade compartilhada.
5. Explique a expansão de VMs e a fuga de VM.

### L. Questões Conceituais: Monitoramento (ver seções 24 a 27)

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
