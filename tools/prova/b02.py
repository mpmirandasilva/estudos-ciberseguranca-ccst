M(26,2,'Complete as frases com o termo certo.',
 [('Um computador pode executar várias ____, cada uma com o próprio sistema operacional e aplicativos.','máquinas virtuais'),('Um(a) ____ é um aplicativo virtualizado junto com as suas dependências.','contêineres'),('Um(a) ____ é o software que permite rodar vários sistemas operacionais na mesma máquina física.','hipervisores')],['máquinas virtuais','contêineres','hipervisores'],
 'A máquina virtual é um computador completo simulado, com o próprio sistema operacional. O contêiner empacota só o aplicativo e as dependências, e compartilha o kernel do sistema. O hipervisor é a camada que cria e gerencia as máquinas virtuais sobre o hardware físico.',
 ['defesa:25.1','defesa:25.2','dispositivos:3.6'])
M(27,1,'Relacione cada política de segurança à sua descrição.',
 [('Política de uso aceitável','Define as regras que usuários ou clientes devem seguir ao usar os recursos de computação'),('Política de identificação e autenticação','Define quem pode acessar os recursos da rede e como esses usuários são verificados'),('Política de acesso à rede','Identifica quais recursos e usos da rede são aceitáveis para a organização'),('Política de manutenção de rede','Define os procedimentos de atualização dos sistemas dos dispositivos e dos aplicativos'),('Política de acesso remoto','Define as condições de acesso de quem se conecta à rede pela WAN'),('Política de senha','Trata do comprimento, quantidade e tipo de caracteres das senhas de logon')],None,
 'Cada política responde a uma pergunta: o que posso fazer com os recursos (uso aceitável), quem entra e como prova quem é (identificação e autenticação), o que a rede permite (acesso à rede), como os sistemas são atualizados (manutenção), como se entra de fora (acesso remoto) e como deve ser a senha (senha).',
 ['ameacas:1.3','endpoint:30.4','defesa:4.3'])
M(28,1,'Relacione cada controle de segurança ao seu tipo.',
 [('Novas fechaduras biométricas são instaladas','Preventivo'),('Um disco com falha é trocado e o backup é restaurado','Corretivo'),('Câmeras de vigilância são instaladas no perímetro do prédio','De detecção (investigativo)')],['Preventivo','Corretivo','De detecção (investigativo)'],
 'A fechadura impede a entrada de quem não é autorizado (preventivo). Trocar o disco e restaurar o backup conserta uma falha que já aconteceu (corretivo). A câmera registra e ajuda a descobrir o que ocorreu (detecção). Câmeras visíveis também têm efeito dissuasivo, mas a apostila as classifica como investigativas.',
 ['ameacas:5.2','ameacas:5.1'])
Q(29,2,'Uma organização quer um dispositivo ou serviço que esconda o endereço IP corporativo e funcione como intermediário entre os usuários internos e a internet. Do que ela precisa?',
 ['Servidor RADIUS','IDS (sistema de detecção de intrusão)','Servidor proxy','VPN (rede privada virtual)'],[2],
 'O servidor proxy fica entre a rede interna e a internet e faz as requisições em nome dos usuários, usando o próprio endereço. Assim, os endereços internos ficam escondidos. O RADIUS autentica usuários, o IDS detecta intrusões e a VPN cria um túnel cifrado.',
 ['endpoint:16.3','defesa:23.2','defesa:2.1'])
Q(30,2,'Quais duas opções são ferramentas de monitoramento de segurança de rede? (Escolha 2.)',
 ['Firewalls','Wireshark','SPAN','SIEM'],[1,3],
 'O SIEM coleta e correlaciona logs e eventos de toda a rede para detectar e investigar ameaças, e o Wireshark captura e analisa o tráfego. O firewall é um controle que filtra tráfego, e o SPAN (espelhamento de portas) é um recurso do switch que copia o tráfego para uma ferramenta de monitoramento, mas não analisa nada sozinho.',
 ['defesa:29.5','ameacas:9.7','endpoint:17.4'])
Q(31,3,'Qual recurso do Windows garante que os dados dos notebooks dos funcionários fiquem protegidos em caso de perda ou roubo?',
 ['Defender Credential Guard','BitLocker','Firewall','Segurança do Windows'],[1],
 'O BitLocker criptografa o disco inteiro. Se o notebook for roubado, quem tirar o disco não consegue ler os dados sem a chave. O firewall protege a rede, e o Credential Guard protege credenciais em memória, não o disco.',
 ['endpoint:26.5','endpoint:26.8'])
Q(32,1,'Qual termo descreve um ponto fraco em uma rede, um sistema ou um dispositivo?',
 ['Ameaça','Ataque','Vulnerabilidade','Exploração'],[2],
 'Vulnerabilidade é a fraqueza. A ameaça é o perigo em potencial que pode aproveitá-la, a exploração é o ato de aproveitá-la e o ataque é a ação do invasor.',
 ['endpoint:2.2','defesa:1.2'])
M(33,2,'Complete as frases com o tipo de nuvem.',
 [('Uma nuvem ____ é compartilhada por organizações de uma mesma área, como saúde ou bancos.','comunidade'),('Uma nuvem ____ costuma ficar atrás de um firewall e é usada por uma única organização.','privada'),('Uma nuvem ____ é usada por quem precisa de nuvem privada para os funcionários, mas usa nuvem pública para aplicativos não críticos.','híbrida')],['comunidade','híbrida','privada','pública'],
 'Comunitária: várias organizações com necessidades parecidas dividem a mesma nuvem. Privada: exclusiva de uma organização. Híbrida: mistura de privada e pública. A pública atende qualquer cliente pela internet.',
 ['dispositivos:3.3','defesa:25.5'])
Q(34,3,'Um técnico precisa identificar drivers não assinados instalados no Windows 10. Quais três ferramentas nativas fazem isso? (Escolha 3.)',
 ['driverquery','msinfo32','sfc','sigverif','Gerenciador de Tarefas'],[0,1,3],
 'O sigverif verifica as assinaturas dos arquivos, o driverquery lista os drivers com detalhes (inclusive a assinatura) e o msinfo32 mostra os drivers registrados e o estado de cada um. O sfc verifica a integridade dos arquivos do sistema, e o Gerenciador de Tarefas mostra processos e serviços, sem tratar de assinaturas.',
 ['endpoint:19.1','endpoint:20.3','endpoint:26.6'])
M(35,1,'Complete a frase: "Um(a) ____ é a possibilidade de um ataque a um sistema ou a uma rede."',
 [('Termo','ameaça')],['ameaça','vulnerabilidade','exploração','rootkit'],
 'A ameaça é o perigo potencial, a possibilidade de um ataque. A vulnerabilidade é a fraqueza, a exploração é o aproveitamento da fraqueza e o rootkit é um tipo de malware.',
 ['endpoint:2.2','ameacas:4.3'])
Q(36,2,'Funcionários que trabalham de casa precisam acessar com segurança a LAN da empresa. Qual tecnologia protege esse tráfego?',
 ['IPsec','Túnel GRE','VLAN','QoS'],[0],
 'O IPsec é o conjunto de protocolos que cria VPNs seguras, com criptografia, integridade e autenticação. O GRE cria túneis, mas sem criptografia; a VLAN separa redes locais; o QoS prioriza tráfego.',
 ['endpoint:17.7','defesa:27.6'])
M(37,3,'Relacione cada evento do Windows ao tipo de evento.',
 [('Um serviço não carrega durante a inicialização','Erro'),('Um usuário tenta, sem sucesso, acessar uma unidade de rede','Auditoria sem êxito'),('Um driver de rede é carregado com sucesso','Informações'),('Um usuário entra no sistema','Auditoria com êxito'),('Um disco está com pouco espaço livre','Aviso')],['Erro','Auditoria sem êxito','Informações','Auditoria com êxito','Aviso'],
 'Informações: operação bem-sucedida. Aviso: algo que pode virar problema (pouco espaço). Erro: problema significativo (serviço que não carrega). As auditorias registram tentativas de acesso auditadas: com êxito (logon bem-sucedido) ou sem êxito (acesso negado).',
 ['endpoint:21.2','defesa:29.1'])
Q(38,4,'Quais três tipos de dados as plataformas de inteligência de ameaças (TIPs) coletam? (Escolha 3.)',
 ['Ferramentas (táticas), técnicas e procedimentos','Capacidade de resposta a incidentes','Procedimentos operacionais padrão','Informações de reputação','Indicadores de comprometimento'],[0,3,4],
 'A TIP reúne IOCs (vestígios de ataques), TTPs (como os atacantes agem) e informações de reputação de domínios e endereços. A apostila escreve "ferramentas, técnicas e procedimentos"; o nome correto de TTP é táticas, técnicas e procedimentos.',
 ['ameacas:6.6','endpoint:2.9'])
M(39,1,'Relacione cada método de autenticação ao fator correspondente.',
 [('Reconhecimento facial','Algo que você é'),('Token por SMS','Algo que você tem'),('Número de PIN','Algo que você sabe')],['Algo que você é','Algo que você tem','Algo que você sabe'],
 'A biometria (rosto, digital) é algo que você é. O código enviado por SMS depende do celular que você tem. O PIN é algo que você memorizou.',
 ['defesa:9.4','defesa:9.5'])
Q(40,2,'Por que é importante bloquear a entrada na rede de pacotes com endereço de broadcast ou com endereços IP privados reservados como origem?',
 ['Os firewalls não conseguem detectar endereços privados.','Bloqueá-los evita o esgotamento dos endereços IPv4.','Esses endereços costumam ser roteados pela internet pelas empresas.','Esses endereços são usados com facilidade em ataques de falsificação de IP.'],[3],
 'Endereços privados e de broadcast nunca deveriam chegar da internet. Se aparecem como origem, quase certamente foram falsificados (IP spoofing), por exemplo em ataques de amplificação. Por isso a borda filtra essas origens com ACLs.',
 ['defesa:22.1','fundamentos:12.7','endpoint:7.7'])
Q(41,4,'Qual prática de segurança procura impedir, de forma proativa, a exploração de pontos fracos de software e sistemas?',
 ['Gerenciamento de ativos','Gerenciamento de configuração','Gerenciamento de riscos','Gerenciamento de vulnerabilidades'],[3],
 'O gerenciamento de vulnerabilidades identifica, prioriza e corrige as falhas antes que sejam exploradas, em um ciclo contínuo. O de ativos mantém o inventário, o de configuração controla as configurações e o de riscos decide como tratar cada risco.',
 ['ameacas:12.1','ameacas:12.5'])
Q(42,2,'Ao configurar uma rede doméstica, que efeito de segurança tem ocultar o SSID (SSID cloaking)?',
 ['Reduz o tráfego sem fio que precisa de criptografia.','Exige que o SSID seja configurado manualmente nos clientes.','Esconde o conteúdo do tráfego sem fio.','Impede que dispositivos específicos acessem a rede.'],[1],
 'Ocultar o SSID desliga o anúncio do nome da rede, então quem quiser conectar precisa digitá-lo. É uma proteção fraca, porque o SSID aparece em outros quadros e pode ser descoberto. Não criptografa nada e não bloqueia aparelhos (isso seria filtro de MAC).',
 ['endpoint:15.1','fundamentos:7.8'])
Q(43,4,'Um invasor envia tráfego para uma mesma porta em todos os hosts de um segmento para ver em quais ela está ativa. Que técnica de varredura é essa?',
 ['Sweep scan (varredura de hosts)','Bounce scan','Ping scan','Vanilla scan'],[0],
 'Na varredura de hosts (sweep, ou port sweeping), o alvo é um serviço: a mesma porta em muitos hosts. Na varredura de portas clássica (vanilla), o alvo é um host: muitas portas dele. O ping scan só descobre quais hosts respondem.',
 ['ameacas:9.3','defesa:15.1'])
Q(44,2,'Um invasor compromete o servidor da empresa para que um nome de domínio seja redirecionado a um site fraudulento. Que ataque é esse?',
 ['Falsificação de ARP','Falsificação de DHCP','Falsificação de DNS','Falsificação de IP'],[2],
 'Na falsificação (ou envenenamento) de DNS, o invasor altera os registros que traduzem nomes em endereços, e a vítima digita o nome certo mas chega ao site falso. ARP troca endereços MAC na rede local, DHCP entrega configurações falsas e IP spoofing falsifica a origem dos pacotes.',
 ['endpoint:10.1','endpoint:10.2','defesa:27.2'])
Q(45,2,'A política de BYOD exige a criptografia mais forte para o acesso de convidados à rede sem fio. Qual método deve estar ativado no aparelho?',
 ['WEP','WPA2','SSH','3DES','AES'],[4],
 'O AES é o algoritmo de criptografia mais forte da lista e é o usado pelo WPA2 e pelo WPA3. O WEP é quebrado, o 3DES é antigo e o SSH é um protocolo de acesso remoto. A apostila pede o algoritmo (AES), e não o protocolo (WPA2).',
 ['endpoint:15.4','defesa:17.1','defesa:5.3'])
M(46,4,'Relacione cada atividade de segurança à sua descrição.',
 [('Processo de auditoria','Exame independente de registros e atividades para ver se os controles garantem a conformidade com as políticas'),('Garantia da informação','Documentação que dá alto grau de confiança de que as medidas de segurança estão em vigor'),('Avaliação de segurança','Processos para avaliar a segurança de todo o sistema ou em resposta a um evento'),('Monitoramento do sistema','Acompanhamento contínuo e em tempo real da rede e dos dispositivos em busca de anomalias')],None,
 'A auditoria é independente e compara a prática com a política. A garantia da informação é a evidência documentada de que a segurança funciona. A avaliação examina a segurança como um todo, e o monitoramento observa continuamente para detectar anomalias.',
 ['ameacas:8.4','ameacas:5.3','defesa:29.5'])
M(47,1,'Relacione cada ataque de engenharia social à sua descrição.',
 [('Vishing','Usa chamadas de voz para convencer a vítima a entregar dados confidenciais'),('Phishing','Envia e-mails em massa para coletar informações para fraude ou roubo de identidade'),('Smishing','Usa mensagens de texto falsas para obter dados da conta ou instalar malware'),('Spear phishing','Envia e-mails feitos sob medida para uma pessoa específica da organização')],None,
 'Todas são variações de phishing: muda o canal (voz no vishing, SMS no smishing) ou o alvo (em massa no phishing comum, uma pessoa específica no spear phishing, executivos no whaling).',
 ['endpoint:6.8','endpoint:4.1'])
Q(48,1,'Em uma violação, criminosos expuseram dados corporativos confidenciais. Qual componente da tríade CIA foi violado?',
 ['Integridade','Confidencialidade','Disponibilidade'],[1],
 'Dados confidenciais expostos a quem não deveria vê-los significam violação da confidencialidade.',
 ['endpoint:1.2','defesa:1.1'])
M(49,5,'Relacione cada fase do ciclo de resposta a incidentes do NIST a uma atividade de exemplo.',
 [('Preparação','Criar a equipe de resposta a incidentes'),('Detecção e análise','Determinar se ocorreu um incidente'),('Contenção, erradicação e recuperação','Validar o endereço IP do host atacante'),('Atividade pós-incidente','Fazer a reunião de lições aprendidas')],None,
 'Na preparação, a equipe é formada e equipada. Na detecção e análise, decide-se se houve incidente. Na contenção, erradicação e recuperação, entre outras ações, o atacante é investigado (como validar o IP dele). No pós-incidente, a reunião de lições aprendidas melhora o processo. O ciclo é descrito na publicação NIST SP 800-61 (a apostila cita a SP 800-86, que trata da perícia forense).',
 ['ameacas:16.4','ameacas:16.7','ameacas:16.8'])
M(50,4,'Complete a frase: "____ é usado para encontrar vulnerabilidades em um sistema de computador."',
 [('Termo','Teste de penetração')],['Um firewall','Teste de penetração','Spyware','Testes de sistema'],
 'O teste de penetração simula ataques autorizados para encontrar (e explorar) pontos fracos. O firewall filtra tráfego, o spyware é malware e os testes de sistema verificam funcionalidades, não segurança.',
 ['ameacas:10.1','ameacas:8.1'])
