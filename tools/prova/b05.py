Q(101,5,'Você precisa analisar tendências nas ações que afetam o armazenamento de arquivos na rede. Qual log mostra isso?',
 ['Log do serviço de replicação de arquivos','Log do sistema','Log de dados','Log de segurança'],[2],
 'Os logs de dados registram como dados, arquivos e aplicativos são armazenados, acessados e modificados, e por isso mostram tendências de uso do armazenamento. O log de segurança foca logons e auditoria, e o do sistema foca drivers e serviços.',
 ['defesa:3.3','defesa:29.1'])
M(102,5,'Relacione cada componente da resposta a incidentes do NIST à sua descrição.',
 [('Política de resposta a incidentes','Define o propósito, os objetivos e o escopo, com a priorização dos incidentes e as medidas de desempenho'),('Plano de resposta a incidentes','Define a abordagem, as estratégias e os recursos, e como a equipe se comunica com as partes internas e externas'),('Procedimentos de resposta a incidentes','Reúnem os SOPs detalhados a seguir durante a resposta')],None,
 'A política diz o quê e por quê (escopo, objetivos, prioridades). O plano diz como a organização vai se estruturar (estratégia, recursos, comunicação). Os procedimentos são o passo a passo técnico (SOPs).',
 ['ameacas:16.1'])
M(103,1,'Relacione cada tipo de ameaça interna (infiltrado) a um exemplo.',
 [('Infiltrado mal-intencionado','Um funcionário rouba especificações técnicas de um produto para ganho pessoal'),('Infiltrado negligente','Um funcionário leva para casa, sem autorização, um disco que é roubado do carro dele'),('Infiltrado comprometido','Um funcionário entrega as credenciais em um spear phishing, e o invasor as usa em novos ataques')],None,
 'O mal-intencionado age de propósito. O negligente não tem má intenção, mas descumpre as regras e causa o problema. O comprometido é vítima: o atacante usa a conta dele.',
 ['endpoint:2.4','endpoint:3.3'])
Q(104,2,'Um DoS impede o servidor de atender os clientes porque ele fica esperando fechar sessões semiabertas da camada 4 com o atacante. Que ataque é esse?',
 ['Inundação de SYN','Falsificação de DNS','Esgotamento (starvation) de DHCP','Inundação de UDP'],[0],
 'Na inundação de SYN, o atacante envia muitos pedidos de conexão TCP (SYN) e nunca completa o handshake. O servidor guarda cada conexão semiaberta esperando o ACK final, até esgotar os recursos.',
 ['endpoint:8.3','endpoint:8.2'])
Q(105,3,'Qual tecnologia a empresa deve usar para aplicar as políticas corporativas aos dispositivos BYOD que se conectam à rede?',
 ['QoS','IPS','NAC','VPN'],[2],
 'O NAC verifica se cada dispositivo cumpre a política (antivírus, patches, configuração) antes de liberar o acesso, o que é essencial com aparelhos pessoais.',
 ['defesa:10.4','defesa:4.4'])
Q(106,5,'Em que fase do ciclo de resposta a incidentes do NIST você investiga os alertas do sensor de detecção de intrusão?',
 ['Detecção e análise','Contenção, erradicação e recuperação','Atividade pós-incidente','Preparação'],[0],
 'Investigar alertas para decidir se houve um incidente é o centro da fase de detecção e análise.',
 ['ameacas:16.6','defesa:30.4'])
Q(107,3,'Um técnico tenta instalar no Windows 10 de 64 bits uma versão de driver baixada da internet, e a instalação falha. Qual é o problema?',
 ['O driver não tem assinatura digital.','O driver tem um certificado de 32 bits.','O driver foi emitido por um fornecedor terceirizado.','O driver não tem certificado emitido pela Microsoft.'],[0],
 'O Windows de 64 bits exige drivers assinados digitalmente: a assinatura prova quem publicou o pacote e que ele não foi alterado. Drivers de outros fornecedores são aceitos, desde que assinados.',
 ['defesa:7.3','defesa:7.1','endpoint:26.6'])
Q(108,3,'Qual é a ferramenta de criptografia de disco embutida no macOS?',
 ['FileVault','GnuPG','BitLocker','Defender'],[0],
 'O FileVault criptografa o disco do Mac, assim como o BitLocker faz no Windows. O GnuPG criptografa arquivos e e-mails, e o Defender é o antivírus do Windows.',
 ['endpoint:26.5','endpoint:26.7'])
Q(109,4,'Qual destas é uma fonte externa de risco para uma organização?',
 ['Desastre natural, como terremoto ou enchente','Hardware obsoleto ou fora do suporte','Falta de criptografia nos bancos de dados locais','Documentação do programa desatualizada'],[0],
 'Fontes externas vêm de fora da organização: desastres naturais, terrorismo, pandemias, ataques de criminosos. As outras opções são fraquezas internas, que a própria empresa criou e pode corrigir.',
 ['ameacas:4.3','ameacas:17.1'])
Q(110,5,'Qual classificação de alerta deve ser escalada para os investigadores de segurança?',
 ['Verdadeiro positivo','Falso positivo','Verdadeiro negativo','Falso negativo'],[0],
 'O verdadeiro positivo é o alerta que corresponde a um incidente real; ele segue para o nível superior. O falso positivo leva a ajustar as regras, e o falso negativo (ataque sem alerta) só é descoberto depois.',
 ['defesa:30.4'])
Q(111,5,'No plano de recuperação de desastres, a empresa decide assinar um serviço de nuvem para guardar arquivos e backups. Que tipo de serviço ela precisa?',
 ['IaaS','BaaS','SaaS','PaaS'],[2],
 'O gabarito considera SaaS, porque armazenamento de arquivos e backup são oferecidos como aplicativos prontos (como um serviço de armazenamento online). No IaaS a empresa alugaria a infraestrutura e montaria tudo; no PaaS, uma plataforma para desenvolver.',
 ['defesa:25.4','dispositivos:3.2'])
Q(112,5,'O que ajuda a identificar eventos suspeitos na rede enquanto eles acontecem?',
 ['SIEM','ACL','nslookup','netstat'],[0],
 'O SIEM reúne e correlaciona logs de toda a rede em tempo real e gera alertas. A ACL filtra tráfego, e nslookup e netstat são comandos de consulta pontual.',
 ['defesa:29.5','ameacas:9.5'])
Q(113,5,'Em uma investigação forense, o supervisor pede uma duplicata do disco antes de examiná-lo. Para que serve isso?',
 ['Preservar o estado original do disco.','Ter uma cópia de backup do disco.','Permitir examinar os dois discos ao mesmo tempo.','Comparar as pegadas digitais dos dois discos.'],[0],
 'A análise é feita na cópia bit a bit, para não alterar a prova original (nem os carimbos de hora). O original fica guardado e pode ser comparado por hash para provar que não houve adulteração.',
 ['ameacas:15.6','ameacas:15.5'])
Q(114,2,'Durante um ataque de negação de serviço, qual tecnologia toma medidas automáticas para tentar pará-lo?',
 ['IDS','IPS','NAT','Servidor proxy'],[1],
 'O IPS fica em linha com o tráfego e pode bloquear pacotes automaticamente. O IDS só alerta. O NAT traduz endereços e o proxy intermedeia conexões.',
 ['endpoint:16.4','endpoint:16.5','endpoint:12.6'])
Q(115,4,'A empresa tem uma vulnerabilidade a DoS. Qual processo reduz a probabilidade do ataque?',
 ['Mitigação','Detecção','Reconhecimento','Identificação'],[0],
 'Mitigar é reduzir a probabilidade ou o impacto do risco com controles. Detectar é descobrir o ataque; identificar e reconhecer fazem parte do levantamento dos riscos.',
 ['ameacas:4.6','endpoint:12.6'])
Q(116,4,'Qual ferramenta um invasor usaria para descobrir os serviços que rodam em um servidor?',
 ['Nmap','Wireshark','hping','nslookup'],[0],
 'O Nmap faz varredura de portas e identifica os serviços (e até o sistema operacional) do alvo. O Wireshark captura tráfego, o hping monta pacotes e o nslookup consulta o DNS.',
 ['ameacas:9.3','ameacas:9.1'])
M(117,3,'Relacione cada boa prática de verificação dos endpoints ao motivo.',
 [('Os dispositivos são gerenciados remotamente pela equipe de segurança','Permite acessar, restaurar e proteger recursos e aplicativos em caso de roubo'),('Funções desnecessárias do navegador estão desativadas','Reduz a execução automática de código malicioso vindo de sites fraudulentos'),('A criptografia de arquivos está ativada e funcionando','Reduz o risco de exposição dos dados se o dispositivo for roubado')],None,
 'O gerenciamento remoto (MDM) permite agir sobre o aparelho mesmo longe dele, a redução da superfície do navegador corta caminhos de ataque e a criptografia deixa os dados ilegíveis para o ladrão.',
 ['ameacas:12.3','endpoint:26.5','endpoint:29.1'])
Q(118,3,'Qual é o termo para o conjunto de ferramentas que dá ao invasor acesso de administrador a um computador?',
 ['Rootkit','Backdoor','Worm','Keylogger'],[0],
 'O rootkit dá acesso de nível root (administrador) e esconde a presença do invasor, alterando o sistema. O backdoor é só uma porta de entrada, o worm se propaga e o keylogger registra o que é digitado.',
 ['endpoint:5.2','endpoint:25.5'])
Q(119,2,'Que ataque monta um servidor falso na rede para entregar aos hosts configurações de IP incorretas?',
 ['Falsificação de DHCP','Falsificação de DNS','Falsificação de IP','Falsificação de ARP'],[0],
 'Na falsificação de DHCP, o servidor falso responde antes do legítimo e entrega gateway ou DNS do atacante, o que permite interceptar o tráfego. A defesa é o DHCP snooping.',
 ['endpoint:9.5','endpoint:9.4'])
Q(120,3,'Quais dois são exemplos de ataque de elevação de privilégio? (Escolha 2.)',
 ['Rooting','Quebra (cracking)','Invasão','Jailbreaking'],[0,3],
 'Rooting (no Android) e jailbreaking (no iOS) removem as restrições do sistema e dão acesso de administrador, o que é elevação de privilégio. Isso também desliga proteções importantes do aparelho.',
 ['defesa:10.2','defesa:17.6'])
Q(121,1,'Qual ataque de engenharia social mira pessoas do alto escalão?',
 ['Whaling','Vishing','Pharming','Smishing'],[0],
 'O whaling ("caça à baleia") mira executivos, os "peixes grandes" da empresa.',
 ['endpoint:6.8'])
Q(122,1,'Você instala um aplicativo que parecia legítimo, mas ele traz um keylogger. Qual elemento da tríade CIA foi comprometido?',
 ['Confidencialidade','Disponibilidade','Integridade'],[0],
 'O keylogger captura o que você digita, como senhas e mensagens, e o envia ao atacante: violação da confidencialidade.',
 ['endpoint:5.3','endpoint:1.2'])
Q(123,2,'O que é usado para autenticar e verificar a identidade de um site?',
 ['Certificado digital','Endereço IP do site','Assinatura de código','Nome de domínio do site'],[0],
 'O certificado digital, emitido por uma autoridade certificadora, liga a chave pública do site à sua identidade. O navegador o verifica antes de estabelecer o HTTPS. A assinatura de código autentica software, não sites.',
 ['defesa:7.4','defesa:7.5','defesa:27.3'])
Q(124,2,'Que ataque intercepta e altera os dados enviados entre dois hosts?',
 ['Man-in-the-middle','Phishing','Injeção de SQL','Ataque de dicionário'],[0],
 'No man-in-the-middle, o atacante se coloca entre os dois lados da comunicação, podendo ler e alterar os dados sem que eles percebam.',
 ['endpoint:5.5'])
Q(125,4,'Quais são os dois objetivos de uma política de gerenciamento de mudanças? (Escolha 2.)',
 ['Garantir que as mudanças nos sistemas não prejudiquem a segurança.','Garantir que as mudanças sejam feitas sem analisar as implicações de segurança.','Garantir que a documentação seja atualizada quando os sistemas forem instalados ou alterados.','Garantir que as mudanças eliminem todos os riscos futuros.'],[0,2],
 'O gerenciamento de mudanças avalia cada alteração antes de aplicá-la, para não abrir brechas, e mantém a documentação em dia. Nenhuma mudança elimina todos os riscos.',
 ['ameacas:12.4','defesa:3.1'])
