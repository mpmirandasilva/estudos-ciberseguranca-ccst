# Questões no estilo CCST Networking (100-150) — trilha Fundamentos.
# dom = domínio do blueprint: 1 padrões e conceitos · 2 endereçamento · 3 endpoints e mídias
#       4 infraestrutura · 5 diagnóstico · 6 segurança.  mc/ms: as primeiras opções são as corretas.
from ccst_lib import *

EX={}
EX[1]=[
 mc('Uma clínica tem consultórios em dois andares do mesmo prédio, ligados por switches da própria clínica e administrados por ela. Como o técnico deve classificar essa rede?',
    ['LAN','WAN','Internet','Backbone de provedor'],
    'A LAN cobre uma área pequena, como um prédio, e é administrada por uma única organização.','1.3.1',1),
 ms('Uma empresa vai interligar a matriz, em São Paulo, à filial, em Recife. Quais duas características essa conexão terá por ser uma WAN? (Escolha duas.)',
    ['Interligar redes em áreas geográficas distantes','Usar normalmente a infraestrutura de provedores de serviço','Ser administrada por uma única pessoa, sem operadoras','Oferecer velocidade maior que a da LAN interna','Dispensar o uso de protocolos comuns'],
    'A WAN interliga LANs distantes e costuma depender de operadoras, com velocidade menor e custo maior que a LAN.','1.3.2',1),
 mc('Um técnico precisa consultar a especificação oficial de um protocolo da Internet. Onde ela é publicada?',
    ['Em uma RFC, publicada pela IETF','No site da ICANN, que define os protocolos','No manual do fabricante do roteador','Em uma norma da IANA sobre portas'],
    'A IETF desenvolve os protocolos da Internet e registra as especificações em documentos públicos chamados RFCs.','8.3.1',1),
 mc('Em uma câmara fria, um sensor envia a temperatura pela rede e um atuador liga o compressor automaticamente. Como esses equipamentos são classificados?',
    ['Dispositivos finais de IoT','Dispositivos intermediários','Roteadores especializados','Meios de transmissão'],
    'Sensores e atuadores conectados fazem parte da Internet das Coisas e são dispositivos finais (hosts).','1.5.3',3),
]
EX[2]=[
 multi('Uma loja virtual guarda informações dos clientes. Classifique cada uma.',[
    C('Nome e e-mail do cadastro',['Voluntário','Observado','Inferido','Secreto'],'Voluntário'),
    C('Histórico de páginas visitadas',['Voluntário','Observado','Inferido','Secreto'],'Observado'),
    C('Preferência por calçados, deduzida das compras',['Voluntário','Observado','Inferido','Secreto'],'Inferido'),
    C('Senha da conta',['Voluntário','Observado','Inferido','Secreto'],'Secreto')],
    'Voluntário → informado pelo usuário; observado → coletado das ações; inferido → deduzido de outros dados; secreto → confidencial.','2.1',6),
 inp('Uma captura mostra os bytes 01000001 01000010. Sabendo que, em ASCII, A = 01000001, qual é o caractere do segundo byte?',['b'],'txt','01000010 = 66, uma unidade acima do A (65): é o B.','2.2.2',1,ph='caractere',d='B'),
 mc('Um galpão industrial tem motores que geram forte interferência eletromagnética. Que tipo de sinal é imune a ela?',
    ['Óptico, na fibra','Elétrico, no cabo de cobre','Ondas de rádio do Wi-Fi','Elétrico, no cabo coaxial'],
    'Pulsos de luz na fibra óptica não sofrem interferência eletromagnética.','2.3.2',3),
 multi('Coloque em ordem o caminho de uma informação até o destino.',ORD(['Informação','Bits','Sinais','Meio de transmissão','Dispositivo de destino']),
    'Informação → Bits → Sinais → Meio de transmissão → Dispositivo de destino.','2.3',1,ord=True),
]
EX[3]=[
 inp('Um cliente contratou 200 Mbps. Qual é o tempo mínimo teórico, em segundos, para baixar um arquivo de 500 MB?',['20'],'num','500 MB × 8 = 4.000 Mb; 4.000 ÷ 200 = 20 s. A velocidade é em bits; o arquivo, em bytes.','3.2',1,ph='segundos'),
 mc('A empresa contratou 300 Mbps, mas no horário de pico os testes mostram 180 Mbps. Como se chama o valor de 180 Mbps?',
    ['Taxa de transferência (throughput)','Largura de banda','Latência','MTU'],
    'A largura de banda é a capacidade teórica; o throughput é a velocidade real em um momento.','3.3',1),
 mc('Um jogador com 500 Mbps reclama de atraso nas jogadas, e o ping mostra 180 ms. Qual indicador explica o problema?',
    ['Latência alta','Largura de banda baixa','Excesso de endereços IP','Uso de UDP'],
    'Uma rede pode ter alta largura de banda e, mesmo assim, alta latência: são características diferentes.','3.4',1),
 ms('Quais dois fatores fazem a taxa de transferência ficar abaixo da largura de banda contratada? (Escolha dois.)',
    ['Congestionamento da rede','Interferências no meio de transmissão','Uso da máscara /24','Uso de IPv6 em vez de IPv4','Uso da porta 443'],
    'Congestionamento, quantidade de dispositivos, equipamentos, meio e interferências reduzem o throughput.','3.3',1),
]
EX[4]=[
 multi('Indique o dispositivo indicado para cada necessidade.',[
    C('Conectar notebooks sem fio à rede cabeada',['Switch','Roteador','Ponto de acesso','Firewall'],'Ponto de acesso'),
    C('Bloquear conexões de entrada não autorizadas',['Switch','Roteador','Ponto de acesso','Firewall'],'Firewall'),
    C('Encaminhar dados entre a LAN e o provedor',['Switch','Roteador','Ponto de acesso','Firewall'],'Roteador'),
    C('Interligar os PCs do mesmo andar',['Switch','Roteador','Ponto de acesso','Firewall'],'Switch')],
    'Switch → mesma rede (MAC); roteador → redes diferentes (IP); AP → Wi-Fi; firewall → regras de segurança.','4.4',4),
 mc('O técnico precisa de um diagrama que mostre em qual sala e rack ficam os switches e por onde passam os cabos. Que diagrama é esse?',
    ['Topologia física','Topologia lógica','Tabela de roteamento','Diagrama de sockets'],
    'A topologia física mostra a localização dos equipamentos e o cabeamento; a lógica, os endereços e o fluxo dos dados.','4.6.1',4),
 ms('Quais duas funções um roteador doméstico normalmente acumula, além de encaminhar pacotes? (Escolha duas.)',
    ['Atribuir endereços IP automaticamente (DHCP)','Traduzir endereços privados para o público (NAT)','Gravar o endereço MAC das placas de rede','Servir como servidor DNS autoritativo de domínios','Fragmentar pacotes IPv6'],
    'O roteador residencial costuma acumular DHCP, NAT, Wi-Fi e firewall.','4.3.2',4),
 mc('Uma câmera IP e um leitor de código de barras sem fio estão conectados à rede. Como são classificados?',
    ['Dispositivos finais (hosts)','Dispositivos intermediários','Meios de transmissão','Gateways padrão'],
    'Dispositivos finais são a origem ou o destino das informações.','4.1',3),
]
EX[5]=[
 mc('Em um escritório com três pessoas, os computadores compartilham uma impressora e pastas diretamente entre si, sem servidor. Qual modelo é usado?',
    ['Ponto a ponto (P2P)','Cliente-servidor','Híbrido com servidor dedicado','Nuvem pública'],
    'No P2P, cada dispositivo atua como cliente e servidor, sem servidor dedicado.','5.3',1),
 ms('Esse escritório cresceu para 60 pessoas e continua em P2P. Quais duas desvantagens tendem a aparecer? (Escolha duas.)',
    ['Falta de administração centralizada','Menor nível de segurança','Necessidade de servidores dedicados caros','Dependência de um único servidor','Profissionais especializados para o servidor'],
    'P2P: sem administração central, menos segurança, pouca escalabilidade. As outras opções são desvantagens do cliente-servidor.','5.3.3',1),
 mc('O servidor de arquivos da empresa parou, e ninguém consegue abrir as pastas compartilhadas. Que desvantagem do modelo cliente-servidor isso mostra?',
    ['A dependência do funcionamento do servidor','A falta de segurança','A dificuldade de fazer backup','A baixa escalabilidade'],
    'No cliente-servidor, se o servidor falha, os serviços ficam indisponíveis.','5.2.5',1),
]
EX[6]=[
 mc('A rede "Financeiro" não aparece na lista do notebook, mas outros computadores já estão conectados a ela. O broadcast de SSID está desativado. O que o técnico deve fazer?',
    ['Adicionar a rede manualmente, informando o SSID e o tipo de segurança','Reiniciar o roteador até a rede aparecer','Trocar o padrão para 802.11b','Desativar a criptografia da rede'],
    'Uma rede oculta não aparece na lista: é preciso informar o SSID e a segurança manualmente.','6.4.3',3),
 ms('Quais dois padrões de segurança devem ser usados em uma rede Wi-Fi? (Escolha dois.)',
    ['WPA3','WPA2','Rede aberta com SSID oculto','Telnet','HTTP'],
    'WPA2 e WPA3 criptografam os dados transmitidos na rede sem fio.','6.7.1',6),
 mc('Uma funcionária precisa acessar o sistema da empresa a partir do Wi-Fi público de um café. Qual é a recomendação?',
    ['Usar uma VPN','Desativar o firewall do notebook','Usar Telnet para acessar o sistema','Compartilhar a senha da rede com a equipe'],
    'A VPN cria uma conexão protegida, que ajuda a proteger as informações em redes públicas.','6.7.3',6),
 multi('Indique a tecnologia sem fio de cada situação.',[
    C('Pagar por aproximação no caixa',['NFC','Bluetooth','Wi-Fi','GPS'],'NFC'),
    C('Conectar um fone de ouvido ao celular',['NFC','Bluetooth','Wi-Fi','GPS'],'Bluetooth'),
    C('Conectar um notebook ao AP do escritório',['NFC','Bluetooth','Wi-Fi','GPS'],'Wi-Fi'),
    C('Rastrear os veículos de uma frota',['NFC','Bluetooth','Wi-Fi','GPS'],'GPS')],
    'NFC → distâncias muito curtas; Bluetooth → curto alcance e baixo consumo; Wi-Fi → LAN sem fio; GPS → localização por satélite.','6',3),
 mc('Um celular em viagem internacional gerou custos altos de Internet. Qual configuração do aparelho estava ativada?',
    ['Roaming de dados','Modo avião','Hotspot por Bluetooth','Esquecer rede'],
    'O roaming de dados usa a rede de outra operadora e pode gerar custos adicionais.','6.4.4',3),
]
EX[7]=[
 mc('O técnico vai fazer a configuração inicial de um roteador doméstico novo. Em qual porta deve ligar o notebook?',
    ['Em uma porta LAN','Na porta WAN/Internet','Na porta do modem','Em qualquer porta, inclusive a WAN'],
    'A porta WAN é reservada ao modem; o computador vai em uma porta LAN.','7.9.1',4),
 ms('Quais duas medidas reforçam a segurança de um roteador doméstico? (Escolha duas.)',
    ['Alterar a senha padrão de administração','Usar WPA2 ou WPA3','Usar o nome do proprietário no SSID','Desativar o firewall integrado','Deixar a rede de visitantes na rede principal'],
    'Também ajudam: SSID que não identifique o dono e rede separada para convidados.','7.10',6),
 mc('Um cliente numa área rural não tem fibra nem cabo e aceita latência maior. Qual conexão é a alternativa?',
    ['Internet via satélite','DSL','Fibra FTTH','Conexão discada'],
    'O satélite atende áreas remotas, com maior latência e custo.','7.7.5',3),
 mc('O usuário quer sinal Wi-Fi no fundo do quintal, longe do roteador, mesmo com menos velocidade. Qual frequência é a mais indicada?',
    ['2,4 GHz','5 GHz','6 GHz','Qualquer uma, o alcance é igual'],
    '2,4 GHz → maior alcance; 5 GHz → maior velocidade e menor alcance.','7.10',3),
 mc('O Wi-Fi cai sempre que o micro-ondas da cozinha é usado. Qual é a primeira ação recomendada?',
    ['Afastar o roteador de aparelhos que causam interferência e deixá-lo em local central e elevado','Trocar o cabo da porta WAN','Mudar a máscara de sub-rede','Desativar o DHCP'],
    'Micro-ondas e telefones sem fio interferem no Wi-Fi; a posição do roteador importa.','7.10',3),
]
EX[8]=[
 multi('Indique a camada do modelo TCP/IP de cada protocolo.',[
    C('HTTP',['Aplicação','Transporte','Internet','Acesso à rede'],'Aplicação'),
    C('TCP',['Aplicação','Transporte','Internet','Acesso à rede'],'Transporte'),
    C('IP',['Aplicação','Transporte','Internet','Acesso à rede'],'Internet'),
    C('Ethernet',['Aplicação','Transporte','Internet','Acesso à rede'],'Acesso à rede')],
    'HTTP → aplicação; TCP → transporte; IP → Internet; Ethernet → acesso à rede.','8.6',1),
 mc('Um cabo de rede foi rompido durante uma obra. Em qual camada do modelo OSI está o problema?',
    ['Física (1)','Enlace de dados (2)','Rede (3)','Transporte (4)'],
    'A camada física transmite os bits pelo meio físico, como os cabos.','8.7.7',1),
 multi('Qual é a PDU de cada camada no encapsulamento?',[
    C('Transporte',['Segmento','Pacote','Quadro','Bits'],'Segmento'),C('Internet',['Segmento','Pacote','Quadro','Bits'],'Pacote'),
    C('Acesso à rede',['Segmento','Pacote','Quadro','Bits'],'Quadro'),C('Física',['Segmento','Pacote','Quadro','Bits'],'Bits')],
    'Dados → segmento → pacote → quadro → bits.','8.9',1),
 mc('Em qual camada do modelo OSI ficam a criptografia e a compressão dos dados?',
    ['Apresentação (6)','Sessão (5)','Aplicação (7)','Transporte (4)'],
    'A camada de apresentação traduz formatos, comprime e criptografa.','8.7.2',1),
]
MAC_X="""Switch# show mac address-table
          Mac Address Table
-------------------------------------------
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
   1    0050.7966.6800    DYNAMIC     Fa0/1
   1    0050.7966.6801    DYNAMIC     Fa0/2
   1    000c.29aa.10bb    DYNAMIC     Gi0/1
   1    000c.29aa.10bc    DYNAMIC     Gi0/1"""
EX[9]=[
 mc('Dois prédios do mesmo campus ficam a 400 metros, e o caminho passa por uma área com motores. Qual mídia o técnico deve usar?',
    ['Fibra óptica multimodo','Cabo UTP Cat 6','Cabo coaxial','Cabo STP Cat 5e'],
    'O par trançado chega a 100 m; a fibra multimodo cobre centenas de metros e é imune à interferência.','9.3.1',3),
 mc('Um PC ligado ao switch por um cabo UTP de 130 metros tem conexão instável. Qual é a causa mais provável?',
    ['O cabo passa do alcance máximo de 100 metros','O conector deveria ser RJ-11','Falta uma rota padrão','O switch precisa de um cabo coaxial'],
    'O cabo UTP tem alcance máximo de 100 metros.','9.1.1',3),
 ms('Quais dois são conectores de fibra óptica? (Escolha dois.)',
    ['LC','SC','RJ-45','RJ-11','Conector coaxial'],
    'Os conectores de fibra mais comuns são SC, LC e ST; o RJ-45 é do par trançado e o RJ-11, da linha telefônica.','9.3.2',3),
 mc('Dois switches antigos, sem Auto-MDIX, precisam ser ligados entre si. Que cabo usar?',
    ['Cabo cruzado','Cabo direto','Cabo coaxial','Cabo console'],
    'Cabo cruzado liga dispositivos semelhantes; o Auto-MDIX dos equipamentos atuais dispensa essa preocupação.','9.1.4',3),
 multi('Indique o padrão IEEE de cada nome comercial.',[
    C('Wi-Fi 4',['802.11n','802.11ac','802.11ax'],'802.11n'),C('Wi-Fi 5',['802.11n','802.11ac','802.11ax'],'802.11ac'),C('Wi-Fi 6',['802.11n','802.11ac','802.11ax'],'802.11ax')],
    'Wi-Fi 4 → 802.11n; Wi-Fi 5 → 802.11ac; Wi-Fi 6 → 802.11ax.','9.6',3),
]
EX[10]=[
 mc('Observe a tabela do switch. Um quadro chega com destino 0050.7966.6801. Por onde o switch o envia?',
    ['Somente pela porta Fa0/2','Por todas as portas, exceto a de entrada','Somente pela porta Gi0/1','O quadro é descartado'],
    'MAC de destino conhecido → o switch filtra e envia só pela porta correspondente.','10.7.3',4,x=MAC_X,xt='switch'),
 mc('Na mesma tabela, por que dois endereços MAC aparecem na porta Gi0/1?',
    ['A porta está ligada a outro switch, com vários dispositivos atrás dela','A tabela está corrompida','A porta Gi0/1 está em half-duplex','São endereços de broadcast'],
    'Uma porta pode ter vários MACs quando está ligada a outro switch.','10.7.4',4,x=MAC_X,xt='switch'),
 mc('O financeiro está na VLAN 10 e vendas na VLAN 20, no mesmo switch. Um PC do financeiro não consegue pingar um PC de vendas. O que é necessário para essa comunicação?',
    ['Um roteador ou um switch de camada 3','Um cabo cruzado entre os PCs','Desativar as VLANs no PC','Usar o mesmo endereço IP nos dois'],
    'VLANs diferentes são domínios de broadcast e redes diferentes; a comunicação exige roteamento.','10.8.1',4),
 ms('Quais duas vantagens a empresa obtém ao dividir o switch em VLANs por setor? (Escolha duas.)',
    ['Redução do tráfego de broadcast','Mais segurança, separando grupos de usuários','Aumento da MTU dos quadros','Fim da necessidade de endereços IP','Dispensa dos switches'],
    'Também facilitam o gerenciamento, pois a divisão é feita por configuração.','10.8.2',4),
 inp('Qual é o tamanho máximo, em bytes, de um quadro Ethernet com a marcação 802.1Q?',['1522'],'num','1518 bytes + 4 bytes da tag 802.1Q = 1522 bytes.','10.8.3',4,ph='bytes'),
]
WS_X="""Internet Protocol Version 4, Src: 192.168.1.10, Dst: 8.8.8.8
    Version: 4
    Time to Live: 1
    Protocol: ICMP (1)"""
EX[11]=[
 mc('Um técnico captura este pacote no Wireshark. O que acontece quando ele chega ao primeiro roteador?',
    ['O TTL chega a 0, o pacote é descartado e a origem recebe "tempo excedido"','O roteador aumenta o TTL para 64 e encaminha','O pacote é entregue normalmente, porque é ICMP','O roteador responde com eco'],
    'Cada roteador diminui o TTL em 1; ao chegar a 0, descarta e envia tempo excedido. É assim que o tracert descobre os saltos.','11.8.3',5,x=WS_X,xt='wireshark'),
 mc('Um roteador recebe um pacote para uma rede que não está na sua tabela de roteamento e não tem rota padrão. O que acontece?',
    ['O pacote é descartado e a origem recebe "destino inacessível"','O pacote é enviado em broadcast','O roteador guarda o pacote até aprender a rota','O pacote volta à origem sem aviso'],
    'Sem rota, o roteador descarta e pode avisar com ICMP de destino (rede) inacessível.','11.8.2',5),
 ms('Quais duas afirmações sobre o protocolo IP são verdadeiras? (Escolha duas.)',
    ['É sem conexão','Não retransmite pacotes perdidos','Garante a ordem de chegada dos pacotes','Confirma o recebimento de cada pacote','Depende do meio físico usado'],
    'O IP é sem conexão, de melhor esforço e independente do meio; a confiabilidade fica com o TCP.','11.5',1),
 mc('Um pacote IPv4 com o bit DF ativo precisa atravessar um enlace com MTU menor que o seu tamanho. O que o roteador faz?',
    ['Não fragmenta o pacote, e ele não segue por esse enlace','Fragmenta o pacote normalmente','Converte o pacote para IPv6','Aumenta a MTU do enlace'],
    'O bit DF (Don\'t Fragment) indica que o pacote não deve ser fragmentado.','11.7.1',1),
]
IPC_X="""Adaptador Ethernet Ethernet:
   Endereço IPv4. . . . . . . . . : 192.168.20.77
   Máscara de Sub-rede . . . . . . : 255.255.255.224
   Gateway Padrão. . . . . . . . . : 192.168.20.65"""
EX[12]=[
 multi('Com base na saída do ipconfig, informe os dados da rede deste computador.',[F('Endereço de rede','192.168.20.64','ip'),F('Broadcast','192.168.20.95','ip'),F('Hosts utilizáveis','30','num')],
    '/27 (255.255.255.224) → blocos de 32: 64 a 95. Rede .64, broadcast .95, 30 hosts; o gateway .65 é o primeiro host.','12.13.3',2,x=IPC_X,xt='ipconfig'),
 multi('Classifique cada endereço encontrado durante um atendimento.',[
    C('172.31.200.1',['Privado','Público','APIPA','Loopback','Multicast'],'Privado'),
    C('172.32.0.1',['Privado','Público','APIPA','Loopback','Multicast'],'Público'),
    C('169.254.33.7',['Privado','Público','APIPA','Loopback','Multicast'],'APIPA'),
    C('127.0.0.53',['Privado','Público','APIPA','Loopback','Multicast'],'Loopback'),
    C('239.1.1.1',['Privado','Público','APIPA','Loopback','Multicast'],'Multicast')],
    'Privados: 10/8, 172.16–172.31, 192.168/16. 169.254 → APIPA; 127 → loopback; 224–239 → multicast.','12.10.5',2),
 inp('Uma rede precisa de 100 hosts. Qual é o maior prefixo (a menor rede) que atende?',['25'],'pfx','2⁷ − 2 = 126 ≥ 100 e 2⁶ − 2 = 62 não basta: 7 bits de host → /25.','12.5.2',2,ph='/n',d='/25'),
 mc('Qual prefixo costuma ser usado no enlace entre dois roteadores, por oferecer exatamente dois endereços de host?',
    ['/30','/24','/29','/32'],'/30 → 2² − 2 = 2 hosts.','12.12.1',2),
 ms('O PC A (192.168.1.130/25) não consegue falar diretamente com o PC B (192.168.1.100/25). Quais duas afirmações são verdadeiras? (Escolha duas.)',
    ['Eles estão em redes diferentes: 192.168.1.128/25 e 192.168.1.0/25','A comunicação entre eles precisa passar por um roteador','Eles estão na mesma rede e o problema é o cabo','O broadcast do PC A alcança o PC B','Basta trocar a máscara do PC B para /24 sem mudar mais nada'],
    'Com /25, o último octeto se divide em 0–127 e 128–255.','12.13.3',2),
 mc('Dois PCs da casa acessam a Internet ao mesmo tempo usando a mesma porta de origem, 49152. Como o roteador diferencia as respostas?',
    ['Com PAT: altera a porta de origem de um deles e registra a tradução','Envia as respostas em broadcast','Usa o endereço MAC dos PCs na Internet','Atribui um IP público a cada PC'],
    'O PAT (NAT com sobrecarga) diferencia as conexões pelos números de porta.','12.8.2',2),
]
EX[13]=[
 inp('Abrevie ao máximo o endereço 2001:0DB8:0000:0000:0000:0000:0000:0001.',['2001:db8::1'],'v6','Remove os zeros à esquerda e troca a sequência de zeros por ::.','13.8',2,ph='IPv6',d='2001:DB8::1'),
 mc('Qual destas representações de endereço IPv6 é inválida?',
    ['2001:DB8::A::1','2001:DB8:0:0:1::1','FE80::1','::1'],
    'O :: só pode aparecer uma vez no endereço; com dois, não dá para saber quantos zeros cada um representa.','13.8.2',2),
 multi('Classifique cada endereço IPv6.',[
    C('FE80::1A2B',['Link-local','Global unicast','Multicast','Loopback'],'Link-local'),
    C('2001:DB8:ACAD::10',['Link-local','Global unicast','Multicast','Loopback'],'Global unicast'),
    C('FF02::1',['Link-local','Global unicast','Multicast','Loopback'],'Multicast'),
    C('::1',['Link-local','Global unicast','Multicast','Loopback'],'Loopback')],
    'FE80::/10 → link-local; 2000::/3 → global; FF00::/8 → multicast; ::1 → loopback.','13.9',2),
 mc('Um notebook tem um endereço IPv4 e um IPv6 e usa um ou outro conforme o destino. Que técnica de transição é essa?',
    ['Pilha dupla (dual stack)','Tunelamento','NAT64','PAT'],
    'Na pilha dupla, o dispositivo executa os dois protocolos ao mesmo tempo.','13.5.1',2),
 inp('Expanda o endereço 2001:DB8::A:1 para o formato completo.',['2001:0db8:0000:0000:0000:0000:000a:0001'],'v6','4 hextetos escritos → o :: vale 4 hextetos de zeros; depois, completa-se cada um com 4 dígitos.','13.8.4',2,ph='8 hextetos',d='2001:0DB8:0000:0000:0000:0000:000A:0001'),
]
APIPA_X="""Adaptador de Rede sem Fio Wi-Fi:
   DHCP Habilitado . . . . . . . . : Sim
   Endereço IPv4 de link local . . : 169.254.88.12
   Máscara de Sub-rede . . . . . . : 255.255.0.0
   Gateway Padrão. . . . . . . . . :"""
EX[14]=[
 mc('Um usuário está sem Internet. Com base na saída, qual é a causa mais provável?',
    ['O computador não conseguiu contato com o servidor DHCP','O servidor DNS está fora do ar','O cabo de fibra do provedor está rompido','O endereço foi configurado manualmente pelo usuário'],
    'Um endereço 169.254.x.x (APIPA) indica falha na obtenção do endereço por DHCP.','14.8',5,x=APIPA_X,xt='ipconfig /all'),
 ms('Depois de corrigir o problema, quais dois comandos o técnico usa no Windows para pedir um novo endereço ao DHCP? (Escolha dois.)',
    ['ipconfig /release','ipconfig /renew','ipconfig /flushdns','ipconfig /displaydns','netstat -n'],
    '/release libera o endereço atual; /renew solicita um novo ao servidor DHCP.','20.1',5),
 inp('O roteador 192.168.0.1 tem o pool configurado com endereço inicial 192.168.0.100 e máximo de 50 usuários. Qual é o último endereço distribuído?',['192.168.0.149'],'ip','De .100 a .149 são 50 endereços.','14.5.1',2,ph='x.x.x.x'),
 mc('A impressora da sala muda de IP toda semana e os computadores a perdem. Qual é a melhor solução?',
    ['Reservar um endereço para a impressora pelo MAC (ou usar IP estático fora do pool)','Reduzir o período de concessão','Desativar o DHCP da rede','Trocar o cabo da impressora'],
    'Dispositivos que precisam de endereço conhecido usam reserva de DHCP ou IP estático fora do pool.','14.5.1',2),
 mc('O DHCPDISCOVER é enviado antes de o cliente ter um endereço. Qual é o endereço IPv4 de destino dessa mensagem?',
    ['255.255.255.255','0.0.0.0','192.168.0.1','169.254.0.1'],
    'Ela usa o broadcast limitado, que não passa por roteadores. A origem é 0.0.0.0.','12.9.4',2),
]
GW_X="""Adaptador Ethernet Ethernet:
   Endereço IPv4. . . . . . . . . : 192.168.1.50
   Máscara de Sub-rede . . . . . . : 255.255.255.0
   Gateway Padrão. . . . . . . . . : 192.168.2.1"""
EX[15]=[
 mc('Este PC imprime na impressora 192.168.1.20, mas não acessa a Internet. Qual é a causa?',
    ['O gateway padrão está em outra rede, portanto incorreto','A máscara deveria ser 255.255.0.0','A impressora está bloqueando a Internet','Falta um endereço IPv6'],
    'O gateway precisa estar na mesma rede do host; com ele errado, só a rede local funciona.','15.7',5,x=GW_X,xt='ipconfig'),
 mc('O PC 192.168.1.10/24 envia dados para 10.10.5.5. Qual endereço MAC de destino vai no quadro?',
    ['O MAC do gateway padrão','O MAC de 10.10.5.5','FF-FF-FF-FF-FF-FF','O MAC do servidor DNS'],
    'Destino em outra rede → IP do destino remoto, MAC do gateway.','15.4',4),
 ms('Ao atravessar um roteador (sem NAT), quais dois campos mudam? (Escolha dois.)',
    ['O endereço MAC de origem','O endereço MAC de destino','O endereço IP de origem','O endereço IP de destino','A porta de destino'],
    'A cada rede os MACs são trocados; os IPs permanecem até o destino.','15.4',4),
 mc('Como o host decide se envia o quadro direto ao destino ou ao gateway?',
    ['Compara a rede do destino com a sua, usando a máscara de sub-rede','Consulta o servidor DNS','Pergunta ao switch','Envia sempre ao gateway'],
    'Mesma rede → direto, pelo MAC do destino; outra rede → gateway.','15.3',4),
]
ARP_X="""C:\\> arp -a
Interface: 192.168.1.10 --- 0x4
  Endereço IP           Endereço físico       Tipo
  192.168.1.1           00-1a-2b-3c-4d-5e     dinâmico
  192.168.1.20          00-0c-29-aa-10-bb     dinâmico
  192.168.1.255         ff-ff-ff-ff-ff-ff     estático"""
EX[16]=[
 mc('O PC 192.168.1.10/24, cujo gateway é 192.168.1.1, vai acessar 8.8.8.8. Qual MAC de destino o quadro terá?',
    ['00-1a-2b-3c-4d-5e','00-0c-29-aa-10-bb','ff-ff-ff-ff-ff-ff','O MAC de 8.8.8.8'],
    'Destino em outra rede → o host procura o IPv4 do gateway na tabela ARP e usa o MAC dele.','16.2',4,x=ARP_X,xt='arp -a'),
 mc('Depois de um incidente, a tabela ARP de vários PCs mostra o MAC de um notebook desconhecido associado ao IP do gateway. Que ataque ocorreu?',
    ['Envenenamento ARP (ARP spoofing)','Negação de serviço por ping','Phishing','Esgotamento do DHCP'],
    'O atacante responde em nome do gateway para receber os quadros; a DAI ajuda a combater.','16.8',6),
 ms('Quais duas afirmações sobre a solicitação ARP são verdadeiras? (Escolha duas.)',
    ['É enviada em broadcast, para FF-FF-FF-FF-FF-FF','Vai direto no quadro Ethernet (EtherType 0x806), sem IPv4','Atravessa o roteador para chegar a outras redes','Usa a porta UDP 67','É enviada em unicast ao gateway'],
    'A resposta é que é unicast; a solicitação é broadcast e fica na rede local.','16.3',4),
 mc('No IPv6, o ND substitui o ARP. Que tipo de mensagem ele usa no lugar do broadcast?',
    ['Multicast ICMPv6','Broadcast FF-FF-FF-FF-FF-FF','Unicast TCP','Anycast UDP'],
    'O IPv6 não tem broadcast; o ND usa mensagens ICMPv6 em multicast.','16.9',2),
]
RT_X="""R1# show ip route
C     192.168.1.0/24 is directly connected, GigabitEthernet0/0
C     192.168.2.0/24 is directly connected, GigabitEthernet0/1
S     10.10.0.0/16 [1/0] via 192.168.2.254
S*    0.0.0.0/0 [1/0] via 203.0.113.1"""
RT_OPT=['Pela G0/0 (rede conectada)','Pela G0/1 (rede conectada)','Via 192.168.2.254','Via 203.0.113.1 (rota padrão)']
EX[17]=[
 multi('Com base na tabela de R1, indique para onde vai cada pacote.',[
    C('Destino 192.168.2.50',RT_OPT,'Pela G0/1 (rede conectada)'),C('Destino 10.10.4.20',RT_OPT,'Via 192.168.2.254'),C('Destino 8.8.8.8',RT_OPT,'Via 203.0.113.1 (rota padrão)')],
    'C → redes conectadas; S → rotas estáticas; S* 0.0.0.0/0 → rota padrão, usada quando nada mais específico corresponde.','17.3.4',4,x=RT_X,xt='roteador'),
 mc('Um roteador tem as rotas 10.0.0.0/8 e 10.10.0.0/16. Qual delas ele usa para o destino 10.10.1.1?',
    ['10.10.0.0/16, por ser a mais específica','10.0.0.0/8, por ser a primeira','As duas, alternando os pacotes','Nenhuma; usa a rota padrão'],
    'Quando mais de uma rota corresponde, vence a de maior prefixo.','17.3.4',4),
 mc('Uma empresa com dezenas de roteadores quer que as rotas se ajustem sozinhas quando um enlace cai. O que usar?',
    ['Roteamento dinâmico, como o OSPF','Rotas estáticas em todos os roteadores','Somente a rota padrão','VLANs'],
    'O roteamento dinâmico se adapta a falhas e facilita a administração de redes grandes.','17.4.2',4),
 mc('Qual comando mostra a tabela de roteamento de um PC com Windows?',
    ['route print','show ip route','arp -a','ipconfig /all'],'No Cisco IOS, o comando é show ip route.','17.5',5),
]
NS_X="""C:\\> netstat -n
  Proto  Endereço local          Endereço externo        Estado
  TCP    192.168.1.10:49712      142.250.79.14:443       ESTABLISHED
  TCP    192.168.1.10:49715      200.147.3.157:80        ESTABLISHED
  TCP    192.168.1.10:49720      10.0.0.5:22             ESTABLISHED"""
EX[18]=[
 multi('Identifique o serviço de cada conexão mostrada pelo netstat.',[
    C('Conexão para a porta 443',['HTTP','HTTPS','SSH','Telnet'],'HTTPS'),C('Conexão para a porta 80',['HTTP','HTTPS','SSH','Telnet'],'HTTP'),C('Conexão para a porta 22',['HTTP','HTTPS','SSH','Telnet'],'SSH')],
    'A porta de destino (no endereço externo) indica o serviço; as portas locais 49xxx são dinâmicas.','18.6.5',5,x=NS_X,xt='netstat'),
 ms('Quais dois protocolos de aplicação usam UDP? (Escolha dois.)',
    ['DHCP','TFTP','SSH','HTTPS','SMTP'],'DHCP (67/68) e TFTP (69) usam UDP; SSH, HTTPS e SMTP usam TCP.','18.4.2',1),
 mc('Por que aplicações de videochamada costumam usar UDP?',
    ['Priorizam baixa latência, e esperar retransmissões atrasaria a conversa','Precisam de entrega garantida e ordenada','O UDP criptografa a voz','O TCP não funciona em redes sem fio'],
    'O UDP tem menos sobrecarga e não retransmite, o que favorece o tempo real.','18.4.2',1),
 mc('Qual flag TCP reinicia uma conexão quando ocorre um erro?',['RST','FIN','SYN','PSH'],'SYN inicia, FIN encerra, RST reinicia.','18.3.4',1),
]
EX[19]=[
 multi('Uma auditoria pede para trocar cada serviço sem criptografia pela versão segura.',[
    C('Telnet',['SSH','HTTPS','SFTP','TFTP'],'SSH'),C('HTTP',['SSH','HTTPS','SFTP','TFTP'],'HTTPS'),C('FTP',['SSH','HTTPS','SFTP','TFTP'],'SFTP')],
    'Telnet (23) → SSH (22); HTTP (80) → HTTPS (443); FTP → SFTP. O TFTP também não tem criptografia nem autenticação.','19.5',6),
 mc('Uma usuária lê os e-mails no celular e no notebook, mas as mensagens somem do servidor quando o notebook as baixa. Qual protocolo está configurado e qual deveria ser usado?',
    ['POP3; trocar por IMAP','IMAP; trocar por POP3','SMTP; trocar por POP3','HTTPS; trocar por SMTP'],
    'O POP3 baixa e remove do servidor; o IMAP mantém as mensagens no servidor e sincroniza os dispositivos.','19.3',1),
 mc('O ping para 8.8.8.8 funciona, mas nenhum site abre pelo nome. Qual serviço é o suspeito?',
    ['DNS','DHCP','ARP','SMTP'],'Se o IP responde e o nome não, a resolução de nomes falhou.','19.1',5),
 mc('O técnico precisa enviar uma imagem do sistema para um switch usando um protocolo simples, em UDP 69, sem autenticação. Qual é?',
    ['TFTP','FTP','SMB','HTTP'],'O TFTP é usado para transferir configurações e sistemas de equipamentos de rede.','19.4.2',1),
 mc('Na URL https://loja.exemplo.com.br/produtos/item.html#fotos, qual parte o DNS converte em endereço IP?',
    ['loja.exemplo.com.br','https','/produtos/item.html','#fotos'],'O nome do host é resolvido pelo DNS; o resto indica protocolo, caminho e fragmento.','19.2.1',1),
]
TR_X="""C:\\> tracert 200.160.2.3
  1    <1 ms    <1 ms    <1 ms  192.168.1.1
  2     8 ms     7 ms     8 ms  100.64.0.1
  3     *        *        *     Esgotado o tempo limite do pedido.
  4     *        *        *     Esgotado o tempo limite do pedido."""
PING_X="""C:\\> ping 192.168.1.1
Resposta de 192.168.1.1: bytes=32 tempo<1ms TTL=64
Resposta de 192.168.1.1: bytes=32 tempo<1ms TTL=64

C:\\> ping 8.8.8.8
Esgotado o tempo limite do pedido.
Esgotado o tempo limite do pedido."""
EX[20]=[
 multi('Um computador não acessa a Internet. Coloque os testes na ordem recomendada.',ORD(['ipconfig','ping 127.0.0.1','ping no gateway padrão','ping em um IP da Internet','nslookup de um nome','tracert até o destino']),
    'Do próprio host para fora: configuração → TCP/IP local → rede local → Internet → DNS → caminho.','20.7',5,ord=True),
 mc('O que a saída do tracert indica?',
    ['Os pacotes passam pelo gateway e pelo provedor; a falha ou o bloqueio está depois do salto 2','O gateway padrão está desligado','O DNS não está funcionando','O cabo do computador está rompido'],
    'Os saltos 1 e 2 responderam; a partir do 3, não há resposta.','20.3',5,x=TR_X,xt='tracert'),
 mc('O que se conclui destes testes?',
    ['A rede local funciona; o problema está além do gateway ou o ICMP está bloqueado','O TCP/IP do computador não está funcionando','O gateway padrão está errado','O endereço foi obtido por APIPA'],
    'Se o ping no gateway funciona, o problema não está na rede local.','20.2',5,x=PING_X,xt='ping'),
 ms('O ping para um servidor falha, mas o site dele abre normalmente por HTTPS. Quais duas explicações são possíveis? (Escolha duas.)',
    ['Um firewall no caminho bloqueia o ICMP','O servidor está configurado para não responder ao ping','O cabo do computador está desconectado','O DNS do computador está fora do ar','O computador está com endereço APIPA'],
    'Muitos dispositivos e firewalls bloqueiam ICMP; a falta de resposta ao ping nem sempre é falha.','20.2',5),
 mc('Qual comando lista as conexões TCP ativas, com endereços e portas em forma numérica?',
    ['netstat -n','arp -a','nslookup','ipconfig /all'],'Sem o -n, o netstat tenta converter endereços e portas em nomes.','20.5',5),
]
