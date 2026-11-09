Q(1,3,'Uma amiga quer usar o Wi-Fi da sua casa no smartphone dela. Quais duas verificações de segurança você deve fazer antes de liberar o acesso? (Escolha 2.)',
 ['O aparelho é o modelo mais recente de Android ou Apple.','O aparelho foi verificado com as definições de antivírus/antimalware mais recentes.','O aparelho está bloqueado com PIN ou senha.','Os dispositivos, periféricos e arquivos importantes ou confidenciais estão em uma rede privada, separada dos convidados.'],[1,3],
 'Antes de deixar um aparelho de fora entrar na rede, duas coisas importam: que ele esteja limpo (antivírus/antimalware atualizado detecta ameaças conhecidas que poderiam se espalhar) e que os seus recursos importantes fiquem separados dos convidados (segmentação: rede de convidados de um lado, arquivos e impressoras do outro). O modelo do aparelho não diz nada sobre a segurança dele, e o bloqueio de tela protege o dono do celular, não a sua rede.',
 ['endpoint:27.3','defesa:16.1','fundamentos:6.7'])
Q(2,1,'Durante alterações autorizadas no servidor de folha de pagamento, um pico de energia danifica o equipamento. Ele é trocado e os dados são restaurados de um backup bom. Qual parte da tríade CIA foi preservada?',
 ['Integridade','Confidencialidade','Disponibilidade'],[2],
 'A tríade CIA é confidencialidade, integridade e disponibilidade. Graças ao backup e à troca do equipamento, o sistema voltou a funcionar e os dados puderam ser acessados de novo: isso é disponibilidade. Repare que a pergunta é sobre o que foi preservado pelas medidas de recuperação.',
 ['endpoint:1.4','defesa:1.1','endpoint:1.1'])
Q(3,5,'Um técnico suspeita que um servidor sofreu um ataque de força bruta contra as senhas. Qual log do Windows ele deve examinar para encontrar evidências?',
 ['Log do sistema','Log de segurança','Log de instalação','Log de aplicativo'],[1],
 'O log de segurança do Windows registra eventos ligados à segurança, como tentativas de logon (com sucesso e com falha) e acesso a arquivos. Um ataque de força bruta aparece ali como uma sequência de logons com falha. O log do sistema trata de drivers e serviços; o de aplicativo, de programas; o de instalação, de instalações.',
 ['endpoint:21.2','defesa:29.1','endpoint:12.5'])
Q(4,1,'Uma empresa guarda dados pessoais das clientes em um sistema interno, e um funcionário sem autorização consegue ver esses dados. Qual princípio da tríade CIA foi comprometido?',
 ['Integridade','Disponibilidade','Confidencialidade','Autenticação'],[2],
 'A confidencialidade garante que só pessoas autorizadas acessem a informação. Ver dados sem autorização é a violação típica da confidencialidade, mesmo que nada tenha sido alterado (integridade) ou ficado fora do ar (disponibilidade). Autenticação não faz parte da tríade: é um dos mecanismos que ajudam a garantir a confidencialidade.',
 ['endpoint:1.2','defesa:1.1','endpoint:1.1'])
Q(5,1,'Que tipo de ataque reúne phishing, tailgating (entrar atrás de alguém autorizado) e shoulder surfing (olhar por cima do ombro)?',
 ['Ataque de rede','Engenharia social','Ataque físico','Watering hole'],[1],
 'Os três exploram as pessoas, e não falhas técnicas: o phishing engana pela mensagem, o tailgating aproveita a gentileza de quem segura a porta e o shoulder surfing observa alguém digitando a senha. Essa é a definição de engenharia social: manipular pessoas para obter acesso ou informações.',
 ['endpoint:4.1','endpoint:4.3','endpoint:4.4','endpoint:6.8'])
Q(6,4,'Qual termo designa um conjunto de especificações para trocar informações sobre ameaças cibernéticas entre organizações?',
 ['AIS','STIX','CVE','CVSS'],[1],
 'O STIX (Structured Threat Information Expression) é o formato padronizado para descrever e trocar informações sobre ameaças. O AIS é um serviço do governo dos EUA que distribui indicadores; o CVE é o dicionário de identificadores de vulnerabilidades; o CVSS é o sistema de notas de gravidade.',
 ['ameacas:6.5','ameacas:6.3','ameacas:6.4'])
M(7,4,'Complete a frase: "Um(a) ____ é a possibilidade de exposição, de perda de um ativo ou de informações, ou de dano à reputação de uma empresa por um ataque cibernético."',
 [('Termo','risco')],['risco','cryptoworm','ataque de ransomware','exploração'],
 'Risco é a probabilidade (a possibilidade) de uma ameaça se concretizar e causar perda. A exploração é o ato de aproveitar uma vulnerabilidade; ransomware e cryptoworm são tipos de malware, não conceitos de gestão.',
 ['endpoint:2.2','ameacas:4.1'])
Q(8,1,'Qual lei de conformidade define uma estrutura que as agências federais dos EUA e seus prestadores de serviço devem seguir para proteger seus dados?',
 ['FERPA','GDPR','HIPAA','FISMA'],[3],
 'A FISMA exige que as agências federais americanas e seus prestadores tenham um programa de segurança da informação para os sistemas que usam. A FERPA trata de registros escolares, a HIPAA de dados de saúde e o GDPR de dados pessoais de cidadãos da União Europeia.',
 ['ameacas:2.5','ameacas:2.7'])
Q(9,1,'Uma empresa trata dados pessoais de cidadãos de vários países da União Europeia. Que regulamento ela deve seguir ao investigar incidentes que envolvam esses cidadãos?',
 ['FISMA','PCI DSS','HIPAA','FERPA','GDPR'],[4],
 'O GDPR (Regulamento Geral sobre a Proteção de Dados) protege os dados pessoais e a privacidade dos cidadãos da União Europeia, inclusive quando a empresa está fora da Europa. No Brasil, o equivalente é a LGPD.',
 ['ameacas:5.3','ameacas:2.7','ameacas:2.8'])
Q(10,4,'Quais duas ferramentas são usadas para examinar redes na avaliação de vulnerabilidades? (Escolha 2.)',
 ['Nessus','Metasploit','Wireshark','OpenSSL'],[0,2],
 'O Nessus é um scanner de vulnerabilidades: procura patches ausentes, portas desnecessárias, configurações fracas e outras falhas. O Wireshark é um analisador de protocolos que captura o tráfego e ajuda a enxergar o que está passando na rede. O Metasploit é usado para explorar falhas (teste de penetração), e o OpenSSL é uma biblioteca de criptografia. Observação: o gabarito da apostila considera o Wireshark, embora ele seja um analisador de tráfego, e não um scanner.',
 ['ameacas:8.2','ameacas:9.2','defesa:3.4'])
Q(11,1,'Ao chegar à recepção de um prédio seguro, você precisa mostrar sua identificação. Qual é a finalidade desse requisito?',
 ['Contabilidade (accounting)','Autenticação','Autorização'],[1],
 'Autenticar é verificar se a pessoa é quem diz ser, e é isso que a recepção faz ao conferir o documento. A autorização vem depois (o que você pode acessar no prédio), e a contabilidade registra o que foi feito (por exemplo, o horário de entrada e saída).',
 ['defesa:9.2','endpoint:17.6'])
Q(12,5,'Uma funcionária informa que o notebook dela foi roubado. Por quais três motivos você deve escalar o evento para o CSIRT? (Escolha 3.)',
 ['Aumento do tempo gasto restaurando backups','Possível interrupção da rede ou negação de serviço','Custo de um aparelho de reposição','Exposição de informações confidenciais ou secretas','Uso não autorizado dos recursos'],[1,3,4],
 'O roubo vira um incidente de segurança porque o notebook pode dar acesso à rede (permitindo interrupções ou um DoS), expor os dados que ele guarda e permitir o uso indevido de contas e recursos da empresa. Tempo de restauração e custo de reposição são problemas administrativos, não motivos para acionar a equipe de resposta a incidentes.',
 ['ameacas:16.2','ameacas:16.6','endpoint:2.5'])
Q(13,5,'Um técnico suspeita de malware do tipo APT em um sistema, colocou-o em quarentena e o desconectou da rede. O que ele deve fazer em seguida?',
 ['Iniciar em modo de segurança e rodar o antimalware atualizado.','Restaurar os dados de backups bons conhecidos.','Rodar um antimalware atualizado.','Reinstalar o sistema operacional e os aplicativos e depois restaurar os dados de backups bons conhecidos.'],[3],
 'Uma APT (ameaça persistente avançada) pode alterar o registro, arquivos do sistema e dos aplicativos de um jeito que o antimalware não consegue desfazer por completo. Por isso, a recuperação segura é reconstruir o sistema do zero e só depois trazer os dados de um backup confiável. Restaurar dados sem reinstalar manteria a infecção.',
 ['ameacas:16.7','endpoint:3.7','endpoint:25.5'])
Q(14,4,'Em um teste de penetração, você está fazendo o reconhecimento do domínio da empresa. Qual comando mostra os endereços IP públicos associados ao nome de domínio?',
 ['ipconfig /all','tracert','nslookup','netstat'],[2],
 'O nslookup consulta o DNS e mostra quais endereços IP correspondem a um nome de domínio. O ipconfig mostra a configuração do próprio computador, o tracert mostra o caminho até um destino e o netstat lista as conexões e portas locais.',
 ['fundamentos:20.4','ameacas:9.1','dispositivos:10.1'])
Q(15,2,'Um invasor na rede local envia pacotes que associam o MAC do computador dele ao IP de um servidor legítimo. Que ataque é esse?',
 ['Falsificação de IP','Falsificação de MAC','Estouro da tabela CAM','Falsificação (envenenamento) de ARP'],[3],
 'O ARP liga endereços IP a endereços MAC e não tem autenticação. Ao anunciar "o IP do servidor está no meu MAC", o invasor envenena o cache ARP das vítimas e passa a receber o tráfego destinado ao servidor, o que permite um ataque man-in-the-middle.',
 ['endpoint:9.2','endpoint:9.1','fundamentos:16.8'])
Q(16,1,'Qual algoritmo é uma função matemática de mão única usada para garantir a integridade dos dados?',
 ['Diffie-Hellman','AES','SHA-2','3DES'],[2],
 'O SHA-2 é um algoritmo de hash: gera uma "impressão digital" de tamanho fixo e não permite voltar ao dado original (mão única). Se um bit muda, o hash muda, o que revela alterações. AES e 3DES são criptografia simétrica (confidencialidade), e o Diffie-Hellman serve para trocar chaves.',
 ['defesa:6.3','defesa:6.2','defesa:5.7'])
Q(17,4,'Qual destas situações é um exemplo de reconhecimento passivo?',
 ['Usar o Nmap para encontrar portas abertas em um host','Usar o SQLMap para detectar falhas de injeção de SQL em um banco de dados','Usar o nslookup para obter informações sobre um nome de host','Usar o Nessus para procurar vulnerabilidades na rede'],[2],
 'No reconhecimento passivo, o atacante não interage diretamente com o alvo: consulta fontes públicas, como o DNS. Nmap, SQLMap e Nessus enviam tráfego ao alvo e por isso são reconhecimento ativo (e podem ser detectados).',
 ['ameacas:10.2','fundamentos:20.4','endpoint:6.1'])
M(18,1,'Para cada método de autenticação, indique Sim se ele pertence ao fator "algo que você tem" ou Não se não pertence.',
 [('Responder a uma pergunta secreta','Não'),('Token recebido por e-mail','Sim'),('Impressão digital','Não'),('Chave','Sim'),('Escaneamento de retina','Não'),('Cartão inteligente','Sim')],['Sim','Não'],
 'Os fatores são: algo que você sabe (senha, pergunta secreta), algo que você tem (chave, cartão inteligente, token enviado ao seu e-mail ou celular) e algo que você é (biometria, como digital e retina). A pergunta secreta é conhecimento; digital e retina são características do corpo.',
 ['defesa:9.4','defesa:9.5'])
Q(19,4,'Quais três padrões permitem trocar inteligência sobre ameaças cibernéticas (CTI) em formato automatizado, consistente e legível por máquina? (Escolha 3.)',
 ['STIX','TAXII','Cisco Talos','FireEye Helix','CybOX'],[0,1,4],
 'STIX é o formato das informações, TAXII é o protocolo que as transporta (sobre HTTPS) e CybOX descreve eventos observáveis (hoje incorporado ao STIX). Cisco Talos e FireEye Helix são serviços comerciais de inteligência, não padrões abertos.',
 ['ameacas:6.5','ameacas:6.3'])
Q(20,2,'Que tipo de ataque troca o endereço IP de origem para se passar por um computador legítimo?',
 ['Man-in-the-middle','Falsificação de IP','Estouro de buffer','Falsificação de ARP'],[1],
 'Na falsificação de IP (IP spoofing), o atacante coloca um IP de origem falso nos pacotes para se passar por outro computador e dificultar o rastreamento. A falsificação de ARP trabalha com endereços MAC na rede local, e o estouro de buffer é uma falha de memória em programas.',
 ['endpoint:7.7','endpoint:7.1'])
Q(21,1,'Qual ataque usa o telefone para obter informações pessoais ou confidenciais?',
 ['Pharming','Vishing','Whaling','Spear phishing'],[1],
 'Vishing é o phishing por voz (telefone). Pharming redireciona a vítima para um site falso, whaling mira executivos e spear phishing mira uma pessoa ou empresa específica, em geral por e-mail.',
 ['endpoint:6.8','endpoint:4.2'])
Q(22,2,'Quais três características valem tanto para o IDS quanto para o IPS? (Escolha 3.)',
 ['Os dois usam assinaturas para detectar tráfego malicioso.','Os dois aumentam a latência do tráfego de rede.','Os dois são apenas ferramentas de monitoramento.','Os dois aceitam ou rejeitam tráfego malicioso conhecido.','Os dois comparam o tráfego com um banco de atividades maliciosas conhecidas.','Os dois usam sensores para ler o tráfego da rede.'],[0,4,5],
 'IDS e IPS leem o tráfego por sensores e o comparam com assinaturas de ataques conhecidos. A diferença é a ação: o IDS só monitora e alerta (fica fora do caminho, sem latência), enquanto o IPS fica em linha e pode bloquear pacotes (o que acrescenta latência).',
 ['endpoint:16.4','defesa:28.1'])
Q(23,3,'Dois prestadores de serviço precisam acessar a rede com aparelhos próprios, e a política exige inspecionar o risco de cada dispositivo. O prestador A tem VPN, mas o navegador está um mês desatualizado. O prestador B usa MFA e tem o sistema operacional com o patch mais recente. Quem deve ter o acesso liberado?',
 ['Prestador A','Prestador B'],[1],
 'Um software desatualizado é uma vulnerabilidade conhecida e explorável, mesmo com VPN. O prestador B atende às duas verificações típicas de postura: sistema corrigido e autenticação multifator. Por isso, só ele passa na inspeção.',
 ['endpoint:26.3','defesa:9.5','endpoint:26.2'])
Q(24,5,'Em uma investigação forense, quais duas ações os invasores costumam praticar para esconder as evidências do ataque? (Escolha 2.)',
 ['Limpar os arquivos de log','Alterar (comprometer) os dados','Elevar as permissões de rede','Monitorar as portas de rede'],[0,1],
 'Para apagar rastros, o invasor limpa os logs e altera dados e carimbos de hora. Elevar permissões faz parte do ataque, mas não esconde nada; monitorar portas também não. Por isso a perícia preserva as evidências, trabalha em cópias e confere hashes.',
 ['ameacas:15.1','ameacas:15.6','ameacas:13.8'])
Q(25,3,'Qual ferramenta do Windows é usada para examinar os logs de segurança?',
 ['Gerenciador de Tarefas','Gerenciador de Dispositivos','Visualizador de Eventos','Console de Gerenciamento'],[2],
 'O Visualizador de Eventos (Event Viewer) mostra os logs do Windows: aplicativo, sistema, segurança e outros. O Gerenciador de Tarefas mostra processos e desempenho, e o Gerenciador de Dispositivos mostra o hardware e os drivers.',
 ['endpoint:21.2','defesa:29.1'])
