def mc(q,o,e,r,dom,x=None,xt=None):
    d={'t':'mc','q':q,'o':o,'e':e,'r':r,'dom':dom}
    if x: d['x']=x; d['xt']=xt or 'saída'
    return d
def ms(q,o,e,r,dom,k=2,x=None,xt=None):
    d={'t':'ms','q':q,'o':o,'k':k,'e':e,'r':r,'dom':dom}
    if x: d['x']=x; d['xt']=xt or 'saída'
    return d
def inp(q,a,n,e,r,dom,ph=None,d=None,x=None,xt=None):
    z={'t':'in','q':q,'a':a,'n':n,'e':e,'r':r,'dom':dom}
    if ph: z['ph']=ph
    if d: z['d']=d
    if x: z['x']=x; z['xt']=xt or 'saída'
    return z
def multi(q,f,e,r,dom,x=None,xt=None,ord=False):
    z={'t':'multi','q':q,'f':f,'e':e,'r':r,'dom':dom}
    if x: z['x']=x; z['xt']=xt or 'saída'
    if ord: z['ord']=True
    return z
def F(l,a,n,d=None,ph=None):
    z={'l':l,'a':a if isinstance(a,list) else [a],'n':n}
    if d: z['d']=d
    if ph: z['ph']=ph
    return z
def C(l,ch,a): return {'l':l,'ch':ch,'a':a}
def ORD(items,labels=None):
    labels=labels or [f'{i+1}º' for i in range(len(items))]
    return [C(l,list(items),it) for l,it in zip(labels,items)]
