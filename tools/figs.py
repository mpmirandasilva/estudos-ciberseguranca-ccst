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
