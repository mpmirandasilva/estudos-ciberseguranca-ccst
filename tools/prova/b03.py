Q(51,3,'Antes de distribuir um novo patch do sistema operacional, você quer testá-lo em um ambiente seguro e isolado. Qual tecnologia oferece isso?',
 ['Máquina virtual','Honeypot','Rede em quarentena','Zona desmilitarizada (DMZ)'],[0],
 'A máquina virtual funciona como uma área isolada (sandbox): dá para aplicar o patch, testar e descartar ou voltar a um snapshot sem afetar os computadores reais. O honeypot é uma isca para atacantes, a quarentena isola máquinas suspeitas e a DMZ hospeda serviços públicos.',
 ['defesa:25.1','endpoint:26.3','endpoint:29.3'])
Q(52,4,'A sede de uma empresa fica em uma região que já sofreu vários furacões e enchentes, e a empresa contrata um seguro contra desastres. Que estratégia de risco é essa?',
 ['Controle (redução) do risco','Transferência do risco','Aceitação do risco','Prevenção (evitar) o risco'],[1],
 'Com o seguro, a perda financeira passa para a seguradora: é transferência do risco. Reduzir seria, por exemplo, elevar o prédio; evitar seria mudar a sede; aceitar seria não fazer nada e arcar com a perda.',
 ['ameacas:4.6','endpoint:2.3'])
Q(53,5,'Que plano é amplo e define como manter as funções críticas do negócio funcionando durante um desastre?',
 ['Plano de resposta a incidentes','Plano de segurança cibernética','Plano de continuidade de negócios','Plano de compra de infraestrutura'],[2],
 'O plano de continuidade de negócios (BCP) é o mais amplo: mantém a empresa operando durante e depois do desastre, inclusive em outro local. O plano de recuperação de desastres é parte dele e trata de restaurar os sistemas.',
 ['ameacas:17.3','ameacas:17.2'])
Q(54,1,'Quais são os três componentes do AAA na segurança cibernética? (Escolha 3.)',
 ['Autenticação','Automação','Autenticidade','Autorização','Contabilidade (accounting)'],[0,3,4],
 'AAA significa autenticação (quem é você), autorização (o que você pode fazer) e contabilidade ou registro (o que você fez e por quanto tempo).',
 ['defesa:9.2','endpoint:17.6','defesa:12.1'])
Q(55,4,'A MITRE Corporation mantém um catálogo de vulnerabilidades conhecidas. Qual é o nome dele?',
 ['TAXII','STIX','CybOX','CVE'],[3],
 'O CVE (Common Vulnerabilities and Exposures) é o dicionário de identificadores das vulnerabilidades publicamente conhecidas, mantido pela MITRE. STIX, TAXII e CybOX são padrões de troca de inteligência.',
 ['ameacas:6.4','ameacas:11.6'])
M(56,2,'Relacione cada ataque à sua descrição.',
 [('Falsificação de IP','Altera os pacotes com um IP de origem falso para se passar por outro computador'),('Falsificação de ARP','Envia mensagens ARP falsas para associar o MAC do atacante a um IP legítimo'),('Ping flood','Tenta sobrecarregar o alvo com pacotes de solicitação de eco'),('Previsão de sequência TCP','Tenta prever os números de sequência do TCP para inserir pacotes falsos na conexão'),('Varredura de portas','Identifica portas abertas e fechadas em dispositivos conectados')],None,
 'Spoofing de IP falsifica a origem; envenenamento de ARP engana a tabela IP–MAC; ping flood é um DoS com ICMP; a previsão de sequência é a base do sequestro de sessão TCP; a varredura de portas é reconhecimento.',
 ['endpoint:7.7','endpoint:9.2','endpoint:7.5','endpoint:8.3','defesa:15.1'])
Q(57,4,'Qual termo designa o dicionário de nomes comuns das vulnerabilidades publicamente conhecidas?',
 ['AIS','CVE','CVSS','STIX'],[1],
 'O CVE dá um identificador único a cada vulnerabilidade (por exemplo, CVE-2024-12345), para que todos falem da mesma falha. O CVSS dá a nota de gravidade, o STIX descreve ameaças e o AIS distribui indicadores.',
 ['ameacas:6.4','ameacas:11.6'])
Q(58,5,'Houve um incêndio no data center da organização. Qual documento a equipe de segurança vai consultar?',
 ['Política de segurança da informação','Especificação de controles preventivos','Plano de recuperação de desastres','Objetivo de ponto de recuperação (RPO)'],[2],
 'O plano de recuperação de desastres (DRP) define como avaliar, recuperar e restaurar as instalações e os sistemas depois de um evento destrutivo. O RPO é uma medida usada dentro desses planos, não um documento.',
 ['ameacas:17.2','ameacas:17.1'])
Q(59,3,'Você quer que o tcpdump capture um número definido de pacotes. Qual opção usar?',
 ['tcpdump -n','tcpdump -a','tcpdump -c','tcpdump -i'],[2],
 'A opção -c (count) define quantos pacotes capturar. O -n evita a resolução de nomes, e o -i escolhe a interface de rede. O tcpdump é o analisador de pacotes de linha de comando, primo do Wireshark.',
 ['ameacas:9.7','defesa:3.4','endpoint:22.3'])
Q(60,2,'Quais dois componentes são necessários para os clientes se conectarem a uma rede sem fio com WPA2-Enterprise? (Escolha 2.)',
 ['Servidor RADIUS','WEP','SSID','PSK'],[0,2],
 'O SSID identifica a rede para a associação, e o modo Enterprise usa 802.1X com um servidor RADIUS para autenticar cada usuário. A PSK (senha compartilhada) é do modo Personal, e o WEP é um protocolo antigo e inseguro.',
 ['endpoint:15.3','endpoint:15.5','defesa:17.2'])
Q(61,1,'Que ataque mira um grupo específico de usuários, infectando um site que eles costumam visitar?',
 ['Vishing','Whaling','Watering hole','Pharming'],[2],
 'No watering hole ("bebedouro"), o atacante infecta um site frequentado pelo grupo-alvo e espera as vítimas chegarem. O pharming redireciona para um site falso, o whaling mira executivos e o vishing usa o telefone.',
 ['endpoint:4.5','endpoint:6.8'])
Q(62,3,'Que tipo de detecção de malware depende de um banco de definições (arquivos DAT) atualizado?',
 ['Área restrita (sandbox)','Verificação de integridade','Detecção por assinatura','Detecção por heurística'],[2],
 'A detecção por assinatura compara os arquivos com um banco de "impressões" de malware conhecido, por isso precisa de atualização constante e não pega ameaças novas. A heurística analisa comportamento, e a sandbox executa o arquivo suspeito em ambiente isolado.',
 ['endpoint:12.2','endpoint:28.3','endpoint:27.3'])
Q(63,5,'Em que fase do ciclo de resposta a incidentes do NIST se monta o kit de salto (jump kit)?',
 ['Atividade pós-incidente','Contenção, erradicação e recuperação','Detecção e análise','Preparação'],[3],
 'O kit de salto é a caixa com notebook, software de análise, mídias de backup e outros itens para uma resposta rápida. Ele é montado na preparação, antes de qualquer incidente.',
 ['ameacas:16.5','ameacas:16.4'])
Q(64,3,'Você quer tirar as permissões de gravação e execução de todos, menos do dono do arquivo. Qual comando faz isso?',
 ['chmod a-wx arquivo','chmod og=wx arquivo','chmod a=r arquivo','chmod og-wx arquivo'],[3],
 'No chmod, u é o dono, g o grupo, o os outros e a todos. "og-wx" remove (-) gravação (w) e execução (x) do grupo e dos outros, sem mexer no dono. "a-wx" tiraria do dono também, e "=" substitui as permissões em vez de remover.',
 ['endpoint:24.3'])
Q(65,5,'Sua equipe precisa reforçar os controles preventivos do plano de recuperação de desastres. O que fazer?',
 ['Configurar o antimalware dos hosts para enviar logs a um servidor central.','Fazer treinamento de segurança com os usuários finais.','Implantar um servidor syslog para reforçar o perímetro.','Criar um plano de continuidade de negócios.'],[1],
 'Controles preventivos evitam que o desastre aconteça. O treinamento reduz a chance de um usuário causar um incidente por engano. Enviar logs a um servidor central é controle de detecção, e o plano de continuidade é um plano, não um controle preventivo.',
 ['ameacas:17.2','endpoint:30.3','ameacas:5.2'])
Q(66,2,'Qual tecnologia permite oferecer serviços a uma rede não confiável (a internet) sem comprometer a rede interna?',
 ['VLAN','DMZ','DHCP','VPN'],[1],
 'A DMZ (zona desmilitarizada) é uma rede intermediária entre a internet e a rede interna, onde ficam os servidores públicos. Se um deles for invadido, o firewall ainda separa a rede interna.',
 ['defesa:16.2','endpoint:16.2'])
M(67,2,'Relacione cada tecnologia de acesso seguro ao seu caso de uso.',
 [('Firewall','Impedir que tráfego malicioso entre na rede privada'),('NAC','Aplicar políticas aos usuários e dispositivos que entram na rede'),('VPN','Proteger o tráfego que passa por uma rede não segura')],None,
 'O firewall filtra o tráfego por regras. O NAC (controle de admissão/acesso à rede) verifica se o dispositivo cumpre a política antes de liberar o acesso. A VPN cria um túnel cifrado sobre uma rede insegura, como a internet.',
 ['defesa:10.4','endpoint:16.1','endpoint:17.7'])
Q(68,1,'Que tipo de atacante usa principalmente código e ferramentas prontas, feitas por outros?',
 ['Script kiddie','Concorrente','Hacktivista','Criminoso'],[0],
 'O script kiddie tem pouco conhecimento técnico e roda ferramentas e scripts prontos. Hacktivistas agem por causas políticas ou sociais, e criminosos buscam lucro, muitas vezes com bastante habilidade.',
 ['endpoint:2.6','endpoint:2.7'])
Q(69,1,'Você recebe um e-mail que parece do seu professor, clica no link e faz logon em uma página igual à do portal da escola. Depois descobre que era phishing e que suas credenciais foram roubadas. Qual parte da tríade CIA foi comprometida?',
 ['Disponibilidade','Integridade','Confidencialidade'],[2],
 'As credenciais foram parar nas mãos de quem não deveria tê-las: violação da confidencialidade.',
 ['endpoint:1.2','endpoint:6.8'])
Q(70,2,'Por que implementar o controle de admissão (acesso) à rede (NAC)?',
 ['Para aplicar a política de segurança aos dispositivos que entram na rede.','Para proteger os switches de ataques de estouro da tabela MAC.','Para impedir a entrada de tráfego malicioso na rede privada.','Para proteger o tráfego entre dois pontos que passa por uma rede insegura.'],[0],
 'O NAC verifica a postura do dispositivo (antivírus, patches, configuração) e só libera o acesso se ele cumprir a política. Bloquear tráfego é papel do firewall, proteger o tráfego em trânsito é papel da VPN e o estouro da tabela MAC é tratado com port security.',
 ['defesa:10.4'])
M(71,1,'Relacione cada termo à definição correta.',
 [('Ameaça','Ataque malicioso em potencial que busca acessar dados, interromper operações ou danificar informações'),('Vetor de ataque','Caminho ou método que o hacker usa para acessar uma rede ou um computador'),('Exploração','Ataque feito para aproveitar um ponto fraco do computador'),('Vulnerabilidade','Ponto fraco de um sistema que pode ser usado para comprometê-lo')],None,
 'A vulnerabilidade é a fraqueza, a ameaça é o perigo em potencial, o vetor é o caminho e a exploração é o ato de aproveitar a fraqueza.',
 ['endpoint:2.2','endpoint:2.4','defesa:1.2'])
Q(72,4,'Qual organização mantém a lista CVE, o dicionário de vulnerabilidades publicamente conhecidas?',
 ['Instituto SANS','FIRST','Cisco Talos','MITRE Corporation'],[3],
 'A MITRE mantém o CVE e também o ATT&CK. O SANS oferece treinamentos e o Internet Storm Center, o FIRST reúne equipes de resposta a incidentes e cuida do CVSS, e o Talos é a equipe de inteligência da Cisco.',
 ['ameacas:6.4','ameacas:6.1'])
Q(73,2,'O que permite o acesso à rede sem fio de casa apenas a dispositivos específicos?',
 ['Ocultar o SSID','Firewall','WEP','Filtragem de MAC'],[3],
 'A filtragem de MAC permite ou nega a associação pelo endereço físico de cada aparelho. É uma proteção fraca, porque o MAC pode ser falsificado, mas é o recurso que restringe por dispositivo.',
 ['endpoint:15.1','fundamentos:7.8'])
Q(74,1,'Uma funcionária faz logon com credenciais válidas, mas o sistema bloqueia o acesso a uma pasta restrita ao financeiro. Qual princípio está sendo aplicado?',
 ['Autorização','Criptografia','Disponibilidade','Auditoria de rede'],[0],
 'Ela foi autenticada (as credenciais são válidas), mas a autorização define o que cada pessoa pode acessar depois de entrar. Como ela não tem permissão para a pasta, o acesso é negado.',
 ['defesa:9.6','defesa:11.4','defesa:10.2'])
M(75,3,'Complete as frases com o tipo de malware.',
 [('Código que se propaga sozinho para outros sistemas pela rede e consome recursos, podendo causar negação de serviço:','worm'),('Código que se replica no computador e se espalha causando danos e distribuindo outros conteúdos prejudiciais:','vírus'),('Programa que parece útil ou inofensivo, mas esconde código que compromete o sistema:','cavalo de Troia')],['cavalo de Troia','vírus','worm'],
 'O worm se propaga sozinho pela rede, sem precisar de um hospedeiro. O vírus se anexa a arquivos e se replica. O cavalo de Troia se disfarça de programa legítimo.',
 ['endpoint:5.1'])
