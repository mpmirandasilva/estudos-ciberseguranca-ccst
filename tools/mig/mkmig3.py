"""Mapa de grifos da versão 2 (reorganizada) para a 3 (enxuta) da mesma numeração.
Só trechos idênticos (blocos iguais de 12+ caracteres) carregam grifos; o resto é descartado."""
import json,sys,os,difflib,re
from html.parser import HTMLParser
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(os.path.dirname(HERE))
tid=sys.argv[1]
exec(open(os.path.join(HERE,'mkmig.py')).read().split('old=boxes')[0].split("tid=sys.argv[1]")[1].replace("def boxes","def boxes"),globals())
v2=boxes(loadjs(os.path.join(HERE,tid+'_v2.js'))); v3=boxes(loadjs(os.path.join(ROOT,'data',tid+'.js')))
hl={}
for k,h in v2.items():
    if k not in v3: continue
    a,am=text(h); b,bm=text(v3[k])
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    seg=[[i1,i2,j1] for t,i1,i2,j1,j2 in sm.get_opcodes() if t=='equal' and i2-i1>=12]
    used=set(); mk=[]
    for t in am:
        j=next((j for j,u in enumerate(bm) if u==t and j not in used),-1)
        if j>=0: used.add(j)
        mk.append(j)
    hl[k]={'seg':seg,'mk':mk}
p=os.path.join(HERE,tid+'.json'); M=json.load(open(p)); M['hv']=3; M['hl3']=hl
json.dump(M,open(p,'w'),ensure_ascii=False,separators=(',',':'))
print('caixas',len(hl))

# grifos já existentes da dona: os que não sobrevivem por trechos idênticos vão para o trecho mais parecido do texto novo
hp=os.path.join(HERE,tid+'_dona_v2.json')
if os.path.exists(hp):
    D=json.load(open(hp)); fix={}
    def pos(seg,p,end):
        for a,b,c in seg:
            if a<=p<=b: return c+p-a
        return None
    for k,rs in D.items():
        if k not in v2 or k not in v3: continue
        a,_=text(v2[k]); b,_=text(v3[k]); y=hl[k]
        for s,e in rs:
            s3,e3=pos(y['seg'],s,0),pos(y['seg'],e,1)
            if s3 is not None and e3 is not None and e3>s3: continue
            t=a[s:e].strip()
            if len(t)>=4 and b.count(t)==1:
                x=b.index(t); fix.setdefault(k,[]).append([s,e,x,x+len(t)])
            else: fix.setdefault(k,[]).append([s,e,-1,-1])
    M['fix3']=fix; json.dump(M,open(p,'w'),ensure_ascii=False,separators=(',',':'))
    print('ajustes',sum(len(v) for v in fix.values()),'descartados',sum(1 for v in fix.values() for r in v if r[2]<0))
