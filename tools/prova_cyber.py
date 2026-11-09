# Banco de questões da trilha de teste "Prova CCST Cybersecurity".
# Base: apostila de questões da autora (enunciados reescritos e explicações próprias).
# Q(n, domínio, enunciado, opções, índices corretos, explicação, refs)  -> escolha única ou múltipla
# M(n, domínio, enunciado, [(item, resposta)], escolhas ou None, explicação, refs) -> associação/complete/verdadeiro-falso
# refs: 'trilha:tópico' (ex.: 'endpoint:21.2') = onde estudar o assunto.
import os, glob
DOMAINS={1:'Princípios essenciais de segurança',2:'Conceitos básicos de segurança de rede',3:'Segurança de endpoints',
         4:'Avaliação de vulnerabilidades e gerenciamento de riscos',5:'Tratamento de incidentes'}
QS=[]
def Q(n,d,q,o,a,e,refs):
    QS.append({'n':n,'d':d,'t':'ms' if len(a)>1 else 'mc','q':q,'o':o,'a':a,'e':e,'refs':refs})
def M(n,d,q,pairs,ch,e,refs):
    if ch is None:
        ch=[]
        for _,b in pairs:
            if b not in ch: ch.append(b)
    QS.append({'n':n,'d':d,'t':'match','q':q,'f':[{'l':a,'a':b} for a,b in pairs],'ch':ch,'e':e,'refs':refs})
HERE=os.path.dirname(os.path.abspath(__file__))
for f in sorted(glob.glob(os.path.join(HERE,'prova','b*.py'))):
    exec(open(f).read())
QS.sort(key=lambda x:x['n'])
