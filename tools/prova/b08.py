Q(176,4,'Qual recurso de segurança permite observar os possíveis hackers e estudar seus métodos e ações?',
 ['NAT','VPN','Firewall','Honeypot'],[3],
 'O honeypot atrai os atacantes para um ambiente de isca, onde as ações deles são registradas sem afetar os sistemas reais.',
 ['defesa:19.6','ameacas:6.6'])
Q(177,1,'Quais dois estados dos dados exigem criptografia e hash para protegê-los? (Escolha 2.)',
 ['Dados em trânsito','Dados em uso','Dados em repouso','Dados na criação'],[0,2],
 'Os dados em repouso (armazenados) e em trânsito (sendo transmitidos) são protegidos com criptografia (confidencialidade) e hash (integridade). Os dados em uso (em processamento) precisam estar decifrados na memória para serem processados, por isso dependem de outros controles.',
 ['endpoint:1.5','endpoint:1.6','defesa:5.2'])
M(178,3,'Complete a frase: "No Windows, ____ é quando o invasor usa uma vulnerabilidade para obter níveis de acesso mais altos em um host."',
 [('Termo','Escalação (elevação) de privilégio')],['PowerShell','Escalação (elevação) de privilégio','Serviço de atualização do servidor','Restauração do sistema'],
 'Na elevação de privilégio, o atacante começa com acesso limitado e explora uma falha para se tornar administrador ou SYSTEM. O privilégio mínimo reduz o estrago quando isso acontece.',
 ['defesa:10.2','endpoint:6.4'])
M(179,4,'Complete a frase: "Testar uma vulnerabilidade procurando pontos fracos para acessar a rede é chamado de ____."',
 [('Termo','varredura de portas')],['varredura de portas','phishing','mapeamento de rede','verificação de vírus'],
 'A varredura de portas sonda os hosts em busca de portas abertas, que indicam serviços que podem ser explorados.',
 ['defesa:15.1','ameacas:9.3'])
Q(180,3,'Um usuário erra o logon no servidor de e-mail Linux da empresa. Em qual arquivo o evento é registrado?',
 ['/var/log/cron','/var/log/maillog','/var/log/secure','/var/log/messages'],[2],
 'O /var/log/secure (no Red Hat e no CentOS) registra autenticação e autorização, inclusive logons com falha. No Debian e no Ubuntu, o equivalente é o /var/log/auth.log.',
 ['endpoint:23.3'])
Q(181,1,'Qual algoritmo de criptografia simétrica oferece a proteção mais forte?',
 ['3DES','DES','AES','Diffie-Hellman'],[2],
 'O AES é o padrão simétrico recomendado hoje, com chaves de 128, 192 ou 256 bits. O DES é inseguro, o 3DES está em desuso e o Diffie-Hellman não cifra dados: serve para trocar chaves.',
 ['defesa:5.3','defesa:5.7'])
Q(182,3,'A empresa entrega tablets aos funcionários, e a política exige que cada dispositivo tenha um identificador único para ser rastreado. O que ajuda a cumprir a política?',
 ['Software de firewall','Etiquetas RFID','Filtragem de MAC','Software MDM'],[3],
 'O MDM (gerenciamento de dispositivos móveis) registra cada aparelho no inventário e permite aplicar políticas, localizar, bloquear e apagar remotamente.',
 ['ameacas:12.3','defesa:17.5'])
Q(183,1,'Você descobre um malware que coleta dados e os envia a um servidor em outro país há vários meses. Que tipo de ataque é esse?',
 ['Dia zero','Negação de serviço distribuída','Ameaça persistente avançada (APT)','Ransomware'],[2],
 'Ficar escondido por meses roubando dados é a marca da APT: presença longa e discreta, com objetivo de espionagem ou roubo de informações.',
 ['endpoint:3.7'])
Q(184,3,'Que tipo de ferramenta antimalware identifica atividades maliciosas pelo comportamento?',
 ['Detecção por heurística','Área restrita (sandbox)','Detecção por assinatura','Verificação de integridade'],[0],
 'A detecção heurística usa regras que descrevem comportamento suspeito e por isso consegue pegar ameaças novas, sem assinatura. Em troca, gera mais falsos positivos.',
 ['endpoint:27.3','endpoint:28.3'])
Q(185,3,'Você precisa impedir que usuários não autorizados leiam um arquivo específico em um notebook. O que implementar?',
 ['DFS (sistema de arquivos distribuído)','EFS (Encrypting File System)','BitLocker','Criptografia AES'],[1],
 'O EFS, recurso do NTFS, criptografa arquivos e pastas individuais, ligados à conta do usuário. O BitLocker criptografa o disco inteiro (protege contra roubo do aparelho, não contra outros usuários do mesmo computador).',
 ['endpoint:26.5','endpoint:19.3'])
Q(186,3,'O computador Windows infectado já está em quarentena e desconectado da rede. Qual é o próximo passo para remover o malware e evitar que ele volte?',
 ['Desativar a restauração do sistema.','Reconectar à rede e rodar uma varredura completa a partir do servidor.','Iniciar o Windows em modo de segurança.','Instalar e rodar um antimalware atualizado.'],[0],
 'O malware costuma contaminar os pontos de restauração. Se a restauração do sistema continuar ativa, um ponto infectado pode trazer o malware de volta. Por isso ela é desativada antes da limpeza (e reativada depois, com um ponto novo e limpo).',
 ['endpoint:26.2','endpoint:12.2'])
Q(187,1,'Qual termo descreve o caminho usado para acessar ilegalmente um sistema?',
 ['Botnet','Vetor de ataque','Ataque criptográfico','Firewall'],[1],
 'O vetor de ataque é o caminho ou método de entrada: e-mail, site, pen drive, porta aberta, credencial roubada.',
 ['endpoint:2.4','ameacas:4.3'])
M(188,5,'Relacione cada solução de segurança à sua descrição.',
 [('SIEM','Analisa e agrega logs de diferentes sistemas para identificar ameaças'),('SOAR','Automatiza operações de segurança, inteligência de ameaças e resposta a incidentes'),('SCAP','Automatiza a avaliação de conformidade e o gerenciamento de vulnerabilidades')],None,
 'O SIEM correlaciona logs; o SOAR orquestra e automatiza a resposta; o SCAP (Security Content Automation Protocol) é um conjunto de padrões do NIST para verificar configurações e vulnerabilidades de forma automática.',
 ['defesa:29.5','defesa:29.6','ameacas:12.4'])
Q(189,2,'Um invasor derruba um servidor enviando mais pedidos GET do que ele consegue processar. Que ataque é esse?',
 ['Inundação HTTP (HTTP flood)','Inundação de SYN','Falsificação de IP','Falsificação de ARP'],[0],
 'O HTTP flood é um DoS na camada de aplicação: pedidos HTTP aparentemente normais, em quantidade enorme. A inundação de SYN atua na camada de transporte, antes de a conexão se completar.',
 ['endpoint:5.4','endpoint:11.1'])
Q(190,3,'Quais são as permissões padrão de arquivo no Linux, segundo a apostila?',
 ['rw-rw-rw-','rw-rwx-','rwx-r-r','rwx-rwx-rwx'],[0],
 'Os arquivos novos partem de rw-rw-rw- (666): leitura e gravação para dono, grupo e outros, sem execução. Na prática, a máscara (umask, geralmente 022) retira permissões e o resultado costuma ser rw-r--r-- (644). A prova cobra o valor base.',
 ['endpoint:24.3'])
Q(191,3,'O que é spyware?',
 ['Programa que coleta informações sobre usuários, sistemas e hábitos de navegação.','Programa que se replica alterando o sistema ou os aplicativos.','Programa que previne, detecta e remove vírus.','Programa malicioso escondido dentro de um programa útil.'],[0],
 'O spyware espiona: coleta dados do usuário e envia ao atacante. Replicar-se é característica do vírus, esconder-se em programa útil é o cavalo de Troia, e remover vírus é o antivírus.',
 ['endpoint:5.3','endpoint:5.1'])
Q(192,4,'Qual organização oferece treinamento de segurança, certificações e recursos gratuitos de notícias?',
 ['Instituto SANS','Cisco Talos','MITRE Corporation','FIRST'],[0],
 'O SANS oferece cursos e certificações e muitos recursos gratuitos: o Internet Storm Center, o NewsBites, o resumo @RISK e alertas.',
 ['ameacas:6.1'])
Q(193,3,'Você quer testar um novo patch, com receio de que ele contenha código malicioso, antes de distribuí-lo para a empresa toda. Qual tecnologia usar?',
 ['Computação em nuvem','Controle de aplicativos','Virtualização','Backup'],[2],
 'A virtualização permite reproduzir vários ambientes de produção em um só computador, isolados, e observar o comportamento do patch sem colocar as máquinas reais em risco.',
 ['defesa:25.1','endpoint:26.3','endpoint:29.3'])
M(194,3,'Verdadeiro ou falso: "Dá para usar o netstat para examinar o UDP sobre IPv6."',
 [('A afirmação é','Verdadeiro')],['Verdadeiro','Falso'],
 'O netstat mostra conexões e estatísticas de TCP e UDP tanto em IPv4 quanto em IPv6 (por exemplo, "netstat -p udpv6" no Windows).',
 ['endpoint:21.1','fundamentos:20.5'])
Q(195,3,'Qual ação no Windows ajuda a detectar um invasor executando comandos do PowerShell sem autorização?',
 ['Ativar o monitoramento do Firewall do Windows Defender.','Ativar o registro de blocos de script (Script Block Logging).','Ativar a criptografia de unidade BitLocker.','Ativar as notificações de proteção contra vírus e ameaças.'],[1],
 'O registro de blocos de script grava no log o código PowerShell executado, inclusive o que foi ofuscado, permitindo detectar e investigar ataques "sem arquivo". Pode ser ativado por política de grupo ou pelo registro.',
 ['endpoint:20.3','endpoint:21.2'])
Q(196,3,'Você quer revisar a lista de pesquisa (search list) de domínios no nslookup. Qual comando usar?',
 ['set srchlist','set search','set type','set querytype'],[0],
 'No modo interativo do nslookup, "set srchlist" define a lista de domínios usados para completar nomes curtos. "set type" e "set querytype" escolhem o tipo de registro consultado.',
 ['fundamentos:20.4'])
Q(197,2,'Quais dois protocolos usam criptografia para proteger os dados em trânsito? (Escolha 2.)',
 ['SSH','FTP','Telnet','HTTPS'],[0,3],
 'O SSH cifra o acesso remoto e o HTTPS cifra a navegação com TLS. FTP e Telnet enviam tudo em texto claro, inclusive senhas.',
 ['defesa:15.3','defesa:15.5','defesa:27.3'])
Q(198,2,'Qual ataque usa uma botnet de muitos computadores para sobrecarregar um servidor web?',
 ['Ransomware','DoS','DDoS','Man-in-the-middle'],[2],
 'O DDoS é a negação de serviço distribuída: muitos computadores infectados (a botnet), comandados pelo atacante, enviam tráfego ao mesmo tempo. No DoS simples, o ataque parte de uma única origem.',
 ['endpoint:5.4'])
Q(199,3,'Qual é o termo para isolar um malware suspeito?',
 ['Exclusão','Quarentena','Execução','Limpeza'],[1],
 'A quarentena isola o arquivo suspeito para que ele não seja executado, sem apagá-lo. Assim, se for um falso positivo, dá para restaurar.',
 ['endpoint:21.5','endpoint:12.2'])
Q(200,3,'Onde o Windows 10 guarda as regras e permissões de acesso aos recursos e objetos?',
 ['ACL (lista de controle de acesso)','Registro do Windows','DAC (controle de acesso discricionário)','HAL (camada de abstração de hardware)'],[0],
 'Cada arquivo, pasta ou objeto tem uma ACL com as entradas de permissão (quem pode ler, gravar etc.). O DAC é o modelo em que o dono decide as permissões, e a ACL é onde elas ficam registradas.',
 ['defesa:11.4','defesa:10.1'])
