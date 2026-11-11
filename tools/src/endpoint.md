# Segurança de Endpoint

Nov 6, 2026 · @Maria Paula

## 1. Princípios da Segurança Cibernética

A **segurança cibernética** é o conjunto de medidas que **protege dados, sistemas e redes contra acesso, alteração ou interrupção indevidos**.

### 1.1 O Cubo da Segurança Cibernética

O **cubo da segurança cibernética** resume a proteção de dados em **três dimensões**:

| Dimensão | O que define | Elementos |
| --- | --- | --- |
| Primeira | Os objetivos da proteção | Confidencialidade, integridade e disponibilidade |
| Segunda | Os estados dos dados | Em trânsito, em repouso e em processamento |
| Terceira | Os pilares da defesa | Tecnologia; políticas e práticas; pessoas |

Os três objetivos formam a **tríade CIA** (*Confidentiality, Integrity, Availability*):

- **confidencialidade**: **impede a divulgação de informações** a quem não está autorizado;
- **integridade**: garante a **precisão, a consistência e a confiabilidade** dos dados;
- **disponibilidade**: informações **acessíveis aos autorizados quando necessário**.

### 1.2 Confidencialidade

As informações confidenciais são **pessoais**, **comerciais** ou **classificadas** (sigilosas, de governo). A proteção mais comum é a **criptografia**. Outras técnicas:

- **tokenização**: troca o dado por um **valor aleatório sem relação matemática** com ele, o *token*; útil no pagamento com cartão;
- **DRM** (*Digital Rights Management*): protege materiais com direitos autorais, como músicas e filmes;
- **IRM** (*Information Rights Management*): protege e-mails e documentos da empresa mesmo depois de compartilhados.

Para a **privacidade**, usam-se também a **minimização de dados** (guardar só o necessário) e a **anonimização**, que transforma de forma **irreversível** dados pessoais em informação anônima.

### 1.3 Integridade

A **integridade** é a precisão e a confiabilidade dos dados **durante todo o seu ciclo de vida**.

Métodos que a garantem:

- **hash**;
- validação dos dados;
- verificações de consistência;
- controles de acesso.

| Necessidade | Exemplo | Tratamento dos dados |
| --- | --- | --- |
| Crítica | Saúde (receitas médicas) | Verificados continuamente |
| Alta | Comércio eletrônico | Verificados com frequência |
| Média | Buscadores | Pouca verificação |
| Baixa | Blogs e redes sociais | Podem não ser verificados |

### 1.4 Disponibilidade

A **disponibilidade** é ameaçada por **falhas de equipamento, desastres naturais, ataques e negação de serviço** (**DoS**, *Denial of Service*, que impede usuários legítimos de usar um sistema).

As principais medidas são:

- manutenção de equipamentos;
- atualizações e correções (*patches*);
- **teste de backup**;
- planejamento contra desastres;
- monitoramento de atividades (logs e alertas);
- testes de disponibilidade (varreduras e testes de penetração).

**Observação:** manutenção e backups não são ameaças; protegem a disponibilidade.

### 1.5 Dados em Repouso

Os **dados em repouso** são os **dados armazenados**, que ninguém está acessando.

| Armazenamento | Como funciona |
| --- | --- |
| DAS (*Direct-Attached Storage*) | Ligado diretamente ao computador, como um disco ou pen drive |
| RAID (*Redundant Array of Independent Disks*) | Vários discos vistos como um só |
| NAS (*Network-Attached Storage*) | Dispositivo na rede que centraliza os dados |
| SAN (*Storage Area Network*) | Rede de armazenamento de alta velocidade ligando servidores a discos centrais |
| Nuvem | Espaço remoto em um provedor, como Google Drive |

**Importante:** o **armazenamento local é o mais difícil de controlar**. Os sistemas em rede são mais seguros, mas, por concentrarem dados, uma falha representa um risco maior.

### 1.6 Dados em Trânsito

Os **dados em trânsito** estão **sendo transmitidos** de um dispositivo para outro, por três meios:

- **rede de tênis** (*sneaker net*): mídia removível levada fisicamente;
- **redes com fio**: LAN (*Local Area Network*) e WAN (*Wide Area Network*);
- **redes sem fio**: aumentam a **superfície de ataque**.

| Objetivo | Ameaça | Proteção |
| --- | --- | --- |
| Confidencialidade | Captura dos dados | Criptografia (VPN, TLS, IPsec) |
| Integridade | Alteração dos dados | Hash e redundância |
| Disponibilidade | Dispositivos falsos ou conexões sequestradas | **Autenticação mútua** |

Uma **VPN** (*Virtual Private Network* — rede privada virtual) cria um túnel criptografado pela internet.

### 1.7 Dados em Processamento

Os **dados em processamento** estão em **entrada, modificação, cálculo ou saída**:

- **entrada**: digitação, digitalização ou sensores; erros vêm de digitação ou formatos incompatíveis;
- **modificação**: alteração pelos usuários ou programas; quando os dados ficam ilegíveis, há **corrupção de dados**;
- **saída**: impressoras, monitores; erros vêm de configurações incorretas.

| Estado | Exemplo | Principal desafio |
| --- | --- | --- |
| Em repouso | Arquivo no servidor | Armazenamento local e concentração de dados |
| Em trânsito | E-mail pela internet | Captura e alteração |
| Em processamento | Planilha sendo editada | Erros de entrada e corrupção |

## 2. O Cenário de Ameaças

As redes são atacadas o tempo todo. Empresas de segurança publicam **mapas de ameaças** que mostram os ataques em tempo real.

### 2.1 Por que Proteger a Rede

A segurança da rede está ligada à **continuidade dos negócios**. Uma violação causa perda de dados, de receita e de propriedade intelectual, além de processos judiciais.

Fontes de informação sobre ameaças:

- **Cisco Talos**: inteligência de ameaças;
- **Cisco PSIRT** (*Product Security Incident Response Team*): avisos sobre vulnerabilidades dos produtos Cisco.

### 2.2 Ameaça, Vulnerabilidade e Risco

| Termo | Significado |
| --- | --- |
| Ativo | Tudo o que tem valor para a organização |
| Ameaça | **Perigo potencial** para um ativo |
| Vulnerabilidade | **Fraqueza** que pode ser explorada |
| Superfície de ataque | **Soma das vulnerabilidades acessíveis** ao atacante |
| Exploração (*exploit*) | **Mecanismo que aproveita uma vulnerabilidade** |
| Risco | **Probabilidade** de uma ameaça explorar uma vulnerabilidade e causar dano |
| Contramedida | Ação que reduz a ameaça ou o risco |
| Impacto | Dano potencial causado pela ameaça |

As explorações podem ser:

- **remotas**: funcionam pela rede, **sem acesso prévio** ao sistema;
- **locais**: o atacante já tem algum acesso ao sistema, o que **não significa acesso físico**.

### 2.3 Gerenciamento de Riscos

Há **quatro formas** de lidar com um risco:

| Estratégia | Como funciona |
| --- | --- |
| Aceitação | O custo de tratar supera o do risco; nada é feito |
| Prevenção (evitar) | **Elimina a atividade** que gera o risco |
| Redução (mitigação) | Diminui a exposição ou o impacto; é a **mais usada** |
| Transferência | Passa o risco **a um terceiro**, como uma seguradora |

### 2.4 Ameaças Internas e Externas

Um **vetor de ataque** é o **caminho pelo qual o atacante chega** ao alvo.

As **ameaças externas** vêm de atacantes de fora, que exploram vulnerabilidades ou usam **engenharia social** (manipulação de pessoas).

As **ameaças internas** vêm de funcionários, terceirizados e parceiros. Um usuário interno pode:

- copiar dados para pen drive ou e-mail;
- desconectar uma ligação crítica;
- conectar um pen drive infectado;
- acessar sites maliciosos.

**Importante:** as ameaças internas podem causar **danos maiores**, porque o usuário interno tem **acesso direto** e **conhece a rede**.

### 2.5 Perda de Dados

Os dados costumam ser **o ativo mais valioso** da organização. A **perda de dados**, ou **exfiltração**, ocorre quando os dados são perdidos, roubados ou vazados.

Consequências: danos à reputação, perda de clientes e de receita, multas e processos.

Os controles de **DLP** (*Data Loss Prevention* — prevenção de perda de dados) combatem esses vetores:

| Vetor | Risco |
| --- | --- |
| E-mail e redes sociais | O mais comum |
| Dispositivos não criptografados | Notebook roubado entrega os dados |
| Armazenamento em nuvem | Configurações fracas |
| Mídia removível | Cópia ou perda de pen drive |
| Cópia impressa | Documentos sem triturar |
| Controle de acesso inadequado | Senhas fracas ou roubadas |

### 2.6 Hackers e Atores de Ameaça

| Tipo | Quem é |
| --- | --- |
| Chapéu branco (*white hat*) | **Hacker ético**; testa e relata vulnerabilidades |
| Chapéu cinza (*gray hat*) | Invade sem permissão, mas **não para ganho pessoal** |
| Chapéu preto (*black hat*) | **Criminoso**, por ganho pessoal ou malícia |

O **ator de ameaça** é o hacker de chapéu cinza ou preto.

### 2.7 Evolução dos Atores de Ameaça

O *hacking* começou nos anos 1960 com o **phreaking** telefônico (manipular o sistema da telefônica para fazer ligações de graça). Nos anos 1980, surgiu a **discagem de guerra** (*war dialing*), que ligava para todos os números em busca de modems.

| Tipo | Características |
| --- | --- |
| Script kiddies | Inexperientes que **usam ferramentas prontas** |
| Corretores de vulnerabilidades | Descobrem falhas e as relatam por recompensa |
| Hacktivistas | **Protestam contra ideias políticas e sociais**, com vazamentos e DDoS |
| Cibercriminosos | **Motivados por dinheiro** |
| Patrocinados pelo Estado | Atacam governos e empresas estrangeiros |

### 2.8 Responsabilidades de Segurança

Os atores de ameaça **não escolhem vítimas**. Por isso, a segurança é uma **responsabilidade compartilhada**.

As organizações devem ter:

- software de segurança atualizado;
- testes de penetração regulares;
- backups;
- política de segurança atualizada;
- senhas fortes;
- **autenticação de dois fatores**.

### 2.9 Indicadores de Comprometimento e de Ataque

Os **IOCs** (*Indicators of Compromise* — indicadores de comprometimento) são **a evidência de que um ataque ocorreu**. Exemplos:

- hashes e nomes de arquivos de malware;
- domínios e IPs usados no ataque;
- alterações feitas no sistema.

Os **IOAs** (*Indicators of Attack* — indicadores de ataque) tratam da **motivação e das estratégias** do atacante e permitem uma defesa **proativa**.

| Indicador | Foco | Tipo de defesa |
| --- | --- | --- |
| IOC | Evidências de um ataque já ocorrido | Reativa |
| IOA | Estratégias do atacante | Proativa |

### 2.10 Compartilhamento de Ameaças e Conscientização

- a **CISA** (*Cybersecurity and Infrastructure Security Agency*, EUA) usa o **AIS** (*Automated Indicator Sharing*) para compartilhar indicadores de ataque gratuitamente;
- em outubro acontece o **mês de conscientização em segurança cibernética**;
- a **ENISA** é a agência de cibersegurança da União Europeia.

## 3. Domínios e Tipos de Ameaças

Um **domínio de ameaça** é uma **área de controle, autoridade ou proteção que os atacantes podem explorar** para entrar em um sistema.

### 3.1 Formas de Explorar um Domínio

Os atacantes exploram um domínio por meio de:

- acesso físico direto;
- redes sem fio que ultrapassam os limites da empresa;
- Bluetooth ou **NFC** (*Near Field Communication* — comunicação por aproximação);
- anexos de e-mail maliciosos;
- elos menos seguros da **cadeia de fornecimento** (fornecedores e parceiros);
- redes sociais;
- mídia removível;
- aplicativos na nuvem.

### 3.2 Tipos de Ameaças Cibernéticas

| Categoria | Exemplos |
| --- | --- |
| Ataques de software | DoS; vírus |
| Erros de software | Bug; aplicativo fora do ar; *cross-site scripting* |
| Sabotagem | Desfiguração (*defacement*) do site |
| Erro humano | Erros de digitação; firewall mal configurado |
| Roubo | Notebooks levados de uma sala destrancada |
| Falhas de hardware | Disco que trava |
| Interrupção de serviços básicos | Falta de energia; vazamento de água |
| Desastres naturais | Inundações, incêndios, terremotos |

Os criminosos muitas vezes **combinam duas ou mais táticas**.

### 3.3 Ameaças ao Usuário

O **domínio do usuário** inclui funcionários, clientes e parceiros. Os usuários são **o elo mais fraco** da segurança.

| Ameaça | Explicação |
| --- | --- |
| Falta de conscientização | Não conhece as políticas e os riscos |
| Políticas mal aplicadas | Não entende as consequências |
| Roubo de dados | Prejuízo financeiro e de reputação |
| Downloads e mídias não autorizados | Origem de muitas infecções |
| VPNs não autorizadas | A criptografia esconde o roubo de dados |
| Sites não autorizados | Baixam scripts, plug-ins ou *adware* maliciosos |
| Destruição de sistemas ou dados | Funcionários insatisfeitos ou concorrentes |

**Importante:** nenhuma tecnologia torna os sistemas mais seguros do que **o comportamento das pessoas** que os usam.

### 3.4 Ameaças aos Dispositivos

As principais ameaças aos dispositivos são:

- equipamentos ligados e sem supervisão;
- arquivos de fontes não confiáveis;
- vulnerabilidades dos programas instalados;
- novos malwares (programas maliciosos) todos os dias;
- mídias não autorizadas;
- **hardware ou software desatualizado**.

### 3.5 Ameaças à Rede Local e à Nuvem

A **LAN** precisa de **segurança forte e controle de acesso rigoroso**. Ameaças:

- acesso não autorizado a salas de equipamentos e sistemas;
- sistemas sem atualização;
- usuários desonestos na rede sem fio;
- sondagem e **varredura de portas**;
- firewalls mal configurados.

A **nuvem privada** atende **uma única organização**. Ameaças: varredura de portas, erros de configuração e usuários remotos que baixam dados confidenciais.

A **nuvem pública** é **compartilhada entre organizações**:

| Modelo | O que oferece |
| --- | --- |
| SaaS (*Software as a Service*) | **Software hospedado na nuvem** |
| PaaS (*Platform as a Service*) | **Plataforma** para desenvolver aplicativos |
| IaaS (*Infrastructure as a Service*) | **Recursos virtuais** de infraestrutura |

O provedor protege o ambiente, mas **cada organização protege seus próprios recursos**.

### 3.6 Ameaças aos Aplicativos e às Instalações

O **domínio dos aplicativos** inclui sistemas e dados críticos. Ameaças: acesso não autorizado, servidor fora do ar, vulnerabilidades e perda de dados.

O **domínio das instalações físicas** trata do acesso físico a prédios e salas.

| Domínio | O que inclui |
| --- | --- |
| Usuário | Pessoas que acessam os sistemas |
| Dispositivo | Computadores, celulares e mídias |
| LAN | Rede local |
| Nuvem privada | Recursos de uma só organização |
| Nuvem pública | Serviços compartilhados |
| Aplicativo | Sistemas e dados críticos |
| Instalações físicas | Prédios e salas |

### 3.7 Complexidade das Ameaças

As vulnerabilidades vêm de **erros de programação, falhas de protocolos ou má configuração**.

- **APT** (*Advanced Persistent Threat* — ameaça persistente avançada): **ataque contínuo e discreto** que **fica sem ser detectado por muito tempo**; visa governos e grandes organizações;
- **ataques de algoritmo**: usam algoritmos legítimos para gerar comportamento indesejado, como consumir toda a memória.

### 3.8 Inteligência de Ameaças

A **inteligência de ameaças** ajuda a entender o risco. O **OSINT** (*Open Source Intelligence*) é a inteligência obtida em **fontes públicas**.

| Fonte | O que é |
| --- | --- |
| CVE (*Common Vulnerabilities and Exposures*) | **Dicionário público de vulnerabilidades**, mantido pela MITRE; exemplo: CVE-2021-44228 |
| Dark web | Conteúdo criptografado, **fora dos buscadores** |
| IOC | Evidências que comprovam uma violação |
| AIS | Troca de indicadores da CISA, com **STIX** (linguagem) e **TAXII** (protocolo) |

## 4. Engenharia Social e Outros Métodos de Engano

A maioria dos ataques envolve algum tipo de **fraude para enganar as vítimas**.

### 4.1 Engenharia Social

A **engenharia social** é uma **estratégia não técnica que manipula pessoas** para que façam algo ou revelem informações. Ela **explora a natureza humana**: a vontade de ajudar, a ganância e a vaidade.

- **pretexto** (*pretexting*): o atacante **mente para obter dados**;
- **quid pro quo** ("algo por algo"): pede informações **em troca de algo**;
- **fraude de identidade**: usa a identidade roubada de alguém.

### 4.2 Táticas de Engenharia Social

| Tática | Como funciona | Exemplo |
| --- | --- | --- |
| Autoridade | Obedecer a quem parece ter autoridade | "Intimação oficial" que é um PDF infectado |
| Intimidação | Pressionar a vítima | Ameaça de demissão |
| Consenso (prova social) | Fazer o que os outros fazem | Post com comentários falsos |
| Escassez | Pouca quantidade | "Poucas unidades" |
| Urgência | Pouco tempo | "Por tempo limitado" |
| Familiaridade | Atender a quem se conhece | Perfil clonado de um amigo |
| Confiança | Construir uma relação com a vítima | Falso especialista |

### 4.3 Olhar por Cima do Ombro e Vasculhar o Lixo

- **shoulder surfing**: **observar o alvo para obter senhas e PINs**;
- **dumpster diving**: **examinar o lixo do alvo**; por isso, documentos confidenciais devem ser **triturados**.

### 4.4 Falsificação de Identidade, Farsas e Entrada Indevida

- **representação** (*impersonation*): **fingir ser outra pessoa**, como um falso funcionário da Receita;
- **farsa** (*hoax*): mensagem enganosa, como o aviso de um vírus inexistente;
- **piggybacking** ou **tailgating** (carona): **seguir uma pessoa autorizada para entrar** em área restrita.

Defesa contra a carona: a **mantrap** (eclusa), em que **a porta externa precisa fechar antes de a interna abrir**.

### 4.5 Outros Métodos de Engano

| Método | Como funciona |
| --- | --- |
| Fraude de fatura | Fatura falsa que leva a pagar ou a digitar credenciais |
| Ataque de bebedouro (*watering hole*) | Infecta **sites que a empresa-alvo usa** |
| Typosquatting | Explora **erros de digitação** no endereço, como "gooogle.com" |
| Adendo (*prepending*) | Remove a etiqueta "externo" do e-mail ou acrescenta marcas como "RE:" no assunto, para a mensagem parecer interna ou uma resposta |
| Campanhas de influência | Notícias falsas e desinformação |

### 4.6 Defesa Contra o Engano

As empresas precisam **conscientizar e treinar** os funcionários:

- nunca revelar credenciais a desconhecidos;
- desconfiar de links e downloads não solicitados;
- criar e ensinar políticas de segurança;
- **não ceder à pressão** de desconhecidos.

## 5. Malware e Sua Mitigação

O **malware** (*malicious software*) é **qualquer código usado para roubar dados, contornar o controle de acesso ou danificar um sistema**.

### 5.1 Vírus, Worms e Cavalos de Troia

- **vírus**: **se replica e se anexa a outros arquivos**; a maioria **exige uma ação do usuário** para ser ativada; sofre mutações para escapar da detecção. Exemplo: Melissa (1999);
- **worm**: **replica-se sozinho explorando vulnerabilidades da rede**; **não precisa de hospedeiro**; carrega uma **carga útil** (*payload*), o código que causa o dano. Exemplo: Code Red (2001);
- **cavalo de Troia** (*trojan*): **parece legítimo, mas esconde intenção maliciosa**; **não se replica**.

| Malware | Precisa de hospedeiro? | Precisa do usuário? | Replica-se? |
| --- | --- | --- | --- |
| Vírus | Sim | Sim, para ser ativado | Sim |
| Worm | Não | Só na infecção inicial | Sim, sozinho pela rede |
| Cavalo de Troia | Disfarça-se de programa legítimo | Sim | Não |

### 5.2 Backdoors e Rootkits

Um **backdoor** (porta dos fundos) dá **acesso não autorizado contornando a autenticação**. Costuma ser instalado por uma **RAT** (*Remote Administration Tool*) e **mantém o acesso mesmo depois da correção da vulnerabilidade**.

Um **rootkit** **modifica o sistema operacional para criar um backdoor** e eleva privilégios. É **muito difícil de detectar**; em geral, o computador precisa ser **apagado e reinstalado**.

### 5.3 Bombas Lógicas, Ransomware e Keyloggers

- **bomba lógica**: **fica inativa até um gatilho** (data, evento) e então sabota o sistema;
- **ransomware**: **mantém os dados presos até o pagamento de um resgate**, em geral criptografando-os; muitas vítimas não recuperam os dados mesmo pagando. Espalha-se por **phishing**;
- **keylogger**: **grava cada tecla digitada** e envia ao criminoso; pode ser software ou dispositivo físico.

### 5.4 Mitigação de Malware

O **antivírus** é a principal defesa contra o malware.

**Importante:** a **atualização automática das definições de vírus** é o requisito mais crítico.

O antivírus é **baseado em host**: **não impede o vírus de entrar na rede**. Por isso, dispositivos no **perímetro** identificam malware pelos **IOCs** e o retiram do tráfego.

**Observação:** **nenhuma técnica é 100% eficaz**.

### 5.5 Mitigação de Worms

A resposta a worms tem **quatro fases**:

1. **contenção**: **limita a propagação**, segmentando a rede com **ACLs** (*Access Control Lists*, listas de regras que permitem ou bloqueiam tráfego);
2. **inoculação**: **aplica a correção em todos os sistemas não infectados**;
3. **quarentena**: **identifica e isola as máquinas infectadas**;
4. **tratamento**: **desinfecta** os sistemas ou os reinstala.

Contenção → Inoculação → Quarentena → Tratamento

## 6. Outros Ataques Cibernéticos e Boas Práticas de Defesa

Além do malware, os atacantes **derrubam serviços, interceptam comunicações e exploram falhas desconhecidas**.

### 6.1 Negação de Serviço

Os ataques de **negação de serviço** (**DoS**) são **simples de fazer, mesmo por atacantes sem experiência**. Há dois tipos:

- **tráfego esmagador**: o alvo recebe **mais dados do que consegue processar**;
- **pacotes maliciosamente formatados**: pacotes com erros que o receptor **não consegue tratar**.

O **DDoS** (*Distributed Denial of Service*) **parte de muitas fontes coordenadas**:

1. o atacante monta uma **botnet**, uma rede de computadores infectados (**zumbis**) controlados por **manipuladores** (*handlers*);
2. os zumbis infectam outros hosts;
3. o atacante ordena o ataque.

Atacante → Manipuladores → Zumbis → Alvo

![No DDoS, o atacante comanda os manipuladores, que comandam os zumbis da botnet; todos atacam o mesmo alvo](img/endpoint/end_ddos.png){width=6in}

### 6.2 Homem no Meio e Ataques de Repetição

- **MitM** (*Man-in-the-Middle* — homem no meio): o criminoso **intercepta, manipula e retransmite** as informações entre origem e destino;
- **MitMo** (*Man-in-the-Mobile*): **assume o controle do celular** da vítima; exemplo: o **ZeuS** captura os SMS com códigos de verificação;
- **ataque de repetição** (*replay*): **captura uma comunicação e a retransmite** para contornar a autenticação.

### 6.3 Ataques de Dia Zero

Um **ataque de dia zero** **explora uma vulnerabilidade antes que o fabricante a conheça ou corrija**. A rede fica exposta entre a descoberta (**hora zero**) e a correção.

### 6.4 Ataques Físicos, à IA, à Cadeia de Fornecimento e à Nuvem

- **ataques físicos**: pen drive com malware, cabos USB com chip sem fio, clonadores de cartão;
- **ataques adversos à IA**: dados corrompidos distorcem o aprendizado de máquina;
- **ataques à cadeia de fornecimento**: atacam os fornecedores de sistemas, peças e software;
- **ataques à nuvem**: exploram dados e serviços em SaaS, PaaS e IaaS.

### 6.5 Defesa Contra os Ataques

As principais medidas são:

- **descartar pacotes de fora com endereço de origem interno**, que só podem ser falsificados;
- manter **correções** em dia;
- **distribuir a carga** entre vários servidores;
- **bloquear o ICMP vindo de fora**; o **ICMP** (*Internet Control Message Protocol*) envia mensagens de erro e controle e é muito usado em DoS.

### 6.6 Ataques de Acesso e Sua Mitigação

Os **ataques de acesso** tentam **entrar em contas e sistemas sem autorização**, muitas vezes por **dicionário** ou **força bruta**. As defesas são:

- senhas com **pelo menos oito caracteres** e complexas;
- **bloqueio da conta** depois de várias tentativas erradas;
- **confiança mínima** entre sistemas;
- criptografia no acesso remoto;
- **MFA** (*Multi-Factor Authentication* — autenticação multifator), como senha mais código ou **token de uso único**;
- educação contra engenharia social.

Os ataques de acesso são detectados pela **revisão dos logs**, como um número incomum de logins com falha.

### 6.7 Boas Práticas de Defesa

As melhores práticas são:

- ter uma **política de segurança escrita**;
- educar contra engenharia social;
- controlar o acesso físico;
- usar senhas fortes;
- criptografar dados confidenciais;
- usar firewalls, IPS, VPN, antivírus e filtragem de conteúdo;
- fazer backups e **testá-los**;
- **desligar serviços e portas desnecessários**;
- instalar as correções com frequência;
- fazer auditorias de segurança.

## 7. Vulnerabilidades do IP

Para reconhecer um ataque, o analista precisa conhecer os campos dos cabeçalhos e como podem ser manipulados.

### 7.1 IPv4 e IPv6

O **IP** (*Internet Protocol*) é o protocolo da **camada 3** que leva o pacote da origem ao destino. É **sem conexão** e não controla o fluxo; isso fica com o **TCP**, na camada 4.

**Importante:** o IP **não verifica se o endereço de origem é verdadeiro**. Por isso, o atacante pode falsificar a origem.

### 7.2 Cabeçalho do IPv4

O cabeçalho do IPv4 tem no mínimo **20 bytes**. Campos principais:

| Campo | Função |
| --- | --- |
| Versão | Valor 4 |
| Serviços diferenciados (DS) | Prioridade do pacote (**DSCP**) |
| Tamanho total | Até 65.535 bytes |
| Identificação, flags e deslocamento | **Fragmentação** e remontagem |
| TTL (*Time to Live*) | **Limita a vida do pacote**: cada roteador subtrai 1; em zero, o pacote é descartado |
| Protocolo | ICMP (1), TCP (6) e UDP (17) |
| Soma de verificação | Detecta erros no cabeçalho |
| Endereços de origem e destino | 32 bits cada |

### 7.3 Cabeçalho do IPv6

O cabeçalho do IPv6 tem **oito campos e 40 bytes**:

| Campo | Função |
| --- | --- |
| Versão | Valor 6 |
| Classe de tráfego | Equivale ao DS do IPv4 |
| Rótulo de fluxo | Mesmo tratamento para o mesmo fluxo |
| Tamanho da carga útil | Tamanho dos dados |
| Próximo cabeçalho | Equivale ao campo Protocolo |
| Limite de saltos | Substitui o TTL |
| Endereços de origem e destino | 128 bits cada |

O IPv6 pode ter **cabeçalhos de extensão** opcionais.

**Observação:** **os roteadores não fragmentam pacotes IPv6**.

### 7.4 Ataques ao IP

| Ataque | Como funciona |
| --- | --- |
| Ataques ICMP | Descobrir hosts, inundar e alterar rotas |
| DoS | Impedir o acesso de usuários legítimos |
| DDoS | Ataque coordenado de várias máquinas |
| Falsificação de endereços | Origem falsa, de forma cega ou não cega |
| Homem no meio (MitM) | Interceptar e alterar a comunicação |
| Sequestro de sessão | Assumir uma sessão já estabelecida |

### 7.5 Ataques ICMP

O **ICMP** transporta **mensagens de diagnóstico e de erro**. O **ping** envia uma **solicitação de eco** e recebe uma **resposta de eco**.

Os atacantes usam o ICMP para **reconhecimento e varredura**: mapear a rede, descobrir hosts e identificar o sistema operacional. Também para a **inundação ICMP**.

| Mensagem ICMP | Uso no ataque |
| --- | --- |
| Solicitação e resposta de eco | Verificação de hosts e DoS |
| Destino inacessível | Reconhecimento e varredura |
| Resposta de máscara | Mapear a rede interna |
| Redirecionamento | Desviar o tráfego por um dispositivo comprometido (MitM) |
| Descoberta de roteador | Injetar rotas falsas |

A defesa é **filtrar o ICMP por ACL na borda da rede**.

### 7.6 Amplificação e Reflexão

No **ataque Smurf**:

1. **amplificação**: pedidos de eco a **muitos hosts**, com o **IP da vítima como origem**;
2. **reflexão**: todos **respondem à vítima**, que fica sobrecarregada.

Atacante → Pedidos com o IP da vítima → Muitos hosts → Respostas → Vítima

![No ataque Smurf, os pedidos de eco levam o IP da vítima como origem, e todas as respostas caem sobre ela](img/endpoint/end_smurf.png){width=6in}

Hoje também se usa reflexão e amplificação pelo **DNS** e pelo **NTP**.

### 7.7 Falsificação de Endereços

A **falsificação de IP** (*IP spoofing*) cria pacotes com **origem falsa** para esconder o remetente ou se passar por outro. Pode ser:

- **não cega**: o atacante **vê o tráfego**; serve para sequestrar sessões;
- **cega**: o atacante **não vê o tráfego**; serve para DoS.

A **falsificação de MAC** exige acesso à rede interna:

1. o atacante usa o **MAC de um alvo**;
2. o switch atualiza a **tabela CAM** (tabela de endereços MAC) com a porta do atacante;
3. o switch passa a **encaminhar ao atacante** os quadros do alvo.

Também há falsificação de serviços, como um **servidor DHCP falso**.

### 7.8 Mitigação de Ataques de Reconhecimento

Os **ataques de reconhecimento** **precedem outros ataques**: o atacante coleta informações. São detectados por **alarmes** de limite, como pedidos ICMP por segundo.

As medidas são:

- autenticação;
- **criptografia**, que torna inútil o **sniffer de pacotes**;
- ferramentas anti-sniffer;
- switches;
- firewall e IPS.

**Observação:** é **impossível impedir a varredura de portas**, mas o IPS e o firewall limitam o que ela descobre.

## 8. Vulnerabilidades do TCP e do UDP

Os atacantes exploram os protocolos da **camada 4**: o TCP e o UDP. Com **varreduras de portas**, descobrem quais serviços o alvo oferece.

### 8.1 Cabeçalho do TCP

O cabeçalho **TCP** (*Transmission Control Protocol*) tem **20 bytes** sem opções. Campos principais: portas de origem e destino (16 bits cada), número de sequência e de confirmação (32 bits cada), bits de controle, janela e soma de verificação.

Os **seis bits de controle** (*flags*) são:

- **URG**: dados urgentes;
- **ACK**: confirmação;
- **PSH**: entregar os dados imediatamente;
- **RST**: encerra a conexão;
- **SYN**: sincroniza os números de sequência (abre a conexão);
- **FIN**: o remetente não tem mais dados.

### 8.2 Serviços do TCP

O TCP oferece:

- **entrega confiável**: confirmações e retransmissões;
- **controle de fluxo**;
- **comunicação com estado**: abre a conexão antes de enviar dados.

O **handshake de três vias**:

1. o cliente envia **SYN** (SEQ=100);
2. o servidor responde **SYN-ACK** (SEQ=300, ACK=101);
3. o cliente envia **ACK** (SEQ=101, ACK=301).

SYN → SYN-ACK → ACK

O encerramento usa **quatro mensagens**: FIN, ACK, FIN, ACK.

### 8.3 Ataques ao TCP

- **inundação SYN**: **muitos SYN com origem falsificada**; o servidor fica com **conexões semiabertas** esperando ACKs que nunca chegam;
- **redefinição** (*TCP reset*): pacote falsificado com **RST** **encerra a conexão**;
- **sequestro de sessão TCP**: o atacante **prevê o número de sequência** e assume um host autenticado; pode enviar dados, mas não recebê-los.

![Na inundação SYN, o servidor guarda cada conexão semiaberta à espera de um ACK que nunca chega](img/endpoint/end_synflood.png){width=6in}

### 8.4 Funcionamento do UDP

O **UDP** (*User Datagram Protocol*) é **sem conexão** e tem **sobrecarga muito menor** que o TCP: não retransmite nem controla o fluxo. Seu cabeçalho tem **8 bytes**.

É usado por DNS, DHCP, **TFTP**, **SNMP** e aplicações em tempo real, como vídeo e VoIP.

### 8.5 Ataques ao UDP

O UDP **não tem criptografia** por padrão, e a soma de verificação é **opcional**.

Na **inundação UDP**:

1. o atacante usa ferramentas como **LOIC**;
2. envia muitos pacotes UDP a portas fechadas;
3. o servidor responde com ICMP de **porta inacessível**;
4. a largura de banda é consumida.

| Protocolo | Ataque | Efeito |
| --- | --- | --- |
| TCP | Inundação SYN | Conexões semiabertas esgotam o servidor |
| TCP | Redefinição (RST) | Conexão encerrada à força |
| TCP | Sequestro de sessão | Atacante envia dados como host autenticado |
| UDP | Alteração dos dados | Dados mudados sem o destino perceber |
| UDP | Inundação UDP | Largura de banda consumida |

## 9. Ataques ao ARP, aos Switches e ao DHCP

Os serviços da rede local também são alvos, porque **não têm autenticação** por padrão.

### 9.1 Funcionamento do ARP

O **ARP** (*Address Resolution Protocol*) **descobre o endereço MAC de um host a partir do seu IP**:

1. o host envia uma **solicitação ARP em difusão**: "qual é o MAC de 192.168.1.7?";
2. só o dono do IP responde com seu MAC;
3. o host guarda o par IP–MAC no **cache ARP**.

O **ARP gratuito** é uma resposta não solicitada que os hosts **guardam sem verificar**.

**Importante:** **qualquer host pode se declarar dono de qualquer IP ou MAC**.

### 9.2 Envenenamento do Cache ARP

O **envenenamento do cache ARP** (*ARP spoofing*) envia **respostas ARP falsas** para **associar o MAC do atacante ao IP de outro dispositivo**, em geral o **gateway padrão**. O atacante fica **entre a vítima e o resto da rede** (MitM).

Exemplo:

1. o PC-A e o roteador R1 conhecem os MACs verdadeiros um do outro;
2. o atacante envia duas respostas ARP gratuitas falsas: ao PC-A, diz ter o IP do R1; ao R1, diz ter o IP do PC-A;
3. **todo o tráfego entre eles passa pelo atacante**.

![Com duas respostas ARP falsas, o atacante se coloca entre o PC e o gateway](img/endpoint/end_arp.png){width=6in}

O envenenamento pode ser:

- **passivo**: **rouba informações**;
- **ativo**: **modifica ou injeta dados**.

Ferramentas: dsniff, Cain & Abel, ettercap e Yersinia.

### 9.3 Ataques aos Switches

O **switch** encaminha cada quadro pela **tabela de endereços MAC** (tabela CAM).

- **falsificação de MAC**: usa o MAC de um dispositivo válido e recebe os quadros dele;
- **inundação de MAC** (*MAC flooding*): **inunda o switch com MACs falsos**. A tabela enche, e o switch passa a enviar os quadros para todas as portas, como um hub; assim, o atacante captura o tráfego dos outros.

| Ataque | O que falsifica | Resultado |
| --- | --- | --- |
| Falsificação de MAC | MAC de um dispositivo válido | Recebe os quadros do outro |
| Envenenamento ARP | Associação entre IP e MAC | MitM |
| Falsificação de IP | IP de origem | Esconde a identidade |
| Inundação de MAC | Muitos MACs falsos | Compromete o switch |

### 9.4 Funcionamento do DHCP

O **DHCP** (*Dynamic Host Configuration Protocol*) **fornece automaticamente a configuração IP**: endereço, máscara, gateway, DNS e tempo de concessão.

Discover → Offer → Request → ACK

### 9.5 Falsificação de DHCP

Na **falsificação de DHCP**, um **servidor DHCP falso** fornece parâmetros falsos:

- **gateway errado** → MitM;
- **DNS errado** → sites maliciosos;
- **IP errado** → negação de serviço.

O ataque funciona porque **o cliente aceita a primeira oferta que recebe**.

![O cliente aceita a primeira oferta que chega; se for a do servidor falso, passa a usar o atacante como gateway](img/endpoint/end_dhcp.png){width=6in}

### 9.6 Mitigação de DoS e Tecnologias Antispoofing

Um dos primeiros sinais de DoS são as **reclamações de usuários** sobre rede lenta. O **monitoramento do uso da rede** deve estar sempre ativo.

Tecnologias **antispoofing** dos switches e roteadores:

- **segurança de porta** (*port security*): limita quais e quantos MACs usam cada porta;
- **DHCP snooping**: aceita respostas DHCP só de portas confiáveis;
- **IP Source Guard**: bloqueia IPs de origem que não correspondem ao entregue pelo DHCP;
- **DAI** (*Dynamic ARP Inspection*): descarta respostas ARP falsas;
- **ACLs**.

| Ataque | Principais defesas |
| --- | --- |
| Malware | Antivírus atualizado e filtragem no perímetro |
| Worms | Contenção, inoculação, quarentena e tratamento |
| Reconhecimento | Criptografia, anti-sniffer, firewall e IPS |
| Acesso | Senhas fortes, bloqueio de conta e MFA |
| DoS | Monitoramento e antispoofing |

## 10. Ataques ao DNS

O **DNS** (*Domain Name System*) **associa nomes, como www.cisco.com, a endereços IP**. As respostas usam **registros de recursos** (**RR**, *Resource Records*).

**Importante:** a proteção do DNS costuma ser esquecida, mas ele é essencial.

### 10.1 Reputação, Sequestro de Domínio e Redirecionamento

- **reputação de domínio**: monitorar a reputação do domínio e do IP da empresa;
- **sequestro de domínio**: o atacante **obtém o controle das informações de DNS** do alvo, em geral por engenharia social contra o e-mail do administrador, achado no **WHOIS**;
- **redirecionamento de URL**: levar o usuário a um site malicioso.

### 10.2 Ataques aos Resolvedores Abertos

Um **resolvedor aberto** **responde a consultas de qualquer cliente**, e por isso é vulnerável a:

| Ataque | Como funciona |
| --- | --- |
| Envenenamento do cache DNS (*DNS spoofing*) | **RRs falsos** levam os usuários a **sites maliciosos** |
| Amplificação e reflexão | Consultas com o **IP da vítima como origem**; aumenta o ataque e esconde a origem |
| Utilização de recursos | DoS que esgota o resolvedor |

### 10.3 Técnicas Furtivas e Sombreamento de Domínio

- **fluxo rápido** (*fast flux*): esconde sites maliciosos atrás de **IPs que mudam a cada poucos minutos**;
- **fluxo duplo** (*double IP flux*): muda os IPs **e o servidor de nomes autoritativo** (o servidor que dá a resposta oficial sobre o domínio);
- **DGA** (algoritmos de geração de domínio): o malware **gera nomes de domínio aleatórios** para achar os servidores de **comando e controle** (**C&C**).

No **sombreamento de domínio** (*domain shadowing*), o atacante **rouba as credenciais de um domínio e cria muitos subdomínios** maliciosos.

### 10.4 Tunelamento DNS

No **tunelamento DNS**, o atacante **coloca tráfego que não é DNS dentro do tráfego DNS**, o que **contorna as soluções de segurança**.

De forma simplificada:

1. os dados são divididos em blocos codificados;
2. cada bloco vai em um **subdomínio** de uma consulta DNS;
3. a consulta chega ao servidor DNS do atacante;
4. as respostas trazem **comandos codificados** para o malware.

![No tunelamento DNS, os dados saem escondidos em consultas e os comandos voltam nas respostas](img/endpoint/end_dnstunnel.png){width=6in}

Para interromper o túnel:

- inspecionar o tráfego DNS;
- desconfiar de **consultas mais longas que a média**;
- usar soluções como o **Cisco Umbrella**;
- considerar suspeitos os domínios de DNS dinâmico.

| Ataque | Objetivo |
| --- | --- |
| Envenenamento de cache | Levar usuários a sites falsos |
| Amplificação e reflexão | Aumentar o DoS e esconder a origem |
| Fluxo rápido e duplo | Esconder servidores maliciosos |
| DGA | Achar os servidores de comando e controle |
| Sombreamento de domínio | Subdomínios maliciosos em domínio legítimo |
| Tunelamento | Esconder comandos e dados roubados no DNS |

## 11. Ataques a Aplicações Web

Nos ataques web, o criminoso aproveita **falhas na programação do aplicativo** ou usa páginas comprometidas para infectar quem as visita.

### 11.1 Como Funciona um Ataque Web

De forma simplificada, o ataque web ocorre da seguinte maneira:

1. a vítima visita uma página **comprometida**;
2. a página a **redireciona** para um site com código malicioso;
3. o computador é infectado só pela visita, o **download automático** (*drive-by download*): um **kit de exploração** procura falhas no sistema e no navegador;
4. o kit baixa o código que explora a falha;
5. o computador baixa a **carga útil** (o malware);
6. o malware é executado.

O objetivo é sempre **levar o navegador da vítima à página do atacante**.

### 11.2 Códigos de Status HTTP

Os **logs dos servidores** revelam ataques pelos códigos de status:

| Código | Classe | Significado |
| --- | --- | --- |
| 1xx | Informativo | Resposta provisória |
| 2xx | Sucesso | Pedido aceito |
| 3xx | Redirecionamento | Ir a outra URL |
| 4xx | Erro do cliente | O cliente errou |
| 5xx | Erro do servidor | O servidor não pode atender |

### 11.3 Cross-Site Scripting (XSS)

No **XSS** (*Cross-Site Scripting* — script entre sites):

1. o criminoso **injeta um script malicioso** em uma página web;
2. o script passa para o navegador da vítima;
3. rouba **cookies** ou **tokens de sessão** (os dados que provam que o usuário está logado);
4. o criminoso **se passa pelo usuário**.

### 11.4 Tipos de XSS e Prevenção

O XSS ataca o **lado do cliente**. A causa é a **falta de validação** do conteúdo publicado. Há dois tipos:

- **armazenado** (persistente): fica **gravado no servidor** e atinge **todos os visitantes**;
- **refletido** (não persistente): fica **em um link**; só é infectado quem clica.

Prevenção: conscientizar os desenvolvedores, usar **IPS**, proxy web e treinar os usuários.

### 11.5 Ataques de Injeção

Nos ataques de injeção, o criminoso digita **comandos em vez de dados** em um campo de formulário; se a entrada não for filtrada, os comandos são executados.

| Ataque | Como funciona |
| --- | --- |
| Injeção de SQL | **Instrução SQL maliciosa em um campo de entrada**; permite ler, alterar ou destruir dados |
| Injeção de XML | Corrompe o processamento dos dados **XML** |
| Injeção de DLL | Faz o aplicativo **chamar uma DLL maliciosa** (biblioteca de código do Windows) |
| Injeção de LDAP | Extrai informações do diretório da empresa (**LDAP**) |

### 11.6 Bancos de Dados Expostos e Injeção de Código

- **injeção de código**: comandos (como PHP) **executados no servidor com as permissões do aplicativo**;
- **injeção de SQL**: um dos ataques mais comuns.

**Importante:** a defesa é a **validação rigorosa da entrada**.

### 11.7 Estouro de Buffer

O **estouro de buffer** ocorre quando os dados são **gravados além dos limites da área de memória** reservada ao aplicativo. Resultado: travamento, comprometimento de dados ou **elevação de privilégios**.

**Observação:** **quase metade das explorações** de programas vem de estouro de buffer.

### 11.8 Execução Remota de Código e Elevação de Privilégios

- **execução remota de código**: **executar qualquer comando** no dispositivo da vítima;
- **elevação de privilégios**: **acessar recursos normalmente restritos**.

O **Metasploit** é uma ferramenta de testes de penetração. Sua carga útil **Meterpreter** roda **direto na memória, sem tocar no disco**, o que **escapa dos antivírus**.

### 11.9 Outros Ataques a Aplicativos

| Ataque | Como funciona |
| --- | --- |
| CSRF (*Cross-Site Request Forgery*) | Envia comandos do navegador do usuário para um site em que ele **já está logado** |
| Condição de corrida (TOC/TOU) | Força o sistema a fazer **duas operações ao mesmo tempo**; o atacante troca algo entre o momento em que o sistema confere uma permissão (*time of check*) e o momento em que a usa (*time of use*) |
| Tratamento inadequado de entrada | Dados sem validação alteram o programa |
| Tratamento de erros | **Mensagens de erro revelam informações** |
| Ataque a API | Abuso de uma **API** (*Application Programming Interface*) |
| Repetição | Transmissão interceptada e repetida |
| Travessia de diretório | **Lê arquivos fora da pasta do site** |
| Exaustão de recursos | Sobrecarrega o **hardware do servidor**, não a banda |

### 11.10 iFrames Maliciosos

Um **iFrame** **carrega dentro da página outra página de outra origem**. O atacante invade um site e insere um iFrame **quase invisível** que entrega malware.

Prevenção: proxy web, Cisco Umbrella e orientar desenvolvedores a evitar iFrames.

### 11.11 Amortecimento HTTP 302

O **amortecimento HTTP 302** (*302 cushioning*) usa o código **302 Found**, que **redireciona o navegador**. O atacante **encadeia vários redirecionamentos** até a página maliciosa. É **difícil de detectar**, porque redirecionamentos são comuns.

### 11.12 Sequência com Sombreamento de Domínio

Os ataques costumam ser combinados:

Site comprometido → Redirecionamento 302 → Subdomínio sombreado → Kit de exploração → Malware

Prevenção: senhas fortes e autenticação de dois fatores nas contas de domínio, proxy web e verificação de subdomínios.

### 11.13 Defesa Contra Ataques a Aplicativos e à Web

As principais medidas são:

- **escrever código sólido**;
- **tratar toda entrada externa como hostil** e validá-la;
- manter tudo **atualizado**;
- usar **proxy web** para bloquear sites maliciosos;
- seguir o **OWASP Top 10**, a lista dos riscos web mais explorados;
- educar os usuários.

## 12. Ataques ao E-mail

O e-mail é a **espinha dorsal da comunicação corporativa** e uma das maiores portas de entrada de ataques.

### 12.1 Spam

O **spam** é o **e-mail não solicitado**, em geral publicidade, muitas vezes com links maliciosos ou golpes.

Os sinais de spam são:

- e-mail sem assunto;
- pedido para atualizar os dados da conta;
- erros de ortografia;
- links longos ou estranhos;
- aparência de empresa legítima com pequenas diferenças;
- pedido urgente para abrir um anexo.

Diante desses sinais, **avisar a equipe de segurança**.

### 12.2 Phishing e Suas Variações

O **phishing** é uma **fraude em que o criminoso se disfarça de pessoa ou empresa legítima** para roubar dados ou instalar malware.

| Ataque | Como funciona |
| --- | --- |
| Spear phishing | **Altamente direcionado** a uma pessoa |
| Whaling | Contra **vítimas de alto escalão** |
| Vishing | **Phishing por voz** |
| SMiShing | **Phishing por SMS** |
| Pharming | **Leva o usuário a uma cópia falsa de um site oficial**, mesmo quando ele digita o endereço certo (por exemplo, com o DNS envenenado) |

### 12.3 Outras Ameaças ao E-mail

Mensagens **HTML** lidas em dispositivos **fora do firewall** abrem mais caminhos para ataques.

| Ameaça | Como funciona |
| --- | --- |
| Ataques por anexo | Arquivos maliciosos de aparência profissional |
| Falsificação de e-mail | Remetente falso, como um banco |
| Retransmissor aberto (*open relay*) | Servidor **SMTP** que **deixa qualquer um enviar e-mails** |
| Homóglifos | Caracteres quase idênticos (O e 0, l e 1) em links |

**Importante:** servidores de e-mail **nunca devem ser retransmissores abertos**.

Os usuários são **a última linha de defesa** quando um ataque passa pelas proteções.

### 12.4 Defesa Contra Ataques ao E-mail

As principais medidas são:

- filtragem de spam e antivírus;
- equipamento de segurança de e-mail;
- **educar os funcionários**;
- **nunca supor que um anexo é seguro**, mesmo de um contato confiável;
- manter os programas atualizados.

## 13. Comunicação sem Fio

As redes sem fio permitem conectar-se de qualquer lugar, mas estão sujeitas a ataques específicos.

### 13.1 LAN sem Fio e LAN com Fio

Uma **WLAN** (*Wireless LAN* — rede local sem fio) usa **radiofrequência** (RF) em vez de cabos. Padrões **IEEE**: **802.3** (Ethernet com fio) e **802.11** (sem fio).

| Característica | WLAN 802.11 | LAN Ethernet 802.3 |
| --- | --- | --- |
| Camada física | Radiofrequência | Cabos |
| Acesso ao meio | Prevenção de colisões (CSMA/CA) | Detecção de colisões (CSMA/CD) |
| Conexão | Ponto de acesso (AP) | Switch |
| Disponibilidade | Qualquer um ao alcance do AP | Exige cabo |
| Interferência | Sim | Mínima |
| Privacidade | Mais problemas: o sinal sai do prédio | Maior |

### 13.2 Quadro 802.11

O quadro 802.11 tem **cabeçalho, carga útil e FCS** (*Frame Check Sequence*, detecção de erros). Tem até **quatro campos de endereço**: quem recebe, quem transmite, o destino e, em casos especiais, um quarto endereço.

### 13.3 CSMA/CA

A WLAN é **half-duplex e de meio compartilhado**: só um cliente transmite por vez. Como não detecta colisões, usa o **CSMA/CA** (*Carrier Sense Multiple Access with Collision Avoidance*):

1. escuta o canal;
2. envia ao AP um **RTS** (*Request to Send*);
3. recebe um **CTS** (*Clear to Send*);
4. transmite;
5. espera a confirmação; sem ela, supõe colisão e recomeça.

### 13.4 Associação ao Ponto de Acesso

Descobrir o AP → Autenticar → Associar

Parâmetros que cliente e AP precisam combinar:

- **SSID** (*Service Set Identifier*): **o nome da rede**;
- **senha**;
- **modo de rede**: 802.11a/b/g/n/ac/ax (n = Wi-Fi 4, ac = Wi-Fi 5);
- **modo de segurança**: sempre o **nível mais alto** disponível;
- **canal**: a faixa de frequência.

### 13.5 Descoberta Passiva e Ativa

- **passiva**: o AP **anuncia a rede** com **quadros beacon**;
- **ativa**: o **cliente envia uma sondagem** (*probe request*); necessária quando o AP não envia beacons.

### 13.6 AP, LWAP e WLC

Os **roteadores sem fio** domésticos juntam roteador, switch e AP.

Em redes maiores, o **WLC** (*Wireless LAN Controller*) **centraliza o controle dos APs**, que viram **LWAPs** (*Lightweight Access Points* — APs leves). Isso simplifica a configuração e o monitoramento.

## 14. Ameaças às Redes sem Fio e aos Dispositivos Móveis

Uma WLAN fica aberta a **qualquer um ao alcance do AP**. O atacante **nem precisa entrar no prédio**.

### 14.1 Principais Ameaças sem Fio

- **interceptação de dados**: exige criptografia;
- **intrusos**: barrados por autenticação eficaz;
- **negação de serviço**;
- **APs não autorizados**.

### 14.2 Negação de Serviço sem Fio

O DoS sem fio pode resultar de:

- dispositivos mal configurados;
- **interferência intencional** (um *jammer* de RF);
- **interferência acidental**: micro-ondas, telefones sem fio, babás eletrônicas.

**Importante:** a **banda de 2,4 GHz sofre mais interferência que a de 5 GHz**.

Para reduzir o risco:

- mudar configurações fora do horário comercial;
- monitorar a interferência;
- usar **5 GHz** nas áreas com interferência.

### 14.3 Pontos de Acesso não Autorizados

Um **AP não autorizado** (*rogue AP*) é **ligado à rede da empresa sem autorização**. Permite capturar pacotes e fazer **MitM**.

Na **desautenticação**, o atacante desconecta o cliente do AP verdadeiro para capturar a nova autenticação.

Até um **hotspot pessoal** pode virar AP não autorizado, contornando a segurança.

Proteção: políticas no WLC e software que **monitora o espectro de rádio**.

### 14.4 Gêmeo do Mal

No **gêmeo do mal** (*evil twin*), o atacante cria um AP com **o mesmo SSID de um AP legítimo** e sinal mais forte. É comum em Wi-Fi grátis com autenticação aberta.

1. os clientes veem dois APs com o mesmo SSID;
2. quem está perto do falso se associa a ele;
3. o AP falso captura e repassa o tráfego;
4. o atacante rouba senhas e dados.

Proteção: **autenticar os usuários** e monitorar dispositivos anormais.

### 14.5 Ataques ao Bluetooth

O **Bluetooth** é **de curto alcance e baixa potência**, por isso **o atacante precisa estar perto**:

- **bluejacking**: **envia mensagens não autorizadas**;
- **bluesnarfing**: **copia informações** do alvo, como contatos e e-mails.

### 14.6 Ameaças aos Dispositivos Móveis

- **grayware**: aplicativo indesejado que **se comporta de forma irritante** (rastreia, exibe anúncios), **sem malware reconhecível**;
- **SMiShing**: phishing por SMS.

### 14.7 Fraquezas dos Protocolos Wi-Fi

O **WEP** (*Wired Equivalent Privacy*) tinha falhas graves:

- **não tinha gerenciamento de chaves**;
- seu **vetor de inicialização** (IV) era **pequeno, legível e estático**; o IV é o valor misturado à chave para que cada pacote seja cifrado de um jeito diferente.

O **WPA** e o **WPA2** o substituíram. Com o WPA2, o atacante **não recupera a chave só observando o tráfego**.

## 15. Proteção das Redes sem Fio

Sem segurança rigorosa, uma WLAN é como **espalhar portas de rede até fora do escritório**.

### 15.1 Ocultação do SSID e Filtragem de MAC

- **ocultação do SSID** (*SSID cloaking*): desativa o beacon com o nome da rede;
- **filtragem de MAC**: permite ou nega o acesso pelo MAC do cliente.

**Importante:** esses recursos **não impedem um intruso habilidoso**: o SSID é fácil de descobrir e o MAC pode ser falsificado. A melhor proteção é **autenticação e criptografia**.

### 15.2 Métodos de Autenticação

- **sistema aberto**: **qualquer cliente se conecta, sem senha**; o cliente é o responsável pela segurança (por exemplo, com VPN);
- **chave compartilhada**: senha combinada antes entre cliente e AP.

| Método | Criptografia | Situação |
| --- | --- | --- |
| WEP | **RC4** com **chave estática** | **Nunca usar** |
| WPA | **TKIP**, que **muda a chave a cada pacote** | Substituto temporário |
| WPA2 | **AES** | Padrão atual |
| WPA3 | Exige **quadros de gerenciamento protegidos** (PMF) | Recomendado |

### 15.3 Pessoal e Corporativo

- **pessoal**: **chave pré-compartilhada** (PSK), sem servidor; casas e pequenos escritórios;
- **corporativo** (*Enterprise*): exige um **servidor RADIUS**; usuários autenticados pelo **802.1X** com **EAP**.

### 15.4 Criptografia no WPA e no WPA2

- **TKIP**: usado pelo **WPA**; inclui o **MIC** (*Message Integrity Check*), que detecta alterações;
- **AES**: usado pelo **WPA2**; o **preferido, por ser muito mais forte**; usa o **CCMP**.

### 15.5 Autenticação na Empresa

No AP, configuram-se:

- o **IP do servidor RADIUS**;
- as **portas UDP**: **1812 para autenticação e 1813 para contabilidade**;
- a **chave compartilhada** entre AP e RADIUS.

**Importante:** a chave compartilhada **não é configurada no cliente**; os usuários são autenticados pelo **802.1X**.

### 15.6 WPA3

| Recurso | O que muda |
| --- | --- |
| WPA3-Personal | Usa **SAE** (*Simultaneous Authentication of Equals*); a **PSK nunca é exposta** à força bruta |
| WPA3-Enterprise | Conjunto criptográfico de **192 bits** |
| Redes abertas | **Criptografam todo o tráfego** com o **OWE** (*Opportunistic Wireless Encryption*) |
| Integração de IoT | O **WPS** é vulnerável; o **DPP** (*Device Provisioning Protocol*) conecta dispositivos sem tela por **QR Code** |

### 15.7 Defesa de Redes sem Fio e Móveis

As principais medidas são:

- **trocar as configurações padrão**;
- posicionar os APs fora do firewall ou em uma **DMZ**;
- detectar APs não autorizados com ferramentas como o **NetStumbler**;
- ter uma **política de acesso para convidados**;
- usar **VPN** para acessar a WLAN.

## 16. Dispositivos de Segurança de Rede

A **infraestrutura de segurança de rede** define como os dispositivos são ligados para obter **comunicação segura de ponta a ponta**.

### 16.1 Firewalls

Um **firewall** é **um sistema que aplica uma política de controle de acesso entre redes**. Exemplos de regras:

- negar entrada com **endereços de origem internos**;
- negar pings vindos de fora;
- permitir tráfego externo para os servidores web e de e-mail.

Propriedades de todo firewall:

- **resiste a ataques**;
- é o **único ponto de passagem** entre as redes;
- **aplica a política** de controle de acesso.

| Benefícios | Limitações |
| --- | --- |
| Protege hosts e aplicações de usuários não confiáveis | Mal configurado, vira **ponto único de falha** |
| Bloqueia dados maliciosos | Usuários tentam contorná-lo |
| Concentra o controle de acesso | Pode reduzir o desempenho |
| | Tráfego não autorizado pode passar em túneis |

### 16.2 Arquiteturas de Firewall

- **privado e público**: o que sai da rede privada é permitido; o que **nasce na pública com destino à privada é bloqueado**;
- **DMZ**: interface interna, externa e **DMZ**, onde ficam os servidores acessados de fora;
- **ZPF** (*Zone-Based Policy Firewall*): agrupa interfaces em **zonas**.

| Origem → destino | Tratamento |
| --- | --- |
| Privada → pública ou DMZ | Permitido e inspecionado |
| DMZ → privada | **Bloqueado** |
| DMZ → pública | Permitido seletivamente |
| Pública → DMZ | **Permitido seletivamente** (e-mail, DNS, HTTP, HTTPS) |
| Pública → privada | **Bloqueado** |

No ZPF, **mesma zona passa livremente; zonas diferentes são bloqueadas** até que uma política permita.

### 16.3 Tipos de Firewall

| Tipo | Camadas | Como funciona |
| --- | --- | --- |
| Filtragem de pacotes (**sem estado**) | 3 e 4 | Regras simples com IPs, portas e protocolo |
| **Com estado** (*stateful*) | 3, 4 e 5 | O **mais usado**; usa uma **tabela de estado** |
| Gateway de aplicação (**proxy**) | 3, 4, 5 e 7 | Conecta-se ao servidor **em nome do cliente** |
| NGFW (*Next-Generation Firewall*) | Até a 7 | Prevenção de intrusão e **controle de aplicativos** |

Outras formas:

- **firewall de host**: software no próprio computador;
- **transparente**: invisível, filtra entre duas interfaces em ponte;
- **híbrido**: combina tipos.

### 16.4 IDS e IPS

- **IDS** (*Intrusion Detection System*): **detecta** e alerta;
- **IPS** (*Intrusion Prevention System*): detecta e **bloqueia**.

Os dois são implantados como **sensores** e usam **assinaturas** (regras que reconhecem atividades maliciosas). Detectam padrões **atômicos** (um pacote) ou **compostos** (vários pacotes).

| Solução | Vantagens | Desvantagens |
| --- | --- | --- |
| IDS (fora de linha) | **Não afeta a rede** | **Não impede o pacote que disparou o alerta** |
| IPS (em linha) | **Bloqueia o pacote de gatilho** | Falhas do sensor **afetam a rede**; causa latência (atraso) e *jitter* (variação do atraso) |

**Observação:** IDS e IPS **se complementam**.

### 16.5 Equipamentos de Segurança Especializados

- **AMP** (*Advanced Malware Protection*): protege **antes, durante e depois** de um ataque; continua monitorando os arquivos mesmo depois de liberados;
- **WSA** (*Web Security Appliance*): gateway web que **bloqueia sites arriscados**; não protege quem está fora da rede;
- **CWS** (*Cloud Web Security*): segurança web na nuvem para **funcionários remotos**;
- **ESA** (*Email Security Appliance*): protege o e-mail, bloqueia spam pela **reputação do remetente** e controla as mensagens de saída.

## 17. Serviços de Segurança de Rede

Além dos dispositivos, a infraestrutura usa **serviços** que controlam, monitoram e protegem a transmissão de dados.

### 17.1 Listas de Controle de Acesso

Uma **ACL** é uma **série de comandos que decide se o dispositivo encaminha ou descarta cada pacote**. Usos:

- limitar o tráfego;
- restringir atualizações de roteamento;
- dar **segurança básica** entre partes da rede;
- filtrar por tipo de tráfego.

| Tipo | O que filtra |
| --- | --- |
| Padrão | **Só o IP de origem** |
| Estendida | Protocolo, IPs de origem e destino e portas |

As ACLs podem **permitir só tráfego TCP de sessões já estabelecidas** (bits ACK ou RST), bloqueando conexões iniciadas de fora.

### 17.2 SNMP

O **SNMP** (*Simple Network Management Protocol*) **gerencia e monitora** os dispositivos da rede. Elementos:

- **gerenciador SNMP**: parte do **NMS** (*Network Management System*);
- **agentes SNMP**: os dispositivos monitorados.

A **MIB** (*Management Information Base*) é o **banco de dados do agente**. O gerenciador:

- **get**: obtém informações;
- **set**: altera configurações;
- **traps**: recebe avisos espontâneos dos agentes.

### 17.3 NetFlow

O **NetFlow** fornece **estatísticas dos fluxos de pacotes IP** a um **coletor**. Serve para monitoramento, segurança e planejamento.

Um fluxo é identificado por **sete campos**: IPs de origem e destino, portas de origem e destino, protocolo, **ToS** (prioridade) e interface de entrada.

### 17.4 Espelhamento de Portas

O switch **isola o tráfego**, e um sniffer ou IDS não vê tudo.

O **espelhamento de portas** (*port mirroring*) faz o switch **copiar o tráfego** para a porta do monitor.

### 17.5 Syslog e NTP

O **syslog** **envia as mensagens de sistema dos dispositivos a um servidor central**.

Sem relógios sincronizados, é **impossível saber a ordem dos eventos**. O **NTP** sincroniza os relógios por uma hierarquia de **estratos**:

| Estrato | Quem é |
| --- | --- |
| 0 | Fontes de tempo de alta precisão |
| 1 | Ligados diretamente ao estrato 0 |
| 2 em diante | Sincronizam com o estrato acima |
| 16 | **Não sincronizado** |

**Quanto menor o estrato, mais perto da fonte oficial.** O máximo é **15 saltos**.

### 17.6 Servidores AAA

Os **servidores AAA** controlam o acesso de forma centralizada:

- **autenticação**: **provar quem é**;
- **autorização**: **o que pode acessar e fazer**;
- **contabilidade**: **registrar o que fez**.

O **TACACS+** é **considerado mais seguro**, porque **criptografa toda a troca**; o **RADIUS** criptografa **só a senha**.

| Característica | TACACS+ | RADIUS |
| --- | --- | --- |
| Funcionalidade | Separa as três funções | Junta autenticação e autorização |
| Padrão | Principalmente Cisco | Aberto |
| Transporte | **TCP** | **UDP** |
| Confidencialidade | **Pacote inteiro** | **Só a senha** |
| Autorização de comandos | Sim | Não |
| Contabilidade | Limitada | Abrangente |

### 17.7 VPN

Uma **VPN** é uma **rede privada criada sobre uma rede pública**:

- **virtual**: usa uma rede pública;
- **privada**: o tráfego é **criptografado**.

O **GRE** (*Generic Routing Encapsulation*) cria túneis **sem criptografia**.

O **IPsec** (*IP Security*) oferece **autenticação, integridade, controle de acesso e confidencialidade**. Topologias:

- **site a site**: liga a matriz às filiais;
- **acesso remoto**: para quem trabalha fora.

## 18. O Sistema Operacional Windows

Para proteger um computador Windows (um **endpoint**, dispositivo final da rede), é preciso entender como ele funciona.

### 18.1 Do MS-DOS ao Windows NT

O **MS-DOS** era um sistema operado por **linha de comando**, de um processo e um usuário só. As primeiras versões do Windows eram só uma interface gráfica sobre ele.

O Windows moderno é baseado no **Windows NT**, que **controla diretamente o hardware** e aceita **vários processos e usuários**.

A janela de comando (**cmd**) aceita comandos como:

| Comando | Função |
| --- | --- |
| `dir` | Lista os arquivos da pasta |
| `cd pasta` | Entra na pasta |
| `cd ..` | Sobe uma pasta |
| `copy` | Copia arquivos |
| `del` | Apaga arquivos |
| `mkdir` | Cria uma pasta |
| `ren` | Renomeia |
| `help` | Lista os comandos |

### 18.2 Versões do Windows

Há edições para estações de trabalho, servidores e data centers.

| Arquitetura | Memória RAM endereçável |
| --- | --- |
| 32 bits | Pouco menos de 4 GB |
| 64 bits | Em teoria, 16,8 milhões de TB |

**Importante:** sistemas de 64 bits rodam programas de 32 bits, mas **programas de 64 bits não rodam em hardware de 32 bits**.

A Microsoft trata o **Windows 10 como um serviço**, atualizado continuamente.

### 18.3 Interface Gráfica

A **GUI** (*Graphical User Interface*) tem a **área de trabalho**, a **lixeira** e a **barra de tarefas**, com o menu Iniciar, ícones de inicialização rápida e a **área de notificação**. O clique direito abre o **menu de contexto**. Pastas e arquivos ficam no **Explorador de Arquivos**.

### 18.4 Vulnerabilidades do Sistema Operacional

Os sistemas têm **milhões de linhas de código**, e com elas vêm vulnerabilidades. As recomendações de segurança do Windows são:

| Área | Recomendação |
| --- | --- |
| Antimalware | Manter o **Windows Defender** ativo |
| Serviços | Cada serviço em segundo plano deve ser identificável e seguro |
| Criptografia | Criptografar os dados, principalmente em portáteis |
| Política de segurança | Configurar e seguir uma boa política |
| Firewall | Revisar as regras e remover as desnecessárias |
| Permissões | **Permissões mínimas necessárias**, nunca "Controle Total" para "Todos" |
| Senhas | Senhas fortes, principalmente na conta **Administrador** |
| Login | Entrar como **usuário padrão** e usar o administrador só quando preciso |

## 19. Arquitetura e Funcionamento do Windows

A arquitetura do Windows isola o sistema operacional das diferenças de hardware.

### 19.1 Camadas da Arquitetura

Aplicativos → API do Windows → Kernel e drivers → HAL → Hardware

- **kernel**: o **núcleo do sistema operacional**, que controla todo o computador;
- **HAL** (*Hardware Abstraction Layer*): **cuida da comunicação entre o hardware e o kernel**;
- **drivers**: permitem ao sistema falar com cada dispositivo.

![Arquitetura do Windows: aplicativos em modo usuário, kernel e HAL em modo kernel, sobre o hardware](img/endpoint/end_wincamadas.png){width=6in}

### 19.2 Modo Usuário e Modo Kernel

| Característica | Modo usuário | Modo kernel |
| --- | --- | --- |
| O que roda | Aplicativos | Sistema operacional e alguns drivers |
| Acesso ao hardware | Só pelo sistema operacional | Irrestrito |
| Espaço de endereços | Privado para cada processo | Compartilhado |
| Efeito de uma falha | Só no aplicativo | Para todo o computador |

### 19.3 Sistemas de Arquivos

Antes de ser usado, o disco é **particionado e formatado** com um sistema de arquivos:

| Sistema | Características |
| --- | --- |
| FAT32 e exFAT | Simples; comuns em pen drives; no FAT32, arquivo de no máximo 4 GB |
| HFS+ | **macOS** |
| EXT | **Linux** |
| NTFS | **O padrão do Windows** |

O **NTFS** é o preferido porque:

- aceita arquivos e partições muito grandes;
- tem recursos de recuperação;
- controla o acesso com **permissões até o nível do arquivo**;
- registra os carimbos de hora **MACE** (modificado, acessado, criado, entrada modificada), usados em **investigações forenses**;
- permite **criptografar o sistema de arquivos**.

A **MFT** (*Master File Table*) guarda a localização e os atributos de todos os arquivos.

**Importante:** formatar **não apaga tudo**. Em discos reutilizados, é preciso um **apagamento seguro**.

### 19.4 Fluxos de Dados Alternativos

O conteúdo do arquivo NTFS fica no atributo **\$DATA**. Os **fluxos de dados alternativos** (**ADS**, *Alternate Data Streams*) anexam dados extras ao arquivo.

**Importante:** o ADS é **fácil de usar para esconder código malicioso**.

Exemplo:

1. `echo "texto" > Testfile.txt:ADS` grava um ADS;
2. `dir` mostra o arquivo com **0 byte**;
3. `dir /r` revela o fluxo escondido.

### 19.5 Processo de Inicialização

Há dois tipos de **firmware** (software da placa-mãe):

- **BIOS** (*Basic Input-Output System*): antigo;
- **UEFI** (*Unified Extensible Firmware Interface*): substituto do BIOS, **mais seguro** na inicialização.

De forma simplificada:

1. o BIOS faz o **POST** (teste dos dispositivos) e lê o **MBR** (o primeiro setor do disco, que aponta onde está o sistema); o UEFI carrega os arquivos **.efi** da partição **ESP** (partição de sistema EFI);
2. o **Bootmgr.exe** lê o **BCD** (configuração de inicialização);
3. se estava hibernando, o **Winresume.exe** restaura o estado;
4. senão, o **Winload.exe** usa a **KMCS** (*Kernel-Mode Code Signing*, assinatura de código do kernel) para garantir que **todos os drivers tenham assinatura digital**;
5. o **Ntoskrnl.exe** inicia o kernel;
6. o **SMSS** prepara o ambiente do usuário e o logon.

BIOS/UEFI → Bootmgr.exe → BCD → Winload.exe → Ntoskrnl.exe → SMSS → Logon

![Sequência de inicialização do Windows, do firmware ao logon](img/endpoint/end_boot.png){width=6in}

### 19.6 Programas que Iniciam com o Windows

Duas chaves do registro iniciam programas automaticamente:

- **HKEY\_LOCAL\_MACHINE**: a cada inicialização do computador;
- **HKEY\_CURRENT\_USER**: quando o usuário faz logon.

O **Msconfig.exe** (Configuração do Sistema) controla a inicialização: normal, de diagnóstico, seletiva e **inicialização segura**.

### 19.7 Desligamento

**Desligar corretamente** evita danos a arquivos e serviços. O sistema fecha primeiro o modo usuário e depois o modo kernel. Opções: desligar, reiniciar e **hibernar** (grava o estado em arquivo).

### 19.8 Processos, Threads e Serviços

- **processo**: **um programa em execução**;
- **thread**: **a parte do processo que a CPU executa**;
- **serviço**: processo que **roda em segundo plano**.

Os processos são vistos no **Gerenciador de Tarefas**, e os serviços no painel **Serviços**.

### 19.9 Memória e Identificadores

Cada processo usa um **espaço de endereços virtuais**, traduzido para endereços físicos.

| Windows | Espaço virtual por processo |
| --- | --- |
| 32 bits | Até 4 GB |
| 64 bits | 8 TB |

O processo usa um **identificador** (*handle*) para acessar recursos do kernel sem ligação direta. A ferramenta **RAMMap** mostra o uso da memória.

### 19.10 Registro do Windows

O **registro** é um **banco de dados hierárquico** com todas as configurações: ramo → chave → subchave → valores. É editado com o **regedit.exe**.

| Ramo | Conteúdo |
| --- | --- |
| HKEY\_CURRENT\_USER (HKCU) | Usuário conectado |
| HKEY\_USERS (HKU) | Todas as contas |
| HKEY\_CLASSES\_ROOT (HKCR) | Tipos de arquivo e qual programa abre cada um (registros OLE) |
| HKEY\_LOCAL\_MACHINE (HKLM) | Informações do sistema |
| HKEY\_CURRENT\_CONFIG (HKCC) | Perfil de hardware atual |

Tipos de valor: **REG\_BINARY** (binário), **REG\_DWORD** (número de 32 bits) e **REG\_SZ** (texto).

**Importante:** não é possível criar ramos novos, e pequenas mudanças podem ter efeitos catastróficos.

Para a segurança:

- **persistência de malware**: malware cria chaves para **iniciar com o computador**; é preciso revisar os locais de inicialização;
- **forense**: o registro guarda os dispositivos conectados e os documentos abertos.

## 20. Configuração e Monitoramento do Windows

Este módulo mostra como configurar o Windows com segurança e acompanhar o que acontece nele.

### 20.1 Executar como Administrador

**Não é recomendável entrar com a conta de Administrador**: todo programa herda esses privilégios, e um malware ganha **acesso total**.

Quando preciso, usar:

- botão direito → **Executar como administrador**;
- um **prompt de comando de administrador**.

### 20.2 Usuários Locais, Grupos e Domínios

As contas **Convidado** e **Administrador** vêm **desabilitadas por padrão** e devem continuar assim.

Os **grupos** reúnem permissões; o usuário as recebe ao entrar no grupo. Quando há conflito, **"negar explicitamente" prevalece**. Usuários e grupos locais ficam no **lusrmgr.msc**.

Um **domínio** guarda **usuários, grupos, computadores e configurações em um banco central**, nos **controladores de domínio** (**DCs**). As configurações do DC **prevalecem sobre as locais**.

### 20.3 Linha de Comando e PowerShell

A **CLI** (*Command-Line Interface*) do Windows é o **cmd.exe**. Regras:

- **não diferencia maiúsculas de minúsculas**;
- caminhos usam barra invertida: `C:\Users\Jim\Desktop\file.txt`;
- opções usam a barra (/);
- **Tab** completa nomes; as setas acessam o histórico.

O **PowerShell** **automatiza tarefas com scripts** e interage com o núcleo do Windows. Executa:

- **cmdlets**: comandos que passam objetos ao próximo;
- **scripts**: arquivos **.ps1**;
- **funções**.

Ajuda: `get-help comando`, com `-examples`, `-detailed` ou `-full`.

### 20.4 WMI e o Comando net

A **WMI** (*Windows Management Instrumentation*) **gerencia computadores remotos**.

**Importante:** atacantes usam a WMI porque ela **escapa da detecção** e quase não deixa rastros. O acesso deve ser **muito restrito**.

| Comando | Função |
| --- | --- |
| `net accounts` | Requisitos de senha e logon |
| `net session` | Sessões com outros computadores |
| `net share` | Compartilhamentos |
| `net start` / `net stop` | Inicia ou para serviços |
| `net use` | Conecta a recursos compartilhados |
| `net view` | Lista os computadores da rede |

### 20.5 Gerenciador de Tarefas e Monitor de Recursos

São **especialmente úteis quando se suspeita de malware**.

| Guia do Gerenciador de Tarefas | O que mostra |
| --- | --- |
| Processos | Programas em execução e uso de recursos |
| Desempenho | CPU, memória, disco e rede |
| Histórico de aplicativos | Uso de recursos ao longo do tempo |
| Inicializar | Programas que iniciam com o computador |
| Usuários | Usuários conectados |
| Detalhes | Prioridade e afinidade de CPU |
| Serviços | Serviços com **PID** e estado |

O **Monitor de Recursos** é mais detalhado. A guia **Rede** mostra **conexões TCP atuais e portas em escuta**, o que revela processos não autorizados acessando a rede.

### 20.6 Rede no Windows

O **Centro de Rede e Compartilhamento** mostra se a rede é **privada, pública ou de convidados** e permite configurar os adaptadores.

Comandos de teste:

- **nslookup**: testa o DNS;
- **netstat**: mostra as **conexões ativas** e as portas abertas.

### 20.7 Compartilhamentos e Área de Trabalho Remota

O **SMB** (*Server Message Block*) **compartilha arquivos e recursos de rede**, usando o formato **UNC**:

`\\servidor\compartilhamento\arquivo`

Os **compartilhamentos administrativos** terminam em **cifrão** (`$`): `C$`, `admin$`, `print$`. **Só administradores** os acessam.

O **RDP** (*Remote Desktop Protocol*) **controla um host remoto como se fosse local**.

**Importante:** o RDP é **alvo natural dos atacantes**. É preciso **limitar sua exposição à internet** e mantê-lo atualizado.

### 20.8 Windows Server

O **Windows Server** é a edição para **data centers**. Oferece:

- serviços de rede: DNS, DHCP, Hyper-V;
- serviços de arquivo: SMB, NFS, DFS;
- serviços web: FTP, HTTP, HTTPS;
- gerenciamento: Política de Grupo e **Active Directory**.

## 21. Segurança do Windows

O Windows tem ferramentas próprias para encontrar sinais de ataque e proteger o computador.

### 21.1 O Comando netstat

O malware costuma **abrir portas de comunicação**. O **netstat** procura **conexões de entrada ou de saída não autorizadas**.

O comando **netstat -abno** (como administrador) **liga cada conexão ao processo e ao PID**.

Como vários processos podem ter o mesmo nome, usa-se o **PID**, que é **único para cada processo**.

### 21.2 Visualizador de Eventos

O **Visualizador de Eventos** registra o **histórico de eventos de aplicativos, segurança e sistema**. Cada evento tem:

- **nível**: informação, aviso, erro ou crítico;
- data e hora;
- origem;
- **ID de evento**.

A exibição **Eventos Administrativos** reúne os eventos críticos, de erro e de aviso e é um bom ponto de partida.

### 21.3 Atualizações do Windows

- **patches** (correções): impedem que falhas recém-descobertas sejam exploradas;
- **service pack**: pacote com várias correções.

As empresas devem **distribuir e instalar as atualizações automaticamente**. O **Windows Update** instala as atualizações e permite definir horários em que o computador não reinicia sozinho.

### 21.4 Política de Segurança Local

Em domínios, vale a **Política de Segurança de Domínio**. Em **computadores autônomos**, a **Política de Segurança Local**, que define:

- **política de senha**;
- **bloqueio de conta**: impede **força bruta**; exemplo: cinco tentativas erradas bloqueiam por 30 minutos;
- bloqueio ao iniciar a proteção de tela;
- direitos de usuário e regras de firewall;
- **AppLocker**: restringe os programas que cada usuário pode executar.

A política pode ser **exportada e importada** em outros computadores.

### 21.5 Windows Defender

| Proteção | Função |
| --- | --- |
| Antivírus | Monitora continuamente e coloca vírus em **quarentena** |
| Contra adware | Programas que exibem publicidade |
| Contra phishing | Bloqueia sites de phishing |
| Contra spyware | Keyloggers e outros espiões |
| Fontes não confiáveis | Avisa antes de instalar programas inseguros |

**Importante:** **só um programa antimalware deve rodar por vez**.

O **Windows Defender** vem **ativado por padrão**, com proteção em tempo real.

### 21.6 Firewall do Windows Defender

O firewall **abre e fecha as portas** usadas pelos aplicativos. Há duas abordagens:

- **restritiva**: **só as portas necessárias ficam abertas**;
- **permissiva**: **tudo é permitido**, menos o explicitamente negado.

Hoje, a maioria dos equipamentos vem **o mais restritiva possível**.

Nas **Configurações avançadas**, criam-se regras de entrada e de saída.

## 22. Fundamentos do Linux

O **Linux** é um sistema operacional **de código aberto**, rápido e muito personalizável, feito para funcionar em rede.

### 22.1 O que é o Linux

O Linux foi criado em **1991** e é mantido por **uma comunidade de programadores**. Exige **poucos recursos de hardware** e roda de relógios a supercomputadores.

Qualquer pessoa pode obter, modificar e redistribuir o código-fonte do **kernel**.

Uma **distribuição** (*distro*) reúne o kernel com ferramentas e programas próprios. Exemplos: **Debian, Red Hat, Ubuntu, CentOS e SUSE**.

### 22.2 O Valor do Linux para a Segurança

O Linux é muito usado no **SOC** (*Security Operations Center* — centro de operações de segurança) porque:

- **é de código aberto** e pode ser adaptado;
- sua **CLI é muito poderosa** e funciona remotamente;
- **dá mais controle ao usuário**: o **root** (superusuário) tem **poder absoluto**;
- controla melhor a comunicação de rede; muitas ferramentas de rede só existem para Linux.

### 22.3 Ferramentas do SOC e de Teste de Penetração

| Ferramenta | Função |
| --- | --- |
| Captura de pacotes | Observar cada detalhe do tráfego; exemplo: Wireshark |
| Análise de malware | Executar o malware **com segurança** |
| IDS | Inspecionar o tráfego em tempo real |
| Firewalls | Permitir ou negar tráfego por regras |
| Gerenciadores de logs | Acompanhar muitos registros |
| SIEM | Analisar alertas e logs **em tempo real** |
| Sistemas de tíquetes | Atribuir e registrar tarefas |

O **Security Onion** reúne ferramentas abertas de análise de segurança.

O **teste de penetração** (*pentest*) **procura vulnerabilidades atacando a rede ou o computador**. O **Kali Linux** reúne muitas ferramentas de pentest.

### 22.4 O Shell do Linux

Para usar a CLI na interface gráfica, abre-se um **emulador de terminal**. Os termos **shell, console** e **terminal** costumam ser sinônimos.

Os comandos são programas procurados no **caminho** (*path*). O comando **man** mostra o manual de um comando.

| Comando | Função |
| --- | --- |
| `ls` | Lista os arquivos |
| `cd` | Muda de diretório |
| `pwd` | Mostra o diretório atual |
| `mkdir` | Cria um diretório |
| `cp` / `mv` / `rm` | Copia / move ou renomeia / remove |
| `cat` | Mostra o conteúdo de um arquivo |
| `chmod` | Altera as permissões |
| `chown` | Altera o dono |
| `ps` | Lista os processos |
| `su` | Entra como outro usuário |
| `sudo` | Executa um comando como superusuário |
| `grep` | Procura textos, inclusive na saída de outro comando (*pipe*, \|) |
| `ip address` | Mostra a placa de rede (substitui o `ifconfig`) |
| `apt-get` | Instala e remove pacotes no Debian |
| `passwd` | Altera a senha |
| `shutdown` | Desliga ou reinicia |

### 22.5 Arquivos de Texto e de Configuração

Os editores de linha de comando, como o **nano**, são essenciais para **editar arquivos em um computador remoto** por **SSH**.

**Importante:** no Linux, **tudo é tratado como arquivo**: memória, discos, monitor e diretórios.

O sistema é configurado por **arquivos de configuração** de texto. Exemplo: **/etc/hosts** associa nomes a IPs; só o superusuário o altera (`sudo nano /etc/hosts`).

### 22.6 Clientes, Servidores e Portas

Os **servidores** **fornecem serviços aos clientes pela rede**. Cada serviço **escuta em uma porta**:

| Porta | Serviço |
| --- | --- |
| 20/21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 67/68 | DHCP |
| 69 | TFTP |
| 80 | HTTP |
| 110 | POP3 |
| 123 | NTP |
| 143 | IMAP |
| 161/162 | SNMP |
| 443 | HTTPS |

Os **clientes** são programas que **falam com um tipo de servidor**, como o navegador com o servidor web.

## 23. Administração de Servidores Linux

Administrar um servidor Linux é cuidar dos arquivos de configuração, reforçar a segurança e acompanhar os logs.

### 23.1 Arquivos de Configuração dos Serviços

Os serviços são configurados por arquivos com opções como porta e regras de acesso. Uma alteração **costuma exigir reiniciar o serviço**. Exemplos:

- **/etc/nginx/nginx.conf**: servidor web **Nginx**;
- **/etc/ntp.conf**: NTP;
- **/etc/snort/snort.conf**: IDS **Snort**; `ipvar HOME_NET` define a rede protegida.

É comum o formato **opção = valor**, e o **#** indica comentário.

### 23.2 Endurecimento de Dispositivos

O **endurecimento** (*hardening*) é **aplicar métodos comprovados para proteger o dispositivo e seu acesso administrativo**. As boas práticas são:

- garantir a segurança física;
- **minimizar os pacotes instalados**;
- **desativar os serviços não usados**;
- usar SSH e **desabilitar o login do root por SSH**;
- manter o sistema atualizado;
- **desativar a detecção automática de USB**;
- exigir senhas fortes, com troca periódica e sem reutilização.

### 23.3 Logs do Linux

Os **logs** registram os eventos do kernel, dos serviços e dos aplicativos. Revisá-los mostra **desempenho, segurança e problemas**.

Os **daemons** são processos que **rodam em segundo plano sem interação do usuário**.

| Arquivo | Conteúdo |
| --- | --- |
| /var/log/messages | Atividade geral (no Debian, **/var/log/syslog**) |
| /var/log/auth.log | **Eventos de autenticação** no Debian e Ubuntu |
| /var/log/secure | Equivalente do auth.log no Red Hat e CentOS |
| /var/log/boot.log | Inicialização |
| /var/log/dmesg | Mensagens do kernel sobre hardware e drivers |
| /var/log/kern.log | Informações do kernel |
| /var/log/cron | **Tarefas agendadas** |
| /var/log/mysqld.log | Banco de dados MySQL |

Cada linha é um evento, com **carimbo de data e hora** no início.

## 24. Sistema de Arquivos e Permissões do Linux

Como no Linux tudo é arquivo, o sistema de arquivos e as permissões são a base da sua segurança.

### 24.1 Tipos de Sistemas de Arquivos

| Sistema | Características |
| --- | --- |
| ext2 | **Sem diário**; ainda usado em memória flash |
| ext3 | Acrescenta o **diário** (*journaling*) |
| ext4 | Sucessor do ext3, com melhor desempenho |
| NFS (*Network File System*) | Sistema **em rede** |
| CDFS | Discos ópticos |
| Swap | Partição usada quando **falta RAM** |
| HFS+ | Apple (antigo) |
| APFS | Apple atual, com **criptografia forte** |

O **diário** registra as alterações **antes de fazê-las**, o que permite recuperar o sistema após uma falha.

### 24.2 Montagem

**Montar** é **associar um diretório a uma partição**, o **ponto de montagem**. O **sistema de arquivos raiz** é **/**. O comando **mount** lista os sistemas montados.

### 24.3 Permissões de Arquivos

Cada arquivo tem permissões para **o dono (usuário), o grupo e os outros**: **ler (r), gravar (w) e executar (x)**. O comando **ls -l** as mostra:

`-rwxrw-r-- 1 analyst staff 253 May 20 12:49 space.txt`

| Campo | Valor | Significado |
| --- | --- | --- |
| 1 | -rwxrw-r-- | Tipo e permissões |
| 2 | 1 | Número de links rígidos |
| 3 | analyst | Usuário dono |
| 4 | staff | Grupo dono |
| 5 | 253 | Tamanho em bytes |
| 6 | May 20 12:49 | Última modificação |
| 7 | space.txt | Nome |

- primeiro caractere: **-** arquivo, **d** diretório;
- **rwx**: o dono lê, grava e executa;
- **rw-**: o grupo lê e grava;
- **r--**: os outros só leem.

Em octal, **r=4, w=2, x=1**:

| Binário | Octal | Permissão |
| --- | --- | --- |
| 000 | 0 | --- |
| 001 | 1 | --x |
| 010 | 2 | -w- |
| 011 | 3 | -wx |
| 100 | 4 | r-- |
| 101 | 5 | r-x |
| 110 | 6 | rw- |
| 111 | 7 | rwx |

#### 24.3.1 Exemplo Resolvido: Permissão em Octal

| Conjunto | Permissão | Soma | Octal |
| --- | --- | --- | --- |
| Usuário | rwx | 4 + 2 + 1 | 7 |
| Grupo | rw- | 4 + 2 + 0 | 6 |
| Outros | r-- | 4 + 0 + 0 | 4 |

A permissão é **764**: `chmod 764 space.txt`.

**Importante:** **só o root pode ignorar as permissões**; por isso tem controle total, e sua senha deve ser forte e não compartilhada.

### 24.4 Links Rígidos e Simbólicos

- **link rígido** (`ln`): **outro nome para o mesmo inode** (a ficha do arquivo); apagar um não apaga o arquivo;
- **link simbólico** (`ln -s`): **aponta para o nome do arquivo**; se o original for apagado, fica quebrado.

| Característica | Link rígido | Link simbólico |
| --- | --- | --- |
| Aponta para | O mesmo inode | O nome do arquivo |
| Se o original for apagado | Continua funcionando | Fica quebrado |
| Outro sistema de arquivos | Não | Sim |
| Diretórios | Não | Sim |
| Comando | `ln` | `ln -s` |

### 24.5 Interface Gráfica do Linux

A GUI se baseia no **X Window System** (X11), que funciona como **servidor**: um aplicativo pode rodar no servidor e aparecer em outro computador.

A aparência fica com os **gerenciadores de janelas**, como **Gnome** e **KDE**. O sistema funciona sem a GUI.

O **Ubuntu** usa o **Gnome**, com menu Aplicativos, **Dock**, barra superior, **Atividades** e menu de status.

## 25. Trabalho em um Host Linux

No dia a dia, administrar um host Linux é instalar e atualizar programas, controlar processos e procurar sinais de comprometimento.

### 25.1 Gerenciadores de Pacotes

Um **pacote** é **um programa com todos os seus arquivos de apoio**. O **gerenciador de pacotes** instala cada arquivo no lugar certo: **pacman** (Arch), **dpkg** e **apt** (Debian e Ubuntu).

- `apt-get update`: **baixa a lista de pacotes** do repositório;
- `apt-get upgrade`: **atualiza todos os pacotes instalados**.

### 25.2 Manter o Sistema Atualizado

As **atualizações** (*patches*) corrigem vulnerabilidades conhecidas. Podem sair **fora do calendário** quando uma falha importante é descoberta.

| Tarefa | Arch | Debian/Ubuntu |
| --- | --- | --- |
| Instalar um pacote | `pacman -S` | `apt install` |
| Remover um pacote | `pacman -Rs` | `apt remove` |
| Atualizar a lista | `pacman -Syy` | `apt-get update` |
| Atualizar todos | `pacman -Syu` | `apt-get upgrade` |

### 25.3 Processos e Bifurcação

Um **processo** é **uma instância em execução de um programa**.

A **bifurcação** (*fork*) permite que **um processo crie uma cópia de si mesmo**; é **a única forma de criar processos no Linux**. O original é o **pai**, e a cópia, o **filho**, com **PIDs diferentes e o mesmo código**.

| Comando | Função |
| --- | --- |
| `ps` | Lista os processos no momento |
| `top` | Lista os processos **de forma dinâmica** |
| `kill` | Encerra, reinicia ou pausa um processo pelo **PID** |

**Observação:** encerrar processos de outros usuários **exige root**.

### 25.4 Malware no Linux

O Linux é considerado **mais protegido**, mas **não é imune**. Por ser aberto, as correções costumam sair **em poucas horas**.

Um vetor comum são os **serviços expostos na rede** com versões desatualizadas. Exemplo: `telnet 209.165.200.224 80` revela `Server: nginx/1.12.0`, e o atacante procura falhas dessa versão.

As defesas são **manter o sistema atualizado** e **fechar serviços e portas não usados**.

### 25.5 Detecção de Rootkits

Um **rootkit** **altera o kernel** para esconder a intrusão e **adultera as ferramentas de diagnóstico**. A maioria **exige acesso root**.

Detecção:

1. iniciar o computador por uma **mídia confiável**;
2. montar o disco comprometido;
3. inspecioná-lo com ferramentas confiáveis.

Quando o rootkit está no kernel, a única solução real é **reinstalar o sistema**; rootkits de firmware podem exigir **troca de hardware**.

O **chkrootkit** procura rootkits conhecidos.

**Importante:** os verificadores de rootkit **não são 100% confiáveis**.

### 25.6 Encadeamento de Comandos

O **pipe** (**|**) **leva a saída de um comando para a entrada de outro**. Exemplo: `ls -l | grep host` mostra só as linhas com "host".

ls -l → | → grep host → Linhas filtradas

## 26. Defesa de Sistemas e Dispositivos

Um **endpoint** é **qualquer host da rede que acessa ou é acessado por outros**: computadores, servidores, impressoras, telefones IP e dispositivos IoT.

### 26.1 Segurança do Sistema Operacional

O administrador:

- **remove programas e serviços desnecessários**;
- **instala a tempo as correções**, seguindo um **plano documentado**;
- define uma **linha de base** (*baseline*) e compara o desempenho com ela.

### 26.2 Cuidados com Malware

- **antivírus falsos** (*rogue antivirus*): janelas que dizem que o computador está infectado; clicar pode **instalar malware**;
- **malware sem arquivo** (*fileless*): vai **direto para a memória**, sem arquivos, e **não deixa rastros**; some ao reiniciar; usa o **PowerShell**;
- **scripts maliciosos**: Python, Bash e **VBA** (macros);
- **software não aprovado**: viola a política e **deve ser removido imediatamente**.

### 26.3 Gerenciamento de Patches

É boa prática **testar um patch antes de distribuí-lo**. Um **serviço de patches automático** permite:

- **aprovar ou recusar** atualizações;
- forçar a atualização até uma data;
- obter relatórios;
- baixar de um **servidor local**;
- **impedir que os usuários contornem** as atualizações.

Também é preciso atualizar **aplicativos de terceiros**, como Adobe, Java e Chrome.

### 26.4 Ferramentas de Segurança do Endpoint

| Ferramenta | Função |
| --- | --- |
| Firewall de host | Filtra o tráfego de entrada e saída do dispositivo |
| HIDS (*Host-based IDS*) | Monitora o sistema e os processos do host; consome muitos recursos |
| HIPS | Monitora chamadas de sistema, arquivos e registro e pode bloquear |
| EDR (*Endpoint Detection and Response*) | **Monitora continuamente, encontra e responde** às ameaças |
| DLP | Impede a perda de dados confidenciais |
| NGFW | Firewall com **inspeção profunda de pacotes** (**DPI**) |

**Importante:** o antivírus só bloqueia; o EDR também **encontra** ameaças no dispositivo.

### 26.5 Criptografia do Host

- **EFS** (*Encrypting File System*): criptografa **arquivos e pastas** no Windows;
- **FDE** (*Full Disk Encryption*): criptografa **todo o disco**; no Windows, pelo **BitLocker**;
- **TPM** (*Trusted Platform Module*): **chip da placa-mãe** que guarda chaves e certificados; ativado no BIOS antes do BitLocker;
- **BitLocker To Go**: criptografa **unidades removíveis**;
- **unidade de autocriptografia**: criptografa tudo automaticamente.

### 26.6 Integridade da Inicialização

A **integridade da inicialização** garante que **o sistema não foi alterado enquanto carrega**.

- **inicialização segura** (*Secure Boot*): o firmware **verifica a assinatura** de cada parte da inicialização;
- **inicialização medida** (*Measured Boot*): **mede cada componente** e guarda as medidas no TPM, para verificação remota.

**Observação:** a **UEFI** é preferível ao BIOS.

### 26.7 Recursos de Segurança da Apple

| Recurso | Função |
| --- | --- |
| Secure Enclave | Chip de segurança com criptografia dedicada |
| FileVault | Criptografa o disco do Mac |
| Inicialização segura | Só roda o sistema genuíno |
| Biometria | Processada separada do sistema |
| Encontre meu Mac | Localiza, bloqueia e apaga remotamente |
| XProtect | Antimalware **por assinatura** |
| MRT (*Malware Removal Tool*) | Remove infecções |
| Gatekeeper | Só instala software **assinado** por desenvolvedor autenticado |

### 26.8 Proteção Física dos Dispositivos

- **travas de cabo**;
- salas de equipamentos trancadas;
- **gaiolas de Faraday**: **bloqueiam campos eletromagnéticos**.

A **fechadura cifrada** abre com código e **registra quando a porta foi aberta e com qual código**.

A **RFID** **identifica e rastreia objetos** por ondas de rádio, sem bateria nas etiquetas.

## 27. Proteção Antimalware

Cada endpoint é uma possível porta de entrada. Um dispositivo que acessa a VPN a partir de uma rede pública pode **injetar malware** na empresa.

### 27.1 Ameaças aos Endpoints

Alguns números citados no curso:

- previsão de **ransomware a cada 11 segundos** em 2021;
- 8% a 10% do spam era malicioso;
- vários malwares **mudam suas características em menos de 24 horas** para escapar da detecção.

### 27.2 Segurança do Perímetro e da LAN

O **perímetro** é protegido por roteador com VPN, NGFW, IPS e servidor AAA.

**Importante:** muitos ataques **vêm de dentro da rede**. Um host interno invadido vira **ponto de partida** para outros alvos. É preciso proteger:

- **endpoints**: notebooks, servidores, impressoras, telefones IP;
- **infraestrutura**: switches e dispositivos sem fio, sujeitos a falsificação, ataques DHCP e ataques ao **STP**.

### 27.3 Proteção Baseada em Host

- **antivírus/antimalware**, com três formas de detecção:
  - **por assinatura**: **malware conhecido**;
  - **heurística**: **características gerais** de malware;
  - **por comportamento**: **comportamentos suspeitos**;
- **firewall de host**: só permite conexões **iniciadas pelo próprio host**; exemplos: Firewall do Windows, **iptables** e **TCP Wrappers** no Linux;
- **pacotes de segurança de host**: reúnem antivírus, antiphishing, HIPS e firewall.

| Antivírus | Como funciona |
| --- | --- |
| Baseado em agente | Roda **em cada máquina** |
| Sem agente | Varreduras **a partir de um sistema central**; comum em ambientes virtualizados |

### 27.4 Proteção Baseada em Rede

Elementos da rede oferecem **mais camadas** e **compartilham informações**:

- **AMP**: proteção contra malware;
- **ESA**: filtra e-mails maliciosos;
- **WSA**: filtra sites;
- **NAC** (*Network Admission Control*): só deixa entrar **sistemas autorizados e em conformidade**.

## 28. Prevenção de Intrusão Baseada em Host

Além do antimalware, o host conta com **firewalls próprios e sistemas que detectam e impedem intrusões**.

### 28.1 IPS de Host e IPS de Rede

- **HIPS** (*Host-based IPS*): software no host que **bloqueia comportamentos fora do normal**, como alterações no registro e estouros de buffer; funciona como **antivírus, antimalware e firewall juntos**;
- **IPS de rede**: **sensores em pontos da rede** que detectam e reagem em tempo real.

| HIPS | |
| --- | --- |
| Vantagens | Proteção específica do host; **protege depois que a mensagem é descriptografada** |
| Desvantagens | Depende do sistema operacional; **precisa ser instalado em todos os hosts**; só tem visão local |

### 28.2 Firewalls de Host

Os **firewalls de host** **controlam o tráfego que entra e sai do computador**, usando **perfis** ou regras por endereço, protocolo e porta.

Os **firewalls distribuídos** combinam o firewall de host com **gerenciamento centralizado**.

| Firewall | Características |
| --- | --- |
| Firewall do Windows Defender | Perfis **Público** (o mais restritivo), **Privado** e **Domínio** |
| iptables | Regras de acesso do **Netfilter** no kernel Linux |
| nftables | Sucessor do iptables |
| TCP Wrappers | Controle de acesso por IP e serviço no Linux |

### 28.3 Detecção de Intrusão Baseada em Host

Um **HIDS** protege contra **malware conhecido e desconhecido**. Oferece:

- monitoramento da configuração e dos aplicativos;
- análise de logs e **correlação de eventos**;
- **verificação de integridade**;
- aplicação de políticas;
- **detecção de rootkits**;
- alertas.

O HIDS é **baseado em agente**, com um **servidor de gerenciamento** central.

### 28.4 Funcionamento do HIDS

O HIDS usa **assinaturas** contra ameaças conhecidas, que não funcionam contra **dia zero** nem contra **malware polimórfico** (que muda a própria assinatura). Por isso, usa também:

- **anomalias**: compara com uma **linha de base** do comportamento normal; pode gerar **muitos falsos alarmes**;
- **política**: detecta **violações de regras** predefinidas.

| Estratégia | Detecta | Limitação |
| --- | --- | --- |
| Assinaturas | Malware conhecido | Não detecta dia zero nem polimórfico |
| Anomalias | Desvios da linha de base | Muitos falsos alarmes |
| Política | Violações de regras | Depende de regras bem definidas |

### 28.5 Produtos HIDS

Exemplos: **Cisco AMP**, **AlienVault USM**, **Tripwire** e **OSSEC**.

O **OSSEC** usa um **servidor central** e **agentes** nos hosts. Recebe alertas por **syslog**, **verifica a integridade dos arquivos** e detecta rootkits.

## 29. Segurança de Aplicações

Mesmo com proteção no host e no perímetro, o malware entra. Por isso, é preciso **reduzir o que pode ser atacado** e analisar com segurança o que parece suspeito.

### 29.1 Superfície de Ataque

A **superfície de ataque** é a **soma das vulnerabilidades acessíveis ao atacante**: portas abertas, software exposto, protocolos sem fio e até os usuários. Ela cresce com **IoT, BYOD, nuvem e mobilidade**.

O **Instituto SANS** descreve **três componentes**:

| Superfície | O que o ataque explora |
| --- | --- |
| De rede | Protocolos com e sem fio |
| De software | Aplicativos web, na nuvem ou no host |
| Humana | **O comportamento do usuário** |

### 29.2 Listas de Bloqueio e de Permissão

- **lista de bloqueio** (*blocklist*): **quais aplicativos não podem rodar**;
- **lista de permissão** (*allowlist*): **só os programas listados podem rodar**.

No Windows, as listas são configuradas no **Editor de Política de Grupo Local**. Também há listas de **sites**, como as do **Talos** e do **Spamhaus**.

### 29.3 Sandboxing

O **sandboxing** permite **executar e analisar arquivos suspeitos em um ambiente seguro**.

De forma simplificada:

1. o **Cisco AMP** rastreia a **trajetória do arquivo** na rede;
2. o arquivo é executado em uma sandbox, que documenta suas atividades;
3. as informações geram **assinaturas** e **regras de detecção**.

Exemplos de sandboxes:

- **Cuckoo Sandbox**: gratuita, local;
- **VirusTotal**, **Joe Sandbox**, **CrowdStrike Falcon Sandbox**: on-line;
- **ANY.RUN**: on-line, com relatórios interativos e **IOCs**, mapeados na matriz **MITRE ATT&CK**.

## 30. Contramedidas, Conscientização e Políticas

Os **pilares da defesa** são **tecnologia**, **políticas e práticas** e **pessoas**.

### 30.1 Tecnologias de Software

| Tecnologia | Função |
| --- | --- |
| Firewalls de software | Controlam o acesso remoto ao sistema |
| Scanners de rede e de portas | Descobrem as **portas abertas** |
| Analisadores de protocolo | Examinam o tráfego e criam a linha de base |
| Scanners de vulnerabilidade | Avaliam **pontos fracos** |
| IDS de host | Examinam a atividade **só no host** |

### 30.2 Tecnologias de Hardware

| Tecnologia | Função |
| --- | --- |
| Firewalls | Bloqueiam o tráfego indesejado |
| Servidores proxy | **Um único IP para toda a empresa**; **ocultam a origem real** |
| Controle de acesso por hardware | Dispositivos **biométricos** |
| Switches | Recursos de segurança da LAN |

### 30.3 Cultura de Conscientização

Gastar muito em tecnologia não adianta se **as pessoas forem o elo mais fraco**. Formas de treinar:

- treinamento na **integração** do funcionário;
- ligar a conscientização às avaliações de desempenho;
- sessões com **gamificação**;
- cursos on-line.

As pessoas são **a primeira linha de defesa**.

**Importante:** a conscientização é **um processo contínuo**, não um evento único.

### 30.4 Políticas de Segurança

Uma **política de segurança** **define os objetivos de segurança, as regras de comportamento e os requisitos dos sistemas**. Ela:

- demonstra o compromisso da empresa;
- define as regras de comportamento;
- garante consistência;
- define as **consequências jurídicas** das violações;
- dá à segurança o **apoio da gerência**.

| Política | O que define |
| --- | --- |
| Identificação e autenticação | Quem acessa e como é verificado |
| Senhas | Requisitos mínimos e troca |
| Uso aceitável | Usos permitidos e consequências |
| Acesso remoto | Como acessar a rede de fora |
| Manutenção de rede | Atualização dos dispositivos e aplicativos |
| Tratamento de incidentes | Como tratar incidentes |

A **AUP** (*Acceptable Use Policy*) define **o que os usuários podem ou não fazer** e deve ser **o mais explícita possível**.

### 30.5 Padrões, Diretrizes e Procedimentos

- **padrões**: requisitos **obrigatórios** que garantem a **consistência**; exemplo: senha com no mínimo oito caracteres, trocada a cada 30 dias, sem repetir as 12 últimas;
- **diretrizes**: **sugestões flexíveis**, em geral não obrigatórias, com as melhores práticas; exemplo: criar a senha a partir de uma frase, como **Ihv@dr3@m** ("I have a dream");
- **procedimentos**: **instruções passo a passo** detalhadas; exemplo: como trocar a senha no Windows.

| Documento | Natureza | Exemplo |
| --- | --- | --- |
| Política | Objetivos e regras gerais | Toda conta deve ter senha |
| Padrão | Requisito obrigatório | Mínimo de oito caracteres |
| Diretriz | Sugestão flexível | Senha a partir de uma frase |
| Procedimento | Passo a passo | Como trocar a senha |

## Glossário de Siglas

| Sigla | Nome completo | Significado |
| --- | --- | --- |
| AAA | Authentication, Authorization and Accounting | Autenticação, autorização e contabilidade |
| ACK | Acknowledgment | Bit de confirmação do TCP |
| ACL | Access Control List | Lista de regras que permite ou bloqueia tráfego |
| ADS | Alternate Data Streams | Fluxos de dados alternativos do NTFS |
| AES | Advanced Encryption Standard | Padrão de criptografia simétrica avançada |
| AIS | Automated Indicator Sharing | Compartilhamento automatizado de indicadores da CISA |
| AMP | Advanced Malware Protection | Proteção avançada contra malware da Cisco |
| AP | Access Point | Ponto de acesso sem fio |
| APFS | Apple File System | Sistema de arquivos atual da Apple |
| API | Application Programming Interface | Interface pela qual programas se comunicam |
| APT | Advanced Persistent Threat | Ameaça persistente avançada |
| APWG | Anti-Phishing Working Group | Grupo internacional contra phishing |
| ARP | Address Resolution Protocol | Protocolo que descobre o MAC a partir do IP |
| ASA | Adaptive Security Appliance | Equipamento de segurança adaptável da Cisco |
| AUP | Acceptable Use Policy | Política de uso aceitável |
| BCD | Boot Configuration Data | Dados de configuração da inicialização do Windows |
| BIOS | Basic Input-Output System | Firmware básico de entrada e saída |
| BYOD | Bring Your Own Device | Uso de dispositivos pessoais no trabalho |
| C&C | Command and Control | Comando e controle de malware |
| CAM | Content Addressable Memory | Tabela de endereços MAC do switch |
| CCMP | Counter Mode with CBC-MAC Protocol | Protocolo de criptografia e integridade do WPA2 |
| CDFS | Compact Disc File System | Sistema de arquivos de discos ópticos |
| CHAP | Challenge Handshake Authentication Protocol | Autenticação por desafio e resposta |
| CIA | Confidentiality, Integrity, Availability | Tríade confidencialidade, integridade e disponibilidade |
| CISA | Cybersecurity and Infrastructure Security Agency | Agência de segurança cibernética dos EUA |
| CLI | Command-Line Interface | Interface de linha de comando |
| CNSA | Commercial National Security Algorithm | Conjunto de algoritmos de alta segurança |
| CPU | Central Processing Unit | Unidade central de processamento |
| CSMA/CA | Carrier Sense Multiple Access with Collision Avoidance | Acesso ao meio com prevenção de colisões |
| CSMA/CD | Carrier Sense Multiple Access with Collision Detection | Acesso ao meio com detecção de colisões |
| CSRF | Cross-Site Request Forgery | Falsificação de solicitação entre sites |
| CTS | Clear to Send | Mensagem que libera o envio na WLAN |
| CVE | Common Vulnerabilities and Exposures | Dicionário público de vulnerabilidades |
| CWS | Cloud Web Security | Segurança web na nuvem da Cisco |
| DAI | Dynamic ARP Inspection | Inspeção dinâmica de ARP |
| DAS | Direct-Attached Storage | Armazenamento ligado diretamente ao computador |
| DC | Domain Controller | Controlador de domínio do Windows |
| DDoS | Distributed Denial of Service | Negação de serviço distribuída |
| DFS | Distributed File System | Sistema de arquivos distribuído |
| DGA | Domain Generation Algorithm | Algoritmo de geração de domínios |
| DHCP | Dynamic Host Configuration Protocol | Protocolo que distribui a configuração IP |
| DLL | Dynamic Link Library | Biblioteca de vínculo dinâmico do Windows |
| DLP | Data Loss Prevention | Prevenção de perda de dados |
| DMZ | Demilitarized Zone | Zona desmilitarizada |
| DNS | Domain Name System | Sistema que associa nomes a endereços IP |
| DoS | Denial of Service | Negação de serviço |
| DOS | Disk Operating System | Sistema operacional de disco |
| DPI | Deep Packet Inspection | Inspeção profunda de pacotes |
| DPP | Device Provisioning Protocol | Protocolo de integração de dispositivos IoT |
| DRM | Digital Rights Management | Gerenciamento de direitos digitais |
| DS | Differentiated Services | Serviços diferenciados (prioridade do pacote) |
| DSCP | Differentiated Services Code Point | Parte do campo DS que marca a prioridade |
| EAP | Extensible Authentication Protocol | Estrutura de autenticação de rede |
| ECN | Explicit Congestion Notification | Notificação explícita de congestionamento |
| EDR | Endpoint Detection and Response | Detecção e resposta no endpoint |
| EFS | Encrypting File System | Sistema de arquivos com criptografia do Windows |
| EH | Extension Header | Cabeçalho de extensão do IPv6 |
| EMI | Electromagnetic Interference | Interferência eletromagnética |
| ENISA | European Union Agency for Cybersecurity | Agência da União Europeia para a Cibersegurança |
| EOL | End of Life | Fim da vida útil de um produto |
| ESA | Email Security Appliance | Equipamento de segurança de e-mail da Cisco |
| ESP | EFI System Partition | Partição do sistema EFI |
| EXT | Extended File System | Sistema de arquivos do Linux |
| FAT | File Allocation Table | Sistema de arquivos simples e antigo |
| FCS | Frame Check Sequence | Verificação de erros do quadro |
| FDE | Full Disk Encryption | Criptografia de disco completo |
| FIN | Finish | Bit do TCP que encerra o envio de dados |
| FTP | File Transfer Protocol | Protocolo de transferência de arquivos |
| GRE | Generic Routing Encapsulation | Encapsulamento genérico em túneis IP |
| GUI | Graphical User Interface | Interface gráfica do usuário |
| HAL | Hardware Abstraction Layer | Camada de abstração de hardware |
| HFS+ | Hierarchical File System Plus | Sistema de arquivos dos Macintosh |
| HIDS | Host-based Intrusion Detection System | Detecção de intrusão no host |
| HIPS | Host-based Intrusion Prevention System | Prevenção de intrusão no host |
| HKCC | HKEY\_CURRENT\_CONFIG | Ramo do registro com o perfil de hardware atual |
| HKCR | HKEY\_CLASSES\_ROOT | Ramo do registro com os registros OLE |
| HKCU | HKEY\_CURRENT\_USER | Ramo do registro do usuário conectado |
| HKLM | HKEY\_LOCAL\_MACHINE | Ramo do registro com informações do sistema |
| HKU | HKEY\_USERS | Ramo do registro com todas as contas |
| HTML | HyperText Markup Language | Linguagem das páginas web |
| HTTP | HyperText Transfer Protocol | Protocolo da web |
| HTTPS | HTTP Secure | HTTP com criptografia SSL/TLS |
| IaaS | Infrastructure as a Service | Infraestrutura como serviço |
| ICMP | Internet Control Message Protocol | Protocolo de mensagens de erro e controle |
| IDS | Intrusion Detection System | Sistema de detecção de intrusão |
| IEEE | Institute of Electrical and Electronics Engineers | Instituto que define os padrões 802 |
| IETF | Internet Engineering Task Force | Grupo que padroniza os protocolos da internet |
| IHL | Internet Header Length | Tamanho do cabeçalho IPv4 |
| IMAP | Internet Message Access Protocol | Protocolo de acesso a e-mails |
| IOA | Indicator of Attack | Indicador de ataque |
| IOC | Indicator of Compromise | Indicador de comprometimento |
| IoT | Internet of Things | Internet das coisas |
| IP | Internet Protocol | Protocolo de rede da camada 3 |
| IPS | Intrusion Prevention System | Sistema de prevenção de intrusão |
| IPsec | IP Security | Conjunto de protocolos de segurança do IP |
| IRM | Information Rights Management | Gerenciamento de direitos de informação |
| ISP | Internet Service Provider | Provedor de acesso à internet |
| ISR | Integrated Services Router | Roteador de serviços integrados da Cisco |
| IV | Initialization Vector | Vetor de inicialização da criptografia |
| KMCS | Kernel Mode Code Signing | Exigência de assinatura dos drivers |
| LAN | Local Area Network | Rede local |
| LDAP | Lightweight Directory Access Protocol | Protocolo de acesso a serviços de diretório |
| LOIC | Low Orbit Ion Cannon | Ferramenta de inundação de pacotes |
| LWAP | Lightweight Access Point | Ponto de acesso leve, controlado por WLC |
| MAC | Media Access Control | Endereço físico da placa de rede |
| MACE | Modified, Accessed, Created, Entry modified | Carimbos de hora do NTFS |
| MBR | Master Boot Record | Registro mestre de inicialização |
| MFA | Multi-Factor Authentication | Autenticação multifator |
| MFT | Master File Table | Tabela mestra de arquivos do NTFS |
| MIB | Management Information Base | Banco de dados do agente SNMP |
| MIC | Message Integrity Check | Verificação de integridade da mensagem |
| MitM | Man-in-the-Middle | Homem no meio |
| MitMo | Man-in-the-Mobile | Homem no celular |
| MPLS | Multiprotocol Label Switching | Comutação de rótulos multiprotocolo |
| MRT | Malware Removal Tool | Ferramenta de remoção de malware da Apple |
| NAC | Network Admission Control | Controle de admissão na rede |
| NAS | Network-Attached Storage | Armazenamento ligado à rede |
| NCSA | National Cyber Security Alliance | Aliança nacional de segurança cibernética dos EUA |
| NCSAM | National Cyber Security Awareness Month | Mês de conscientização em segurança cibernética dos EUA |
| NetBIOS | Network Basic Input/Output System | Nome curto dos computadores na rede Windows |
| NFC | Near Field Communication | Comunicação por aproximação |
| NFS | Network File System | Sistema de arquivos em rede |
| NGFW | Next-Generation Firewall | Firewall de última geração |
| NIC | Network Interface Card | Placa de rede |
| NIST | National Institute of Standards and Technology | Instituto de padrões e tecnologia dos EUA |
| NMS | Network Management System | Sistema de gerenciamento de rede |
| NSA | National Security Agency | Agência de segurança nacional dos EUA |
| NT | New Technology | Base do Windows moderno |
| NTFS | New Technology File System | Sistema de arquivos padrão do Windows |
| NTP | Network Time Protocol | Protocolo de sincronização de relógios |
| OLE | Object Linking and Embedding | Inserção de objetos entre aplicativos |
| OSI | Open Systems Interconnection | Modelo de referência de sete camadas |
| OSINT | Open Source Intelligence | Inteligência de fontes abertas |
| OSSEC | Open Source HIDS Security | HIDS de código aberto |
| OWASP | Open Web Application Security Project | Projeto aberto de segurança de aplicações web |
| OWE | Opportunistic Wireless Encryption | Criptografia das redes abertas no WPA3 |
| PaaS | Platform as a Service | Plataforma como serviço |
| PAN | Personal Area Network | Rede pessoal |
| PID | Process Identifier | Identificador do processo |
| PIN | Personal Identification Number | Senha numérica curta |
| PMF | Protected Management Frames | Quadros de gerenciamento protegidos |
| POP3 | Post Office Protocol version 3 | Protocolo de recebimento de e-mails |
| POST | Power-On Self-Test | Autoteste ao ligar o computador |
| PSH | Push | Bit de função push do TCP |
| PSIRT | Product Security Incident Response Team | Equipe da Cisco para vulnerabilidades em produtos |
| PSK | Pre-Shared Key | Chave pré-compartilhada |
| QoS | Quality of Service | Qualidade de serviço: prioridade para certos tipos de tráfego |
| RADIUS | Remote Authentication Dial-In User Service | Protocolo de autenticação AAA em padrão aberto |
| RAID | Redundant Array of Independent Disks | Conjunto redundante de discos |
| RAM | Random Access Memory | Memória principal do computador |
| RAT | Remote Administration Tool | Ferramenta de administração remota |
| RC4 | Rivest Cipher 4 | Algoritmo de criptografia usado no WEP |
| RDP | Remote Desktop Protocol | Protocolo de área de trabalho remota |
| RF | Radio Frequency | Radiofrequência |
| RFC | Request for Comments | Documento que define padrões da internet |
| RFI | Radio Frequency Interference | Interferência de radiofrequência |
| RFID | Radio Frequency Identification | Identificação por radiofrequência |
| ROM | Read-Only Memory | Memória somente de leitura |
| RR | Resource Record | Registro de recurso do DNS |
| RST | Reset | Bit do TCP que encerra a conexão |
| RTS | Request to Send | Pedido de envio na WLAN |
| SaaS | Software as a Service | Software como serviço |
| SAE | Simultaneous Authentication of Equals | Autenticação do WPA3-Personal |
| SAN | Storage Area Network | Rede de armazenamento |
| SANS | SysAdmin, Audit, Network and Security | Instituto de treinamento em segurança |
| SHA | Secure Hash Algorithm | Família de algoritmos de hash |
| SIEM | Security Information and Event Management | Gerenciamento de informações e eventos de segurança |
| SMB | Server Message Block | Protocolo de compartilhamento do Windows |
| SMS | Short Message Service | Mensagem de texto |
| SMSS | Session Manager Subsystem | Subsistema gerenciador de sessões do Windows |
| SMTP | Simple Mail Transfer Protocol | Protocolo de envio de e-mail |
| SNMP | Simple Network Management Protocol | Protocolo de gerenciamento de rede |
| SOC | Security Operations Center | Centro de operações de segurança |
| SQL | Structured Query Language | Linguagem de consulta a bancos de dados |
| SSD | Solid-State Drive | Unidade de estado sólido |
| SSH | Secure Shell | Acesso remoto seguro |
| SSID | Service Set Identifier | Nome da rede sem fio |
| SSL | Secure Sockets Layer | Antiga criptografia da web, sucedida pelo TLS |
| SSSD | System Security Services Daemon | Serviço de autenticação do Linux |
| STIX | Structured Threat Information Expression | Linguagem de informações de ameaças |
| STP | Spanning Tree Protocol | Protocolo que evita laços entre switches |
| SYN | Synchronize | Bit do TCP que inicia a conexão |
| TACACS+ | Terminal Access Controller Access-Control System Plus | Protocolo AAA da Cisco |
| TAXII | Trusted Automated Exchange of Intelligence Information | Protocolo de troca de informações de ameaças |
| TCP | Transmission Control Protocol | Protocolo de transporte confiável |
| TFTP | Trivial File Transfer Protocol | Transferência de arquivos simplificada |
| TI | Tecnologia da Informação | Área de tecnologia da empresa |
| TKIP | Temporal Key Integrity Protocol | Protocolo de criptografia do WPA |
| TLS | Transport Layer Security | Criptografia do transporte, sucessora do SSL |
| TOC/TOU | Time of Check / Time of Use | Tempo de verificação e tempo de uso |
| ToS | Type of Service | Antigo campo de tipo de serviço do IPv4 |
| TPM | Trusted Platform Module | Chip que guarda chaves e certificados |
| TTL | Time to Live | Tempo de vida do pacote |
| UDP | User Datagram Protocol | Protocolo de transporte sem conexão |
| UEFI | Unified Extensible Firmware Interface | Firmware sucessor do BIOS |
| UNC | Universal Naming Convention | Formato de caminho de recursos de rede |
| URG | Urgent | Bit de ponteiro urgente do TCP |
| URL | Uniform Resource Locator | Endereço de um recurso na internet |
| US-CERT | United States Computer Emergency Readiness Team | Equipe de resposta a emergências de computação dos EUA |
| USB | Universal Serial Bus | Barramento serial universal |
| VBA | Visual Basic for Applications | Linguagem das macros da Microsoft |
| VLAN | Virtual LAN | Rede local virtual |
| VoIP | Voice over IP | Voz sobre IP |
| VPN | Virtual Private Network | Rede privada virtual |
| WAN | Wide Area Network | Rede de longa distância |
| WEP | Wired Equivalent Privacy | Primeira segurança Wi-Fi, insegura |
| WLAN | Wireless LAN | Rede local sem fio |
| WLC | Wireless LAN Controller | Controlador de LAN sem fio |
| WMI | Windows Management Instrumentation | Instrumentação de gerenciamento do Windows |
| WPA | Wi-Fi Protected Access | Acesso protegido Wi-Fi |
| WPA2 | Wi-Fi Protected Access 2 | Segunda versão do WPA, com AES |
| WPA3 | Wi-Fi Protected Access 3 | Terceira versão do WPA |
| WPS | Wi-Fi Protected Setup | Configuração rápida do Wi-Fi, vulnerável |
| WSA | Web Security Appliance | Equipamento de segurança web da Cisco |
| XML | Extensible Markup Language | Linguagem de marcação extensível |
| XSS | Cross-Site Scripting | Script entre sites |
| ZPF | Zone-Based Policy Firewall | Firewall de política baseada em zonas |

## Exercícios

### A. Permissões do Linux (ver item 24.3)

1. Informe o valor octal das permissões `rwxr-xr-x`.
2. Informe o valor octal das permissões `rw-r-----`.
3. Escreva em letras as permissões 750 e 644.
4. Indique quem pode ler, gravar e executar um arquivo com permissão 711.
5. Analise a linha `drwxr-x--- 2 ana vendas 4096 Mar 3 10:15 relatorios` e informe o tipo do item, o dono, o grupo e o que os outros usuários podem fazer.
6. Escreva o comando que dá ao dono acesso total e não dá nenhum acesso ao grupo nem aos outros no arquivo segredo.txt.

### B. Campos dos Cabeçalhos (ver itens 7.2, 7.3 e 8.2)

1. Calcule o tamanho máximo de um pacote IPv4 a partir do tamanho do campo Tamanho total.
2. Um pacote sai do host com TTL 64 e passa por 5 roteadores. Informe o TTL ao chegar ao destino e o que acontece se o TTL inicial for 3.
3. Informe o protocolo indicado pelo campo Protocolo com valor 6, 17 e 1.
4. No handshake de três vias, o cliente envia SYN com SEQ=500 e o servidor responde com SEQ=900. Informe os números de SEQ e ACK do SYN-ACK e do ACK final.
5. Compare o tamanho mínimo dos cabeçalhos IPv4, IPv6, TCP e UDP.

### C. Memória e Arquitetura do Windows (ver itens 18.2 e 19.9)

1. Calcule, em GB, a memória que um sistema de 32 bits consegue endereçar, sabendo que 1 GB = 2^30 bytes.
2. Calcule, em milhões de TB, o limite teórico de 64 bits, sabendo que 1 TB = 2^40 bytes.
3. Indique se um programa de 64 bits roda em hardware de 32 bits e se um de 32 bits roda em um sistema de 64 bits.

### D. Estratos do NTP (ver item 17.5)

1. Um servidor sincroniza com um servidor de estrato 1. Informe o seu estrato.
2. Um roteador sincroniza com esse servidor. Informe o estrato do roteador.
3. Informe o que indica um dispositivo de estrato 16.

### E. Questões Conceituais: Fundamentos e Ameaças

1. Classifique cada situação no objetivo da tríade CIA afetado: um site fora do ar; um extrato bancário alterado; uma planilha de salários vista por um estagiário.
2. Indique o estado dos dados em cada caso: um e-mail sendo enviado; um backup guardado no NAS; uma planilha sendo editada.
3. Diferencie ameaça, vulnerabilidade, exploração e risco.
4. Indique a estratégia de risco adotada quando a empresa contrata um seguro e quando deixa de oferecer um serviço arriscado.
5. Explique por que as ameaças internas podem ser mais graves que as externas.
6. Diferencie IOC e IOA.
7. Diferencie hacker de chapéu branco, cinza e preto.

### F. Questões Conceituais: Engano, Malware e Aplicativos

1. Identifique a tática de engenharia social: "Últimas cinco unidades com 80% de desconto!".
2. Diferencie vírus, worm e cavalo de Troia.
3. Explique por que um rootkit é tão difícil de remover.
4. Explique como funciona uma botnet em um ataque DDoS.
5. Diferencie phishing, spear phishing, whaling, vishing e SMiShing.
6. Explique a causa comum da injeção de SQL e do XSS e a principal defesa.
7. Diferencie XSS armazenado e refletido.

### G. Questões Conceituais: Protocolos e Serviços

1. Explique como funciona o ataque Smurf.
2. Descreva a inundação SYN.
3. Explique por que o ARP permite o envenenamento de cache e qual é o objetivo do atacante.
4. Explique por que o cliente aceita o servidor DHCP falso.
5. Indique três sinais de tunelamento DNS e uma defesa.
6. Explique por que os servidores de e-mail não devem ser retransmissores abertos.
7. Ordene as quatro fases da resposta a um worm.

### H. Questões Conceituais: Redes sem Fio e Infraestrutura

1. Explique por que ocultar o SSID e filtrar MAC não bastam.
2. Diferencie WPA2-Personal e WPA2-Enterprise.
3. Descreva o ataque do gêmeo do mal.
4. Compare IDS e IPS quanto ao posicionamento, ao bloqueio e ao impacto na rede.
5. Indique o tratamento do tráfego da internet para a DMZ e da DMZ para a rede privada.
6. Diferencie TACACS+ e RADIUS quanto ao transporte e à criptografia.
7. Explique para que serve o espelhamento de portas.

### I. Questões Conceituais: Windows, Linux e Endpoints

1. Diferencie modo usuário e modo kernel.
2. Explique por que o ADS é útil para atacantes e como revelá-lo.
3. Indique o comando do Windows que liga cada conexão ao processo que a criou.
4. Diferencie link rígido e link simbólico quando o arquivo original é apagado.
5. Cite quatro práticas de endurecimento do Linux.
6. Diferencie inicialização segura e inicialização medida.
7. Diferencie detecção por assinatura, por anomalia e por política no HIDS.
8. Diferencie lista de bloqueio e lista de permissão.
9. Diferencie política, padrão, diretriz e procedimento.

## Gabarito

### A. Permissões do Linux

1. rwx = 4+2+1 = 7; r-x = 4+0+1 = 5; r-x = 5 → **755**.
2. rw- = 6; r-- = 4; --- = 0 → **640**.
3. 750 = **rwxr-x---**; 644 = **rw-r--r--**.
4. 711 = rwx--x--x: o **dono** lê, grava e executa; o **grupo** e os **outros** só executam.
5. O **d** indica um **diretório**; dono: **ana**; grupo: **vendas**; os outros **não têm nenhum acesso** (---).
6. rwx------ = 700 → **`chmod 700 segredo.txt`**.

### B. Campos dos Cabeçalhos

1. O campo tem 16 bits: 2^16 − 1 = **65.535 bytes**.
2. 64 − 5 = **59**. Com TTL 3, o terceiro roteador reduz o valor a zero, **descarta o pacote** e envia à origem um ICMP de **tempo excedido**.
3. 6 = **TCP**; 17 = **UDP**; 1 = **ICMP**.
4. SYN-ACK: **SEQ=900, ACK=501**; ACK final: **SEQ=501, ACK=901**.
5. IPv4: **20 bytes**; IPv6: **40 bytes**; TCP: **20 bytes**; UDP: **8 bytes**.

### C. Memória e Arquitetura do Windows

1. 2^32 = 4.294.967.296 bytes ÷ 2^30 = **4 GB**.
2. 2^64 ÷ 2^40 = 2^24 = 16.777.216 TB ≈ **16,8 milhões de TB**.
3. Um programa de 64 bits **não roda** em hardware de 32 bits; um programa de 32 bits **roda** em um sistema de 64 bits.

### D. Estratos do NTP

1. Estrato **2**.
2. Estrato **3**.
3. O dispositivo **não está sincronizado**.

### E. Questões Conceituais: Fundamentos e Ameaças

1. Site fora do ar: **disponibilidade**; extrato alterado: **integridade**; planilha vista por quem não devia: **confidencialidade**.
2. E-mail sendo enviado: **em trânsito**; backup no NAS: **em repouso**; planilha sendo editada: **em processamento**.
3. **Ameaça** é o perigo potencial; **vulnerabilidade** é a fraqueza; **exploração** é o mecanismo que aproveita a fraqueza; **risco** é a probabilidade de a ameaça explorar a vulnerabilidade e causar dano.
4. Seguro: **transferência**; deixar de oferecer o serviço: **prevenção** (evitar o risco).
5. O usuário interno tem **acesso direto** ao prédio e aos equipamentos e **conhece a rede**, os dados e as contramedidas.
6. O **IOC** é a **evidência de um ataque que já aconteceu** (defesa reativa); o **IOA** trata da **motivação e das estratégias** do atacante (defesa proativa).
7. **Branco**: hacker ético, que relata as falhas; **cinza**: comete atos ilegais ou antiéticos, mas não para ganho pessoal; **preto**: criminoso, por ganho pessoal ou malícia.

### F. Questões Conceituais: Engano, Malware e Aplicativos

1. **Escassez** (e, com prazo, também **urgência**).
2. O **vírus** se anexa a outro programa e precisa do usuário; o **worm** se replica sozinho pela rede, sem hospedeiro; o **cavalo de Troia** parece legítimo, esconde sua intenção e não se replica.
3. Ele **altera o sistema operacional e as ferramentas de diagnóstico**, escondendo-se; muitas vezes é preciso **apagar e reinstalar** o sistema.
4. O atacante infecta computadores (**zumbis**) controlados por **manipuladores**; os zumbis infectam outros e, sob comando, atacam juntos o alvo.
5. **Phishing**: fraude que se disfarça de fonte legítima; **spear phishing**: direcionado a uma pessoa; **whaling**: a executivos; **vishing**: por voz; **SMiShing**: por SMS.
6. A causa é a **falta de validação da entrada**; a principal defesa é **tratar toda entrada como hostil e validá-la**.
7. O **armazenado** fica gravado no servidor e atinge todos os visitantes; o **refletido** fica em um link e só atinge quem clica.

### G. Questões Conceituais: Protocolos e Serviços

1. O atacante envia pedidos de eco ICMP a muitos hosts com o **IP da vítima como origem** (amplificação), e todos **respondem à vítima** (reflexão).
2. O atacante envia muitos **SYN com origens falsas**; o servidor responde SYN-ACK e espera ACKs que não chegam, até esgotar com **conexões semiabertas**.
3. O ARP **não autentica as respostas** e aceita ARP gratuito; o atacante associa **seu MAC ao IP do gateway** para ficar no meio da comunicação (MitM).
4. O cliente **aceita a primeira oferta** que recebe, e o servidor legítimo para de responder quando a solicitação é confirmada pelo outro.
5. Consultas **mais longas que a média**, **nomes de domínio suspeitos** e domínios de **DNS dinâmico**; defesa: **filtro que inspeciona o DNS** ou serviço como o Cisco Umbrella.
6. Porque um **retransmissor aberto** deixa **qualquer pessoa enviar e-mails** por ele, o que é usado para spam e malware.
7. **Contenção → inoculação → quarentena → tratamento**.

### H. Questões Conceituais: Redes sem Fio e Infraestrutura

1. O **SSID é fácil de descobrir** mesmo oculto, e o **MAC pode ser falsificado**; a proteção real é autenticação e criptografia.
2. O **Personal** usa uma **chave pré-compartilhada**, sem servidor; o **Enterprise** usa **servidor RADIUS** e autenticação **802.1X/EAP** de cada usuário.
3. O atacante cria um AP com **o mesmo SSID** e sinal mais forte; as vítimas se conectam a ele, que captura e repassa o tráfego (MitM).
4. O **IDS** fica **fora de linha**, **não bloqueia** o pacote e **não afeta** a rede; o **IPS** fica **em linha**, **bloqueia** e pode causar **latência e jitter**.
5. Internet → DMZ: **permitido seletivamente e inspecionado** (e-mail, DNS, HTTP, HTTPS); DMZ → rede privada: **bloqueado**.
6. **TACACS+**: **TCP** e **pacote inteiro criptografado**; **RADIUS**: **UDP** e **só a senha criptografada**.
7. Faz o switch **copiar o tráfego** para uma porta onde está um analisador ou IDS, que de outro modo não veria esse tráfego.

### I. Questões Conceituais: Windows, Linux e Endpoints

1. O **modo kernel** tem acesso irrestrito ao hardware e uma falha para o computador; o **modo usuário** só acessa o hardware pelo sistema, e uma falha afeta só o aplicativo.
2. O ADS **esconde dados** atrás de um arquivo comum, que aparece com o tamanho normal; é revelado com **`dir /r`**.
3. **`netstat -abno`**, em prompt de administrador.
4. O **link rígido continua funcionando**, porque aponta para o mesmo inode; o **simbólico fica quebrado**, porque aponta para o nome.
5. Quatro entre: segurança física; poucos pacotes instalados; desativar serviços não usados; usar SSH e **bloquear o login do root por SSH**; manter atualizado; desativar a detecção automática de USB; senhas fortes; troca periódica; impedir reutilização.
6. A **segura** verifica **as assinaturas** do software de inicialização; a **medida** **mede cada componente** e guarda as medidas no **TPM**, em um log que pode ser verificado remotamente.
7. **Assinatura**: reconhece malware conhecido; **anomalia**: compara com a linha de base e pode gerar falsos alarmes; **política**: age quando uma regra predefinida é violada.
8. A **lista de bloqueio** diz o que **não pode** rodar; a **lista de permissão** diz o **único** que pode rodar.
9. **Política**: objetivos e regras gerais; **padrão**: requisito obrigatório e consistente; **diretriz**: sugestão flexível; **procedimento**: passo a passo detalhado.
