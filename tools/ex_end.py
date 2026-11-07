# Exercícios da trilha "Segurança de Endpoint"
# mc: a primeira opção é a correta (o site embaralha). in: resposta digitada. multi: vários campos.
def mc(q,o,e,r): return {'t':'mc','q':q,'o':o,'e':e,'r':r}
def inp(q,a,n,e,r,ph=None,d=None):
    x={'t':'in','q':q,'a':a,'n':n,'e':e,'r':r}
    if ph: x['ph']=ph
    if d: x['d']=d
    return x
def multi(q,f,e,r): return {'t':'multi','q':q,'f':f,'e':e,'r':r}
def C(l,ch,a): return {'l':l,'ch':ch,'a':a}
def assoc(q,pairs,e,r):
    ch=[b for _,b in pairs]
    return multi(q,[C(a,ch,b) for a,b in pairs],e,r)

EX={}
EX[1]=[
 assoc('Associe cada situação ao objetivo da tríade CIA que foi afetado.',[
    ('Um site da loja fica fora do ar','Disponibilidade'),
    ('O valor de um extrato bancário é alterado','Integridade'),
    ('Um estagiário vê a planilha de salários','Confidencialidade')],
    'Fora do ar → disponibilidade; dado alterado → integridade; acesso indevido → confidencialidade.','1.1'),
 assoc('Indique o estado dos dados em cada caso.',[
    ('Um e-mail sendo enviado','Em trânsito'),
    ('Um backup guardado no NAS','Em repouso'),
    ('Uma planilha sendo editada','Em processamento')],
    'Os dados precisam de proteção nos três estados: em repouso, em trânsito e em processamento.','1.5'),
 mc('Qual técnica troca o dado original por um valor aleatório sem relação matemática com ele?',
    ['Tokenização','Hash','Criptografia simétrica','Compressão'],
    'Na tokenização, o token não vale nada fora do sistema que guarda a correspondência.','1.2'),
 mc('Qual é a principal desvantagem dos sistemas de armazenamento em rede (RAID, NAS e SAN)?',
    ['São mais complexos e, por concentrarem muitos dados, uma falha representa um risco maior','São mais lentos que o armazenamento local','Não têm redundância','Não podem ser monitorados'],
    'Eles são mais seguros, rápidos e redundantes, mas mais complexos de configurar, testar e monitorar.','1.5'),
]
EX[2]=[
 mc('Qual estratégia de risco é a mais usada?',
    ['Redução (mitigação)','Aceitação','Prevenção','Transferência'],
    'Reduzir a exposição ou o impacto é a forma mais comum de lidar com um risco.','2.3'),
 assoc('Associe cada ação à estratégia de risco.',[
    ('Contratar um seguro','Transferência'),
    ('Deixar de oferecer um serviço arriscado','Prevenção (evitar)'),
    ('Instalar um firewall','Redução (mitigação)'),
    ('Não fazer nada porque tratar custa mais que o risco','Aceitação')],
    'Seguro transfere; eliminar a atividade evita; controles reduzem; não agir é aceitar.','2.3'),
 mc('Por que as ameaças internas podem causar danos maiores que as externas?',
    ['O usuário interno tem acesso direto e conhece a rede, os dados e as contramedidas','Os ataques internos sempre usam malware mais avançado','A rede interna não tem firewall','Os funcionários são todos administradores'],
    'O usuário interno tem acesso ao prédio e aos equipamentos e conhece as defesas.','2.4'),
 mc('Que tipo de hacker invade sem permissão, sem buscar ganho pessoal, e depois divulga a falha?',
    ['Chapéu cinza','Chapéu branco','Chapéu preto','Script kiddie'],
    'O chapéu cinza comete atos antiéticos, mas não para ganho pessoal nem para causar dano.','2.6'),
 mc('Qual é a diferença entre IOC e IOA?',
    ['O IOC é a evidência de que um ataque ocorreu; o IOA revela a motivação e a estratégia do atacante','O IOC é usado só em redes sem fio','O IOA é a evidência de que um ataque ocorreu; o IOC revela a motivação','Não há diferença'],
    'IOCs são vestígios (hashes, IPs, arquivos); IOAs focam a motivação e a estratégia, de forma proativa.','2.9'),
]
EX[3]=[
 mc('O que é um domínio de ameaça?',
    ['Uma área de controle, autoridade ou proteção que os atacantes podem explorar para entrar em um sistema','Um nome de site malicioso','Um tipo de firewall','Uma lista de vulnerabilidades'],
    'Exemplos de domínios: usuário, dispositivo, rede local, nuvem, aplicativos e instalações.','3'),
 mc('Qual domínio é considerado o elo mais fraco da segurança?',
    ['O do usuário','O dos aplicativos','O da nuvem privada','O das instalações físicas'],
    'Nenhuma tecnologia torna os sistemas mais seguros do que o comportamento das pessoas que os usam.','3.3'),
 mc('Qual característica define uma APT (ameaça persistente avançada)?',
    ['Ataque prolongado e discreto, com malware sofisticado, contra alvos como governos e grandes organizações','Ataque rápido que derruba um site por poucos minutos','Mensagem de spam enviada a muitas pessoas','Erro de configuração de um servidor'],
    'A APT fica sem ser detectada por muito tempo e costuma ser bem financiada.','3.7'),
 mc('Na nuvem pública, quem protege os recursos de cada organização?',
    ['A própria organização; o provedor protege o ambiente','Só o provedor','Ninguém, porque a nuvem já é segura','O governo'],
    'O provedor protege o ambiente, mas cada organização protege seus próprios recursos.','3.5'),
]
EX[4]=[
 mc('O que é engenharia social?',
    ['Uma estratégia não técnica que manipula pessoas para que façam algo ou revelem informações','Um tipo de malware que se replica sozinho','Uma técnica de criptografia','Um método de varredura de portas'],
    'Ela explora a vontade das pessoas de ajudar e outras reações humanas previsíveis.','4.1'),
 assoc('Associe cada exemplo à tática de engenharia social.',[
    ('Frete grátis "por tempo limitado"','Urgência'),
    ('Item de luxo barato com "poucas unidades"','Escassez'),
    ('Uma "intimação oficial" em PDF infectado','Autoridade'),
    ('Post com dezenas de comentários falsos que o validam','Consenso (prova social)')],
    'As táticas exploram urgência, escassez, autoridade, consenso, intimidação, familiaridade e confiança.','4.2'),
 mc('Como se chama examinar o lixo do alvo em busca de informações descartadas?',
    ['Dumpster diving','Shoulder surfing','Tailgating','Pretexting'],
    'Por isso, documentos confidenciais devem ser triturados ou guardados até o descarte seguro.','4.3'),
 mc('Que controle físico impede a entrada indevida exigindo que a porta externa feche antes de a interna abrir?',
    ['Mantrap (eclusa)','Catraca comum','Câmera de vigilância','Crachá visível'],
    'O mantrap deixa passar uma pessoa por vez e impede o tailgating.','4.4'),
]
EX[5]=[
 assoc('Associe cada malware à sua característica.',[
    ('Vírus','Anexa-se a outros arquivos e em geral exige uma ação do usuário'),
    ('Worm','Replica-se sozinho explorando vulnerabilidades da rede'),
    ('Cavalo de Troia','Disfarça-se de programa legítimo'),
    ('Rootkit','Modifica o sistema para se esconder e é muito difícil de detectar')],
    'O worm não precisa de hospedeiro nem de ação do usuário depois da infecção inicial.','5.1'),
 mc('O que costuma ser necessário depois da infecção por um rootkit?',
    ['Apagar e reinstalar o sistema','Apenas reiniciar o computador','Trocar o mouse','Desativar o Wi-Fi'],
    'Como o rootkit adultera até as ferramentas de monitoramento, na maioria dos casos o computador precisa ser apagado e reinstalado.','5.2'),
 mc('Que ataque captura uma comunicação e a retransmite para enganar o destinatário?',
    ['Ataque de repetição (replay)','Inundação SYN','Bomba lógica','Smishing'],
    'O replay contorna a autenticação retransmitindo ou atrasando uma comunicação capturada.','5.5'),
 mc('O que é um ataque de dia zero?',
    ['A exploração de uma vulnerabilidade desconhecida pelo fornecedor, antes de haver correção','Um ataque feito à meia-noite','Um ataque que dura um dia','Um DoS de curta duração'],
    'Não há patch nem assinatura, por isso a defesa depende de camadas e de detecção por comportamento.','5.6'),
]
EX[6]=[
 mc('Quando a injeção de SQL funciona?',
    ['Quando o aplicativo não filtra os caracteres digitados nos campos de entrada','Quando o banco de dados está desligado','Quando o site usa HTTPS','Quando o usuário tem antivírus'],
    'A instrução SQL maliciosa é digitada em um campo e executada pelo banco.','6.2'),
 mc('O que acontece em um estouro de buffer?',
    ['Os dados são gravados além dos limites do buffer e invadem a memória de outros processos','O disco fica cheio','A rede fica lenta por excesso de tráfego','O navegador abre muitas abas'],
    'O resultado pode ser travamento, comprometimento de dados ou elevação de privilégios.','6.3'),
 mc('Por que o Meterpreter escapa dos antivírus?',
    ['Carrega extensões direto na memória, sem tocar no disco','Usa criptografia quântica','Só roda em Linux','Apaga o antivírus antes de agir'],
    'É uma carga útil do Metasploit que assume o controle do alvo pela memória.','6.4'),
 assoc('Associe cada variação de phishing.',[
    ('Por SMS','Smishing'),
    ('Por voz','Vishing'),
    ('Direcionado a uma pessoa ou empresa','Spear phishing'),
    ('Direcionado a executivos','Whaling')],
    'Todas são fraudes em que o criminoso se passa por alguém legítimo.','6.8'),
]
EX[7]=[
 mc('Por que é fácil falsificar o endereço de origem de um pacote IP?',
    ['O IP não verifica se o endereço de origem é verdadeiro','O IP criptografa os endereços','O roteador sempre corrige a origem','O IPv4 não tem campo de origem'],
    'O IP é sem conexão e não verifica a origem; isso permite o IP spoofing.','7.1'),
 inp('Quantos bytes tem o cabeçalho do IPv6?',['40'],'num','O cabeçalho do IPv6 tem oito campos e 40 bytes.','7.3',ph='bytes'),
 mc('Qual é a diferença entre IPv4 e IPv6 quanto à fragmentação?',
    ['Os roteadores não fragmentam pacotes IPv6','Os roteadores fragmentam só pacotes IPv6','O IPv6 não aceita pacotes grandes','Não há diferença'],
    'No IPv6, a fragmentação não é feita pelos roteadores do caminho.','7.3'),
 mc('No ataque Smurf, o que o atacante faz?',
    ['Envia pedidos de eco ICMP a muitos hosts com o IP da vítima como origem','Envia muitos SYN sem completar o handshake','Altera o cache ARP do gateway','Clona o SSID de um AP'],
    'Os hosts respondem à vítima, que fica sobrecarregada: amplificação e reflexão.','7.6'),
 mc('Qual é a defesa contra o uso do ICMP em reconhecimento e ataques?',
    ['Filtragem rigorosa de ICMP por ACL na borda da rede','Desligar o DHCP','Usar só IPv6','Trocar os cabos'],
    'A ACL na borda limita quais mensagens ICMP entram e saem.','7.5'),
]
EX[8]=[
 mc('Como funciona a inundação SYN?',
    ['O atacante envia muitos SYN com origens falsas, e o servidor fica com conexões semiabertas','O atacante envia pacotes RST a um dos lados','O atacante clona o MAC do servidor','O atacante envia consultas DNS longas'],
    'Esperando ACKs que nunca chegam, o servidor nega o serviço aos usuários legítimos.','8.3'),
 multi('No handshake de três vias, o cliente envia SYN com SEQ=500 e o servidor responde com SEQ=900. Complete o SYN-ACK.',[
    {'l':'ACK do SYN-ACK','a':['501'],'n':'num'},
    {'l':'SEQ do ACK final','a':['501'],'n':'num'},
    {'l':'ACK do ACK final','a':['901'],'n':'num'}],
    'Cada lado confirma o número recebido + 1: ACK=501 no SYN-ACK; o ACK final tem SEQ=501 e ACK=901.','8.2'),
 mc('Que ataque encerra uma conexão TCP de forma abrupta com um pacote falsificado?',
    ['Reset TCP (RST)','Inundação UDP','Sequestro de DNS','Bluejacking'],
    'O atacante envia um RST falsificado a um ou aos dois lados.','8.3'),
 mc('Por que o UDP é fácil de atacar?',
    ['Não tem criptografia por padrão, e a soma de verificação é opcional','Usa sempre a porta 80','Só funciona em redes sem fio','Criptografa todo o tráfego'],
    'Qualquer um pode ver o tráfego UDP, alterá-lo e reenviá-lo; o atacante pode até recalcular a soma de verificação.','8.5'),
]
EX[9]=[
 mc('Por que o ARP é vulnerável?',
    ['Não tem autenticação: qualquer host pode se declarar dono de qualquer IP ou MAC','Usa criptografia fraca','Só funciona com IPv6','Exige senha em texto claro'],
    'Os hosts guardam o par IP–MAC das respostas, inclusive do ARP gratuito, sem verificar.','9.1'),
 mc('Qual é o resultado típico do envenenamento do cache ARP?',
    ['Um MitM entre a vítima e o gateway padrão','A queda do servidor DNS','O bloqueio do Wi-Fi','A troca da senha do usuário'],
    'O atacante associa o seu MAC ao IP do gateway e passa a receber o tráfego da vítima.','9.2'),
 mc('O que faz a inundação de MAC (MAC flooding)?',
    ['Enche a tabela CAM do switch com endereços falsos','Clona o SSID da rede','Envia SYN em massa','Altera o registro do Windows'],
    'O ataque compromete a segurança do switch e dos dados transmitidos.','9.3'),
 mc('Na falsificação de DHCP, por que o cliente aceita o servidor falso?',
    ['Porque aceita a primeira oferta que recebe','Porque o servidor falso tem senha','Porque o DHCP legítimo é desligado pelo cliente','Porque o falso usa IPv6'],
    'Se a oferta falsa chega primeiro, o cliente envia o DHCPREQUEST para ela.','9.5'),
 mc('Qual tecnologia dos switches Cisco aceita respostas DHCP só de portas confiáveis?',
    ['DHCP snooping','Port mirroring','NetFlow','SNMP'],
    'O DHCP snooping é uma das defesas antispoofing, junto com port security, IP Source Guard e DAI.','12.6'),
]
EX[10]=[
 mc('O que é um resolvedor DNS aberto?',
    ['Um servidor que responde a consultas de qualquer cliente, mesmo de fora do seu domínio','Um servidor DNS sem endereço IP','Um servidor que só aceita consultas internas','Um navegador sem proxy'],
    'Por isso ele fica vulnerável a envenenamento de cache, amplificação e consumo de recursos.','10.2'),
 mc('No tunelamento DNS, onde os dados são escondidos?',
    ['Em rótulos de subdomínio de consultas DNS','No campo TTL do IPv4','No cabeçalho do quadro Ethernet','No certificado do site'],
    'Os dados são divididos em blocos codificados, cada um em um subdomínio, e seguem até o servidor do atacante.','10.4'),
 mc('Qual é a forma mais comum de sequestro de domínio?',
    ['Mudar, por engenharia social, as informações do domínio no registrador','Desligar o servidor DNS da vítima','Enviar SYN ao servidor','Clonar o MAC do roteador'],
    'Com o controle das informações de DNS, o atacante redireciona o domínio.','10.1'),
]
EX[11]=[
 assoc('Associe cada classe de código HTTP ao seu significado.',[
    ('2xx','Sucesso'),('3xx','Redirecionamento'),('4xx','Erro do cliente'),('5xx','Erro do servidor')],
    'Os logs de conexão revelam varreduras e ataques pelos códigos de status.','11.2'),
 mc('O que um iFrame malicioso faz?',
    ['Carrega, dentro de uma página invadida, conteúdo de um site do atacante','Apaga o cache do navegador','Bloqueia anúncios','Criptografa a página'],
    'O iFrame é muito usado para anúncios; o atacante o usa para entregar malware.','11.4'),
 mc('Por que um servidor de e-mail corporativo nunca deve ser um retransmissor aberto?',
    ['Porque qualquer pessoa poderia usá-lo para enviar spam','Porque ficaria mais lento para ler e-mails','Porque não aceitaria anexos','Porque precisaria de IPv6'],
    'Retransmissores abertos são usados por spammers para enviar mensagens em massa.','11.7'),
 mc('Qual é a última linha de defesa quando um ataque por e-mail passa pelas proteções?',
    ['Os usuários educados para reconhecer spam e phishing','O switch de acesso','O servidor DHCP','O cabo de rede'],
    'Por isso a conscientização dos usuários é essencial.','11.7'),
]
EX[12]=[
 mc('Qual é o requisito mais crítico para manter a rede livre de vírus?',
    ['A atualização automática das definições de vírus','Trocar as senhas a cada semana','Usar só cabos de fibra','Desligar os computadores à noite'],
    'Sem definições atualizadas, o antivírus não reconhece as ameaças novas.','12.2'),
 mc('Por que o antivírus de host não basta?',
    ['Ele não impede que o vírus entre na rede; o perímetro precisa de dispositivos de segurança','Ele só funciona em Linux','Ele apaga os arquivos do usuário','Ele bloqueia a internet'],
    'Os dispositivos de perímetro identificam o malware antes que chegue aos hosts.','12.2'),
 mc('É possível impedir totalmente a varredura de portas?',
    ['Não; o IPS e o firewall limitam o que ela descobre','Sim, desligando o ICMP','Sim, com um antivírus','Sim, trocando o roteador'],
    'Desligar serviços desnecessários também reduz o que a varredura encontra.','12.4'),
 mc('Qual costuma ser um dos primeiros sinais de um DoS?',
    ['Reclamações de usuários sobre recursos indisponíveis ou rede lenta','Aumento de e-mails de marketing','Mensagens no Visualizador de Eventos sobre atualizações','Queda da temperatura da sala'],
    'Um monitoramento contínuo do uso da rede ajuda a detectar o ataque.','12.6'),
]
EX[13]=[
 mc('Por que as WLANs usam CSMA/CA em vez de detectar colisões?',
    ['O cliente não consegue ouvir enquanto transmite','O Wi-Fi é full-duplex','Os APs não têm antena','As colisões não existem no ar'],
    'A WLAN é half-duplex e de meio compartilhado; o cliente evita colisões com RTS e CTS.','13.3'),
 mc('No CSMA/CA, o que o AP envia para liberar a transmissão do cliente?',
    ['CTS (Clear to Send)','RTS (Request to Send)','ACK','SYN'],
    'O cliente pede com RTS e só transmite depois de receber o CTS.','13.3'),
 mc('Na descoberta ativa, o que o cliente envia?',
    ['Uma solicitação de sondagem (probe request) com o SSID','Um beacon','Um DHCPDISCOVER','Um RST'],
    'Na descoberta passiva, o cliente apenas escuta os beacons dos APs.','13.5'),
 mc('Qual modo de segurança deve ser habilitado na associação ao AP?',
    ['O nível mais alto disponível','Sempre o WEP','Nenhum, para facilitar o acesso','O mais antigo, por compatibilidade'],
    'Deve-se sempre usar o modo mais forte que os dispositivos suportam.','13.4'),
]
EX[14]=[
 mc('O que é um AP não autorizado (rogue AP)?',
    ['Um AP ligado à rede da empresa sem autorização e contra a política','Um AP com senha forte','O AP principal da empresa','Um repetidor de sinal autorizado'],
    'Com ele, o atacante pode capturar pacotes, acessar recursos ou fazer um MitM.','14.3'),
 mc('Como funciona o ataque do gêmeo do mal (evil twin)?',
    ['O atacante cria um AP com o mesmo SSID de um legítimo e sinal mais forte','O atacante envia mensagens por Bluetooth','O atacante desliga o AP com um jammer','O atacante quebra a senha do WEP'],
    'Os clientes próximos se associam ao AP falso, que captura e repassa o tráfego.','14.4'),
 assoc('Associe cada ataque Bluetooth.',[
    ('Bluejacking','Envia mensagens não autorizadas a outro dispositivo'),
    ('Bluesnarfing','Copia informações do alvo, como e-mails e contatos')],
    'Pelo alcance curto, o atacante precisa estar perto do alvo.','14.5'),
 mc('Qual banda é mais sujeita a interferência?',
    ['2,4 GHz','5 GHz','As duas igualmente','Nenhuma'],
    'Micro-ondas, telefones sem fio e babás eletrônicas interferem em 2,4 GHz.','14.2'),
]
EX[15]=[
 mc('Ocultar o SSID e filtrar endereços MAC impedem um intruso habilidoso?',
    ['Não; o SSID é fácil de descobrir e o MAC pode ser falsificado','Sim, sempre','Só se a rede usar WEP','Só em redes de 5 GHz'],
    'A melhor proteção é usar autenticação e criptografia.','15.1'),
 mc('Qual criptografia o WPA2 usa e é a preferida?',
    ['AES com CCMP','RC4 com chave estática','TKIP','DES'],
    'O AES é muito mais forte que o TKIP do WPA.','15.4'),
 mc('O que o modo corporativo (Enterprise) do WPA2 exige?',
    ['Um servidor RADIUS e autenticação 802.1X com EAP','Apenas uma chave pré-compartilhada','Nenhuma senha','Um servidor DHCP dedicado'],
    'No modo pessoal, os clientes usam uma PSK sem servidor especial.','15.3'),
 mc('O que o WPA3-Personal usa para proteger a senha?',
    ['A SAE, que nunca expõe a PSK','O WPS','O WEP','O OWE'],
    'No WPA2-Personal, o atacante podia capturar o handshake e tentar adivinhar a PSK.','15.6'),
 mc('Nas redes abertas, o que o WPA3 acrescenta?',
    ['Criptografia de todo o tráfego com o OWE','Autenticação por senha','Servidor RADIUS obrigatório','Filtragem de MAC'],
    'As redes abertas continuam sem autenticação, mas o tráfego deixa de ir em texto claro.','15.6'),
]
EX[16]=[
 mc('Qual tipo de firewall é o mais versátil e mais usado?',
    ['Com estado (stateful)','Filtragem de pacotes sem estado','Proxy de aplicação','Firewall de host'],
    'Ele filtra com base nas informações de conexão guardadas em uma tabela de estado.','16.3'),
 mc('Em um gateway de aplicação (proxy), o que o servidor vê?',
    ['Só o proxy, que se conecta em nome do cliente','O IP real de cada cliente','Nada, porque a conexão é bloqueada','O MAC do cliente'],
    'O proxy trabalha até a camada 7 e esconde os clientes.','16.3'),
 mc('No ZPF, o que acontece com o tráfego entre zonas diferentes?',
    ['É bloqueado até que uma política o permita ou inspecione','Passa livremente','É sempre criptografado','É enviado ao servidor DNS'],
    'O tráfego entre interfaces da mesma zona passa livremente.','16.2'),
 mc('Qual é a principal diferença entre IDS e IPS?',
    ['O IDS só detecta e alerta; o IPS fica em linha e pode bloquear o tráfego','O IDS bloqueia e o IPS só alerta','O IDS é físico e o IPS é virtual','Não há diferença'],
    'O IDS trabalha fora de linha e não impede o pacote que disparou o alerta; o IPS fica em linha e pode descartá-lo.','16.4'),
]
EX[17]=[
 mc('O que uma ACL faz?',
    ['Decide se o dispositivo encaminha ou descarta cada pacote, com base no cabeçalho','Distribui endereços IP','Sincroniza relógios','Armazena logs'],
    'As ACLs também podem permitir só o tráfego de sessões estabelecidas (bits ACK ou RST).','17.1'),
 assoc('Associe cada ação do SNMP.',[
    ('get','Obtém informações do agente'),
    ('set','Altera configurações do agente'),
    ('trap','Aviso espontâneo enviado pelo agente')],
    'A MIB é o banco de dados do agente com dados e estatísticas do dispositivo.','17.2'),
 mc('Por que o NTP é importante para a segurança?',
    ['Sem relógios sincronizados, é impossível saber a ordem dos eventos em partes diferentes da rede','Porque criptografa os logs','Porque bloqueia malware','Porque distribui endereços IP'],
    'Os logs só podem ser correlacionados com data e hora precisas.','17.5'),
 inp('Um roteador sincroniza com um servidor de estrato 2. Qual é o estrato do roteador?',['3'],'num',
    'Cada salto acrescenta 1 ao estrato.','17.5',ph='estrato'),
 assoc('Associe cada função do AAA.',[
    ('Autenticação','Verifica quem é o usuário'),
    ('Autorização','Define o que ele pode acessar e fazer'),
    ('Contabilidade (accounting)','Registra o que ele fez e por quanto tempo')],
    'A autorização vem depois da autenticação.','17.6'),
]
EX[18]=[
 mc('Em que sistema o Windows moderno é baseado?',
    ['Windows NT','MS-DOS','Unix','Linux'],
    'O Windows NT controla diretamente o hardware e aceita vários processos e usuários.','18.1'),
 mc('Um programa de 64 bits roda em hardware de 32 bits?',
    ['Não; mas programas de 32 bits rodam em sistemas de 64 bits','Sim, sempre','Só com antivírus','Só no Windows Server'],
    'A arquitetura de 64 bits é compatível com programas de 32 bits, mas não o contrário.','18.2'),
 inp('Quantos GB de memória um sistema de 32 bits consegue endereçar?',['4'],'num',
    '2^32 bytes = 4 GB.','18.2',ph='GB'),
 mc('O que é uma exploração (exploit) de sistema operacional?',
    ['Uma técnica ou ferramenta que faz o computador agir fora do previsto, aproveitando uma vulnerabilidade','Uma atualização de segurança','Um programa de backup','Uma conta de usuário'],
    'Em geral, o objetivo é obter controle, alterar permissões ou roubar dados.','18.4'),
]
EX[19]=[
 mc('O que faz a HAL do Windows?',
    ['Cuida da comunicação entre o hardware e o kernel','Armazena as senhas','Gerencia a interface gráfica','Faz o backup do registro'],
    'A HAL é a camada de abstração de hardware.','19.1'),
 mc('Por que uma falha em um aplicativo em modo usuário não derruba o sistema?',
    ['Porque cada aplicativo tem um processo e um espaço de endereços privado, sem acesso direto ao hardware','Porque o modo usuário tem prioridade máxima','Porque o antivírus impede','Porque o kernel é desligado'],
    'No modo kernel, ao contrário, uma falha pode parar o computador inteiro.','19.2'),
 mc('Por que os fluxos de dados alternativos (ADS) do NTFS são um risco?',
    ['Permitem esconder código malicioso dentro de um arquivo aparentemente comum','Apagam os arquivos do usuário','Deixam o disco mais lento','Desativam o firewall'],
    'O comando dir /r revela os fluxos alternativos.','19.4'),
 mc('Formatar um disco apaga todos os dados de forma definitiva?',
    ['Não; os dados antigos podem ser recuperados do espaço livre','Sim, sempre','Só no FAT32','Só em SSDs'],
    'Para descarte seguro, é preciso sobrescrever ou destruir a mídia.','19.3'),
 mc('Qual firmware substitui o BIOS e entra direto no modo protegido?',
    ['UEFI','MBR','POST','BCD'],
    'O UEFI carrega os programas .efi da partição ESP.','19.5'),
]
EX[20]=[
 mc('Por que não se deve usar o computador sempre como administrador?',
    ['Todo programa herda os privilégios, e um malware teria acesso total','Porque o computador fica mais lento','Porque o administrador não acessa a internet','Porque a conta expira'],
    'Quando um programa precisa de privilégios, usa-se "Executar como administrador".','20.1'),
 mc('Por que a WMI é perigosa nas mãos de atacantes?',
    ['O tráfego é comum, confiado pelos dispositivos de segurança, e deixa poucos rastros','Porque apaga o disco','Porque só funciona em Linux','Porque é sempre criptografada'],
    'Por isso o acesso à WMI deve ser muito restrito.','20.4'),
 mc('Qual é a recomendação sobre a conta Convidado do Windows?',
    ['Não habilitá-la','Usá-la para administrar o computador','Dar a ela privilégios de administrador','Deixá-la sem senha e habilitada'],
    'A conta Convidado não tem senha e vem desabilitada por padrão.','20.2'),
 mc('Por que o RDP precisa de cuidado?',
    ['Foi feito para controlar hosts remotamente e é alvo natural dos atacantes','Porque só funciona em redes sem fio','Porque apaga os compartilhamentos','Porque desativa o antivírus'],
    'Deve-se limitar sua exposição à internet e aplicar correções e políticas de confiança zero.','20.7'),
]
EX[21]=[
 mc('Qual comando liga cada conexão ao processo e ao PID que a criou?',
    ['netstat -abno','ipconfig /all','tasklist','ping -t'],
    'Executado como administrador, ele ajuda a achar conexões abertas por malware.','21.1'),
 mc('Por que se usa o PID para achar um processo no Gerenciador de Tarefas?',
    ['Porque é único para cada processo, enquanto vários podem ter o mesmo nome','Porque indica a porta usada','Porque mostra o usuário','Porque é o nome do arquivo'],
    'O nome pode se repetir; o PID não.','21.1'),
 assoc('Associe cada nível de evento do Visualizador de Eventos à gravidade crescente.',[
    ('Menor gravidade','Informação'),('Problema possível','Aviso'),('Falha','Erro'),('Maior gravidade','Crítico')],
    'Cada evento tem nível, data e hora, origem e ID de evento.','21.2'),
 mc('O que é uma política de segurança local do Windows?',
    ['Um conjunto de objetivos e regras que garante a segurança do computador, como senhas e bloqueio de conta','Um antivírus','Um tipo de firewall de rede','Um log do sistema'],
    'Em um domínio, as políticas são aplicadas de forma centralizada.','21.4'),
]
EX[22]=[
 mc('Por que o Linux é valioso para o SOC?',
    ['É de código aberto, flexível e tem muitas ferramentas de segurança e de pentest','Porque só roda em servidores','Porque não tem vulnerabilidades','Porque não usa linha de comando'],
    'Os analistas o usam para captura de pacotes, análise de logs e testes de penetração.','22.2'),
 mc('No Linux, como são tratados a memória, os discos e os diretórios?',
    ['Como arquivos','Como processos','Como usuários','Como serviços'],
    'No Linux, tudo é tratado como arquivo.','22.5'),
 mc('Por que os editores de texto de linha de comando são essenciais?',
    ['Permitem editar arquivos em um computador remoto, por SSH, sem interface gráfica','São mais bonitos','Corrigem erros automaticamente','São os únicos que salvam arquivos'],
    'Em uma sessão SSH não há interface gráfica.','22.5'),
 mc('O que é uma porta para um servidor?',
    ['Um recurso de rede reservado a um serviço, no qual ele fica escutando','Um cabo físico','Um usuário do sistema','Um arquivo de log'],
    'Exemplo: um servidor web escuta na porta 80 ou 443.','22.6'),
]
EX[23]=[
 mc('Por que os arquivos de configuração dos serviços precisam de proteção?',
    ['Os serviços costumam rodar com privilégios de superusuário','Porque são muito grandes','Porque mudam sozinhos','Porque são públicos'],
    'Uma alteração costuma exigir reiniciar o serviço.','23.1'),
 mc('O que é endurecimento (hardening) de um dispositivo?',
    ['Aplicar métodos comprovados para proteger o dispositivo e seu acesso administrativo','Trocar o disco por um SSD','Aumentar a memória','Instalar mais programas'],
    'Inclui senhas fortes, parar serviços desnecessários e manter atualizações.','23.2'),
 assoc('Associe cada log do Linux ao seu conteúdo.',[
    ('/var/log/messages','Atividade geral do computador'),
    ('/var/log/auth.log','Autenticação no Debian e no Ubuntu'),
    ('/var/log/secure','Autenticação no Red Hat e no CentOS')],
    'No Debian, o equivalente ao messages é /var/log/syslog.','23.3'),
]
EX[24]=[
 inp('Qual é o valor octal das permissões rwxr-xr-x?',['755'],'num','rwx = 7; r-x = 5; r-x = 5.','24.3',ph='octal'),
 inp('Qual é o valor octal das permissões rw-r-----?',['640'],'num','rw- = 6; r-- = 4; --- = 0.','24.3',ph='octal'),
 mc('Quem pode ignorar as permissões de arquivos no Linux?',
    ['Só o root','Qualquer usuário do grupo','O dono do arquivo','Ninguém, nem o root'],
    'Por isso as credenciais do root precisam de senha forte.','24.3.1'),
 mc('O que acontece com um link simbólico quando o arquivo original é apagado?',
    ['Passa a apontar para algo que não existe mais','Continua acessando o conteúdo','Vira um link rígido','Apaga o diretório'],
    'O link rígido, ao contrário, continua acessando o conteúdo pelo inode.','24.4'),
 mc('Qual tipo de link pode apontar para outro sistema de arquivos e para diretórios?',
    ['Simbólico','Rígido','Os dois','Nenhum'],
    'O link rígido aponta para o inode e fica no mesmo sistema de arquivos.','24.4'),
]
EX[25]=[
 mc('O que faz um gerenciador de pacotes?',
    ['Instala cada arquivo do programa no lugar certo e cuida das dependências','Compacta arquivos','Faz backup do sistema','Bloqueia malware'],
    'Exemplos: dpkg e apt no Debian e no Ubuntu; pacman no Arch Linux.','25.1'),
 mc('Qual é a única forma de criar processos no Linux?',
    ['A bifurcação (fork)','O pipe','O comando ls','A montagem'],
    'O kernel cria uma cópia do processo, que recebe um novo PID.','25.3'),
 mc('Por que um rootkit é tão perigoso?',
    ['Altera o kernel, esconde a intrusão e adultera as ferramentas de diagnóstico','Só deixa o computador lento','Envia spam','Apaga o histórico do navegador'],
    'A grande maioria exige acesso root; o chkrootkit procura rootkits conhecidos, mas a solução real costuma ser reinstalar o sistema.','25.5'),
 mc('O que o comando ls -l | grep host faz?',
    ['Lista o diretório e mostra só as linhas que contêm "host"','Apaga os arquivos com "host"','Cria um arquivo host','Muda as permissões'],
    'O pipe leva a saída de um comando para a entrada de outro.','25.6'),
]
EX[26]=[
 mc('O que é um endpoint?',
    ['Qualquer host da rede que acessa ou é acessado por outros hosts','Só o roteador de borda','Apenas o servidor de e-mail','O cabo de rede'],
    'Computadores, servidores, impressoras, telefones IP e dispositivos IoT são endpoints.','26'),
 mc('Por que se testa um patch antes de distribuí-lo?',
    ['Para evitar que ele cause problemas em toda a empresa','Porque os patches são sempre maliciosos','Para deixar o download mais rápido','Porque a lei exige'],
    'Uma ferramenta de gerenciamento de patches automatiza a distribuição depois do teste.','26.3'),
 mc('O que a criptografia de disco completo (FDE) protege?',
    ['Todo o conteúdo da unidade, inclusive arquivos temporários','Só os e-mails','Só os arquivos da área de trabalho','O tráfego de rede'],
    'No Windows, é feita pelo BitLocker.','26.5'),
 assoc('Associe cada mecanismo de integridade da inicialização.',[
    ('Inicialização segura (Secure Boot)','Verifica a assinatura de cada parte do software de inicialização'),
    ('Inicialização medida (Measured Boot)','Mede cada componente e guarda as medidas no TPM')],
    'A inicialização medida é a validação mais forte e pode ser verificada remotamente.','26.6'),
]
EX[27]=[
 mc('Em quanto tempo vários tipos de malware mudam suas características para escapar da detecção?',
    ['Menos de 24 horas','Uma semana','Um mês','Um ano'],
    'Por isso a proteção precisa ir além das assinaturas.','27.1'),
 mc('Por que proteger a LAN interna é quase tão importante quanto proteger o perímetro?',
    ['Muitos ataques vêm de dentro da rede','A LAN não tem dispositivos','A internet já é segura','O perímetro não existe mais'],
    'Endpoints e infraestrutura da LAN precisam de proteção própria.','27.2'),
 mc('Qual é a vantagem da proteção antimalware baseada em rede?',
    ['Identifica e bloqueia o malware antes que chegue aos hosts','Funciona sem eletricidade','Dispensa atualizações','Substitui o backup'],
    'Ela complementa a proteção baseada em host.','27.4'),
]
EX[28]=[
 mc('O que faz um firewall de host?',
    ['Controla o tráfego que entra e sai do computador','Distribui endereços IP','Faz backup dos arquivos','Gerencia patches'],
    'Também existem para celulares e tablets Android.','28.1'),
 mc('O que o OSSEC faz?',
    ['Monitora os logs dos hosts, verifica a integridade dos arquivos e detecta rootkits','Bloqueia sites na nuvem','Distribui patches do Windows','Gerencia senhas'],
    'É um HIDS de código aberto que pode executar scripts em resposta a eventos.','28.4'),
 mc('Como um HIDS detecta um ataque?',
    ['Comparando a atividade do host com assinaturas e com o comportamento normal','Pela temperatura do processador','Pelo tamanho dos e-mails','Pelo número de usuários'],
    'Ele combina detecção por assinaturas e por anomalias.','28.3'),
]
EX[29]=[
 mc('O que é a superfície de ataque?',
    ['A soma das vulnerabilidades de um sistema acessíveis ao atacante','O tamanho do monitor','A área do data center','O número de usuários'],
    'Portas abertas, softwares expostos e o comportamento das pessoas fazem parte dela.','29.1'),
 assoc('Associe cada lista ao que ela define.',[
    ('Lista de bloqueio (blocklist)','Quais aplicativos não podem rodar'),
    ('Lista de permissão (allowlist)','Quais aplicativos podem rodar')],
    'Limitar o que pode rodar reduz a superfície de ataque.','29.2'),
 mc('Para que serve uma sandbox?',
    ['Executar e analisar arquivos suspeitos em um ambiente seguro','Guardar senhas','Acelerar a rede','Fazer backup do disco'],
    'Exemplos: Cuckoo Sandbox, VirusTotal e Cisco Threat Grid Glovebox.','29.3'),
]
EX[30]=[
 mc('Por que a conscientização em segurança precisa ser contínua?',
    ['Porque novas ameaças surgem sempre','Porque os funcionários esquecem as senhas','Porque a lei exige um curso por dia','Porque o antivírus expira'],
    'Gastar muito em tecnologia não adianta se as pessoas forem o elo mais fraco.','30.3'),
 mc('O que a AUP define?',
    ['O que os usuários podem ou não fazer nos sistemas','A configuração do firewall','A topologia da rede','O orçamento de TI'],
    'A AUP deve ser o mais explícita possível.','30.4'),
 assoc('Associe cada documento à sua característica.',[
    ('Padrão','Garante a consistência e é obrigatório'),
    ('Diretriz','Sugestão mais flexível, em geral não obrigatória'),
    ('Procedimento','Passo a passo detalhado para executar uma tarefa')],
    'A política se desdobra em padrões, diretrizes e procedimentos.','30.5'),
]
