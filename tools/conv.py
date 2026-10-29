import re, json, subprocess, html
from bs4 import BeautifulSoup, NavigableString
import os
HERE=os.path.dirname(os.path.abspath(__file__))
md=open(os.path.join(HERE,'src','dispositivos.md')).read()
body=md.split('\n## Glossário')[0]
gl=md.split('\n## Glossário de Siglas')[1].split('\n## Exercícios')[0]
phr=json.load(open(os.path.join(HERE,'src','grifos_dispositivos.json')))
def tohtml(t):
    t=re.sub(r'!\[([^\]]*)\]\((?:/tmp/claude-0/diag|img/dispositivos)/(\w+)\.png\)(\{[^}]*\})?', r'![\1](img/dispositivos/\2.png)', t)
    return subprocess.run(['pandoc','-f','markdown-smart','-t','html5','--wrap=none'],input=t,capture_output=True,text=True,check=True).stdout
def post(h):
    s=BeautifulSoup(h,'html.parser')
    for t in s.find_all('table'):
        for a in ('style','class'): 
            for el in [t]+t.find_all(True): el.attrs.pop(a,None)
        for cg in t.find_all('colgroup'): cg.decompose()
        w=s.new_tag('div',attrs={'class':'tbl'}); t.wrap(w)
    for h_ in s.find_all(['h4','h5','h6']):
        for a in list(h_.attrs): del h_[a]
    for im in s.find_all('img'): im['loading']='lazy'
    return s
done=set()
def highlight(s):
    for el in s.find_all(['p','li','td','th']):
        if el.find(['p','ul','ol']) and el.name=='li':
            pass
        txt=el.get_text()
        for ph in phr:
            if ph in done: continue
            i=txt.find(ph)
            if i<0: continue
            wrap_range(s,el,i,i+len(ph)); done.add(ph); txt=el.get_text()
def wrap_range(s,el,a,b):
    pos=0
    for node in list(el.descendants):
        if not isinstance(node,NavigableString): continue
        L=len(node); na,nb=pos,pos+L; pos=nb
        if nb<=a or na>=b: continue
        x=max(a,na)-na; y=min(b,nb)-na
        t=str(node); pre,mid,suf=t[:x],t[x:y],t[y:]
        m=s.new_tag('mark'); m.string=mid
        parts=[p for p in (NavigableString(pre) if pre else None, m, NavigableString(suf) if suf else None) if p is not None]
        node.replace_with(*parts)
secs=re.split(r'\n(?=## \d+\. )', '\n'+body)
mods=[]
for sec in secs:
    sec=sec.strip()
    if not sec.startswith('## '): continue
    head,rest=sec.split('\n',1)
    num,title=re.match(r'## (\d+)\. (.*)',head).groups()
    parts=re.split(r'\n(?=### )','\n'+rest)
    intro=parts[0].strip(); topics=[]
    for p in parts[1:]:
        p=p.strip(); h,c=(p.split('\n',1)+[''])[:2]
        tn,tt=re.match(r'### ([\d.]+) (.*)',h).groups()
        c=re.sub(r'^#### ',r'#### ',c,flags=re.M)
        topics.append({'num':tn,'title':tt,'md':c.strip()})
    mods.append({'title':title,'intro':intro,'topics':topics})
out=[]
for m in mods:
    si=post(tohtml(m['intro'])) if m['intro'] else None
    if si: highlight(si)
    tps=[]
    for t in m['topics']:
        # shift headings: #### -> h4, ##### -> h5
        s=post(tohtml(t['md'])); highlight(s)
        tps.append({'num':t['num'],'title':t['title'],'html':str(s).strip()})
    out.append({'title':m['title'],'intro':str(si).strip() if si else '','topics':tps})
gs=post(tohtml(gl.strip()))
json.dump({'DATA':out,'GLOSS':str(gs).strip()},open(os.path.join(HERE,'src','dispositivos.json'),'w'),ensure_ascii=False)
print('mods',len(out),'topics',sum(len(m['topics']) for m in out),'hl',len(done),'/',len(phr),[p for p in phr if p not in done])
