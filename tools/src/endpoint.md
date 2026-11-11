# Segurança de Endpoint

Nov 6, 2026 · @Maria Paula

## 1. Princípios da Segurança Cibernética

A **segurança cibernética** é o conjunto de medidas que protege dados, sistemas e redes contra acesso, alteração ou interrupção indevidos. Antes de estudar as ameaças, é preciso saber o que se quer proteger e de que forma.

### 1.1 O Cubo da Segurança Cibernética

O **cubo da segurança cibernética** é um modelo que resume a tarefa de proteger dados em **três dimensões**:

| Dimensão | O que define | Elementos |
| --- | --- | --- |
| Primeira | Os objetivos da proteção | Confidencialidade, integridade e disponibilidade |
| Segunda | Os estados em que os dados podem estar | Em trânsito, em repouso (armazenamento) e em processamento |
| Terceira | Os pilares da defesa | Tecnologia; políticas e práticas; pessoas (educação, treinamento e conscientização) |

Os três objetivos da primeira dimensão formam a **tríade CIA** (*Confidentiality, Integrity, Availability*; em português, também tríade CID), que ajuda o profissional a priorizar ações ao proteger qualquer sistema em rede:

- **confidencialidade**: **impede a divulgação de informações** a pessoas, recursos ou processos não autorizados;
- **integridade**: garante a **precisão, a consistência e a confiabilidade** dos dados;
- **disponibilidade**: garante que as informações estejam **acessíveis aos usuários autorizados quando necessário**.

A proteção precisa cobrir **os três estados dos dados**: não basta proteger só os dados armazenados ou só os que estão sendo processados. E nenhuma tecnologia resolve sozinha; o profissional combina várias disciplinas e conhecimentos.

### 1.2 Confidencialidade

As informações confidenciais se dividem em três categorias: **pessoais**, **comerciais** e **classificadas** (sigilosas, de governo). A forma mais comum de protegê-las é a criptografia, que embaralha os dados para que só quem tem a chave consiga lê-los. Há também outras técnicas:

- **tokenização**: troca o dado original por um **valor aleatório sem relação matemática** com ele, o *token*; fora do sistema, o token não vale nada. Pode manter o formato do dado (tipo e tamanho), o que é útil em bancos de dados e no pagamento com cartão;
- **gerenciamento de direitos**: usa criptografia para controlar quem acessa um conteúdo:
  - **DRM** (*Digital Rights Management* — gerenciamento de direitos digitais): protege materiais com direitos autorais, como músicas, filmes e livros digitais; a mídia não pode ser copiada sem a chave, que só as partes licenciadas têm;
  - **IRM** (*Information Rights Management* — gerenciamento de direitos de informação): protege e-mails e documentos da empresa e permite ao dono controlar o acesso mesmo depois de compartilhá-los.

Para a **privacidade**, as empresas usam tecnologias como a tokenização, a **minimização de dados** (guardar só o necessário) e a **anonimização**, que oculta os dados que identificam uma pessoa e os transforma de forma **irreversível** em informação anônima.

### 1.3 Integridade

A **integridade** é a precisão, a consistência e a confiabilidade dos dados **durante todo o seu ciclo de vida**. Os dados passam por captura, armazenamento, recuperação, atualização e transferência, e precisam permanecer inalterados por pessoas não autorizadas em todas essas etapas.

Os métodos que garantem a integridade são:

- **hash**, um resumo matemático do dado que muda se o dado mudar;
- verificações de **validação** dos dados;
- verificações de **consistência**;
- **controles de acesso**.

A perda de integridade pode tornar um conjunto inteiro de dados inútil. A importância varia com o uso dos dados:

| Necessidade | Exemplo | Tratamento dos dados |
| --- | --- | --- |
| Crítica | Serviços de saúde (receitas médicas) | Validados, testados e verificados continuamente |
| Alta | Comércio eletrônico e análises | Validados e verificados com frequência |
| Média | Buscadores e vendas on-line que coletam dados públicos | Pouca verificação; dados não totalmente confiáveis |
| Baixa | Blogs, fóruns e redes sociais | Podem não ser verificados; confiança baixa |

### 1.4 Disponibilidade

A **disponibilidade** é manter as informações acessíveis sempre que forem necessárias. Ela é ameaçada por **falhas de equipamento**, **desastres naturais**, **ataques maliciosos** e pela **negação de serviço** (**DoS**, *Denial of Service*), ataque que impede usuários legítimos de usar um sistema. Derrubar o site de um concorrente, por exemplo, dá vantagem comercial ao atacante.

**Observação:** a manutenção de equipamentos e os backups não são ameaças; são medidas que protegem a disponibilidade.

As principais medidas para garantir a disponibilidade são:

- **manutenção de equipamentos**: troca, limpeza e alinhamento de componentes, o que aumenta o tempo de funcionamento;
- **atualizações e correções** (*patches*) do sistema operacional e dos aplicativos, que eliminam erros e vulnerabilidades;
- **teste de backup**: os backups precisam ser testados para garantir que os dados possam ser recuperados;
- **planejamento contra desastres**: funcionários e clientes sabem como agir, e a equipe pratica a resposta e a restauração dos sistemas críticos;
- **novas tecnologias**: avaliação contínua, já que os criminosos também usam as ferramentas mais recentes;
- **monitoramento de atividades**: logs de eventos, alertas e logs de acesso em tempo real, que podem revelar um ataque em segundos;
- **teste de disponibilidade**: varreduras de portas, varreduras de vulnerabilidades e testes de penetração.

Também ajudam a redundância e a resiliência dos sistemas.

### 1.5 Dados em Repouso

Os **dados em repouso** (*data at rest*) são os **dados armazenados**, que nenhum usuário ou processo está acessando, pedindo ou alterando. Incluem os backups quando não estão sendo gravados nem transmitidos. As principais opções de armazenamento são:

| Armazenamento | Como funciona |
| --- | --- |
| DAS (*Direct-Attached Storage*) | Ligado diretamente ao computador, como um disco rígido ou um pen drive; por padrão, não é compartilhado na rede |
| RAID (*Redundant Array of Independent Disks*) | Vários discos que o sistema vê como um só; melhora o desempenho e a tolerância a falhas |
| NAS (*Network-Attached Storage*) | Dispositivo ligado à rede que centraliza os dados para os usuários autorizados; flexível e escalável |
| SAN (*Storage Area Network*) | Rede de armazenamento com interfaces de alta velocidade que liga vários servidores a um repositório central de discos |
| Nuvem | Espaço remoto em um provedor, acessado pela internet, em geral por assinatura; exemplos: Google Drive, iCloud e Dropbox |

O **armazenamento local é o mais difícil de controlar** e fica vulnerável a ataques no próprio computador. Por isso, convém limitar os dados guardados em DAS e automatizar e centralizar os backups.

Os sistemas em rede (RAID, NAS e SAN) são **mais seguros, rápidos e redundantes**, mas mais complexos de configurar, testar e monitorar. Como concentram muitos dados, **uma falha representa um risco maior**.

### 1.6 Dados em Trânsito

Os **dados em trânsito** são os que estão **sendo transmitidos** de um dispositivo para outro. A transmissão pode ocorrer de três formas:

- **rede de tênis** (*sneaker net*): mídia removível levada fisicamente de um computador a outro; nunca pode ser eliminada por completo;
- **redes com fio**: cobre e fibra óptica, em redes locais (**LAN**, *Local Area Network*) ou de longa distância (**WAN**, *Wide Area Network*);
- **redes sem fio**: ondas de rádio; cada vez mais rápidas e comuns, aumentam os usuários convidados e, com isso, a **superfície de ataque**, isto é, o conjunto de pontos por onde um atacante pode entrar.

As redes transmitem **pacotes**, unidades de dados cuja estrutura é definida por protocolos públicos, como o IP e o HTTP. Os desafios de proteção seguem a tríade CIA:

| Objetivo | Ameaça | Proteção |
| --- | --- | --- |
| Confidencialidade | Captura, gravação ou roubo dos dados | Criptografia: VPNs (túneis protegidos pela internet), SSL/TLS (o cadeado do HTTPS), IPsec (criptografia dos pacotes IP) e outros métodos |
| Integridade | Interceptação e alteração dos dados | Sistemas de integridade: hash e redundância de dados |
| Disponibilidade | Dispositivos falsos que capturam e até apagam os dados, como um celular que se passa por ponto de acesso sem fio, ou sequestro de uma conexão autorizada | **Autenticação mútua**: o usuário se autentica no servidor e o servidor se autentica no usuário |

Uma **VPN** (*Virtual Private Network* — rede privada virtual) cria um túnel criptografado pela internet, por exemplo entre o notebook de quem trabalha em casa e a rede da empresa.

### 1.7 Dados em Processamento

Os **dados em processamento** (*data in process*) são os dados durante a **entrada, a modificação, o cálculo ou a saída**:

- **entrada**: digitação manual, digitalização de formulários, envio de arquivos ou leitura de sensores; a corrupção pode vir de rótulos errados, formatos incompatíveis, erros de digitação ou sensores com defeito;
- **modificação**: qualquer alteração dos dados originais, feita por usuários ou programas; codificar, compactar e criptografar são modificações intencionais. Quando a alteração torna os dados ilegíveis ou inúteis, ocorre **corrupção de dados**, causada por falhas de equipamento ou por código malicioso;
- **saída**: envio para impressoras, monitores e alto-falantes; a corrupção pode vir de delimitadores errados (os caracteres que separam os campos, como a vírgula em uma planilha CSV), configurações de comunicação incorretas ou impressoras mal configuradas.

A saída influencia decisões, por isso sua precisão é fundamental. Proteger os dados em processamento exige **sistemas bem projetados** e políticas de teste, manutenção e atualização.

| Estado | Exemplo | Principal desafio |
| --- | --- | --- |
| Em repouso | Arquivo no servidor da empresa | Controle do armazenamento local e falha de sistemas que concentram dados |
| Em trânsito | E-mail viajando pela internet | Captura, alteração e dispositivos falsos |
| Em processamento | Planilha sendo editada | Erros de entrada, corrupção e saída incorreta |

## 2. O Cenário de Ameaças

As redes são atacadas o tempo todo, e notícias de empresas comprometidas são frequentes. Empresas de segurança, como a Kaspersky, publicam **mapas de ameaças cibernéticas** que mostram os ataques acontecendo em tempo real no mundo.

### 2.1 Por que Proteger a Rede

A segurança da rede está ligada à **continuidade dos negócios**. Uma violação pode interromper o comércio eletrônico, causar perda de dados, ameaçar a privacidade e a integridade das informações e resultar em perda de receita, roubo de propriedade intelectual, processos judiciais e até riscos à segurança pública.

Manter a rede segura exige **vigilância constante** sobre ameaças novas e vulnerabilidades de dispositivos e aplicativos. Há fontes que ajudam nisso:

- **Cisco Talos Intelligence Group**: inteligência de segurança e de ameaças para proteger os clientes;
- **Cisco PSIRT** (*Product Security Incident Response Team*): investiga e mitiga vulnerabilidades dos produtos Cisco e publica avisos de segurança em tempo real.

### 2.2 Ameaça, Vulnerabilidade e Risco

Os **ativos** são tudo o que tem valor para a organização: dados, propriedade intelectual, servidores, computadores, smartphones e tablets. Para discutir segurança, alguns termos são essenciais:

| Termo | Significado |
| --- | --- |
| Ameaça | **Perigo potencial** para um ativo, como os dados ou a própria rede |
| Vulnerabilidade | **Fraqueza** em um sistema ou no seu projeto que pode ser explorada por uma ameaça |
| Superfície de ataque | **Soma das vulnerabilidades acessíveis** ao atacante: os pontos por onde ele entra ou retira dados |
| Exploração (*exploit*) | **Mecanismo usado para aproveitar uma vulnerabilidade** e comprometer um ativo |
| Risco | **Probabilidade** de uma ameaça explorar uma vulnerabilidade e causar uma consequência indesejável |
| Contramedida | Ação tomada para proteger os ativos, atenuando a ameaça ou reduzindo o risco |
| Impacto | Dano potencial causado pela ameaça |

Exemplo de superfície de ataque: o sistema operacional e o navegador sem as correções de segurança, ambos expostos na internet.

As explorações podem ser:

- **remotas**: funcionam pela rede, **sem acesso prévio** ao sistema; o atacante não precisa de conta;
- **locais**: o atacante já tem algum acesso de usuário ou de administrador ao sistema, o que **não significa acesso físico**.

### 2.3 Gerenciamento de Riscos

O **gerenciamento de riscos** equilibra o custo das medidas de proteção com o ganho de proteger o ativo. Há **quatro formas** de lidar com um risco:

| Estratégia | Como funciona |
| --- | --- |
| Aceitação | O custo de tratar o risco supera o custo do próprio risco; **o risco é aceito** e nada é feito |
| Prevenção (evitar) | **Elimina a atividade ou o dispositivo** que gera o risco, perdendo também seus benefícios |
| Redução (mitigação) | Toma medidas para **diminuir a exposição ou o impacto**; é a estratégia **mais usada** |
| Transferência | Passa parte ou todo o risco **a um terceiro**, como uma seguradora |

### 2.4 Ameaças Internas e Externas

Um **vetor de ataque** é o **caminho pelo qual o atacante chega** a um servidor, equipamento ou rede. Ele pode vir de fora ou de dentro da empresa.

As **ameaças externas** vêm de atacantes amadores ou experientes que exploram vulnerabilidades dos dispositivos ou usam truques de **engenharia social**, a manipulação de pessoas para obter acesso. Exemplo: atacar a rede pela internet para derrubá-la com um ataque DoS.

As **ameaças internas** vêm de funcionários atuais ou antigos, terceirizados e parceiros, por acidente ou de propósito. Um usuário interno pode:

- copiar dados confidenciais para mídia removível, e-mail ou aplicativos de mensagem;
- comprometer servidores internos ou equipamentos de rede;
- desconectar uma ligação crítica e interromper a rede;
- conectar um pen drive infectado ao computador da empresa;
- acessar e-mails ou sites maliciosos.

**Importante:** as ameaças internas podem causar **danos maiores que as externas**, porque o usuário interno tem **acesso direto** ao prédio e aos equipamentos e **conhece a rede**, os dados confidenciais e as contramedidas em uso.

### 2.5 Perda de Dados

Os dados costumam ser **o ativo mais valioso** da organização: pesquisa e desenvolvimento, vendas, finanças, recursos humanos, dados jurídicos e dados de funcionários, terceirizados e clientes.

A **perda de dados**, ou **exfiltração**, ocorre quando os dados são perdidos, roubados ou vazados para fora, de propósito ou não. As consequências são:

- danos à marca e à reputação;
- perda de vantagem competitiva;
- perda de clientes e de receita;
- processos judiciais, multas e penalidades;
- custo e esforço para avisar os afetados e se recuperar.

Por isso, as empresas usam controles de **DLP** (*Data Loss Prevention* — prevenção de perda de dados), que combinam medidas estratégicas, operacionais e táticas. Os vetores mais comuns são:

| Vetor | Risco |
| --- | --- |
| E-mail e redes sociais | O mais comum; mensagens interceptadas revelam informações confidenciais |
| Dispositivos não criptografados | Um notebook roubado entrega os dados se eles não estiverem criptografados |
| Armazenamento em nuvem | Configurações de segurança fracas expõem os dados |
| Mídia removível | Cópia não autorizada para um pen drive ou perda do pen drive |
| Cópia impressa | Documentos jogados fora sem triturar podem ser recuperados |
| Controle de acesso inadequado | Senhas fracas ou roubadas dão acesso fácil aos dados |

### 2.6 Hackers e Atores de Ameaça

O termo **hacker** tem vários sentidos: um programador habilidoso, um profissional que protege redes, alguém que invade dispositivos ou que derruba serviços e apaga dados. Os hackers costumam ser classificados pela cor do "chapéu":

| Tipo | Quem é |
| --- | --- |
| Chapéu branco (*white hat*) | **Hacker ético**; faz testes de penetração e relata as vulnerabilidades para que sejam corrigidas; algumas empresas pagam recompensas |
| Chapéu cinza (*gray hat*) | Comete crimes ou atos antiéticos, mas **não para ganho pessoal** nem para causar dano; por exemplo, invade sem permissão e depois divulga a falha |
| Chapéu preto (*black hat*) | **Criminoso** que viola a segurança para ganho pessoal ou por motivos maliciosos |

Neste resumo, **ator de ameaça** é o indivíduo ou grupo que se enquadra como hacker de chapéu cinza ou preto.

### 2.7 Evolução dos Atores de Ameaça

O *hacking* começou nos anos 1960 com o **phreaking** telefônico: as centrais usavam tons para indicar funções, e imitar um tom com um apito permitia fazer ligações de longa distância de graça. Nos anos 1980, com os modems discados (aparelhos que ligavam o computador à rede pela linha telefônica), surgiram os programas de **discagem de guerra** (*war dialing*), que ligavam para todos os números de uma região em busca de computadores e depois usavam programas de quebra de senha.

Os principais tipos de atores de ameaça hoje são:

| Tipo | Características |
| --- | --- |
| Script kiddies | Jovens ou atacantes inexperientes que **usam ferramentas prontas**; surgiram nos anos 1990 e em geral não visam lucro |
| Corretores de vulnerabilidades | Hackers de chapéu cinza que descobrem falhas e as relatam aos fabricantes, às vezes por recompensa |
| Hacktivistas | Hackers de chapéu cinza que **protestam contra ideias políticas e sociais**, publicando material, vazando informações e fazendo ataques DDoS (negação de serviço distribuída, em que muitos computadores atacam o mesmo alvo ao mesmo tempo) |
| Cibercriminosos | Hackers de chapéu preto, autônomos ou de organizações criminosas, **motivados por dinheiro** |
| Patrocinados pelo Estado | Roubam segredos e sabotam redes de governos estrangeiros, grupos terroristas e empresas; são vistos como chapéu branco ou preto **conforme o ponto de vista** |

Os **cibercriminosos** roubam bilhões de dólares por ano. Atuam em um mercado clandestino onde compram e vendem explorações, ferramentas, dados pessoais e propriedade intelectual roubados, e atacam de pequenos consumidores a grandes empresas.

### 2.8 Responsabilidades de Segurança

Os atores de ameaça **não escolhem vítimas**: atacam usuários domésticos, pequenas e médias empresas e grandes organizações. Por isso, a segurança é uma **responsabilidade compartilhada**: cada pessoa deve denunciar crimes cibernéticos, desconfiar de ameaças no e-mail e na web e proteger suas informações.

As organizações devem seguir uma lista de tarefas como:

- fornecedor de TI (tecnologia da informação) confiável;
- software de segurança atualizado;
- testes de penetração regulares;
- backup em nuvem e em disco rígido;
- troca periódica da senha do Wi-Fi;
- política de segurança atualizada;
- exigência de senhas fortes;
- **autenticação de dois fatores**, que pede uma segunda prova além da senha, como um código no celular.

### 2.9 Indicadores de Comprometimento e de Ataque

Todo ataque tem características que permitem identificá-lo. Compartilhar essas características ajuda a evitar novos ataques.

Os **IOCs** (*Indicators of Compromise* — indicadores de comprometimento) são **a evidência de que um ataque ocorreu**. Exemplos:

- os hashes (SHA-256, SHA-1, MD5; o hash é um resumo matemático que identifica o arquivo, como uma impressão digital) e o nome do arquivo de um malware;
- os domínios consultados no DNS (o serviço que traduz nomes, como www.exemplo.com, em endereços IP) e os IPs dos servidores usados no ataque;
- as alterações que o malware faz no sistema;
- em um e-mail falso de prêmio: o fato de a pessoa não participar de sorteio, o IP do remetente, o assunto, o link e o anexo.

Os **IOAs** (*Indicators of Attack* — indicadores de ataque) tratam da **motivação e das estratégias** do atacante. Como as estratégias se repetem em vários ataques, defender-se de uma delas protege contra ataques futuros parecidos, o que permite uma **segurança proativa**.

| Indicador | Foco | Tipo de defesa |
| --- | --- | --- |
| IOC | Evidências de um ataque que já aconteceu | Reativa |
| IOA | Estratégias e motivação do atacante | Proativa |

### 2.10 Compartilhamento de Ameaças e Conscientização

Os governos promovem a segurança cibernética e o compartilhamento de informações:

- a **CISA** (*Cybersecurity and Infrastructure Security Agency*), dos EUA, usa o **AIS** (*Automated Indicator Sharing* — compartilhamento automatizado de indicadores) para trocar indicadores de ataque entre o governo e o setor privado, sem custo, assim que as ameaças são verificadas;
- a CISA e a **NCSA** (*National Cyber Security Alliance*) fazem em outubro uma campanha anual, o **mês nacional de conscientização em segurança cibernética** (NCSAM, *National Cyber Security Awareness Month*), com temas como redes sociais, configurações de privacidade, aplicativos, atualizações, compras on-line, Wi-Fi e dados de clientes;
- a **ENISA** (Agência da União Europeia para a Cibersegurança) tem papel semelhante ao da CISA nos países da União Europeia.

## 3. Domínios e Tipos de Ameaças

Para se proteger, a empresa precisa saber onde estão suas vulnerabilidades. Um **domínio de ameaça** é uma **área de controle, autoridade ou proteção que os atacantes podem explorar** para entrar em um sistema.

### 3.1 Formas de Explorar um Domínio

Os atacantes podem explorar um domínio por meio de:

- acesso físico direto aos sistemas e às redes;
- redes sem fio que ultrapassam os limites da empresa;
- Bluetooth ou **NFC** (*Near Field Communication* — comunicação por aproximação);
- anexos de e-mail maliciosos;
- elos menos seguros da **cadeia de fornecimento**, isto é, fornecedores e parceiros;
- contas da empresa em redes sociais;
- mídia removível, como pen drives;
- aplicativos na nuvem.

### 3.2 Tipos de Ameaças Cibernéticas

Classificar as ameaças ajuda a avaliar a probabilidade de cada uma e o impacto financeiro, para priorizar os esforços. As categorias são:

| Categoria | Exemplos |
| --- | --- |
| Ataques de software | Ataque DoS bem-sucedido; vírus de computador |
| Erros de software | Bug (defeito no programa); aplicativo fora do ar; falha de *cross-site scripting* (o site exibe código malicioso enviado por um atacante, que roda no navegador das vítimas); compartilhamento ilegal em servidor de arquivos |
| Sabotagem | Usuário autorizado que invade o banco de dados principal; desfiguração (*defacement*) do site da empresa |
| Erro humano | Erros de digitação; firewall mal configurado |
| Roubo | Notebooks ou equipamentos levados de uma sala destrancada |
| Falhas de hardware | Disco rígido que trava |
| Interrupção de serviços básicos | Falta de energia; danos por água de um sprinkler (chuveiro automático contra incêndio) com defeito |
| Desastres naturais | Furacões, tornados, terremotos, inundações e incêndios |

Os criminosos muitas vezes **combinam duas ou mais táticas**, e cabe aos profissionais de segurança educar as pessoas sobre elas.

### 3.3 Ameaças ao Usuário

O **domínio do usuário** inclui todos os que acessam os sistemas da empresa: funcionários, clientes e parceiros. Os usuários são considerados **o elo mais fraco** da segurança. As principais ameaças são:

| Ameaça | Explicação |
| --- | --- |
| Falta de conscientização | O usuário não conhece os dados confidenciais, as políticas, as tecnologias e as contramedidas |
| Políticas mal aplicadas | O usuário não entende as políticas nem as consequências de descumpri-las |
| Roubo de dados | Causa prejuízo financeiro, dano à reputação e responsabilidade legal |
| Downloads e mídias não autorizados | Fotos, músicas, jogos e aplicativos baixados e discos externos ou pen drives são a origem de muitas infecções |
| VPNs não autorizadas | A criptografia esconde o roubo de dados, porque o administrador não consegue acompanhar a transmissão |
| Sites não autorizados | Pedem para baixar scripts (pequenos programas) ou plug-ins (complementos do navegador) com código malicioso ou *adware* (programa que exibe propagandas) e podem até assumir câmeras e aplicativos |
| Destruição de sistemas ou dados | Ativistas, funcionários insatisfeitos ou concorrentes apagam dados ou destroem dispositivos |

**Importante:** nenhuma tecnologia torna os sistemas mais seguros do que **o comportamento das pessoas** que os usam.

### 3.4 Ameaças aos Dispositivos

As principais ameaças aos dispositivos são:

- equipamentos ligados e sem supervisão, que permitem acesso não autorizado;
- arquivos, fotos, músicas ou vídeos de fontes não confiáveis, que podem executar código malicioso;
- vulnerabilidades dos programas instalados, exploradas para iniciar ataques;
- novos vírus, worms e outros malwares (programas maliciosos, explicados no módulo 5) descobertos todos os dias;
- pen drives, CDs ou DVDs não autorizados;
- violação proposital das políticas, que pode trazer consequências graves ao usuário;
- **hardware ou software desatualizado**, que deixa os sistemas mais vulneráveis.

### 3.5 Ameaças à Rede Local e à Nuvem

A **LAN** é o conjunto de dispositivos de uma mesma área ligados por cabo ou sem fio. Como dá acesso aos sistemas e dados, precisa de **segurança forte e controle de acesso rigoroso**. As ameaças são:

- acesso não autorizado a armários de fiação, data centers e salas de computadores;
- acesso não autorizado a sistemas, aplicativos e dados;
- vulnerabilidades e falta de atualização do sistema operacional de rede e dos programas;
- usuários desonestos entrando na rede sem fio;
- explorações de dados em trânsito;
- servidores com hardware ou sistemas diferentes, que dificultam a gestão;
- sondagem e **varredura de portas** não autorizadas;
- firewalls mal configurados.

A **nuvem privada** reúne servidores e recursos disponíveis pela internet **para uma única organização**. Mesmo parecendo mais segura, tem ameaças:

- sondagem e varredura de portas não autorizadas;
- acesso não autorizado aos recursos;
- vulnerabilidades e erros de configuração de roteadores, firewalls e outros dispositivos;
- usuários remotos que baixam dados confidenciais.

A **nuvem pública** reúne serviços oferecidos por um provedor **ao público e compartilhados entre organizações**, em três modelos de assinatura:

| Modelo | O que oferece |
| --- | --- |
| SaaS (*Software as a Service*) | **Software hospedado na nuvem**, usado pelo navegador ou por um aplicativo |
| PaaS (*Platform as a Service*) | **Plataforma** para desenvolver, executar e gerenciar aplicativos com as ferramentas do provedor |
| IaaS (*Infrastructure as a Service*) | **Recursos virtuais**: servidores, armazenamento e outros componentes de infraestrutura |

O provedor protege o ambiente, mas **cada organização protege seus próprios recursos**. As ameaças mais comuns são violações de dados, perda ou roubo de propriedade intelectual, credenciais comprometidas e sequestro de contas, engenharia social e violação de conformidade (descumprimento de leis e normas).

### 3.6 Ameaças aos Aplicativos e às Instalações

O **domínio dos aplicativos** inclui os sistemas, aplicativos e dados críticos para as operações, cada vez mais levados para a nuvem pública. As ameaças são:

- acesso não autorizado a data centers, salas, armários de fiação ou sistemas;
- servidor fora do ar durante a manutenção;
- vulnerabilidades do sistema operacional de rede;
- perda de dados;
- vulnerabilidades no desenvolvimento de aplicativos cliente-servidor ou web.

O **domínio das instalações físicas** trata do acesso físico aos prédios, salas e equipamentos.

| Domínio | O que inclui |
| --- | --- |
| Usuário | Pessoas que acessam os sistemas |
| Dispositivo | Computadores, celulares e mídias |
| LAN | Rede local com e sem fio |
| Nuvem privada | Recursos de uma só organização |
| Nuvem pública | Serviços compartilhados (SaaS, PaaS, IaaS) |
| Aplicativo | Sistemas e dados críticos |
| Instalações físicas | Prédios, salas e equipamentos |

### 3.7 Complexidade das Ameaças

As vulnerabilidades de software surgem de **erros de programação**, **falhas de protocolos** ou **má configuração**, e os ataques estão cada vez mais sofisticados. Dois exemplos:

- **APT** (*Advanced Persistent Threat* — ameaça persistente avançada): **ataque contínuo e discreto**, com táticas de espionagem, vários agentes e malware sofisticado; o atacante **fica sem ser detectado por muito tempo**; costuma visar governos e grandes organizações e é bem financiado;
- **ataques de algoritmo**: usam algoritmos de programas legítimos para gerar comportamentos indesejados; por exemplo, o algoritmo que mede o consumo de energia pode ser usado para escolher alvos ou gerar alertas falsos, ou o computador pode ser travado ao consumir toda a memória RAM (a memória de trabalho) ou a CPU (o processador).

### 3.8 Inteligência de Ameaças

Muitas empresas usam **dados de inteligência de ameaças** para entender o risco e planejar a prevenção e a resposta. Alguns são fechados e pagos; outros são **OSINT** (*Open Source Intelligence* — inteligência de fontes abertas), obtidos em fontes públicas. Governos, universidades, saúde e empresas privadas compartilham cada vez mais esses dados.

As principais fontes de pesquisa são:

| Fonte | O que é |
| --- | --- |
| CVE (*Common Vulnerabilities and Exposures*) | **Dicionário público de vulnerabilidades**, patrocinado pelo US-CERT (a equipe de resposta a emergências de computação dos EUA) e pelo Departamento de Segurança Interna dos EUA e mantido pela MITRE (organização americana sem fins lucrativos de pesquisa); cada falha recebe um código, como CVE-2021-44228; cada entrada tem um número padrão, uma descrição e referências |
| Dark web | Conteúdo criptografado, **fora dos buscadores**, que exige software ou autorização específica; pesquisadores a monitoram em busca de novas ameaças |
| IOC | Assinaturas de malware ou nomes de domínio que provam e detalham uma violação |
| AIS | Troca de indicadores da CISA em tempo real, usando a linguagem **STIX** (*Structured Threat Information Expression*) e o protocolo **TAXII** (*Trusted Automated Exchange of Intelligence Information*) |

## 4. Engenharia Social e Outros Métodos de Engano

Depois de conhecer as vulnerabilidades de um alvo, o criminoso se esforça para **enganar as vítimas** e obter informações confidenciais. A maioria dos ataques envolve algum tipo de fraude.

### 4.1 Engenharia Social

A **engenharia social** é uma **estratégia não técnica que manipula pessoas** para que façam algo ou revelem informações confidenciais. Em vez de falhas de software ou hardware, ela **explora a natureza humana**: a vontade de ajudar e fraquezas como a ganância e a vaidade. Os principais tipos são:

- **pretexto** (*pretexting*): o atacante **mente para obter dados**; por exemplo, finge precisar dos dados pessoais ou financeiros da vítima para confirmar a identidade dela;
- **quid pro quo** ("algo por algo"): pede informações pessoais **em troca de algo**, como um e-mail que promete férias grátis;
- **fraude de identidade**: usa a identidade roubada de alguém para obter bens ou serviços, como um cartão de crédito no nome da vítima.

### 4.2 Táticas de Engenharia Social

As táticas exploram reações humanas previsíveis:

| Tática | Como funciona | Exemplo |
| --- | --- | --- |
| Autoridade | As pessoas **obedecem a quem parece ter autoridade** | Executivo abre uma "intimação oficial" que é um PDF infectado |
| Intimidação | O criminoso **pressiona** a vítima | Ligação acusando a secretária de corromper os arquivos do chefe e exigindo que os envie já, sob risco de demissão |
| Consenso (prova social) | As pessoas **fazem o que os outros fazem** | Post de "oportunidade de negócio" com dezenas de comentários falsos que a validam |
| Escassez | As pessoas agem quando há **pouca quantidade** | Item de luxo barato com "poucas unidades" |
| Urgência | As pessoas agem quando há **pouco tempo** | Frete grátis "por tempo limitado" |
| Familiaridade | As pessoas atendem a **quem conhecem ou de quem gostam** | Perfil clonado de um amigo em rede social |
| Confiança | O criminoso **constrói uma relação** com a vítima, o que leva mais tempo | Falso especialista que "descobre um erro grave" e, ao corrigi-lo, invade o sistema |

As táticas podem ser **combinadas** para aumentar as chances de sucesso.

### 4.3 Olhar por Cima do Ombro e Vasculhar o Lixo

O **shoulder surfing** (olhar por cima do ombro) é **observar o alvo para obter informações** como senhas, PINs (as senhas numéricas, como a do cartão) e dados de cartão. O criminoso pode usar binóculos ou câmeras. Por isso, a tela do caixa eletrônico só é visível de certos ângulos.

O **dumpster diving** (mergulho no lixo) é **examinar o lixo do alvo** em busca de informações descartadas. Por isso, documentos confidenciais devem ser **triturados** ou guardados em sacos de queima até serem incinerados.

### 4.4 Falsificação de Identidade, Farsas e Entrada Indevida

Outras técnicas de engano são:

- **representação** (*impersonation*): **fingir ser outra pessoa** para induzir a vítima a agir; por exemplo, um falso funcionário da Receita que exige um pagamento imediato sob ameaça de prisão. Também é usada para **minar a credibilidade da vítima**, publicando em nome dela;
- **farsa** (*hoax*): mensagem enganosa que causa o mesmo transtorno de uma violação real, como o aviso de um vírus inexistente que pede para ser repassado a todos e espalha medo pelo e-mail e pelas redes sociais;
- **piggybacking** ou **tailgating** (carona): o criminoso **segue uma pessoa autorizada para entrar** em uma área restrita, dando a impressão de estar acompanhado, misturando-se a um grupo ou visando alguém descuidado com as regras.

Uma defesa contra a carona é a **mantrap** (eclusa): duas portas em sequência, em que **a externa precisa fechar antes de a interna abrir**.

### 4.5 Outros Métodos de Engano

Os atacantes ainda usam:

| Método | Como funciona |
| --- | --- |
| Fraude de fatura | Fatura falsa, muitas vezes com linguagem urgente ou ameaçadora, que leva a vítima a pagar ou a digitar credenciais em uma tela de login falsa |
| Ataque de bebedouro (*watering hole*) | O atacante descobre **quais sites a empresa usa** e infecta um ou mais deles com malware |
| Typosquatting | Registra endereços parecidos com os verdadeiros e explora **erros de digitação** na URL (o endereço do site, como www.exemplo.com.br) para coletar dados pessoais ou financeiros; exemplo: "gooogle.com" |
| Adendo (*prepending*) | **Remove a etiqueta "externo"** que a empresa coloca nos e-mails de fora, para que a mensagem pareça interna |
| Campanhas de influência | Muito usadas na guerra cibernética; combinam **notícias falsas**, desinformação e publicações em redes sociais |

### 4.6 Defesa Contra o Engano

As empresas precisam **conscientizar e treinar** os funcionários. As principais recomendações são:

- nunca revelar informações confidenciais ou credenciais a desconhecidos, por qualquer meio;
- resistir a e-mails e links atraentes;
- desconfiar de downloads automáticos ou não solicitados;
- criar políticas de segurança e ensiná-las aos funcionários;
- incentivar os funcionários a assumir responsabilidade pela segurança;
- **não ceder à pressão** de desconhecidos.

## 5. Malware e Sua Mitigação

O **malware** (*malicious software*) é **qualquer código usado para roubar dados, contornar o controle de acesso ou danificar e comprometer um sistema**. Ele é a ferramenta de muitos ataques. Este módulo apresenta os tipos de malware e, em seguida, como impedir que eles entrem e se espalhem.

### 5.1 Vírus, Worms e Cavalos de Troia

Os três tipos clássicos de malware diferem na forma de se espalhar:

- **vírus**: programa que, ao ser executado, **se replica e se anexa a outros arquivos**, inserindo seu código em programas legítimos. A maioria **exige uma ação do usuário** para ser ativada, como abrir um arquivo, e pode ser programada para agir em uma data ou hora. Espalha-se por pen drives, downloads e anexos, infecta outros programas e computadores e **sofre mutações para escapar da detecção**. Exemplo: o vírus **Melissa** (1999), espalhado por e-mail, com prejuízo estimado em US$ 1,2 bilhão;
- **worm** (verme): **replica-se sozinho explorando vulnerabilidades das redes**. Ao contrário do vírus, **não precisa de um programa hospedeiro** nem da participação do usuário depois da infecção inicial, e se espalha muito rápido, deixando a rede lenta. Todo worm explora uma vulnerabilidade, tem um meio de se propagar e carrega uma **carga útil** (*payload*), o código que causa o dano. Exemplo: o **Code Red** infectou mais de 300 mil servidores em 19 horas, em 2001;
- **cavalo de Troia** (*trojan*): **parece legítimo, mas esconde sua intenção maliciosa**. Usa os privilégios de quem o executa e, ao contrário do vírus, **não se replica**; costuma vir junto de arquivos como imagens, áudio ou vídeo, que servem de isca.

| Malware | Precisa de hospedeiro? | Precisa do usuário? | Replica-se? |
| --- | --- | --- | --- |
| Vírus | Sim | Sim, para ser ativado | Sim |
| Worm | Não | Só na infecção inicial | Sim, sozinho pela rede |
| Cavalo de Troia | Disfarça-se de programa legítimo | Sim | Não |

### 5.2 Backdoors e Rootkits

Um **backdoor** (porta dos fundos) dá **acesso não autorizado a um sistema contornando a autenticação normal**. Exemplos: **Netbus** e **Back Orifice**. Em geral, o criminoso leva um usuário autorizado a executar uma **RAT** (*Remote Administration Tool* — ferramenta de administração remota), que instala o backdoor e dá controle de administrador. O backdoor **mantém o acesso mesmo depois que a vulnerabilidade original é corrigida**.

Um **rootkit** **modifica o sistema operacional para criar um backdoor**. A maioria explora falhas de software para **elevar privilégios** e alterar arquivos do sistema. Também modifica as ferramentas forenses e de monitoramento, por isso é **muito difícil de detectar**. Na maioria dos casos, o computador infectado precisa ser **apagado e reinstalado**.

### 5.3 Bombas Lógicas, Ransomware e Keyloggers

Outros tipos de malware são:

- **bomba lógica**: **fica inativa até um gatilho**, como uma data ou um registro no banco de dados, e então sabota registros, apaga arquivos ou ataca o sistema. Algumas **destroem o hardware**, sobrecarregando ventiladores, CPU, memória, discos e fontes até superaquecerem;
- **ransomware**: **mantém o sistema ou os dados presos até que um resgate seja pago**, em geral criptografando os dados. O criminoso promete enviar a chave após o pagamento por um meio não rastreável, mas **muitas vítimas não recuperam os dados mesmo pagando**. Espalha-se principalmente por **e-mails de phishing** e por vulnerabilidades de software;
- **keylogger** (registro de teclas): **grava cada tecla digitada** e envia o registro ao criminoso, revelando usuários, senhas e sites visitados. Pode ser software instalado ou um dispositivo físico ligado ao computador. Muitos programas *anti-spyware* o detectam.

**Observação:** o keylogger também tem usos legítimos, como pais que acompanham o uso da internet pelos filhos.

### 5.4 Mitigação de Malware

O **antivírus** é a principal defesa contra o malware: impede que os hosts sejam infectados e espalhem código malicioso. Limpar computadores infectados leva muito mais tempo do que mantê-los atualizados. É o produto de segurança **mais usado** no mercado, de empresas como Symantec, McAfee e Trend Micro, muitas vezes com licenças por volume.

**Importante:** a **atualização automática das definições de vírus** é o requisito mais crítico para manter a rede livre de vírus e deve constar na política de segurança.

O antivírus é **baseado em host**: instalado em computadores e servidores, ele **não impede o vírus de entrar na rede**. Por isso, os dispositivos de segurança no **perímetro** identificam arquivos de malware pelos seus **IOCs** e os retiram do tráfego antes que causem um incidente. Os atacantes alteram o malware para escapar dessa detecção, e **nenhuma técnica é 100% eficaz**: incidentes vão acontecer.

### 5.5 Mitigação de Worms

Os worms dependem mais da rede que os vírus, e combatê-los exige coordenação. A resposta tem **quatro fases**:

1. **contenção**: **limita a propagação** às áreas já afetadas, segmentando a rede com **ACLs** (*Access Control Lists*, listas de regras que permitem ou bloqueiam tráfego) de entrada e saída em roteadores e firewalls;
2. **inoculação**: ao mesmo tempo ou logo depois, **aplica a correção do fabricante em todos os sistemas não infectados**, tirando alvos do worm;
3. **quarentena**: **identifica as máquinas infectadas** dentro das áreas contidas e as desconecta, bloqueia ou remove;
4. **tratamento**: **desinfecta** os sistemas: encerra o processo do worm, remove arquivos e configurações alterados e corrige a vulnerabilidade; nos casos graves, reinstala o sistema.

Contenção → Inoculação → Quarentena → Tratamento

## 6. Outros Ataques Cibernéticos e Boas Práticas de Defesa

Além do malware, os atacantes **derrubam serviços, interceptam comunicações e exploram falhas ainda desconhecidas**. Este módulo reúne esses ataques e fecha com as boas práticas que protegem a rede contra todos eles.

### 6.1 Negação de Serviço

Os ataques de **negação de serviço** (**DoS**) são **simples de fazer, mesmo por atacantes sem experiência**, e interrompem os serviços, com grande perda de tempo e dinheiro. Até a **tecnologia operacional**, que controla processos físicos em prédios, fábricas e serviços públicos, pode ser afetada e desligada. Há dois tipos principais:

- **tráfego esmagador**: a rede, o host ou o aplicativo recebe **mais dados do que consegue processar**, o que deixa a transmissão lenta ou derruba o serviço;
- **pacotes maliciosamente formatados**: o atacante envia pacotes com erros que o receptor **não consegue tratar**, o que o deixa lento ou o faz travar.

O **DDoS** (*Distributed Denial of Service* — negação de serviço distribuída) é semelhante, mas **parte de muitas fontes coordenadas**:

1. o atacante monta uma **botnet**, uma rede de computadores infectados chamados **zumbis**, controlados por sistemas manipuladores (*handlers*);
2. os zumbis procuram e infectam outros hosts, criando mais zumbis;
3. quando está pronto, o atacante manda os manipuladores ordenarem o ataque.

Atacante → Manipuladores → Zumbis → Alvo

![No DDoS, o atacante comanda os manipuladores, que comandam os zumbis da botnet; todos atacam o mesmo alvo](img/endpoint/end_ddos.png){width=6in}

### 6.2 Homem no Meio e Ataques de Repetição

Os atacantes podem **interceptar ou alterar a comunicação** entre dois dispositivos:

- **MitM** (*Man-in-the-Middle* — homem no meio): o criminoso assume o controle de um dispositivo sem que o usuário saiba e passa a **interceptar, manipular e retransmitir** informações entre a origem e o destino;
- **MitMo** (*Man-in-the-Mobile* — homem no celular): variação que **assume o controle do celular** da vítima e envia as informações aos atacantes. Exemplo: o malware **ZeuS** captura em silêncio os SMS (mensagens de texto) com os códigos de verificação em duas etapas;
- **ataque de repetição** (*replay*): o atacante **captura uma comunicação e a retransmite**, ou a atrasa, para enganar o destinatário e contornar a autenticação.

### 6.3 Ataques de Dia Zero

Um **ataque de dia zero** **explora uma vulnerabilidade antes que ela seja conhecida ou divulgada pelo fabricante**. A rede fica muito vulnerável entre o momento em que a falha é descoberta (**hora zero**) e o lançamento da correção. A defesa exige uma visão **holística**, de toda a arquitetura da rede.

### 6.4 Ataques Físicos, à IA, à Cadeia de Fornecimento e à Nuvem

Os ataques também vão além da rede e do software:

- **ataques físicos**: ações para destruir, expor, alterar, desativar ou roubar a infraestrutura ou o hardware. Exemplos: pen drive com malware; cabos USB, carregadores e adaptadores com um chip sem fio que permite controlar o dispositivo; leitores que copiam cartões de crédito para criar clones;
- **ataques adversos à inteligência artificial**: o **aprendizado de máquina** (programas que aprendem padrões a partir de exemplos) usa modelos matemáticos que dependem dos dados de entrada; dados corrompidos distorcem o resultado. Exemplo: enganar um veículo autônomo para que leia errado as placas;
- **ataques à cadeia de fornecimento**: interceptam os fornecedores de sistemas, peças e software. Exemplo: alterar a data de fim de vida útil (**EOL**, *End of Life*) de um software para que a empresa perca o suporte;
- **ataques à nuvem**: exploram os dados, aplicações, plataformas e infraestruturas na nuvem (SaaS, PaaS e IaaS), já que o provedor mantém o equipamento, mas a empresa fica exposta a novas ameaças.

### 6.5 Defesa Contra os Ataques

As principais medidas contra esses ataques são:

- configurar o firewall para **descartar pacotes vindos de fora com endereço de origem interno**, que só podem ser falsificados;
- manter **correções e atualizações** em dia;
- **distribuir a carga** entre vários servidores;
- **bloquear o ICMP vindo de fora** no firewall. O **ICMP** (*Internet Control Message Protocol*) envia mensagens de erro e de controle, como se um dispositivo consegue falar com outro, e é muito usado em ataques DoS e DDoS.

### 6.6 Ataques de Acesso e Sua Mitigação

Os **ataques de acesso** tentam **entrar em contas e sistemas sem autorização**. Muitos usam a simples adivinhação de senhas ou **ataques de dicionário e de força bruta**, que testam muitas senhas seguidas. As defesas são:

- **política de autenticação forte**:
  - senhas com **pelo menos oito caracteres**, com letras maiúsculas e minúsculas, números e caracteres especiais;
  - **bloqueio da conta** depois de um número de tentativas erradas;
- **princípio da confiança mínima**: os sistemas não confiam uns nos outros sem necessidade; por exemplo, um servidor confiável não deve confiar sem condições em servidores web;
- **criptografia** no acesso remoto e no tráfego dos protocolos de roteamento, o que reduz as chances de MitM;
- protocolos de autenticação **criptografados ou com hash**;
- **MFA** (*Multi-Factor Authentication* — autenticação multifator): **dois ou mais meios independentes de verificação**, como a senha mais um código por SMS ou um **token de uso único** gerado por software ou dispositivo;
- educação contra engenharia social.

Os ataques de acesso são detectados pela **revisão dos logs**, do uso de banda e da carga dos processos; por exemplo, um número incomum de logins com falha. A política deve exigir logs de todos os dispositivos e servidores.

### 6.7 Boas Práticas de Defesa

Para fechar, as melhores práticas para proteger uma rede contra todos esses ataques são:

- ter uma **política de segurança escrita**;
- educar os funcionários sobre engenharia social e criar formas de **validar identidades** por telefone, e-mail ou pessoalmente;
- controlar o **acesso físico** aos sistemas;
- usar senhas fortes e trocá-las com frequência;
- criptografar e proteger com senha os dados confidenciais;
- usar hardware e software de segurança: firewalls, IPS, VPN, antivírus e filtragem de conteúdo;
- fazer backups e **testá-los** regularmente;
- **desligar serviços e portas desnecessários**;
- instalar as correções semanal ou, se possível, diariamente, porque elas fecham as falhas que os ataques exploram;
- fazer **auditorias de segurança**.

## 7. Vulnerabilidades do IP

Os protocolos são a base da comunicação de dados e, por isso, são alvo dos atacantes há muito tempo. Para reconhecer um ataque, o analista precisa conhecer os campos dos cabeçalhos e saber como podem ser manipulados.

### 7.1 IPv4 e IPv6

O **IP** (*Internet Protocol*) é o protocolo da **camada 3** (camada de rede) que leva um pacote do host de origem ao de destino através de várias redes. Ele é **sem conexão** (não combina nada com o destino antes de enviar) e **não rastreia nem gerencia o fluxo** de pacotes; essas funções ficam com o TCP (*Transmission Control Protocol*), na camada 4, a de transporte.

**Importante:** o IP **não verifica se o endereço de origem é verdadeiro**. Por isso, o atacante pode enviar pacotes com origem falsificada e adulterar outros campos do cabeçalho.

### 7.2 Cabeçalho do IPv4

O cabeçalho do IPv4 tem no mínimo **20 bytes**:

| Campo | Tamanho | Função |
| --- | --- | --- |
| Versão | 4 bits | Valor 0100, que identifica o IPv4 |
| Tamanho do cabeçalho (IHL, *Internet Header Length*) | 4 bits | Tamanho do cabeçalho; mínimo de 20 bytes |
| Serviços diferenciados (DS) | 8 bits | Antigo **ToS** (*Type of Service*); define a prioridade do pacote (por exemplo, voz antes de download): 6 bits de **DSCP** (*Differentiated Services Code Point*, o código de prioridade) e 2 de **ECN** (*Explicit Congestion Notification*, aviso de congestionamento) |
| Tamanho total | 16 bits | Tamanho do pacote com cabeçalho e dados; máximo de 65.535 bytes |
| Identificação, flags e deslocamento do fragmento | 16, 3 e 13 bits | Usados para **fragmentar** o pacote quando a rota não aceita seu tamanho e remontá-lo depois |
| TTL (*Time to Live*) | 8 bits | **Limita a vida do pacote**: cada roteador subtrai 1; ao chegar a zero, o pacote é descartado e o roteador envia à origem um ICMP de **tempo excedido** |
| Protocolo | 8 bits | Protocolo da camada acima; valores comuns: **ICMP (1), TCP (6) e UDP (17)** |
| Soma de verificação do cabeçalho | 16 bits | Calculada sobre o cabeçalho para detectar erros na transmissão |
| Endereço de origem | 32 bits | Sempre um endereço **unicast** (de um único host) |
| Endereço de destino | 32 bits | Endereço IPv4 de destino |
| Opções e preenchimento | 0 ou múltiplo de 32 bits | Opções extras, completadas com zeros até um múltiplo de 32 bits |

### 7.3 Cabeçalho do IPv6

O cabeçalho do IPv6 tem **oito campos e 40 bytes**:

| Campo | Tamanho | Função |
| --- | --- | --- |
| Versão | 4 bits | Valor 0110, que identifica o IPv6 |
| Classe de tráfego | 8 bits | Equivale ao campo DS do IPv4 |
| Rótulo de fluxo | 20 bits | Pacotes com o mesmo rótulo recebem o mesmo tratamento dos roteadores |
| Tamanho da carga útil | 16 bits | Tamanho da parte de dados |
| Próximo cabeçalho | 8 bits | Equivale ao campo Protocolo do IPv4 |
| Limite de saltos | 8 bits | Substitui o TTL; ao chegar a zero, o pacote é descartado e a origem recebe um ICMPv6 de tempo excedido |
| Endereço de origem | 128 bits | Endereço do host que envia |
| Endereço de destino | 128 bits | Endereço do host que recebe |

O IPv6 pode ter **cabeçalhos de extensão** (**EH**, *Extension Headers*), opcionais, entre o cabeçalho e a carga, usados para fragmentação, segurança e mobilidade.

**Observação:** diferentemente do IPv4, **os roteadores não fragmentam pacotes IPv6**.

### 7.4 Ataques ao IP

Os ataques mais comuns ao IP são:

| Ataque | Como funciona |
| --- | --- |
| Ataques ICMP | Usam pings para descobrir sub-redes e hosts, fazer inundações DoS e alterar tabelas de roteamento |
| DoS | Impedem usuários legítimos de acessar informações ou serviços |
| DDoS | Ataque simultâneo e coordenado de várias máquinas |
| Falsificação de endereços | Falsificam o IP de origem, de forma cega ou não cega |
| Homem no meio (MitM) | O atacante se coloca entre a origem e o destino para monitorar, capturar e controlar a comunicação, apenas espiando ou alterando os pacotes |
| Sequestro de sessão | Com acesso à rede física, o atacante usa um MitM para assumir uma sessão |

### 7.5 Ataques ICMP

O **ICMP** transporta **mensagens de diagnóstico e de erro** quando rotas, hosts ou portas não estão disponíveis. O comando **ping** envia uma **solicitação de eco** (*echo request*) para testar a conexão, e o destino devolve uma **resposta de eco** (*echo reply*).

Os atacantes usam o ICMP para **reconhecimento e varredura**: mapear a topologia, descobrir os hosts ativos, identificar o sistema operacional (**impressão digital do sistema operacional**) e saber o estado de um firewall. Também o usam em ataques DoS e DDoS (ver item 6.1), como a **inundação ICMP**, com pedidos de eco de origem falsificada. As mensagens de maior interesse para o atacante são:

| Mensagem ICMP | Uso no ataque |
| --- | --- |
| Solicitação e resposta de eco | Verificação de hosts e DoS |
| Destino inacessível | Reconhecimento e varredura |
| Resposta de máscara | Mapear a rede interna |
| Redirecionamento | Fazer o host enviar todo o tráfego por um dispositivo comprometido (MitM) |
| Descoberta de roteador | Injetar rotas falsas na tabela de roteamento do alvo |

**Observação:** o ICMPv4 e o ICMPv6 são vulneráveis a ataques semelhantes.

A defesa é uma **filtragem rigorosa de ICMP por ACL** (*Access Control List* — lista de regras que permite ou bloqueia tráfego) **na borda da rede**, para impedir sondagens vindas da internet. Os analistas observam o tráfego capturado e os logs, e, em redes grandes, firewalls e **IDS** (*Intrusion Detection System* — sistema de detecção de intrusão) geram alertas.

### 7.6 Amplificação e Reflexão

Os atacantes usam a **amplificação e a reflexão** para criar ataques DoS. No **ataque Smurf**:

1. **amplificação**: o atacante envia pedidos de eco ICMP a **muitos hosts**, com o **IP da vítima como origem**;
2. **reflexão**: todos os hosts **respondem à vítima**, que fica sobrecarregada.

Atacante → Pedidos com o IP da vítima → Muitos hosts → Respostas → Vítima

![No ataque Smurf, os pedidos de eco levam o IP da vítima como origem, e todas as respostas caem sobre ela](img/endpoint/end_smurf.png){width=6in}

Hoje também são usadas a reflexão e amplificação pelo **DNS** e pelo **NTP** (*Network Time Protocol*, protocolo que sincroniza relógios). Os atacantes ainda usam **ataques de exaustão de recursos**, que consomem os recursos do alvo ou da rede até travá-los.

### 7.7 Falsificação de Endereços

A **falsificação de endereço IP** (*IP spoofing*) cria pacotes com **origem falsa** para **esconder a identidade** do remetente ou **se passar por um usuário legítimo**, obtendo acesso a dados ou contornando a segurança. Costuma fazer parte de outro ataque, como o Smurf. Pode ser:

- **não cega**: o atacante **vê o tráfego** entre o host e o destino; serve para inspecionar a resposta da vítima, descobrir o estado de um firewall, **prever números de sequência** (a numeração que o TCP dá aos dados de cada conexão, explicada no item 8.2) e sequestrar uma sessão;
- **cega**: o atacante **não vê o tráfego**; serve para ataques DoS.

A **falsificação de endereço MAC** exige acesso à rede interna. O **endereço MAC** (*Media Access Control*) é o endereço físico da placa de rede, e o switch guarda em sua **tabela CAM** (*Content Addressable Memory*, a tabela de endereços MAC) em qual porta está cada MAC. O ataque ocorre assim:

1. o atacante troca o MAC do seu computador pelo **MAC de um alvo**, como um servidor;
2. envia um quadro com esse MAC;
3. o switch **atualiza a tabela CAM**, associando o MAC à porta do atacante;
4. o switch passa a **encaminhar ao atacante** os quadros destinados ao alvo.

Também há falsificação de **aplicativos e serviços**: por exemplo, conectar um **servidor DHCP falso** (o DHCP é o serviço que distribui endereços IP automaticamente) para criar uma condição MitM (ver item 6.2).

### 7.8 Mitigação de Ataques de Reconhecimento

Os **ataques de reconhecimento** **precedem outros ataques**: o atacante coleta informações para depois invadir ou derrubar a rede. Eles são detectados por **alarmes** que disparam quando um limite é ultrapassado, como o número de pedidos ICMP por segundo. O **Cisco ASA** (*Adaptive Security Appliance*) oferece prevenção de intrusão em um dispositivo próprio, e os roteadores **Cisco ISR** (*Integrated Services Routers*) a oferecem com software adicional.

As medidas são:

- **autenticação**, para garantir o acesso adequado;
- **criptografia**, que torna inútil o **sniffer de pacotes** (programa que captura o tráfego), porque os dados capturados ficam ilegíveis;
- **ferramentas anti-sniffer**, que detectam mudanças no tempo de resposta dos hosts, sinal de que processam mais tráfego que o normal;
- **infraestrutura comutada**, com switches;
- **firewall e IPS**.

**Observação:** é **impossível impedir a varredura de portas**, mas o IPS e o firewall limitam o que ela descobre. Desligar o eco ICMP nos roteadores de borda impede as varreduras de ping, mas **perde os dados de diagnóstico**, e a varredura de portas pode ser feita sem ping, apenas mais devagar.

## 8. Vulnerabilidades do TCP e do UDP

Além do IP, os atacantes exploram os protocolos da **camada 4** (transporte): o TCP e o UDP. As aplicações de rede usam portas TCP ou UDP, e o atacante faz **varreduras de portas** para descobrir quais serviços o alvo oferece.

### 8.1 Cabeçalho do TCP

O segmento **TCP** (*Transmission Control Protocol*) vem logo depois do cabeçalho IP. Seu cabeçalho tem **20 bytes** sem opções:

| Campo | Tamanho (bits) |
| --- | --- |
| Porta de origem | 16 |
| Porta de destino | 16 |
| Número de sequência | 32 |
| Número de confirmação | 32 |
| Tamanho do cabeçalho | 4 |
| Reservado | 6 |
| Bits de controle | 6 |
| Janela | 16 |
| Soma de verificação | 16 |
| Urgente | 16 |
| Opções | 0 ou 32 |

Os **seis bits de controle** (*flags*) são:

- **URG**: o campo de ponteiro urgente é significativo;
- **ACK**: o campo de confirmação é significativo;
- **PSH**: função *push* (entregar os dados ao aplicativo imediatamente, sem esperar juntar mais);
- **RST**: redefine (encerra) a conexão;
- **SYN**: sincroniza os números de sequência;
- **FIN**: o remetente não tem mais dados.

### 8.2 Serviços do TCP

O TCP oferece três serviços:

- **entrega confiável**: usa **confirmações** (*acknowledgments*) e retransmite o que não foi confirmado a tempo, o que pode causar atrasos; usado por HTTP, SSL/TLS, FTP e transferências de zona do DNS;
- **controle de fluxo**: vários segmentos são confirmados por uma única confirmação;
- **comunicação com estado** (*stateful*): antes de enviar dados, os dois lados abrem a conexão com o **handshake de três vias**.

O **handshake de três vias** ocorre assim:

1. o cliente envia **SYN**, pedindo a sessão cliente-servidor (exemplo: SEQ=100);
2. o servidor responde **SYN-ACK**, confirmando e pedindo a sessão servidor-cliente (SEQ=300, ACK=101);
3. o cliente envia **ACK**, confirmando (SEQ=101, ACK=301), e a sessão é estabelecida.

SYN → SYN-ACK → ACK

O encerramento normal usa **quatro mensagens**:

1. o cliente envia **FIN** quando não tem mais dados;
2. o servidor responde **ACK**;
3. o servidor envia seu **FIN**;
4. o cliente responde **ACK**.

### 8.3 Ataques ao TCP

Os principais ataques ao TCP são:

- **inundação SYN**: o atacante envia **muitos SYN com IPs de origem falsificados**; o servidor responde com SYN-ACK e **espera ACKs que nunca chegam**. Com tantas **conexões semiabertas**, o serviço é negado aos usuários legítimos;
- **ataque de redefinição** (*TCP reset*): o atacante envia um pacote falsificado com **RST** a um ou aos dois lados, o que **encerra a conexão de forma abrupta**;
- **sequestro de sessão TCP**: difícil de executar; o atacante **assume um host já autenticado**: falsifica o IP de um dos lados, **prevê o próximo número de sequência** e envia um ACK ao outro. Se der certo, **pode enviar dados, mas não recebê-los**.

![Na inundação SYN, o servidor guarda cada conexão semiaberta à espera de um ACK que nunca chega](img/endpoint/end_synflood.png){width=6in}

### 8.4 Funcionamento do UDP

O **UDP** (*User Datagram Protocol*) é usado pelo DNS, pelo DHCP, pelo **TFTP** (*Trivial File Transfer Protocol*, transferência simples de arquivos), pelo **NFS** (*Network File System*, compartilhamento de arquivos em rede), pelo **SNMP** (*Simple Network Management Protocol*, monitoramento de equipamentos) e por aplicações em tempo real, como streaming de vídeo e VoIP (telefonia pela internet). É **sem conexão** e tem **sobrecarga muito menor** que o TCP, porque não oferece retransmissão, sequenciamento nem controle de fluxo. Seu cabeçalho tem só **8 bytes**: porta de origem, porta de destino, comprimento e soma de verificação, com 16 bits cada.

**Observação:** o UDP divide os dados em **datagramas**, mas o termo genérico "segmento" também é usado.

Chamar o UDP de "não confiável" não significa que ele seja inferior: as funções de confiabilidade, se necessárias, ficam em outra camada. Ele é ideal para transações simples de pedido e resposta, como o DHCP; se não houver resposta, o dispositivo reenvia o pedido.

### 8.5 Ataques ao UDP

O UDP **não tem criptografia** por padrão. Qualquer um pode ver o tráfego, alterá-lo e reenviá-lo. A soma de verificação é **opcional**, e o atacante pode recalculá-la para os novos dados, de modo que o destino não perceba a alteração. Esse ataque é pouco usado.

Mais comum é a **inundação UDP**, que consome todos os recursos da rede:

1. o atacante usa uma ferramenta como **UDP Unicorn** ou **LOIC** (*Low Orbit Ion Cannon*);
2. envia muitos pacotes UDP, em geral de origem falsificada, a um servidor, **varrendo as portas** em busca de portas fechadas;
3. o servidor responde a cada uma com um ICMP (ver item 7.5) de **porta inacessível**;
4. o excesso de tráfego consome a largura de banda, com efeito semelhante ao de um DoS.

| Protocolo | Ataque | Efeito |
| --- | --- | --- |
| TCP | Inundação SYN | Conexões semiabertas esgotam o servidor |
| TCP | Redefinição (RST) | Conexão encerrada à força |
| TCP | Sequestro de sessão | Atacante envia dados como um host autenticado |
| UDP | Alteração dos dados | Dados mudados sem o destino perceber |
| UDP | Inundação UDP | Largura de banda consumida |

## 9. Ataques ao ARP, aos Switches e ao DHCP

Proteger a base da rede não basta: os protocolos que fazem a rede funcionar no dia a dia também são alvos. Os primeiros são os serviços da rede local.

### 9.1 Funcionamento do ARP

O **ARP** (*Address Resolution Protocol*) **descobre o endereço MAC de um host a partir do seu endereço IP**, já que, dentro da rede local, os quadros são entregues pelo MAC:

1. o host envia uma **solicitação ARP em difusão** (*broadcast*) para todos: "qual é o MAC de 192.168.1.7?";
2. todos os hosts da sub-rede recebem e processam a solicitação;
3. só o dono do IP responde com uma **resposta ARP** contendo seu MAC;
4. o host guarda o par IP–MAC no seu **cache ARP** e envia os dados.

Qualquer host pode enviar uma resposta não solicitada, o **ARP gratuito**, em geral ao ligar, para anunciar seu MAC. Os outros hosts **guardam o par IP–MAC sem verificar**.

**Importante:** como o ARP não tem autenticação, **qualquer host pode se declarar dono de qualquer IP ou MAC**.

### 9.2 Envenenamento do Cache ARP

O **envenenamento do cache ARP** (*ARP spoofing* ou *ARP poisoning*) envia **respostas ARP falsas** para **associar o MAC do atacante ao IP de outro dispositivo**, em geral o **gateway padrão** (o roteador que dá saída da rede local). Assim, o atacante fica **entre a vítima e o resto da rede**, em um ataque MitM. Exemplo:

1. o PC-A (192.168.10.10, MAC AA:AA:AA:AA:AA:AA) pede o MAC do gateway R1 (192.168.10.1);
2. o R1 responde com seu MAC verdadeiro (A1:A1:A1:A1:A1:A1), e os dois atualizam seus caches;
3. o atacante (MAC EE:EE:EE:EE:EE:EE) envia **duas respostas ARP gratuitas falsas**: "192.168.10.1 tem EE:EE:EE:EE:EE:EE" para o PC-A e "192.168.10.10 tem EE:EE:EE:EE:EE:EE" para o R1;
4. os dois atualizam seus caches, e **todo o tráfego entre eles passa pelo atacante**.

![Com duas respostas ARP falsas, o atacante se coloca entre o PC e o gateway](img/endpoint/end_arp.png){width=6in}

O envenenamento pode ser:

- **passivo**: o atacante **rouba informações** confidenciais;
- **ativo**: o atacante **modifica os dados em trânsito ou injeta dados maliciosos**.

Há muitas ferramentas para esse ataque, como **dsniff**, **Cain & Abel**, **ettercap** e **Yersinia**.

### 9.3 Ataques aos Switches

O **switch** liga os dispositivos da rede local e encaminha cada quadro apenas à porta do destino, consultando sua **tabela de endereços MAC** (tabela CAM). Os ataques de camada 2 exploram esse funcionamento:

- **falsificação de MAC**: o atacante disfarça seu dispositivo com o MAC de um dispositivo válido; assim **contorna a autenticação** e o switch passa a lhe enviar os quadros do outro;
- **inundação de MAC** (*MAC flooding*): o atacante **inunda o switch com endereços MAC falsos**, comprometendo a segurança do switch e os dados transmitidos.

| Ataque | O que falsifica | Resultado |
| --- | --- | --- |
| Falsificação de MAC | O MAC de um dispositivo válido | Recebe os quadros do outro e contorna a autenticação |
| Envenenamento ARP | A associação entre IP e MAC | MitM entre a vítima e o gateway |
| Falsificação de IP | O IP de origem | Esconde a identidade ou se passa por outro |
| Inundação de MAC | Muitos MACs falsos | Compromete o switch |

### 9.4 Funcionamento do DHCP

O **DHCP** (*Dynamic Host Configuration Protocol*) **fornece automaticamente aos clientes a configuração IP**: endereço, máscara, gateway padrão, servidor DNS e tempo de concessão. A troca normal tem quatro mensagens:

1. **DHCPDISCOVER** (difusão): o cliente procura um servidor;
2. **DHCPOFFER** (direta, *unicast*): o servidor oferece um endereço, por exemplo 192.168.10.15/24 com gateway 192.168.10.1 e concessão de 3 dias;
3. **DHCPREQUEST** (difusão): o cliente aceita a oferta;
4. **DHCPACK** (direta): o servidor confirma.

Discover → Offer → Request → ACK

### 9.5 Falsificação de DHCP

Na **falsificação de DHCP** (*DHCP spoofing*), o atacante conecta um **servidor DHCP não autorizado** na mesma sub-rede, que **fornece parâmetros falsos** aos clientes:

- **gateway errado**: o IP do atacante como gateway, o que cria um **MitM** difícil de detectar;
- **servidor DNS errado**: leva o usuário a **sites maliciosos**;
- **endereço IP errado**: um IP ou gateway inválido, o que causa uma **negação de serviço** no cliente.

O ataque funciona porque **o cliente aceita a primeira oferta que recebe**:

1. o cliente envia o DHCPDISCOVER, recebido pelos dois servidores;
2. os dois respondem com ofertas;
3. a oferta do servidor falso chega primeiro, e o cliente envia o DHCPREQUEST aceitando-a;
4. só o servidor falso confirma; o legítimo para de responder, porque a solicitação já foi aceita.

![O cliente aceita a primeira oferta que chega; se for a do servidor falso, passa a usar o atacante como gateway](img/endpoint/end_dhcp.png){width=6in}

### 9.6 Mitigação de DoS e Tecnologias Antispoofing

Um dos primeiros sinais de DoS são as **reclamações de usuários** sobre recursos indisponíveis ou rede lenta. Um programa de **monitoramento do uso da rede** deve estar sempre ativo, e a **análise de comportamento** detecta padrões incomuns, que também aparecem nos gráficos de utilização.

O DoS pode fazer parte de uma ofensiva maior e afetar também os equipamentos do caminho: por exemplo, exceder a capacidade de pacotes por segundo do roteador entre a internet e a LAN. Em escala grande, pode comprometer a conectividade de **regiões inteiras**.

Como muitos ataques DoS usam **endereços falsificados**, os roteadores e switches Cisco têm tecnologias **antispoofing**:

- **segurança de porta** (*port security*), que limita quais e quantos endereços MAC podem usar cada porta do switch;
- **DHCP snooping**, que aceita respostas DHCP só de portas confiáveis;
- **IP Source Guard**, que bloqueia pacotes cujo IP de origem não corresponde ao que o DHCP entregou naquela porta;
- **DAI** (*Dynamic ARP Inspection* — inspeção dinâmica de ARP), que descarta respostas ARP falsas;
- **ACLs**.

| Ataque | Principais defesas |
| --- | --- |
| Malware | Antivírus atualizado e filtragem no perímetro |
| Worms | Contenção, inoculação, quarentena e tratamento |
| Reconhecimento | Criptografia, anti-sniffer, switches, firewall e IPS |
| Acesso | Senhas fortes, bloqueio de conta, confiança mínima, criptografia e MFA |
| DoS | Monitoramento e tecnologias antispoofing |

## 10. Ataques ao DNS

O **DNS** (*Domain Name System*) **associa nomes**, como www.cisco.com, **aos endereços IPv4 ou IPv6** de que os computadores precisam. Se um servidor DNS não sabe a resposta, pergunta a outro. As respostas usam **registros de recursos** (**RR**, *Resource Records*), que indicam o tipo de informação.

**Importante:** a proteção do DNS costuma ser esquecida, mas ele é **essencial para a rede** e precisa ser protegido.

### 10.1 Reputação, Sequestro de Domínio e Redirecionamento

Alguns riscos envolvem o próprio domínio da empresa:

- **reputação de domínio**: a empresa precisa monitorar a reputação do seu domínio e do seu IP para se proteger de domínios externos maliciosos;
- **sequestro de domínio**: o atacante **obtém o controle das informações de DNS** do alvo e as altera. A forma mais comum é mudar, por engenharia social (ver item 4.1), o **e-mail de contato do administrador** ou invadir essa conta; o e-mail é fácil de achar no registro **WHOIS**, uma consulta pública que mostra quem registrou cada domínio;
- **redirecionamento de URL**: a **URL** (*Uniform Resource Locator*) identifica um recurso na internet. Redirecionar é comum e legítimo, como um portal que leva o usuário de volta ao login, mas o atacante pode **redirecionar para um site malicioso**.

### 10.2 Ataques aos Resolvedores Abertos

Muitas organizações usam servidores DNS públicos, como o do Google (8.8.8.8). Um **resolvedor aberto** **responde a consultas de qualquer cliente**, mesmo de fora do seu domínio, e por isso é vulnerável a:

| Ataque | Como funciona |
| --- | --- |
| Envenenamento do cache DNS (*DNS spoofing*) | O atacante envia **RRs falsos** ao resolvedor para **levar os usuários a sites maliciosos** ou para que ele use um servidor de nomes malicioso |
| Amplificação e reflexão | O atacante envia consultas com o **IP da vítima como origem**; o resolvedor responde à vítima, o que **aumenta o volume do ataque e esconde a origem** |
| Utilização de recursos | DoS que **consome os recursos do resolvedor**, podendo exigir sua reinicialização |

O **cache DNS** é o banco de dados temporário que guarda as consultas recentes. O envenenamento explora uma falha do software DNS para desviar o tráfego de um domínio para o computador do atacante.

### 10.3 Técnicas Furtivas e Sombreamento de Domínio

Para esconder a identidade, os atacantes usam **técnicas furtivas de DNS**:

- **fluxo rápido** (*fast flux*): esconde os sites de phishing (páginas falsas que imitam empresas legítimas para roubar dados) e de malware atrás de **hosts DNS comprometidos cujos IPs mudam a cada poucos minutos**; muito usado por botnets;
- **fluxo duplo** (*double IP flux*): muda rapidamente os IPs **e também o servidor de nomes autoritativo** (o servidor que dá a resposta oficial sobre o domínio), o que dificulta ainda mais achar a origem;
- **algoritmos de geração de domínio** (**DGA**): o malware **gera nomes de domínio aleatórios** usados como ponto de encontro com os servidores de **comando e controle** (**C&C**), os computadores que dão ordens ao malware.

No **sombreamento de domínio** (*domain shadowing*), o atacante **rouba as credenciais da conta de um domínio** e cria em silêncio **muitos subdomínios** que apontam para servidores maliciosos, sem que o dono perceba. Se um subdomínio for descoberto, ele simplesmente cria outros.

### 10.4 Tunelamento DNS

As **botnets** espalham malware e fazem ataques DDoS e de phishing, e o DNS é muitas vezes ignorado como canal usado por elas. Quando o tráfego DNS é identificado como parte de um incidente, **o ataque geralmente já acabou**.

No **tunelamento DNS**, o atacante **coloca tráfego que não é DNS dentro do tráfego DNS**, o que costuma **contornar as soluções de segurança**. Para isso, usa registros como TXT (texto livre), MX (servidor de e-mail), SRV, NULL, A (endereço IPv4) ou CNAME (apelido de outro nome). Com registros TXT, que podem levar comandos aos bots, o processo é:

1. os dados são divididos em **vários blocos codificados**;
2. cada bloco vai em um **rótulo de subdomínio** de uma consulta DNS;
3. sem resposta no DNS local, a consulta segue para os servidores recursivos do provedor (os que procuram a resposta em nome do cliente);
4. o servidor recursivo a encaminha ao **servidor de nomes autoritativo do atacante** (o servidor "oficial" do domínio, que o atacante controla);
5. o processo se repete até todos os blocos serem enviados;
6. o servidor do atacante responde a cada consulta com **comandos codificados**;
7. o malware no host infectado junta os blocos e executa os comandos.

![No tunelamento DNS, os dados saem escondidos em consultas e os comandos voltam nas respostas](img/endpoint/end_dnstunnel.png){width=6in}

Para interromper o túnel:

- usar um **filtro que inspecione o tráfego DNS**;
- dar atenção às **consultas mais longas que a média** e aos nomes de domínio suspeitos;
- usar soluções de segurança de DNS, como o **Cisco Umbrella** (antigo OpenDNS), que bloqueiam domínios suspeitos;
- considerar **altamente suspeitos os domínios de DNS dinâmico**;
- bloquear as comunicações de saída dos hosts infectados.

| Ataque | Objetivo |
| --- | --- |
| Envenenamento de cache | Levar usuários a sites falsos |
| Amplificação e reflexão | Aumentar o DoS e esconder a origem |
| Fluxo rápido e fluxo duplo | Esconder servidores maliciosos |
| DGA | Encontrar os servidores de comando e controle |
| Sombreamento de domínio | Criar subdomínios maliciosos em domínio legítimo |
| Tunelamento | Esconder comandos e dados roubados no DNS |

## 11. Ataques a Aplicações Web

Os ataques por meio de **aplicativos web** são cada vez mais comuns. Neles, o criminoso aproveita **falhas na programação do aplicativo** para chegar ao banco de dados ou ao servidor, ou usa páginas comprometidas para infectar quem as visita. Bloquear a navegação não é uma opção, porque as empresas precisam da web.

### 11.1 Como Funciona um Ataque Web

O analista precisa conhecer as etapas de um ataque web típico:

1. a vítima visita, sem saber, uma página **comprometida** por malware;
2. a página a **redireciona**, muitas vezes por vários servidores comprometidos, para um site com código malicioso;
3. o computador é infectado só pela visita, o chamado **download automático** (*drive-by download*): um **kit de exploração**, em geral um script em PHP (linguagem usada em sites) com um painel de gerenciamento para o atacante, verifica o sistema operacional, o Java e o Flash (programas que rodavam conteúdo dentro do navegador) da vítima em busca de uma falha;
4. ao achar um programa vulnerável, o kit baixa do seu servidor o código que explora a falha;
5. o computador comprometido se conecta ao servidor de malware e baixa uma **carga útil**, que pode ser o malware ou um serviço que baixa outros malwares;
6. o malware final é executado.

Seja qual for o ataque, o objetivo é **levar o navegador da vítima à página do atacante**. Redes grandes usam IDS para verificar os arquivos baixados, gerar alertas e registrar o evento.

### 11.2 Códigos de Status HTTP

Os **logs de conexão dos servidores** revelam o tipo de varredura ou ataque pelos códigos de status:

| Código | Classe | Significado |
| --- | --- | --- |
| 1xx | Informativo | Resposta provisória |
| 2xx | Sucesso | Pedido recebido, entendido e aceito |
| 3xx | Redirecionamento | O navegador precisa agir de novo, por exemplo ir a outra URL; deve detectar laços infinitos |
| 4xx | Erro do cliente | O cliente parece ter errado |
| 5xx | Erro do servidor | O servidor errou ou não pode atender |

### 11.3 Cross-Site Scripting (XSS)

O **XSS** (*Cross-Site Scripting* — script entre sites) é uma vulnerabilidade comum em aplicativos web:

1. o criminoso **injeta um script malicioso** em uma página web;
2. a vítima acessa a página, e o script passa para o navegador dela;
3. o script acessa **cookies** (pequenos arquivos que o site guarda no navegador, por exemplo para manter o login), **tokens de sessão** (o código que prova que o usuário já está logado) ou outras informações e as envia ao criminoso;
4. com elas, o criminoso **se passa pelo usuário**.

### 11.4 Tipos de XSS e Prevenção

O XSS ataca o **lado do cliente**: o script malicioso roda no navegador da vítima. Os scripts, em JavaScript, Visual Basic e outras linguagens, coletam informações, espalham malware ou preparam outros ataques. Como na injeção de SQL, a causa é a **falta de validação** do conteúdo publicado em um site confiável. Há dois tipos:

- **armazenado** (persistente): fica **gravado no servidor** e atinge **todos os visitantes** da página;
- **refletido** (não persistente): fica **em um link**, e só é infectado quem clica nele.

Para prevenir:

- conscientizar os desenvolvedores sobre o XSS;
- usar um **IPS** (*Intrusion Prevention System* — sistema de prevenção de intrusão) para detectar e bloquear scripts maliciosos;
- usar proxy web e Cisco Umbrella;
- ensinar os usuários a identificar phishing e avisar a equipe de segurança da informação.

### 11.5 Ataques de Injeção

A maioria dos sites guarda seus dados em um banco de dados, como os de **SQL** (*Structured Query Language* — a linguagem de consulta dos bancos relacionais) ou de **XML** (*Extensible Markup Language*). Nos ataques de injeção, o criminoso digita, em um campo de formulário, comandos em vez de dados comuns; se o sistema não filtrar a entrada, executa esses comandos. Eles exploram as fraquezas desses bancos e de outros componentes:

| Ataque | Como funciona |
| --- | --- |
| Injeção de SQL | O criminoso **digita uma instrução SQL maliciosa em um campo de entrada**; funciona quando o aplicativo **não filtra os caracteres** digitados. Permite ler, alterar ou destruir dados, falsificar identidades e até virar administrador do servidor |
| Injeção de XML | Interfere no processamento dos dados XML ou na consulta, corrompendo o banco e dando acesso às informações e ao site |
| Injeção de DLL | Engana um aplicativo para **chamar uma DLL maliciosa**, executada como parte do processo. A **DLL** (*Dynamic Link Library*) é uma biblioteca de código e dados que os programas do Windows usam para ganhar funções |
| Injeção de LDAP | Injeta consultas em servidores **LDAP** (*Lightweight Directory Access Protocol*, protocolo aberto que autentica o acesso a serviços de diretório) para extrair informações do diretório da empresa |

### 11.6 Bancos de Dados Expostos e Injeção de Código

Os aplicativos web costumam se ligar a um **banco de dados relacional**, que guarda dados confidenciais e por isso é alvo frequente:

- **injeção de código**: o atacante digita comandos em um campo de entrada inseguro, como código PHP, e eles **são executados no servidor com as permissões do aplicativo web**; ocorre por **validação insuficiente da entrada**;
- **injeção de SQL**: um dos ataques mais comuns; a consulta maliciosa entra pelos dados do cliente e permite **ler e alterar dados, executar operações de administração** e às vezes dar comandos ao sistema operacional.

Sem **validação rigorosa da entrada**, o aplicativo fica vulnerável. O analista precisa reconhecer consultas SQL suspeitas, descobrir **qual ID de usuário** o atacante usou e o que mais ele pode ter acessado.

### 11.7 Estouro de Buffer

Os **buffers** são áreas de memória reservadas a um aplicativo. O **estouro de buffer** ocorre quando os dados são **gravados além dos limites do buffer**, invadindo a memória de outros processos. O resultado pode ser travamento do sistema, comprometimento de dados ou **elevação de privilégios**.

Essas falhas podem dar **controle total do dispositivo**: o atacante altera as instruções do programa enquanto ele é carregado na memória e instala malware. Segundo a Universidade Carnegie Mellon, **quase metade das explorações** de programas vem de alguma forma de estouro de buffer.

### 11.8 Execução Remota de Código e Elevação de Privilégios

A **execução remota de código** permite ao criminoso **executar qualquer comando** no dispositivo, com os privilégios do usuário que roda o aplicativo vulnerável. A **elevação de privilégios** explora um bug, uma falha de projeto ou uma configuração errada para **acessar recursos normalmente restritos**.

O **Metasploit** é um projeto que reúne informações sobre vulnerabilidades e ajuda nos testes de penetração. Seu **Metasploit Framework** desenvolve e executa explorações em alvos remotos. O **Meterpreter**, uma carga útil do Metasploit, assume o controle do alvo carregando extensões **direto na memória, sem tocar no disco**, o que **escapa dos antivírus**. Ele tem até um módulo para controlar a webcam do alvo.

### 11.9 Outros Ataques a Aplicativos

Cada informação obtida sobre um sistema pode virar arma. Outros ataques são:

| Ataque | Como funciona |
| --- | --- |
| CSRF (*Cross-Site Request Forgery* — falsificação de solicitação entre sites) | Comandos não autorizados são enviados **do navegador do usuário para um aplicativo web confiável** em que ele já está logado, por imagens, formulários ocultos ou JavaScript (a linguagem de programação das páginas web), sem que ele perceba; exemplo: um link que faz o banco aberto em outra aba executar uma transferência |
| Condição de corrida | Também chamado de **TOC/TOU** (tempo de verificação/tempo de uso): o sistema, feito para executar tarefas em sequência, é **forçado a fazer duas ou mais operações ao mesmo tempo**; por exemplo, dois *threads* (as menores sequências de instruções de um programa) alteram os mesmos dados juntos |
| Tratamento inadequado de entrada | Dados digitados **sem validação** alteram o fluxo do programa e causam estouro de buffer ou injeção de SQL |
| Tratamento de erros | **Mensagens de erro revelam informações**, como nomes de hosts, diretórios, arquivos, bancos, tabelas e campos, usadas em ataques de injeção |
| Ataque a API | Abuso de um ponto de acesso (*endpoint*) de uma **API** (*Application Programming Interface*), a interface que leva o pedido do usuário ao sistema e devolve a resposta |
| Repetição | Uma transmissão válida é interceptada, alterada e repetida ou atrasada |
| Travessia de diretório | O atacante **lê arquivos do servidor fora da pasta do site**, como arquivos de configuração, e pode até assumir o servidor |
| Exaustão de recursos | Trava ou paralisa um programa **sobrecarregando o hardware do servidor**, e não a largura de banda como o DoS |

### 11.10 iFrames Maliciosos

Um **iFrame** (*inline frame*) é um elemento do HTML (a linguagem das páginas web) que **carrega dentro da página outra página de outra origem**; é muito usado para inserir anúncios. O atacante invade um servidor web e acrescenta um iFrame que aponta para o seu servidor. Às vezes o iFrame tem **poucos pixels**, quase invisível, e entrega spam, kits de exploração e outros malwares.

Para prevenir:

- usar um proxy web;
- orientar os desenvolvedores a **não usar iFrames**, o que isola o conteúdo de terceiros e facilita achar páginas alteradas;
- usar um serviço como o Cisco Umbrella para bloquear sites conhecidos como maliciosos;
- explicar aos usuários o que é um iFrame.

### 11.11 Amortecimento HTTP 302

O **amortecimento HTTP 302** (*302 cushioning*) usa uma função legítima: o código **302 Found**, que **redireciona o navegador para outra URL**, informada no campo Location. É usado, por exemplo, quando um conteúdo muda de endereço. O atacante encadeia **vários redirecionamentos** até a página com a exploração. Como redirecionamentos legítimos são frequentes, o ataque é **difícil de detectar**.

As defesas são o proxy web, o Cisco Umbrella e a explicação aos usuários sobre as cadeias de redirecionamento.

### 11.12 Sequência com Sombreamento de Domínio

O sombreamento de domínio, que cria subdomínios maliciosos com credenciais roubadas, costuma ser combinado com os ataques anteriores:

1. um site é comprometido;
2. o amortecimento HTTP 302 leva o navegador a sites maliciosos;
3. o sombreamento de domínio leva o navegador a um servidor comprometido;
4. a página do kit de exploração é acessada;
5. o malware é baixado.

Para prevenir:

- proteger as contas dos donos de domínio com **senhas fortes e autenticação de dois fatores**;
- usar proxy web e Cisco Umbrella;
- fazer os donos **validarem suas contas** e procurarem subdomínios não autorizados.

### 11.13 Defesa Contra Ataques a Aplicativos e à Web

As principais medidas são:

- **escrever código sólido**, a primeira linha de defesa;
- **tratar toda entrada externa como hostil** e validá-la;
- manter sistemas e aplicativos **atualizados**, sem ignorar os avisos de atualização, já que nem todo programa se atualiza sozinho.

Na navegação, as contramedidas são:

- usar um **proxy web**, como o Cisco Cloud Web Security ou o Cisco Web Security Appliance, para **bloquear sites maliciosos**;
- seguir as boas práticas do **OWASP** (*Open Web Application Security Project*) ao desenvolver aplicativos; sua lista **OWASP Top 10** reúne os riscos de segurança web mais explorados;
- **educar os usuários**.

## 12. Ataques ao E-mail

O e-mail é usado por bilhões de pessoas e é a **espinha dorsal da comunicação corporativa**, por isso virou uma das maiores portas de entrada de ataques. Este módulo reúne as ameaças que chegam pela caixa de entrada e as formas de se defender delas.

### 12.1 Spam

O **spam** (lixo eletrônico) é o **e-mail não solicitado**, em geral publicidade. Muito spam é enviado por computadores infectados e traz links maliciosos, malware ou golpes para obter dados como números de documentos e de conta bancária. Mesmo filtrado, ele consome largura de banda.

Os sinais de spam são:

- e-mail sem assunto;
- pedido para atualizar os dados da conta;
- erros de ortografia ou pontuação estranha;
- links longos ou incompreensíveis;
- aparência de empresa legítima com pequenas diferenças ou assunto irrelevante;
- pedido para abrir um anexo, muitas vezes com urgência.

Diante desses sinais, não se deve abrir o e-mail nem o anexo, e sim **avisar a equipe de segurança**.

### 12.2 Phishing e Suas Variações

O **phishing** é uma **fraude em que o criminoso se disfarça de pessoa ou empresa legítima** para levar a vítima a instalar malware ou revelar dados, como credenciais e informações financeiras. Pode chegar por e-mail, mensagem ou outro meio. Exemplo: um e-mail de uma "loja conhecida" anuncia um prêmio e leva a um site falso. As variações são:

| Ataque | Como funciona |
| --- | --- |
| Spear phishing | **Altamente direcionado**: e-mail personalizado para uma pessoa, com base em seus interesses e atividades; exemplo: anúncio falso do carro que a vítima procura em um fórum |
| Whaling | Phishing contra **vítimas de alto escalão**, como executivos |
| Vishing | **Phishing por voz**: chamadas falsas por **VoIP** (*Voice over IP*) ou mensagens gravadas para obter dados como os do cartão |
| SMiShing | **Phishing por SMS**: mensagens de texto falsas que levam a sites maliciosos ou a números fraudulentos |
| Pharming | **Leva o usuário a uma cópia falsa de um site oficial**, onde ele digita suas credenciais |

### 12.3 Outras Ameaças ao E-mail

São mais de **100 bilhões de mensagens corporativas por dia**. Antes, era texto lido em servidores protegidos pelo firewall; hoje, mensagens **HTML** são lidas em muitos dispositivos **fora do firewall**, o que abre mais caminhos para ataques. Além do spam e do phishing, as principais ameaças são:

| Ameaça | Como funciona |
| --- | --- |
| Ataques por anexo | Conteúdo malicioso em arquivos de aparência profissional, como um e-mail "do departamento de TI", muitas vezes voltado a um setor específico |
| Falsificação de e-mail | Remetente falso, como um banco com logotipo idêntico, pedindo dinheiro, dados ou "confirmação" de credenciais |
| Retransmissor aberto (*open relay*) | Servidor **SMTP** (*Simple Mail Transfer Protocol*, o protocolo de envio de e-mail) mal configurado que **deixa qualquer um na internet enviar e-mails**; usado para mandar grandes volumes de spam e malware |
| Homóglifos | Caracteres quase idênticos, como O (letra) e 0 (zero) ou l (L minúsculo) e 1 (um), em links de phishing; no DNS, levam a um endereço totalmente diferente |

**Importante:** os servidores de e-mail corporativos **nunca devem ser configurados como retransmissores abertos**.

As defesas são:

- manter o software SMTP atualizado;
- usar um equipamento de segurança de e-mail, como o **Cisco Email Security Appliance**, que bloqueia phishing, spam e malware;
- **educar os usuários**, que são **a última linha de defesa** quando um ataque passa pelas proteções: reconhecer spam, phishing, links suspeitos e homóglifos e nunca abrir anexos suspeitos.

### 12.4 Defesa Contra Ataques ao E-mail

As principais medidas são:

- contar com a filtragem de spam dos provedores (**ISPs**, *Internet Service Providers*) e com antivírus e programas de e-mail que removem spam perigoso;
- **educar os funcionários** sobre e-mails não solicitados e anexos;
- **nunca supor que um anexo é seguro**, mesmo de um contato confiável; sempre verificá-lo antes;
- participar do **APWG** (*Anti-Phishing Working Group*), associação internacional contra fraudes de phishing e falsificação de e-mail;
- manter os programas atualizados com as correções de segurança.

## 13. Comunicação sem Fio

As redes sem fio permitem conectar-se de qualquer lugar, mas exigem dispositivos próprios e estão sujeitas a ataques específicos. Para protegê-las, é preciso primeiro entender como funcionam.

### 13.1 LAN sem Fio e LAN com Fio

Uma **WLAN** (*Wireless LAN* — rede local sem fio) usa **radiofrequência** (**RF**, as ondas de rádio) em vez de cabos na camada física e na subcamada MAC da camada de enlace (a camada 2, que entrega os quadros dentro da rede local). As duas redes vêm da família de padrões **IEEE 802** (o IEEE, *Institute of Electrical and Electronics Engineers*, é a entidade que publica esses padrões): o **802.3** define a Ethernet com fio, e o **802.11**, a rede sem fio. As WLANs diferem das LANs com fio porque:

- conectam os clientes por um **ponto de acesso** (**AP**, *Access Point*) ou roteador sem fio, e não por um switch;
- conectam dispositivos móveis a bateria, e a placa sem fio reduz a duração da bateria;
- usam **prevenção de colisões** (**CSMA/CA**, explicado no item 13.3) em vez de detecção de colisões (**CSMA/CD**, usado na antiga Ethernet com hubs); a colisão acontece quando dois aparelhos transmitem ao mesmo tempo e os sinais se misturam;
- usam um quadro diferente, com mais informações no cabeçalho;
- trazem **mais problemas de privacidade**, porque o sinal sai das instalações.

| Característica | WLAN 802.11 | LAN Ethernet 802.3 |
| --- | --- | --- |
| Camada física | Radiofrequência | Cabos |
| Acesso ao meio | Prevenção de colisões | Detecção de colisões |
| Disponibilidade | Qualquer um com placa sem fio ao alcance do AP | Exige conexão física por cabo |
| Interferência | Sim | Mínima |
| Regulamentação | Varia por país | Definida pelo padrão IEEE |

### 13.2 Quadro 802.11

Todo quadro da camada 2 tem **cabeçalho, carga útil e FCS** (*Frame Check Sequence*, um código no final que permite detectar se o quadro chegou com erro). O quadro 802.11 é parecido com o Ethernet, mas tem mais campos:

| Campo | Função |
| --- | --- |
| Controle do quadro | Tipo do quadro e subcampos de versão, endereço, gerenciamento de energia e segurança |
| Duração | Tempo restante para receber a próxima transmissão |
| Endereço 1 | MAC do dispositivo ou AP que recebe |
| Endereço 2 | MAC do dispositivo ou AP que transmite |
| Endereço 3 | Às vezes, o MAC do destino, como o gateway ao qual o AP está ligado |
| Controle de sequência | Sequência e fragmentação dos quadros |
| Endereço 4 | Em geral ausente; usado só no modo ad hoc (aparelhos conectados diretamente entre si, sem AP) e em pontes entre APs |
| Carga útil | Dados transmitidos |
| FCS | Controle de erros da camada 2 |

### 13.3 CSMA/CA

A WLAN é **half-duplex** (envia ou recebe, nunca os dois ao mesmo tempo) **e de meio compartilhado**: só um cliente transmite por vez, e todos usam o mesmo canal. Como o cliente não consegue ouvir enquanto transmite, **não detecta colisões**; por isso usa o **CSMA/CA** (*Carrier Sense Multiple Access with Collision Avoidance*):

1. **escuta o canal** (a portadora) para ver se está livre;
2. envia ao AP um **RTS** (*Request to Send*), pedindo acesso;
3. recebe do AP um **CTS** (*Clear to Send*), que libera o envio; sem CTS, espera um tempo aleatório e recomeça;
4. transmite os dados;
5. espera a **confirmação**; se não chegar, supõe uma colisão e recomeça.

### 13.4 Associação ao Ponto de Acesso

Para se comunicar, o cliente precisa se associar a um AP em **três etapas**:

Descobrir o AP → Autenticar → Associar

O cliente e o AP precisam concordar nos parâmetros:

- **SSID** (*Service Set Identifier*): o **nome da rede** que aparece na lista; em empresas, cada SSID corresponde a uma **VLAN** (rede local virtual que separa o tráfego), e vários APs podem compartilhar o mesmo SSID;
- **senha**: exigida para autenticar no AP;
- **modo de rede**: os padrões 802.11a/b/g/n/ac/ad (as gerações do Wi-Fi, de velocidades e frequências diferentes; o 802.11n é o Wi-Fi 4 e o 802.11ac, o Wi-Fi 5); os APs podem operar em **modo misto**, aceitando vários ao mesmo tempo;
- **modo de segurança**: WEP, WPA ou WPA2; deve-se **sempre habilitar o nível mais alto** disponível;
- **canal**: a faixa de frequência; o AP pode escolhê-lo sozinho ou ele pode ser configurado à mão em caso de interferência.

### 13.5 Descoberta Passiva e Ativa

O cliente descobre os APs por uma varredura:

- **passiva**: o AP **anuncia a rede** enviando periodicamente **quadros beacon** com o SSID, os padrões suportados e as configurações de segurança;
- **ativa**: o **cliente envia uma solicitação de sondagem** (*probe request*) com o SSID e os padrões em vários canais, e os APs com esse SSID respondem (*probe response*). É necessária quando o AP **não envia beacons**.

Uma sondagem **sem SSID** descobre as redes próximas: os APs que enviam beacons respondem, e os que têm a transmissão do SSID desativada não.

### 13.6 AP, LWAP e WLC

Uma WLAN precisa de APs e de clientes com **placa de rede sem fio** (**NIC**, *Network Interface Card*). Os **roteadores sem fio** domésticos e de pequenas empresas juntam roteador, switch e AP em um só aparelho; em redes pequenas, ele pode ser o único AP.

Em redes maiores, o **WLC** (*Wireless LAN Controller* — controlador de LAN sem fio) **centraliza o controle e o gerenciamento** dos APs. Os APs deixam de ser autônomos e viram **LWAPs** (*Lightweight Access Points* — APs leves), que apenas encaminham os dados entre a WLAN e o WLC. A definição de SSIDs e a autenticação ficam no WLC, o que **simplifica a configuração e o monitoramento**.

## 14. Ameaças às Redes sem Fio e aos Dispositivos Móveis

Uma WLAN fica aberta a **qualquer um ao alcance do AP** que tenha as credenciais. Com uma placa sem fio e técnicas de quebra de senha, o atacante **nem precisa entrar no prédio**. Os ataques podem vir de pessoas de fora, de funcionários insatisfeitos e até, sem querer, de funcionários comuns.

### 14.1 Principais Ameaças sem Fio

As redes sem fio são vulneráveis a:

- **interceptação de dados**: os dados precisam ser criptografados para não serem lidos;
- **intrusos**: usuários não autorizados, barrados por uma autenticação eficaz;
- **negação de serviço**: o acesso pode ser comprometido por acidente ou de propósito;
- **APs não autorizados**: instalados por boa ou má intenção, detectados por software de gerenciamento.

### 14.2 Negação de Serviço sem Fio

O DoS sem fio pode resultar de:

- **dispositivos mal configurados**: um administrador muda uma configuração por engano, ou um atacante com privilégios desativa a WLAN de propósito;
- **interferência intencional**: o atacante tenta desativar a rede por completo;
- **interferência acidental**: fornos de micro-ondas, telefones sem fio, babás eletrônicas e outros aparelhos. A **banda de 2,4 GHz é mais sujeita a interferência que a de 5 GHz**.

O sinal sem fio também sofre com a **EMI** (*Electromagnetic Interference*, interferência eletromagnética), a **RFI** (*Radio Frequency Interference*, interferência de radiofrequência), raios e lâmpadas fluorescentes. O atacante pode **bloquear deliberadamente a transmissão** com um *jammer* de RF; para isso, a **frequência, a modulação e a potência** do jammer precisam ser iguais às do dispositivo atacado.

Para reduzir o risco:

- proteger os dispositivos, manter as senhas seguras e fazer backups;
- fazer as mudanças de configuração **fora do horário comercial**;
- monitorar a interferência e resolvê-la logo;
- usar **5 GHz** nas áreas sujeitas a interferência.

### 14.3 Pontos de Acesso não Autorizados

Um **AP não autorizado** (*rogue AP*) é um AP ou roteador sem fio **ligado à rede da empresa sem autorização** e contra a política. Qualquer pessoa com acesso ao prédio pode instalar um roteador barato, às vezes só querendo um sinal melhor, ou usar engenharia social para entrar e instalá-lo. Uma vez ligado, o atacante pode capturar endereços MAC e pacotes, acessar recursos da rede ou fazer um **MitM**, capturando, por exemplo, as credenciais de login.

Um exemplo de captura usa a **desautenticação**: o atacante desconecta o cliente do AP verdadeiro, o que obriga a rede a enviar quadros de autenticação; ele então falsifica o MAC do cliente e envia seus próprios dados de autenticação.

Até um **hotspot pessoal** pode virar AP não autorizado: um usuário com acesso seguro transforma seu computador Windows em ponto de acesso Wi-Fi, e outros dispositivos passam a usar a rede **contornando a segurança**.

Para impedir, as organizações configuram no WLC **políticas contra APs não autorizados** e usam software que **monitora o espectro de rádio**.

### 14.4 Gêmeo do Mal

No ataque do **gêmeo do mal** (*evil twin*), o atacante cria um AP com **o mesmo SSID de um AP legítimo**, e com sinal mais forte, para parecer uma conexão melhor. É comum em locais com Wi-Fi grátis e **autenticação aberta**, como aeroportos, cafés e restaurantes:

1. os clientes veem dois APs com o mesmo SSID;
2. quem está perto do AP falso recebe o sinal mais forte e se associa a ele;
3. o AP falso captura o tráfego e o repassa ao AP legítimo, e faz o mesmo com o tráfego de volta;
4. o atacante rouba senhas e dados pessoais e pode comprometer o dispositivo.

Para impedir um MitM, a rede precisa **autenticar os usuários** para conhecer os dispositivos legítimos e então **monitorar** dispositivos e tráfego anormais.

### 14.5 Ataques ao Bluetooth

O **Bluetooth** é um protocolo **de curto alcance e baixa potência** que transmite dados em uma **PAN** (*Personal Area Network* — rede pessoal) e usa o **emparelhamento** para ligar celulares, notebooks e impressoras. Por causa do alcance curto, **o atacante precisa estar perto** do alvo:

- **bluejacking**: **envia mensagens não autorizadas** ou imagens chocantes a outro dispositivo Bluetooth;
- **bluesnarfing**: **copia informações** do alvo, como e-mails e listas de contatos.

### 14.6 Ameaças aos Dispositivos Móveis

Os dispositivos móveis também sofrem com:

- **grayware**: aplicativo indesejado que **se comporta de forma irritante**, como rastrear a localização ou exibir publicidade. **Não tem malware reconhecível**, e seus autores se protegem colocando esses recursos nas letras miúdas da licença, que muitos usuários de smartphone não leem;
- **SMiShing**: o phishing por SMS, que leva a sites maliciosos ou a números fraudulentos.

### 14.7 Fraquezas dos Protocolos Wi-Fi

O **WEP** (*Wired Equivalent Privacy*) foi criado para dar à WLAN uma proteção comparável à da rede com fio, criptografando os dados. Mas tinha falhas graves:

- **não tinha gerenciamento de chaves**: a mesma chave era compartilhada por cada vez mais pessoas, o que dava aos criminosos muito tráfego para analisar;
- seu **vetor de inicialização** (**IV**), parte essencial da chave, era **pequeno, legível e estático**.

O **WPA** (*Wi-Fi Protected Access*) e o **WPA2** foram criados para substituí-lo. Com o WPA2, **o atacante não consegue recuperar a chave apenas observando o tráfego**, mas ainda pode usar um *sniffer* para analisar os pacotes entre o AP e um usuário legítimo.

## 15. Proteção das Redes sem Fio

O sinal sem fio atravessa tetos, pisos e paredes e sai do prédio. Sem segurança rigorosa, instalar uma WLAN é como **espalhar portas de rede até fora do escritório**.

### 15.1 Ocultação do SSID e Filtragem de MAC

Dois recursos antigos ainda existem na maioria dos roteadores e APs:

- **ocultação do SSID** (*SSID cloaking*): desativa o beacon com o SSID, e os clientes precisam digitar o nome da rede manualmente;
- **filtragem de endereços MAC**: o administrador **permite ou nega o acesso pelo MAC** de cada cliente.

**Importante:** esses recursos afastam a maioria dos usuários, mas **não impedem um intruso habilidoso**: o SSID é fácil de descobrir mesmo oculto, e o MAC pode ser falsificado. A melhor proteção é usar **autenticação e criptografia**.

### 15.2 Métodos de Autenticação

O padrão 802.11 original trouxe dois tipos de autenticação:

- **sistema aberto**: **qualquer cliente se conecta, sem senha**. Só deve ser usado quando a segurança não importa, como no Wi-Fi grátis de cafés e hotéis, e **o cliente é o responsável pela segurança**, por exemplo usando uma VPN;
- **chave compartilhada**: usa WEP, WPA, WPA2 ou WPA3 para autenticar e criptografar, com uma **senha combinada antes** entre o cliente e o AP.

As quatro técnicas de chave compartilhada são:

| Método | Criptografia | Situação |
| --- | --- | --- |
| WEP | **RC4** (uma cifra antiga, hoje considerada quebrada) com **chave estática**, que nunca muda | Fácil de quebrar; **nunca deve ser usado** |
| WPA | WEP reforçado com **TKIP** (*Temporal Key Integrity Protocol*), que **muda a chave a cada pacote** | Substituto temporário do WEP |
| WPA2 | **AES** (*Advanced Encryption Standard*), o protocolo mais forte | **Padrão atual** do setor |
| WPA3 | Métodos mais recentes; **exige quadros de gerenciamento protegidos** (**PMF**, *Protected Management Frames*, que impedem, por exemplo, a desautenticação falsa do item 14.3) | Próxima geração; recomendado quando disponível |

**Observação:** o curso recomenda usar WPA2 até o WPA3 se tornar comum, mas lembra que o WPA2 **já não é considerado totalmente seguro**.

### 15.3 Pessoal e Corporativo

Os roteadores domésticos oferecem dois modos de WPA2:

- **pessoal**: para casas e pequenos escritórios; os clientes se autenticam com uma **chave pré-compartilhada** (**PSK**, *Pre-Shared Key*), sem servidor especial;
- **corporativo** (*Enterprise*): para empresas; exige um **servidor RADIUS** (*Remote Authentication Dial-In User Service*), um servidor central que confere o usuário e a senha de cada pessoa. É mais complexo, mas mais seguro: o dispositivo é autenticado pelo servidor, e os usuários, pelo padrão **802.1X**, que usa o **EAP** (*Extensible Authentication Protocol*).

### 15.4 Criptografia no WPA e no WPA2

A criptografia impede que dados capturados sejam decifrados em tempo razoável. Os protocolos usados são:

- **TKIP** (*Temporal Key Integrity Protocol*): usado pelo **WPA**; atende equipamentos antigos e corrige as falhas do WEP. Usa o WEP, mas criptografa a carga útil da camada 2 com TKIP e faz um **MIC** (*Message Integrity Check*) para garantir que a mensagem não foi alterada;
- **AES**: usado pelo **WPA2**; é o **preferido, por ser muito mais forte**. Usa o **CCMP** (*Counter Cipher Mode with Block Chaining Message Authentication Code Protocol*), que permite ao destino perceber se os bits foram alterados.

### 15.5 Autenticação na Empresa

O modo corporativo exige um servidor RADIUS de **AAA** (*Authentication, Authorization and Accounting* — autenticação, autorização e contabilidade), que verifica quem é o usuário, o que ele pode fazer e registra o que ele fez. No AP, configuram-se:

- o **endereço IP do servidor RADIUS**;
- as **portas UDP**: **1812 para autenticação e 1813 para contabilidade**, ou as antigas 1645 e 1646;
- a **chave compartilhada**, que autentica o AP no servidor.

**Importante:** a chave compartilhada **não é configurada no cliente**; ela só serve para o AP se autenticar no RADIUS. Os usuários são autenticados pelo **802.1X**, de forma centralizada.

O login 802.1X usa o **EAP** para a comunicação entre o AP e o RADIUS. O EAP é uma estrutura de autenticação que também negocia uma **chave privada para a sessão**, usada na criptografia TKIP ou AES.

### 15.6 WPA3

O WPA3 é o método recomendado. Tem quatro recursos:

| Recurso | O que muda |
| --- | --- |
| WPA3-Personal | No WPA2-Personal, o atacante pode escutar o handshake e tentar adivinhar a PSK por **força bruta**. O WPA3 usa a **SAE** (*Simultaneous Authentication of Equals*), do IEEE 802.11-2016, e a **PSK nunca é exposta** |
| WPA3-Enterprise | Continua com 802.1X/EAP, mas exige um **conjunto criptográfico de 192 bits** e não mistura protocolos antigos; segue o **CNSA** (*Commercial National Security Algorithm*), usado em redes de alta segurança |
| Redes abertas | No WPA2, o tráfego vai em texto claro. No WPA3, as redes abertas continuam sem autenticação, mas **criptografam todo o tráfego** com o **OWE** (*Opportunistic Wireless Encryption*) |
| Integração de IoT | O **WPS** (*Wi-Fi Protected Setup*) do WPA2 é vulnerável e não é recomendado. O **DPP** (*Device Provisioning Protocol*) atende os dispositivos de **IoT** (*Internet of Things* — internet das coisas) **sem tela** (*headless*): cada um tem uma chave pública no firmware, em geral impressa como **QR Code**, que o administrador lê para conectá-lo |

### 15.7 Defesa de Redes sem Fio e Móveis

As principais medidas são:

- usar os recursos básicos de autenticação e criptografia, **trocando as configurações padrão**;
- posicionar os APs **fora do firewall ou em uma DMZ** (*Demilitarized Zone* — zona desmilitarizada), rede de perímetro que protege a LAN de dispositivos não confiáveis;
- usar ferramentas de WLAN, como o **NetStumbler**, para detectar APs e estações não autorizados;
- ter uma **política de acesso para convidados**;
- fazer os funcionários usarem uma **VPN de acesso remoto** para acessar a WLAN.

## 16. Dispositivos de Segurança de Rede

A **infraestrutura de segurança de rede** define como os dispositivos são ligados para obter **comunicação segura de ponta a ponta**. Há muitas formas de construí-la, mas o setor recomenda alguns projetos padrão, apoiados em dispositivos e serviços de segurança.

### 16.1 Firewalls

Um **firewall** é um **sistema ou grupo de sistemas que aplica uma política de controle de acesso entre redes**. Exemplos de regras de um firewall entre a internet e a rede interna:

- negar o tráfego de entrada com **endereços de origem internos**;
- negar os pedidos de eco ICMP vindos de fora;
- negar consultas externas ao Active Directory (o cadastro central de usuários do Windows) e ao servidor SQL (o banco de dados);
- permitir o tráfego externo para o **servidor web**, o FTP (transferência de arquivos), o SMTP (envio de e-mail) e o IMAP (leitura de e-mail).

Todos os firewalls têm três propriedades:

- **resistem a ataques** de rede;
- são o **único ponto de passagem** entre a rede interna e as externas;
- **aplicam a política** de controle de acesso.

| Benefícios | Limitações |
| --- | --- |
| Impedem a exposição de hosts, recursos e aplicações a usuários não confiáveis | Mal configurado, vira um **ponto único de falha** |
| "Limpam" o fluxo dos protocolos, evitando a exploração de falhas | Os dados de muitos aplicativos não passam com segurança |
| Bloqueiam dados maliciosos de servidores e clientes | Usuários procuram formas de contorná-lo, o que expõe a rede |
| Simplificam a gestão, concentrando o controle de acesso em poucos firewalls | Podem reduzir o desempenho |
|  | Tráfego não autorizado pode passar disfarçado de legítimo, em túneis |

### 16.2 Arquiteturas de Firewall

O projeto do firewall trata das **interfaces** que permitem ou negam tráfego conforme a origem, o destino e o tipo. Os três projetos comuns são:

- **privado e público**: a rede pública (externa) **não é confiável**, e a privada (interna) é. O tráfego que sai da rede privada é permitido e inspecionado, e as respostas voltam; o que **nasce na rede pública com destino à privada é bloqueado**;
- **DMZ** (zona desmilitarizada): o firewall tem uma interface interna, uma externa e uma **DMZ**, onde ficam os servidores acessados de fora;
- **firewall de política baseada em zonas** (**ZPF**, *Zone-Based Policy Firewall*): agrupa em **zonas** as interfaces com funções semelhantes, como duas LANs privadas.

Na arquitetura com DMZ, o tráfego é tratado assim:

| Origem → destino | Tratamento |
| --- | --- |
| Privada → pública ou DMZ | Inspecionado e permitido com pouca ou nenhuma restrição; as respostas voltam |
| DMZ → privada | **Bloqueado** |
| DMZ → pública | Permitido seletivamente, conforme os serviços |
| Pública → DMZ | **Permitido seletivamente e inspecionado**: em geral e-mail, DNS, HTTP e HTTPS; as respostas voltam dinamicamente |
| Pública → privada | **Bloqueado** |

No ZPF, **o tráfego entre interfaces da mesma zona passa livremente**, e **todo o tráfego entre zonas diferentes é bloqueado** até que uma política o permita ou inspecione. A exceção é a **zona própria** (*self zone*), o próprio roteador com todos os seus IPs: por padrão, não há política para o tráfego que chega ao roteador ou sai dele. Ao planejá-la, considera-se o tráfego de gerenciamento e de controle, como **SSH** (acesso remoto seguro), SNMP e protocolos de roteamento.

### 16.3 Tipos de Firewall

Os tipos de firewall diferem nas camadas do modelo OSI que examinam (a camada 3 tem os endereços IP; a 4, as portas TCP e UDP; a 5, o controle das sessões; e a 7, o conteúdo dos aplicativos, como o HTTP):

| Tipo | Camadas | Como funciona |
| --- | --- | --- |
| Filtragem de pacotes (**sem estado**) | 3 e 4 | Parte de um roteador; consulta uma tabela de regras simples com IP de origem e destino, protocolo, portas e pacotes SYN. Exemplo: bloquear a porta 25 (SMTP) de uma estação para impedir que ela espalhe um vírus por e-mail |
| **Com estado** (*stateful*) | 3, 4 e 5 | O **mais versátil e mais usado**; filtra com base nas informações de conexão guardadas em uma **tabela de estado** |
| Gateway de aplicação (**proxy**) | 3, 4, 5 e 7 | Filtragem feita em software; o cliente se conecta ao proxy, que se conecta ao servidor **em nome do cliente**; o servidor só vê o proxy |
| Última geração (**NGFW**, *Next-Generation Firewall*) | Além do com estado | Prevenção de intrusão integrada, **reconhecimento e controle de aplicativos**, atualização com novas fontes de informação e técnicas contra ameaças em evolução |

Outras formas de implementação são:

- **firewall de host**: software de firewall em um PC ou servidor;
- **firewall transparente**: fica no meio do caminho, invisível para a rede, e filtra o tráfego entre duas interfaces ligadas em ponte;
- **firewall híbrido**: combina tipos; por exemplo, o de inspeção de aplicações junta o com estado e o gateway de aplicação.

### 16.4 IDS e IPS

Contra ataques rápidos e em evolução, a rede precisa de **sistemas de detecção e prevenção** nos pontos de entrada e saída:

- **IDS** (*Intrusion Detection System*): **detecta** o ataque e alerta;
- **IPS** (*Intrusion Prevention System*): detecta e **bloqueia**; é mais escalável.

Os dois têm características em comum:

- são implantados como **sensores**: um roteador com Cisco IOS IPS, um equipamento dedicado ou um módulo em um ASA, switch ou roteador;
- usam **assinaturas**, conjuntos de regras que reconhecem atividades maliciosas, para detectar violações graves, ataques comuns e coletar informações;
- detectam padrões **atômicos** (um único pacote) ou **compostos** (vários pacotes).

Quando o tráfego malicioso chega a um sensor com IPS, o sensor envia um registro ao **console de gerenciamento** e descarta o tráfego, mandando-o para o "*bit bucket*" (a "lixeira de bits", isto é, ele simplesmente some).

| Solução | Vantagens | Desvantagens |
| --- | --- | --- |
| IDS (fora de linha, *offline*) | **Não afeta a rede**: sem latência nem variação; se o sensor falhar ou sobrecarregar, a rede continua | **Não impede o pacote que disparou o alerta**; pouco útil contra vírus de e-mail e worms; ajuste demorado; mais vulnerável a técnicas de evasão |
| IPS (em linha, *inline*) | **Bloqueia o pacote de gatilho**, a conexão ou a origem; usa a **normalização de fluxo**, que reconstrói o fluxo quando o ataque vem dividido em vários segmentos | Falhas e sobrecarga do sensor **afetam a rede**; causa latência e *jitter* (variação do atraso); precisa ser bem dimensionado para não prejudicar o VoIP |

**Observação:** IDS e IPS **se complementam**. O IDS pode validar o IPS com uma inspeção mais profunda fora de linha, enquanto o IPS se concentra nos padrões mais críticos. A escolha depende dos objetivos da política de segurança.

### 16.5 Equipamentos de Segurança Especializados

A Cisco oferece equipamentos especializados:

- **AMP** (*Advanced Malware Protection*): protege **antes, durante e depois** de um ataque:
  - antes: fortalece as defesas contra ameaças conhecidas e emergentes;
  - durante: impede a entrada de arquivos que violam a política, explorações e arquivos maliciosos;
  - depois: **monitora continuamente** os arquivos, mesmo os considerados "bons"; se um começar a se comportar mal, alerta com um IOC e mostra a origem, os sistemas afetados e as ações da ameaça. Usa a inteligência do **Cisco Talos**, a maior rede de detecção de ameaças do mundo;
- **WSA** (*Web Security Appliance*): gateway web seguro que **bloqueia sites arriscados**, testa sites desconhecidos antes de liberá-los e oferece proteção contra malware, controle de aplicativos e de uso aceitável, relatórios e mobilidade segura. Não protege quem se conecta **fora da rede**, como em um Wi-Fi público;
- **CWS** (*Cloud Web Security*): complementa o WSA e dá aos **funcionários remotos** a mesma segurança dos que estão no local, com filtragem e segurança web e relatórios centralizados;
- **ESA** (*Email Security Appliance*) ou Cisco Cloud Email Security: protege os sistemas de e-mail, atualizado em tempo real pelo Talos:
  - inteligência global contra ameaças, com visão 24 horas do tráfego mundial;
  - **bloqueio de spam** em camadas: filtro externo pela **reputação do remetente** e filtro interno com análise profunda da mensagem;
  - proteção avançada contra malware com AMP;
  - **controle das mensagens de saída**, para cumprir as normas e protegê-las em trânsito.

## 17. Serviços de Segurança de Rede

Além dos dispositivos, a infraestrutura usa **serviços** que controlam, monitoram e protegem a transmissão de dados.

### 17.1 Listas de Controle de Acesso

Uma **ACL** é uma **série de comandos que decide se o dispositivo encaminha ou descarta cada pacote**, com base no cabeçalho. As ACLs:

- **limitam o tráfego** para melhorar o desempenho; por exemplo, bloqueiam vídeo se a política não o permite;
- **controlam o fluxo**, restringindo as atualizações de roteamento a fontes conhecidas;
- dão um **nível básico de segurança**, permitindo que um host acesse uma parte da rede e outro não, como a rede de recursos humanos;
- **filtram pelo tipo de tráfego**, permitindo e-mail e bloqueando Telnet;
- permitem ou negam o acesso a serviços, como FTP ou HTTP.

As ACLs também **classificam o tráfego**, por exemplo para dar prioridade a certos tipos, como um ingresso VIP.

Há dois tipos de ACL IPv4 da Cisco:

| Tipo | O que filtra |
| --- | --- |
| Padrão | **Só o endereço IPv4 de origem** |
| Estendida | Protocolo, IPv4 de origem e de destino, portas TCP ou UDP de origem e de destino e informações opcionais do protocolo |

Os dois tipos podem ser identificados por **número** ou por **nome**; o nome indica o propósito da ACL. O **registro de ACL** gera uma mensagem quando o tráfego atende a um critério. As ACLs também podem **permitir só o tráfego TCP com os bits ACK ou RST**, ou seja, apenas de sessões **já estabelecidas**, o que bloqueia as tentativas de abrir sessões vindas de fora.

### 17.2 SNMP

O **SNMP** (*Simple Network Management Protocol*) permite **gerenciar** servidores, estações, roteadores, switches e dispositivos de segurança: monitorar o desempenho, resolver problemas e planejar o crescimento. É um protocolo da camada de aplicação com dois elementos:

- **gerenciador SNMP**: roda o software de gerenciamento e faz parte de um **NMS** (*Network Management System*);
- **agentes SNMP**: os nós monitorados e gerenciados.

A **MIB** (*Management Information Base*) é o **banco de dados do agente** com dados e estatísticas do dispositivo. O gerenciador:

- **obtém** informações com a ação **get**;
- **altera** configurações com a ação **set**;
- recebe dos agentes avisos espontâneos, os **traps**.

### 17.3 NetFlow

O **NetFlow** é uma tecnologia do Cisco IOS que fornece **estatísticas dos pacotes IP** que passam por roteadores e switches multicamadas. Enquanto o SNMP cobre muitas funções de gerenciamento, o NetFlow se concentra nos fluxos. Ele serve para monitoramento da rede e da segurança, planejamento, identificação de gargalos e contabilidade para cobrança.

O NetFlow conta os bytes e pacotes de cada fluxo, como uma conexão HTTPS entre dois PCs, e envia as estatísticas a um **coletor NetFlow**. O NetFlow original identifica um fluxo por **sete campos**; se um deles mudar, é outro fluxo:

- endereço IP de origem;
- endereço IP de destino;
- porta de origem;
- porta de destino;
- tipo de protocolo da camada 3 (em geral TCP ou UDP, ou ICMP);
- marcação **ToS** (*Type of Service*), que indica as regras de qualidade de serviço (**QoS**, *Quality of Service*, que dá prioridade a certos tipos de tráfego);
- interface lógica de entrada.

### 17.4 Espelhamento de Portas

Um **analisador de pacotes** (*sniffer*) é um software que **captura os pacotes que entram e saem da placa de rede**. Muitas vezes é melhor usá-lo em uma estação separada. Mas o switch **isola o tráfego**, e o analisador ou o IDS (ver item 16.4) não veem tudo o que passa no segmento.

O **espelhamento de portas** (*port mirroring*) faz o switch **copiar o tráfego** que passa por ele e enviar a cópia por uma porta onde está o monitor. O tráfego original segue normalmente.

### 17.5 Syslog e NTP

Os dispositivos de rede notificam o administrador com **mensagens de sistema**, críticas ou não. O meio mais comum de acessá-las é o **syslog**, que **envia as mensagens pela rede a um servidor syslog**. É aceito por roteadores, switches, servidores, firewalls e outros. Ele permite:

- **coletar** registros para monitorar e resolver problemas;
- **escolher** que tipo de informação é capturada;
- **definir o destino** das mensagens.

Todos os aspectos de gestão, proteção e solução de problemas dependem de **data e hora precisas e consistentes**; sem relógios sincronizados, é **impossível saber a ordem dos eventos** em partes diferentes da rede. A configuração manual não é ideal, nem em redes pequenas: um dispositivo reiniciado perde a hora. A solução é o **NTP**, que sincroniza os relógios com um servidor, privado ou público na internet.

O NTP usa uma hierarquia de fontes de tempo, os **estratos**, contados em saltos a partir da fonte oficial:

| Estrato | Quem é |
| --- | --- |
| 0 | Fontes de tempo de alta precisão, com pouco ou nenhum atraso |
| 1 | Ligados diretamente às fontes de estrato 0; são o **padrão de horário** da rede |
| 2 em diante | Sincronizam pela rede com o estrato acima e podem servir ao estrato abaixo |
| 16 | **Dispositivo não sincronizado** |

**Quanto menor o estrato, mais perto da fonte oficial**. O máximo é **15 saltos**. Servidores do mesmo estrato podem atuar como **pares**, para backup ou verificação.

### 17.6 Servidores AAA

Os **servidores AAA** controlam o acesso à rede de forma centralizada:

- **autenticação**: usuários e administradores **provam quem são**, com usuário e senha, perguntas de desafio, tokens e outros métodos;
- **autorização**: depois da autenticação, define **o que o usuário pode acessar e fazer**; exemplo: "o usuário aluno só acessa o host serverXYZ por SSH";
- **contabilidade** (*accounting*): **registra o que o usuário faz**: o que acessou, por quanto tempo e o que mudou; exemplo: "o aluno acessou o serverXYZ por SSH durante 15 minutos".

Os protocolos de comunicação com os servidores AAA são o **TACACS+** (*Terminal Access Controller Access-Control System Plus*) e o **RADIUS**. O **TACACS+ é considerado mais seguro**, porque **criptografa toda a troca**, enquanto o RADIUS **criptografa só a senha**.

| Característica | TACACS+ | RADIUS |
| --- | --- | --- |
| Funcionalidade | Separa autenticação, autorização e contabilidade (modular) | Junta autenticação e autorização; separa a contabilidade |
| Padrão | Principalmente Cisco | Padrão aberto (RFC, os documentos que definem os padrões da internet) |
| Transporte | **TCP** | **UDP** |
| Desafio CHAP (prova de senha sem enviá-la pela rede) | Bidirecional | Unidirecional, do servidor para o cliente |
| Confidencialidade | **Pacote inteiro criptografado** | **Só a senha** |
| Personalização | Autoriza comandos do roteador por usuário ou grupo | Não autoriza comandos |
| Contabilidade | Limitada | Abrangente |

### 17.7 VPN

Uma **VPN** é uma **rede privada criada sobre uma rede pública**, em geral a internet, usando conexões virtuais em vez de uma linha física dedicada. Ela é:

- **virtual**, porque leva informações privadas por uma rede pública;
- **privada**, porque o tráfego é **criptografado** para manter a confidencialidade.

As primeiras VPNs eram túneis IP sem autenticação nem criptografia, como o **GRE** (*Generic Routing Encapsulation*), da Cisco, que encapsula vários protocolos de rede em túneis IP e cria um link virtual ponto a ponto. Hoje, VPN significa uma implementação **segura e criptografada**.

A VPN liga dois pontos, como uma filial e a matriz, em uma conexão lógica na camada 2 ou 3. Exemplos de VPNs de camada 3 são o GRE, o **MPLS** (*Multiprotocol Label Switching*, rede das operadoras que encaminha os pacotes por rótulos) e o **IPsec**. O GRE e o IPsec fazem conexões ponto a ponto; o MPLS liga muitos sites.

O **IPsec** (*IP Security*) é um conjunto de protocolos, apoiado pelo **IETF** (*Internet Engineering Task Force*, a entidade que publica os padrões da internet), que oferece **autenticação, integridade, controle de acesso e confidencialidade** em redes IP. As VPNs IPsec são usadas em duas topologias:

- **site a site**: liga a matriz às filiais;
- **acesso remoto**: dá acesso seguro a quem viaja ou trabalha de casa.

## 18. O Sistema Operacional Windows

O Windows passou por muitas versões desde 1985, do Windows 1.0 ao Windows 10 e ao Windows Server 2019. Para proteger um computador Windows (um **endpoint**, isto é, um dispositivo final da rede), é preciso entender como ele funciona.

### 18.1 Do MS-DOS ao Windows NT

Os primeiros computadores guardavam dados em cartões perfurados, fitas de papel, fitas magnéticas e até fitas cassete. Disquetes e discos rígidos exigem software para ler, gravar e organizar os arquivos: o **DOS** (*Disk Operating System* — sistema operacional de disco), que oferece um **sistema de arquivos**. A Microsoft comprou o DOS e criou o **MS-DOS**, operado por **linha de comando**.

As primeiras versões do Windows, a partir do Windows 1.0 (1985), eram uma **interface gráfica** (**GUI**, *Graphical User Interface*) que rodava sobre o MS-DOS, que ainda controlava o hardware. O Windows moderno não é um sistema de disco: é baseado no **Windows NT** ("Novas Tecnologias"), que **controla diretamente o hardware** e aceita **vários processos e usuários**, ao contrário do MS-DOS, de um processo e um usuário só.

A janela de comando do Windows (aberta com **cmd**) não é mais o MS-DOS, mas aceita comandos parecidos:

| Comando | Função |
| --- | --- |
| `dir` | Lista os arquivos da pasta atual |
| `cd pasta` | Entra na pasta indicada |
| `cd ..` | Sobe para a pasta acima |
| `cd \` | Vai para a raiz (em geral C:) |
| `copy origem destino` | Copia arquivos |
| `del arquivo` | Apaga arquivos |
| `find` | Procura texto em arquivos |
| `mkdir pasta` | Cria uma pasta |
| `ren antigo novo` | Renomeia um arquivo |
| `help` | Lista os comandos; `help comando` mostra a ajuda de um deles |

### 18.2 Versões do Windows

Desde 1993 houve mais de 20 versões baseadas no NT, adotadas por pessoas e empresas pela **segurança de arquivos** do seu sistema de arquivos. Há edições para estações de trabalho, profissionais, servidores e data centers.

A partir do Windows XP surgiu a edição de **64 bits**, uma arquitetura nova. Como os bits são binários, o espaço não dobra: o Windows de **32 bits** endereça pouco menos de **4 GB de RAM**, e o de **64 bits**, em teoria, **16,8 milhões de terabytes**, o que permite bancos de dados enormes, computação científica e edição de vídeo em alta definição. Os sistemas de 64 bits rodam programas de 32 bits, mas **programas de 64 bits não rodam em hardware de 32 bits**.

Cada versão trouxe mais recursos e edições: o Windows 7 teve seis, o 8 até cinco e o 10 oito. A Microsoft afirma que o **Windows 10 é a última versão**, que passa a ser **um serviço**, atualizado continuamente.

| Sistema | Edições |
| --- | --- |
| Windows 7 | Starter, Home Basic, Home Premium, Professional, Enterprise, Ultimate |
| Windows Server 2008 R2 | Foundation, Standard, Enterprise, Datacenter, Web Server, HPC Server, Itanium |
| Windows 8 | 8, 8 Pro, 8 Enterprise, RT |
| Windows Server 2012 | Foundation, Essentials, Standard, Datacenter |
| Windows 10 | Home, Pro, Pro Education, Enterprise, Education, IoT Core, Mobile, Mobile Enterprise |
| Windows Server 2016 | Essentials, Standard, Datacenter, Multipoint Premium Server, Storage Server, Hyper-V Server |

### 18.3 Interface Gráfica

A área principal da GUI é a **área de trabalho**, que cada usuário pode personalizar e onde ficam arquivos, pastas, atalhos e a **lixeira**, que guarda os arquivos apagados até ser esvaziada. Na parte de baixo fica a **barra de tarefas**, com três áreas:

- **menu Iniciar e pesquisa**, à esquerda: programas, configurações e busca;
- **ícones de inicialização rápida**, no centro: abrem programas ou pastas;
- **área de notificação**, à direita: mostra o estado de programas e recursos, como um envelope piscando (novo e-mail) ou um X vermelho na rede.

O clique com o botão direito abre o **menu de contexto**, com as funções mais usadas, como copiar, excluir, compartilhar e imprimir. Pastas e arquivos são manipulados no **Explorador de Arquivos**.

### 18.4 Vulnerabilidades do Sistema Operacional

Os sistemas operacionais e os programas têm **milhões de linhas de código**, e com elas vêm vulnerabilidades. Para aproveitar uma delas, o atacante usa uma técnica ou ferramenta de exploração e faz o computador agir fora do previsto, em geral para **obter controle, alterar permissões ou roubar e manipular dados**. As recomendações de segurança do Windows são:

| Área | Recomendação |
| --- | --- |
| Proteção contra vírus e malware | Manter ativo o **Windows Defender**, a proteção padrão; desativado, o sistema fica mais vulnerável |
| Serviços desconhecidos | Garantir que **cada serviço em segundo plano seja identificável e seguro** |
| Criptografia | Criptografar os dados, principalmente nos dispositivos móveis |
| Política de segurança | Configurar e seguir uma boa política; muitas opções da Diretiva de Segurança do Windows impedem ataques |
| Firewall | Revisar periodicamente as regras do **Firewall do Windows** e remover as que não se aplicam, como portas que ficaram abertas |
| Permissões de arquivos e compartilhamentos | Dar a cada usuário ou grupo **as permissões mínimas necessárias**, e não "Controle Total" ao grupo "Todos" |
| Senhas | Usar senhas fortes em todas as contas, principalmente na de **Administrador** |
| Login como administrador | Entrar como **usuário padrão** e usar a senha de administrador só quando preciso, porque todo programa herda os privilégios da conta |

## 19. Arquitetura e Funcionamento do Windows

O Windows roda em muitos tipos de hardware, comprados prontos ou montados pelo usuário. Sua arquitetura isola o sistema operacional dessas diferenças.

### 19.1 Camadas da Arquitetura

A arquitetura básica do Windows tem estas camadas, de cima para baixo:

Aplicativos → API do Windows e drivers de modo usuário → Kernel, drivers de modo kernel e drivers do sistema de arquivos → HAL → Hardware

- **kernel**: o **núcleo do sistema operacional**, que controla todo o computador: entrada e saída, memória e periféricos;
- **HAL** (*Hardware Abstraction Layer* — camada de abstração de hardware): software que **cuida de toda a comunicação entre o hardware e o kernel**. Os dois não são totalmente independentes: o kernel às vezes fala direto com o hardware, e a HAL precisa do kernel para algumas funções;
- **drivers**: programas que permitem ao sistema operacional se comunicar com um dispositivo.

![Arquitetura do Windows: aplicativos em modo usuário, kernel e HAL em modo kernel, sobre o hardware](img/endpoint/end_wincamadas.png){width=6in}

### 19.2 Modo Usuário e Modo Kernel

A CPU do Windows opera em dois modos:

- **modo kernel**: roda o código do sistema operacional, com **acesso irrestrito ao hardware**, a qualquer instrução da CPU e a qualquer endereço de memória. É reservado às funções mais confiáveis, e **uma falha nele para o computador inteiro**;
- **modo usuário**: roda os aplicativos, **sem acesso direto ao hardware nem à memória**; tudo passa pelo sistema operacional. Graças a esse isolamento, **uma falha afeta só o aplicativo** e pode ser recuperada.

A maioria dos programas roda em modo usuário, e os drivers podem rodar em qualquer um dos dois. Todo o código do modo kernel usa **o mesmo espaço de endereços**, sem isolamento: um driver de kernel que grava no endereço errado pode derrubar todo o sistema. Já cada aplicativo em modo usuário recebe do kernel **um processo e um espaço de endereços privado**, que outros aplicativos não podem alterar.

| Característica | Modo usuário | Modo kernel |
| --- | --- | --- |
| O que roda | Aplicativos | Sistema operacional e alguns drivers |
| Acesso ao hardware | Só pelo sistema operacional | Irrestrito |
| Espaço de endereços | Privado para cada processo | Compartilhado |
| Efeito de uma falha | Só no aplicativo; recuperável | Para todo o computador |

### 19.3 Sistemas de Arquivos

Antes de ser usado, um disco precisa ser **particionado** (dividido em **partições**, unidades lógicas de armazenamento) e **formatado** com um sistema de arquivos. Na instalação, o sistema costuma fazer isso sozinho. Os principais sistemas são:

| Sistema de arquivos | Características |
| --- | --- |
| FAT (FAT16 e FAT32) e exFAT | Simples e aceitos por muitos sistemas; o FAT tem limites de partições e de tamanho (no FAT32, nenhum arquivo passa de 4 GB) e **não é mais usado em HDs e SSDs** (os discos internos); o FAT32 e o exFAT ainda são comuns em pen drives e cartões de memória |
| HFS+ (*Hierarchical File System Plus*) | Usado no **macOS**; o Windows lê suas partições com software especial |
| EXT (*Extended File System*) | Usado no **Linux**; o Windows lê suas partições com software especial |
| NTFS (*New Technology File System*) | **O mais usado ao instalar o Windows**; aceito por todas as versões do Windows e do Linux; o macOS só lê, a menos que instale drivers |

O **NTFS** é o preferido porque:

- aceita **arquivos e partições muito grandes**;
- é **confiável** e tem recursos de recuperação;
- controla o acesso por **descritores de segurança**, com permissões e dono **até o nível do arquivo**;
- registra os carimbos de hora **MACE** (*Modified, Accessed, Created, Entry modified*), muito usados em **investigações forenses** para reconstruir o histórico de um arquivo;
- permite **criptografar o sistema de arquivos** inteiro.

A formatação NTFS cria estas estruturas:

- **setor de inicialização da partição**: os primeiros 16 setores (o setor é o menor bloco de gravação do disco, em geral 512 bytes), com a localização da MFT; os últimos 16 guardam uma cópia;
- **MFT** (*Master File Table* — tabela mestra de arquivos): a localização de todos os arquivos e pastas, com atributos como segurança e carimbos de hora;
- **arquivos de sistema**: arquivos ocultos com informações sobre volumes e atributos;
- **área de arquivos**: onde ficam os arquivos e pastas.

**Importante:** formatar **não apaga tudo**: os dados antigos podem ser recuperados do espaço livre. Em um disco reutilizado, deve-se fazer um **apagamento seguro**, que grava dados no disco inteiro várias vezes.

### 19.4 Fluxos de Dados Alternativos

O NTFS guarda cada arquivo como uma série de **atributos**, como o nome e os carimbos de hora. O conteúdo fica no atributo **$DATA**, o **fluxo de dados**. É possível anexar ao arquivo **fluxos de dados alternativos** (**ADS**, *Alternate Data Streams*), usados por alguns programas para guardar informações extras.

**Importante:** o ADS é **fácil de usar para esconder dados**: um atacante pode guardar código malicioso em um ADS e chamá-lo de outro arquivo.

O ADS é indicado por dois-pontos depois do nome, como `Testfile.txt:ADS`. Exemplo:

1. `echo "Alternate Data Here" > Testfile.txt:ADS` grava o texto em um ADS chamado ADS;
2. `dir` mostra o arquivo com **0 byte**: o ADS não aparece;
3. `more < Testfile.txt:ADS` mostra o conteúdo escondido;
4. `dir /r` revela o fluxo `Testfile.txt:ADS:$DATA`.

### 19.5 Processo de Inicialização

Há dois tipos de **firmware** (o software gravado na placa-mãe):

- **BIOS** (*Basic Input-Output System*): criado no início dos anos 1980; tem dificuldade de suportar os recursos novos;
- **UEFI** (*Unified Extensible Firmware Interface*): criado para substituir o BIOS. Guarda o código de inicialização no firmware e **entra direto no modo protegido**, o que **aumenta a segurança** na inicialização.

A inicialização ocorre assim:

1. **BIOS**: inicializa o hardware e faz o **POST** (*Power-On Self-Test*), que testa os dispositivos; ao achar o disco do sistema, procura o **MBR** (*Master Boot Record*), que tem um pequeno programa que localiza e carrega o sistema. **UEFI**: carrega os programas **.efi** de uma partição especial, a **ESP** (*EFI System Partition*);
2. o **Bootmgr.exe** passa a CPU do modo real (o modo antigo, que só enxerga 1 MB de memória) para o **modo protegido**, para usar toda a memória, e lê o **BCD** (*Boot Configuration Data*), que diz se o computador está saindo da hibernação;
3. **saindo da hibernação**: o **Winresume.exe** lê o **Hiberfil.sys**, que guarda o estado do computador, e vai para o logon;
4. **inicialização a frio**: o **Winload.exe** registra a configuração de hardware no registro e usa a **KMCS** (*Kernel Mode Code Signing*) para garantir que **todos os drivers tenham assinatura digital**;
5. o **Ntoskrnl.exe** inicia o kernel e configura a HAL;
6. o **SMSS** (*Session Manager Subsystem*) lê o registro, cria o ambiente do usuário, inicia o **Winlogon** e prepara a área de trabalho de cada usuário.

BIOS/UEFI → Bootmgr.exe → BCD → Winload.exe → Ntoskrnl.exe → SMSS → Logon

![Sequência de inicialização do Windows, do firmware ao logon](img/endpoint/end_boot.png){width=6in}

### 19.6 Programas que Iniciam com o Windows

O **registro** do Windows, banco de dados com todas as configurações, tem duas chaves que iniciam programas e serviços automaticamente:

- **HKEY\_LOCAL\_MACHINE**: configurações do computador, incluindo os serviços que **iniciam a cada inicialização**;
- **HKEY\_CURRENT\_USER**: configurações do usuário conectado, incluindo os serviços que **iniciam só quando ele faz logon**.

Os tipos de entrada são **Run, RunOnce, RunServices, RunServicesOnce e Userinit**. É mais seguro alterá-las com o **Msconfig.exe** (Configuração do Sistema), que tem cinco guias:

| Guia | Função |
| --- | --- |
| Geral | Escolhe a inicialização **normal** (todos os drivers e serviços), **de diagnóstico** (só os básicos) ou **seletiva** |
| Inicialização do sistema | Escolhe o sistema a iniciar e a **inicialização segura**, usada para resolver problemas |
| Serviços | Lista os serviços que podem iniciar com o sistema |
| Inicialização de programas | Abre o Gerenciador de Tarefas para ativar ou desativar os programas que iniciam sozinhos |
| Ferramentas | Abre ferramentas comuns do sistema |

### 19.7 Desligamento

É sempre melhor **desligar corretamente**: arquivos abertos, serviços fechados fora de ordem e aplicativos travados podem ser danificados se a energia for cortada. O sistema fecha primeiro os aplicativos do **modo usuário** e depois os processos do **modo kernel**. Se um processo de usuário não responder, o usuário pode esperar ou encerrá-lo; se um de kernel não responder, o desligamento trava e pode exigir o botão de energia.

O desligamento é feito pelo menu Iniciar, pelo comando **shutdown** ou por **Ctrl+Alt+Delete**, com três opções:

- **desligar**;
- **reiniciar**;
- **hibernar**: grava o estado do computador em um arquivo e permite voltar rapidamente com tudo aberto.

### 19.8 Processos, Threads e Serviços

Um aplicativo é formado por **processos**. Um **processo** é **um programa em execução**, e cada um tem pelo menos um **thread**, a **parte do processo que pode ser executada**; é nela que a CPU faz os cálculos. Os processos são vistos e configurados no **Gerenciador de Tarefas**.

Os threads de um processo ficam **no mesmo espaço de endereços** e não acessam o de outros processos, o que evita corrupção. Como o Windows é multitarefa, vários threads rodam ao mesmo tempo, conforme o número de processadores.

Os **serviços** são processos que **rodam em segundo plano** para apoiar o sistema e os aplicativos, como o acesso sem fio ou um servidor FTP. Podem iniciar automaticamente ou à mão e ser parados, reiniciados ou desativados no painel **Serviços**. É preciso cuidado: encerrar um serviço pode afetar programas que dependem dele.

### 19.9 Memória e Identificadores

As instruções ficam na **RAM** até a CPU processá-las. O **espaço de endereços virtuais** de um processo é o conjunto de endereços que ele pode usar; o endereço virtual não é o local físico, mas uma entrada em uma **tabela de páginas** que o traduz para o endereço físico.

| Windows | Espaço virtual por processo |
| --- | --- |
| 32 bits | Até 4 GB |
| 64 bits | 8 TB |

Cada processo de usuário roda em seu espaço privado e **não acessa diretamente os recursos do kernel**; para isso usa um **identificador** (*handle*), que dá o acesso necessário sem ligação direta. A ferramenta **RAMMap**, do pacote **Windows Sysinternals**, mostra como a memória está distribuída entre kernel, processos, drivers e aplicativos.

### 19.10 Registro do Windows

O **registro** é um **banco de dados hierárquico** com todas as informações de hardware, aplicativos, usuários e configurações, e de como eles interagem, como os arquivos que cada aplicativo abre. A hierarquia é: **ramo** (*hive*) → **chave** → **subchave**, e os **valores** guardam os dados. Uma chave pode ter até **512 níveis**. Os cinco ramos são:

| Ramo | Conteúdo |
| --- | --- |
| HKEY\_CURRENT\_USER (HKCU) | Usuário conectado no momento |
| HKEY\_USERS (HKU) | Todas as contas de usuário do host |
| HKEY\_CLASSES\_ROOT (HKCR) | Registros **OLE** (*Object Linking and Embedding*), que permitem inserir objetos de um aplicativo em outro, como uma planilha em um documento do Word |
| HKEY\_LOCAL\_MACHINE (HKLM) | Informações do sistema |
| HKEY\_CURRENT\_CONFIG (HKCC) | Perfil de hardware atual |

**Não é possível criar ramos novos**; chaves e valores podem ser criados, alterados ou apagados por uma conta de administrador, com o **regedit.exe**. Pequenas mudanças podem ter **efeitos catastróficos**. O caminho das chaves usa a barra invertida (`\`), como as pastas; exemplo: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`. Os tipos de valor são:

- **REG\_BINARY**: dados binários brutos;
- **REG\_DWORD**: um número de 32 bits, muito usado como chave liga e desliga (0 ou 1);
- **REG\_SZ**: textos (*strings*).

Para a segurança, o registro importa de duas formas:

- **persistência de malware**: um programa malicioso pode criar uma chave para **iniciar com o computador sem mostrar nada**, como um keylogger. Nas auditorias e na limpeza de sistemas infectados, deve-se **revisar os locais de inicialização** no registro;
- **forense**: o registro guarda a atividade do usuário, como todos os dispositivos já conectados (nome, fabricante e número de série) e quais documentos foram abertos, onde estão e quando foram acessados.

## 20. Configuração e Monitoramento do Windows

Conhecida a arquitetura, o próximo passo é saber configurar o Windows com segurança e acompanhar o que acontece nele.

### 20.1 Executar como Administrador

**Não é recomendável entrar no Windows com a conta de Administrador** ou com uma conta de privilégios administrativos, porque todo programa executado herda esses privilégios, e um **malware com privilégios de administrador tem acesso total** aos arquivos. Quando um programa precisa desses privilégios, há duas formas:

- clicar com o botão direito no executável e escolher **Executar como administrador**;
- abrir um **prompt de comando de administrador**: tudo o que for executado nele, inclusive instalações, terá privilégios de administrador.

### 20.2 Usuários Locais, Grupos e Domínios

Na primeira inicialização, o Windows pede para criar uma conta, o **usuário local**, com as configurações, permissões e arquivos daquele usuário. Também existem as contas **Convidado** e **Administrador**, **desabilitadas por padrão**. As boas práticas são:

- **não habilitar a conta Administrador** nem dar privilégios administrativos aos usuários padrão: quando for preciso, o sistema pede a senha de administrador só para aquela tarefa, o que impede software não autorizado de se instalar;
- **não habilitar a conta Convidado**: ela não tem senha e serve para computadores usados por muitas pessoas sem conta, com ambiente padrão e privilégios limitados.

Para facilitar a administração, o Windows usa **grupos**: cada grupo tem um nome e um conjunto de permissões, que o usuário recebe ao entrar nele. Um usuário pode estar em vários grupos; quando as permissões se sobrepõem, algumas, como **"negar explicitamente"**, prevalecem. Há grupos prontos, como o **Usuários do Log de Desempenho**. Usuários e grupos locais são gerenciados no **lusrmgr.msc**.

Um **domínio** é um serviço de rede em que **usuários, grupos, computadores, periféricos e configurações de segurança ficam em um banco de dados** guardado nos **controladores de domínio** (**DCs**). Todos se autenticam no DC para entrar e acessar recursos, e as configurações do DC **prevalecem sobre as do computador local**.

### 20.3 Linha de Comando e PowerShell

A **CLI** (*Command-Line Interface*) do Windows, aberta pelo **cmd.exe**, executa programas e gerencia arquivos e pastas. Arquivos **batch** executam vários comandos em sequência, como um script simples. Regras da CLI:

- nomes de arquivos e caminhos **não diferenciam maiúsculas de minúsculas**;
- cada unidade tem uma letra seguida de dois-pontos e barra invertida, que indica a raiz; as pastas também são separadas por barra invertida, como em `C:\Users\Jim\Desktop\file.txt`;
- as opções dos comandos usam a **barra** (/);
- a tecla **Tab** completa nomes de pastas e arquivos;
- as **setas para cima e para baixo** acessam o histórico de comandos da sessão;
- para trocar de unidade, digita-se a letra e dois-pontos.

O **PowerShell** cria scripts para automatizar tarefas que a CLI não consegue, porque ela **não interage com o núcleo do Windows nem com a GUI**. Também pode rodar como administrador. Executa três tipos de comandos:

- **cmdlets**: executam uma ação e passam a saída ou um objeto ao próximo comando;
- **scripts**: arquivos **.ps1** com comandos do PowerShell;
- **funções**: trechos de código chamados em um script.

A ajuda tem quatro níveis: `get-help comando` (básica), `-examples` (com exemplos), `-detailed` (detalhada) e `-full` (completa).

### 20.4 WMI e o Comando net

A **WMI** (*Windows Management Instrumentation* — instrumentação de gerenciamento do Windows) **gerencia computadores remotos**: obtém informações de componentes, estatísticas de hardware e software e monitora a saúde dos computadores. Fica em Gerenciamento do Computador > Serviços e Aplicativos > Controle WMI, com quatro guias: Geral, Backup/Restaurar, Segurança e Avançado.

**Importante:** atacantes usam a WMI para se conectar a sistemas remotos, alterar o registro (ver item 19.10) e executar comandos. Ela **escapa da detecção** porque é tráfego comum, confiado pelos dispositivos de segurança, e os comandos remotos **quase não deixam rastros**. Por isso, o acesso à WMI deve ser **muito restrito**.

O comando **net** administra e mantém o sistema, com vários subcomandos (`net help` lista todos):

| Comando | Função |
| --- | --- |
| `net accounts` | Define os requisitos de senha e de logon |
| `net session` | Lista ou desconecta sessões com outros computadores |
| `net share` | Cria, remove ou gerencia compartilhamentos |
| `net start` | Inicia um serviço de rede ou lista os que estão rodando |
| `net stop` | Para um serviço de rede |
| `net use` | Conecta, desconecta e mostra recursos compartilhados |
| `net view` | Lista os computadores e dispositivos da rede |

### 20.5 Gerenciador de Tarefas e Monitor de Recursos

Essas duas ferramentas mostram os aplicativos, serviços e processos em execução e o desempenho (CPU, memória, disco e rede). São **especialmente úteis quando se suspeita de malware**.

O **Gerenciador de Tarefas** tem estas guias:

| Guia | O que mostra |
| --- | --- |
| Processos | Programas e processos em execução, com o uso de recursos; permite examinar ou encerrar um processo |
| Desempenho | Visão geral e detalhada de CPU, memória, disco e rede |
| Histórico de aplicativos | Uso de recursos ao longo do tempo, que revela aplicativos que consomem demais |
| Inicializar | Programas que iniciam com o computador; permite desativá-los |
| Usuários | Usuários conectados e seus recursos; permite desconectá-los |
| Detalhes | Mais opções: **prioridade**, **afinidade de CPU** (qual núcleo o programa usa) e **analisar cadeia de espera**, que mostra se um processo está esperando outro ou travado |
| Serviços | Serviços carregados, com **PID** (identificador do processo), descrição e estado |

O **Monitor de Recursos** dá informações mais detalhadas, úteis para achar a causa de um comportamento irregular:

| Guia | O que mostra |
| --- | --- |
| Visão geral | Uso geral de cada recurso; selecionar um processo filtra todas as guias |
| CPU | PID, threads, CPU usada, uso médio, serviços, identificadores e módulos de cada processo |
| Memória | Uso de memória por processo e da RAM inteira |
| Disco | Processos que usam o disco, com leitura e gravação |
| Rede | Processos que usam a rede, **conexões TCP atuais e portas em escuta**; revela se um processo não autorizado acessa a rede e com qual endereço fala |

### 20.6 Rede no Windows

O **Centro de Rede e Compartilhamento** verifica e cria conexões, configura o compartilhamento e altera os adaptadores. Mostra se há acesso à internet, se a rede é **privada, pública ou de convidados** e se é com ou sem fio. Em **Alterar configurações do adaptador**, abre-se o adaptador e o protocolo **TCP/IPv4** ou **TCP/IPv6**, para obter o IP automaticamente ou defini-lo à mão.

**Observação:** o **Grupo Doméstico** foi removido do Windows 10 na versão 1803.

Dois comandos testam a rede:

- **nslookup**: testa o DNS; `nslookup cisco.com` deve retornar o endereço do servidor;
- **netstat**: mostra as **conexões ativas**, as portas abertas, onde estão ligadas e o estado, como ESTABLISHED (estabelecida) e TIME\_WAIT.

### 20.7 Compartilhamentos e Área de Trabalho Remota

O **SMB** (*Server Message Block*), criado pela IBM com ajuda da Microsoft, **compartilha recursos de rede**, principalmente arquivos em hosts remotos. A conexão usa o formato **UNC** (*Universal Naming Convention*):

`\\servidor\compartilhamento\arquivo`

O servidor pode ser um nome DNS (ver seção 10), um nome **NetBIOS** (o nome curto do computador na rede Windows) ou um IP; o compartilhamento é a pasta raiz no host remoto. Ao compartilhar, define-se a área do sistema de arquivos e o controle de acesso: ler, gravar ou negar.

O Windows cria **compartilhamentos administrativos**, identificados pelo **cifrão** (`$`): **`C$`, `D$`** para cada volume, **`admin$`** para a pasta do Windows e **`print$`** para as impressoras. **Só administradores** os acessam. Para conectar, digita-se o UNC no Explorador de Arquivos, com as **credenciais do computador remoto**.

O **RDP** (*Remote Desktop Protocol*) permite **entrar em um host remoto e controlá-lo como se fosse local**. Os analistas o usam muito nas investigações.

**Importante:** como foi feito para controlar hosts remotamente, o RDP é **alvo natural dos atacantes**. É preciso cuidado ao ativá-lo, principalmente em versões antigas sem correções, como em sistemas de controle industrial; **limitar sua exposição à internet** e usar políticas como a **Confiança Zero** (*Zero Trust*), que não confia automaticamente em ninguém.

### 20.8 Windows Server

O **Windows Server** é a edição usada principalmente em **data centers**, numa família iniciada no **Windows Server 2003** (o Windows 2000 Server é considerado uma versão cliente do NT 5.0; o 2003 é baseado no NT 5.2). Ele oferece:

- **serviços de rede**: DNS, DHCP, serviços de terminal (acesso remoto de vários usuários ao mesmo servidor), controlador de rede e virtualização Hyper-V (máquinas virtuais);
- **serviços de arquivo**: SMB, NFS (compartilhamento de arquivos com Linux) e DFS (*Distributed File System*, que reúne pastas de vários servidores sob um só caminho);
- **serviços web**: FTP, HTTP e HTTPS;
- **gerenciamento**: Política de Grupo e **Active Directory** (serviço de diretório dos domínios).

## 21. Segurança do Windows

O Windows tem ferramentas próprias para encontrar sinais de ataque e proteger o computador.

### 21.1 O Comando netstat

O malware costuma **abrir portas de comunicação** para enviar e receber dados. O **netstat** procura **conexões de entrada ou de saída não autorizadas**; sozinho, mostra todas as conexões TCP ativas. Se um programa parecer suspeito, uma pesquisa confirma se é legítimo; depois, o processo é encerrado no Gerenciador de Tarefas e o computador é limpo com software antimalware.

O comando **netstat -abno**, em um prompt de administrador, **liga cada conexão ao processo e ao PID** que a criou. Exemplos de saída: a porta 3389 em escuta pelo TermService (área de trabalho remota) e a porta 135 pelo svchost.exe.

**Observação:** sem privilégios de administrador, aparece a mensagem "A operação solicitada requer elevação".

Como pode haver vários processos com o mesmo nome, usa-se o **PID**, que é **único para cada processo**, para achar o processo certo no Gerenciador de Tarefas (a coluna PID é ativada com o botão direito no cabeçalho).

### 21.2 Visualizador de Eventos

O **Visualizador de Eventos** registra o **histórico de eventos de aplicativos, segurança e sistema**, uma ferramenta valiosa para identificar problemas. Há duas categorias de logs: **Logs do Windows** e **Logs de Aplicativos e Serviços**. Cada evento tem:

- um **nível**: informação, aviso, erro ou crítico;
- a data e a hora;
- a origem;
- um **ID de evento**, que identifica o tipo.

É possível criar **exibições personalizadas** por tipo, período ou nível. A exibição pronta **Eventos Administrativos** reúne os eventos críticos, de erro e de aviso de todos os logs administrativos e é um bom ponto de partida. Os **logs de segurança** ficam em Logs do Windows e usam IDs de evento.

### 21.3 Atualizações do Windows

Nenhum software é perfeito, e alguns ataques chegam antes das defesas, os **ataques de dia zero** (ver item 6.3). Para a maior proteção possível, o Windows deve estar sempre com as correções e os service packs mais recentes:

- **patches** (correções): atualizações de código que impedem que um vírus ou worm recém-descoberto tenha sucesso;
- **service pack**: um pacote que reúne várias correções e atualizações.

Muitos ataques teriam sido bem menos graves se mais usuários tivessem instalado o último service pack. As empresas devem usar sistemas que **distribuam, instalem e acompanhem as atualizações automaticamente**.

O **Windows Update** verifica regularmente as atualizações de alta prioridade (de segurança, críticas e service packs) e, conforme a configuração, **as instala sozinho ou avisa o usuário**. Também permite verificar manualmente, ver o histórico, definir os **horários em que o computador não reinicia sozinho**, como o expediente, e escolher quando reiniciar.

### 21.4 Política de Segurança Local

Uma **política de segurança** é um **conjunto de objetivos que garante a segurança** da rede, dos dados e dos computadores. É um documento sempre em evolução, conforme a tecnologia, o negócio e as necessidades dos funcionários.

Na maioria das redes Windows, o **Active Directory** organiza os computadores em domínios, e o administrador define uma **Política de Segurança de Domínio** aplicada a todos. Para **computadores autônomos**, fora de um domínio, usa-se a **Política de Segurança Local**, que define:

- **política de senha** (em Políticas de Conta): os critérios de senha de todos os usuários locais. Senhas evitam roubo de dados e confirmam que os registros de eventos são válidos;
- **política de bloqueio de conta**: impede ataques de **força bruta**; por exemplo, depois de **cinco tentativas erradas**, a conta fica **bloqueada por 30 minutos**, e então a contagem volta a zero;
- **bloqueio ao iniciar a proteção de tela**: depois de pouco tempo sem uso, o computador só volta a ser usado com novo login;
- **direitos de usuário**, **regras de firewall** (ver item 16.1) e o **AppLocker**, que restringe os arquivos que usuários ou grupos podem executar.

Se vários computadores autônomos precisam da mesma política, ela pode ser **exportada**, por exemplo como workstation.inf, e importada nos outros.

### 21.5 Windows Defender

O **malware** inclui vírus, worms, cavalos de Troia, keyloggers, **spyware** (que espiona o usuário) e **adware** (que exibe publicidade). Os tipos de proteção antimalware são:

| Proteção | Função |
| --- | --- |
| Antivírus | Monitora continuamente; ao achar um vírus, avisa e tenta colocá-lo em **quarentena** ou excluí-lo |
| Contra adware | Procura programas que exibem publicidade |
| Contra phishing | Bloqueia os IPs de sites de phishing conhecidos e avisa sobre sites suspeitos |
| Contra spyware | Procura keyloggers e outros spywares |
| Fontes confiáveis e não confiáveis | Avisa sobre programas inseguros antes da instalação e sites inseguros antes da visita |

Pode ser preciso usar vários programas e várias varreduras para remover todo o malware, mas **só um programa antimalware deve rodar por vez**. Empresas como McAfee, Symantec e Kaspersky oferecem proteção completa.

O **Windows Defender** é a proteção interna contra vírus e spyware, **ativada por padrão** com proteção em tempo real. Permite varreduras manuais, atualização manual das definições e consulta ao histórico do que foi encontrado.

### 21.6 Firewall do Windows Defender

Um firewall nega seletivamente o tráfego, **abrindo e fechando as portas** usadas pelos aplicativos. Há duas abordagens:

- **política restritiva**: **só as portas necessárias ficam abertas**; o que não for explicitamente permitido é negado;
- **política permissiva**: **tudo é permitido**, menos o que for explicitamente negado.

Antes, os equipamentos vinham com configurações permissivas, e como os usuários não as ajustavam, muitos ficavam expostos. Hoje, a maioria vem **o mais restritiva possível**.

No Painel de Controle, em Sistema e Segurança, o **Firewall do Windows Defender** permite liberar aplicativos, ativá-lo ou desativá-lo (para usar outro firewall) e, nas **Configurações avançadas**, criar regras de entrada e saída, importar e exportar políticas e monitorar o firewall.

## 22. Fundamentos do Linux

O **Linux** é um sistema operacional **de código aberto**, rápido, poderoso e muito personalizável, feito para funcionar em rede como cliente ou servidor. Saber usá-lo é muito valorizado nas operações de segurança cibernética.

### 22.1 O que é o Linux

O Linux foi criado em **1991**. É de código aberto, rápido, confiável e pequeno, exige **poucos recursos de hardware** e é muito personalizável. Ao contrário do Windows e do macOS, foi criado e é mantido por **uma comunidade de programadores**, e está em dispositivos "de relógios de pulso a supercomputadores".

Ele foi projetado para **funcionar em rede**, o que facilita criar aplicativos de rede. Como é aberto, qualquer pessoa ou empresa pode obter o código-fonte do **kernel**, examiná-lo, modificá-lo, recompilá-lo e redistribuí-lo, cobrando ou não.

Uma **distribuição** (*distro*) é um pacote que reúne o kernel Linux com ferramentas e programas próprios. Algumas organizações cobram pelo suporte, mas a maioria oferece a distribuição de graça, sem suporte. Exemplos: **Debian, Red Hat, Ubuntu, CentOS e SUSE**.

### 22.2 O Valor do Linux para a Segurança

O Linux é muitas vezes o sistema escolhido no **SOC** (*Security Operations Center* — centro de operações de segurança), porque:

- **é de código aberto**: pode ser obtido de graça e adaptado, por exemplo, para criar um sistema próprio de análise de segurança;
- **sua CLI é muito poderosa**: a GUI facilita tarefas, mas acrescenta complexidade e consome mais recursos; a CLI permite trabalhar no terminal e também **remotamente**;
- **dá mais controle ao usuário**: o administrador, chamado **root** ou **superusuário**, tem **poder absoluto** sobre o computador e pode controlar com precisão como o sistema trata os pacotes de rede;
- **permite controlar melhor a comunicação de rede**: por ser ajustável em quase tudo, é ótimo para criar aplicativos de rede, e muitas ferramentas de rede **só existem para Linux**.

### 22.3 Ferramentas do SOC e de Teste de Penetração

O Linux pode ser adaptado para ser a plataforma de análise ideal, instalando só os pacotes necessários. Um exemplo é o **Security Onion**, conjunto de ferramentas abertas para análise de segurança de rede, cujo console do analista é o **Sguil**. As ferramentas típicas de um SOC são:

| Ferramenta | Função |
| --- | --- |
| Captura de pacotes | Permite observar cada detalhe de uma transação de rede; exemplo: **Wireshark** |
| Análise de malware | Executa e observa o malware **com segurança**, sem comprometer o sistema |
| IDS | Monitora e inspeciona o tráfego em tempo real; se algo corresponder a uma regra, executa uma ação predefinida |
| Firewalls | Decidem, por regras, se o tráfego pode entrar ou sair |
| Gerenciadores de logs | Facilitam o acompanhamento do grande volume de registros de eventos |
| SIEM (*Security Information and Event Management*) | Analisa **em tempo real** os alertas e logs de IDS, firewalls e outros dispositivos |
| Sistemas de tíquetes | Atribuem, editam e registram tarefas; os alertas costumam ser entregues aos analistas por tíquetes |

Os computadores Linux do SOC também têm ferramentas de **teste de penetração** (*pentest*), o processo de **procurar vulnerabilidades atacando a rede ou o computador**, como geradores de pacotes, scanners de portas e explorações de prova de conceito. O **Kali Linux** é uma distribuição que reúne muitas dessas ferramentas, organizadas em categorias como coleta de informações, análise de vulnerabilidades, ataques a senhas e a redes sem fio, *sniffing* e *spoofing*, exploração, forense e engenharia social.

### 22.4 O Shell do Linux

O usuário se comunica com o Linux pela **CLI** ou pela **GUI**. O Linux costuma iniciar na GUI, que esconde a CLI; para usá-la, abre-se um **emulador de terminal**, como Terminator, eterm, xterm, konsole e gnome-terminal. O **JSLinux**, de Fabrice Bellard, roda um Linux emulado no navegador.

**Observação:** os termos **shell, console, terminal** e janela do terminal costumam ser usados como sinônimos.

Os comandos do Linux são **programas** guardados no disco. Ao digitar um comando, o shell o procura em uma lista de diretórios chamada **caminho** (*path*); se o comando não estiver no caminho, é preciso indicar onde ele está. O comando **man** (manual) mostra a documentação, como em `man ls`. Os comandos básicos são:

| Comando | Função |
| --- | --- |
| `mv` | Move ou renomeia arquivos e diretórios |
| `chmod` | Altera as permissões de arquivos |
| `chown` | Altera o dono de um arquivo |
| `dd` | Copia dados de uma entrada para uma saída |
| `pwd` | Mostra o diretório atual |
| `ps` | Lista os processos em execução |
| `su` | Entra como outro usuário ou como superusuário |
| `sudo` | Executa um comando como superusuário (ou outro usuário) |
| `grep` | Procura textos em um arquivo ou na saída de outro comando, ligado por um *pipe* (\|) |
| `ifconfig` | Mostra ou configura a placa de rede; está obsoleto, e o atual é `ip address` |
| `apt-get` | Instala, configura e remove pacotes no Debian e derivados; é a interface amigável do **dpkg** |
| `iwconfig` | Mostra ou configura a placa de rede sem fio |
| `shutdown` | Desliga, reinicia ou suspende o sistema e pode desconectar os usuários |
| `passwd` | Altera a senha |
| `cat` | Mostra o conteúdo de um arquivo |
| `man` | Mostra a documentação de um comando |

Para arquivos e diretórios, os principais são: `ls` (lista os arquivos), `cd` (muda de diretório), `mkdir` (cria um diretório), `cp` (copia), `mv` (move ou renomeia) e `rm` (remove).

**Observação:** os comandos só funcionam se o usuário tiver as **permissões** adequadas.

### 22.5 Arquivos de Texto e de Configuração

O Linux tem muitos editores de texto, gráficos ou de linha de comando. Os de **linha de comando** são essenciais porque permitem **editar arquivos em um computador remoto**: em uma sessão **SSH** (acesso remoto seguro por texto), não há interface gráfica. Um editor popular é o **nano**, controlado só pelo teclado: **Ctrl+O** salva, **Ctrl+W** busca e **Ctrl+G** mostra a ajuda.

**Importante:** no Linux, **tudo é tratado como arquivo**: a memória, os discos, o monitor e os diretórios. Mostrar algo na tela, por exemplo, é gravar no arquivo que representa o monitor.

O próprio sistema é configurado por **arquivos de configuração**, em geral de texto, que guardam os ajustes de cada aplicativo ou serviço; alguns serviços têm vários. Ao iniciar, os serviços leem esses arquivos para definir seu comportamento.

Exemplo: o arquivo **/etc/hosts** guarda associações fixas entre nomes e IPs, que permitem usar um nome em vez do endereço. Só o superusuário pode alterá-lo, por isso o administrador usa `sudo nano /etc/hosts`.

### 22.6 Clientes, Servidores e Portas

Os **servidores** são computadores com software que **fornece serviços aos clientes pela rede**: arquivos, e-mails, páginas web ou tarefas de manutenção, como gerenciamento de registros e varredura de disco. **Cada serviço exige um software de servidor**, como um servidor de arquivos que permite baixar (*download*) e enviar (*upload*) arquivos.

Para que um computador ofereça vários serviços, usam-se **portas**: uma porta é um **recurso de rede reservado a um serviço**, e o servidor fica **"escutando"** na porta associada a ele. O administrador pode escolher a porta, mas é comum manter a padrão, porque os clientes já vêm configurados para ela. São as **portas bem conhecidas**:

| Porta | Serviço |
| --- | --- |
| 20/21 | FTP (*File Transfer Protocol*) |
| 22 | SSH (*Secure Shell*) |
| 23 | Telnet (login remoto) |
| 25 | SMTP |
| 53 | DNS |
| 67/68 | DHCP |
| 69 | TFTP (*Trivial File Transfer Protocol*) |
| 80 | HTTP |
| 110 | POP3 (*Post Office Protocol* versão 3) |
| 123 | NTP |
| 143 | IMAP (*Internet Message Access Protocol*) |
| 161/162 | SNMP |
| 443 | HTTPS |

Os **clientes** são programas feitos para **falar com um tipo de servidor** usando um protocolo definido. Exemplos: o navegador é um cliente web que usa HTTP na porta 80, e o cliente FTP envia e recebe arquivos de um servidor FTP.

## 23. Administração de Servidores Linux

No Linux, administrar um servidor é, em grande parte, cuidar dos seus arquivos de configuração, reforçar sua segurança e acompanhar seus registros.

### 23.1 Arquivos de Configuração dos Serviços

Os serviços são gerenciados por **arquivos de configuração**, com opções como o número da porta, o local dos recursos hospedados e as regras de autorização dos clientes. O serviço lê esses arquivos ao iniciar, e uma alteração **costuma exigir reiniciar o serviço**. Como os serviços em geral rodam com privilégios de superusuário, editar seus arquivos também exige esses privilégios. Exemplos:

- **/etc/nginx/nginx.conf**: o **Nginx**, servidor web leve;
- **/etc/ntp.conf**: o NTP (ver item 17.5), com os servidores do *pool* (o grupo de servidores públicos de hora) e as restrições de consulta;
- **/etc/snort/snort.conf**: o **Snort**, IDS baseado em Linux; por exemplo, `ipvar HOME_NET [209.165.200.224/27]` define a rede protegida e `ipvar EXTERNAL_NET any`, a externa.

Não há um formato obrigatório, mas é comum usar **opção = valor**, e o caractere **#** indica comentário.

### 23.2 Endurecimento de Dispositivos

O **endurecimento** (*hardening*) é **aplicar métodos comprovados para proteger o dispositivo e seu acesso administrativo**: manter senhas, configurar recursos avançados de login remoto, usar login seguro por SSH (ver item 22.5) e definir **papéis administrativos**, já que nem todo o pessoal de TI precisa do mesmo nível de acesso.

Muitas distribuições vêm com serviços ativos por motivos históricos que não são mais necessários; **pará-los e impedir que iniciem sozinhos** também é endurecimento. As **atualizações** são essenciais: novas vulnerabilidades surgem todos os dias, e um computador atualizado tem menos chance de ser comprometido. As boas práticas são:

- garantir a **segurança física**;
- **minimizar os pacotes instalados**;
- **desativar os serviços não usados**;
- usar SSH e **desabilitar o login do root (ver item 22.2) por SSH**;
- manter o sistema atualizado;
- **desativar a detecção automática de USB**;
- exigir senhas fortes;
- forçar a troca periódica de senhas;
- impedir a reutilização de senhas antigas.

### 23.3 Logs do Linux

Os **arquivos de log** registram os eventos importantes do kernel, dos serviços e dos aplicativos. Revisá-los periodicamente dá uma visão clara do **desempenho, da segurança e dos problemas** do computador e permite agir antes que eles piorem. Os logs se dividem em quatro categorias:

- de aplicativos;
- de eventos;
- de serviços;
- do sistema.

Alguns logs tratam dos **daemons**, processos que **rodam em segundo plano sem interação do usuário**. Exemplo: o **SSSD** (*System Security Services Daemon*) gerencia o acesso remoto e a autenticação de login único. Os principais logs são:

| Arquivo | Conteúdo |
| --- | --- |
| /var/log/messages | Atividade geral do computador, com mensagens informativas e não críticas; no Debian, o equivalente é **/var/log/syslog** |
| /var/log/auth.log | **Eventos de autenticação** no Debian e no Ubuntu |
| /var/log/secure | Equivalente do auth.log no **Red Hat e no CentOS**; registra logins sudo e SSH e erros do SSSD |
| /var/log/boot.log | Mensagens do processo de inicialização |
| /var/log/dmesg | Mensagens do *ring buffer* do kernel (uma área de memória circular onde o kernel anota seus avisos) sobre o hardware e os drivers; importante porque, nesses eventos de baixo nível, o syslog ainda não está rodando |
| /var/log/kern.log | Informações registradas pelo kernel |
| /var/log/cron | Execução das **tarefas agendadas** (*cron jobs*), com estado e erros |
| /var/log/mysqld.log ou mysql.log | Mensagens do MySQL (um banco de dados gratuito muito usado em sites); o primeiro no Red Hat, CentOS e Fedora, o segundo no Debian e Ubuntu |

Cada linha de um log é um evento, e o **carimbo de data e hora** no início marca quando ele ocorreu.

## 24. Sistema de Arquivos e Permissões do Linux

Como no Linux tudo é arquivo, o sistema de arquivos e as permissões são a base da sua organização e da sua segurança.

### 24.1 Tipos de Sistemas de Arquivos

Os sistemas de arquivos variam em velocidade, flexibilidade, segurança, tamanho e estrutura, e o administrador escolhe o mais adequado:

| Sistema | Características |
| --- | --- |
| ext2 | Antigo padrão de muitas distribuições; **sem diário**, o que melhora o desempenho e reduz as gravações; por isso ainda é escolhido para **memória flash**, que aceita um número limitado de gravações |
| ext3 | Melhora o ext2 com o **diário** (*journaling*); arquivos de até 32 TB |
| ext4 | Sucessor do ext3, com extensões que melhoram o desempenho e o tamanho dos arquivos; pode operar sem diário |
| NFS (*Network File System*) | Sistema **em rede**: acessar um arquivo remoto parece igual a acessar um local; padrão aberto |
| CDFS (*Compact Disc File System*) | Criado para **discos ópticos** |
| Swap (troca) | Partição usada quando **falta RAM**: o kernel move para o disco o conteúdo inativo da memória; não deve ser a solução principal, porque o disco é muito mais lento |
| HFS+ | Usado pela Apple nos Macintosh; o kernel Linux tem um módulo para lê-lo e gravá-lo |
| APFS (*Apple File System*) | Sistema atual da Apple, com **criptografia forte**, otimizado para flash e SSD |

O **diário** registra as alterações **antes de fazê-las**; se o computador falhar no meio de uma alteração, como em uma queda de energia, o diário permite restaurar ou corrigir o sistema de arquivos.

O ext4 nasceu porque os desenvolvedores do kernel temiam problemas de estabilidade ao acrescentar as extensões ao ext3 estável; o projeto se dividiu, e a versão com as extensões virou o ext4.

O **MBR**, no primeiro setor do disco particionado, guarda as informações de organização do sistema de arquivos e passa o controle a uma função que carrega o sistema operacional.

### 24.2 Montagem

**Montar** é **associar um diretório a uma partição**; depois disso, o sistema de arquivos da partição é acessado por esse diretório, o **ponto de montagem**. É algo parecido com a letra de unidade do Windows. O comando **mount**, sem opções, lista os sistemas montados. O **sistema de arquivos raiz**, representado por **/**, contém todos os arquivos do computador; um exemplo é `/dev/sda1 on / type ext4`, a primeira partição do primeiro disco, formatada em ext4.

### 24.3 Permissões de Arquivos

Para organizar o sistema e impor limites, cada arquivo tem **permissões** que definem o que **o dono (usuário), o grupo e os outros** podem fazer: **ler (r), gravar (w) e executar (x)**. O comando **ls -l** as mostra. Exemplo:

`-rwxrw-r-- 1 analyst staff 253 May 20 12:49 space.txt`

| Campo | Valor | Significado |
| --- | --- | --- |
| 1 | -rwxrw-r-- | Tipo e permissões |
| 2 | 1 | Número de links rígidos |
| 3 | analyst | Usuário dono |
| 4 | staff | Grupo dono |
| 5 | 253 | Tamanho em bytes |
| 6 | May 20 12:49 | Data e hora da última modificação |
| 7 | space.txt | Nome |

As permissões aparecem sempre na ordem **usuário, grupo e outros**:

- o primeiro caractere indica o tipo: **-** para arquivo e **d** para diretório;
- **rwx**: o usuário analyst pode ler, gravar e executar;
- **rw-**: o grupo staff pode ler e gravar;
- **r--**: os outros só podem ler.

As permissões também são definidas por **valores octais**, um dígito para cada conjunto de três bits (r=4, w=2, x=1):

| Binário | Octal | Permissão | Significado |
| --- | --- | --- | --- |
| 000 | 0 | --- | Sem acesso |
| 001 | 1 | --x | Só executar |
| 010 | 2 | -w- | Só gravar |
| 011 | 3 | -wx | Gravar e executar |
| 100 | 4 | r-- | Só ler |
| 101 | 5 | r-x | Ler e executar |
| 110 | 6 | rw- | Ler e gravar |
| 111 | 7 | rwx | Ler, gravar e executar |

#### 24.3.1 Exemplo Resolvido: Permissão em Octal

Para obter o valor octal de `rwxrw-r--`, soma-se cada conjunto:

| Conjunto | Permissão | Soma | Octal |
| --- | --- | --- | --- |
| Usuário | rwx | 4 + 2 + 1 | 7 |
| Grupo | rw- | 4 + 2 + 0 | 6 |
| Outros | r-- | 4 + 0 + 0 | 4 |

A permissão é **764**, e o comando para defini-la seria `chmod 764 space.txt`.

**Importante:** as permissões **não podem ser contornadas**: o usuário só tem os direitos que elas permitem. **Só o root pode ignorá-las**, por isso pode gravar em qualquer arquivo e, como tudo é arquivo, **tem controle total do computador**. As credenciais do root devem ter **senha forte** e não ser compartilhadas além dos administradores.

### 24.4 Links Rígidos e Simbólicos

Um **link rígido** (*hard link*) é **outro nome que aponta para o mesmo lugar do arquivo** no sistema de arquivos, o **inode** (a "ficha" de cada arquivo, com seu dono, suas permissões e sua localização no disco). É criado com `ln arquivo novo`. Exemplo: `ln space.txt space.hard.txt` faz o número de links subir para 2; alterar um altera o outro, e **apagar um deles não apaga o arquivo**, que continua acessível pelo outro nome.

Um **link simbólico** (*symbolic link* ou *soft link*) também reflete as alterações no original, mas **aponta para o nome do arquivo**. É criado com `ln -s`. Exemplo: `ln -s test.txt mytest.txt`; se **test.txt for apagado**, o link passa a apontar para algo que **não existe mais**. O `ls -l` mostra `mytest.txt -> test.txt`.

O link simbólico tem um **ponto único de falha** (o arquivo original), mas tem vantagens:

- **mostra onde está o original**, enquanto links rígidos são difíceis de localizar;
- pode apontar para **outro sistema de arquivos**, e o rígido não;
- pode apontar para **diretórios**, e o rígido não, porque o próprio sistema usa links rígidos para montar a hierarquia de diretórios.

| Característica | Link rígido | Link simbólico |
| --- | --- | --- |
| Aponta para | O mesmo inode | O nome do arquivo |
| Se o original for apagado | Continua funcionando | Fica quebrado |
| Outro sistema de arquivos | Não | Sim |
| Diretórios | Não | Sim |
| Comando | `ln` | `ln -s` |

### 24.5 Interface Gráfica do Linux

A GUI da maioria dos Linux é baseada no **X Window System** (**X** ou **X11**), que dá a estrutura básica: desenhar e mover janelas e interagir com mouse e teclado. O X funciona como **servidor**: um usuário remoto pode iniciar um aplicativo gráfico que **roda no servidor**, mas cuja janela aparece no seu computador.

O X **não define a aparência**; isso fica com os **gerenciadores de janelas**, como **Gnome** e **KDE**, o que dá muita flexibilidade e faz a GUI variar entre as distribuições. A GUI pode ser trocada pelo usuário, e o sistema funciona sem ela.

O **Ubuntu** usa o **Gnome 3**, com estes componentes:

| Componente | Função |
| --- | --- |
| Menu Aplicativos | Ícones dos aplicativos instalados |
| Dock do Ubuntu | Barra à esquerda que inicia e alterna os aplicativos favoritos |
| Barra superior | Menu do aplicativo em foco, hora e mensagens do sistema |
| Calendário e mensagens | Compromissos e mensagens atuais do sistema |
| Atividades | Alterna ou fecha aplicativos, pesquisa aplicativos, arquivos e conteúdos e troca de espaço de trabalho |
| Menu de status | Configura a rede e outros dispositivos, faz logoff, bloqueia ou desliga |

## 25. Trabalho em um Host Linux

No dia a dia, administrar um host Linux envolve instalar e atualizar programas, controlar processos e procurar sinais de comprometimento.

### 25.1 Gerenciadores de Pacotes

Muitos aplicativos são programas complexos. Um **pacote** é **um programa com todos os seus arquivos de apoio**, e o **gerenciador de pacotes** coloca cada arquivo no lugar certo. Eles variam por distribuição: o **pacman** no Arch Linux e o **dpkg** e o **apt** (*Advanced Packaging Tool*) no Debian e no Ubuntu.

- `apt-get update`: **baixa a lista de pacotes** do repositório e atualiza o banco de dados local;
- `apt-get upgrade`: **atualiza todos os pacotes instalados** para as versões mais recentes.

### 25.2 Manter o Sistema Atualizado

As **atualizações** (*patches*) corrigem vulnerabilidades conhecidas. As empresas têm calendários, mas podem lançar atualizações **fora do calendário** quando uma falha importante é descoberta. Os sistemas avisam quando há atualizações, e o usuário pode verificá-las a qualquer momento, inclusive pela GUI, como no **Atualizador de Software** do Ubuntu.

| Tarefa | Arch | Debian/Ubuntu |
| --- | --- | --- |
| Instalar um pacote | `pacman -S` | `apt install` |
| Remover um pacote | `pacman -Rs` | `apt remove` |
| Atualizar a lista de pacotes | `pacman -Syy` | `apt-get update` |
| Atualizar todos os pacotes | `pacman -Syu` | `apt-get upgrade` |

### 25.3 Processos e Bifurcação

Um **processo** é **uma instância em execução de um programa**, e os sistemas multitarefa rodam muitos ao mesmo tempo. A **bifurcação** (*fork*) é o método pelo qual o kernel permite que **um processo crie uma cópia de si mesmo**, e é **a única forma de criar processos no Linux**:

- o processo que chama vira o **pai**, e o novo, o **filho**;
- depois do fork, os dois são em certa medida independentes: têm **PIDs diferentes, mas rodam o mesmo código**.

O fork ajuda na **escalabilidade**: o servidor web **Apache**, ao se bifurcar, atende muitos pedidos com menos recursos que um servidor de processo único. Os comandos de processos são:

| Comando | Função |
| --- | --- |
| `ps` | Lista os processos no momento em que é chamado, do usuário atual ou de outros |
| `top` | Lista os processos **de forma dinâmica**, atualizando sem parar; sai com **q** |
| `kill` | Remove, reinicia ou pausa um processo; em geral, usa-se antes `ps` ou `top` para descobrir o **PID** |

**Observação:** listar processos não exige privilégios de root, mas **encerrar ou alterar processos de outros usuários exige**.

### 25.4 Malware no Linux

O Linux também sofre com vírus, cavalos de Troia e worms. Por causa da estrutura do sistema de arquivos, das permissões e das restrições das contas, ele é considerado **mais protegido**, mas **não é imune**: já houve muitas vulnerabilidades, de servidores ao kernel. Por ser aberto, as correções costumam sair **em poucas horas**.

Um vetor de ataque comum são os **serviços e processos** expostos na rede, como uma versão desatualizada do Apache. Os atacantes testam as portas abertas para descobrir o servidor e a versão e depois pesquisam falhas conhecidas. Exemplo: `telnet 209.165.200.224 80` revela na resposta `Server: nginx/1.12.0`, e o atacante procura vulnerabilidades dessa versão.

As defesas são **manter o computador atualizado** e **fechar todos os serviços e portas não usados**.

### 25.5 Detecção de Rootkits

Um **rootkit** (ver item 5.2) é um malware que **aumenta os privilégios de um usuário não autorizado** ou dá acesso a partes do sistema normalmente proibidas, e muitas vezes protege um **backdoor**. Pode ser instalado automaticamente na infecção ou à mão pelo atacante. É destrutivo porque **altera o código do kernel e seus módulos**: esconde a intrusão, apaga os rastros da instalação e até **adultera as ferramentas de diagnóstico**. A grande maioria **exige acesso root**.

Como o próprio sistema está comprometido, a detecção é difícil:

1. o computador é iniciado a partir de uma **mídia confiável**, como um CD de diagnóstico;
2. o disco comprometido é montado;
3. ferramentas confiáveis inspecionam o sistema de arquivos por **comportamento, assinaturas, diferenças e análise da memória** (*memory dump*).

A remoção é complicada e muitas vezes impossível; quando o rootkit está no kernel, a única solução real é **reinstalar o sistema**, e os rootkits de **firmware** costumam exigir **troca de hardware**.

O **chkrootkit** é um script que procura rootkits conhecidos: usa ferramentas como **strings** e **grep** para comparar as assinaturas dos programas principais e compara o diretório **/proc** com a saída do `ps` em busca de discrepâncias.

**Importante:** os verificadores de rootkit **não são 100% confiáveis**.

### 25.6 Encadeamento de Comandos

Os comandos de linha costumam fazer uma tarefa bem definida, mas podem ser combinados pelo **encadeamento** (*piping*): o caractere **|** (*pipe*) **leva a saída de um comando para a entrada de outro**. Exemplo: `ls -l | grep host` lista o diretório e mostra só as linhas com "host", como hostfile1.txt, hostfile2.txt e hostfile3.txt.

ls -l → | → grep host → Linhas filtradas

## 26. Defesa de Sistemas e Dispositivos

Um **endpoint** é **qualquer host da rede que acessa ou é acessado por outros hosts**: computadores, servidores, impressoras, telefones IP e, com a IoT, câmeras, controladores e até lâmpadas. Cada um pode ser atacado. Como o sistema operacional é alvo de muitos ataques, o primeiro trabalho é protegê-lo.

### 26.1 Segurança do Sistema Operacional

Um bom administrador configura o sistema para resistir a ameaças externas:

- **remove todos os programas e serviços desnecessários**;
- **instala a tempo as correções e atualizações** de segurança;
- trata as atualizações de forma **sistemática**:
  - cria procedimentos para acompanhar informações de segurança;
  - avalia se cada atualização se aplica;
  - planeja a instalação de atualizações e patches;
  - instala seguindo um **plano documentado**;
- define uma **linha de base** (*baseline*), um parâmetro de comparação, e compara o desempenho do sistema com ela para identificar possíveis vulnerabilidades.

### 26.2 Cuidados com Malware

Alguns pontos merecem atenção especial:

- **antivírus falsos** (*rogue antivirus*): anúncios ou janelas que imitam avisos do Windows, dizem que o computador está infectado e pedem para "limpá-lo"; clicar em qualquer lugar da janela pode **instalar malware**;
- **malware sem arquivo** (*fileless*): usa programas legítimos e vai **direto para a memória**, sem depender de arquivos, por isso **não deixa rastros** e é difícil de detectar e remover. O ataque termina quando o sistema reinicia. Usa linguagens de script como o **PowerShell** (ver item 20.3);
- **scripts maliciosos**: linguagens como **Python**, **Bash** (a linguagem da linha de comando do macOS e da maioria dos Linux) e **VBA** (*Visual Basic for Applications*, usado nas macros da Microsoft) podem criar malware;
- **software não aprovado**: instalado por engano ou de propósito, pode não ser malicioso, mas viola a política e interfere nos serviços da empresa. **Deve ser removido imediatamente**.

### 26.3 Gerenciamento de Patches

Os **patches** são atualizações de código que os fabricantes fornecem para impedir que um vírus ou worm recém-descoberto tenha sucesso; muitas vezes são reunidos em um **service pack**. Muitos ataques teriam sido evitados com o último service pack instalado.

É boa prática **testar um patch antes de distribuí-lo** para toda a empresa. Uma ferramenta de gerenciamento de patches permite gerenciá-los localmente, em vez de usar o serviço on-line do fabricante. Um **serviço de patches automático** dá aos administradores mais controle:

- **aprovam ou recusam** atualizações;
- **forçam a atualização** até uma data;
- obtêm **relatórios** das atualizações necessárias em cada sistema;
- cada computador baixa as atualizações de um **servidor local**, sem se conectar ao fabricante;
- **os usuários não podem desativar ou contornar** as atualizações.

Também é preciso atualizar os **aplicativos de terceiros**, como Adobe Acrobat, Java e Chrome. Uma abordagem **proativa** ajuda a evitar ransomware (ver item 5.3) e outras ameaças.

### 26.4 Ferramentas de Segurança do Endpoint

Uma **solução baseada em host** é um software que roda no computador e trabalha com o sistema operacional para evitar ataques. As principais são:

| Ferramenta | Função |
| --- | --- |
| Firewall de host | Restringe o tráfego de entrada e saída do dispositivo, inspecionando e filtrando os pacotes; bloqueia as conexões, salvo exceções que abrem as portas de cada programa; o Firewall do Windows vem instalado |
| HIDS (*Host-based IDS*) | Monitora o sistema operacional e os processos críticos do host; guarda os registros localmente e **consome muitos recursos**; não vê o tráfego que não chega ao host |
| HIPS | Monitora **chamadas de sistema**, acesso a arquivos e configurações no registro, além de anomalias de banda, protocolos e portas; ao detectar algo, pode **alertar, registrar, redefinir a conexão ou descartar os pacotes** |
| EDR (*Endpoint Detection and Response*) | **Monitora e coleta dados continuamente** do endpoint, analisa e **responde** às ameaças; o antivírus só bloqueia, e o EDR também **encontra** ameaças no dispositivo |
| DLP | Garante, de forma centralizada, que dados confidenciais não sejam perdidos, mal usados ou acessados por quem não deve |
| NGFW | Combina o firewall tradicional com outras filtragens, como um firewall de aplicação com **inspeção profunda de pacotes** (**DPI**, *Deep Packet Inspection*, que examina o conteúdo do pacote, e não só os cabeçalhos) em linha em um IPS |

A **criptografia** transforma os dados com um algoritmo complexo para torná-los ilegíveis; uma **chave** especial os torna legíveis de novo.

### 26.5 Criptografia do Host

As ferramentas de criptografia do host são:

- **EFS** (*Encrypting File System*), do Windows: criptografa **arquivos, pastas ou o disco inteiro**;
- **FDE** (*Full Disk Encryption* — criptografia de disco completo): criptografa **todo o conteúdo da unidade**, inclusive arquivos temporários e memória; no Windows, é feita pelo **BitLocker**;
- **TPM** (*Trusted Platform Module*): **chip da placa-mãe** que guarda chaves de criptografia, certificados digitais e senhas; precisa ser **ativado no BIOS** antes de usar o BitLocker;
- **BitLocker To Go**: criptografa **unidades removíveis**; não usa o TPM, mas exige senha para descriptografar;
- **unidade de autocriptografia**: criptografa automaticamente todos os dados do disco, impedindo o acesso pelo sistema operacional.

### 26.6 Integridade da Inicialização

O ataque pode ocorrer até no curto tempo da inicialização. A **integridade da inicialização** garante que **o sistema é confiável e não foi alterado enquanto o sistema operacional carrega**.

O **firmware**, instruções das funções básicas do computador, fica em um chip da placa-mãe. O **BIOS** é o primeiro programa executado; a **UEFI**, mais nova, define uma interface padrão entre o sistema, o firmware e os dispositivos e é **preferível por rodar em 64 bits**. Há dois mecanismos:

- **inicialização segura** (*Secure Boot*): o firmware **verifica a assinatura** de cada parte do software de inicialização (drivers e aplicativos UEFI e o sistema operacional); só com assinaturas válidas ele passa o controle ao sistema;
- **inicialização medida** (*Measured Boot*): validação **mais forte**; **mede cada componente**, do firmware aos drivers de inicialização, e **guarda as medidas no TPM**, formando um log que pode ser **verificado remotamente**. Identifica aplicativos não confiáveis e permite carregar o antimalware mais cedo.

### 26.7 Recursos de Segurança da Apple

A Apple oferece no hardware e no macOS:

| Recurso | Função |
| --- | --- |
| Hardware com foco em segurança | CPU especial, inicialização e motor de criptografia AES dedicado em um chip chamado **Secure Enclave** |
| Armazenamento criptografado | **Data Protection** e **FileVault** criptografam e descriptografam os arquivos ao gravar e ler, **sem expor as chaves** à CPU, ao sistema ou aos aplicativos |
| Inicialização segura | A ROM de inicialização (memória gravada de fábrica, que não pode ser alterada) só permite rodar o sistema da Apple **genuíno e inalterado** |
| Dados biométricos | Processados no hardware de segurança, **separados do sistema e dos aplicativos**, inclusive de malware |
| Encontre meu Mac | Localiza dispositivos perdidos ou roubados e permite **bloqueá-los e apagá-los** remotamente |
| XProtect | Antimalware **por assinatura**, que alerta e oferece remover os arquivos |
| MRT (*Malware Removal Tool*) | Remove infecções quando a Apple atualiza as regras; monitora na reinicialização e no login |
| Gatekeeper | Só permite instalar software **autêntico e assinado** por desenvolvedor autenticado pela Apple |

### 26.8 Proteção Física dos Dispositivos

Para proteger fisicamente os equipamentos:

- usar **travas de cabo**;
- manter as **salas de telecomunicações trancadas**;
- usar **gaiolas de Faraday** em volta dos equipamentos, que **bloqueiam campos eletromagnéticos**.

As **travas de portas** mais comuns usam chave padrão e são fáceis de abrir; um **ferrolho** aumenta a segurança. Toda fechadura de chave fica vulnerável se a chave for perdida, roubada ou copiada. A **fechadura cifrada** abre com botões pressionados em sequência, pode limitar o código de cada usuário a certos dias e horários e **registra quando a porta foi aberta e com qual código**.

A **RFID** (*Radio Frequency Identification* — identificação por radiofrequência) usa ondas de rádio para **identificar e rastrear objetos**. As etiquetas têm um circuito com antena e, por usarem pouquíssima energia, **não precisam de bateria**. Ajudam a automatizar o inventário e a bloquear, desbloquear ou configurar dispositivos sem fio.

## 27. Proteção Antimalware

O malware continua sendo um grande desafio, e cada endpoint é uma possível porta de entrada. A nuvem e as VPNs ampliam ainda mais os limites da rede: um dispositivo que acessa a VPN (ver item 17.7) a partir de uma rede pública pode **injetar malware** na rede da empresa.

### 27.1 Ameaças aos Endpoints

Alguns números mostram o tamanho do problema, segundo as previsões citadas no curso:

- até 2021, uma organização seria vítima de **ransomware a cada 11 segundos** (Cybersecurity Ventures);
- o ransomware custaria à economia global **US$ 6 trilhões por ano** até 2021;
- em 2018, houve **8 milhões** de tentativas de roubar recursos com malware de criptomineração;
- entre 2016 e o início de 2017, o volume de spam cresceu muito, e **8% a 10%** dele era malicioso, com anexos como .zip, .js, .hta, .docm e .wsf;
- os ataques por dispositivo macOS passariam de 4,8 em 2018 para 14,2 em 2020;
- vários tipos de malware **mudam suas características em menos de 24 horas** para escapar da detecção.

### 27.2 Segurança do Perímetro e da LAN

A imprensa costuma noticiar ataques externos: DoS que derruba o acesso público, invasão do servidor web para desfigurar o site e invasão de servidores para roubar dados. O **perímetro** é protegido por um roteador reforçado com VPN, um NGFW (como o ASA), um IPS (ver item 16.4) e um servidor AAA, com ESA e WSA para e-mail e web.

**Importante:** muitos ataques **vêm de dentro da rede**, por isso proteger a LAN interna é quase tão importante quanto o perímetro. Um host interno invadido vira **ponto de partida** para chegar a servidores e dados confidenciais. Há dois elementos a proteger:

- **endpoints**: notebooks, desktops, impressoras, servidores e telefones IP, sujeitos a malware;
- **infraestrutura de rede**: switches, dispositivos sem fio e de telefonia IP, sujeitos a estouro da tabela MAC, falsificação, ataques DHCP, tempestades na LAN, manipulação do **STP** (protocolo que evita laços entre switches) e ataques a VLANs.

### 27.3 Proteção Baseada em Host

O perímetro está sempre se expandindo: as pessoas acessam a rede da empresa por VPN com dispositivos que também usam redes públicas e domésticas pouco protegidas. Esses dispositivos são protegidos por:

- **antivírus/antimalware**: detecta e mitiga vírus e malware; exemplos: Windows Defender, **Cisco AMP (ver item 16.5) for Endpoints**, Norton, McAfee e Trend Micro. Há três formas de detecção:
  - **por assinatura**: reconhece características de **malware conhecido**;
  - **heurística**: reconhece **características gerais** comuns a vários tipos de malware;
  - **por comportamento**: analisa **comportamentos suspeitos**;
- **firewall de host**: só permite conexões **iniciadas pelo próprio host**, e alguns impedem que ele se infecte ou espalhe malware; exemplos: Firewall do Windows Defender, **iptables** e **TCP Wrappers** no Linux;
- **pacotes de segurança de host**: reúnem antivírus, antiphishing, navegação segura, HIPS e firewall, em uma **defesa em camadas**. Recomendados para casas e empresas.

Muitos antivírus dão **proteção em tempo real**, analisando os dados à medida que são usados, e também procuram malware que já entrou antes de ser reconhecível.

| Antivírus | Como funciona |
| --- | --- |
| Baseado em agente | Roda **em cada máquina** protegida |
| Sem agente | Faz as varreduras **a partir de um sistema central**; popular em ambientes virtualizados, onde um agente em cada máquina virtual desperdiçaria recursos; usa um equipamento virtual de segurança, como o **vShield** da VMware |

Esses produtos também têm **telemetria**: registros detalhados, essenciais para as operações de segurança, que alguns enviam a um local central. O laboratório independente **AV-TEST** avalia esses produtos.

### 27.4 Proteção Baseada em Rede

Nas **redes sem fronteiras**, os endpoints contam com elementos de varredura da própria rede, que oferecem **mais camadas** do que um endpoint sozinho e **compartilham informações** entre si. Exemplos:

- **AMP**: proteção de endpoint contra vírus e malware;
- **ESA**: filtra spam e e-mails maliciosos antes que cheguem ao endpoint;
- **WSA**: filtra sites e aplica listas negras, controla o acesso à internet e as políticas de uso aceitável e verifica malware;
- **NAC** (*Network Admission Control* — controle de admissão na rede): só permite que **sistemas autorizados e em conformidade** se conectem.

Essas tecnologias trabalham com NGFW, IPS de nova geração, sensores HIDS nos endpoints, a nuvem AMP, *sandboxing*, a inteligência do Talos e do Threat Grid e integrações de terceiros, dando mais proteção que os pacotes de host sozinhos.

## 28. Prevenção de Intrusão Baseada em Host

Além do antimalware, o host conta com firewalls próprios e com sistemas que detectam e impedem intrusões.

### 28.1 IPS de Host e IPS de Rede

Há dois tipos de IPS:

- **HIPS** (*Host-based IPS*): software instalado no host que monitora o sistema operacional e os processos críticos. Bloqueia comportamentos fora do normal, como alterações não autorizadas no registro (o banco de configurações do Windows, visto no módulo 19), mudanças em diretórios do sistema, instalação de programas e estouros de buffer, e impede o host de participar de um DoS ou de uma sessão FTP ilícita. Funciona como **antivírus, antimalware e firewall juntos**;
- **IPS de rede**: equipamento dedicado ou não, com **sensores em pontos definidos da rede**, que detectam e reagem em tempo real, onde quer que esteja o alvo. É **componente essencial** da prevenção de intrusão; o HIPS deve ser integrado a ele.

| HIPS |  |
| --- | --- |
| Vantagens | Proteção específica para o sistema do host; protege aplicativos e sistema; **protege depois que a mensagem é descriptografada** |
| Desvantagens | Depende do sistema operacional; **precisa ser instalado em todos os hosts**; só tem visão local, sem enxergar eventos coordenados na rede |

### 28.2 Firewalls de Host

Os **firewalls pessoais de host** são programas que **controlam o tráfego que entra e sai do computador**; também existem para celulares e tablets Android. Eles usam **perfis** (conjuntos de políticas predefinidas) ou regras por endereço, protocolo e porta, e podem **alertar o usuário** sobre comportamento suspeito, perguntando se o aplicativo pode rodar.

Os **logs** costumam trazer a data e a hora, se a conexão foi permitida ou negada, os IPs e as portas de origem e de destino. Como eventos rotineiros, como as consultas DNS, também aparecem, são necessárias **filtragem e outras técnicas de análise**.

Os **firewalls distribuídos** combinam o firewall de host com **gerenciamento centralizado**, que envia as regras aos hosts e recebe seus logs. Instalados no host ou distribuídos, são uma camada importante, junto com os firewalls de rede. Exemplos:

| Firewall | Características |
| --- | --- |
| Firewall do Windows Defender | Incluído desde o Windows XP; usa **perfis**: **Público** (o mais restritivo, para redes públicas), **Privado** (computadores protegidos por outro dispositivo, como um roteador doméstico com firewall) e **Domínio** (rede confiável de empresa); tem logs e gestão central por políticas de grupo, como no System Center 2012 Configuration Manager |
| iptables | Configura regras de acesso que fazem parte dos módulos **Netfilter** do kernel Linux |
| nftables | Sucessor do iptables; usa uma **máquina virtual simples no kernel** que inspeciona os pacotes e aplica as regras |
| TCP Wrappers | Controle de acesso e registro por regras no Linux, filtrando por IP e serviço de rede |

### 28.3 Detecção de Intrusão Baseada em Host

A diferença entre detecção e prevenção no host é pouco nítida, e algumas fontes falam em **HIPDS**; o setor prefere a sigla **HIDS**. Um **HIDS** protege o host contra **malware conhecido e desconhecido** e oferece:

- monitoramento detalhado da configuração e da atividade dos aplicativos;
- análise de logs e **correlação de eventos**;
- **verificação de integridade**;
- aplicação de políticas;
- **detecção de rootkits**;
- alertas.

O HIDS **combina antimalware e firewall**: além de detectar o malware, **impede que ele rode**. Como roda no próprio host, é um sistema **baseado em agente**, em geral com um **servidor de gerenciamento** central que recebe os logs e alertas para a equipe de segurança.

### 28.4 Funcionamento do HIDS

O HIDS usa estratégias **proativas e reativas**. Contra ameaças conhecidas, usa **assinaturas**, que não funcionam contra ameaças novas ou de dia zero nem contra o **malware polimórfico**, cujas variações mudam a assinatura o suficiente para escapar. Por isso, há mais duas estratégias:

- **baseada em anomalias**: compara o comportamento do host com uma **linha de base** aprendida do comportamento normal; desvios significativos indicam intrusão, e o HIDS registra, alerta e age. Como muitas coisas além do malware mudam o comportamento, pode gerar **muitos falsos alarmes**, o que sobrecarrega a equipe e reduz a credibilidade do sistema;
- **baseada em política**: o comportamento normal é descrito por **regras predefinidas**; ao detectar uma violação, o HIDS pode encerrar o processo, registrar e alertar. A maioria vem com regras prontas, e alguns aceitam políticas personalizadas distribuídas por um sistema central.

| Estratégia | Detecta | Limitação |
| --- | --- | --- |
| Assinaturas | Malware conhecido | Não detecta dia zero nem malware polimórfico |
| Anomalias | Desvios da linha de base | Muitos falsos alarmes |
| Política | Violações de regras | Depende de regras bem definidas |

### 28.5 Produtos HIDS

A maioria dos produtos combina software no host com **gerenciamento centralizado**, integrado ao monitoramento da rede e à inteligência de ameaças. Exemplos: **Cisco AMP**, **AlienVault USM**, **Tripwire** e **OSSEC**.

O **OSSEC** (*Open Source HIDS Security*) usa um **servidor gerenciador central** e **agentes** para Mac, Windows, Linux e Solaris. O gerenciador também recebe alertas de dispositivos de rede e firewalls por **syslog** (ver item 17.5). O OSSEC monitora os logs dos hosts, **verifica a integridade dos arquivos**, detecta rootkits e outros malwares e pode executar scripts ou aplicativos em resposta a eventos.

## 29. Segurança de Aplicações

Mesmo com proteção no host e no perímetro, o malware entra. Por isso, também é preciso reduzir o que pode ser atacado e analisar com segurança o que parece suspeito.

### 29.1 Superfície de Ataque

A **superfície de ataque** é a **soma das vulnerabilidades de um sistema acessíveis ao atacante**: portas abertas, software em servidores voltados para a internet, protocolos sem fio e até os usuários. Ela não para de crescer, com a **IoT**, o **BYOD** (*Bring Your Own Device*, o uso de dispositivos pessoais no trabalho), a nuvem e a mobilidade. As previsões citadas no curso eram:

- **IoT**: 30 bilhões de dispositivos conectados até 2020;
- **nuvem**: 92% das cargas de trabalho dos data centers processadas na nuvem até 2020;
- **BYOD**: 70% dos profissionais trabalhando em dispositivos próprios até 2018;
- **tráfego global**: quase o triplo em cinco anos;
- **mobilidade**: 20% do tráfego IP vindo de dispositivos móveis até 2021.

O **Instituto SANS** descreve **três componentes** da superfície de ataque:

| Superfície | O que o ataque explora |
| --- | --- |
| De rede | Vulnerabilidades das redes: protocolos com e sem fio, inclusive de smartphones e IoT, e as camadas de rede e transporte |
| De software | Vulnerabilidades de aplicativos web, na nuvem ou no host |
| Humana | **O comportamento do usuário**: engenharia social, ações maliciosas de pessoas de confiança e erros |

### 29.2 Listas de Bloqueio e de Permissão

Uma forma de **reduzir a superfície de ataque** é limitar o que pode rodar:

- **lista de bloqueio** (*blocklist* ou lista negra): diz **quais aplicativos não podem rodar**;
- **lista de permissão** (*allowlist* ou lista branca): diz **quais programas podem rodar**; só eles são permitidos.

As listas de permissão seguem a **linha de base de segurança** da organização, que define o **risco aceito** e os componentes que contribuem para ele; um software fora da lista pode violar essa linha de base. No Windows, as listas são configuradas no **Editor de Política de Grupo Local**, com as opções "não executar os aplicativos especificados" e "executar somente os aplicativos especificados".

Os **sites** também podem entrar nessas listas, criadas à mão ou obtidas de serviços de segurança que as atualizam e distribuem a firewalls e outros sistemas. Exemplos: o **Cisco Firepower** usa as listas do **Talos**, e o **Spamhaus Project** oferece uma lista negra gratuita.

### 29.3 Sandboxing

O **sandboxing** (caixa de areia) permite **executar e analisar arquivos suspeitos em um ambiente seguro**. As sandboxes automáticas observam os efeitos do malware desconhecido para descobrir seu comportamento e criar defesas.

O malware polimórfico e o novo malware **entram na rede apesar das melhores defesas**. O HIDS (ver item 28.3) e outros sistemas alertam sobre um possível malware; então:

1. o **Cisco AMP** rastreia a **trajetória do arquivo** na rede e "volta no tempo" para obter uma cópia;
2. o arquivo é executado em uma sandbox, como o **Cisco Threat Grid Glovebox**, que documenta suas atividades;
3. as informações geram **assinaturas** que impedem o arquivo de entrar de novo e **regras de detecção** que identificam outros sistemas infectados.

Há sandboxes gratuitas e on-line:

- **Cuckoo Sandbox**: gratuita e popular, roda localmente;
- **VirusTotal**, **Joe Sandbox** e **CrowdStrike Falcon Sandbox**: serviços on-line que recebem amostras;
- **ANY.RUN**: sandbox on-line com **relatórios interativos**, capturas de tela, atividade de rede (pedidos HTTP e consultas DNS), arquivos executados e classificados, hashes, conteúdo em hexadecimal e ASCII, alterações no sistema e **IOCs**. As táticas do malware são mapeadas na matriz **MITRE ATT&CK**.

## 30. Contramedidas, Conscientização e Políticas

A terceira dimensão do cubo da segurança cibernética define os **pilares da defesa**: **tecnologia**, **políticas e práticas** e **pessoas**. Depois de conhecer as ameaças e as ferramentas, este é o fechamento: como esses três pilares se combinam.

### 30.1 Tecnologias de Software

As proteções de tecnologia incluem programas e serviços que protegem sistemas operacionais, bancos de dados e outros serviços em estações, dispositivos portáteis e servidores. Os administradores instalam em cada host ou servidor:

| Tecnologia | Função |
| --- | --- |
| Firewalls de software | Controlam o acesso remoto ao sistema; vêm com o sistema operacional ou são instalados à parte |
| Scanners de rede e de portas | Descobrem e monitoram as **portas abertas** em um host ou servidor |
| Analisadores de protocolo | Também chamados de analisadores de assinatura; coletam e examinam o tráfego para achar problemas de desempenho, configurações erradas e aplicativos com mau comportamento, criar a **linha de base** do tráfego normal e depurar a comunicação |
| Scanners de vulnerabilidade | Avaliam **pontos fracos** de computadores ou redes |
| IDS de host | Examinam a atividade **só no host** e geram logs e alarmes; indicados para sistemas com dados confidenciais ou serviços essenciais |

### 30.2 Tecnologias de Hardware

As principais tecnologias de hardware são:

| Tecnologia | Função |
| --- | --- |
| Firewalls | Bloqueiam o tráfego indesejado com regras que definem o que pode entrar e sair |
| Servidores proxy | Apresentam à internet **um único IP para toda a empresa** e fazem os pedidos em nome do cliente, **ocultando a origem real** |
| Controle de acesso por hardware | Dispositivos **biométricos**, como leitores de digital ou de íris, que confirmam a identidade de quem acessa servidores, dados e sistemas |
| Switches | Ponto de conexão dos dispositivos da LAN, com recursos que aumentam a segurança da rede |

### 30.3 Cultura de Conscientização

Gastar muito em tecnologia não adianta se **as pessoas forem o elo mais fraco**. Um funcionário pode não ter má intenção e apenas desconhecer os procedimentos corretos. Por isso, são essenciais um **programa de conscientização** e **políticas sólidas**. Formas de treinar:

- incluir o treinamento de segurança na **integração** do funcionário;
- ligar a conscientização aos **requisitos do cargo** ou às **avaliações de desempenho**;
- fazer sessões presenciais com **gamificação** e atividades, como desafios de capturar a bandeira;
- oferecer cursos e módulos on-line.

Um programa ativo depende do **ambiente da empresa**, do **nível de ameaça** e da **natureza dos dados** que ela mantém. As pessoas são **a primeira linha de defesa**, e cada membro precisa conhecer e aplicar as políticas.

**Importante:** a conscientização **não é feita uma vez só**: é um **processo contínuo**, porque novas ameaças surgem sempre, e exige liderança constante da gerência e o compromisso de todos.

### 30.4 Políticas de Segurança

Uma **política de segurança** **define os objetivos de segurança, as regras de comportamento e os requisitos dos sistemas**. Ela informa usuários, funcionários e gerentes sobre os requisitos para proteger os ativos e especifica os mecanismos para cumpri-los. Uma política abrangente:

- demonstra o **compromisso** da empresa com a segurança;
- define as **regras de comportamento** esperado;
- garante **consistência** nas operações e na aquisição, uso e manutenção de software e hardware;
- define as **consequências jurídicas** das violações;
- dá à equipe de segurança o **apoio da gerência**.

Uma política costuma incluir:

| Política | O que define |
| --- | --- |
| Identificação e autenticação | Quem pode acessar os recursos e como esses usuários são verificados |
| Senhas | Requisitos mínimos e troca regular |
| Uso aceitável | Os recursos e usos permitidos e as consequências das violações |
| Acesso remoto | Como os usuários remotos acessam a rede e o que podem acessar |
| Manutenção de rede | Os sistemas dos dispositivos de rede e os procedimentos de atualização dos aplicativos |
| Tratamento de incidentes | Como os incidentes de segurança são tratados |

A **AUP** (*Acceptable Use Policy* — política de uso aceitável) é uma das mais comuns: define **o que os usuários podem ou não fazer** nos sistemas. Deve ser **o mais explícita possível**, listando, por exemplo, sites, grupos de notícias ou aplicativos que consomem muita banda e não podem ser acessados nos computadores ou na rede da empresa.

### 30.5 Padrões, Diretrizes e Procedimentos

A política se desdobra em três tipos de documentos:

- **padrões**: garantem a **consistência**, um dos princípios mais importantes da segurança, e ajudam a TI a ter eficiência e simplicidade no projeto, na manutenção e na solução de problemas. Cada empresa cria os seus. Exemplo de padrão de senha: **no mínimo oito caracteres** alfanuméricos, com maiúsculas, minúsculas e **pelo menos um caractere especial**, troca a **cada 30 dias** e um **histórico das 12 últimas senhas** para impedir a reutilização por 12 meses;
- **diretrizes**: **sugestões** para fazer as coisas de forma mais eficiente e segura; parecidas com os padrões, mas **mais flexíveis e em geral não obrigatórias**. Definem como os padrões são desenvolvidos e reúnem as **melhores práticas**. Também há diretrizes do **NIST** (*National Institute of Standards and Technology*, pelo seu Centro de Recursos de Segurança de Computadores), da **NSA** (*National Security Agency*, com seus guias de configuração) e do padrão **Common Criteria**. Exemplo: transformar uma frase fácil de lembrar, como "Eu tenho um sonho" (*I have a dream*), em uma senha forte, trocando letras por caracteres: **Ihv@dr3@m**; outras senhas saem da mesma frase mudando o número, o símbolo ou a pontuação;
- **procedimentos**: documentos **mais longos e detalhados** que os padrões e as diretrizes, com **instruções passo a passo** e figuras. Grandes empresas os usam para manter a consistência necessária a um ambiente seguro. Exemplo de procedimento para trocar a senha no Windows:
  1. pressionar Ctrl+Alt+Del para abrir a tela de login;
  2. clicar em "Alterar senha";
  3. digitar a senha atual;
  4. digitar a nova senha;
  5. digitar a nova senha de novo para confirmar.

| Documento | Natureza | Exemplo |
| --- | --- | --- |
| Política | Objetivos e regras gerais | Toda conta deve ter senha |
| Padrão | Requisito obrigatório e consistente | Mínimo de oito caracteres, troca a cada 30 dias |
| Diretriz | Sugestão flexível | Criar a senha a partir de uma frase |
| Procedimento | Passo a passo detalhado | Como trocar a senha no Windows |

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
