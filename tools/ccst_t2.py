# Questões no estilo CCST Networking (100-150) — trilha Dispositivos.
from ccst_lib import *
EX={}
EX[1]=[
 mc('Em horário de pico, a voz das chamadas de vídeo da empresa picota, mas os downloads seguem normais. O que o administrador deve configurar?',
    ['Uma política de QoS que priorize o tráfego de voz','Mais largura de banda só para downloads','A desativação do firewall de rede','Um segundo SSID'],
    'A QoS prioriza o tráfego sensível ao tempo quando há congestionamento; ela não cria banda nova.','1.4.2',1),
 multi('Indique o requisito da Tríade CIA afetado em cada incidente.',[
    C('Um ataque de negação de serviço derruba o site',['Confidencialidade','Integridade','Disponibilidade'],'Disponibilidade'),
    C('O valor de uma transferência é alterado no caminho',['Confidencialidade','Integridade','Disponibilidade'],'Integridade'),
    C('Um estagiário lê a planilha de salários',['Confidencialidade','Integridade','Disponibilidade'],'Confidencialidade')],
    'Confidencialidade → quem pode ler; integridade → dados sem alteração; disponibilidade → acesso quando necessário.','1.5.1',6),
 ms('Quais duas medidas são de segurança da infraestrutura de rede, e não da informação? (Escolha duas.)',
    ['Trancar o rack onde ficam os switches','Impedir o acesso não autorizado ao software de gerenciamento dos roteadores','Criptografar os arquivos do servidor','Fazer backup das planilhas dos usuários','Usar HTTPS no site da empresa'],
    'Infraestrutura → proteger fisicamente os equipamentos e o acesso a eles; informação → proteger os dados.','1.5',6),
 mc('O enlace principal entre dois prédios caiu, e o tráfego passou sozinho por um caminho alternativo, sem que os usuários percebessem. Que característica da rede é essa?',
    ['Tolerância a falhas, obtida com redundância','Escalabilidade','Qualidade de serviço','Confidencialidade'],
    'A rede tolerante a falhas usa vários caminhos e continua funcionando quando um componente falha.','1.2',1),
]
EX[2]=[
 mc('Um notebook sai da rede do prédio A e passa a usar a rede do prédio B. O que muda?',
    ['O endereço IP muda; o endereço MAC continua o mesmo','O MAC muda; o IP continua o mesmo','Os dois mudam','Nenhum dos dois muda'],
    'O MAC é físico, gravado na placa; o IP é lógico e depende da rede.','2.1',2),
 mc('Um prédio novo terá 600 usuários. O projetista quer conter os broadcasts e localizar os hosts com facilidade. O que deve fazer?',
    ['Dividir a rede em redes menores, interligadas pela camada de distribuição','Colocar todos os hosts em uma única rede Ethernet','Usar só endereços MAC, sem IP','Ligar todos os switches em série, sem roteador'],
    'Redes Ethernet grandes geram broadcasts demais; a solução é o design hierárquico.','2.2',4),
 ms('Quais dois dispositivos são típicos da camada de acesso? (Escolha dois.)',
    ['Switches de acesso','Pontos de acesso sem fio','Switches modulares de alta velocidade do núcleo','Roteadores que interligam as redes da distribuição','Servidores DNS raiz'],
    'Acesso → conexão dos usuários; distribuição → controle entre redes; núcleo → backbone.','2.4.1',4),
]
EX[3]=[
 mc('Uma startup quer rodar o próprio sistema na nuvem, instalando o sistema operacional e as aplicações, sem comprar servidores. Qual serviço contratar?',
    ['IaaS','SaaS','PaaS','Nuvem comunitária'],
    'No IaaS, o provedor entrega servidores, armazenamento e rede virtualizados; o cliente gerencia o restante.','3.2',1),
 mc('A equipe usa um pacote de escritório pelo navegador, pago por assinatura, sem instalar nada. Que tipo de serviço é esse?',
    ['SaaS','IaaS','PaaS','Hipervisor Tipo 2'],
    'SaaS → software pronto, sob demanda, normalmente por assinatura.','3.2',1),
 ms('Quais duas vantagens a empresa obtém ao consolidar seus servidores em máquinas virtuais? (Escolha duas.)',
    ['Menos equipamentos e menor consumo de energia','Provisionamento mais rápido de novos servidores','Fim da necessidade de rede','Garantia de que o hardware nunca falha','Eliminação dos sistemas operacionais'],
    'Também melhoram a recuperação de desastres e o suporte a sistemas legados.','3.5.1',1),
 mc('Um técnico quer testar o Linux no notebook com Windows, sem apagar o Windows. O que usar?',
    ['Um hipervisor Tipo 2, como o VirtualBox','Um hipervisor Tipo 1, como o ESXi','Um switch virtual Nexus 1000V','Uma nuvem comunitária'],
    'O Tipo 2 é instalado sobre um sistema operacional existente; o Tipo 1, direto no hardware.','3.6.2',1),
 mc('Por exigência legal, um órgão público precisa manter os dados sob seu controle, com acesso restrito à própria organização. Que modelo de nuvem atende?',
    ['Nuvem privada','Nuvem pública','Nuvem comunitária aberta a outros órgãos','SaaS gratuito'],
    'A nuvem privada é destinada a uma organização específica.','3.3.2',1),
]
EX[4]=[
 inp('O primeiro byte de um endereço MAC é 1A. Qual é o valor em decimal?',['26'],'num','(1 × 16) + 10 = 26.','4.3.2',2,ph='decimal'),
 inp('O último octeto de uma máscara é 11100000. Qual é o valor em decimal?',['224'],'num','128 + 64 + 32 = 224.','4.1.2',2,ph='decimal'),
 inp('Um analisador mostra os dois primeiros bytes de um endereço IPv4 como C0 A8. Escreva-os em decimal, separados por ponto.',['192.168'],'ip','C0 = 12 × 16 = 192; A8 = (10 × 16) + 8 = 168.','4.3.1',2,ph='x.x'),
 mc('Qual destes valores não é um número hexadecimal válido?',['1G','FF','0A','C5'],'O hexadecimal usa 0 a 9 e A a F.','4.3',2),
]
SW_X="""S1# show mac address-table
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
   1    0050.7966.6800    DYNAMIC     Fa0/1
   1    0050.7966.6801    DYNAMIC     Fa0/2
   1    0050.7966.6802    DYNAMIC     Fa0/3"""
EX[5]=[
 mc('Um quadro com destino FF-FF-FF-FF-FF-FF chega ao S1 pela Fa0/1. Por onde ele sai?',
    ['Por todas as portas, exceto a Fa0/1','Somente pela Fa0/2','Por nenhuma; broadcast é descartado','Pelo roteador, para outras redes'],
    'O broadcast vai a todas as portas, exceto a de entrada, e não é encaminhado por roteadores.','5.4.2',4,x=SW_X,xt='switch'),
 mc('O PC que estava na Fa0/2 foi ligado na Fa0/5 e enviou um quadro. O que acontece com a tabela?',
    ['A entrada do MAC passa para a Fa0/5, a porta mais recente','O switch descarta o quadro','O switch mantém as duas entradas para sempre','A tabela é apagada inteira'],
    'Mesmo MAC em outra porta → a entrada é atualizada para a porta mais recente.','5.5.2',4,x=SW_X,xt='switch'),
 mc('Uma interface registra muitos quadros menores que 64 bytes. Como esses quadros são chamados?',
    ['Fragmentos de colisão (runts)','Quadros jumbo','Baby giants','Quadros de broadcast'],
    'Quadros fora dos limites são descartados; os menores que 64 bytes costumam vir de colisões.','5.3.1',5),
 ms('Quais dois campos fazem parte do quadro Ethernet? (Escolha dois.)',
    ['Endereços MAC de origem e de destino','FCS (sequência de verificação)','TTL','Porta TCP de destino','Número de sequência'],
    'O quadro tem preâmbulo, SFD, MACs, EtherType, dados e FCS. TTL é do IP; portas e sequência, do transporte.','5.3.2',1),
 mc('Duas placas de rede têm endereços 00-1A-2B-11-22-33 e 00-1A-2B-44-55-66. O que isso indica?',
    ['São do mesmo fabricante, pois têm o mesmo OUI','Estão na mesma VLAN','Têm o mesmo endereço IP','Uma delas é multicast'],
    'Os 3 primeiros bytes (OUI) identificam o fabricante.','5.4',4),
]
EX[6]=[
 inp('Um servidor envia pacotes com TTL inicial 64, e a resposta do ping chega com TTL=58. Por quantos roteadores o pacote passou?',['6'],'num','Cada roteador diminui o TTL em 1: 64 − 58 = 6.','6.4.2',5,ph='número'),
 mc('Por que o NAT atrapalha a conectividade de ponta a ponta?',
    ['Porque vários dispositivos compartilham um endereço público e o endereço interno de cada um fica oculto','Porque aumenta o tamanho do cabeçalho IPv6','Porque remove o TTL','Porque bloqueia o DNS'],
    'O NAT também acrescenta complexidade e latência.','6.5',2),
 ms('Quais duas diferenças do cabeçalho IPv6 em relação ao IPv4 são verdadeiras? (Escolha duas.)',
    ['Não tem soma de verificação do cabeçalho','Tem tamanho fixo de 40 bytes','Os roteadores fragmentam os pacotes','O endereço tem 64 bits','O TTL foi mantido com o mesmo nome'],
    'No IPv6, o TTL virou Limite de Saltos e a fragmentação é feita pela origem.','6.8',2),
 mc('Um pacote IPv6 precisa ser dividido porque o caminho tem MTU menor. Quem faz a fragmentação?',
    ['O dispositivo de origem, com um cabeçalho de extensão','Cada roteador do caminho','O switch de acesso','O servidor DNS'],
    'Os roteadores não fragmentam pacotes IPv6.','6.7.2',2),
]
IP7_X="""Adaptador Ethernet Ethernet:
   Endereço IPv4. . . . . . . . . : 10.10.5.70
   Máscara de Sub-rede . . . . . . : 255.255.255.192
   Gateway Padrão. . . . . . . . . : 10.10.5.65"""
EX[7]=[
 multi('Com base na saída, informe os dados da rede deste computador.',[F('Endereço de rede','10.10.5.64','ip'),F('Primeiro host','10.10.5.65','ip'),F('Broadcast','10.10.5.127','ip'),F('Hosts utilizáveis','62','num')],
    '/26 → blocos de 64: 64 a 127. 2⁶ − 2 = 62 hosts.','7.5.2',2,x=IP7_X,xt='ipconfig'),
 mc('Os hosts 192.168.10.30/27 e 192.168.10.40/27 estão na mesma rede?',
    ['Não: um está em 192.168.10.0/27 e o outro em 192.168.10.32/27','Sim, porque os três primeiros octetos são iguais','Sim, porque a máscara é a mesma','Não dá para saber sem o gateway'],
    '/27 → blocos de 32: 0–31 e 32–63.','7.4.1',2),
 ms('Quais dois endereços podem ser atribuídos a hosts da rede 172.16.4.0/22? (Escolha dois.)',
    ['172.16.5.0','172.16.7.254','172.16.4.0','172.16.7.255','172.16.8.1'],
    '/22 → 172.16.4.0 a 172.16.7.255. O primeiro é a rede, o último é o broadcast, e 172.16.8.1 está fora.','7.5',2),
 inp('Quantos bits de host tem uma rede /22?',['10'],'num','32 − 22 = 10 bits de host (2¹⁰ − 2 = 1.022 hosts).','7.5.1',2,ph='bits'),
 mc('Um PC foi configurado manualmente com 192.168.1.255/24 e não se comunica. Qual é o problema?',
    ['Esse é o endereço de broadcast da rede e não pode ser atribuído a um host','O endereço é público','Falta o servidor DNS','O prefixo deveria ser /32'],
    'Bits de host todos em 1 → broadcast; todos em 0 → endereço de rede.','7.5',2),
]
ARPR_X="""R1# show ip arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.10.1            -   0011.2233.4401  ARPA   GigabitEthernet0/0/0
Internet  192.168.10.20           3   00e0.4c68.1234  ARPA   GigabitEthernet0/0/0
Internet  192.168.11.30           1   00e0.4c68.5678  ARPA   GigabitEthernet0/0/1"""
EX[8]=[
 mc('Pela tabela ARP de R1, por qual interface o roteador alcança o host 192.168.11.30?',
    ['GigabitEthernet0/0/1','GigabitEthernet0/0/0','Pelas duas interfaces','Por nenhuma; o host está em outra rede'],
    'Cada mapeamento mostra o IPv4, o MAC e a interface em que ele foi aprendido.','8.1.5',5,x=ARPR_X,xt='roteador'),
 ms('O PC 192.168.10.10/24 (gateway 192.168.10.1) envia dados para 172.16.1.1. Quais duas afirmações são verdadeiras? (Escolha duas.)',
    ['Ele procura na tabela ARP o endereço do gateway, 192.168.10.1','O IP de destino do pacote continua 172.16.1.1','Ele envia uma solicitação ARP perguntando por 172.16.1.1','O MAC de destino do quadro é o de 172.16.1.1','O roteador encaminha a solicitação ARP para a rede 172.16.1.0'],
    'Destino em outra rede → o host resolve o MAC do gateway; o ARP fica na rede local.','8.1.2',4),
 mc('Qual recurso de switches corporativos ajuda a combater o envenenamento ARP?',
    ['DAI (Dynamic ARP Inspection)','DHCPv6','NAT','QoS'],'O envenenamento ARP grava o MAC do atacante no lugar do gateway; a DAI ajuda a impedir.','8.2.2',6),
 mc('Um técnico liga um PC novo e o primeiro ping para o servidor da rede local falha, mas os seguintes funcionam. Por quê?',
    ['O PC ainda precisava descobrir o MAC do destino pelo ARP','O servidor estava desligado','O TTL do primeiro ping era zero','O DNS estava em cache'],
    'Enquanto o ARP resolve o endereço, a primeira solicitação pode não sair a tempo.','13.3',5),
]
NS2_X="""C:\\> netstat -n
  Proto  Endereço local        Endereço externo        Estado
  TCP    10.1.1.5:49200        10.1.1.100:443          ESTABLISHED
  TCP    10.1.1.5:49210        10.1.1.100:22           ESTABLISHED
  TCP    10.1.1.5:49215        185.199.108.9:4444      ESTABLISHED"""
EX[9]=[
 mc('Durante um atendimento, o técnico roda o netstat no PC do usuário. Qual conexão merece investigação de segurança?',
    ['A conexão com 185.199.108.9 na porta 4444','A conexão com 10.1.1.100 na porta 443','A conexão com 10.1.1.100 na porta 22','Nenhuma; todas são normais'],
    'Conexões desconhecidas, para portas incomuns e endereços externos, podem indicar uma ameaça.','9.3.4',6,x=NS2_X,xt='netstat'),
 mc('O firewall da empresa bloqueia conexões de entrada para a porta TCP 23. Que serviço fica bloqueado?',
    ['Telnet','SSH','SMTP','DNS'],'Telnet → TCP 23; SSH → 22; SMTP → 25; DNS → 53.','9.3.3',6),
 mc('Os usuários precisam navegar em sites seguros. Que regra de saída o firewall precisa permitir?',
    ['TCP 443','UDP 69','TCP 23','UDP 161'],'HTTPS usa TCP 443.','9.3.3',6),
 ms('Quais duas portas bem conhecidas usam UDP? (Escolha duas.)',
    ['69 (TFTP)','161 (SNMP)','22 (SSH)','25 (SMTP)','443 (HTTPS)'],'UDP: 53 (consultas DNS), 67/68 (DHCP), 69 (TFTP) e 161 (SNMP).','9.3.3',1),
 inp('O PC B anunciou janela de 10.000 bytes e acabou de confirmar com ACK 2.921. Até que byte o PC A pode enviar sem nova confirmação?',['12920','12.920'],'num','A janela desliza: 2.920 + 10.000 = 12.920.','9.5.3',1,ph='byte'),
 mc('Na resposta de um servidor Web, quais são as portas de origem e de destino, se a solicitação saiu da porta 49152 para a 80?',
    ['Origem 80, destino 49152','Origem 49152, destino 80','Origem 80, destino 80','Origem 443, destino 49152'],'Na resposta, o servidor inverte as portas da solicitação.','9.4.4',1),
]
EX[10]=[
 mc('O ping para www.empresa.com.br diz que o host não foi encontrado, mas o ping para 8.8.8.8 funciona. Qual utilitário o técnico usa para investigar?',
    ['nslookup','arp -a','netstat','ipconfig /release'],'O nslookup consulta o servidor DNS manualmente.','10.1.6',5),
 mc('O site da empresa mudou de servidor, mas alguns PCs continuam acessando o endereço antigo. Qual é a explicação?',
    ['A resposta antiga ainda está no cache DNS desses PCs','O DHCP distribuiu o IP errado','O registro MX está errado','O TLD .br está fora do ar'],
    'Servidores e clientes guardam as respostas em cache; o ipconfig /displaydns mostra o cache do Windows.','10.1.3',5),
 mc('Um café recebe 200 visitantes por dia e o pool DHCP tem 100 endereços, que se esgotam à tarde. O que ajuda?',
    ['Reduzir o período de concessão, para os endereços voltarem ao pool mais cedo','Aumentar o período de concessão','Usar endereços estáticos nos celulares','Desativar o DHCP'],
    'O endereço volta ao pool quando a concessão termina ou quando o cliente envia DHCPRELEASE.','10.2.2',2),
 ms('Quais duas informações o servidor DHCPv4 entrega ao cliente? (Escolha duas.)',
    ['A máscara de sub-rede','O gateway padrão','O endereço MAC do cliente','A tabela ARP do roteador','O registro MX do domínio'],
    'Também entrega o endereço IPv4, o servidor DNS e a duração da concessão.','10.2',2),
 mc('Dois servidores DHCP responderam com ofertas. Como o cliente informa qual oferta aceitou?',
    ['Na mensagem DHCPREQUEST, identificando o servidor escolhido','Com um DHCPACK para cada servidor','Com um DHCPNAK para o servidor recusado','Não informa; usa as duas'],
    'DORA: Discover → Offer → Request (com o servidor escolhido) → Ack.','10.2.4',2),
]
AMB_X="""Switch# con
% Ambiguous command:  "con"
Switch# conf
Configuring from terminal, memory, or network [terminal]?"""
EX[11]=[
 mc('No prompt Switch>, o técnico digita configure terminal e recebe erro. Por quê?',
    ['Ele precisa estar no EXEC privilegiado; antes, deve digitar enable','O comando está errado; o certo é config all','O switch não tem modo de configuração','Falta salvar a configuração'],
    'Os modos de configuração só são acessados a partir do EXEC privilegiado (#).','11.2.4',5),
 mc('O que a saída mostra sobre a abreviação de comandos?',
    ['"con" corresponde a mais de um comando; "conf" já identifica configure','O IOS não aceita abreviações','"con" é o comando de console','O switch está sem memória'],
    'Comandos podem ser abreviados até o menor número de letras que os identifique de forma única.','11.3.3',5,x=AMB_X,xt='switch'),
 mc('O técnico não lembra o que vem depois de "show ip". O que ele digita para ver as opções?',
    ['show ip ?','help show ip','show ip --list','? show ip'],'Comando seguido de espaço e ? mostra as palavras-chave e argumentos possíveis.','11.3.2',5),
 ms('Quais duas formas de acesso à CLI dependem da rede estar funcionando (dentro da banda)? (Escolha duas.)',
    ['SSH','Telnet','Porta de console','Cabo direto no console','Acesso físico ao equipamento desligado'],
    'O console é fora da banda e é usado na configuração inicial.','11.1',5),
]
SVI_X="""S1(config)# interface vlan 1
S1(config-if)# ip address 192.168.1.20 255.255.255.0
S1(config-if)# exit
S1(config)# ip default-gateway 192.168.1.1"""
VTY_X="""S1# show running-config
...
line vty 0 15
 password 7 0822455D0A16
 login
 transport input telnet
..."""
EX[12]=[
 mc('Depois desta configuração, ninguém consegue pingar o S1. O que faltou?',
    ['O comando no shutdown na interface vlan 1','O comando ip routing','Um servidor DHCP','O comando hostname'],
    'A SVI precisa ser ativada com no shutdown.','12.2.2',4,x=SVI_X,xt='switch'),
 mc('A política da empresa exige acesso remoto criptografado ao S1. O que o técnico deve fazer?',
    ['Configurar o SSH e trocar para transport input ssh, com login local','Trocar a senha das linhas VTY','Usar service password-encryption','Desativar as linhas VTY 5 a 15'],
    'O Telnet envia usuário e senha em texto simples; o SSH criptografa.','12.4.3',6,x=VTY_X,xt='switch'),
 mc('O técnico configurou o switch, reiniciou o equipamento e perdeu toda a configuração. O que faltou?',
    ['Salvar com copy running-config startup-config','Usar o comando end','Configurar a VLAN 1','Usar o enable secret'],
    'A running-config fica na RAM e é perdida ao desligar; a startup-config fica na NVRAM.','12.1.3',4),
 ms('Quais dois itens precisam estar configurados antes de gerar as chaves RSA para o SSH? (Escolha dois.)',
    ['Um nome de host exclusivo','O domínio IP (ip domain-name)','Um servidor DHCP','A VLAN 99','O protocolo Telnet'],
    'Antes do crypto key generate rsa: hostname exclusivo e ip domain-name.','12.4.3',6),
 mc('As senhas de console e VTY aparecem em texto simples no show running-config. Qual comando resolve?',
    ['service password-encryption','enable secret','login local','transport input ssh'],
    'Ele criptografa as senhas guardadas em texto simples; as definidas com secret já ficam com hash.','12.4.2',6),
]
PING13_X="""C:\\> ping 192.168.1.1
Resposta de 192.168.1.1: bytes=32 tempo<1ms TTL=255
Resposta de 192.168.1.1: bytes=32 tempo<1ms TTL=255

C:\\> ping 10.50.0.10
Esgotado o tempo limite do pedido.
Esgotado o tempo limite do pedido."""
TR13_X="""C:\\> tracert 10.50.0.10
  1    <1 ms    <1 ms    <1 ms  192.168.1.1
  2     3 ms     2 ms     3 ms  10.0.0.2
  3     *        *        *     Esgotado o tempo limite do pedido.
  4     6 ms     5 ms     6 ms  10.20.0.1
  5     7 ms     7 ms     6 ms  10.50.0.10"""
EX[13]=[
 mc('O que se conclui destes testes?',
    ['O host e o gateway funcionam; o problema está depois do gateway ou o ICMP está bloqueado','O TCP/IP do host não está instalado','O cabo do host está desconectado','O gateway padrão está errado'],
    'Do mais próximo para o mais distante: loopback → gateway → host remoto.','13.3.1',5,x=PING13_X,xt='ping'),
 mc('No tracert, o salto 3 mostra asteriscos, mas o destino é alcançado no salto 5. O que isso indica?',
    ['O roteador do salto 3 não respondeu ao traceroute, mas encaminhou os pacotes','A conexão com o destino falhou','O destino bloqueia ping','O salto 3 é o gateway padrão'],
    'O asterisco é uma resposta que não veio; como os saltos seguintes responderam, o caminho funciona.','13.4.1',5,x=TR13_X,xt='tracert'),
 ms('Quais duas mensagens ICMP o traceroute usa para montar o caminho? (Escolha duas.)',
    ['Tempo excedido, enviada pelos roteadores','Porta inalcançável (ou resposta de eco), enviada pelo destino','Solicitação de roteador (RS)','DHCPDISCOVER','Redirecionamento'],
    'Cada roteador que zera o TTL envia tempo excedido; o destino responde com porta inalcançável ou eco.','13.4.2',5),
 mc('Um host IPv6 se configurou por SLAAC. Qual endereço ele usa como gateway padrão?',
    ['O do roteador que enviou a RA','O do servidor DHCPv6','::1','FF02::1'],
    'No SLAAC, o host monta o próprio endereço com as informações da RA e usa o roteador como gateway.','13.2.1',2),
 mc('O ping para ::1 falha. O que isso indica?',
    ['O IPv6 não está funcionando no próprio host','O gateway IPv6 está desligado','O DNS IPv6 está errado','O cabo está desconectado'],
    '::1 é o loopback do IPv6; o teste não depende da rede.','13.3.1',5),
]
