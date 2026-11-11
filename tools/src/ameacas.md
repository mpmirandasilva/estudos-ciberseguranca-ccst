# Gerenciamento de Ameaças Cibernéticas

Nov 6, 2026 · @Maria Paula

## 1. Governança da Segurança Cibernética

A **governança** descreve **as políticas e os processos que definem as responsabilidades e a prestação de contas** para reduzir os riscos digitais.

### 1.1 Governança e Gerenciamento

A **governança da segurança de TI** **determina quem está autorizado a tomar decisões sobre os riscos digitais** e garante que a segurança esteja **alinhada aos objetivos do negócio**.

**Importante:** a governança **decide**; o **gerenciamento** de segurança **define e implementa os controles**.

A **governança de dados** define quem decide sobre os dados:

| Função | Responsabilidade |
| --- | --- |
| Proprietário dos dados | **Atribui a classificação** e define os critérios de acesso |
| Controlador dos dados | Define **para que e como** os dados pessoais são tratados |
| Processador (operador) | Trata dados pessoais **em nome do controlador** |
| Custodiante dos dados | **Implementa os controles** definidos pelo proprietário |
| Administrador dos dados (*data steward*) | Garante que os dados atendam ao negócio e às normas |
| Encarregado (*DPO*, *Data Protection Officer*) | **Supervisiona a estratégia de proteção de dados** |

Exemplo: o diretor financeiro é o **proprietário** dos dados de salários e decide quem pode vê-los; a equipe de TI, que configura as permissões e faz os backups, é a **custodiante**.

### 1.2 Políticas de Segurança Cibernética

Uma **política de segurança cibernética** é um **documento de alto nível com a visão da empresa sobre segurança**: metas, escopo e responsabilidades. Ela:

- demonstra o compromisso da organização;
- define padrões de comportamento;
- garante consistência;
- define as **consequências legais** das violações;
- dá à segurança o **apoio da alta gerência**.

| Tipo | O que é | Exemplo |
| --- | --- | --- |
| Política mestra | **Plano estratégico** do programa de segurança | Política de Segurança Cibernética |
| Específica do sistema | Para **dispositivos ou sistemas** específicos | Política do firewall |
| Específica do problema | Instruções detalhadas para **situações operacionais** | Uso aceitável de e-mail |

### 1.3 Tipos de Políticas de Segurança

As políticas precisam ser **claras, conhecidas por todos e apoiadas pela alta gerência**.

| Política | O que define |
| --- | --- |
| Identificação e autenticação | Quem acessa e como é verificado |
| Senhas | Requisitos e frequência de troca |
| Uso aceitável (**AUP**) | Uso dos recursos e consequências |
| Acesso remoto | Conexão remota à rede interna |
| Manutenção de rede | Atualização de sistemas e aplicativos |
| Tratamento de incidentes | Como **relatar e responder** a incidentes |
| Dados | Onde são guardados, como são **classificados**, tratados e descartados |
| Credenciais | Composição das senhas |
| Organizacional | Gerenciamento de **mudanças** e de ativos |

**Observação:** o profissional de segurança tem as mesmas habilidades de um criminoso; o que os diferencia é **a ética**.

## 2. Ética, Crime Cibernético e Leis

O profissional de segurança precisa agir guiado pela ética e pelo conhecimento da lei.

### 2.1 Perspectivas Éticas

| Perspectiva | Princípio |
| --- | --- |
| Utilitarista | É ética a ação que traz **o maior bem para o maior número de pessoas** |
| Abordagem dos direitos | Cada pessoa **tem o direito de fazer as próprias escolhas** |
| Abordagem do bem comum | Ações que **beneficiam toda a comunidade** |

### 2.2 Os Dez Mandamentos da Ética em Informática

O **CEI** (*Computer Ethics Institute*) criou os **dez mandamentos da ética em informática**:

1. não usar o computador para prejudicar outras pessoas;
2. não interferir no trabalho dos outros;
3. não bisbilhotar os arquivos dos outros;
4. não usar o computador para roubar;
5. não usar o computador para dar falso testemunho;
6. não copiar software proprietário sem pagar;
7. não usar recursos de outros sem autorização;
8. não se apropriar da produção intelectual alheia;
9. pensar nas consequências sociais do que se cria;
10. usar o computador com consideração e respeito.

Exemplo: entrar com as credenciais de um colega é **antiético**.

### 2.3 Crime Cibernético

O **crime cibernético** tem **três categorias**:

- **contra o computador**: o computador é **o alvo** (malware, invasão, DoS);
- **assistido por computador**: o computador é **usado para cometer o crime** (fraude);
- **incidental ao computador**: o computador **guarda informações** de um crime.

Nos EUA, combatem esse crime o **IC3** (centro de denúncias do FBI), a **InfraGard** e a **SIIA** (contra a pirataria).

### 2.4 Fontes das Leis Cibernéticas

Nos EUA, há **três fontes** de leis:

| Fonte | O que é |
| --- | --- |
| Lei estatutária | Leis do Congresso, com penalidades civis e criminais |
| Direito administrativo | Rege as **agências do governo**, como FCC e FTC |
| Direito comum | Decisões judiciais que criam **precedentes** |

### 2.5 FISMA e Leis Setoriais

A **FISMA** (*Federal Information Security Management Act*, 2002) exige das **agências federais dos EUA** um programa de segurança, com avaliação de riscos, inventário, treinamento, testes, resposta a incidentes e continuidade.

| Setor | Lei ou norma | O que exige |
| --- | --- | --- |
| Finanças | **GLBA** (*Gramm-Leach-Bliley Act*) | Restringe o compartilhamento de dados financeiros com terceiros |
| Contabilidade | **SOX** (*Sarbanes-Oxley*) | Padrões financeiros das **empresas de capital aberto** |
| Cartões | **PCI DSS** (*Payment Card Industry Data Security Standard*) | **Proteger os dados do portador do cartão** |
| Criptografia | Regras do Departamento de Comércio | Controle de importação e exportação |

### 2.6 Notificação de Violações e Acesso Indevido

Várias leis exigem **avisar as pessoas quando seus dados são violados**.

- **ECPA** (*Electronic Communications Privacy Act*): protege as **comunicações eletrônicas** contra interceptação;
- **CFAA** (*Computer Fraud and Abuse Act*, 1986): **proíbe o acesso não autorizado** a sistemas.

### 2.7 Proteção da Privacidade

| Lei | O que protege |
| --- | --- |
| Privacy Act (1974) | Dados pessoais em registros federais |
| **FOIA** (*Freedom of Information Act*) | **Acesso público aos registros do governo**, com nove isenções |
| **FERPA** | Registros **escolares** |
| **COPPA** | Privacidade de **crianças menores de 13 anos** |
| **CIPA** | Menores de 17 anos contra conteúdo ofensivo |
| **VPPA** | Histórico de aluguel de vídeos |
| **HIPAA** | **Informações de saúde** |
| California SB 1386 | Primeira lei estadual de **aviso de violação** |

A **PIA** (*Privacy Impact Assessment*) garante que as **informações de identificação pessoal** (**PII**) sejam bem tratadas.

**Observação:** no Brasil, vale a **LGPD** (Lei Geral de Proteção de Dados, Lei 13.709/2018).

### 2.8 Leis Internacionais

As leis variam entre os países, o que **dificulta punir crimes que cruzam fronteiras**.

- a **Convenção de Budapeste** é o **primeiro tratado internacional** sobre crimes na internet;
- o **EPIC** (*Electronic Privacy Information Center*) promove a privacidade.

## 3. Estruturas de Gerenciamento de Segurança

As **estruturas** (*frameworks*) organizam **como** a empresa protege seus ativos, com domínios, objetivos e controles reconhecidos.

### 3.1 ISO/IEC 27000 e o ISMS

A **ISO/IEC 27000** é uma **série de padrões e boas práticas de segurança da informação** que estabelece os requisitos de um **ISMS** (*Information Security Management System*).

O **ISMS** é o conjunto de **todos os controles administrativos, técnicos e operacionais** que mantêm a informação segura.

### 3.2 Os Doze Domínios

O padrão tem **doze domínios**:

| Domínio | O que trata |
| --- | --- |
| Avaliação de risco | Valor quantitativo e qualitativo do risco |
| Política de segurança | Quem pode acessar quais dados |
| Organização da segurança | Modelo de governança |
| Gerenciamento de ativos | Inventário e classificação |
| Recursos humanos | Admissão, transferência e demissão |
| Segurança física e ambiental | Instalações |
| Operações e comunicações | Controles técnicos |
| Aquisição e desenvolvimento | Segurança integrada aos sistemas |
| Controle de acesso | Restrição de acesso |
| Gerenciamento de incidentes | Resposta a violações |
| Continuidade de negócios | Recuperar atividades essenciais |
| Conformidade | Cumprir normas e leis |

**Importante:** o modelo OSI usa **camadas**; o ISO usa **domínios** e é **não hierárquico**.

### 3.3 Objetivos de Controle e Controles

- **objetivos de controle** (**ISO 27001**): **requisitos de alto nível**, usados como **lista de verificação na auditoria**;
- **controles** (**ISO 27002**): **como atingir os objetivos**.

Exemplo: o objetivo "controlar o acesso às redes" é atingido pelo controle "usar senhas fortes".

**Observação:** os controles são **diretrizes, não obrigações**, e devem ser **neutros** (sem indicar produtos).

### 3.4 Aplicação da ISO 27000

A empresa escolhe os controles aplicáveis em uma **SOA** (*Statement of Applicability* — **declaração de aplicabilidade**), conforme suas prioridades na tríade CIA. Exemplo: na Amazon, a **disponibilidade** pesa mais.

Cada estado dos dados costuma ficar a cargo de uma equipe diferente:

| Estado dos dados | Responsável típico |
| --- | --- |
| Em trânsito | Equipe de segurança de rede |
| Em processamento | Programadores e analistas |
| Em repouso | Suporte de hardware |

**Importante:** a alta gerência **define a política**; os profissionais de TI **a implementam**.

### 3.5 Estrutura da Força de Trabalho do NIST

O **NIST** criou a **National Cybersecurity Workforce Framework**, com **sete categorias** de trabalho em segurança:

| Categoria | O que faz |
| --- | --- |
| Operar e manter | Suporte e administração dos sistemas |
| Proteger e defender | **Identifica, analisa e mitiga ameaças** |
| Investigar | Investiga eventos e ataques |
| Coletar e operar | Operações especializadas e coleta de informações |
| Analisar | Avalia informações para a inteligência |
| Supervisionar e governar | **Liderança** e direção |
| Provisionar com segurança | **Projeta e cria** sistemas seguros |

### 3.6 Controles do CIS

O **CIS** (*Center for Internet Security*) criou **controles essenciais** por nível de recursos:

- **básicos**: inventário de hardware e software, gestão de vulnerabilidades, privilégios administrativos controlados, configurações seguras e logs de auditoria;
- **fundamentais**: e-mail e navegador, malware, portas e serviços, recuperação, perímetro, proteção de dados e acesso sem fio;
- **organizacionais**: conscientização, segurança de software, resposta a incidentes e **testes de penetração**.

Os **CIS Benchmarks** são **guias de configuração segura** para várias plataformas.

### 3.7 Matriz de Controles de Nuvem

A **CCM** (*Cloud Controls Matrix*), da **CSA** (*Cloud Security Alliance*), **mapeia os controles da nuvem para os principais padrões e regulamentações**. É o **padrão de fato** da segurança na nuvem.

### 3.8 Conformidade e Certificações

- **SOC 2** (*Service Organization Control*): **auditoria independente** dos controles de um provedor; **Tipo I**: controles existem em um momento; **Tipo II**: funcionam por pelo menos seis meses;
- **CMMC** (*Cybersecurity Maturity Model Certification*): certificação de **fornecedores da defesa dos EUA**, com cinco níveis.

| Estrutura | Criada por | Para que serve |
| --- | --- | --- |
| ISO 27001/27002 | ISO e IEC | Controles de um ISMS |
| Workforce Framework | NIST | Funções dos profissionais |
| Controles do CIS | CIS | Controles essenciais |
| CCM | CSA | Controles da nuvem |
| SOC 2 | AICPA (norma SSAE 18) | Auditoria de provedores |
| CMMC | DoD | Fornecedores da defesa dos EUA |

## 4. Gerenciamento de Riscos

O **gerenciamento de riscos** **identifica os riscos e as vulnerabilidades que ameaçam a empresa** e aplica soluções para protegê-la.

### 4.1 Risco, Impacto e Níveis de Cuidado

- **risco**: a **probabilidade de perda causada por uma ameaça**;
- **impacto**: o **dano causado** pelo evento.

O objetivo é **reduzir as ameaças a um nível aceitável**.

| Atitude | O que significa | Risco |
| --- | --- | --- |
| Negligência | **Nenhuma ação** | Alto |
| Devido cuidado (*due care*) | Etapas razoáveis que **reduzem** a perda | Menor |
| Devida diligência (*due diligence*) | Medidas para **eliminar** o risco, com vários controles | Aceitável |

### 4.2 O Processo de Gerenciamento de Riscos

É um processo formal que **mede o impacto de uma ameaça e o custo dos controles**.

**Importante:** **o risco não pode ser eliminado por completo**, só gerenciado. O custo da contramedida **não deve ser maior que o valor do ativo**.

Identificar → Avaliar → Responder → Monitorar

1. **identificar**: levantar as ameaças em toda a empresa;
2. **avaliar**: analisar a gravidade, pelo **impacto financeiro** (quantitativa) ou por uma **escala** (qualitativa);
3. **responder**: **mitigar, transferir ou aceitar**;
4. **monitorar**: revisar continuamente; os riscos aceitos precisam de acompanhamento de perto.

![O gerenciamento de riscos é um ciclo: identificar, avaliar, responder e monitorar, sem parar](img/ameacas/gt_risco.png){width=6in}

O **registro de riscos** (*risk register*) guarda os detalhes de cada risco e a resposta adotada.

### 4.3 Fontes de Ameaça

A **avaliação de ameaças** é a **base da avaliação de riscos**. O **vetor de ameaça** é o **caminho que o atacante usa**.

Fontes de ameaça:

- **adversarial**: indivíduos, grupos, organizações ou nações;
- **acidental**: **sem intenção maliciosa**;
- **estrutural**: **falhas de equipamento e de software**;
- **ambiental**: desastres naturais ou causados pelo homem.

### 4.4 Metodologia de Avaliação de Riscos

A avaliação combina três estimativas:

- **probabilidade de ataque**: habilidade, motivação, oportunidade e tamanho do grupo;
- **vulnerabilidade**: facilidade de descoberta e de exploração e capacidade de detecção;
- **magnitude do impacto**: de insignificante a catastrófico.

Quanto maiores a probabilidade e o impacto, maior o risco.

### 4.5 Análise de Riscos

A **análise de riscos** examina os **perigos para os ativos**. Objetivos:

1. identificar os ativos e seu valor;
2. identificar vulnerabilidades e ameaças;
3. quantificar probabilidade e impacto;
4. **equilibrar o impacto da ameaça com o custo da contramedida**.

#### 4.5.1 Análise Quantitativa

A **análise quantitativa** **atribui números** ao processo:

| Valor | Significado |
| --- | --- |
| AV (*Asset Value*) | **Valor do ativo** |
| EF (*Exposure Factor*) | **Porcentagem do valor perdida** (perda total = 1,0) |
| SLE (*Single Loss Expectancy*) | Perda em **uma ocorrência** |
| ARO (*Annualized Rate of Occurrence*) | Ocorrências esperadas **por ano** |
| ALE (*Annual Loss Expectancy*) | **Perda esperada por ano** |

**SLE = AV × EF**

**ALE = SLE × ARO**

#### 4.5.2 Exemplo Resolvido: Falha de um Servidor de Arquivos

Um servidor de US$ 15.000 é perdido por completo se falhar, o que ocorre em 15% dos anos.

| Etapa | Cálculo | Resultado |
| --- | --- | --- |
| SLE | US$ 15.000 × 1,0 | US$ 15.000 |
| ALE | US$ 15.000 × 0,15 | **US$ 2.250** |

Não faz sentido gastar mais de US$ 2.250 por ano para proteger esse servidor.

#### 4.5.3 Análise Qualitativa

A **análise qualitativa** usa **opiniões e cenários** que cruzam **probabilidade** e **impacto**.

A **matriz de riscos** **prioriza os riscos**; colorida do verde ao vermelho, é o **mapa de calor** (*heat map*).

| Característica | Quantitativa | Qualitativa |
| --- | --- | --- |
| Base | Números e valores financeiros | Opiniões e cenários |
| Resultado | ALE em dinheiro | Posição na matriz |
| Ferramenta | Fórmulas SLE e ALE | Matriz ou mapa de calor |

### 4.6 Respostas ao Risco

A **mitigação** reduz a **gravidade ou a probabilidade** da perda.

| Estratégia | O que faz | Exemplo |
| --- | --- | --- |
| Aceitar | **Assume o risco** e o reavalia | Riscos do dia a dia |
| Reduzir | **Implementa controles** | Atualizações e patches regulares |
| Evitar | **Elimina a atividade arriscada** | Deixar de oferecer um serviço vulnerável |
| Transferir | **Passa o risco a terceiros** | Seguro ou terceirização |

Um bom plano pode **combinar duas ou mais estratégias**.

### 4.7 Priorização dos Ativos

A empresa ordena os riscos **da maior para a menor prioridade**, em geral pela **perda anual esperada** (ALE).

### 4.8 Avaliação de Riscos Segundo o NIST

O **NIST** descreve o gerenciamento de riscos como **contínuo e cíclico**:

Identificação → Avaliação → Planejamento da resposta → Implementação → Monitoramento

O **NIST SP 800-30** define a avaliação de riscos como **identificar, estimar e priorizar os riscos**.

Os **pares T-V** (*threat-vulnerability*) associam cada ameaça à vulnerabilidade que ela explora e formam o **perfil de risco inerente** (antes dos controles).

| Resposta (NIST) | Equivale a | Exemplo |
| --- | --- | --- |
| Prevenção (*avoidance*) | Evitar | Descontinuar um serviço |
| Redução | Reduzir | Corrigir os servidores |
| Compartilhamento | Transferir parte do risco | Seguro; contratar um **CSIRT** (equipe de resposta a incidentes) como serviço |
| Retenção | Aceitar | Riscos de baixo impacto e mitigação cara |

## 5. Controles de Segurança

Os **controles de segurança** são **proteções que evitam, detectam, neutralizam ou minimizam os riscos**. Sem eles, resta o **risco inerente**: o risco do sistema **sem controles**.

### 5.1 Tipos de Controle

- **administrativos**: **procedimentos e políticas**; determinam **como as pessoas agem**;
- **técnicos**: **hardware e software**;
- **físicos**: **cercas e fechaduras**, que **separam fisicamente** as ameaças.

### 5.2 Controles por Função

| Função | O que faz | Exemplos |
| --- | --- | --- |
| Preventiva | **Impede atividades indesejadas** | Firewall bloqueando uma porta |
| Dissuasiva | **Desencoraja**, mas **não impede** | Câmeras e avisos |
| De detecção | **Descobre a violação depois** | IDS, detector de movimento |
| Corretiva | **Restaura o sistema** depois da ameaça | Antivírus, políticas |
| De recuperação | **Restaura recursos depois de uma violação** | **Backup e restauração**, clusters |
| Compensatória | **Reforça ou substitui** um controle que não pode ser usado | Monitoramento, supervisão |

Exemplo de controle compensatório: sem cão de guarda, um **detector de movimento com som de latidos**.

**Importante:** a dissuasão **desencoraja**, a prevenção **impede**, a detecção **descobre depois**, e a correção e a recuperação **consertam**.

### 5.3 Auditoria e Conformidade dos Controles

O **CIS** mapeou seus **18 controles essenciais** para estruturas como **PCI DSS, NIST, FISMA, HIPAA, GDPR** (regulamento de proteção de dados da União Europeia) e **ISO 27001**. A ferramenta **CIS-CAT Pro** **avalia a conformidade**.

## 6. Inteligência de Ameaças

A **inteligência de ameaças** é o **conhecimento atualizado sobre atacantes, vulnerabilidades e técnicas**.

### 6.1 Comunidades de Inteligência

| Organização | O que oferece |
| --- | --- |
| **SANS** | Recursos gratuitos: **Internet Storm Center** (alerta antecipado), boletins e cursos |
| **MITRE** | Mantém a lista **CVE** |
| **FIRST** (*Forum of Incident Response and Security Teams*) | Reúne **equipes de resposta a incidentes** |
| **(ISC)²** | Certificações e carreira |
| **CIS** | **MS-ISAC**, alertas 24 horas para governos locais dos EUA |

O profissional precisa **manter-se informado sobre as ameaças mais recentes** e atualizar suas habilidades continuamente.

### 6.2 Relatórios, Blogs e Podcasts

Relatórios como o **Cisco Annual Cybersecurity Report** mostram **como os atacantes estão mirando as redes**. O **Cisco Talos** mantém blogs e podcasts.

### 6.3 Serviços de Inteligência de Ameaças

Os **serviços de inteligência de ameaças** **trocam informações sobre ameaças**, como vulnerabilidades e **IOCs** (*Indicators of Compromise*). Eles **distribuem regras de firewall e IOCs** aos dispositivos assinantes.

- **Cisco Talos**: uma das **maiores equipes comerciais** de inteligência de ameaças; mantém as regras do **Snort**, do **ClamAV** e do **SpamCop**;
- **FireEye**: plataforma **Helix**, com SIEM e SOAR, e detecção **sem assinaturas** de ameaças de dia zero;
- **AIS** (*Automated Indicator Sharing*): **serviço gratuito do governo dos EUA** que troca indicadores **em tempo real**.

### 6.4 Banco de Dados CVE

O **CVE** (*Common Vulnerabilities and Exposures*), mantido pela **MITRE**, é um **dicionário de identificadores para as vulnerabilidades publicamente conhecidas**. Com um identificador único, todos falam da mesma vulnerabilidade.

### 6.5 Padrões de Compartilhamento

Para trocar **CTI** (*Cyber Threat Intelligence*) de forma automatizada:

| Padrão | O que é |
| --- | --- |
| **STIX** (*Structured Threat Information Expression*) | **Formato para descrever** informações sobre ameaças |
| **TAXII** (*Trusted Automated Exchange of Indicator Information*) | **Protocolo que transporta a CTI** sobre HTTPS |
| **CybOX** (*Cyber Observable Expression*) | Descreve eventos observáveis da rede |

**Importante:** o STIX é **o formato**; o TAXII é **o transporte**.

O **MISP** (*Malware Information Sharing Platform*) é uma **plataforma aberta para compartilhar IOCs**.

### 6.6 Plataformas de Inteligência de Ameaças

A **TIP** (*Threat Intelligence Platform*) **centraliza dados de ameaças de várias fontes** e os torna utilizáveis. Tipos de dados:

- **IOCs**;
- **TTPs** (*Tactics, Techniques and Procedures*): **como os atacantes agem**;
- informações de **reputação** de domínios.

Os **honeypots** são **redes ou servidores simulados para atrair atacantes**; hospedá-los **na nuvem os isola** da produção.

| Fonte | Tipo | Destaque |
| --- | --- | --- |
| Cisco Talos | Comercial | Regras do Snort, ClamAV e SpamCop |
| FireEye Helix | Comercial | SIEM e SOAR na nuvem |
| AIS | Governo dos EUA | Gratuito, em tempo real |
| CVE | Dicionário | Identificador único |
| MISP | Plataforma aberta | Compartilhamento de IOCs |
| TIP | Plataforma | IOCs, TTPs e reputação |

## 7. Perfis de Rede, Detecção de Anomalias, SIEM e SOAR

A **criação de perfis** gera uma **linha de base estatística** do funcionamento normal. **Desvios inexplicáveis em relação à linha de base podem indicar um comprometimento.**

### 7.1 Perfil de Rede

Ao capturar a linha de base:

- **incluir todas as operações normais**, como os picos dos backups;
- **mantê-la atual**.

A **janela deslizante** (*sliding window*) usa o período mais representativo e **descarta os dados desatualizados**. A linha de base deve ser medida **durante um período prolongado**, com **NetFlow** e **Wireshark**.

| Elemento | O que mede |
| --- | --- |
| Duração da sessão | Início e fim de um fluxo |
| Taxa de transferência total | Quantidade de dados em um período |
| Portas usadas | Portas TCP e UDP em uso |
| Espaço de endereços de ativos críticos | Onde estão os sistemas essenciais |

Sinais de alerta:

- tráfego por **portas incomuns**;
- **aumento do tráfego entre clientes**, sinal de malware se espalhando **lateralmente**;
- **uso incomum dos links WAN** em horários estranhos, sinal de **retirada de dados**;
- domínios de **DNS dinâmico**;
- **mudanças no comportamento dos usuários**, como login de madrugada de um local remoto.

**Importante:** **desvios são difíceis de detectar se o normal não é conhecido**.

### 7.2 Perfil de Servidor

O **perfil de servidor** é a **linha de base de segurança de um servidor específico**.

| Elemento | O que define |
| --- | --- |
| Portas de escuta | Portas que podem ficar abertas |
| Usuários e contas | Acesso e comportamento esperados |
| Contas de serviço | Serviços que os aplicativos executam |
| Ambiente de software | **Processos e aplicativos permitidos** |

### 7.3 Detecção de Anomalias

A **NBA** (*Network Behavior Analysis*) usa **estatística e aprendizado de máquina** para comparar a linha de base com o desempenho atual. **Desvios significativos podem ser indicadores de comprometimento.**

#### 7.3.1 Exemplo Resolvido: Alarme por Contagem de Fluxos

A cada X minutos → contar os fluxos com amostragem de 1/Y durante Z segundos → se fluxos > N → alarme

Com X = 5, Y = 100, Z = 30 e N = 500: a cada 5 minutos, amostrar 1 de cada 100 fluxos por 30 segundos; mais de 500 fluxos gera alarme.

| Abordagem | Como detecta |
| --- | --- |
| Estatística e comportamental | Desvio da linha de base |
| Baseada em regras | Padrões conhecidos de ataque |

### 7.4 SIEM

O **SIEM** (*Security Information and Event Management*) **reúne os logs** de dispositivos, servidores e aplicativos, com relatórios em tempo real e análise de longo prazo. Une o **SIM** (gerenciamento de informações de segurança, que guarda e analisa os logs) e o **SEM** (gerenciamento de eventos de segurança, que monitora em tempo real).

Funções essenciais:

- **correlação**: liga eventos de sistemas diferentes e **acelera a detecção**;
- **agregação**: **reduz o volume** consolidando registros duplicados;
- **análise forense**: **pesquisa os logs de toda a empresa**;
- **retenção e relatórios**.

O SIEM ajuda a gerar **relatórios de conformidade para auditorias**. Os mais avançados têm **UEBA** (*User and Entity Behavior Analytics*), análise de comportamento de usuários.

| Informação | Exemplos |
| --- | --- |
| Do usuário | Nome, autenticação, local, grupo |
| Do dispositivo | Fabricante, SO, MAC, localização |
| De postura | Conformidade com a política, antivírus e patches |

**Observação:** o SIEM é **caro** e só compensa com **milhões de eventos por dia**.

### 7.5 SOAR

O **SOAR** (*Security Orchestration, Automation and Response*) **coleta dados de ameaças e responde a eventos de nível mais baixo sem intervenção humana**. Recursos:

- gerenciamento de ameaças e vulnerabilidades;
- resposta a incidentes;
- automação das operações.

O SIEM detecta e correlaciona; o SOAR automatiza a resposta.

## 8. Avaliações e Testes de Segurança

Com a linha de base definida, a empresa precisa descobrir **onde está vulnerável antes que um atacante descubra**.

### 8.1 Análise de Risco, Avaliação de Vulnerabilidades e Teste de Penetração

| Atividade | O que faz | Ferramentas |
| --- | --- | --- |
| Análise de risco | Avalia **probabilidade, atacantes e impacto** | Consultores, estruturas de riscos |
| Avaliação de vulnerabilidades | **Procura vulnerabilidades** com software, como patches ausentes; vai além da varredura de portas | OpenVAS, Nessus, Qualys, Nmap |
| Teste de penetração | **Ataques simulados autorizados** que **exploram** as vulnerabilidades | Metasploit, CORE Impact |

**Importante:** a avaliação de vulnerabilidades **encontra**; o teste de penetração **explora**.

### 8.2 Scanners de Vulnerabilidades

Um **scanner de vulnerabilidades** **procura pontos fracos** e **gera uma lista priorizada** do que corrigir. Ele procura:

- **senhas padrão**;
- **patches não instalados**;
- **portas abertas**;
- erros de configuração;
- dispositivos inesperados na rede.

Exemplos: **Nessus**, **Retina**, **Core Impact** e **GFI LanGuard**.

Categorias:

- **de rede**: portas abertas e vulnerabilidades conhecidas;
- **de aplicativos**: **examinam o código-fonte sem executá-lo**;
- **de aplicativos web**.

| Varredura | Característica |
| --- | --- |
| Invasiva | **Tenta explorar** e pode **travar o alvo** |
| Não invasiva | Tenta não causar danos |
| Credenciada | Entra com **usuário e senha**; gera **menos falsos positivos e negativos** |
| Não credenciada | **Visão de quem está de fora** |

- **falso positivo**: aponta vulnerabilidade que **não existe**;
- **falso negativo**: **não aponta** uma vulnerabilidade que existe.

### 8.3 Segurança das Operações

A **segurança das operações** trata das **práticas diárias para implantar e manter um sistema seguro**. A equipe de testes precisa conhecer sistemas operacionais, programação, protocolos, mitigação de riscos, *hardening*, firewalls e IPS.

### 8.4 Teste e Avaliação de Segurança (ST&E)

O **teste de segurança** verifica **se as proteções funcionam como esperado**. Os resultados devem ser **documentados e compartilhados**.

O **ST&E** (*Security Test and Evaluation*) **examina as proteções de uma rede em operação**:

- descobre falhas de projeto, implementação e operação;
- verifica se os mecanismos aplicam a política;
- avalia a **consistência entre documentação e implementação**.

Os testes devem ser **repetidos periodicamente e a cada mudança**.

### 8.5 Tipos de Teste de Rede

| Teste | O que faz |
| --- | --- |
| Teste de penetração | **Simula ataques**, inclusive **engenharia social** |
| Varredura de rede | Ping e **portas TCP de escuta** |
| Varredura de vulnerabilidades | Configuração incorreta e **senhas em branco ou padrão** |
| Quebra de senhas | Detecta **senhas fracas** |
| Revisão de logs | Acha **atividades anormais** |
| Verificador de integridade | **Detecta mudanças nos arquivos** |
| Detecção de vírus | Remove malware |

**Observação:** o **war dialing** (discagem em massa para achar modems) e o **war driving** (procura de redes sem fio a partir de um veículo) são testes legados.

### 8.6 Uso dos Resultados

Os resultados servem para:

- **definir as ações de mitigação**;
- acompanhar o progresso;
- **análises de custo-benefício**;
- referência para as **ações corretivas**.

## 9. Teste de Penetração

O **teste de penetração** (*pen test*), ou **hacking ético**, **testa os pontos fracos usando as técnicas de um atacante**, com permissão da empresa.

**Importante:** o pen test **não é o mesmo que o teste de vulnerabilidades**, que só identifica problemas. O objetivo é **encontrar e corrigir as falhas antes dos criminosos**.

### 9.1 Tipos de Teste

| Tipo | Conhecimento do especialista | Custo e tempo |
| --- | --- | --- |
| Caixa preta | **Nenhum** | **Menor** |
| Caixa cinza | **Limitado** | Intermediário |
| Caixa branca | **Completo** (simula alguém de dentro) | **Maior** |

### 9.2 Fases do Teste de Penetração

Planejamento → Descoberta → Ataque → Relatório

1. **planejamento**: define as **regras de engajamento**;
2. **descoberta**: **reconhecimento** do alvo:
   - **passivo** (*footprinting*): sem interagir com o alvo;
   - **ativo**: com interação, como a varredura de portas;
3. **ataque**: entra no sistema, tenta **escalada de privilégios** e **movimento lateral** (*pivoting*); pode plantar um backdoor (**persistência**) e, no fim, **limpa o sistema**;
4. **relatório**: **documentação detalhada das vulnerabilidades e dos resultados**.

### 9.3 Exercícios de Equipes

| Equipe | Papel |
| --- | --- |
| Vermelha (*red team*) | **Ataca** sem ser percebida |
| Azul (*blue team*) | **Defende** |
| Branca (*white team*) | **Árbitro**: define regras e supervisiona |
| Roxa (*purple team*) | Vermelha e azul **juntas** |

O **bug bounty** é um programa, em geral **aberto ao público**, que paga **recompensas** por falhas encontradas.

## 10. Ferramentas de Teste de Segurança

As avaliações e os testes usam ferramentas que vão de comandos do sistema operacional a scanners e analisadores de pacotes.

### 10.1 Utilitários de Linha de Comando

| Comando | O que faz | Equivalente no Linux/macOS |
| --- | --- | --- |
| ipconfig | Configuração TCP/IP (IP, máscara, gateway, DNS, MAC) | ifconfig |
| ping | Testa a conectividade com **ICMP** | ping |
| arp | Tabela que **associa MAC a IP** | arp |
| tracert | **Rastreia a rota** do pacote | traceroute |
| nslookup | **Consulta o DNS** | dig |
| netstat | **Portas em escuta** e conexões ativas | netstat |
| nbtstat | Nomes NetBIOS no Windows | — |
| nmap | Localiza hosts, **detecta o sistema operacional** e serviços | nmap |
| netcat | Lê e grava conexões TCP e UDP; captura de banner | netcat |
| hping | **Monta pacotes**; teste de firewall | hping |

### 10.2 Ferramentas de Teste de Rede

- **Nmap/Zenmap**: **mapa da rede**;
- **SuperScan**: varredura de portas TCP e UDP;
- **GFI LanGuard**: scanner de vulnerabilidades;
- **Tripwire**: **valida configurações** contra políticas e padrões;
- **Nessus**: varredura de vulnerabilidades;
- **L0phtCrack**: **recuperação de senhas**;
- **Metasploit**: **testes de penetração**.

### 10.3 Nmap e Zenmap

O **Nmap** é um scanner gratuito para **mapear a rede e fazer reconhecimento**; o **Zenmap** é sua versão gráfica. Funções:

- **varredura de portas**: **vários serviços em um host**;
- **varredura de hosts** (*port sweeping*): **o mesmo serviço em vários hosts**;
- **varreduras furtivas**: **mais difíceis de detectar**;
- **identificação remota do sistema operacional** (*OS fingerprinting*).

**Importante:** o Nmap **também serve a fins maliciosos** e pode usar **hosts falsos (iscas)** para esconder a origem.

### 10.4 SuperScan

O **SuperScan** é um scanner de portas para **Windows**, que exige **privilégios de administrador**. Faz varredura TCP SYN e UDP, **captura de banners** e enumeração de hosts Windows.

### 10.5 Analisadores de Pacotes

Os **analisadores de pacotes** (*sniffers*) **interceptam e registram o tráfego de rede**. Usos:

- análise de problemas;
- detecção de tentativas de invasão;
- isolamento do sistema explorado;
- registro do tráfego.

No **sniffing**, o atacante **examina todo o tráfego que passa pela placa de rede**. A **segurança física** impede que sniffers sejam ligados à rede interna.

## 11. Pontuação de Vulnerabilidades (CVSS)

O **CVSS** (*Common Vulnerability Scoring System*) **descreve a gravidade das vulnerabilidades com uma nota numérica**, usada para decidir **a urgência e a prioridade da correção**.

### 11.1 Visão Geral

O CVSS é **aberto, neutro e padrão do setor**. Benefícios:

- **notas padronizadas**, com o mesmo significado em todas as empresas;
- estrutura aberta;
- priorização significativa para cada empresa.

O **FIRST** é o **guardião do CVSS**. A versão atual é a **3.1** (2019).

Uma **autoridade** é uma entidade que concede acessos e privilégios, como um sistema operacional ou um banco de dados.

### 11.2 Grupos de Métricas

O CVSS usa **três grupos de métricas**:

| Grupo | O que mede | Quem define |
| --- | --- | --- |
| Base | Características **constantes no tempo e em qualquer contexto** | Fornecedor; **não muda** |
| Temporal | Características que **mudam com o tempo** | Fornecedor |
| Ambiental | Aspectos do **ambiente de cada empresa** | Usuário final, **opcional** |

O grupo **temporal** reflete que a gravidade **cai à medida que surgem patches** e contramedidas. Métricas: maturidade do código de exploração, nível de correção e confiança no relatório.

### 11.3 Grupo de Métricas Base

As **métricas de explorabilidade** descrevem a exploração:

| Métrica | O que expressa |
| --- | --- |
| Vetor de ataque (AV) | **Proximidade do atacante**; **quanto mais distante, maior a gravidade**: uma falha explorável pela internet é mais grave que uma que exige tocar no equipamento |
| Complexidade do ataque (AC) | Condições **fora do controle do atacante** |
| Privilégios necessários (PR) | **Nível de acesso** necessário |
| Interação do usuário (UI) | Se precisa da **ação de um usuário** |
| Escopo (S) | Se a exploração **passa de uma autoridade para outra**; exemplo: uma falha em uma máquina virtual que permite atingir o servidor físico |

As **métricas de impacto** seguem a **tríade CIA**: impacto na confidencialidade (C), na integridade (I) e na disponibilidade (A).

### 11.4 O Processo CVSS

A avaliação usa a **Calculadora CVSS v3.1**, do FIRST: para cada métrica, escolhe-se **um único valor**.

**Importante:** o **grupo base é preenchido primeiro**; as métricas temporais e ambientais **modificam a nota base**.

Métricas base → Nota base → Nota temporal → Nota ambiental

A **string de vetor** resume as escolhas: pares **sigla:valor** separados por **barras**.

| Métrica | Sigla | Valores |
| --- | --- | --- |
| Vetor de ataque | AV | N = rede; A = adjacente; L = local; P = físico |
| Complexidade do ataque | AC | L = baixa; H = alta |
| Privilégios necessários | PR | N = nenhum; L = baixo; H = alto |
| Interação do usuário | UI | N = nenhuma; R = necessária |
| Escopo | S | U = inalterado; C = alterado |
| Confidencialidade | C | H = alto; L = baixo; N = nenhum |
| Integridade | I | H = alto; L = baixo; N = nenhum |
| Disponibilidade | A | H = alto; L = baixo; N = nenhum |

#### 11.4.1 Exemplo Resolvido: Leitura de uma String de Vetor

`CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:N`

| Par | Leitura |
| --- | --- |
| AV:N | Ataque pela **rede** |
| AC:L | Complexidade **baixa** |
| PR:H | Privilégios **altos** |
| UI:N | **Nenhuma** interação do usuário |
| S:U | Escopo **inalterado** |
| C:L | Impacto **baixo** na confidencialidade |
| I:L | Impacto **baixo** na integridade |
| A:N | **Nenhum** impacto na disponibilidade |

### 11.5 Classificação das Notas

| Classificação | Nota CVSS |
| --- | --- |
| Nenhuma | 0 |
| Baixa | 0,1 a 3,9 |
| Média | 4,0 a 6,9 |
| Alta | 7,0 a 8,9 |
| Crítica | 9,0 a 10,0 |

O **fornecedor informa as notas base e temporal**; a **empresa completa o grupo ambiental**.

**Importante:** em geral, **toda vulnerabilidade acima de 3,9 deve ser corrigida**.

### 11.6 CVE e NVD

- **CVE**: o **identificador** de cada vulnerabilidade conhecida, mantido pela MITRE; é a forma padrão de **pesquisar uma vulnerabilidade e achar suas correções**;
- **NVD** (*National Vulnerability Database*): **usa os identificadores CVE** e acrescenta **notas CVSS e detalhes técnicos**; mantido pelo **NIST**.

| Recurso | Mantido por | O que oferece |
| --- | --- | --- |
| CVSS | FIRST | Nota de gravidade |
| CVE | MITRE | Identificador único |
| NVD | NIST | CVE + nota CVSS + detalhes |

## 12. Gerenciamento Seguro de Dispositivos

É preciso **manter os dispositivos sob controle** de forma contínua, com o gerenciamento de vulnerabilidades, ativos, dispositivos móveis, configurações e patches.

### 12.1 Gerenciamento de Vulnerabilidades

O **gerenciamento de vulnerabilidades** **impede proativamente a exploração das vulnerabilidades**. Agir antes custa muito menos do que responder depois.

Ele exige:

- **identificar vulnerabilidades** por boletins dos fornecedores e pelo CVE;
- pessoal para avaliar o impacto;
- implementar soluções com cuidado;
- **testar a solução**.

Descobrir → Priorizar ativos → Avaliar → Relatar → Corrigir → Verificar

1. **descobrir**: **inventariar os ativos** e fazer varreduras regulares;
2. **priorizar os ativos**: dar um **valor comercial** a cada grupo;
3. **avaliar**: definir um **perfil de risco**;
4. **relatar**: medir o risco e documentar o plano;
5. **corrigir**: **resolver em ordem de risco**;
6. **verificar**: **auditorias de acompanhamento**.

### 12.2 Gerenciamento de Ativos

O **gerenciamento de ativos** **controla a localização e a configuração de dispositivos e software**. Também **identifica dispositivos não autorizados**.

O **NISTIR 8011** define um ciclo:

Estado atual + Estado desejado → Discrepâncias → Corrigir, aceitar ou atualizar a política → Repetir

### 12.3 Gerenciamento de Dispositivos Móveis

O **MDM** (*Mobile Device Management*) é desafiador, principalmente com o **BYOD**, porque os aparelhos **não ficam fisicamente na empresa**.

Se um aparelho for perdido:

- **desativar o dispositivo**;
- **criptografar os dados**;
- reforçar a autenticação.

**Importante:** **todo dispositivo móvel é não confiável até que a empresa o proteja**.

Exemplo de MDM: **Cisco Meraki Systems Manager**, gerenciado pela nuvem.

### 12.4 Gerenciamento de Configurações

O **gerenciamento de configurações** **controla as configurações de hardware e software**. Exemplo: **imagens de linha de base** para cada tipo de computador, que impedem o usuário de alterar configurações sensíveis.

Para o NIST (**SP 800-128**), ele **mantém a integridade** dos sistemas controlando a inicialização, a mudança e o monitoramento das configurações.

Ferramentas para servidores e nuvem: **Puppet, Chef, Ansible e SaltStack**.

### 12.5 Gerenciamento de Patches

O **gerenciamento de patches** cobre identificar, obter, distribuir, instalar e **verificar** os patches.

**Importante:** aplicar patches é **a forma mais eficaz**, às vezes **a única**, de mitigar vulnerabilidades de software.

Regulamentações como **SOX** e **HIPAA** **exigem** o gerenciamento de patches. Ele **depende do gerenciamento de ativos** para saber o que corrigir.

| Técnica | Como funciona | Limitação |
| --- | --- | --- |
| Baseada em agente | **Agente em cada host** | **Preferida para dispositivos móveis** |
| Varredura sem agente | O **servidor varre a rede** | Só alcança os segmentos varridos |
| Monitoramento passivo | Identifica pelo **tráfego de rede** | Só se o software informa a versão |

Antes da distribuição, **os patches são testados**.

## 13. Cyber Kill Chain

A **Cyber Kill Chain**, da **Lockheed Martin**, descreve **as sete etapas que um atacante precisa completar** para atingir seu objetivo.

### 13.1 As Sete Etapas

Reconhecimento → Armamento → Entrega → Exploração → Instalação → Comando e controle → Ações nos objetivos

![As sete etapas da Cyber Kill Chain; romper qualquer uma delas faz o ataque fracassar](img/ameacas/gt_killchain.png){width=6in}

| Etapa | O que o atacante faz |
| --- | --- |
| 1. Reconhecimento | **Pesquisa informações** sobre o alvo |
| 2. Armamento (*weaponization*) | **Junta o malware a um backdoor** |
| 3. Entrega | **Envia a arma à vítima** |
| 4. Exploração | **Executa o código** no sistema vulnerável |
| 5. Instalação | **Instala um backdoor** |
| 6. Comando e controle (C2) | Cria um **canal externo** para manipular o alvo |
| 7. Ações nos objetivos | Cumpre o objetivo com acesso "mãos no teclado" |

**Importante:** se o atacante for parado **em qualquer etapa, a cadeia se rompe**. Quanto antes, **menor o dano**.

### 13.2 Reconhecimento

O atacante **pesquisa e escolhe os alvos**, usando informações públicas e **redes sociais dos funcionários**.

| Táticas do atacante | Defesa do SOC |
| --- | --- |
| Coletar e-mails; identificar funcionários; **varrer a rede** | **Descobrir a intenção do adversário** nos logs; priorizar a defesa das pessoas e tecnologias visadas |

O **SOC** (*Security Operations Center*) é a equipe que monitora e defende a rede.

### 13.3 Armamento

O atacante **desenvolve uma arma** a partir das vulnerabilidades descobertas. Ataques conhecidos também são conhecidos pelos defensores; por isso, um **ataque de dia zero** é mais eficaz.

| Táticas do atacante | Defesa do SOC |
| --- | --- |
| Obter ferramentas de armamento; criar documento-isca e backdoor | **Coletar os artefatos de armamento**; manter as regras do IDS atualizadas; analisar o malware |

### 13.4 Entrega

**Se a arma não for entregue, o ataque fracassa.** O atacante criptografa ou **ofusca** o código.

| Táticas do atacante | Defesa do SOC |
| --- | --- |
| Entrega **direta** contra servidores; **indireta** por e-mail, pen drive ou sites comprometidos | **Bloquear a entrega**; **guardar e-mails e logs web** para a perícia |

### 13.5 Exploração

O atacante **explora a vulnerabilidade e ganha o controle do alvo**: aplicativos, sistema operacional ou usuários.

| Táticas do atacante | Defesa do SOC |
| --- | --- |
| Exploração acionada pelo atacante ou pela vítima (abrir um anexo) | **Treinar os funcionários**; pen tests regulares; **hardening dos endpoints** |

### 13.6 Instalação

O atacante **instala um backdoor para manter o acesso contínuo**, que sobrevive a reinicializações.

| Táticas do atacante | Defesa do SOC |
| --- | --- |
| Instalar um **webshell** no servidor web; criar **persistência** com chaves AutoRun | **HIPS** para alertar ou bloquear a instalação; auditar os endpoints |

### 13.7 Comando e Controle

Os hosts comprometidos **"chamam" um controlador na internet**. O analista os descobre ao **detectar a comunicação C2**, como tráfego para domínios suspeitos.

| Táticas do atacante | Defesa do SOC |
| --- | --- |
| Canal bidirecional por **web, DNS e e-mail** | **Última chance de bloquear a operação**; isolar tráfego para **DNS dinâmico**; **bloquear o canal C2** |

### 13.8 Ações nos Objetivos

O atacante **alcança seu objetivo**: roubar dados, DDoS, spam ou mineração. Ele já está **profundamente enraizado**, e é **extremamente difícil removê-lo**.

| Táticas do atacante | Defesa do SOC |
| --- | --- |
| **Escalar privilégios**, movimento lateral, retirar ou destruir dados | Detectar com **evidências forenses**; responder a todos os alertas; **capturas de pacotes** para recriar a atividade |

## 14. Modelo Diamond de Análise de Intrusão

O **Modelo Diamond** olha para **cada evento** e mostra **quem atacou, com o quê, por onde e contra quem**.

### 14.1 Os Quatro Elementos

Um **evento** é uma atividade em que **um adversário usa uma capacidade sobre uma infraestrutura para atacar uma vítima**.

| Elemento | O que é |
| --- | --- |
| Adversário | **Responsável pela intrusão** |
| Capacidade | **Ferramenta ou técnica** usada |
| Infraestrutura | **Caminho de rede** usado para o comando e controle |
| Vítima | **Alvo** do ataque; pode virar infraestrutura para novos ataques |

Exemplo: um adversário usa um malware (capacidade) por meio do e-mail (infraestrutura) para explorar uma vítima.

![Modelo Diamond: o adversário usa uma capacidade, por meio de uma infraestrutura, contra uma vítima](img/ameacas/gt_diamond.png){width=6in}

### 14.2 Meta-recursos

| Meta-recurso | O que indica |
| --- | --- |
| Carimbo de hora | **Início e fim** do evento |
| Fase | Equivale às **etapas da Cyber Kill Chain** |
| Resultado | O que foi comprometido (CIA) |
| Direção | Sentido do evento entre os elementos |
| Metodologia | **Tipo geral do evento**, como phishing ou varredura |
| Recursos | Software, conhecimento, informações e ativos usados |

### 14.3 Pivotar pelo Modelo

O analista **"gira" (*pivot*) de um elemento a outro** na investigação:

1. a **vítima** relata um problema, e acha-se um malware (**capacidade**);
2. o malware revela **domínios de C2** (**infraestrutura**);
3. os domínios resolvem para **IPs de C2**;
4. os logs do firewall mostram **outras vítimas** contatando esses IPs;
5. os dados dos IPs **revelam o adversário**.

### 14.4 Modelo Diamond e Cyber Kill Chain

Os eventos formam uma **linha de atividade** (*activity thread*), mapeada nas etapas da Cyber Kill Chain. O adversário percorre a cadeia **verticalmente** e **gira horizontalmente** para outra vítima.

#### 14.4.1 Exemplo: Duas Vítimas Encadeadas

1. o adversário pesquisa a Gadgets, Inc. e acha os e-mails dos administradores de rede;
2. envia **phishing com cavalo de Troia**;
3. um administrador abre o anexo, e o host se registra no **controlador de C2**;
4. o malware vira um **proxy web**;
5. pelo proxy, o adversário acha uma segunda empresa e seu diretor de pesquisa nos contatos do administrador;
6. o diretor recebe um **spear phishing vindo do endereço da Gadgets**.

O adversário tem agora **duas vítimas comprometidas**.

| Modelo | Foco | Pergunta que responde |
| --- | --- | --- |
| Cyber Kill Chain | **Etapas** do ataque | Em que ponto o ataque está e onde pode ser interrompido? |
| Modelo Diamond | **Elementos** de cada evento | Quem atacou, com o quê, por onde e contra quem? |

## 15. Perícia Forense Digital e Atribuição de Ataques

Quando o analista confirma um alerta, ele tem **provas de uma atividade criminosa** e precisa tratá-las corretamente.

### 15.1 Perícia Forense Digital

A **perícia forense digital** é a **recuperação e investigação das informações de dispositivos digitais** ligadas a crimes. **Todos os IOCs precisam ser preservados**: discos, **memória volátil**, **pcaps** e logs.

- **investigação privada**: pessoas **de dentro** com condutas não criminosas;
- **investigação pública**: quando há **crime**, a polícia conduz;
- **atacante externo**: as provas documentam o **alcance da exploração**.

Exemplo: pela **HIPAA**, os afetados por uma violação de dados de saúde **precisam ser notificados**; acima de 500 pessoas, a mídia também.

**Importante:** se ficar provada a **intenção de destruir provas**, a empresa e **até o analista** podem sofrer penalidades criminais.

### 15.2 O Processo Forense

O **NIST SP 800-86** recomenda quatro fases:

Coleta → Exame → Análise → Relatório

1. **coleta**: **identificar as fontes** e obter os dados **sem danificá-los**;
2. **exame**: **extrair as informações relevantes**;
3. **análise**: **tirar conclusões**, correlacionando várias fontes;
4. **relatório**: resultados **imparciais**, com explicações alternativas e limitações.

### 15.3 Tipos de Evidência

As provas são **diretas** (com o acusado ou de **testemunhas oculares**) ou **indiretas**.

| Tipo | O que é |
| --- | --- |
| Melhor evidência | Evidência **em seu estado original** |
| Corroborativa | **Apoia uma afirmação** baseada na melhor evidência |
| Indireta (circunstancial) | **Junto com outros fatos, sustenta uma hipótese** |

### 15.4 Ordem de Coleta

A **RFC 3227** orienta a coleta **da evidência mais volátil para a menos volátil**. A **RAM** é a **mais volátil**: some ao desligar.

1. **registradores e caches**;
2. tabela de roteamento, cache ARP, tabela de processos e **RAM**;
3. sistemas de arquivos temporários;
4. **mídias não voláteis**;
5. logs remotos;
6. topologia física;
7. **mídias de arquivamento** e backups.

![Ordem de coleta das evidências, da mais volátil (some primeiro) para a menos volátil](img/ameacas/gt_coleta.png){width=6in}

### 15.5 Cadeia de Custódia

A **cadeia de custódia** é **a coleta, o manuseio e o armazenamento seguro das evidências**, com registros de:

- **quem coletou** as provas;
- todos os detalhes do manuseio: **horários, locais e pessoas**;
- **quem é o responsável** e quando a custódia mudou;
- **quem teve acesso físico** às provas.

Assim, a defesa não pode alegar que as provas foram **alteradas ou fabricadas**.

### 15.6 Integridade e Preservação

- **a análise é feita só em cópias**, nunca no original;
- as cópias devem ser **cópias bit a bit**;
- o **original é arquivado e protegido** para comparação;
- a **memória volátil** é preservada **antes de desligar** o dispositivo.

**Importante:** os usuários **não devem desligar nem desconectar** máquinas infectadas, a menos que a segurança mande.

### 15.7 Atribuição de Ataques

A **atribuição de ameaças** é **determinar o responsável** por uma intrusão: indivíduo, organização ou **estado-nação**.

A atribuição deve vir de uma **investigação sistemática das provas**, não de especulação. A equipe **compara as TTPs do incidente com as de ataques conhecidos**.

**Importante:** semelhanças de TTPs são **evidência circunstancial**.

Nas **ameaças internas**, **IPs, MACs, logs de DHCP e logs AAA** ligam o ataque a um dispositivo e a uma pessoa.

### 15.8 MITRE ATT&CK

O **MITRE ATT&CK** (*Adversarial Tactics, Techniques and Common Knowledge*) é uma **base de conhecimento do comportamento dos atacantes**, construída com ataques reais. Organiza-se em uma **matriz**:

- **táticas**: os **objetivos** do atacante;
- **técnicas**: **os meios** para cumprir as táticas;
- **procedimentos**: as **ações específicas** documentadas no mundo real.

## 16. Resposta a Incidentes

A **resposta a incidentes** reúne os **métodos, políticas e procedimentos** para reagir a um ataque. Objetivos: **limitar o impacto, avaliar os danos e recuperar** os sistemas.

### 16.1 Capacidade de Resposta a Incidentes

O guia de referência é o **NIST SP 800-61, revisão 2**.

O primeiro passo é criar uma **CSIRC** (*Computer Security Incident Response Capability*), com três documentos:

| Documento | O que contém |
| --- | --- |
| Política | **Como os incidentes são tratados**: objetivos, definições, funções, **níveis de autoridade** e **priorização por gravidade** |
| Plano | **Missão**, estratégias, **aprovação da alta gerência** e métricas |
| Procedimentos | Processos técnicos e **listas de verificação** |

Os procedimentos são **SOPs** (*Standard Operating Procedures*), que **reduzem os erros de quem trabalha sob estresse**.

### 16.2 Partes Interessadas

Além do **CSIRT** (equipe de resposta a incidentes), participam, com cooperação combinada **antes** do incidente:

| Parte | Papel |
| --- | --- |
| Gerência | **Coordena a resposta**, define orçamento e equipe |
| Garantia da informação | Muda regras de firewall |
| Suporte de TI | **Contém o ataque e preserva as provas** |
| Jurídico | Revisa planos e cuida de questões legais |
| Relações públicas | Informa a mídia e o público |
| Recursos humanos | **Medidas disciplinares** contra funcionários |
| Planejadores de continuidade | Ajustam os planos de continuidade |
| Segurança física | Ataques físicos, como **tailgating** |

### 16.3 CMMC e a Resposta a Incidentes

O **CMMC** avalia os fornecedores da **cadeia de suprimentos militar** dos EUA. Na resposta a incidentes, tem **quatro níveis** (do 2 ao 5); **quanto maior o nível, mais madura a capacidade**:

| Nível | Exigências |
| --- | --- |
| 2 | Plano que **siga o processo do NIST** |
| 3 | **Testar a capacidade de resposta** |
| 4 | Usar as **TTPs**; ter um **SOC 24/7** |
| 5 | Forense sistemática e respostas **automatizadas em tempo real** |

### 16.4 Ciclo de Vida da Resposta a Incidentes

O NIST define **quatro fases**:

Preparação → Detecção e análise → Contenção, erradicação e recuperação → Atividade pós-incidente

![Ciclo de vida da resposta a incidentes do NIST](img/ameacas/gt_ir.png){width=6in}

| Fase | O que o CSIRT faz |
| --- | --- |
| Preparação | É **criado e treinado** |
| Detecção e análise | **Identifica, analisa e valida** o incidente |
| Contenção, erradicação e recuperação | **Contém, elimina e restaura**; pode voltar à detecção |
| Atividade pós-incidente | **Documenta** e define como evitar a repetição |

**Importante:** cada incidente melhora o tratamento dos próximos.

### 16.5 Preparação

Na **preparação**:

- criar os processos de **comunicação** e a lista de contatos;
- montar o **SOC**;
- adquirir ferramentas de análise, como **software forense e sniffers**;
- implementar controles a partir das **avaliações de risco**;
- preparar o **treinamento de conscientização**.

Também ajudam: lista de ativos críticos, diagramas de rede, **hashes dos arquivos críticos** e **linhas de base**.

O **kit de salto** (*jump kit*) é **uma caixa portátil com o necessário para uma resposta rápida**, inspecionada regularmente.

### 16.6 Detecção e Análise

Vetores de ataque mais comuns:

- **web**;
- **e-mail**;
- **perda ou roubo** de equipamentos;
- **personificação** (*impersonation*): algo ou alguém **substituído com intenção maliciosa**;
- **desgaste** (*attrition*): ataques de **força bruta**;
- **mídia**: armazenamento removível.

**Importante:** a detecção pode ser **a fase mais difícil**; alguns incidentes passam despercebidos por meses.

| Sinal | O que indica | Exemplos |
| --- | --- | --- |
| Precursor | Que um incidente **pode ocorrer no futuro** | Varredura de portas; vulnerabilidade nova |
| Indicador | Que um incidente **já ocorreu ou está ocorrendo** | Malware no host; alerta do IDS |

**Até sintomas ambíguos devem ser analisados**, documentando cada etapa.

A **análise inicial do escopo** identifica **o que foi afetado, quem originou e como**.

Depois, a equipe **notifica as partes adequadas**: CIO, segurança da informação, dono do sistema, RH, relações públicas, jurídico e, se for o caso, a polícia.

### 16.7 Contenção, Erradicação e Recuperação

As estratégias de **contenção** devem **existir antes do incidente**. Consideram tempo, recursos, **preservação das evidências**, impacto na disponibilidade e eficácia. O atacante pode ser **redirecionado para uma sandbox**.

**Importante:** **nem sempre convém desconectar o host comprometido**: o malware pode perceber e **apagar ou criptografar os dados**.

As provas exigem a **cadeia de custódia**. Registrar:

- **local** de cada prova;
- **identificação** (número de série, MAC, IP);
- **todas as pessoas** que as manusearam;
- **data e hora** de cada manuseio.

**Identificar o atacante é secundário** à contenção. Recursos: bancos de incidentes como o **VERIS**.

**Erradicação**: eliminar malware e **contas comprometidas** e **corrigir as vulnerabilidades**.

**Recuperação**:

- restaurar com **backups limpos** ou reconstruir;
- atualizar e corrigir os sistemas;
- **trocar todas as senhas**;
- revisar a segurança, porque **os atacantes costumam voltar**.

### 16.8 Atividade Pós-incidente

A reunião de **lições aprendidas** avalia o tratamento e reforça os controles. Perguntas:

- o que aconteceu, e quando?
- os procedimentos foram seguidos e eram adequados?
- alguma ação **atrapalhou a recuperação**?
- o que fazer diferente?
- quais **precursores ou indicadores** observar no futuro?

### 16.9 Coleta e Retenção dos Dados

Os dados devem ser **acionáveis**: servem para calcular o **custo do incidente** e avaliar o CSIRT.

**Observação:** **muitos incidentes** podem indicar falha; **poucos** podem indicar **falta de detecção**.

A avaliação é **objetiva** (logs, causa real, dano financeiro) e **subjetiva** (desempenho da equipe).

A **política de retenção** define o prazo das evidências conforme:

- **processo judicial**: até o fim de todas as ações legais;
- **tipo de dado**: e-mails, 90 dias; dados de incidente sem ação legal, três anos ou mais;
- **custo** do armazenamento.

### 16.10 Relatórios e Compartilhamento de Informações

O **jurídico** define a obrigação de relatar o incidente. O NIST recomenda:

- **planejar a coordenação antes** dos incidentes;
- consultar o jurídico;
- compartilhar durante todo o ciclo;
- **automatizar** o compartilhamento;
- equilibrar benefícios e riscos de expor informações.

## 17. Recuperação de Desastres e Continuidade de Negócios

A empresa precisa continuar funcionando diante de **desastres**, com dois planos: **recuperação de desastres** e **continuidade de negócios**.

### 17.1 Tipos de Desastres

Um **desastre** é **qualquer evento natural ou humano que prejudica a capacidade de operação** da empresa.

**Naturais**:

- geológicos: terremotos, deslizamentos;
- meteorológicos: furacões, raios;
- de saúde: **pandemias**;
- diversos: incêndios, inundações.

**Provocados por pessoas**:

- trabalhistas: greves;
- sociopolíticos: vandalismo, **sabotagem**, terrorismo;
- materiais: vazamentos de produtos perigosos;
- **interrupção de serviços essenciais**: falta de energia, falhas de comunicação.

### 17.2 Plano de Recuperação de Desastres

O **DRP** (*Disaster Recovery Plan*) é posto em ação **enquanto o desastre está em curso**, para **avaliar, recuperar, reparar e restaurar** instalações e ativos.

Para cada processo, responde-se: **quem, o que, onde, qual e por quê**.

**Importante:** a recuperação começa pelos **sistemas de missão crítica**.

| Controle | O que faz |
| --- | --- |
| Preventivo | **Evita que o desastre ocorra** |
| De detecção | **Descobre eventos indesejados** |
| Corretivo | **Restaura o sistema** depois do desastre |

### 17.3 Plano de Continuidade de Negócios

**Importante:** o **BCP** (*Business Continuity Plan*) é **mais amplo que o DRP**: inclui **levar os sistemas essenciais para outro local** e continuar os processos de forma alternativa.

O BCP começa pela **BIA** (*Business Impact Analysis* — análise de impacto nos negócios), que **identifica os processos mais importantes e as consequências de uma interrupção**.

| Medida | Significado |
| --- | --- |
| **RTO** (*Recovery Time Objective*) | **Tempo máximo tolerável de indisponibilidade** |
| **RPO** (*Recovery Point Objective*) | **Perda máxima de dados tolerável**, medida em tempo; define a frequência dos backups |
| **MTTR** (*Mean Time To Repair*) | **Tempo médio para consertar** |
| **MTBF** (*Mean Time Between Failures*) | **Tempo médio entre falhas** |

Exemplo: com **RPO de 4 horas**, os backups precisam ser feitos pelo menos a cada 4 horas.

### 17.4 Considerações e Boas Práticas

A continuidade é **mais que backup e hardware redundante**. É preciso:

- **pessoas certas nos lugares certos**;
- configurações documentadas;
- canais de comunicação diferentes para voz e dados;
- fornecimento de energia;
- conhecer **todas as dependências**;
- saber executar **manualmente** as tarefas automatizadas.

Boas práticas do NIST:

1. escrever uma **política**;
2. fazer a **análise de impacto nos negócios**;
3. calcular o risco;
4. implementar controles;
5. desenvolver estratégias de recuperação;
6. desenvolver o **plano de contingência**;
7. **testar o plano**;
8. **manter o plano** atualizado.

### 17.5 Exercícios do Plano

| Exercício | Como funciona |
| --- | --- |
| De mesa (*tabletop*) | Os participantes **discutem um cenário**; **nada é executado** |
| Teste funcional | **Testa certos aspectos** do plano |
| Exercício operacional (simulação completa) | **Interrompe os serviços** para testar o plano inteiro |

| Plano | Quando atua | Abrangência |
| --- | --- | --- |
| DRP | Durante o desastre | Recuperar e restaurar ativos |
| BCP | Durante e depois | Manter a empresa funcionando, inclusive em outro local |

## Glossário de Siglas

| Sigla | Nome completo | Significado |
| --- | --- | --- |
| AAA | Authentication, Authorization and Accounting | Autenticação, autorização e registro dos acessos |
| AC | Attack Complexity | Complexidade do ataque, métrica do CVSS |
| AICPA | American Institute of Certified Public Accountants | Entidade dos contadores dos EUA, autora da norma SSAE 18 |
| AIS | Automated Indicator Sharing | Compartilhamento automatizado de indicadores do DHS |
| ALE | Annual Loss Expectancy | Expectativa de perda anual |
| APT | Advanced Persistent Threat | Ameaça persistente avançada |
| ARO | Annualized Rate of Occurrence | Taxa anualizada de ocorrência |
| ARP | Address Resolution Protocol | Protocolo que associa endereços IP a endereços MAC |
| ATT&CK | Adversarial Tactics, Techniques and Common Knowledge | Base de conhecimento do MITRE sobre o comportamento dos atacantes |
| AUP | Acceptable Use Policy | Política de uso aceitável |
| AV | Asset Value | Valor do ativo, usado na análise quantitativa de riscos |
| AV (CVSS) | Attack Vector | Vetor de ataque, métrica do CVSS |
| AV (risco) | Asset Value | Valor do ativo |
| BCP | Business Continuity Plan | Plano de continuidade de negócios |
| BIA | Business Impact Analysis | Análise de impacto nos negócios |
| BYOD | Bring Your Own Device | Uso de dispositivos pessoais no trabalho |
| C&A | Certification and Accreditation | Certificação e autorização de sistemas |
| C2 | Command and Control | Comando e controle, também escrito CnC |
| CCM | Cloud Controls Matrix | Matriz de controles de nuvem da CSA |
| CEI | Computer Ethics Institute | Instituto de Ética em Informática |
| CFAA | Computer Fraud and Abuse Act | Lei americana contra fraude e abuso de computadores |
| CIA | Confidentiality, Integrity, Availability | Tríade confidencialidade, integridade e disponibilidade |
| CIO | Chief Information Officer | Diretor de informação |
| CIPA | Children's Internet Protection Act | Lei americana de proteção de crianças na internet |
| CIS | Center for Internet Security | Centro de Segurança da Internet |
| CIS-CAT | CIS Configuration Assessment Tool | Ferramenta do CIS que avalia a conformidade |
| CMMC | Cybersecurity Maturity Model Certification | Certificação de maturidade dos fornecedores do DoD |
| COPPA | Children's Online Privacy Protection Act | Lei americana de privacidade online de crianças |
| CSA | Cloud Security Alliance | Aliança de Segurança na Nuvem |
| CSIRC | Computer Security Incident Response Capability | Capacidade de resposta a incidentes de segurança |
| CSIRT | Computer Security Incident Response Team | Equipe de resposta a incidentes de segurança |
| CTI | Cyber Threat Intelligence | Inteligência de ameaças cibernéticas |
| CVE | Common Vulnerabilities and Exposures | Dicionário de identificadores de vulnerabilidades |
| CVSS | Common Vulnerability Scoring System | Sistema comum de pontuação de vulnerabilidades |
| CybOX | Cyber Observable Expression | Esquemas para descrever eventos observáveis |
| DHCP | Dynamic Host Configuration Protocol | Protocolo que distribui endereços IP automaticamente |
| DHS | Department of Homeland Security | Departamento de Segurança Interna dos EUA |
| DNS | Domain Name System | Sistema que traduz nomes em endereços IP |
| DoD | Department of Defense | Departamento de Defesa dos EUA |
| DoS / DDoS | (Distributed) Denial of Service | Negação de serviço (distribuída) |
| DPO | Data Protection Officer | Encarregado de proteção de dados |
| DRP | Disaster Recovery Plan | Plano de recuperação de desastres |
| ECPA | Electronic Communications Privacy Act | Lei americana de privacidade das comunicações eletrônicas |
| EF | Exposure Factor | Fator de exposição |
| EPIC | Electronic Privacy Information Center | Centro de pesquisa sobre privacidade eletrônica |
| FBI | Federal Bureau of Investigation | Polícia federal dos EUA |
| FCC | Federal Communications Commission | Comissão Federal de Comunicações dos EUA |
| FERPA | Family Educational Rights and Privacy Act | Lei americana de privacidade dos registros escolares |
| FIRST | Forum of Incident Response and Security Teams | Fórum de equipes de resposta a incidentes; guardião do CVSS |
| FISMA | Federal Information Security Management Act | Lei de segurança da informação das agências federais dos EUA |
| FOIA | Freedom of Information Act | Lei americana de acesso à informação |
| FTC | Federal Trade Commission | Comissão Federal de Comércio dos EUA |
| GDPR | General Data Protection Regulation | Regulamento de proteção de dados da União Europeia |
| GLBA | Gramm-Leach-Bliley Act | Lei americana de privacidade no setor financeiro |
| GRE | Generic Routing Encapsulation | Protocolo de tunelamento da camada 3 |
| HIPAA | Health Insurance Portability and Accountability Act | Lei americana de proteção das informações de saúde |
| HIPS | Host-based Intrusion Prevention System | Sistema de prevenção de intrusão no host |
| HTTP / HTTPS | Hypertext Transfer Protocol (Secure) | Protocolo da web (seguro) |
| IC3 | Internet Crime Complaint Center | Centro de denúncias de crimes na internet do FBI |
| ICMP | Internet Control Message Protocol | Protocolo de mensagens de controle, usado pelo ping |
| IDS | Intrusion Detection System | Sistema de detecção de intrusão |
| IEC | International Electrotechnical Commission | Comissão Eletrotécnica Internacional |
| IETF | Internet Engineering Task Force | Organização que publica as RFCs |
| IOC | Indicator of Compromise | Indicador de comprometimento |
| IP | Internet Protocol | Protocolo de endereçamento da internet |
| IPS | Intrusion Prevention System | Sistema de prevenção de intrusão |
| IRC | Internet Relay Chat | Protocolo de bate-papo, às vezes usado em C2 |
| (ISC)² | International Information Systems Security Certification Consortium | Consórcio internacional de certificação em segurança |
| ISE | Identity Services Engine | Solução da Cisco de identidade e controle de acesso |
| ISMS | Information Security Management System | Sistema de gerenciamento de segurança da informação |
| ISO | International Organization for Standardization | Organização Internacional de Normalização |
| LAN | Local Area Network | Rede local |
| LGPD | Lei Geral de Proteção de Dados | Lei brasileira de proteção de dados pessoais |
| MAC | Media Access Control | Endereço físico da placa de rede |
| MDM | Mobile Device Management | Gerenciamento de dispositivos móveis |
| MISP | Malware Information Sharing Platform | Plataforma aberta de compartilhamento de IOCs |
| MS-ISAC | Multi-State Information Sharing and Analysis Center | Centro de compartilhamento de informações dos governos estaduais dos EUA |
| MTBF | Mean Time Between Failures | Tempo médio entre falhas |
| MTTF | Mean Time To Failure | Tempo médio até a falha |
| MTTR | Mean Time To Repair | Tempo médio de reparo |
| NBA | Network Behavior Analysis | Análise de comportamento de rede |
| NIST | National Institute of Standards and Technology | Instituto Nacional de Padrões e Tecnologia dos EUA |
| NISTIR | NIST Interagency Report | Relatório interagências do NIST |
| NVD | National Vulnerability Database | Banco de dados nacional de vulnerabilidades |
| OSPF | Open Shortest Path First | Protocolo de roteamento dinâmico |
| OSI | Open Systems Interconnection | Modelo de referência em sete camadas |
| PCI DSS | Payment Card Industry Data Security Standard | Padrão de segurança dos dados de cartões de pagamento |
| PIA | Privacy Impact Assessment | Avaliação de impacto à privacidade |
| PII | Personally Identifiable Information | Informações de identificação pessoal |
| PR | Privileges Required | Privilégios necessários, métrica do CVSS |
| RAM | Random Access Memory | Memória volátil do computador |
| RFC | Request for Comments | Documento de padrões da internet |
| RPO | Recovery Point Objective | Objetivo de ponto de recuperação |
| RTO | Recovery Time Objective | Objetivo de tempo de recuperação |
| SANS | SysAdmin, Audit, Network, Security | Instituto de pesquisa e treinamento em segurança |
| SCCM | System Center Configuration Manager | Ferramenta da Microsoft de distribuição de patches |
| SECaaS | Security as a Service | Segurança como serviço |
| SEM | Security Event Management | Gerenciamento de eventos de segurança |
| SIEM | Security Information and Event Management | Gerenciamento de eventos e informações de segurança |
| SIIA | Software and Information Industry Association | Associação da indústria de software e informação |
| SIM | Security Information Management | Gerenciamento de informações de segurança |
| SLE | Single Loss Expectancy | Expectativa de perda única |
| SLTT | State, Local, Tribal and Territorial | Governos estaduais, locais, tribais e territoriais dos EUA |
| SOA | Statement of Applicability | Declaração de aplicabilidade |
| SOAR | Security Orchestration, Automation and Response | Orquestração, automação e resposta de segurança |
| SOC | Security Operations Center | Centro de operações de segurança |
| SOC 2 | Service Organization Control 2 | Relatório de auditoria dos controles de um provedor |
| SOP | Standard Operating Procedure | Procedimento operacional padrão |
| SOX | Sarbanes-Oxley Act | Lei americana sobre controles financeiros das empresas |
| SP | Special Publication | Publicação especial do NIST |
| SSAE | Statement on Standards for Attestation Engagements | Norma de auditoria de atestação |
| ST&E | Security Test and Evaluation | Teste e avaliação de segurança |
| STIX | Structured Threat Information Expression | Formato padrão de informações sobre ameaças |
| SYN | Synchronize | Bit de início de conexão do TCP |
| TAXII | Trusted Automated Exchange of Indicator Information | Protocolo de transporte de CTI sobre HTTPS |
| TCP | Transmission Control Protocol | Protocolo de transporte confiável |
| TI | Tecnologia da Informação | Área de tecnologia da empresa |
| TIP | Threat Intelligence Platform | Plataforma de inteligência de ameaças |
| TTP | Tactics, Techniques and Procedures | Táticas, técnicas e procedimentos dos atacantes |
| T-V | Threat-Vulnerability | Par ameaça-vulnerabilidade |
| UDP | User Datagram Protocol | Protocolo de transporte sem conexão |
| UEBA | User and Entity Behavior Analytics | Análise de comportamento de usuários e entidades |
| UI | User Interaction | Interação do usuário, métrica do CVSS |
| US-CERT | United States Computer Emergency Readiness Team | Equipe de resposta a emergências do governo dos EUA |
| VERIS | Vocabulary for Event Recording and Incident Sharing | Vocabulário e banco comunitário de incidentes |
| VPPA | Video Privacy Protection Act | Lei americana de privacidade do histórico de vídeos |
| WAN | Wide Area Network | Rede de longa distância |

## Exercícios

### A. Análise Quantitativa de Riscos (ver item 4.5)

1. Um servidor vale US$ 40.000. Um ataque destrói metade do seu valor e deve ocorrer uma vez a cada cinco anos. Calcule o EF, a SLE, a ARO e a ALE.
2. A empresa perde em média três notebooks de US$ 2.000 por ano, sem recuperação. Calcule a SLE e a ALE.
3. Um data center de US$ 1.000.000 perde 60% do valor em uma inundação, que ocorre em média uma vez a cada 50 anos. Calcule a ALE e informe se vale a pena pagar US$ 15.000 por ano por uma proteção contra inundações.
4. Calcule a ALE de cada risco e ordene-os da maior para a menor prioridade.

| Risco | Valor do ativo | EF | ARO |
| --- | --- | --- | --- |
| Falha da fonte do servidor | US$ 3.000 | 100% | 0,3 |
| Ataque ao servidor web | US$ 60.000 | 40% | 0,25 |
| Roubo de notebooks | US$ 1.500 | 100% | 3 |
| Falha de disco do banco de dados | US$ 25.000 | 100% | 0,5 |

### B. Notas e Vetores do CVSS (ver itens 11.4 e 11.5)

1. Classifique as notas 0; 3,9; 4,0; 7,5 e 9,8.
2. Informe quais das vulnerabilidades do item anterior devem ser corrigidas, pela regra geral.
3. Leia a string `CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H`.
4. Escreva a parte base da string de uma vulnerabilidade explorável pela rede, de baixa complexidade, sem privilégios, sem interação do usuário, com escopo inalterado e alto impacto na confidencialidade, na integridade e na disponibilidade.

### C. Alarme por Contagem de Fluxos (ver item 7.3.1)

1. Com X = 10, Y = 50, Z = 20 e N = 300, escreva a regra do algoritmo em palavras.
2. Com essa regra, a amostra registrou 350 fluxos. Informe o que acontece.
3. Na amostra seguinte, foram 280 fluxos. Informe o que acontece.

### D. Medidas de Continuidade (ver item 17.3)

1. Uma empresa faz backup a cada 6 horas. Informe a perda máxima de dados se o servidor falhar logo antes do próximo backup.
2. O RPO de um sistema é de 2 horas. Informe com que frequência mínima os backups devem ser feitos.
3. O RTO de um sistema é de 4 horas e ele foi restaurado em 6 horas. Informe se o objetivo foi cumprido.
4. Um disco falha em média a cada 10.000 horas e leva 5 horas para ser trocado. Informe o MTBF e o MTTR.

### E. Questões Conceituais: Governança, Ética e Leis

1. Diferencie governança de gerenciamento de segurança de TI.
2. Indique a função de cada um na governança de dados: quem atribui a classificação e quem implementa os controles.
3. Classifique as políticas em mestra, específica do sistema ou específica do problema: política de uso aceitável de e-mail; configuração do firewall; Política de Segurança Cibernética.
4. Classifique os crimes em contra o computador, assistido por computador ou incidental ao computador: um ataque DoS; uma fraude bancária online; um computador com registros de tráfico de drogas.
5. Indique a lei americana correspondente: privacidade de crianças menores de 13 anos; acesso a registros escolares; proibição de acesso não autorizado a sistemas.
6. Diferencie objetivos de controle (ISO 27001) e controles (ISO 27002).
7. Diferencie o relatório SOC 2 Tipo I do Tipo II.

### F. Questões Conceituais: Riscos e Controles

1. Ordene negligência, devido cuidado e devida diligência do maior para o menor risco.
2. Classifique as fontes de ameaça: um incêndio; um funcionário que apaga um arquivo por engano; um grupo de hackers; um disco que queima.
3. Indique a resposta ao risco: contratar um seguro; deixar de oferecer um serviço vulnerável; instalar um firewall; conviver com um risco de baixo impacto.
4. Classifique os controles por função: backup e restauração; câmera visível; IDS; privilégios por usuário; detector de movimento com som de latidos no lugar de um cão de guarda.
5. Explique o que é o perfil de risco inerente e como os pares T-V o formam.

### G. Questões Conceituais: Inteligência e Vulnerabilidades

1. Diferencie STIX de TAXII.
2. Indique a função do CVE e a do NVD.
3. Diferencie IOC de TTP.
4. Explique por que os backups de servidor entram na linha de base e o tráfego de um servidor já levado para a nuvem não entra.
5. Diferencie avaliação de vulnerabilidades de teste de penetração.
6. Diferencie varredura credenciada de não credenciada e falso positivo de falso negativo.
7. Diferencie teste de caixa preta, cinza e branca.
8. Indique a equipe de um exercício: o árbitro; os atacantes; os defensores; as duas equipes trabalhando juntas.
9. Indique a técnica de aplicação de patches mais indicada para dispositivos móveis e explique por quê.

### H. Questões Conceituais: Ataques e Resposta

1. Ordene as sete etapas da Cyber Kill Chain e explique por que é melhor interromper o ataque cedo.
2. Indique a etapa da Cyber Kill Chain: um webshell instalado no servidor; um e-mail com anexo malicioso; uma varredura de portas; tráfego excessivo para um domínio de DNS dinâmico.
3. Indique os quatro elementos do Modelo Diamond e como eles se relacionam.
4. Ordene a coleta das evidências pela volatilidade: backup em fita; RAM; disco rígido; cache ARP.
5. Explique por que a análise forense é feita em cópias bit a bit.
6. Diferencie precursor de indicador e dê um exemplo de cada.
7. Ordene as quatro fases do ciclo de resposta a incidentes do NIST.
8. Explique por que nem sempre é bom desconectar da rede um host comprometido.
9. Diferencie DRP de BCP.
10. Ordene os exercícios de mesa, funcional e operacional do mais simples ao mais completo.

## Gabarito

### A. Análise Quantitativa de Riscos

1. EF = **0,5 (50%)**; SLE = US$ 40.000 × 0,5 = **US$ 20.000**; ARO = 1 ÷ 5 = **0,2**; ALE = US$ 20.000 × 0,2 = **US$ 4.000 por ano**.
2. SLE = US$ 2.000 × 1,0 = **US$ 2.000**; ALE = US$ 2.000 × 3 = **US$ 6.000 por ano**.
3. SLE = US$ 1.000.000 × 0,6 = US$ 600.000; ARO = 1 ÷ 50 = 0,02; ALE = **US$ 12.000 por ano**. A proteção de US$ 15.000 por ano **não compensa**, porque custa mais do que a perda anual esperada.
4. As ALEs são:

| Risco | SLE | ALE | Prioridade |
| --- | --- | --- | --- |
| Falha de disco do banco de dados | US$ 25.000 | **US$ 12.500** | 1 |
| Ataque ao servidor web | US$ 24.000 | **US$ 6.000** | 2 |
| Roubo de notebooks | US$ 1.500 | **US$ 4.500** | 3 |
| Falha da fonte do servidor | US$ 3.000 | **US$ 900** | 4 |

### B. Notas e Vetores do CVSS

1. 0 = **nenhuma**; 3,9 = **baixa**; 4,0 = **média**; 7,5 = **alta**; 9,8 = **crítica**.
2. As de **4,0, 7,5 e 9,8**, porque toda vulnerabilidade **acima de 3,9** deve ser corrigida, começando pela de nota maior.
3. Ataque **local**, complexidade **alta**, **nenhum** privilégio necessário, interação do usuário **necessária**, escopo **alterado** e impacto **alto** na confidencialidade, na integridade e na disponibilidade.
4. **`AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`**.

### C. Alarme por Contagem de Fluxos

1. A cada **10 minutos**, amostrar **1 de cada 50 fluxos** durante **20 segundos**; se houver **mais de 300 fluxos**, gerar um alarme.
2. 350 > 300 → **gera o alarme**.
3. 280 ≤ 300 → **não faz nada**.

### D. Medidas de Continuidade

1. Até **6 horas de dados**.
2. Pelo menos **a cada 2 horas**.
3. **Não**: o sistema ficou 6 horas parado, 2 horas além do RTO.
4. MTBF = **10.000 horas**; MTTR = **5 horas**.

### E. Questões Conceituais: Governança, Ética e Leis

1. A governança **decide** quem toma as decisões sobre os riscos e alinha a segurança aos objetivos do negócio; o gerenciamento **define e implementa os controles**.
2. O **proprietário dos dados** atribui a classificação; o **custodiante** implementa os controles.
3. Uso aceitável de e-mail = **específica do problema**; configuração do firewall = **específica do sistema**; Política de Segurança Cibernética = **mestra**.
4. DoS = **contra o computador**; fraude bancária = **assistido por computador**; registros de tráfico = **incidental ao computador**.
5. **COPPA**; **FERPA**; **CFAA**.
6. Os objetivos de controle definem os **requisitos de alto nível** e servem de lista na auditoria; os controles dizem **como atingir** esses objetivos.
7. O Tipo I confirma que os controles **existem em um momento**; o Tipo II, que **funcionam por pelo menos seis meses**.

### F. Questões Conceituais: Riscos e Controles

1. **Negligência** (risco alto) → **devido cuidado** (menor) → **devida diligência** (aceitável).
2. Incêndio = **ambiental**; arquivo apagado por engano = **acidental**; hackers = **adversarial**; disco queimado = **estrutural**.
3. Seguro = **transferir**; deixar o serviço = **evitar**; firewall = **reduzir**; risco de baixo impacto = **aceitar**.
4. Backup = **recuperação**; câmera visível = **dissuasivo**; IDS = **detecção**; privilégios = **preventivo**; detector com latidos = **compensatório**.
5. É o **risco antes dos controles**. Cada ameaça é associada à vulnerabilidade que explora (par T-V), e o conjunto dos pares forma a linha de base usada para medir a eficácia dos controles.

### G. Questões Conceituais: Inteligência e Vulnerabilidades

1. O STIX é o **formato** da informação sobre ameaças; o TAXII é o **protocolo que a transporta** sobre HTTPS.
2. O CVE dá o **identificador único** de cada vulnerabilidade; o NVD usa esse identificador e acrescenta **nota CVSS e detalhes técnicos**.
3. O IOC é o **vestígio** de que um ataque ocorreu; as TTPs descrevem **como o atacante age**.
4. Os backups fazem parte da **operação normal** atual; o tráfego do servidor que foi para a nuvem **deixou de ser normal**, e a linha de base precisa estar atualizada.
5. A avaliação **encontra** as vulnerabilidades; o teste de penetração **as explora** para medir o impacto.
6. A credenciada **entra no sistema** com usuário e senha e erra menos; a não credenciada mostra a **visão de fora**. O falso positivo aponta uma vulnerabilidade **inexistente**; o falso negativo **deixa passar** uma real.
7. Caixa preta: **nenhum conhecimento**, mais barato; caixa cinza: **conhecimento limitado**; caixa branca: **conhecimento completo**, mais caro.
8. Árbitro = **branca**; atacantes = **vermelha**; defensores = **azul**; juntas = **roxa**.
9. A **baseada em agente**, porque o agente no aparelho fala com o servidor de patches mesmo fora dos segmentos de rede varridos.

### H. Questões Conceituais: Ataques e Resposta

1. **Reconhecimento → armamento → entrega → exploração → instalação → comando e controle → ações nos objetivos**. Quanto mais cedo a cadeia é rompida, **menor o dano** e menos o atacante aprende sobre a rede.
2. Webshell = **instalação**; anexo malicioso = **entrega**; varredura de portas = **reconhecimento**; tráfego para DNS dinâmico = **comando e controle**.
3. **Adversário, capacidade, infraestrutura e vítima**: o adversário usa a infraestrutura para se conectar à vítima e desenvolve a capacidade para explorá-la.
4. **RAM e cache ARP** (os mais voláteis, na mesma faixa da ordem de coleta) → **disco rígido** → **backup em fita**.
5. Para **não alterar a prova original**, inclusive os carimbos de hora, e poder comparar a cópia investigada com a original e provar que não houve adulteração.
6. O precursor indica que um incidente **pode ocorrer**, como uma varredura de portas; o indicador mostra que ele **já ocorreu ou está ocorrendo**, como um alerta do IDS.
7. **Preparação → detecção e análise → contenção, erradicação e recuperação → atividade pós-incidente**.
8. O malware pode perceber a perda do contato com o C2 e **apagar ou criptografar os dados**.
9. O DRP **avalia, recupera e restaura** os ativos durante o desastre; o BCP é **mais amplo** e mantém a empresa funcionando, inclusive **em outro local**.
10. **Mesa → funcional → operacional**.
