Q(151,2,'Qual é um ataque comum contra dispositivos IoT?',
 ['Falsificação de ARP','Inundação de SYN','DDoS','Falsificação de MAC'],[2],
 'Os dispositivos IoT têm poucos recursos e muitas vezes senhas padrão. Eles são alvo de DDoS (ficam indisponíveis facilmente) e também são recrutados em botnets para lançar DDoS contra outros alvos, como fez a botnet Mirai.',
 ['defesa:19.2','endpoint:5.4'])
M(152,2,'Complete as frases com o ataque ou técnica ICMP/IP.',
 [('Em um ataque ____, o atacante falsifica a origem de pacotes ICMP e os envia ao endereço de broadcast, gerando tráfego suficiente para derrubar a rede.','smurf'),('____ é a técnica que usa respostas ao eco ICMP para descobrir o sistema operacional do alvo.','impressão digital (fingerprinting)'),('Em um ataque ____, o atacante envia fragmentos IP sobrepostos; o alvo não consegue remontá-los e trava ou reinicia.','teardrop')],['impressão digital (fingerprinting)','túnel ICMP','smurf','teardrop'],
 'O smurf é um ataque de amplificação e reflexão com ICMP e broadcast. A impressão digital do sistema operacional analisa detalhes das respostas. O teardrop explora a remontagem de fragmentos. O túnel ICMP esconde dados dentro de pacotes ICMP.',
 ['endpoint:7.5','endpoint:7.6','endpoint:7.4'])
Q(153,5,'Qual termo descreve o processo que garante que as provas não foram alteradas nem fabricadas depois da coleta?',
 ['Atribuição de ataque','Evidência direta','Cadeia de custódia','Melhor evidência'],[2],
 'A cadeia de custódia documenta quem coletou, manuseou e guardou cada prova, quando e onde, o que garante que ela não foi adulterada. A melhor evidência é a prova no estado original, e a atribuição identifica o autor do ataque.',
 ['ameacas:15.5','ameacas:15.3'])
Q(154,4,'Em um teste de penetração interno, você faz um reconhecimento ativo. Qual é o objetivo?',
 ['Instalar um mecanismo de controle para acessar outros sistemas.','Explorar dados de vulnerabilidade e criar um modelo de ameaça.','Explorar uma falha para entrar na rede.','Examinar os sistemas em busca de vulnerabilidades e pontos fracos para atacar.'],[3],
 'O reconhecimento, ativo ou passivo, serve para descobrir onde estão os pontos fracos. A exploração e a instalação de mecanismos de controle (persistência) vêm em fases posteriores.',
 ['ameacas:10.2','ameacas:13.2'])
Q(155,3,'Como proteger um dispositivo contra acessos indesejados e malware que passaram pelo firewall da rede?',
 ['Usar criptografia de arquivos no dispositivo.','Exigir logon para usar o dispositivo.','Usar um firewall de host no dispositivo.','Rodar o verificador de arquivos do sistema.'],[2],
 'O firewall de host protege cada máquina individualmente, controlando o que entra e sai dela. É a segunda camada, caso algo tenha passado pelo firewall de perímetro.',
 ['endpoint:28.1','endpoint:27.3','endpoint:21.6'])
Q(156,2,'Você está implantando o controle de acesso à rede 802.1X para autenticar usuários e dispositivos. Qual servidor de autenticação usar?',
 ['RADIUS','SNMP','LDAP','TACACS+'],[0],
 'No 802.1X, o switch ou o AP repassa as credenciais a um servidor RADIUS, que autentica o usuário. O TACACS+ é mais usado para autenticar administradores de equipamentos, o LDAP é um diretório e o SNMP serve para gerenciamento.',
 ['defesa:12.2','endpoint:15.5'])
Q(157,3,'Um Windows 10 não conseguiu instalar algumas atualizações de segurança. Onde o técnico encontra informações sobre as que falharam?',
 ['Gerenciador de Tarefas','Histórico de atualizações','Visualizador de Eventos','Informações do Sistema'],[1],
 'O histórico de atualizações do Windows Update lista o que foi instalado e o que falhou, com o código do erro.',
 ['endpoint:21.3'])
Q(158,4,'Qual organização oferece o serviço AIS (compartilhamento automatizado de indicadores) a órgãos públicos e empresas privadas?',
 ['Instituto SANS','FIRST','DHS dos EUA (Departamento de Segurança Interna)','MITRE Corporation'],[2],
 'O AIS é um serviço gratuito do DHS que distribui indicadores de ameaça em tempo real, no formato STIX, assim que uma ameaça é reconhecida.',
 ['ameacas:6.3'])
Q(159,3,'Como começar um plano de atualização de firmware?',
 ['Usar o WSUS para evitar interrupções.','Criar uma política de grupo com horários fora do pico.','Avaliar e priorizar as atualizações pelo potencial de interrupção para usuários e sistemas.','Rodar todas as atualizações primeiro em máquinas virtuais.'],[2],
 'Atualizar firmware pode deixar sistemas críticos parados por bastante tempo. Por isso o primeiro passo é avaliar e priorizar, como em qualquer gerenciamento de patches, antes de agendar ou testar.',
 ['endpoint:26.3','ameacas:12.5'])
Q(160,5,'Depois de identificar uma possível vulnerabilidade no servidor de e-mail, o adversário obtém uma ferramenta automatizada para entregar a carga de malware. Que etapa da Cyber Kill Chain é essa?',
 ['Exploração','Entrega','Armamento','Reconhecimento'],[2],
 'No armamento, o atacante usa o que aprendeu no reconhecimento para preparar a arma: junta o exploit e o malware e obtém a ferramenta para entregá-los. A entrega é o envio propriamente dito.',
 ['ameacas:13.3','ameacas:13.1'])
Q(161,3,'Trabalhadores remotos com pouca banda precisam baixar patches críticos e de segurança do Windows, mas não as atualizações de recursos. Qual recurso do Windows permite isso?',
 ['WSUS','Conexão limitada','SFC','Agendador de Tarefas'],[1],
 'Com a rede marcada como conexão limitada (medida), o Windows deixa de baixar as atualizações de recursos, mas continua baixando os patches críticos e de segurança.',
 ['endpoint:21.3'])
Q(162,1,'No site do banco, depois do usuário e da senha, aparece uma pergunta secreta. Qual fator de autenticação o banco está usando?',
 ['Algum lugar onde você está','Algo que você é','Algo que você tem','Algo que você sabe'],[3],
 'Senha e resposta secreta são as duas "algo que você sabe". Por isso, a rigor, isso não é autenticação multifator: são duas informações do mesmo fator.',
 ['defesa:9.4','defesa:9.5'])
M(163,2,'Complete as frases com o ataque ao DHCP ou ao DNS.',
 [('Em um ataque de ____ de DHCP, o atacante coloca um servidor DHCP falso na rede para entregar endereços aos clientes.','falsificação'),('Em um ataque de ____ de DHCP, o atacante inunda o servidor com pedidos até usar todos os endereços disponíveis.','starvation (esgotamento)'),('Em um ataque de ____ de DNS, o atacante usa resolvedores abertos para inundar a vítima com respostas DNS.','amplificação'),('Em um ataque de ____ de DNS, o atacante altera o registro A do domínio para apontar para um endereço escolhido por ele.','sequestro')],['falsificação','starvation (esgotamento)','estouro de buffer','MitM','amplificação','sequestro','envenenamento','túnel'],
 'No DHCP: falsificação é o servidor falso, starvation é esgotar o pool. No DNS: amplificação usa resolvedores abertos para multiplicar o tráfego, e sequestro (hijacking) altera os registros do domínio para desviar os visitantes.',
 ['endpoint:9.5','endpoint:10.1','endpoint:10.2'])
Q(164,3,'Você vai analisar um tráfego capturado com "tcpdump -w". Que tipo de arquivo esperar?',
 ['.pcap','.txt','.xml','.data'],[0],
 'A opção -w grava a captura em formato pcap (packet capture), que pode ser aberto depois no Wireshark ou no próprio tcpdump com -r.',
 ['ameacas:9.7','defesa:28.4'])
Q(165,2,'A empresa tem um servidor VPN e roteadores com acesso remoto, e você vai implantar o AAA centralizado. Qual servidor instalar?',
 ['Servidor DNS','Servidor DHCP','Servidor RADIUS','Servidor de acesso remoto'],[2],
 'O RADIUS (ou o TACACS+) centraliza a autenticação, a autorização e a contabilidade para VPN, roteadores e outros equipamentos, em vez de ter usuários locais em cada um.',
 ['defesa:12.1','defesa:12.2','endpoint:17.6'])
Q(166,2,'Quais duas opções servem para monitorar o tráfego de rede? (Escolha 2.)',
 ['Keylogger','NetFlow','Captura de pacotes','Reconhecimento'],[1,2],
 'O NetFlow registra os fluxos (quem falou com quem, quanto e por quanto tempo), e a captura de pacotes guarda o conteúdo do tráfego. O keylogger é malware, e o reconhecimento é uma fase do ataque.',
 ['endpoint:17.3','defesa:28.4','defesa:3.4'])
Q(167,5,'Usuários relatam lentidão em um servidor web interno, e você, analista júnior, vê nos logs e nas capturas muitos pacotes do mesmo IP inundando a rede. O que fazer primeiro?',
 ['Bloquear o tráfego da LAN inteira com o dispositivo ofensivo.','Escalar o problema para um analista mais experiente.','Alterar as regras do firewall.','Calcular quanto tempo levaria para desligar o servidor.'],[1],
 'O analista de nível 1 confirma o alerta e escala o verdadeiro positivo para o nível superior, que tem ferramentas e autoridade para investigar e conter. Mudar firewall ou bloquear a rede por conta própria pode causar mais danos e destruir evidências.',
 ['defesa:30.4','ameacas:16.6'])
Q(168,3,'A empresa quer atualizar o Windows 10 seguindo uma lista de diretrizes de conformidade predefinidas. Qual estratégia usar?',
 ['Criar um modelo de política de segurança.','Usar a linha de base do Windows Update.','Configurar um servidor WSUS.','Editar as políticas de conta no GPO local.'],[1],
 'A linha de base do Windows Update (Windows Update Baseline) é um conjunto de configurações recomendadas pela Microsoft para garantir que os dispositivos recebam as atualizações mensais no prazo, de forma padronizada.',
 ['endpoint:21.3','ameacas:12.4'])
Q(169,4,'Uma varredura mostra que mais da metade dos computadores dos usuários está com o sistema operacional desatualizado. Qual mitigação é a adequada?',
 ['Implantar um sistema de gerenciamento de patches que aplique as atualizações automaticamente.','Usar firewalls e ACLs contra sites maliciosos.','Instalar um pacote de segurança de e-mail.','Criar uma política de permissões para restringir o acesso a bancos de dados.'],[0],
 'O problema é software desatualizado, e a mitigação que ataca a causa é o gerenciamento de patches. As outras medidas ajudam em outros riscos, mas deixam as vulnerabilidades abertas.',
 ['ameacas:12.5','endpoint:26.3'])
Q(170,1,'Que ataque físico consiste em entrar em uma área restrita aproveitando o acesso de outra pessoa?',
 ['Vishing','Whaling','Tailgating','Spear phishing'],[2],
 'No tailgating (ou piggybacking), o invasor entra logo atrás de alguém autorizado. Defesas: catracas, mantraps e funcionários orientados a não segurar a porta.',
 ['endpoint:4.4','defesa:13.1'])
Q(171,4,'Qual ferramenta de teste de penetração explora um ativo para verificar se ele é realmente vulnerável?',
 ['OpenSSL','Wireshark','Nessus','Metasploit'],[3],
 'O Metasploit traz exploits prontos para testar se a vulnerabilidade pode mesmo ser explorada. O Nessus só aponta as vulnerabilidades, o Wireshark captura tráfego e o OpenSSL é uma biblioteca de criptografia.',
 ['ameacas:9.2','ameacas:8.1'])
Q(172,2,'O que oferece a segurança mais forte para o tráfego sem fio?',
 ['Filtragem de MAC','WEP','Ocultação do SSID','WPA3'],[3],
 'O WPA3 é o padrão mais recente: protege a senha com SAE, cifra até redes abertas (OWE) e usa criptografia mais forte. WEP é quebrado, e filtragem de MAC e ocultação do SSID são fáceis de contornar.',
 ['endpoint:15.6','defesa:17.1'])
M(173,1,'Verdadeiro ou falso: "Seguir a política de tela limpa significa deixar o computador bloqueado quando você se afasta da mesa."',
 [('A afirmação é','Verdadeiro')],['Verdadeiro','Falso'],
 'A política de tela limpa (e mesa limpa) pede que o computador seja bloqueado ao se afastar e que documentos não fiquem expostos, evitando uso indevido e espiadas.',
 ['endpoint:30.4','endpoint:26.8'])
Q(174,3,'Qual tipo de evento do log do Windows registra a operação bem-sucedida de um aplicativo, driver ou serviço?',
 ['Informações','Aviso','Erro','Auditoria com êxito'],[0],
 'Informações registram operações bem-sucedidas. A auditoria com êxito é diferente: registra uma tentativa de acesso de segurança auditada que deu certo, como um logon.',
 ['endpoint:21.2'])
Q(175,1,'Qual termo designa a soma de todos os vetores de ataque possíveis contra um ambiente?',
 ['Risco','Comprometimento','Superfície de ataque','Vulnerabilidade'],[2],
 'A superfície de ataque é o conjunto de todos os pontos por onde um atacante pode tentar entrar: portas abertas, aplicativos, usuários, dispositivos. Reduzi-la é um dos objetivos do endurecimento.',
 ['endpoint:29.1'])
