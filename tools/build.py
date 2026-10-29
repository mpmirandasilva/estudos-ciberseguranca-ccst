#!/usr/bin/env python3
"""Gera o site a partir das fontes: normaliza o HTML de cada trilha (figuras, tabelas, notas,
fluxos, terminais) para um único vocabulário visual e escreve data/<trilha>.js."""
import json, re, sys, os, hashlib, importlib.util
from bs4 import BeautifulSoup, NavigableString, Tag
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
import figs
OUT=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(HERE)

def modload(p):
    spec=importlib.util.spec_from_file_location(os.path.basename(p)[:-3],p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

FIG_BY_ALT=[('Símbolos','simbolos'),('Encapsulamento','encapsulamento'),('hierárquico','hierarquico'),('DORA','dora'),
            ('Caminho de um pacote','caminho'),('Solicitação ARP','arp'),('ARP','arp'),('handshake','handshake'),('traceroute','traceroute')]
CAPTION={'simbolos':'Símbolos usados nos diagramas de rede',
 'encapsulamento':'Na origem, cada camada acrescenta seu cabeçalho (encapsulamento); no destino, eles são retirados na ordem inversa',
 'hierarquico':'Modelo hierárquico: conexões redundantes entre as camadas superiores; os usuários se conectam na camada de acesso',
 'dora':'Processo DORA: as quatro mensagens com que o cliente obtém um endereço IPv4',
 'caminho':'Entre duas redes, os endereços MAC mudam a cada trecho, e os endereços IP permanecem até o destino',
 'arp':'A solicitação ARP chega a todos (broadcast); só o dono do endereço responde, diretamente a quem perguntou (unicast)',
 'handshake':'O handshake de três vias abre as duas sessões de uma conexão TCP full-duplex',
 'traceroute':'O traceroute aumenta o TTL a cada rodada; cada roteador que zera o TTL se identifica com "tempo excedido"'}
SVG={k:f() for k,f in figs.FIGS.items()}

CMD=re.compile(r'^(show|copy|ip |ipv6 |interface|int |line |enable|disable|configure|conf |hostname|crypto|username|service |banner|transport|login|no shutdown|ping|tracert|traceroute|ipconfig|arp |arp$|nslookup|netstat|exit|end$|password|description|ifconfig|ip$)',re.I)
NUM=re.compile(r'^[\s0-9A-Fa-fx.:/\-–·,]+$')
def is_code(t):
    t=t.strip()
    if not t or len(t)>60: return False
    if CMD.match(t): return True
    if NUM.match(t) and re.search(r'\d',t):
        if re.fullmatch(r'\d{1,5}',t): return False  # números simples: texto normal
        if re.search(r'[.:\-/]',t) or re.fullmatch(r'[01]{4,}',t) or t.lower().startswith('0x'): return True
    return False

def norm_html(html,tid,midx,figc):
    pres={}
    def keep_pre(m):
        k=f'@@PRE{len(pres)}@@'; pres[k]=m.group(0); return k
    html=re.sub(r'<pre>.*?</pre>',keep_pre,html,flags=re.S)
    html=re.sub(r'>\s+<','><',html).strip()
    for k,v in pres.items(): html=html.replace(k,v)
    s=BeautifulSoup(html,'html.parser')
    # figuras
    for fg in s.find_all('figure'):
        img=fg.find('img'); key=None
        if img is not None:
            src=img.get('src',''); alt=img.get('alt','')
            m=re.search(r'img/\w+/(\w+)\.png',src)
            if m: key=m.group(1)
            else:
                for a,k in FIG_BY_ALT:
                    if a.lower() in alt.lower(): key=k; break
        if key not in SVG: raise SystemExit(f'figura sem desenho: {tid} {midx} {img and img.get("alt")}')
        figc[midx]=figc.get(midx,0)+1
        new=BeautifulSoup(f'<figure class="fig blk"><div class="fig-c">{SVG[key]}</div><figcaption><b>FIGURA {midx}.{figc[midx]}</b><span>{CAPTION[key]}</span></figcaption></figure>','html.parser')
        fg.replace_with(new)
    # tabelas
    for t in s.find_all('table'):
        par=t.parent
        if not (isinstance(par,Tag) and par.name=='div' and 'tbl' in (par.get('class') or [])):
            w=s.new_tag('div',attrs={'class':'tbl'}); t.wrap(w); par=w
        par['class']=['tbl','blk']
        for a in list(t.attrs): del t[a]
        if not t.find('thead'):
            rows=t.find_all('tr',recursive=True)
            if rows and rows[0].find('th'):
                th=s.new_tag('thead'); first=rows[0].extract(); th.append(first)
                tb=t.find('tbody')
                if tb is None:
                    tb=s.new_tag('tbody')
                    for r in t.find_all('tr'): tb.append(r.extract())
                    t.append(tb)
                t.insert(0,th)
        for th in t.select('thead th'):
            for st in th.find_all(['strong','b']): st.unwrap()
        for td in t.find_all('td'):
            for a in list(td.attrs): del td[a]
            if not td.find(['mark']) and is_code(td.get_text()): td['class']=['c']
    # notas
    for p in s.find_all('p'):
        st=p.find('strong')
        if st and p.contents and p.contents[0] is st and re.match(r'^(Importante|Observação|Atenção|Dica):$',st.get_text().strip()):
            kind=st.get_text().strip()[:-1]; st.extract()
            if p.contents and isinstance(p.contents[0],NavigableString): p.contents[0].replace_with(p.contents[0].lstrip())
            cls='imp' if kind in ('Importante','Atenção') else 'obs'
            box=s.new_tag('div',attrs={'class':f'note {cls}'}); b=s.new_tag('b'); b.string=kind; inner=s.new_tag('div')
            for c in list(p.contents): inner.append(c.extract())
            box.append(b); box.append(inner); p.replace_with(box)
    # fluxos
    for p in s.find_all('p'):
        tx=p.get_text().strip()
        if tx.count('→')>=2 and not re.match(r'^(Exemplo|Ex\.)',tx) and not tx.endswith('.'):
            segs=[x.strip() for x in tx.split('→')]
            if all(0<len(x)<=44 for x in segs):
                hl=bool(p.find('mark'))
                html_='<div class="flow blk'+(' hl' if hl else '')+'" role="note" aria-label="Fluxo">'+'<i>→</i>'.join(f'<span>{BeautifulSoup(x,"html.parser").get_text()}</span>' for x in segs)+'</div>'
                p.replace_with(BeautifulSoup(html_,'html.parser'))
    # terminais
    for pre in s.find_all('pre'):
        code=pre.get_text()
        lines=code.split('\n')
        ios=any(re.match(r'^\S+(\(config[^)]*\))?[#>]',l) for l in lines)
        out=[]
        for l in lines:
            m=re.match(r'^(\S+(?:\(config[^)]*\))?[#>])(\s?)(.*)$',l)
            if m and ios: out.append(f'<span class="pr">{esc(m.group(1))}</span>{m.group(2)}{esc(m.group(3))}')
            else: out.append(f'<span class="cm">{esc(l)}</span>' if ios else esc(l))
        new=BeautifulSoup(f'<div class="cli blk"><div class="cli-bar"><i></i><i></i><i></i><span>{"CISCO IOS" if ios else "TERMINAL"}</span></div><pre>'+'\n'.join(out)+'</pre></div>','html.parser')
        pre.replace_with(new)
    for h in s.find_all('h4'):
        tx=h.get_text()
        if tx.startswith('Entendendo') or 'Exemplo Resolvido' in tx: h['class']=['ex']
    return str(s)
def esc(x): return x.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def check_ex(tid,EX,DATA):
    nums={t['num'] for m in DATA for t in m['topics']}
    nums|={str(i+1) for i in range(len(DATA))}
    probs=[]
    for k,qs in EX.items():
        for i,q in enumerate(qs):
            r=q.get('r','')
            base='.'.join(r.split('.')[:2])
            if base not in nums and r.split('.')[0]!=str(k) and r not in nums: probs.append((k,i,'ref',r))
            if q['t'] in ('mc','ms') and len(set(q['o']))!=len(q['o']): probs.append((k,i,'opções repetidas'))
            if q['t']=='ms' and not (1<q.get('k',2)<len(q['o'])): probs.append((k,i,'k'))
            if q['t']=='multi':
                for f in q['f']:
                    if 'ch' in f and f['a'] not in f['ch']: probs.append((k,i,'ch',f['l']))
            if q.get('dom') and q['dom'] not in range(1,7): probs.append((k,i,'d'))
    return probs

def build_track(meta,DATA,GLOSS,EX,ICONS):
    figc={}
    out=[]
    for i,m in enumerate(DATA):
        mi=i+1
        out.append({'title':m['title'],'intro':norm_html(m['intro'],meta['id'],mi,figc) if m['intro'] else '',
                    'topics':[{'num':t['num'],'title':t['title'],'html':norm_html(t['html'],meta['id'],mi,figc)} for t in m['topics']]})
    G=norm_html(GLOSS,meta['id'],0,{})
    probs=check_ex(meta['id'],EX,DATA)
    if probs: print('PROBLEMAS',meta['id'],probs)
    tr=dict(meta); tr.update({'DATA':out,'GLOSS':G,'EX':{str(k):v for k,v in EX.items()},'ICONS':{str(k):v for k,v in ICONS.items()}})
    js='window.TRACKS=window.TRACKS||[];\nwindow.TRACKS.push('+json.dumps(tr,ensure_ascii=False,separators=(',',':'))+');\n'
    os.makedirs(os.path.join(OUT,'data'),exist_ok=True)
    open(os.path.join(OUT,'data',meta['id']+'.js'),'w').write(js)
    nq=sum(len(v) for v in EX.values()); nc=sum(1 for v in EX.values() for q in v if q.get('dom'))
    print(meta['id'],'módulos',len(out),'tópicos',sum(len(m['topics']) for m in out),'questões',nq,'ccst',nc,'figuras',sum(figc.values()),'kB',len(js)//1024)

def main():
    src=os.path.join(HERE,'src')
    # trilha 1
    t1=json.load(open(os.path.join(src,'fundamentos.json')))
    ex1={int(k):v for k,v in t1['EX'].items()}
    c1=modload(os.path.join(HERE,'ccst_t1.py')).EX
    for k,v in c1.items(): ex1.setdefault(k,[]).extend(v)
    build_track({'id':'fundamentos','order':1,'short':'Fundamentos','label':'Trilha 1 · Networking Basics',
                 'title':'Fundamentos de Redes de Computadores',
                 'desc':'Do bit aos utilitários de teste: dados, desempenho, mídia, Ethernet, modelos OSI e TCP/IP, IPv4 e sub-redes, IPv6, DHCP, ARP, roteamento, TCP e UDP e serviços de aplicação.',
                 'icon':t1['ICONS']['1']},t1['DATA'],t1['GLOSS'],ex1,{int(k):v for k,v in t1['ICONS'].items()})
    # trilha 2
    import subprocess; subprocess.run([sys.executable,os.path.join(HERE,'conv.py')],check=True)
    d2=json.load(open(os.path.join(src,'dispositivos.json')))
    ex2=modload(os.path.join(HERE,'ex_disp.py')).EX
    c2=modload(os.path.join(HERE,'ccst_t2.py')).EX
    for k,v in c2.items(): ex2.setdefault(k,[]).extend(v)
    ic2=modload(os.path.join(HERE,'icons_disp.py')).ICONS
    build_track({'id':'dispositivos','order':2,'short':'Dispositivos','label':'Trilha 2 · Networking Devices and Initial Configuration',
                 'title':'Dispositivos de Rede e Configuração Inicial',
                 'desc':'Redes confiáveis, design hierárquico, nuvem, sistemas numéricos, Ethernet e switches, camada de rede, ARP, transporte, DNS e DHCP, Cisco IOS, configuração de switches e roteadores e ICMP.',
                 'icon':ic2[5]},d2['DATA'],d2['GLOSS'],ex2,ic2)
    # css e shell
    css='\n'.join(l for l in open(os.path.join(HERE,'base.css')).read().split('\n') if not re.match(r'\s*(\.tbl|figure|\.gl td:first-child)',l))+open(os.path.join(HERE,'components.css')).read()
    os.makedirs(os.path.join(OUT,'assets'),exist_ok=True)
    open(os.path.join(OUT,'assets','site.css'),'w').write(css)
    app=open(os.path.join(OUT,'assets','app.js')).read()
    v=hashlib.md5((css+app+open(os.path.join(OUT,'data','fundamentos.js')).read()[:100000]+open(os.path.join(OUT,'data','dispositivos.js')).read()).encode()).hexdigest()[:8]
    open(os.path.join(OUT,'index.html'),'w').write(open(os.path.join(HERE,'shell.html')).read().replace('__V__',v))
    print('versão',v)
if __name__=='__main__': main()
