# Exercícios da trilha "Dispositivos de Rede e Configuração Inicial"
# mc: a primeira opção é a correta (o site embaralha). in: resposta digitada. multi: vários campos.
def mc(q,o,e,r): return {'t':'mc','q':q,'o':o,'e':e,'r':r}
def inp(q,a,n,e,r,ph=None,d=None):
    x={'t':'in','q':q,'a':a,'n':n,'e':e,'r':r}
    if ph: x['ph']=ph
    if d: x['d']=d
    return x
def multi(q,f,e,r): return {'t':'multi','q':q,'f':f,'e':e,'r':r}
def F(l,a,n,d=None,ph=None):
    x={'l':l,'a':a if isinstance(a,list) else [a],'n':n}
    if d: x['d']=d
    if ph: x['ph']=ph
    return x
def C(l,ch,a): return {'l':l,'ch':ch,'a':a}

EX={}
EX[1]=[
 mc('Quais são as quatro características básicas que a arquitetura de uma rede confiável deve garantir?',
    ['Tolerância a falhas, escalabilidade, QoS e segurança','Velocidade, cobertura, custo e segurança','Redundância, broadcast, QoS e criptografia','Escalabilidade, virtualização, roteamento e DNS'],
    'A arquitetura de rede deve garantir tolerância a falhas, escalabilidade, qualidade de serviço (QoS) e segurança.','1.1'),
 mc('Como se chama a existência de vários caminhos entre a origem e o mesmo destino?',
    ['Redundância','Escalabilidade','Congestionamento','Convergência'],
    'Redundância é ter vários caminhos até o mesmo destino; se um falhar, as mensagens seguem por outro.','1.2'),
 mc('Na comutação de pacotes, o que acontece quando um enlace falha no meio do caminho?',
    ['O roteador altera a rota automaticamente e o usuário não percebe','A mensagem inteira é perdida e precisa ser reenviada pelo usuário','Todos os pacotes passam a seguir obrigatoriamente o mesmo caminho','A rede para até o enlace ser consertado'],
    'Cada pacote leva origem e destino, então os roteadores escolhem outro caminho sozinhos.','1.2.1'),
 mc('O que torna uma rede escalável?',
    ['O uso de padrões e protocolos aceitos','O uso de um único caminho entre os hosts','A priorização do tráfego de voz','A criptografia dos dados'],
    'A rede cresce sem perder desempenho porque os projetistas seguem padrões e protocolos aceitos.','1.3'),
 mc('Em uma rede congestionada, entre uma ligação de voz e o download de um arquivo, o que a QoS prioriza?',
    ['A ligação de voz, porque é sensível ao tempo','O download, porque é maior','Os dois igualmente','O que chegou primeiro ao roteador'],
    'A QoS prioriza o tráfego sensível ao tempo; um atraso na voz corta a conversa.','1.4.2'),
 mc('Qual afirmação sobre a QoS está correta?',
    ['Ela decide quem passa primeiro, mas não aumenta a largura de banda','Ela aumenta a largura de banda disponível','Ela analisa o conteúdo das mensagens para priorizá-las','Ela só funciona quando a rede está vazia'],
    'A QoS considera o tipo de tráfego, não o conteúdo, e não cria largura de banda nova.','1.4.2'),
 multi('Associe cada requisito da segurança da informação à sua definição.',[
    C('Confidencialidade',['Só os autorizados leem os dados','Os dados não são alterados no caminho','Os autorizados acessam quando precisam'],'Só os autorizados leem os dados'),
    C('Integridade',['Só os autorizados leem os dados','Os dados não são alterados no caminho','Os autorizados acessam quando precisam'],'Os dados não são alterados no caminho'),
    C('Disponibilidade',['Só os autorizados leem os dados','Os dados não são alterados no caminho','Os autorizados acessam quando precisam'],'Os autorizados acessam quando precisam')],
    'Confidencialidade, integridade e disponibilidade formam a Tríade CIA.','1.5.1'),
 inp('Qual é o nome do conjunto formado por confidencialidade, integridade e disponibilidade? (sigla)',['cia','triadecia'],'txt','É a Tríade CIA (Confidentiality, Integrity and Availability).','1.5.1',ph='sigla',d='CIA'),
 mc('Qual é a diferença entre um firewall pessoal e um firewall de rede?',
    ['O pessoal protege um único dispositivo; o de rede protege a rede inteira, na borda','O pessoal é físico; o de rede é sempre um software','O pessoal fica na borda da rede; o de rede fica no computador','Não há diferença, são nomes do mesmo recurso'],
    'Firewall pessoal → um dispositivo; firewall de rede → toda a rede, entre a rede interna e a Internet.','1.5.2'),
]
EX[2]=[
 mc('Por que o endereço MAC é chamado de endereço físico?',
    ['Porque é gravado na placa de rede e não muda quando o host troca de rede','Porque indica onde o host está localizado','Porque é configurado pelo administrador','Porque muda a cada nova conexão'],
    'O MAC é gravado na NIC e não muda, como o nome de uma pessoa.','2.1.1'),
 mc('Por que o endereço IP é chamado de endereço lógico?',
    ['Porque é atribuído de acordo com a rede e muda quando o host troca de rede','Porque é gravado de fábrica na placa','Porque tem 48 bits','Porque identifica o fabricante'],
    'O IP depende da rede em que o host está, como o endereço residencial.','2.1.2'),
 multi('Complete: o endereço MAC diz ___ é o dispositivo; o endereço IP diz ___ ele está.',[
    C('MAC',['quem','onde'],'quem'),C('IP',['quem','onde'],'onde')],
    'MAC → quem é; IP → onde está.','2.1.2'),
 mc('Quais são os dois motivos pelos quais redes Ethernet grandes, com muitos hosts, não são eficientes?',
    ['É difícil localizar um host só pelo MAC, e o excesso de broadcasts sobrecarrega a rede','Os cabos ficam longos demais e o MAC muda com frequência','O IP acaba e os switches desligam','O roteador não encaminha unicast e o DNS falha'],
    'Por isso a rede é dividida em redes menores, num design hierárquico.','2.2'),
 mc('Qual vantagem do design hierárquico mantém o tráfego local e restringe os broadcasts a cada rede menor?',
    ['Desempenho','Redundância','Escalabilidade','Facilidade de gerenciamento'],
    'Desempenho: o tráfego local permanece local e os broadcasts ficam restritos.','2.3'),
 multi('Indique a camada do modelo hierárquico responsável por cada função.',[
    C('Conectar os dispositivos dos usuários',['Acesso','Distribuição','Núcleo'],'Acesso'),
    C('Controlar o tráfego entre as redes',['Acesso','Distribuição','Núcleo'],'Distribuição'),
    C('Transportar grandes volumes de dados rapidamente',['Acesso','Distribuição','Núcleo'],'Núcleo')],
    'Acesso → usuários; distribuição → controle entre redes; núcleo → backbone de alta velocidade.','2.5'),
 mc('Um host da camada de acesso envia dados para um destino em outra rede. Para onde a mensagem vai?',
    ['Para a camada de distribuição','Fica na camada de acesso','Vai direto para o núcleo, sem passar pela distribuição','É descartada'],
    'Destino em outra rede → a mensagem segue para a camada de distribuição.','2.4.1'),
 mc('Quais dispositivos são típicos da camada de núcleo?',
    ['Roteadores e switches modulares de alta velocidade','Pontos de acesso sem fio','Computadores e impressoras','Hubs'],
    'O núcleo é o backbone de alta velocidade. Exemplo: Cisco Catalyst 9600.','2.4.3'),
]
SVC=['SaaS','PaaS','IaaS']
EX[3]=[
 multi('Classifique cada serviço de nuvem.',[
    C('E-mail online',SVC,'SaaS'),C('Servidores virtuais alugados',SVC,'IaaS'),C('Ambiente para desenvolver e publicar aplicações',SVC,'PaaS')],
    'SaaS → software pronto; PaaS → plataforma para desenvolvedores; IaaS → infraestrutura virtualizada.','3.2'),
 mc('No IaaS, o que fica sob responsabilidade do cliente?',
    ['Sistemas operacionais, aplicações e dados','Apenas o uso do aplicativo','Somente os dados','Nada; o provedor gerencia tudo'],
    'No IaaS o provedor entrega servidores, armazenamento e rede; o cliente instala e gerencia o restante.','3.2'),
 mc('Um grupo de hospitais precisa cumprir as mesmas leis de proteção de dados. Qual tipo de nuvem é indicado?',
    ['Comunitária','Pública','Híbrida','Privada de um único hospital'],
    'A nuvem comunitária é personalizada para uma comunidade com necessidades em comum.','3.3.4'),
 mc('Qual tipo de nuvem combina duas ou mais nuvens, como uma parte privada e outra pública?',
    ['Híbrida','Comunitária','Pública','Privada'],
    'A nuvem híbrida une nuvens diferentes em uma única arquitetura.','3.3.3'),
 mc('No modelo de servidores dedicados, o que é a "expansão de servidores" (server sprawl)?',
    ['Um servidor físico para cada serviço, aumentando espaço, energia e refrigeração','Um servidor que falha e derruba o serviço','Um servidor com recursos ociosos','A migração de servidores para a nuvem'],
    'Os três problemas são ponto único de falha, subutilização e expansão de servidores.','3.4'),
 mc('Qual afirmação sobre nuvem e virtualização está correta?',
    ['A virtualização é a tecnologia; a nuvem é o serviço oferecido a partir dela','São sinônimos','A nuvem é a tecnologia; a virtualização é o serviço','A virtualização só existe dentro da nuvem pública'],
    'Nuvem e virtualização não são sinônimos.','3.5'),
 multi('Classifique cada hipervisor.',[
    C('VMware ESXi',['Tipo 1','Tipo 2'],'Tipo 1'),C('Oracle VirtualBox',['Tipo 1','Tipo 2'],'Tipo 2'),
    C('Microsoft Hyper-V',['Tipo 1','Tipo 2'],'Tipo 1'),C('VMware Workstation',['Tipo 1','Tipo 2'],'Tipo 2')],
    'Tipo 1 (bare metal) → direto no hardware; Tipo 2 (hospedado) → sobre um sistema operacional.','3.6'),
 mc('Por que o hipervisor Tipo 1 é mais eficiente que o Tipo 2?',
    ['Porque é instalado diretamente no hardware e tem acesso direto aos recursos','Porque roda sobre o Windows','Porque não usa máquinas virtuais','Porque não precisa de processador'],
    'Sem sistema operacional por baixo, o Tipo 1 tem acesso direto ao hardware.','3.7'),
 inp('Com a virtualização, 100 servidores físicos foram consolidados em 10. Quantas máquinas virtuais, em média, cada servidor físico executa?',['10'],'num','100 ÷ 10 = 10 VMs por servidor físico.','3.6',ph='número'),
]
EX[4]=[
 inp('Converta 10000000 para decimal.',['128'],'num','Só o bit de valor 128 está ligado.','4.1.2',ph='decimal'),
 inp('Converta 11111111 para decimal.',['255'],'num','128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255.','4.1.2',ph='decimal'),
 inp('Converta 10101010 para decimal.',['170'],'num','128 + 32 + 8 + 2 = 170.','4.1.2',ph='decimal'),
 inp('Converta 01100100 para decimal.',['100'],'num','64 + 32 + 4 = 100.','4.1.2',ph='decimal'),
 inp('Converta 11000000.10101000.00000001.00001010 para decimal pontilhado.',['192.168.1.10'],'ip','192 · 168 · 1 · 10: cada octeto é convertido separadamente.','4.1.3',ph='x.x.x.x'),
 inp('Converta 172 para binário (8 bits).',['10101100'],'bin','172 − 128 = 44 − 32 = 12 − 8 = 4 − 4 = 0 → 10101100.','4.1.4',ph='8 bits'),
 inp('Converta 224 para binário (8 bits).',['11100000'],'bin','224 − 128 = 96 − 64 = 32 − 32 = 0 → 11100000.','4.1.4',ph='8 bits'),
 inp('Converta 99 para binário (8 bits).',['01100011'],'bin','99 − 64 = 35 − 32 = 3 − 2 = 1 − 1 = 0 → 01100011.','4.1.4',ph='8 bits'),
 inp('Converta 10.1.200.254 para binário.',['00001010.00000001.11001000.11111110'],'bin','10 = 00001010; 1 = 00000001; 200 = 11001000; 254 = 11111110.','4.1.5',ph='4 octetos'),
 multi('Converta para hexadecimal (dois dígitos).',[
    F('255','FF','hex'),F('168','A8','hex'),F('10','0A','hex',d='0A'),F('192','C0','hex')],
    '255 = FF; 168 = 1010 1000 = A8; 10 = 0000 1010 = 0A; 192 = 1100 0000 = C0.','4.3.1'),
 multi('Converta para decimal.',[F('0x1F','31','num'),F('0xA0','160','num'),F('0xFF','255','num'),F('0x3C','60','num')],
    '(1 × 16) + 15 = 31; (10 × 16) + 0 = 160; (15 × 16) + 15 = 255; (3 × 16) + 12 = 60.','4.3.2'),
 inp('Converta 250 para hexadecimal pelo método de dividir por 16.',['FA'],'hex','250 ÷ 16 = 15, resto 10. 15 = F e 10 = A → FA.','4.3.2',ph='hex'),
 multi('Quantos dígitos hexadecimais são necessários para escrever cada endereço?',[F('Endereço MAC (48 bits)','12','num'),F('Endereço IPv6 (128 bits)','32','num')],
    'Cada dígito hexadecimal representa 4 bits: 48 ÷ 4 = 12 e 128 ÷ 4 = 32.','4.4'),
]
MACT=['Unicast','Broadcast','Multicast']
EX[5]=[
 mc('Em quais camadas do modelo OSI a Ethernet atua?',
    ['Física (1) e enlace de dados (2)','Rede (3) e transporte (4)','Somente na camada de rede','Aplicação (7) e apresentação (6)'],
    'A Ethernet transmite os bits (camada 1) e organiza-os em quadros com endereços MAC (camada 2).','5'),
 mc('No nome 100BASE-T, o que indica a letra T?',
    ['O tipo de cabo: par trançado','A velocidade em terabits','A transmissão em banda larga','O padrão IEEE 802.3T'],
    '100 → 100 Mbps; BASE → banda base; T → par trançado.','5.1.2'),
 mc('Qual subcamada de enlace indica no quadro qual protocolo de rede é transportado?',
    ['LLC (IEEE 802.2)','MAC (IEEE 802.3)','CSMA/CD','FCS'],
    'A LLC liga o software das camadas superiores ao hardware; a MAC encapsula e controla o acesso ao meio.','5.2.1'),
 mc('Por que as redes atuais, com switches, não precisam do CSMA/CD?',
    ['Porque funcionam em full-duplex, enviando e recebendo ao mesmo tempo','Porque usam hubs','Porque não usam endereços MAC','Porque funcionam em half-duplex'],
    'O CSMA/CD era necessário no meio compartilhado em half-duplex dos hubs.','5.2.3'),
 multi('Qual é o tamanho mínimo e o máximo de um quadro Ethernet, em bytes?',[F('Mínimo','64','num'),F('Máximo','1518','num')],
    'Contados do MAC de destino até o FCS; o preâmbulo não entra.','5.3.1'),
 multi('Que protocolo é transportado quando o campo EtherType vale:',[
    C('0x800',['IPv4','IPv6','ARP'],'IPv4'),C('0x86DD',['IPv4','IPv6','ARP'],'IPv6'),C('0x806',['IPv4','IPv6','ARP'],'ARP')],
    '0x800 → IPv4; 0x86DD → IPv6; 0x806 → ARP.','5.3.2'),
 mc('O que o receptor faz quando o valor CRC calculado é diferente do campo FCS?',
    ['Descarta o quadro, porque os dados foram alterados','Corrige o quadro automaticamente','Encaminha o quadro mesmo assim','Pede ao roteador que refaça o cálculo'],
    'Valores iguais → sem erros; diferentes → o quadro é descartado.','5.3.3'),
 mc('O que os 3 primeiros bytes de um endereço MAC (OUI) identificam?',
    ['O fabricante da placa','A rede em que o host está','A porta do switch','O tipo de cabo'],
    'OUI → fabricante; os 3 últimos bytes identificam a placa dentro daquele fabricante.','5.4'),
 multi('Classifique cada endereço MAC de destino.',[
    C('FF-FF-FF-FF-FF-FF',MACT,'Broadcast'),C('01-00-5E-00-00-05',MACT,'Multicast'),C('00-1A-2B-3C-4D-5E',MACT,'Unicast'),C('33-33-00-00-00-01',MACT,'Multicast')],
    'FF-FF... → broadcast; 01-00-5E → multicast IPv4; 33-33 → multicast IPv6; o resto é unicast.','5.4.4'),
 mc('Um switch recém-ligado tem o PC-A na porta 1, o PC-B na 2 e o PC-C na 3. O PC-A envia um quadro ao PC-C. O que acontece?',
    ['O switch registra o MAC do PC-A na porta 1 e envia o quadro pelas portas 2 e 3','O switch registra o MAC do PC-C na porta 3 e envia só por ela','O switch descarta o quadro porque a tabela está vazia','O switch envia o quadro por todas as portas, inclusive a 1'],
    'O switch aprende pelo MAC de origem; destino desconhecido → unicast desconhecido, por todas as portas exceto a de entrada.','5.5.2'),
 mc('Em seguida, o PC-C responde ao PC-A. Por onde o switch envia o quadro?',
    ['Somente pela porta 1','Pelas portas 1 e 2','Por todas as portas','Somente pela porta 3'],
    'Ele registra o PC-C na porta 3 e, como já conhece o PC-A, filtra o quadro para a porta 1.','5.5.3'),
 mc('O PC1 envia dados para um host em outra rede. Qual MAC de destino vai no quadro?',
    ['O MAC do gateway padrão','O MAC do host remoto','FF-FF-FF-FF-FF-FF','O MAC do próprio PC1'],
    'O IP de destino continua o do host remoto; o MAC de destino passa a ser o do gateway.','5.5.5'),
]
EX[6]=[
 multi('Coloque em ordem as quatro operações básicas da camada de rede.',[
    C('1ª',['Endereçamento','Encapsulamento','Roteamento','Desencapsulamento'],'Endereçamento'),
    C('2ª',['Endereçamento','Encapsulamento','Roteamento','Desencapsulamento'],'Encapsulamento'),
    C('3ª',['Endereçamento','Encapsulamento','Roteamento','Desencapsulamento'],'Roteamento'),
    C('4ª',['Endereçamento','Encapsulamento','Roteamento','Desencapsulamento'],'Desencapsulamento')],
    'Endereçamento → encapsulamento (na origem) → roteamento → desencapsulamento (no destino).','6.1'),
 mc('Como se chama cada roteador pelo qual o pacote passa até chegar ao destino?',['Salto (hop)','Segmento','Quadro','Socket'],'Cada roteador do caminho é um salto.','6.1'),
 mc('O que acontece com os endereços IP de origem e de destino durante o caminho (sem NAT)?',
    ['Permanecem os mesmos do início ao fim','Mudam a cada roteador','O de destino muda para o do gateway','São removidos pelos switches'],
    'Só o NAT substitui o endereço de origem; sem ele, os IPs não mudam.','6.2'),
 mc('Por que o IP é chamado de "melhor esforço"?',
    ['Porque não garante a entrega nem retransmite pacotes perdidos','Porque escolhe sempre o caminho mais rápido','Porque confirma cada pacote recebido','Porque estabelece uma conexão antes do envio'],
    'A entrega garantida fica com o TCP, na camada de transporte.','6.3.2'),
 mc('Qual característica do meio o IP leva em conta para definir o tamanho dos pacotes?',['A MTU','O TTL','O FCS','O OUI'],'A MTU é o maior pacote que o meio transporta; se o próximo meio tiver MTU menor, o IPv4 é fragmentado.','6.3.4'),
 inp('Um pacote IPv4 sai do host com TTL 64 e passa por 3 roteadores. Qual é o TTL ao chegar ao destino?',['61'],'num','Cada roteador diminui 1: 64 − 3 = 61.','6.4.2',ph='número'),
 multi('Qual protocolo o campo Protocolo do IPv4 indica em cada valor?',[
    C('1',['ICMP','TCP','UDP'],'ICMP'),C('6',['ICMP','TCP','UDP'],'TCP'),C('17',['ICMP','TCP','UDP'],'UDP')],
    'ICMP (1), TCP (6) e UDP (17).','6.4.1'),
 multi('Qual campo do IPv6 substitui cada campo do IPv4?',[
    C('TTL',['Limite de Saltos','Próximo Cabeçalho','Classe de Tráfego','Etiqueta de Fluxo'],'Limite de Saltos'),
    C('Protocolo',['Limite de Saltos','Próximo Cabeçalho','Classe de Tráfego','Etiqueta de Fluxo'],'Próximo Cabeçalho'),
    C('Serviços Diferenciados',['Limite de Saltos','Próximo Cabeçalho','Classe de Tráfego','Etiqueta de Fluxo'],'Classe de Tráfego')],
    'TTL → Limite de Saltos; Protocolo → Próximo Cabeçalho; DS → Classe de Tráfego.','6.7.1'),
 mc('Qual afirmação sobre o IPv6 está correta?',
    ['Os roteadores não fragmentam pacotes IPv6','O cabeçalho tem soma de verificação recalculada a cada salto','O cabeçalho varia de 20 a 60 bytes','Os endereços têm 32 bits'],
    'No IPv6, a fragmentação é feita pela origem, com um cabeçalho de extensão.','6.7.2'),
 multi('Complete o comparativo.',[F('Tamanho do cabeçalho IPv6 (bytes)','40','num'),F('Cabeçalho IPv4 mínimo (bytes)','20','num'),F('Cabeçalho IPv4 máximo (bytes)','60','num')],
    'IPv6: fixo de 40 bytes; IPv4: 20 a 60 bytes.','6.8'),
 mc('Qual destes é um problema do IPv4 resolvido pelo IPv6?',
    ['O esgotamento dos endereços','A falta de endereços MAC','A ausência de roteamento','O uso de hexadecimal'],
    'O IPv4 tem cerca de 4,3 bilhões de endereços; o IPv6, cerca de 340 undecilhões.','6.5'),
]
EX[7]=[
 multi('Escreva o prefixo de cada máscara.',[F('255.255.0.0','16','pfx'),F('255.255.255.192','26','pfx'),F('255.255.255.248','29','pfx')],
    'O prefixo é a quantidade de bits 1: 16, 26 (24 + 2) e 29 (24 + 5).','7.3'),
 multi('Escreva a máscara de cada prefixo.',[F('/8','255.0.0.0','ip'),F('/25','255.255.255.128','ip'),F('/28','255.255.255.240','ip')],
    '/25 → último octeto 10000000 = 128; /28 → 11110000 = 240.','7.3'),
 inp('Use a operação AND para encontrar o endereço de rede de 172.16.45.200/16.',['172.16.0.0'],'ip','Onde a máscara tem 255 o octeto se repete; onde tem 0, vira 0.','7.4.1',ph='x.x.x.x'),
 inp('Use a operação AND para encontrar o endereço de rede de 192.168.5.130/26.',['192.168.5.128'],'ip','130 = 10000010 AND 11000000 = 10000000 = 128.','7.4.1',ph='x.x.x.x'),
 mc('Quando o AND entre dois bits resulta em 1?',['Somente quando os dois bits são 1','Quando pelo menos um bit é 1','Quando os bits são diferentes','Quando os dois bits são 0'],'O AND só é verdadeiro quando as duas entradas são verdadeiras.','7.4'),
 multi('Para 192.168.1.100/24, informe:',[F('Rede','192.168.1.0','ip'),F('Primeiro host','192.168.1.1','ip'),F('Último host','192.168.1.254','ip'),F('Broadcast','192.168.1.255','ip'),F('Hosts','254','num')],
    '8 bits de host → 2⁸ − 2 = 254 hosts.','7.5.1'),
 multi('Para 192.168.1.100/28, informe:',[F('Rede','192.168.1.96','ip'),F('Primeiro host','192.168.1.97','ip'),F('Último host','192.168.1.110','ip'),F('Broadcast','192.168.1.111','ip'),F('Hosts','14','num')],
    'Blocos de 16 (0, 16, ..., 96, 112); o 100 está no bloco de 96 a 111.','7.5.2'),
 multi('Para 10.0.0.50/29, informe:',[F('Rede','10.0.0.48','ip'),F('Primeiro host','10.0.0.49','ip'),F('Último host','10.0.0.54','ip'),F('Broadcast','10.0.0.55','ip'),F('Hosts','6','num')],
    'Blocos de 8; o 50 está no bloco de 48 a 55; 2³ − 2 = 6 hosts.','7.5.2'),
 multi('Para 172.16.10.65/27, informe:',[F('Rede','172.16.10.64','ip'),F('Primeiro host','172.16.10.65','ip'),F('Último host','172.16.10.94','ip'),F('Broadcast','172.16.10.95','ip'),F('Hosts','30','num')],
    'Blocos de 32; o 65 está no bloco de 64 a 95; 2⁵ − 2 = 30 hosts.','7.5.2'),
 mc('Qual comando do Windows mostra também o endereço MAC e os servidores DNS?',['ipconfig /all','ipconfig','arp -a','nslookup'],'O ipconfig simples mostra IP, máscara e gateway; o /all mostra também MAC, DNS e DHCP.','7.2.2'),
]
EX[8]=[
 inp('O PC1 (192.168.10.10/24) quer enviar dados para 192.168.10.20. Qual endereço IPv4 ele procura na tabela ARP?',['192.168.10.20'],'ip','O destino está na mesma rede, então ele procura o próprio destino.','8.1.2',ph='x.x.x.x'),
 mc('E se o destino for 8.8.8.8, qual endereço o PC1 procura na tabela ARP?',['O do gateway padrão','8.8.8.8','O do servidor DNS','FF-FF-FF-FF-FF-FF'],'Destino em outra rede → o quadro vai ao gateway, então ele procura o IPv4 do gateway.','8.1.2'),
 multi('Como cada mensagem ARP é enviada?',[C('Solicitação ARP',['Broadcast','Unicast'],'Broadcast'),C('Resposta ARP',['Broadcast','Unicast'],'Unicast')],
    'Na solicitação o host ainda não sabe o MAC; na resposta, o destino já sabe quem perguntou.','8.1.3'),
 inp('Qual é o valor do campo EtherType nas mensagens ARP?',['0x806','806','0806'],'hex','As mensagens ARP vão direto no quadro Ethernet, sem pacote IPv4.','8.1.3',ph='hex',d='0x806'),
 mc('Por que a solicitação ARP fica restrita à rede local?',['Porque o roteador não encaminha broadcasts','Porque o switch descarta broadcasts','Porque o ARP usa TCP','Porque o TTL do ARP é 1'],'Os roteadores não encaminham broadcasts entre suas interfaces.','8.1.3'),
 multi('Qual comando mostra a tabela ARP em cada dispositivo?',[F('PC com Windows',['arp -a','arp-a'],'txt',d='arp -a'),F('Roteador Cisco',['show ip arp'],'txt',d='show ip arp')],
    'Windows → arp -a; roteador Cisco → show ip arp.','8.1.5'),
 mc('O que caracteriza uma entrada ARP estática?',['É configurada manualmente e não expira','Expira entre 15 e 45 segundos','É criada por uma resposta ARP','Só existe no IPv6'],'Entradas estáticas só saem da tabela quando removidas por comando.','8.1.4'),
 mc('No envenenamento ARP, o que o atacante faz?',['Responde a uma solicitação ARP com o próprio MAC, fingindo ser outro dispositivo','Desliga o switch','Envia pings em excesso','Muda o endereço IP do gateway'],'O host grava o MAC errado e passa a enviar os pacotes ao atacante. A DAI protege contra isso.','8.2.2'),
 mc('No IPv6, qual recurso substitui o ARP?',['ND (Neighbor Discovery), com mensagens ICMPv6','DHCPv6','DNS','RSA'],'O IPv6 não usa ARP; a descoberta do MAC é feita pelo ND.','8.3'),
]
EX[9]=[
 mc('Qual protocolo da camada de transporte é orientado à conexão e garante a entrega?',['TCP','UDP','IP','ICMP'],'O TCP estabelece conexão e garante a entrega; o UDP é sem conexão e de melhor esforço.','9.2'),
 multi('Indique o serviço associado a cada porta.',[
    F('22','ssh','txt',d='SSH'),F('23','telnet','txt',d='Telnet'),F('25','smtp','txt',d='SMTP'),F('53','dns','txt',d='DNS'),
    F('80','http','txt',d='HTTP'),F('110',['pop3','pop'],'txt',d='POP3'),F('443','https','txt',d='HTTPS')],
    'Portas bem conhecidas: 22 SSH, 23 Telnet, 25 SMTP, 53 DNS, 80 HTTP, 110 POP3, 443 HTTPS.','9.3.3'),
 multi('Classifique cada porta.',[
    C('80',['Bem conhecida','Registrada','Dinâmica'],'Bem conhecida'),C('1812',['Bem conhecida','Registrada','Dinâmica'],'Registrada'),
    C('50000',['Bem conhecida','Registrada','Dinâmica'],'Dinâmica'),C('443',['Bem conhecida','Registrada','Dinâmica'],'Bem conhecida')],
    '0–1.023 bem conhecidas; 1.024–49.151 registradas; 49.152–65.535 dinâmicas.','9.3.2'),
 multi('Indique o protocolo preferido por cada aplicação.',[
    C('Transferência bancária',['TCP','UDP'],'TCP'),C('VoIP',['TCP','UDP'],'UDP'),C('Consulta DNS',['TCP','UDP'],'UDP'),
    C('Envio de e-mail',['TCP','UDP'],'TCP'),C('Vídeo ao vivo',['TCP','UDP'],'UDP')],
    'TCP quando tudo precisa chegar em ordem; UDP para tempo real e pedidos simples.','9.7'),
 inp('Escreva o par de sockets de um cliente 10.1.1.5, porta 49200, acessando um servidor HTTPS em 10.1.1.100.',['10.1.1.5:49200,10.1.1.100:443'],'ip','Socket = IP + porta; HTTPS usa a porta 443.','9.3.1',ph='ip:porta, ip:porta',d='10.1.1.5:49200, 10.1.1.100:443'),
 inp('Calcule o MSS de uma interface Ethernet com MTU de 1500 bytes usando IPv4 e TCP.',['1460'],'num','1500 − 20 (IPv4) − 20 (TCP) = 1460 bytes.','9.5.4',ph='bytes'),
 multi('Coloque em ordem as mensagens do handshake de três vias.',[
    C('1ª',['SYN','SYN-ACK','ACK'],'SYN'),C('2ª',['SYN','SYN-ACK','ACK'],'SYN-ACK'),C('3ª',['SYN','SYN-ACK','ACK'],'ACK')],
    'SYN → SYN-ACK → ACK abre as duas sessões da conexão full-duplex.','9.4.5'),
 inp('Quantas trocas são necessárias para encerrar uma sessão TCP?',['4'],'num','FIN, ACK, FIN, ACK: cada sentido é fechado com um FIN e um ACK.','9.4.6',ph='número'),
 mc('Na resposta do servidor, o que acontece com as portas da solicitação?',['São invertidas: a origem vira destino e vice-versa','Permanecem iguais','O servidor escolhe duas portas novas','A porta de origem vira 80'],'Na resposta, o servidor inverte as portas de origem e de destino.','9.4.4'),
 mc('O host A envia os segmentos 1 a 10 e se perdem o 3 e o 4. Com SACK, o que o host A reenvia?',['Apenas os segmentos 3 e 4','Do 3 ao 10','Todos os 10','Nada, o UDP cuida disso'],'Com a confirmação seletiva, o host B informa que recebeu 1, 2 e 5 a 10.','9.5.2'),
 mc('Qual é a diferença entre tamanho da janela e prevenção de congestionamento?',['A janela é definida pelo destino; no congestionamento, quem reduz o envio é a origem','Os dois são definidos pelo roteador','A janela é definida pela origem; o congestionamento, pelo destino','Não há diferença'],'É importante não confundir quem controla cada um.','9.5.5'),
 multi('Complete o comparativo dos cabeçalhos.',[F('Cabeçalho TCP (bytes)','20','num'),F('Cabeçalho UDP (bytes)','8','num')],'TCP: 20 bytes, 10 campos; UDP: 8 bytes, 4 campos.','9.8'),
]
REG=['A','AAAA','NS','MX']
EX[10]=[
 multi('Qual registro DNS faz cada função?',[
    C('Associa um nome a um endereço IPv6',REG,'AAAA'),C('Identifica o servidor de e-mail',REG,'MX'),
    C('Associa um nome a um endereço IPv4',REG,'A'),C('Indica o servidor autoritativo do domínio',REG,'NS')],
    'A → IPv4; AAAA → IPv6; NS → servidor autoritativo; MX → e-mail.','10.1.2'),
 multi('Coloque em ordem as etapas de uma consulta DNS.',[
    C('1ª',['Cache local','Servidor recursivo','Servidor raiz','Servidor TLD','Servidor autoritativo'],'Cache local'),
    C('2ª',['Cache local','Servidor recursivo','Servidor raiz','Servidor TLD','Servidor autoritativo'],'Servidor recursivo'),
    C('3ª',['Cache local','Servidor recursivo','Servidor raiz','Servidor TLD','Servidor autoritativo'],'Servidor raiz'),
    C('4ª',['Cache local','Servidor recursivo','Servidor raiz','Servidor TLD','Servidor autoritativo'],'Servidor TLD'),
    C('5ª',['Cache local','Servidor recursivo','Servidor raiz','Servidor TLD','Servidor autoritativo'],'Servidor autoritativo')],
    'Cache local → recursivo → raiz → TLD → autoritativo.','10.1.5'),
 mc('Em www.cisco.com.br, qual é o domínio de nível superior (TLD)?',['.br','.com','cisco','www'],'O TLD é a parte final do nome, depois do último ponto.','10.1.5'),
 inp('Qual comando do Windows mostra as entradas DNS em cache?',['ipconfig /displaydns','ipconfig/displaydns'],'txt','O ipconfig /displaydns lista os nomes já resolvidos.','10.1.3',ph='comando',d='ipconfig /displaydns'),
 mc('Qual utilitário permite consultar manualmente um servidor DNS?',['nslookup','netstat','tracert','arp -a'],'O nslookup ajuda a identificar problemas de resolução de nomes.','10.1.6'),
 multi('Escreva, em ordem, as quatro mensagens do DHCPv4.',[
    C('1ª',['DHCPDISCOVER','DHCPOFFER','DHCPREQUEST','DHCPACK'],'DHCPDISCOVER'),C('2ª',['DHCPDISCOVER','DHCPOFFER','DHCPREQUEST','DHCPACK'],'DHCPOFFER'),
    C('3ª',['DHCPDISCOVER','DHCPOFFER','DHCPREQUEST','DHCPACK'],'DHCPREQUEST'),C('4ª',['DHCPDISCOVER','DHCPOFFER','DHCPREQUEST','DHCPACK'],'DHCPACK')],
    'Processo DORA: Discover → Offer → Request → Ack.','10.2.4'),
 mc('Qual mensagem o servidor DHCP envia quando a oferta não é mais válida?',['DHCPNAK','DHCPRELEASE','DHCPDISCOVER','DHCPACK'],'Com o DHCPNAK, o cliente recomeça o processo.','10.2.4'),
 mc('Quais dispositivos normalmente recebem endereço estático?',['Roteadores, switches, servidores e impressoras','Celulares dos visitantes','Notebooks dos funcionários','Todos os dispositivos da rede'],'Dispositivos de rede precisam manter sempre o mesmo endereço.','10.2.1'),
 multi('Quais são os dois papéis DHCP de um roteador doméstico?',[
    C('Para a rede local',['Servidor DHCP','Cliente DHCP'],'Servidor DHCP'),C('Na interface WAN, ligada ao provedor',['Servidor DHCP','Cliente DHCP'],'Cliente DHCP')],
    'Ele distribui endereços na LAN e recebe um IPv4 público do provedor.','10.2.3'),
 mc('Qual informação o DHCPv6 não fornece?',['O gateway padrão, obtido pela mensagem RA','O endereço IPv6','O servidor DNS','O nome de domínio'],'No IPv6, o gateway vem do Anúncio de Roteador (RA).','10.2.5'),
 multi('Quais portas UDP o DHCP usa?',[F('Servidor','67','num'),F('Cliente','68','num')],'DHCP: UDP 67 (servidor) e 68 (cliente).','10.3'),
]
MODOS=['EXEC do usuário','EXEC privilegiado','Configuração global','Configuração de linha','Configuração de interface']
EX[11]=[
 mc('Qual tipo de acesso à CLI não depende da rede estar funcionando?',['Fora da banda, pela porta de console','Dentro da banda, por SSH','Dentro da banda, por Telnet','Por HTTP'],'O console (out-of-band) é usado na configuração inicial.','11.1'),
 multi('Identifique o modo de cada prompt.',[
    C('R1>',MODOS,'EXEC do usuário'),C('R1#',MODOS,'EXEC privilegiado'),C('R1(config)#',MODOS,'Configuração global'),
    C('R1(config-line)#',MODOS,'Configuração de linha'),C('R1(config-if)#',MODOS,'Configuração de interface')],
    'O prompt mostra o modo: > usuário, # privilegiado, (config)# configuração.','11.2.3'),
 multi('Qual comando faz cada mudança de modo?',[
    F('EXEC do usuário → EXEC privilegiado','enable','txt',d='enable'),F('EXEC privilegiado → configuração global',['configure terminal','conf t','config t','configure t'],'txt',d='configure terminal')],
    'enable e configure terminal.','11.2.4'),
 mc('Qual comando volta de qualquer modo de configuração direto para o EXEC privilegiado?',['end (ou Ctrl+Z)','exit','disable','enable'],'exit sobe um nível; end ou Ctrl+Z volta ao EXEC privilegiado.','11.2.4'),
 mc('Em "ping 192.168.10.5", o que é o endereço?',['Um argumento','Uma palavra-chave','Um modo','Um prompt'],'Argumento → valor definido pelo usuário; palavra-chave → parâmetro predefinido.','11.3'),
 mc('Por que "con" não funciona como abreviação de configure?',['Porque mais de um comando começa com essas letras','Porque abreviações não são permitidas','Porque o comando precisa de ?','Porque falta o argumento'],'A abreviação precisa identificar o comando de forma única, como conf.','11.3.3'),
 multi('Qual tecla ou combinação faz cada ação na CLI?',[
    C('Completar um comando',['Tab','Ctrl+Shift+6','Ctrl+A','Espaço'],'Tab'),
    C('Interromper um ping ou traceroute',['Tab','Ctrl+Shift+6','Ctrl+A','Espaço'],'Ctrl+Shift+6'),
    C('Levar o cursor ao início da linha',['Tab','Ctrl+Shift+6','Ctrl+A','Espaço'],'Ctrl+A'),
    C('Mostrar a próxima tela no --More--',['Tab','Ctrl+Shift+6','Ctrl+A','Espaço'],'Espaço')],
    'Tab completa; Ctrl+Shift+6 interrompe; Ctrl+A vai ao início; Espaço mostra a próxima tela.','11.3.4'),
 mc('Qual comando mostra as informações de roteamento?',['show ip route','show interfaces','show version','show running-config'],'show ip route → tabela de roteamento.','11.4'),
 mc('Qual comando mostra a memória, as interfaces e as licenças do dispositivo?',['show version','show protocols','show arp','show ip interface'],'show version → hardware e licenças.','11.4'),
]
EX[12]=[
 mc('Qual é a diferença entre running-config e startup-config?',['A running-config está em uso na RAM e se perde ao desligar; a startup-config fica salva na NVRAM','A running-config fica na NVRAM; a startup-config na RAM','As duas ficam na RAM','A startup-config é perdida ao desligar'],'Depois de cada alteração, salva-se com copy running-config startup-config.','12.1.3'),
 inp('Qual comando salva a configuração em uso?',['copy running-config startup-config','copy run start','wr','write memory'],'txt','O comando copia a running-config (RAM) para a startup-config (NVRAM).','12.1.3',ph='comando',d='copy running-config startup-config'),
 mc('Por que o Telnet não é recomendado para o acesso remoto?',['Porque envia o usuário e a senha em texto simples','Porque não funciona em switches','Porque usa a porta 22','Porque exige chaves RSA'],'O SSH criptografa essas informações e é o método recomendado.','12.1.2'),
 multi('Escreva os comandos para dar ao switch S1 o endereço de gerenciamento 192.168.1.2/24 e o gateway 192.168.1.1.',[
    F('Entrar na SVI',['interface vlan 1','int vlan 1','int vlan1','interface vlan1'],'txt',d='interface vlan 1'),
    F('Definir endereço e máscara',['ip address 192.168.1.2 255.255.255.0','ip add 192.168.1.2 255.255.255.0'],'txt',d='ip address 192.168.1.2 255.255.255.0'),
    F('Ativar a interface',['no shutdown','no shut'],'txt',d='no shutdown'),
    F('Definir o gateway (configuração global)',['ip default-gateway 192.168.1.1'],'txt',d='ip default-gateway 192.168.1.1')],
    'interface vlan 1 → ip address → no shutdown → exit → ip default-gateway.','12.2.2'),
 mc('Por que um switch de camada 2 precisa de gateway padrão?',['Para responder a um administrador que o acessa a partir de outra rede','Para encaminhar quadros entre portas','Para criar a tabela MAC','Para gerar as chaves RSA'],'Sem gateway, a resposta do switch não sai da rede local.','12.5.2'),
 mc('Por que o comando no shutdown é obrigatório nas interfaces do roteador?',['Porque elas ficam desativadas por padrão','Porque ele salva a configuração','Porque ele define o endereço IP','Porque ele ativa o SSH'],'As interfaces do roteador começam desligadas.','12.3.3'),
 multi('Coloque em ordem as etapas para ativar o SSH.',[
    C('1ª',['Configurar o domínio IP','Gerar as chaves RSA','Criar o usuário local','Configurar as linhas VTY','Ativar a versão 2'],'Configurar o domínio IP'),
    C('2ª',['Configurar o domínio IP','Gerar as chaves RSA','Criar o usuário local','Configurar as linhas VTY','Ativar a versão 2'],'Gerar as chaves RSA'),
    C('3ª',['Configurar o domínio IP','Gerar as chaves RSA','Criar o usuário local','Configurar as linhas VTY','Ativar a versão 2'],'Criar o usuário local'),
    C('4ª',['Configurar o domínio IP','Gerar as chaves RSA','Criar o usuário local','Configurar as linhas VTY','Ativar a versão 2'],'Configurar as linhas VTY'),
    C('5ª',['Configurar o domínio IP','Gerar as chaves RSA','Criar o usuário local','Configurar as linhas VTY','Ativar a versão 2'],'Ativar a versão 2')],
    'ip domain-name → crypto key generate rsa → username ... secret → line vty (transport input ssh, login local) → ip ssh version 2.','12.4.3'),
 mc('Qual comando nas linhas VTY aceita somente SSH, bloqueando o Telnet?',['transport input ssh','login local','ip ssh version 2','service password-encryption'],'transport input ssh aceita só SSH; login local autentica com o usuário local.','12.4.3'),
 multi('Quantas linhas VTY costumam ter os equipamentos Cisco?',[F('Switch','16','num'),F('Roteador','5','num')],'Switches: 0 a 15; roteadores: 0 a 4.','12.4.2'),
 mc('Qual senha é considerada forte?',['b67n42d39c','bob1967','toyota','Blueleaf23'],'Mistura de letras e números, sem palavras ou datas.','12.4.1'),
 mc('Que tipo de criptografia as chaves RSA usam?',['Assimétrica: chave pública e chave privada','Simétrica: a mesma chave nos dois lados','Nenhuma; o RSA só autentica','Hash, como o enable secret'],'O SSH usa RSA para autenticar e combinar a chave de sessão, e criptografia simétrica para os dados.','12.4.3'),
]
EX[13]=[
 mc('O ping para 127.0.0.1 funciona, mas o ping para o gateway padrão falha. O que isso indica?',['O TCP/IP funciona no host, mas há um problema na rede local','O TCP/IP não está instalado no host','O problema está no servidor remoto','O DNS está fora do ar'],'Pode ser gateway errado, cabo ou placa com defeito, interface do roteador ou bloqueio ao ping.','13.3.1'),
 multi('Coloque os testes de ping na ordem correta.',[
    C('1º',['Loopback','Gateway padrão','Host remoto'],'Loopback'),C('2º',['Loopback','Gateway padrão','Host remoto'],'Gateway padrão'),C('3º',['Loopback','Gateway padrão','Host remoto'],'Host remoto')],
    'Do mais próximo para o mais distante.','13.3.1'),
 multi('Qual é o endereço de loopback?',[F('IPv4','127.0.0.1','ip'),F('IPv6','::1','v6')],'127.0.0.1 e ::1 testam o IP no próprio host.','13.3.1'),
 mc('Quais mensagens ICMP o ping usa?',['Solicitação e resposta de eco','Tempo excedido','RS e RA','NS e NA'],'Echo Request e Echo Reply.','13.1.1'),
 mc('Por que é comum o primeiro ping falhar?',['Porque o host ainda precisa descobrir o MAC do destino (ARP ou ND)','Porque o TTL começa em zero','Porque o roteador está desligado','Porque o ping usa TCP'],'Depois que o MAC é descoberto, os pings seguintes funcionam.','13.3'),
 mc('Como o traceroute descobre cada roteador do caminho?',['Envia pacotes com TTL 1, 2, 3...; cada roteador que zera o TTL responde com "tempo excedido"','Pede a tabela de roteamento a cada roteador','Envia um broadcast para todos os roteadores','Usa respostas de eco de cada roteador'],'O destino final responde com "porta inalcançável" ou com eco.','13.4.2'),
 mc('O que significa um asterisco (*) na saída do traceroute?',['Um pacote perdido ou sem resposta naquele salto','O destino foi alcançado','O roteador é o gateway padrão','Um erro de digitação'],'Tempos altos ou perdas indicam que aquele salto pode estar sobrecarregado.','13.4.1'),
 multi('Qual mensagem do ICMPv6 cada um envia?',[
    C('Dispositivo pede informações ao roteador',['RS','RA','NS','NA'],'RS'),C('Roteador informa prefixo, gateway e DNS',['RS','RA','NS','NA'],'RA'),
    C('Dispositivo pergunta o MAC de um IPv6',['RS','RA','NS','NA'],'NS'),C('Dispositivo responde com o seu MAC',['RS','RA','NS','NA'],'NA')],
    'RS/RA entre dispositivo e roteador; NS/NA entre dispositivos.','13.2'),
 mc('No DAD, o dispositivo envia uma NS para o próprio endereço e alguém responde com uma NA. O que isso significa?',['O endereço já está em uso','O endereço é exclusivo','O roteador está fora do ar','O MAC foi descoberto'],'Se ninguém responder, o endereço é exclusivo.','13.2.2'),
 multi('Qual é o código de destino inalcançável no ICMPv4?',[
    C('Rede inalcançável',['0','1','2','3'],'0'),C('Host inalcançável',['0','1','2','3'],'1'),C('Porta inalcançável',['0','1','2','3'],'3')],
    'ICMPv4: 0 rede, 1 host, 2 protocolo, 3 porta.','13.1.2'),
 mc('No Windows, qual é o comando do traceroute?',['tracert','traceroute','trace','ping -t'],'No Cisco IOS e no Linux, é traceroute.','13.5'),
]
