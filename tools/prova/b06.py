Q(126,4,'Qual organização mantém a ferramenta de avaliação que dá uma nota numérica à gravidade de uma vulnerabilidade?',
 ['MITRE Corporation','Instituto SANS','FIRST (Forum of Incident Response and Security Teams)','DHS dos EUA'],[2],
 'O FIRST é o guardião do CVSS, o sistema que dá notas de 0 a 10 às vulnerabilidades. A MITRE mantém o CVE (os identificadores), e o DHS mantém o serviço AIS.',
 ['ameacas:11.1','ameacas:6.1'])
M(127,3,'Verdadeiro ou falso: "No modo não interativo, o nslookup consulta informações sobre vários sites ou servidores."',
 [('A afirmação é','Falso')],['Verdadeiro','Falso'],
 'No modo não interativo, você digita "nslookup nome" e recebe uma única resposta. Para fazer várias consultas seguidas, sobre vários sites ou servidores, usa-se o modo interativo (digitar só "nslookup" e depois os comandos).',
 ['fundamentos:20.4'])
M(128,5,'Relacione cada nível de gravidade do syslog à situação correspondente.',
 [('Nível 1 (alerta)','A condição deve ser corrigida imediatamente'),('Nível 4 (aviso)','Um erro poderá ocorrer se a situação não for corrigida'),('Nível 5 (notificação)','Evento incomum, mas não um erro'),('Nível 6 (informativo)','Operação normal, sem necessidade de intervenção')],None,
 'Os níveis do syslog vão de 0 (emergência, sistema inutilizável) a 7 (depuração). Quanto menor o número, mais grave: 1 alerta, 2 crítico, 3 erro, 4 aviso, 5 notificação, 6 informativo.',
 ['defesa:29.2','defesa:27.1','endpoint:17.5'])
M(129,1,'Complete a frase: "____ aproveitam a vulnerabilidade do computador e nem sempre são maliciosas."',
 [('Termo','Explorações')],['Explorações','Ameaças','Malware','Riscos'],
 'A exploração (exploit) é o código ou a técnica que aproveita uma vulnerabilidade. Ela também é usada de forma legítima, por exemplo em testes de penetração autorizados, por isso nem sempre é maliciosa.',
 ['endpoint:2.2','endpoint:18.4'])
Q(130,2,'Como a segmentação de rede aumenta a segurança?',
 ['Fornece um método para mapear as partes da rede que têm vírus.','Divide a rede em grupos lógicos para controlar o acesso aos recursos.','Ajuda a entregar pacotes mapeando MACs desconhecidos para IPs conhecidos.','Monitora eventos em uma parte da rede, e não na rede toda.'],[1],
 'Segmentar (com VLANs, sub-redes, zonas de firewall) separa grupos e permite controlar quem acessa o quê. Se um segmento for invadido, o atacante não chega automaticamente aos outros, e o tráfego desnecessário também diminui.',
 ['defesa:16.1','defesa:16.3','fundamentos:12.13'])
M(131,5,'Verdadeiro ou falso: "O plano de continuidade de negócios é importante porque define como a empresa restaura as funções críticas do negócio em caso de desastre."',
 [('A afirmação é','Verdadeiro')],['Verdadeiro','Falso'],
 'O BCP define como manter e restaurar o mais rápido possível as funções críticas durante e depois de um desastre, inclusive operando em outro local.',
 ['ameacas:17.3'])
Q(132,2,'O que cria e gerencia a validação digital dos sites dentro da PKI (infraestrutura de chave pública)?',
 ['Autoridade certificadora (CA)','Assinatura de código','Diffie-Hellman','Padrão FIPS do governo dos EUA'],[0],
 'A autoridade certificadora emite os certificados digitais, ligando uma chave pública a uma identidade confirmada (como um site), e também os revoga quando necessário.',
 ['defesa:7.5','defesa:7.4','defesa:7.9'])
Q(133,3,'Qual comando altera as permissões de um arquivo no Linux?',
 ['chmod','chgrp','mkdir','chown'],[0],
 'O chmod muda as permissões (leitura, gravação e execução). O chown muda o dono, o chgrp muda o grupo e o mkdir cria diretórios.',
 ['endpoint:24.3'])
Q(134,2,'Uma ACL deve permitir SSH ao servidor 10.0.0.1 apenas a partir da rede 172.17.1.128/28, bloquear todo o resto do tráfego IP para esse servidor e permitir só tráfego web para os outros hosts. Em que ordem entram as linhas? A) access-list 110 deny ip any any; B) access-list 110 deny ip any host 10.0.0.1; C) access-list 110 permit tcp 172.17.1.128 0.0.0.15 host 10.0.0.1 eq 22; D) access-list 110 permit tcp any any eq 80',
 ['DCBA','ABCD','BDCA','CBDA'],[3],
 'A ACL é lida de cima para baixo e para na primeira linha que combina. Por isso, a regra mais específica vem primeiro: C (libera o SSH da rede autorizada), depois B (nega o resto para o servidor), depois D (libera web para os demais) e por fim A (nega tudo o mais). Se B viesse antes de C, o SSH seria bloqueado.',
 ['defesa:20.3','defesa:21.3','defesa:21.7'])
Q(135,1,'Qual parte da tríade CIA é atacada no shoulder surfing (olhar por cima do ombro)?',
 ['Disponibilidade','Confidencialidade','Integridade'],[1],
 'Quem espia a tela ou o teclado obtém informações que não deveria ver, como senhas: ataque à confidencialidade.',
 ['endpoint:4.3','endpoint:1.2'])
Q(136,4,'Um bug no software de folha de pagamento pode ser explorado com facilidade, e uma interrupção teria grandes consequências para os funcionários e para a reputação. Pela matriz de risco do NIST (probabilidade × impacto), qual nível de risco atribuir?',
 ['Muito baixo','Moderado','Baixo','Alto'],[3],
 'Fácil de explorar significa probabilidade alta, e grandes consequências significam impacto alto. Na matriz, probabilidade alta com impacto alto resulta em risco alto.',
 ['ameacas:4.4','ameacas:4.5'])
Q(137,5,'Em que ordem devem ser coletadas as evidências digitais de um computador?',
 ['Conteúdo da RAM, conteúdo do disco, backup arquivado','Backup arquivado, conteúdo do disco, conteúdo da RAM','Conteúdo do disco, conteúdo da RAM, backup arquivado','Conteúdo do disco, backup arquivado, conteúdo da RAM'],[0],
 'Pela ordem de volatilidade (RFC 3227), coleta-se primeiro o que se perde mais fácil: a RAM some quando o computador desliga, o disco é mais estável e o backup arquivado é o mais permanente.',
 ['ameacas:15.4'])
Q(138,3,'Você precisa registrar o acesso aos arquivos. Que tipo de auditoria do Windows deve ser ativada?',
 ['Auditoria de logon','Acompanhamento de processos','Acesso ao serviço de diretório','Acesso a objetos'],[3],
 'A auditoria de acesso a objetos registra as tentativas de acessar arquivos, pastas e outros objetos. A de logon registra entradas no sistema, e a de processos registra programas iniciados e encerrados.',
 ['endpoint:21.4','defesa:9.7'])
Q(139,1,'Que tipo de criptografia usa uma chave pré-compartilhada para cifrar e decifrar os dados?',
 ['Simétrica','SHA-2','Assimétrica','Diffie-Hellman'],[0],
 'Na simétrica, remetente e destinatário usam a mesma chave secreta, combinada antes da comunicação. Na assimétrica há um par de chaves diferentes; o Diffie-Hellman serve justamente para combinar uma chave secreta com segurança.',
 ['defesa:5.3','defesa:5.6'])
M(140,2,'Para cada afirmação, indique Sim se for um motivo válido para proteger ou ocultar endereços IP de um hacker, ou Não se não for.',
 [('Um endereço IP pode ser usado para rastrear o comportamento online.','Sim'),('Um endereço IP identifica de forma única um dispositivo na rede ou na internet.','Sim'),('Os endereços IP são usados só internamente e não devem sair da rede.','Não'),('Os endereços IPv4 estão desatualizados e não têm mais suporte.','Não'),('Os endereços IPv6 são mais longos, mas também estão sujeitos a ataques.','Sim')],['Sim','Não'],
 'O IP identifica o dispositivo, revela localização aproximada e permite rastrear a navegação, e o IPv6 tem vulnerabilidades parecidas com as do IPv4. Já as outras duas afirmações são falsas: IPs são necessários para comunicar fora da rede, e o IPv4 continua em uso.',
 ['fundamentos:12.9','fundamentos:12.7','endpoint:7.1'])
Q(141,1,'Qual é a característica principal da proteção em camadas na segurança cibernética?',
 ['Criptografia','Vários firewalls','Várias camadas de segurança sobrepostas','Políticas de senha forte'],[2],
 'A defesa em profundidade usa vários controles sobrepostos (físicos, técnicos e administrativos), de modo que, se um falhar, os outros continuam protegendo.',
 ['defesa:2.1','defesa:2.3'])
M(142,4,'Verdadeiro ou falso: "Os serviços de inteligência de ameaças usam os dados dos assinantes para se manter atualizados."',
 [('A afirmação é','Verdadeiro')],['Verdadeiro','Falso'],
 'Muitas organizações compartilham, em geral de forma automática, os dados de intrusão com os serviços que assinam, e esses serviços usam as informações para melhorar a proteção de todos.',
 ['ameacas:6.6','ameacas:6.3'])
Q(143,2,'O que acontece em um ataque de roteamento pela origem (source routing)?',
 ['O atacante cria muitas sessões semiabertas para negar novas conexões.','O atacante tenta adivinhar os números de sequência do TCP.','O atacante falsifica o IP de origem para fazer o sistema reenviar os mesmos dados a um servidor.','O atacante manipula as opções de rota do pacote para definir o caminho que ele percorre.'],[3],
 'O IPv4 tem opções que permitem ao remetente definir a rota do pacote. O atacante usa isso para forçar o tráfego a passar por um ponto que ele controla. Por isso os roteadores costumam descartar pacotes com roteamento pela origem. As outras opções descrevem inundação de SYN, previsão de sequência TCP e ataque de repetição.',
 ['endpoint:7.4','endpoint:7.2'])
Q(144,2,'Um invasor conecta um notebook à rede sem fio e tenta obter todos os endereços disponíveis do servidor DHCP. Que ataque é esse?',
 ['Esgotamento (starvation) de DHCP','Falsificação de IP','Falsificação de DHCP','Falsificação de DNS'],[0],
 'No starvation, o atacante pede endereços com muitos MACs falsos até esgotar o pool, e os clientes legítimos ficam sem IP (negação de serviço). Muitas vezes isso prepara uma falsificação de DHCP, com um servidor falso assumindo o lugar.',
 ['endpoint:9.5','fundamentos:14.5'])
Q(145,3,'Qual comando do Linux altera o diretório raiz visto por um processo?',
 ['chmod','chroot','sudo','su'],[1],
 'O chroot executa um processo com outro diretório como raiz, confinando-o a uma parte do sistema de arquivos. O sudo e o su executam comandos com outro usuário, e o chmod muda permissões.',
 ['endpoint:24.1','endpoint:22.4'])
Q(146,5,'Qual estrutura é uma base de conhecimento sobre táticas, técnicas e procedimentos dos adversários, feita a partir de observações reais?',
 ['MITRE ATT&CK','Cyber Kill Chain','Modelo Diamond de análise de intrusão','Processo forense'],[0],
 'O MITRE ATT&CK organiza o comportamento real dos atacantes em uma matriz de táticas e técnicas. A Kill Chain descreve as etapas de um ataque, e o Modelo Diamond descreve os elementos de cada evento.',
 ['ameacas:15.8','ameacas:13.1','ameacas:14.1'])
Q(147,4,'Uma empresa monta um sistema de isca para atrair invasores e estudar novas ameaças. Como se chama?',
 ['Honeypot','DMZ','Servidor proxy','IDS'],[0],
 'O honeypot é um sistema ou rede simulado para atrair atacantes e observar as técnicas deles, sem risco para a produção.',
 ['ameacas:6.6','defesa:19.6'])
Q(148,2,'Qual é a vantagem de usar o MAC, e não o IP, para permitir ou negar dispositivos na rede de convidados?',
 ['O MAC não pode ser falsificado, mas o IP pode.','O MAC do dispositivo continua o mesmo, mas o IP pode mudar.','O IDS detecta o MAC mais rápido que o IP.','O MAC não é usado para enviar dados, então é mais fácil de proteger.'],[1],
 'O IP muda conforme a rede e o DHCP, enquanto o MAC é o endereço físico da placa e acompanha o aparelho, o que permite filtrá-lo. Atenção: o MAC também pode ser falsificado, então a filtragem é uma proteção fraca.',
 ['endpoint:15.1','fundamentos:10.4'])
Q(149,1,'Uma empresa francesa vende online e processa pagamentos com cartão de crédito. Qual padrão ela deve adotar para reduzir incidentes com esses pagamentos?',
 ['GDPR','PCI DSS','HIPAA','FERPA'],[1],
 'O PCI DSS é o padrão do setor de cartões e vale no mundo todo para quem armazena, processa ou transmite dados de cartão. A empresa também precisa cumprir o GDPR por estar na União Europeia, mas a pergunta é sobre os pagamentos com cartão.',
 ['ameacas:2.5','defesa:4.5'])
M(150,4,'Relacione cada ameaça à estratégia de mitigação adequada.',
 [('Interrupção na cadeia de fornecimento','Fontes alternativas e gestão de estoque'),('Erros de funcionários','Procedimentos padrão e treinamento'),('Ataque cibernético','Firewalls, IDS/IPS e analisadores de log'),('Desastres naturais','Instalações reforçadas e locais alternativos')],None,
 'Cada ameaça pede um tipo de controle: redundância de fornecedores para a cadeia de suprimentos, SOPs e treinamento para erros humanos, controles técnicos para ataques e redundância física para desastres.',
 ['ameacas:4.6','ameacas:17.4','endpoint:6.10'])
