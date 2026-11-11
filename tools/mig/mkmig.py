"""Gera o mapa de migração (versão antiga → nova) de uma trilha reorganizada.
uso: python3 mkmig.py <trilha>  (lê tools/mig/<trilha>_v1.js e data/<trilha>.js; grava tools/mig/<trilha>.json)"""
import json,sys,os,re,difflib
from html.parser import HTMLParser
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(os.path.dirname(HERE))
tid=sys.argv[1]
def loadjs(p):
    s=open(p).read(); i=s.index('window.TRACKS.push(')+len('window.TRACKS.push('); return json.loads(s[i:s.rindex(');')])
class T(HTMLParser):
    def __init__(s): super().__init__(convert_charrefs=True); s.out=[]; s.svg=0; s.marks=[]; s.mk=None
    def handle_starttag(s,tag,a):
        if tag=='svg': s.svg+=1
        if tag=='mark' and not s.svg: s.mk=len(''.join(s.out))
    def handle_endtag(s,tag):
        if tag=='svg': s.svg-=1
        if tag=='mark' and s.mk is not None: t=''.join(s.out); s.marks.append(t[s.mk:]); s.mk=None
    def handle_data(s,d):
        if not s.svg: s.out.append(d)
def text(h):
    p=T(); p.feed(h); p.close(); return ''.join(p.out),p.marks
def boxes(tr):
    b={}
    for i,m in enumerate(tr['DATA'],1):
        b['m%d'%i]=m.get('intro','')
        for x in m['topics']: b[x['num']]=x['html']
    return b
old=boxes(loadjs(os.path.join(HERE,tid+'_v1.js'))); new=boxes(loadjs(os.path.join(ROOT,'data',tid+'.js')))
R=json.load(open(os.path.join(ROOT,'tools','remap_'+tid+'.json')))
M=json.load(open(os.path.join(HERE,tid+'_map.json')))  # idmap/modmap completos do compose
idmap,modmap=M['idmap'],M['modmap']; forced=M.get('intro',{})
def target(k):
    if k.startswith('m'): return 'm'+forced[k[1:]] if k[1:] in forced else None
    return idmap.get(k)
# grifos da dona feitos sobre uma versão ainda mais antiga do texto (o site dela estava em cache): usar essa versão como origem
v0k=os.path.join(HERE,tid+'_v0keys.json')
V0=json.load(open(v0k)) if os.path.exists(v0k) else []
v0=boxes(loadjs(os.path.join(HERE,tid+'_v0.js'))) if V0 else {}
hl={}; opn={}
for k,h in old.items():
    nk=target(k)
    if not k.startswith('m'):
        # tópicos antigos que viraram vários novos (filhos promovidos): todos contam como lidos
        kids=[v for c,v in idmap.items() if c.startswith(k+'.') and v.count('.')==1]
        opn[k]=[x for x in ([nk] if nk and nk.count('.')==1 else [])+kids]
    if not nk or nk not in new: continue
    a,am=text(v0[k] if k in V0 else h); b,bm=text(new[nk])
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    seg=[[i1,i2,j1] for tag,i1,i2,j1,j2 in sm.get_opcodes() if tag=='equal']
    # grifos originais: índice antigo → novo, pelo texto do grifo
    used=set(); mk=[]
    for i,t in enumerate(am):
        j=next((j for j,u in enumerate(bm) if u==t and j not in used),-1)
        if j>=0: used.add(j)
        mk.append(j)
    hl[k]={'to':nk,'seg':seg,'mk':mk,'same':a==b}
json.dump({'v':2,'hl':hl,'open':opn,'idmap':idmap,'modmap':modmap},open(os.path.join(HERE,tid+'.json'),'w'),ensure_ascii=False,separators=(',',':'))
print('caixas',len(hl),'iguais',sum(v['same'] for v in hl.values()),'sem destino',[k for k in old if k not in hl][:40])
