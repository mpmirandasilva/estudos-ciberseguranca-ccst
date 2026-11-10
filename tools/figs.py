# Figuras em SVG com os tokens do site (classes .fg-*). Mesmo traço, mesma tipografia, tema claro/escuro.
from html import escape as E
W=640
def svg(h,body,label):
    return (f'<svg class="fg" viewBox="0 0 {W} {h}" role="img" aria-label="{E(label)}" '
            f'xmlns="http://www.w3.org/2000/svg">{body}</svg>')
def box(x,y,w,h,txt='',c='',sub=None,bold=True,fs=14):
    s=f'<rect class="fg-sh" x="{x+3}" y="{y+3}" width="{w}" height="{h}"/>'
    s+=f'<rect class="fg-bx {c}" x="{x}" y="{y}" width="{w}" height="{h}"/>'
    lines=txt.split('\n') if txt else []
    subs=sub.split('\n') if sub else []
    n=len(lines)+len(subs)
    cy=y+h/2-(n-1)*8.5
    for i,l in enumerate(lines):
        s+=f'<text x="{x+w/2}" y="{cy+i*17+5}" text-anchor="middle" class="{"fg-h" if bold else ""}" style="font-size:{fs}px">{E(l)}</text>'
    for k,l in enumerate(subs):
        s+=f'<text x="{x+w/2}" y="{cy+(len(lines)+k)*17+4}" text-anchor="middle" class="fg-s">{E(l)}</text>'
    return s
def line(x1,y1,x2,y2,c='',dash=False):
    return f'<line class="fg-ln {c}{" d" if dash else ""}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>'
def arrow(x1,y1,x2,y2,c='',dash=False):
    import math
    a=math.atan2(y2-y1,x2-x1); L=10; w=5.5
    bx,by=x2-L*math.cos(a),y2-L*math.sin(a)
    p=[(x2,y2),(bx+w*math.sin(a),by-w*math.cos(a)),(bx-w*math.sin(a),by+w*math.cos(a))]
    pts=' '.join(f'{px:.1f},{py:.1f}' for px,py in p)
    return line(x1,y1,bx,by,c,dash)+f'<polygon class="fg-ah {c}" points="{pts}"/>'
def text(x,y,t,cls='',anchor='middle',fs=None):
    st=f' style="font-size:{fs}px"' if fs else ''
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}"{st}>{E(t)}</text>'

def seq(actors,msgs,label,gap=58,notes=None,aw=148):
    """actors: [(nome, x, classe)], msgs: [(i,j,rotulo,sub,resposta?)]"""
    top=14; bh=46; y0=top+bh+40
    h=y0+gap*(len(msgs)-1)+44+(52 if notes else 0)
    s=''
    yl=h-(58 if notes else 14)
    for name,x,c in actors:
        s+=line(x,top+bh,x,yl,'fg-life')
    for name,x,c in actors:
        s+=box(x-aw/2,top,aw,bh,name,c)
    for k,(i,j,lab,sub,resp) in enumerate(msgs):
        y=y0+gap*k; x1=actors[i][1]; x2=actors[j][1]; d=8 if x2>x1 else -8
        s+=arrow(x1+d,y,x2-d,y,'t' if resp else '',dash=resp)
        mx=(x1+x2)/2
        s+=text(mx,y-9,lab,'fg-h')
        if sub: s+=text(mx,y+19,sub,'fg-s')
    if notes:
        yb=h-46
        for x,t in notes:
            w=max(120,len(t)*7+24); x0=max(8,min(W-8-w,x-w/2))
            s+=f'<rect class="fg-bx c4" x="{x0}" y="{yb}" width="{w}" height="32"/>'+text(x0+w/2,yb+21,t,'',fs=12.5)
    return svg(h,s,label)

def hierarquia():
    s=''
    rows=[('Núcleo',70,'c2'),('Distribuição',170,'c3'),('Acesso',270,'c1')]
    for t,y,c in rows: s+=text(18,y+5,t,'fg-h','start',fs=14)
    core=[285,475]; dist=[235,525]; acc=[150,287,424,561]
    for a in core:
        for b in dist: s+=line(a,70,b,170,'fg-mu')
    for a in dist:
        for b in acc: s+=line(a,170,b,270,'fg-mu')
    s+=line(300,70,500,70,'fg-mu'); s+=line(270,170,530,170,'fg-mu')
    for x in core: s+=box(x-62,52,124,36,'Switch de núcleo','c2',fs=13)
    for x in dist: s+=box(x-70,150,140,40,'Switch L3 ou roteador','c3',fs=12.5)
    devs=['PCs','Telefones IP','Impressoras','Pontos de acesso']
    for x,dv in zip(acc,devs):
        s+=box(x-58,252,116,36,'Switch de acesso','c1',fs=12.5)
        s+=line(x,288,x,330,'fg-mu')
        s+=box(x-58,330,116,32,dv,'c4',bold=False,fs=12.5)
    s+=text(18,351,'Usuários','fg-s','start')
    return svg(376,s,'Modelo hierárquico com camadas de núcleo, distribuição e acesso')

def encapsulamento():
    rows=[('Aplicação',[('Dados','c3',124)],'Dados'),
          ('Transporte',[('Cab. TCP/UDP','c1',98),('Dados','c3',124)],'Segmento'),
          ('Internet',[('Cab. IP','c2',64),('Cab. TCP/UDP','c1',98),('Dados','c3',124)],'Pacote'),
          ('Acesso à rede',[('Cab. Ethernet','c4',94),('Cab. IP','c2',64),('Cab. TCP/UDP','c1',98),('Dados','c3',124),('FCS','c4',40)],'Quadro')]
    s=''; right=508; y=18
    for name,parts,pdu in rows:
        s+=text(14,y+22,name,'fg-h','start',fs=13.5)
        total=sum(p[2] for p in parts)
        # alinha "Dados" na mesma coluna: a soma até Dados termina em right (exceto FCS)
        dados_end=right
        x=dados_end-sum(p[2] for p in parts if p[0]!='FCS')
        for t,c,w in parts:
            s+=f'<rect class="fg-bx {c}" x="{x}" y="{y}" width="{w}" height="34"/>'+text(x+w/2,y+22,t,'',fs=12.5)
            x+=w
        s+=text(560,y+22,pdu,'fg-k','start',fs=13)
        y+=50
    s+=text(14,y+22,'Física','fg-h','start',fs=13.5)
    s+=f'<rect class="fg-bx c4" x="124" y="{y}" width="424" height="34"/>'+text(336,y+22,'0 1 1 0 1 0 0 1 0 1 1 1 0 0 1 0 1 0 1 1','fg-m',fs=12.5)
    s+=text(560,y+22,'Bits','fg-k','start',fs=13)
    # seta de encapsulamento
    s+=arrow(622,26,622,y+28,'t');
    return svg(y+52,s,'Encapsulamento dos dados em cada camada do modelo TCP/IP')

def caminho_roteador():
    s=''
    s+=box(14,30,150,66,'PC A','c1',sub='192.168.1.10\nMAC AA')
    s+=box(236,30,168,66,'Roteador','c2',sub='G0/0: 192.168.1.1 (MAC R1)\nG0/1: 192.168.2.1 (MAC R2)')
    s+=box(476,30,150,66,'Servidor','c1',sub='192.168.2.50\nMAC BB')
    s+=arrow(167,63,232,63); s+=arrow(407,63,472,63)
    s+=text(200,20,'rede 192.168.1.0/24','fg-s'); s+=text(440,20,'rede 192.168.2.0/24','fg-s')
    def quadro(x,t,vals):
        r=text(x+105,128,t,'fg-h',fs=13.5)
        labs=['MAC origem','MAC destino','IP origem','IP destino']
        for i,(l,v) in enumerate(zip(labs,vals)):
            y=140+i*34; c='c2' if i<2 else 'c1'
            r+=f'<rect class="fg-bx {c}" x="{x}" y="{y}" width="96" height="28"/>'+text(x+48,y+18,l,'',fs=12)
            r+=f'<rect class="fg-bx {c}" x="{x+102}" y="{y}" width="108" height="28"/>'+text(x+156,y+18,v,'fg-h fg-m',fs=12)
        return r
    s+=quadro(40,'Quadro no trecho 1',['AA (PC A)','R1 (roteador)','192.168.1.10','192.168.2.50'])
    s+=quadro(390,'Quadro no trecho 2',['R2 (roteador)','BB (servidor)','192.168.1.10','192.168.2.50'])
    s+=text(320,296,'MAC muda a cada rede · IP permanece até o destino','fg-s')
    return svg(310,s,'Caminho de um pacote entre duas redes: os endereços MAC mudam e os IP permanecem')

# glifos 12x12 no estilo dos ícones do site: # tinta, + destaque
G={
'Roteador':["............","............","..########..",".#..+..+..#.","#..+++++...#","#...+..+...#","#..+++++...#",".#..+..+..#.","..########..","............","............","............"],
'Roteador sem fio':["..#......#..","..#......#..","..#......#..","..########..",".#..+..+..#.","#..+++++...#","#...+..+...#","#..+++++...#",".#..+..+..#.","..########..","............","............"],
'Switch':["............","............","............","############","#..........#","#.+.+.+.+.+#","#..........#","############","............","............","............","............"],
'Ponto de acesso':["....####....","...#....#...","..#..##..#..","....#..#....",".....##.....","............",".##########.","#..........#","#.++....++.#",".##########.","............","............"],
'Firewall':["############","#+++#+++#++#","############","#++#+++#+++#","############","#+++#+++#++#","############","#++#+++#+++#","############","............","............","............"],
'Internet':["............","....####....","...#++++#...","..#++++++#..",".##++++++##.","#++++++++++#","#++++++++++#",".##########.","............","............","............","............"],
'Computador':["############","#++++++++++#","#++++++++++#","#++++++++++#","#++++++++++#","############",".....##.....",".....##.....","...######...","............","............","............"],
'Notebook':["............","..########..","..#++++++#..","..#++++++#..","..#++++++#..","..########..",".##########.","############","............","............","............","............"],
'Servidor':["..########..","..#......#..","..#.+..++#..","..########..","..#......#..","..#.+..++#..","..########..","..#......#..","..#.+..++#..","..########..","............","............"],
'Smartphone':["...######...","...#++++#...","...#++++#...","...#++++#...","...#++++#...","...#++++#...","...#++++#...","...#....#...","...#.##.#...","...######...","............","............"],
'Impressora':["...######...","...#....#...","############","#..........#","#........+.#","#..........#","############","...#....#...","...######...","............","............","............"],
'Telefone IP':[".##########.","#..........#","##########.#","#.+.+.+..#.#","#.+.+.+..#.#","#.+.+.+..#.#","##########.#","............","............","............","............","............"],
}
def glyph(name,x,y,sc=3):
    r=''
    for j,row in enumerate(G[name]):
        for i,ch in enumerate(row):
            if ch=='#': r+=f'<rect class="fg-ink" x="{x+i*sc}" y="{y+j*sc}" width="{sc}" height="{sc}"/>'
            elif ch=='+': r+=f'<rect class="fg-acc" x="{x+i*sc}" y="{y+j*sc}" width="{sc}" height="{sc}"/>'
    return r
def simbolos():
    s=''
    groups=[('Dispositivos intermediários',['Roteador','Roteador sem fio','Switch','Ponto de acesso','Firewall','Internet']),
            ('Dispositivos finais',['Computador','Notebook','Servidor','Smartphone','Impressora','Telefone IP'])]
    y=10
    for g,items in groups:
        s+=text(14,y+16,g.upper(),'fg-k','start',fs=12.5)
        for k,it in enumerate(items):
            cx=60+k*104
            s+=f'<rect class="fg-bx c4" x="{cx-40}" y="{y+28}" width="80" height="62"/>'
            s+=glyph(it,cx-18,y+40)
            s+=text(cx,y+108,it,'',fs=12.5)
        y+=128
    s+=text(14,y+16,'CONEXÕES','fg-k','start',fs=12.5)
    s+=line(20,y+40,90,y+40)+text(100,y+44,'Cabo (Ethernet)','','start',fs=12.5)
    s+=line(240,y+40,310,y+40,'t',dash=True)+text(320,y+44,'Sem fio','','start',fs=12.5)
    s+=f'<polyline class="fg-ln a" points="430,{y+40} 456,{y+40} 468,{y+30} 480,{y+50} 492,{y+40} 520,{y+40}"/>'+text(530,y+44,'WAN (serial)','','start',fs=12.5)
    return svg(y+60,s,'Símbolos usados nos diagramas de rede')

def arp():
    return seq([('PC A\n192.168.1.10',105,'c1'),('PC B\n192.168.1.20',325,'c3'),('PC C\n192.168.1.30',540,'c4')],
       [(0,2,'Solicitação ARP · broadcast','MAC destino FF-FF-FF-FF-FF-FF · "quem tem 192.168.1.20?"',False),
        (1,0,'Resposta ARP · unicast','"o MAC de 192.168.1.20 é 00-1A-2B-3C-4D-5E"',True)],
       'Solicitação ARP em broadcast e resposta ARP em unicast',gap=78,
       notes=[(118,'PC A grava IP → MAC na tabela ARP'),(528,'PC C descarta: não é o seu IP')])

def dora():
    return seq([('Cliente DHCP',130,'c1'),('Servidor DHCP',510,'c2')],
      [(0,1,'1. DHCPDISCOVER','broadcast: procura um servidor DHCP',False),
       (1,0,'2. DHCPOFFER','oferece IP, máscara, gateway, DNS e concessão',True),
       (0,1,'3. DHCPREQUEST','aceita a oferta escolhida',False),
       (1,0,'4. DHCPACK','confirma a concessão',True)],'Processo DORA entre o cliente e o servidor DHCP')
def handshake():
    return seq([('Cliente',130,'c1'),('Servidor',510,'c2')],
      [(0,1,'1. SYN','pede a sessão cliente → servidor',False),
       (1,0,'2. SYN-ACK','confirma e pede a sessão servidor → cliente',True),
       (0,1,'3. ACK','confirma: conexão estabelecida',False)],'Handshake de três vias do TCP')
def traceroute():
    return seq([('PC',70,'c1'),('R1',235,'c3'),('R2',400,'c3'),('Servidor',566,'c2')],
      [(0,1,'TTL = 1','',False),(1,0,'tempo excedido','o PC descobre o 1º salto (R1)',True),
       (0,2,'TTL = 2','',False),(2,0,'tempo excedido','o PC descobre o 2º salto (R2)',True),
       (0,3,'TTL = 3','',False),(3,0,'porta inalcançável / eco','destino alcançado: fim do rastreamento',True)],
      'Funcionamento do traceroute com o aumento do TTL',gap=64,aw=118)

FIGS={'simbolos':simbolos,'encapsulamento':encapsulamento,'hierarquico':hierarquia,'dora':dora,
      'caminho':caminho_roteador,'arp':arp,'handshake':handshake,'traceroute':traceroute}

# ---------- Trilha 4: Defesa de Rede ----------
def chain(items,label,y=20,h=56,gap=30,sub=None):
    n=len(items); w=(W-16-gap*(n-1))/n; s=''
    for i,(t,c) in enumerate(items):
        x=8+i*(w+gap)
        s+=box(x,y,w,h,t,c,sub=(sub[i] if sub else None),fs=13)
        if i<n-1: s+=arrow(x+w+2,y+h/2,x+w+gap-3,y+h/2)
    return s
def def_camadas():
    s=chain([('Internet','c4'),('Roteador\nde borda','c3'),('Firewall','c2'),('Roteador\ninterno','c3'),('Rede interna\n(LAN)','c1')],'',y=20,h=60,gap=26)
    labs=['não confiável','1ª linha','2ª linha','3ª linha','confiável']
    n=5; gap=26; w=(W-16-gap*4)/5
    for i,l in enumerate(labs): s+=text(8+i*(w+gap)+w/2,104,l,'fg-s')
    return svg(118,s,'Três linhas de defesa entre a internet e a rede interna')
def def_cripto():
    s=chain([('Texto claro','c1'),('Criptografia','c3'),('Texto cifrado','c2'),('Descripto-\ngrafia','c3'),('Texto claro','c1')],'',y=20,h=50,gap=24)
    w=(W-16-24*4)/5
    for i in (1,3):
        cx=8+i*(w+24)+w/2
        s+=arrow(cx,108,cx,74,'t')
        s+=text(cx,124,'chave','fg-k')
    s+=text(8+2*(w+24)+w/2,100,'ilegível sem a chave','fg-s')
    return svg(136,s,'Criptografia e descriptografia com chave')
def def_assim():
    s=''
    s+=text(10,22,'Confidencialidade','fg-h','start',fs=14)
    s+=chain([('Alice','c1'),('cifra com a\npública de Bob','c3'),('decifra com a\nprivada de Bob','c2'),('Bob','c1')],'',y=34,h=50,gap=26)
    s+=text(10,120,'Autenticação','fg-h','start',fs=14)
    s+=chain([('Alice','c1'),('cifra com a\nprivada de Alice','c2'),('decifra com a\npública de Alice','c3'),('Bob','c1')],'',y=132,h=50,gap=26)
    s+=text(320,208,'só Bob lê  ·  só Alice poderia ter enviado','fg-s')
    return svg(220,s,'Uso das chaves pública e privada para confidencialidade e para autenticação')
def def_assinatura():
    s=text(10,22,'Assinar (Bob)','fg-h','start',fs=14)
    s+=chain([('Documento','c1'),('Hash','c3'),('Cifra com a\nprivada de Bob','c2'),('Assinatura','c4')],'',y=32,h=50,gap=26)
    s+=text(10,118,'Verificar (Alice)','fg-h','start',fs=14)
    s+=chain([('Assinatura','c4'),('Decifra com a\npública de Bob','c3'),('Hash enviado','c3')],'',y=128,h=50,gap=26)
    s+=chain([('Documento','c1'),('Hash calculado','c3')],'',y=200,h=44,gap=26)
    s+=box(8,262,W-16,40,'Hashes iguais → veio de Bob e não foi alterado','c1',fs=13)
    return svg(312,s,'Criação e verificação de uma assinatura digital')
def def_pki():
    s=box(210,14,220,54,'CA','c2',sub='autoridade de certificação')
    s+=box(20,200,170,54,'Bob','c1',sub='titular')
    s+=box(450,200,170,54,'Alice','c1',sub='quem confere')
    s+=arrow(70,198,226,72); s+=text(30,128,'1. pede o','fg-s','start'); s+=text(30,144,'certificado','fg-s','start')
    s+=arrow(270,72,140,196,'t'); s+=text(214,150,'2. confirma a identidade','fg-s','start'); s+=text(214,166,'e emite','fg-s','start')
    s+=arrow(194,227,446,227); s+=text(320,218,'3. apresenta o certificado','fg-s')
    s+=arrow(570,198,414,72,'t',dash=True); s+=text(610,128,'4. confere com a','fg-s','end'); s+=text(610,144,'pública da CA','fg-s','end')
    return svg(266,s,'Emissão e verificação de um certificado digital na PKI')
def def_dmz():
    s=box(250,94,140,54,'Firewall','c2',sub='três interfaces')
    s+=box(8,94,170,54,'Internet','c4',sub='não confiável')
    s+=box(462,94,170,54,'LAN privada','c1',sub='confiável')
    s+=box(235,212,170,54,'DMZ','c3',sub='servidores web e e-mail')
    s+=line(178,121,250,121); s+=line(390,121,462,121); s+=line(320,148,320,212)
    s+=text(214,82,'pública → LAN: bloqueado','fg-s'); s+=text(426,82,'LAN → fora: inspecionado','fg-s')
    s+=text(470,236,'DMZ → LAN: bloqueado','fg-s','start'); s+=text(170,236,'pública → DMZ:','fg-s','end'); s+=text(170,252,'permitido seletivamente','fg-s','end')
    return svg(278,s,'Firewall com DMZ entre a internet e a rede privada')
def def_acl():
    s=box(220,10,200,40,'Pacote chega','c4',fs=13)
    s+=arrow(320,50,320,72)
    s+=box(170,72,300,44,'Compara com a próxima ACE','c3',fs=13)
    s+=arrow(320,116,320,138)
    s+=box(200,138,240,44,'Corresponde?','c2',fs=13)
    s+=arrow(440,160,500,160); s+=text(470,152,'sim','fg-k')
    s+=box(500,138,132,44,'permit / deny','c1',fs=13)
    s+=arrow(320,182,320,206); s+=text(334,198,'não','fg-k','start')
    s+=box(185,206,270,44,'Há mais ACEs na lista?','c2',fs=13)
    s+=line(185,228,120,228); s+=line(120,228,120,94); s+=arrow(120,94,168,94); s+=text(132,220,'sim','fg-k','start')
    s+=arrow(320,250,320,274); s+=text(334,266,'não','fg-k','start')
    s+=box(180,274,280,44,'Negação implícita: descarta','c4',fs=13)
    return svg(330,s,'Processamento de um pacote por uma ACL, de cima para baixo')
def def_https():
    return seq([('Navegador',130,'c1'),('Servidor',510,'c2')],
      [(0,1,'1. pede a página https://','',False),
       (1,0,'2. chave pública + certificado','',True),
       (0,0,'',"",False)][:2]+[
       (0,1,'3. confere o certificado e envia a chave simétrica','cifrada com a chave pública do servidor',False),
       (1,0,'4. página cifrada com a chave simétrica','o navegador decifra e mostra',True)],
      'Estabelecimento de uma conexão HTTPS',gap=64)
def def_kerberos():
    return seq([('Cliente',100,'c1'),('Servidor Kerberos',320,'c2'),('Serviço',540,'c3')],
      [(0,1,'1. autentica-se','',False),(1,0,'2. recebe o TGT','tíquete de concessão de tíquete',True),
       (0,1,'3. apresenta o TGT','e pede um serviço',False),(1,0,'4. tíquete de serviço','com carimbo de hora e validade',True),
       (0,2,'5. apresenta o tíquete e acessa','',False)],'Autenticação com tíquetes no Kerberos',gap=60,aw=150)
FIGS.update({'def_camadas':def_camadas,'def_cripto':def_cripto,'def_assim':def_assim,'def_assinatura':def_assinatura,'def_pki':def_pki,'def_dmz':def_dmz,'def_acl':def_acl,'def_https':def_https,'def_kerberos':def_kerberos})

# ---------- Trilha 3: Segurança de Endpoint ----------
def end_ddos():
    s=box(240,10,160,44,'Atacante','c2',fs=13)
    for x in (110,410): s+=box(x,90,120,40,'Manipulador','c3',fs=12.5); 
    for x in (170,470): s+=arrow(320,54,x,88)
    zs=[30,150,270,390,510]
    for i,x in enumerate(zs):
        s+=box(x,168,100,38,'Zumbi','c4',fs=12.5)
        src=170 if i<3 else 470
        s+=arrow(src,130,x+50,166,dash=True)
        s+=arrow(x+50,206,320,250,'t')
    s+=box(240,252,160,44,'Alvo','c1',fs=13)
    s+=text(320,318,'milhares de pedidos ao mesmo tempo: o serviço cai','fg-s')
    return svg(330,s,'Ataque DDoS com botnet: atacante, manipuladores, zumbis e alvo')
def end_smurf():
    s=box(20,20,150,48,'Atacante','c2',fs=13)
    s+=box(20,200,150,48,'Vítima','c1',fs=13)
    for k,y in enumerate((14,84,154,224)):
        s+=box(440,y,170,40,'Host','c4',fs=12.5)
        s+=arrow(172,44,436,y+20)
        s+=arrow(438,y+20,174,224,'t',dash=True)
    s+=text(20,96,'1. eco ICMP com o IP','fg-s','start'); s+=text(20,112,'da vítima como origem','fg-s','start')
    s+=text(20,272,'2. todas as respostas vão à vítima','fg-s','start')
    return svg(286,s,'Ataque Smurf: amplificação e reflexão')
def end_synflood():
    return seq([('Atacante (IPs falsos)',140,'c2'),('Servidor',500,'c1')],
      [(0,1,'SYN','origem 10.9.9.1 (falsa)',False),(1,0,'SYN-ACK','vai para um endereço que não responde',True),
       (0,1,'SYN','origem 10.9.9.2 (falsa)',False),(0,1,'SYN, SYN, SYN...','',False)],
      'Inundação SYN',gap=58,aw=190,notes=[(500,'conexões semiabertas lotam a tabela'),(140,'o ACK nunca é enviado')])
def end_arp():
    s=box(20,30,150,50,'PC-A','c1',sub='192.168.10.10'); s+=box(470,30,150,50,'R1 (gateway)','c3',sub='192.168.10.1')
    s+=box(245,190,150,50,'Atacante','c2',sub='MAC EE:EE…')
    s+=line(170,55,470,55,'',dash=True); s+=text(320,46,'caminho normal','fg-s')
    s+=arrow(250,188,130,84,'t'); s+=text(80,150,'"o MAC de .1','fg-s','start'); s+=text(80,166,'é EE:EE…"','fg-s','start')
    s+=arrow(390,188,510,84,'t'); s+=text(560,150,'"o MAC de .10','fg-s','end'); s+=text(560,166,'é EE:EE…"','fg-s','end')
    s+=text(320,270,'todo o tráfego entre PC-A e R1 passa pelo atacante (MitM)','fg-s')
    return svg(284,s,'Envenenamento do cache ARP com respostas gratuitas falsas')
def end_dhcp():
    return seq([('Cliente',100,'c1'),('Servidor falso',320,'c2'),('Servidor legítimo',540,'c3')],
      [(0,2,'1. DHCPDISCOVER (broadcast)','chega aos dois servidores',False),
       (1,0,'2. oferta falsa chega primeiro','gateway e DNS do atacante',True),
       (0,1,'3. DHCPREQUEST','aceita a primeira oferta',False),
       (1,0,'4. DHCPACK','o cliente passa a usar o atacante como gateway',True)],
      'Falsificação de DHCP',gap=62,aw=160)
def end_dnstunnel():
    s=chain([('Host\ninfectado','c2'),('DNS local','c4'),('DNS recursivo\ndo provedor','c3'),('DNS autoritativo\ndo atacante','c2')],'',y=20,h=56,gap=28)
    s+=text(320,104,'dados roubados viajam como subdomínios: dGVzdGU.exemplo-mal.com','fg-m',fs=12)
    s+=text(320,126,'as respostas (registros TXT) trazem comandos de volta ao malware','fg-s')
    return svg(140,s,'Tunelamento DNS: dados e comandos escondidos em consultas DNS')
def end_wincamadas():
    rows=[('Aplicativos','c1','modo usuário'),('API do Windows e drivers de modo usuário','c1','modo usuário'),('Kernel, drivers de modo kernel e sistema de arquivos','c3','modo kernel'),('HAL (camada de abstração de hardware)','c3','modo kernel'),('Hardware','c4','')]
    s=''; y=10
    for t,c,m in rows:
        s+=box(20,y,470,40,t,c,fs=13)
        if m: s+=text(510,y+25,m,'fg-k','start')
        y+=50
    return svg(y+4,s,'Camadas da arquitetura do Windows')
def end_boot():
    s=chain([('BIOS/UEFI','c4'),('Bootmgr','c3'),('Winload','c3'),('Ntoskrnl','c2'),('SMSS → Logon','c1')],'',y=20,h=50,gap=24)
    s+=text(320,96,'POST e MBR/ESP · lê o BCD · confere assinaturas (KMCS) · inicia kernel e HAL · cria a sessão','fg-s')
    return svg(110,s,'Etapas da inicialização do Windows')
FIGS.update({'end_ddos':end_ddos,'end_smurf':end_smurf,'end_synflood':end_synflood,'end_arp':end_arp,'end_dhcp':end_dhcp,'end_dnstunnel':end_dnstunnel,'end_wincamadas':end_wincamadas,'end_boot':end_boot})
