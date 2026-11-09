Q(76,3,'Qual é a proteção padrão contra malware do Windows?',
 ['PowerShell','Microsoft Defender','DWM (Gerenciador de Janelas da Área de Trabalho)','WMI (Instrumentação de Gerenciamento do Windows)'],[1],
 'O Microsoft Defender é o antivírus/antimalware que já vem no Windows. O PowerShell é um shell de comandos, o DWM desenha as janelas e a WMI é uma interface de gerenciamento.',
 ['endpoint:21.5','endpoint:27.3'])
Q(77,1,'Qual afirmação é verdadeira sobre as ameaças persistentes avançadas (APTs)?',
 ['Elas miram dispositivos IoT.','Elas são usadas para roubar dados.','Elas dependem de métodos de ataque antigos.','Elas entram e saem do alvo o mais rápido possível.'],[1],
 'A APT é um ataque prolongado e discreto, geralmente bem financiado, cujo objetivo é ficar dentro da rede por muito tempo para roubar informações, e não destruir sistemas. Por isso ela não entra e sai rápido, e costuma usar técnicas sofisticadas.',
 ['endpoint:3.7','ameacas:13.8'])
M(78,3,'Relacione cada tipo de malware à sua descrição.',
 [('Adware','Redireciona o navegador para sites escolhidos pelo atacante e exibe propaganda'),('Cryptojacking','Usa os recursos do computador da vítima para minerar criptomoedas'),('Rootkit','Conjunto de ferramentas para acessar e controlar o computador remotamente, escondendo a presença'),('Ransomware','Criptografa o conteúdo do disco da vítima e pede resgate'),('Spyware','Coleta dados em segredo e os envia ao atacante')],None,
 'Cada nome indica o objetivo: ad (propaganda), crypto (mineração), root (acesso de administrador escondido), ransom (resgate) e spy (espionagem).',
 ['endpoint:5.2','endpoint:5.3','endpoint:5.1'])
M(79,2,'Relacione cada ferramenta de monitoramento à sua descrição.',
 [('SNMP','Protocolo que permite monitorar e gerenciar o desempenho dos dispositivos de rede'),('Captura de pacotes','Intercepta e armazena os dados que trafegam na rede'),('SOAR','Coleta dados, analisa ameaças e usa fluxos de trabalho para automatizar a resposta'),('SIEM','Coleta dados de segurança, detecta ameaças e apoia a investigação')],None,
 'O SIEM centraliza e correlaciona; o SOAR vai além e automatiza a resposta com playbooks; a captura de pacotes guarda o tráfego real; o SNMP é o protocolo de gerenciamento dos equipamentos.',
 ['defesa:29.5','defesa:29.6','endpoint:17.2','ameacas:9.7'])
Q(80,1,'Quais são as duas classes de algoritmos de criptografia? (Escolha 2.)',
 ['Simétrica','SHA-2','Assimétrica','MD5'],[0,2],
 'Na criptografia simétrica, a mesma chave cifra e decifra (AES). Na assimétrica, há um par de chaves, pública e privada (RSA). SHA-2 e MD5 são funções de hash, que não cifram: só geram um resumo de mão única.',
 ['defesa:5.3','defesa:5.4','defesa:5.7'])
Q(81,3,'Você suspeita que alguém tenta invadir a rede por um dos aplicativos e quer usar o netstat para ver as conexões TCP de cada aplicativo (processo). Qual opção usar?',
 ['netstat -a','netstat -e','netstat -r','netstat -o'],[3],
 'O -o mostra o PID (identificador do processo) dono de cada conexão, o que permite ligá-la ao aplicativo no Gerenciador de Tarefas. O -a lista todas as conexões e portas, o -e mostra estatísticas da interface e o -r mostra a tabela de roteamento. Combinado como "netstat -abno", também aparece o nome do executável.',
 ['endpoint:21.1','fundamentos:20.5'])
M(82,4,'Complete a frase: "____ usa dados públicos para coletar informações sobre um alvo."',
 [('Termo','Reconhecimento passivo')],['Reconhecimento ativo','Reconhecimento passivo','Verificação de vulnerabilidades','Teste de vulnerabilidade'],
 'No reconhecimento passivo, o atacante pesquisa fontes públicas (site da empresa, redes sociais, DNS) sem interagir com o sistema-alvo. O ativo interage com o alvo, por exemplo com uma varredura de portas.',
 ['ameacas:10.2','ameacas:13.2'])
Q(83,4,'O que é usado para encontrar possíveis vulnerabilidades em um sistema de computador?',
 ['Teste de penetração','Autenticação','Kill chains','Bancos de dados de vulnerabilidades'],[0],
 'O teste de penetração examina o sistema ativamente, como um atacante faria, para encontrar e confirmar falhas. Bancos de vulnerabilidades (como o CVE) catalogam falhas conhecidas, mas não examinam o seu sistema.',
 ['ameacas:10.1','ameacas:8.1'])
Q(84,1,'Você está implantando uma VPN para os representantes de vendas e precisa verificar a identidade de quem se conecta. O que mudar na política de conexão?',
 ['Exigir um aplicativo de senha de uso único (OTP) além das credenciais.','Exigir troca de senha a cada 30 dias.','Aumentar o tamanho mínimo da senha.','Exigir senhas complexas.'],[0],
 'A OTP acrescenta um segundo fator ("algo que você tem", o celular) à senha, e isso é autenticação multifator. As outras opções só endurecem a senha, que continua sendo um único fator.',
 ['defesa:9.5','defesa:9.4'])
Q(85,3,'Os logs de segurança do Windows mostram várias tentativas suspeitas de logon com o usuário Administrador, como em um ataque de força bruta. Qual política de senha você deve ajustar?',
 ['Reduzir o prazo de troca de senha.','Exigir senhas complexas.','Limitar o número de tentativas de logon.','Aumentar o tamanho mínimo da senha.'],[2],
 'O limite de tentativas (bloqueio de conta) trava a conta depois de algumas falhas, e o atacante não consegue mais testar milhares de senhas. As outras medidas deixam a senha mais difícil, mas não param as tentativas.',
 ['endpoint:21.4','defesa:11.5','endpoint:12.5'])
M(86,2,'Para cada servidor, indique Sim se ele costuma ficar na DMZ da empresa ou Não se não costuma.',
 [('Serviços de diretório','Não'),('E-mail','Sim'),('Impressão','Não'),('Web','Sim')],['Sim','Não'],
 'Na DMZ ficam os servidores que precisam atender o público, como web e e-mail. O servidor de impressão e o de diretório (contas de usuários) atendem só a rede interna e devem ficar protegidos dentro dela.',
 ['defesa:16.2','endpoint:16.2'])
Q(87,3,'O servidor DNS não consegue resolver alguns nomes, e você quer que, no nslookup, ele consulte outros servidores quando não tiver a resposta. Qual comando usar?',
 ['set recurse','set querytype','set domain','set retry'],[0],
 'No modo interativo do nslookup, "set recurse" pede consulta recursiva: o servidor busca a resposta em outros servidores DNS. O querytype escolhe o tipo de registro, o domain define o domínio padrão e o retry o número de tentativas.',
 ['fundamentos:20.4','dispositivos:10.1'])
Q(88,3,'Qual afirmação é verdadeira sobre o malware sem arquivo (fileless) que usa o PowerShell do Windows?',
 ['A maioria dos aplicativos o vê como processo confiável e legítimo.','Ele roda a partir do disco rígido do computador.','É facilmente detectado pelo antimalware.','Exige que o invasor crie e instale ferramentas próprias.'],[0],
 'O malware sem arquivo roda na memória usando ferramentas que já existem no sistema, como o PowerShell, que é confiável e tem amplo acesso. Como não grava arquivos no disco, escapa da detecção por assinatura e não precisa de ferramentas novas.',
 ['endpoint:20.3','endpoint:6.4'])
Q(89,5,'Qual campo de uma mensagem syslog indica onde está o dispositivo em que o evento ocorreu?',
 ['Carimbo de data e hora','Gravidade','Nome do host','Facilidade (facility)'],[2],
 'O nome do host (ou endereço) identifica o equipamento que gerou a mensagem. A gravidade indica o nível do problema (0 a 7), a facilidade indica o tipo de processo que gerou a mensagem e o carimbo de hora indica quando ocorreu.',
 ['defesa:29.2','defesa:27.1'])
Q(90,2,'Qual tecnologia protege o tráfego enquanto ele atravessa uma rede não protegida?',
 ['VPN','Firewall','IPS','NAC'],[0],
 'A VPN cifra o tráfego dentro de um túnel, de modo que quem estiver no caminho não consegue ler nem alterar os dados. Firewall e IPS filtram o tráfego, e o NAC controla quem entra na rede.',
 ['endpoint:17.7','defesa:27.6'])
Q(91,3,'Antes de instalar um patch no servidor de produção, um técnico precisa testá-lo em diferentes ambientes Windows. Qual solução oferece isso?',
 ['Área restrita (sandbox) virtualizada','Windows Server Update Services','Sistema de não produção','Imagem de linha de base'],[0],
 'A sandbox virtualizada permite criar vários ambientes isolados (versões diferentes do Windows, por exemplo), testar o patch e descartar tudo sem risco. O WSUS distribui atualizações, mas não testa.',
 ['endpoint:29.3','endpoint:26.3','defesa:25.1'])
Q(92,1,'Qual lei um hospital dos EUA deve cumprir ao investigar incidentes que envolvem dados médicos dos pacientes?',
 ['FISMA','HIPAA','FERPA','PCI DSS'],[1],
 'A HIPAA protege a privacidade das informações de saúde e vale para hospitais, clínicas e planos de saúde. A FERPA é para registros escolares, o PCI DSS para dados de cartão e a FISMA para agências federais.',
 ['ameacas:2.7','ameacas:2.5'])
Q(93,3,'Você quer que o netstat mostre apenas as conexões UDP. Qual opção usar?',
 ['netstat -a','netstat -n','netstat -s','netstat -p'],[3],
 'O -p escolhe o protocolo (por exemplo, "netstat -p udp"). O -a mostra todas as conexões, o -n mostra endereços numéricos e o -s mostra estatísticas por protocolo.',
 ['endpoint:21.1','fundamentos:20.5'])
Q(94,3,'Qual afirmação é verdadeira sobre a detecção por assinatura?',
 ['É eficaz contra explorações de dia zero.','Tem regras que identificam a estrutura suspeita de um malware.','Usa um banco de assinaturas de malware para procurar um padrão de bits ou um hash.','É eficaz contra vírus compactados.'],[2],
 'A detecção por assinatura compara arquivos com padrões e hashes de malware conhecido. Por isso não detecta ameaças de dia zero, ainda sem assinatura, nem variantes modificadas. Regras sobre estrutura suspeita são detecção heurística.',
 ['endpoint:12.2','endpoint:28.3','endpoint:5.6'])
Q(95,5,'Segundo o NIST, em que fase do ciclo de resposta a incidentes é feita a correlação de eventos?',
 ['Atividade pós-incidente','Contenção, erradicação e recuperação','Detecção e análise','Preparação'],[2],
 'Na detecção e análise, a equipe junta logs e alertas de várias fontes (correlação) para decidir se houve um incidente e qual o seu alcance.',
 ['ameacas:16.6','defesa:29.5'])
Q(96,1,'Qual lei dos EUA exige que as faculdades protejam a privacidade das informações dos alunos?',
 ['HIPAA','PCI DSS','GDPR','FERPA'],[3],
 'A FERPA protege os registros educacionais dos estudantes em instituições de ensino americanas.',
 ['ameacas:2.7'])
Q(97,2,'Engenheiros que trabalham de casa precisam acessar servidores na LAN da empresa. Qual porta TCP liberar no firewall para um acesso remoto seguro?',
 ['23','21','22','20'],[2],
 'A porta 22 é a do SSH, que cifra a sessão de acesso remoto. A 23 é o Telnet (texto claro, inseguro), e 20 e 21 são do FTP.',
 ['defesa:15.3','fundamentos:19.5','fundamentos:18.6'])
Q(98,3,'Que recurso o antimalware usa para isolar os arquivos infectados no computador?',
 ['Recuperação do Windows','Quarentena','Windows Update','Área restrita (sandbox)'],[1],
 'A quarentena move o arquivo infectado para um local isolado, onde ele não pode ser executado, mas ainda pode ser restaurado se for um falso positivo. A sandbox serve para executar e observar arquivos suspeitos.',
 ['endpoint:21.5','endpoint:12.2'])
Q(99,4,'Que tipo de backup deve ser feito em um servidor novo?',
 ['Incremental','Diferencial','Completo','Espelho'],[2],
 'O primeiro backup precisa ser completo, porque incrementais e diferenciais só copiam o que mudou desde um backup anterior. Sem um completo, não há base para eles.',
 ['defesa:18.9'])
Q(100,5,'Os e-mails de phishing aumentaram. O que a equipe pode implementar para reduzir o tempo de detecção e resposta de forma automática, com o mínimo de intervenção humana?',
 ['Fazer uma varredura de vulnerabilidades.','Implementar SOAR.','Implementar SIEM.','Fazer uma captura de pacotes.'],[1],
 'O SOAR automatiza a resposta com fluxos de trabalho (playbooks): pode, por exemplo, analisar o e-mail suspeito, bloquear o remetente e abrir o chamado sozinho. O SIEM detecta e correlaciona, mas a resposta depende do analista.',
 ['defesa:29.6','ameacas:9.6'])
