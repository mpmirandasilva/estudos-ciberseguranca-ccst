/* Trilhas de Redes — app de estudo (HTML, CSS e JS puros).
   Dados: window.TRACKS (um arquivo por trilha em /data). Progresso: localStorage por trilha,
   sincronizado com a conta Google quando o Firebase está configurado (firebase-config.js). */
(function(){
'use strict';
const TR=(window.TRACKS||[]).slice().sort((a,b)=>a.order-b.order);
const TRK={}; TR.forEach(t=>TRK[t.id]=t);
const DOMAINS={1:'Padrões e conceitos',2:'Endereçamento e sub-redes',3:'Endpoints e mídias',4:'Infraestrutura',5:'Diagnóstico de problemas',6:'Segurança'};
const $=(s,el=document)=>el.querySelector(s);
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const pad=n=>String(n).padStart(2,'0');

/* ---------- armazenamento ---------- */
const LEGACY={fundamentos:'redes-estudo-v1'};
const keyOf=id=>LEGACY[id]||('redes-estudo-'+id+'-v1');
const SIMKEY='redes-simulado-v1', THEMEKEY='redes-estudo-v1-theme';
function load(k){try{const r=localStorage.getItem(k); return r?JSON.parse(r):null}catch(e){return null}}
function store(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}
const ST={}; TR.forEach(t=>{ST[t.id]=Object.assign({open:{},ex:{},last:null,lastTs:0},load(keyOf(t.id))||{})});
let SIM=Object.assign({hist:[],cur:null},load(SIMKEY)||{});
function save(id){ if(id) store(keyOf(id),ST[id]); store(SIMKEY,SIM); Sync.push() }

/* ---------- tema ---------- */
const root=document.documentElement;
try{const t=localStorage.getItem(THEMEKEY); if(t) root.setAttribute('data-theme',t)}catch(e){}
$('#themeBtn').addEventListener('click',()=>{
  const cur=root.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
  const nx=cur==='dark'?'light':'dark'; root.setAttribute('data-theme',nx);
  try{localStorage.setItem(THEMEKEY,nx)}catch(e){}
  netColors();
});

/* ---------- ícones pixel ---------- */
function pixSvg(rows){
  if(!rows) return '';
  const used=rows.filter(r=>/[#+]/.test(r)); const top=Math.floor((12-used.length)/2); let out='';
  used.forEach((r,y)=>{[...r].forEach((c,x)=>{if(c==='#')out+=`<rect x="${x}" y="${y+top}" width="1" height="1" fill="currentColor"/>`; else if(c==='+')out+=`<rect x="${x}" y="${y+top}" width="1" height="1" style="fill:var(--turq)"/>`})});
  return `<svg class="px" viewBox="0 0 12 12" aria-hidden="true">${out}</svg>`;
}
const SIMICON=["....####....","..##....##..",".#...#....#.",".#...#....#.","#....#.....#","#....###...#","#..........#",".#........#.",".#........#.","..##....##..","....####....","............"];
const SITEICON=["............","....####....","..##....##..",".#..++++..#.","...+....+...","....+..+....",".....++.....","............",".....##.....",".....##.....","............","............"];
$('#brandIco').innerHTML=pixSvg(SITEICON);

/* ---------- preparação das trilhas ---------- */
TR.forEach(t=>{
  t.MODS=t.DATA.map((s,i)=>({...s,idx:i+1}));
  t.topicMod={}; t.MODS.forEach(m=>m.topics.forEach(x=>t.topicMod[x.num]=m.idx));
  t.TOTALQ=t.MODS.reduce((a,m)=>a+(t.EX[m.idx]||[]).length,0);
  t.TOTALT=t.MODS.reduce((a,m)=>a+m.topics.length,0);
  t.CCSTQ=t.MODS.reduce((a,m)=>a+(t.EX[m.idx]||[]).filter(q=>q.dom).length,0);
});
function refMod(t,r){const parts=String(r).split('.'); const m=+parts[0]; let num=parts.slice(0,2).join('.'); if(!t.topicMod[num]) num=null; return {m,num}}

/* ---------- correção ---------- */
function strip(s){return String(s).normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase().trim().replace(/[.;]+$/,'')}
function norm(s,n){
  s=strip(s);
  switch(n){
    case 'num': return s.replace(/[a-z\s/]/g,'').replace(/[.;]+$/,'');
    case 'ip': return s.replace(/\s/g,'');
    case 'bin': return s.replace(/[\s.]/g,'');
    case 'pfx': return s.replace(/[\s/]/g,'');
    case 'hex': return s.replace(/\s/g,'').replace(/^0x/,'').replace(/^0+(?=.)/,'');
    case 'v6': return s.replace(/\s/g,'');
    case 'cmd': return s.replace(/\s+/g,' ');
    default: return s.replace(/\s/g,'');
  }
}
function okField(f,v){ if(f.ch) return v===f.a; const nv=norm(v,f.n); if(!nv) return false; return f.a.some(a=>norm(a,f.n)===nv) }
function shown(f){if(f.ch) return f.a; if(f.d) return f.d; const a=f.a[0]; if(f.n==='pfx') return '/'+a; if(f.n==='hex'||f.n==='v6') return a.toUpperCase(); if(f.n==='txt'&&a.length<=7) return a.toUpperCase(); return a}
function fieldsOf(q){return q.t==='in'?[{l:'Resposta',a:q.a,n:q.n,ph:q.ph,d:q.d}]:q.f}
function grade(q,v){
  if(v==null) return false;
  if(q.t==='mc') return v===0;
  if(q.t==='ms'){const k=q.k||2; return Array.isArray(v)&&v.length===k&&v.every(x=>x<k)}
  const fs=fieldsOf(q); return fs.every((f,j)=>okField(f,(v||[])[j]||''));
}
function seeded(seed){let x=0; for(const c of String(seed)) x=(x*31+c.charCodeAt(0))>>>0; x=x||1; return ()=>{x^=x<<13;x>>>=0;x^=x>>17;x^=x<<5;x>>>=0;return x/4294967296}}
function shuffled(arr,seed){const r=seeded(seed); const a=arr.map((v,i)=>[v,i]); for(let i=a.length-1;i>0;i--){const j=Math.floor(r()*(i+1)); [a[i],a[j]]=[a[j],a[i]]} return a}

/* ---------- estatísticas ---------- */
function modStats(t,m){
  const S=ST[t.id]; const total=m.topics.length; const opened=m.topics.filter(x=>S.open[x.num]).length;
  const qs=t.EX[m.idx]||[]; let ans=0, ok=0;
  qs.forEach((q,i)=>{const r=S.ex[m.idx+'-'+i]; if(r){ans++; if(r.ok) ok++}});
  return {total,opened,q:qs.length,ans,ok};
}
function trackTotals(t){let o=0,a=0,k=0,done=0; t.MODS.forEach(m=>{const s=modStats(t,m); o+=s.opened; a+=s.ans; k+=s.ok; if(s.opened===s.total&&s.ans===s.q) done++}); return {o,a,k,done,p:(o+a)/((t.TOTALT+t.TOTALQ)||1)}}
function overall(){let n=0,d=0; TR.forEach(t=>{const x=trackTotals(t); n+=x.o+x.a; d+=t.TOTALT+t.TOTALQ}); return d?n/d:0}
let ctxTrack=null;
function updMeter(){const p=Math.round((ctxTrack?trackTotals(ctxTrack).p:overall())*100); $('#meterTxt').textContent=p+'%'; $('#meterBar').style.width=p+'%'; $('.xp').title=ctxTrack?('Progresso da trilha '+ctxTrack.short):'Progresso geral nas trilhas'}
const seg=(v,cls='')=>`<div class="seg ${cls}"><i style="width:${Math.round(v*100)}%"></i></div>`;
const statBox=(b,s)=>`<div class="frame stat"><b>${b}</b><span>${s}</span></div>`;

/* ---------- início ---------- */
function renderHome(){
  $('#simIco').innerHTML=pixSvg(SIMICON);
  const tm=TR.reduce((a,t)=>a+t.MODS.length,0), tt=TR.reduce((a,t)=>a+t.TOTALT,0), tq=TR.reduce((a,t)=>a+t.TOTALQ,0);
  $('#stats').innerHTML=[statBox(TR.length,'trilhas'),statBox(tm,'módulos'),statBox(tq,'exercícios'),statBox(Math.round(overall()*100)+'%','seu progresso')].join('');
  $('#tracks').innerHTML=TR.map(t=>{
    const x=trackTotals(t); const qok=x.k;
    return `<a class="frame track" href="#t/${t.id}">
      <div class="th"><div class="ico">${pixSvg(t.icon)}</div><div><div class="label">${esc(t.label)}</div><h3>${esc(t.title)}</h3></div></div>
      <p>${esc(t.desc)}</p>
      <div class="meta"><span class="chip">${t.MODS.length} módulos</span><span class="chip">${t.TOTALT} tópicos</span><span class="chip">${t.TOTALQ} exercícios</span></div>
      <div class="bars"><div><span>Tópicos ${x.o}/${t.TOTALT}</span>${seg(x.o/(t.TOTALT||1))}<em>${Math.round(x.o/(t.TOTALT||1)*100)}%</em></div>
      <div><span>Acertos ${qok}/${t.TOTALQ}</span>${seg(qok/(t.TOTALQ||1),'ex')}<em>${Math.round(qok/(t.TOTALQ||1)*100)}%</em></div></div>
      <span class="go">${x.o||x.a?'Continuar a trilha ▸':'Começar a trilha ▸'}</span></a>`}).join('');
  const last=TR.map(t=>({t,ts:ST[t.id].lastTs||0,m:ST[t.id].last})).filter(x=>x.m).sort((a,b)=>b.ts-a.ts)[0];
  const box=$('#continueBox');
  box.innerHTML=last?`<a class="btn" href="#t/${last.t.id}/m-${last.m}">Continuar: ${esc(last.t.short)}, módulo ${last.m} ▸</a><a class="btn ghost" href="#simulado">Simulado CCST</a>`
    :`<a class="btn" href="#t/${TR[0].id}">Começar pela trilha 1 ▸</a><a class="btn ghost" href="#simulado">Simulado CCST</a>`;
  const h=SIM.hist[SIM.hist.length-1];
  $('#simSub').textContent=h?`Último simulado: ${h.ok}/${h.n} (${Math.round(h.ok/h.n*100)}%) em ${new Date(h.end).toLocaleDateString('pt-BR')}.`:'Questões das duas trilhas no formato da prova, com tempo e resultado por domínio do blueprint.';
}

/* ---------- trilha ---------- */
function renderTrack(t){
  const x=trackTotals(t);
  const v=$('#v-trilha');
  v.innerHTML=`<div class="crumbs"><a href="#inicio">Início</a><span>/</span><span>${esc(t.short)}</span></div>
   <div class="mod-head"><div class="frame big">${pixSvg(t.icon)}</div><div><div class="label">${esc(t.label)}</div><h1>${esc(t.title)}</h1></div></div>
   <p class="lead" style="margin:-6px 0 22px">${esc(t.desc)}</p>
   <div class="stats">${statBox(t.MODS.length,'módulos')}${statBox(t.TOTALT,'tópicos')}${statBox(t.TOTALQ,'exercícios')}${statBox(Math.round(x.p*100)+'%','progresso')}</div>
   <div class="sec-head"><div><div class="label">Trilha</div><h2>Módulos</h2></div><a class="linkbtn" href="#t/${t.id}/glossario">Glossário de siglas →</a></div>
   <div class="grid" id="tiles"></div>`;
  const tiles=$('#tiles',v);
  t.MODS.forEach(m=>{
    const s=modStats(t,m); const done=s.opened===s.total&&s.ans===s.q;
    const a=document.createElement('a'); a.className='frame tile'+(done?' done':''); a.href=`#t/${t.id}/m-${m.idx}`;
    a.innerHTML=`<div class="ico">${pixSvg(t.ICONS[m.idx])}</div><div class="n">Módulo ${pad(m.idx)}</div><h3>${esc(m.title)}</h3>
      <div class="bars"><div><span>Tópicos ${s.opened}/${s.total}</span>${seg(s.total?s.opened/s.total:0)}</div>
      <div><span>Acertos ${s.ok}/${s.q}</span>${seg(s.q?s.ok/s.q:0,'ex')}</div>${done?'<span class="stamp">Concluído</span>':''}</div>`;
    tiles.appendChild(a);
  });
}

/* ---------- módulo ---------- */
const chev='<svg class="px" viewBox="0 0 5 5" fill="currentColor"><path d="M0 1h1v1H0zM1 2h1v1H1zM2 3h1v1H2zM3 2h1v1H3zM4 1h1v1H4z"/></svg>';
const chevUp='<svg class="px" viewBox="0 0 5 5" fill="currentColor"><path d="M0 3h1v1H0zM1 2h1v1H1zM2 1h1v1H2zM3 2h1v1H3zM4 3h1v1H4z"/></svg>';
const lockI='<svg class="px" viewBox="0 0 7 7" fill="currentColor"><path d="M2 0h3v1H2zM1 1h1v2H1zM5 1h1v2H5zM0 3h7v4H0z"/></svg>';
let cur={t:null,m:null};
const openUI={};
const cid=num=>'c-'+num.replace(/\./g,'-');
function isUnlocked(t,m,i){const S=ST[t.id]; return i===0||S.open[m.topics[i-1].num]||S.open[m.topics[i].num]}
function renderMod(t,idx,focus){
  const m=t.MODS[idx-1]; if(!m){location.hash='#t/'+t.id;return}
  cur={t,m:idx}; const S=ST[t.id]; S.last=idx; S.lastTs=Date.now(); save(t.id);
  const v=$('#v-mod'); const prev=t.MODS[idx-2], next=t.MODS[idx];
  v.innerHTML=`
    <div class="crumbs"><a href="#inicio">Início</a><span>/</span><a href="#t/${t.id}">${esc(t.short)}</a><span>/</span><span>Módulo ${pad(idx)} de ${t.MODS.length}</span></div>
    <div class="mod-head"><div class="frame big">${pixSvg(t.ICONS[idx])}</div><div><div class="label">${esc(t.short)} · Módulo ${pad(idx)}</div><h1>${esc(m.title)}</h1></div></div>
    <div class="mod-tools"><span class="count" id="cnt"></span>
      <button class="btn ghost sm" id="openAll" type="button">Abrir todos</button>
      <button class="btn sm" type="button" id="goEx">Ir aos exercícios ▾</button></div>
    <div class="layout">
      <nav class="frame toc" id="toc" aria-label="Tópicos do módulo"></nav>
      <div style="min-width:0">
        ${m.intro?`<div class="frame intro prose" data-k="m${idx}" style="border-top:2px solid var(--edge)">${m.intro}</div>`:''}
        <div class="cards" id="cards"></div>
        <div class="ex-wrap" id="ex-box"></div>
        <div class="nextmod">
          ${prev?`<a class="btn ghost" href="#t/${t.id}/m-${prev.idx}">◂ ${prev.idx}. ${esc(prev.title)}</a>`:'<span></span>'}
          ${next?`<a class="btn" href="#t/${t.id}/m-${next.idx}">${next.idx}. ${esc(next.title)} ▸</a>`:`<a class="btn" href="#t/${t.id}">Voltar à trilha</a>`}
        </div>
      </div>
    </div>`;
  const cards=$('#cards');
  m.topics.forEach((x,i)=>{
    const c=document.createElement('article'); c.className='frame card'; c.id=cid(x.num);
    c.innerHTML=`<button class="card-h" type="button" aria-expanded="false"><span class="n">${x.num}</span><span class="t">${esc(x.title)}</span><span class="hint"></span></button>
      <div class="card-b"><div><div class="prose" data-k="${x.num}">${x.html}</div></div></div>`;
    c.querySelector('.card-h').addEventListener('click',()=>toggle(t,m,i));
    cards.appendChild(c);
  });
  $('#goEx').addEventListener('click',()=>$('#ex-box').scrollIntoView({behavior:'smooth'}));
  $('#openAll').addEventListener('click',()=>{m.topics.forEach(x=>S.open[x.num]=1); save(t.id); m.topics.forEach((x,i)=>setCard(m,i,true)); refreshMod(t,m)});
  v.querySelectorAll('.prose[data-k]').forEach(b=>HL.render(t,b));
  refreshMod(t,m); renderEx(t,m);
  if(focus) openTo(t,m,focus); else window.scrollTo(0,0);
}
function setCard(m,i,open){
  const c=document.getElementById(cid(m.topics[i].num)); if(!c) return;
  openUI[m.topics[i].num]=open; c.classList.toggle('open',open); c.querySelector('.card-h').setAttribute('aria-expanded',open);
}
function toggle(t,m,i){
  const x=m.topics[i]; if(!isUnlocked(t,m,i)) return;
  const now=!openUI[x.num]; if(now){ST[t.id].open[x.num]=1; save(t.id)}
  setCard(m,i,now); refreshMod(t,m);
}
function refreshMod(t,m){
  const S=ST[t.id]; let nextSet=false;
  m.topics.forEach((x,i)=>{
    const c=document.getElementById(cid(x.num)); const un=isUnlocked(t,m,i); const seen=!!S.open[x.num];
    c.classList.toggle('locked',!un);
    const isNext=un&&!seen&&!nextSet; if(isNext) nextSet=true;
    c.classList.toggle('next',isNext);
    c.querySelector('.hint').innerHTML=!un?lockI+'bloqueado':(openUI[x.num]?'fechar '+chevUp:(seen?'rever '+chev:'abrir '+chev));
  });
  const s=modStats(t,m);
  $('#cnt').innerHTML=`${s.opened}/${s.total} tópicos ${seg(s.total?s.opened/s.total:0)}`;
  $('#openAll').hidden=s.opened===s.total;
  const toc=$('#toc'); toc.innerHTML=m.topics.map((x,i)=>`<a href="#" data-n="${x.num}" class="${S.open[x.num]?'open':(isUnlocked(t,m,i)?'':'locked')}"><b>${x.num}</b><span>${esc(x.title)}</span></a>`).join('')+`<div class="sep">Prática</div><a href="#" data-ex="1"><b>&gt;_</b><span>Exercícios (${s.ans}/${s.q})</span></a>`;
  toc.querySelectorAll('a').forEach(a=>a.addEventListener('click',e=>{e.preventDefault(); if(a.dataset.ex){$('#ex-box').scrollIntoView({behavior:'smooth'});return} openTo(t,m,a.dataset.n)}));
  updMeter();
}
function openTo(t,m,num){
  const i=m.topics.findIndex(x=>x.num===num); if(i<0) return;
  ST[t.id].open[num]=1; save(t.id); setCard(m,i,true); refreshMod(t,m);
  const c=document.getElementById(cid(num)); setTimeout(()=>c.scrollIntoView({behavior:'smooth',block:'start'}),60);
}

/* ---------- grifos pessoais (só da pessoa; salvos com o progresso) ---------- */
const HL={
  get(t,k){const S=ST[t.id]; S.hl=S.hl||{}; const h=S.hl[k]; return h?{add:(h.add||[]).slice(),off:(h.off||[]).slice(),ts:h.ts||0}:{add:[],off:[],ts:0}},
  put(t,k,h){const S=ST[t.id]; S.hl=S.hl||{}; h.ts=Date.now(); if(!h.add.length&&!h.off.length) S.hl[k]={add:[],off:[],ts:h.ts}; else S.hl[k]=h; save(t.id)},
  nodes(root){const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode:n=>n.parentElement&&n.parentElement.closest('svg,.hl-foot')?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT}); const a=[]; let n; while((n=w.nextNode())) a.push(n); return a},
  render(t,box){
    const h=this.get(t,box.dataset.k);
    box.querySelectorAll('mark.u').forEach(mk=>mk.replaceWith(...mk.childNodes)); box.normalize();
    box.querySelectorAll('mark:not(.u)').forEach((mk,i)=>{mk.dataset.b=i; mk.classList.toggle('off',h.off.includes(i))});
    h.add.forEach((r,j)=>this.wrap(box,r.s,r.e,j));
    let f=box.querySelector('.hl-foot'); if(f) f.remove();
    if(h.add.length||h.off.length){
      f=document.createElement('div'); f.className='hl-foot';
      f.innerHTML=`<span>Seus grifos neste tópico</span>${h.add.length?'<button type="button" class="linkbtn" data-a="clear">apagar os meus</button>':''}${h.off.length?'<button type="button" class="linkbtn" data-a="restore">restaurar os originais</button>':''}`;
      f.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{const x=this.get(t,box.dataset.k); if(b.dataset.a==='clear') x.add=[]; else x.off=[]; this.put(t,box.dataset.k,x); this.render(t,box)}));
      box.appendChild(f);
    }
  },
  wrap(box,s,e,j){
    let pos=0;
    for(const n of this.nodes(box)){
      const L=n.length, a=pos, b=pos+L; pos=b;
      if(b<=s||a>=e) continue;
      const x=Math.max(s,a)-a, y=Math.min(e,b)-a; if(y<=x) continue;
      let node=n; if(x>0) node=node.splitText(x); if(y-x<node.length) node.splitText(y-x);
      if(!node.textContent.trim()&&node.parentNode&&/^(TR|TBODY|THEAD|TABLE|UL|OL)$/.test(node.parentNode.nodeName)) continue;
      const mk=document.createElement('mark'); mk.className='u'; mk.dataset.u=j; node.parentNode.insertBefore(mk,node); mk.appendChild(node);
    }
  },
  offset(box,container,off){
    const r=document.createRange(); r.setStart(box,0); r.setEnd(container,off); let n=0;
    for(const t of this.nodes(box)){ if(!r.intersectsNode(t)) break; n+= t===container?off:t.length }
    return n;
  },
  merge(list){list.sort((a,b)=>a.s-b.s); const o=[]; list.forEach(r=>{const l=o[o.length-1]; if(l&&r.s<=l.e) l.e=Math.max(l.e,r.e); else o.push({s:r.s,e:r.e})}); return o},
  selInfo(){
    const sel=getSelection(); if(!sel||sel.isCollapsed||!sel.rangeCount) return null;
    const rg=sel.getRangeAt(0); const box=(rg.commonAncestorContainer.nodeType===1?rg.commonAncestorContainer:rg.commonAncestorContainer.parentElement).closest('.prose[data-k]');
    if(!box||!box.closest('#v-mod')||box.closest('.card:not(.open)')) return null;
    const s=this.offset(box,rg.startContainer,rg.startOffset), e=this.offset(box,rg.endContainer,rg.endOffset);
    if(e-s<1) return null; return {box,s,e,rect:rg.getBoundingClientRect()};
  },
  bar:null, ctx:null,
  showBar(rect,buttons){
    let b=this.bar; if(!b){b=this.bar=document.createElement('div'); b.className='hl-bar frame'; b.setAttribute('role','toolbar'); b.setAttribute('aria-label','Grifos'); document.body.appendChild(b);
      b.addEventListener('mousedown',e=>e.preventDefault()); b.addEventListener('click',e=>{const x=e.target.closest('button'); if(x) this.act(x.dataset.a)})}
    b.innerHTML=buttons.map(([a,l])=>`<button type="button" data-a="${a}">${l}</button>`).join('');
    b.hidden=false; const touch=matchMedia('(pointer:coarse)').matches;
    const w=b.offsetWidth, h=b.offsetHeight; let x=rect.left+rect.width/2-w/2; x=Math.max(8,Math.min(innerWidth-w-8,x));
    let y=touch?rect.bottom+10:rect.top-h-8; if(y<70) y=rect.bottom+10; if(y+h>innerHeight-8) y=Math.max(70,rect.top-h-8);
    b.style.left=x+'px'; b.style.top=y+'px';
  },
  hide(){if(this.bar) this.bar.hidden=true; this.ctx=null},
  act(a){
    const c=this.ctx; if(!c) return; const t=cur.t; const k=c.box.dataset.k; const h=this.get(t,k);
    if(a==='add'){h.add.push({s:c.s,e:c.e}); h.add=this.merge(h.add)}
    if(a==='del'){ // apaga a seleção: recorta os grifos pessoais e desliga os originais tocados
      const o=[]; h.add.forEach(r=>{ if(r.e<=c.s||r.s>=c.e) o.push(r); else { if(r.s<c.s) o.push({s:r.s,e:c.s}); if(r.e>c.e) o.push({s:c.e,e:r.e}) } }); h.add=o;
      (c.base||[]).forEach(i=>{if(!h.off.includes(i)) h.off.push(i)});
    }
    if(a==='delu'){ h.add.splice(c.u,1) }
    if(a==='delb'){ if(!h.off.includes(c.b)) h.off.push(c.b) }
    this.put(t,k,h); this.render(t,c.box); getSelection().removeAllRanges(); this.hide();
  },
  baseIn(box,s,e){ // grifos originais que a seleção toca
    const out=[]; box.querySelectorAll('mark:not(.u):not(.off)').forEach(mk=>{const a=this.offset(box,mk,0), b=a+mk.textContent.length; if(b>s&&a<e) out.push(+mk.dataset.b)}); return out;
  },
  init(){
    const check=()=>{const i=this.selInfo(); if(!i){ if(this.ctx&&this.ctx.sel) this.hide(); return }
      const h=this.get(cur.t,i.box.dataset.k); const base=this.baseIn(i.box,i.s,i.e); const anyU=h.add.some(r=>r.e>i.s&&r.s<i.e);
      this.ctx={box:i.box,s:i.s,e:i.e,base,sel:true};
      this.showBar(i.rect,[['add','Grifar'],...((anyU||base.length)?[['del','Apagar grifo']]:[])]);};
    let tm=null; document.addEventListener('selectionchange',()=>{clearTimeout(tm); tm=setTimeout(check,matchMedia('(pointer:coarse)').matches?450:120)});
    document.addEventListener('click',e=>{
      if(e.target.closest('.hl-bar')) return;
      const mk=e.target.closest('#v-mod .prose[data-k] mark'); const sel=getSelection();
      if(mk&&(!sel||sel.isCollapsed)&&!mk.classList.contains('off')){
        const box=mk.closest('.prose[data-k]');
        if(mk.classList.contains('u')) this.ctx={box,u:+mk.dataset.u}; else this.ctx={box,b:+mk.dataset.b};
        this.showBar(mk.getBoundingClientRect(),[[mk.classList.contains('u')?'delu':'delb','Apagar grifo']]); return;
      }
      if(!this.ctx||!this.ctx.sel) this.hide();
    });
    addEventListener('scroll',()=>{if(this.ctx&&!this.ctx.sel) this.hide()},{passive:true});
    addEventListener('hashchange',()=>this.hide());
  }
};
HL.init();

/* ---------- exercícios ---------- */
function renderEx(t,m){
  const box=$('#ex-box'); const qs=t.EX[m.idx]||[];
  const base=qs.map((q,i)=>[q,i]).filter(([q])=>!q.dom), cc=qs.map((q,i)=>[q,i]).filter(([q])=>q.dom);
  box.innerHTML=`<div class="ex-head"><div><div class="label">Fase final</div><h2>Exercícios do módulo ${m.idx}</h2><p>${qs.length} questões: ${base.length} de fixação e ${cc.length} no estilo da prova CCST. Múltipla escolha corrige no clique; as demais, em "Verificar".</p></div>
    <div class="score" id="score"></div></div><div id="qs" style="display:grid;gap:16px"></div>`;
  const list=$('#qs',box); let n=0;
  if(base.length){list.insertAdjacentHTML('beforeend','<div class="ex-sec">Fixação</div>'); base.forEach(([q,i])=>list.appendChild(renderQ(t,m,q,i,++n)))}
  if(cc.length){list.insertAdjacentHTML('beforeend','<div class="ex-sec">Estilo CCST <span class="dom">· cenários, saídas de comando e mais de uma resposta</span></div>'); cc.forEach(([q,i])=>list.appendChild(renderQ(t,m,q,i,++n)))}
  updScore(t,m);
}
function updScore(t,m){
  const S=ST[t.id]; const s=modStats(t,m); const el=$('#score'); if(!el) return; const wrong=s.ans-s.ok;
  el.innerHTML=`<span class="pill">${s.ans}/${s.q} feitas</span><span class="pill ok">${s.ok} acertos</span>${wrong?`<span class="pill bad">${wrong} erros</span><button class="btn ghost sm" type="button" id="redo">Refazer as erradas</button>`:''}${s.ans?`<button class="linkbtn" type="button" id="reset">zerar</button>`:''}`;
  const r=$('#redo'); if(r) r.addEventListener('click',()=>{(t.EX[m.idx]||[]).forEach((q,i)=>{const k=m.idx+'-'+i; if(S.ex[k]&&!S.ex[k].ok) delete S.ex[k]}); S.exTs=Date.now(); save(t.id); renderEx(t,m); refreshMod(t,m); $('#ex-box').scrollIntoView({behavior:'smooth'})});
  const z=$('#reset'); if(z) z.addEventListener('click',()=>{(t.EX[m.idx]||[]).forEach((q,i)=>delete S.ex[m.idx+'-'+i]); S.exTs=Date.now(); save(t.id); renderEx(t,m); refreshMod(t,m)});
}
function refLink(t,q){ if(!q.r) return ''; const {m,num}=refMod(t,q.r); return ` <button class="linkbtn" type="button" data-ref="${q.r}" data-t="${t.id}" data-m="${m}" data-n="${num||''}">Rever item ${q.r}${t!==ctxTrack?' ('+esc(t.short)+')':''}</button>` }
function bindRef(el){
  el.querySelectorAll('[data-ref]').forEach(b=>b.addEventListener('click',()=>{
    const t=TRK[b.dataset.t], m=+b.dataset.m, n=b.dataset.n;
    if(cur.t===t && m===cur.m && !$('#v-mod').hidden){ if(n) openTo(t,t.MODS[m-1],n); return }
    location.hash=`#t/${t.id}/m-${m}`+(n?'-t-'+n.replace(/\./g,'-'):'');
  }));
}
function feedback(t,q,ok,extra){return `<div class="fb ${ok?'ok':'bad'}"><b>${ok?'Correto!':'Não foi dessa vez'}</b>${extra||''}<span>${esc(q.e)}${refLink(t,q)}</span></div>`}
function exhibit(q){return q.x?`<div class="cli"><div class="cli-bar"><i></i><i></i><i></i><span>${esc(q.xt||'saída')}</span></div><pre>${esc(q.x)}</pre></div>`:''}
function kindOf(q){
  if(q.t==='mc') return 'múltipla escolha';
  if(q.t==='ms') return 'escolha '+(q.k===3?'três':'duas');
  if(q.t==='multi'&&q.f.every(f=>f.ch)) return q.ord?'ordenar':'associação';
  return 'resposta digitada';
}
function qHead(q,n){return `<div class="q-top"><span class="k">${pad(n)}</span><div class="txt">${esc(q.q)}</div><span class="kind">${kindOf(q)}</span>${q.dom?`<span class="kind ccst" title="Domínio ${q.dom} do blueprint CCST Networking: ${esc(DOMAINS[q.dom])}">CCST ${q.dom}.0</span>`:''}</div>`}
function renderQ(t,m,q,i,n){
  const S=ST[t.id]; const key=m.idx+'-'+i; const st=S.ex[key];
  const el=document.createElement('div'); el.className='frame q'+(st?(st.ok?' ok':' bad'):'');
  el.innerHTML=qHead(q,n)+exhibit(q)+'<div class="body"></div><div class="out"></div>';
  const body=$('.body',el), out=$('.out',el);
  const record=(ok,v)=>{S.ex[key]={ok,v,ts:Date.now()}; save(t.id); updScore(t,m); refreshMod(t,m)};
  const retry=()=>{$('[data-retry]',out).addEventListener('click',()=>{delete S.ex[key]; save(t.id); const nn=renderQ(t,m,q,i,n); el.replaceWith(nn); updScore(t,m); refreshMod(t,m); const f=nn.querySelector('input,select,.opt'); if(f) f.focus()})};
  const again='<div class="actions" style="margin-top:8px"><button class="linkbtn" type="button" data-retry>Tentar de novo</button></div>';
  if(q.t==='mc'||q.t==='ms'){
    const multi=q.t==='ms'; const k=q.k||2;
    const opts=shuffled(q.o,key+q.q);
    body.innerHTML=`<div class="opts">${opts.map(([tx,orig],j)=>`<button type="button" class="opt" data-o="${orig}">${multi?'<span class="box"></span>':''}<span class="l">${'ABCDEFGH'[j]}</span><span>${esc(tx)}</span></button>`).join('')}</div>${multi?`<div class="actions"><button class="btn" type="button" data-check disabled>Verificar</button><span class="sync" style="align-self:center">selecione ${k}</span></div>`:''}`;
    const btns=[...body.querySelectorAll('.opt')];
    const show=(pick)=>{
      btns.forEach(b=>{b.disabled=true; const o=+b.dataset.o; const right=multi?o<k:o===0; const picked=multi?pick.includes(o):o===pick; if(right) b.classList.add('right'); else if(picked) b.classList.add('wrong'); if(multi) b.classList.toggle('sel',picked)});
      const chk=$('[data-check]',body); if(chk) chk.parentElement.hidden=true;
      const ok=grade(q,pick); el.className='frame q '+(ok?'ok':'bad'); out.innerHTML=feedback(t,q,ok)+again; bindRef(out); retry();
    };
    if(!multi) btns.forEach(b=>b.addEventListener('click',()=>{const p=+b.dataset.o; record(grade(q,p),p); show(p)}));
    else{
      const sel=new Set(); const chk=$('[data-check]',body);
      btns.forEach(b=>b.addEventListener('click',()=>{const o=+b.dataset.o; if(sel.has(o)) sel.delete(o); else{ if(sel.size>=k) return; sel.add(o)} b.classList.toggle('sel',sel.has(o)); chk.disabled=sel.size!==k}));
      chk.addEventListener('click',()=>{const p=[...sel].sort((a,b)=>a-b); record(grade(q,p),p); show(p)});
    }
    if(st) show(st.v);
  } else {
    const fields=fieldsOf(q);
    body.innerHTML=`<div class="${q.t==='in'?'single':'fields'}">${fields.map((f,j)=>{
      const id=`f-${t.id}-${key}-${j}`;
      const ctl=f.ch?`<select id="${id}"><option value="">Escolha…</option>${shuffled(f.ch,key+j).map(([c])=>c).map(c=>`<option>${esc(c)}</option>`).join('')}</select>`
        :`<input id="${id}" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="${esc(f.ph||'')}">`;
      return `<div class="field" data-j="${j}"><label for="${id}">${esc(f.l)}</label>${ctl}<span class="exp" hidden></span></div>`}).join('')}
      ${q.t==='in'?'<button class="btn" type="button" data-check>Verificar</button>':''}</div>
      ${q.t!=='in'?'<div class="actions"><button class="btn" type="button" data-check>Verificar</button></div>':''}`;
    const ctls=[...body.querySelectorAll('input,select')];
    const check=(vals,storeIt)=>{
      let all=true;
      fields.forEach((f,j)=>{
        const fe=body.querySelector(`.field[data-j="${j}"]`); const ok=okField(f,vals[j]||''); if(!ok) all=false;
        fe.classList.toggle('right',ok); fe.classList.toggle('wrong',!ok);
        const ex=$('.exp',fe); if(!ok){ex.hidden=false; ex.textContent='✓ '+shown(f)} else ex.hidden=true;
      });
      ctls.forEach(c=>c.disabled=true); body.querySelectorAll('[data-check]').forEach(b=>b.hidden=true);
      if(storeIt) record(all,vals);
      el.className='frame q '+(all?'ok':'bad');
      out.innerHTML=feedback(t,q,all,(!all&&fields.length>1)?'<span>Os campos em vermelho mostram a resposta esperada.</span>':'')+again;
      bindRef(out); retry();
    };
    const go=()=>{const vals=ctls.map(c=>c.value); if(vals.every(v=>!v.trim())){ctls[0].focus(); return} check(vals,true)};
    body.querySelectorAll('[data-check]').forEach(b=>b.addEventListener('click',go));
    ctls.forEach((c,j)=>c.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault(); if(j<ctls.length-1) ctls[j+1].focus(); else go()}}));
    if(st){ctls.forEach((c,j)=>c.value=(st.v||[])[j]||''); check(st.v||[],false)}
  }
  return el;
}

/* ---------- glossário ---------- */
function renderGloss(t){
  const v=$('#v-glossario');
  v.innerHTML=`<div class="page-head"><div class="crumbs"><a href="#inicio">Início</a><span>/</span><a href="#t/${t.id}">${esc(t.short)}</a><span>/</span><span>Glossário</span></div><h1>Glossário de Siglas</h1><p class="lead">${esc(t.title)}</p></div>
   <div class="search"><input id="glq" type="search" placeholder="Buscar sigla ou significado (ex.: DHCP, roteamento)" autocomplete="off"></div>
   <div class="prose gl" id="glbody" style="padding:0;border:0">${t.GLOSS}</div><p class="empty" id="glempty" hidden>Nenhuma sigla encontrada.</p>`;
  const rows=[...v.querySelectorAll('tbody tr')]; const q=$('#glq');
  q.addEventListener('input',()=>{const s=strip(q.value); let n=0; rows.forEach(r=>{const hit=!s||strip(r.textContent).includes(s); r.hidden=!hit; if(hit)n++}); $('#glempty').hidden=n>0});
}

/* ---------- simulado ---------- */
const SIMN=40, SIMMIN=50;
function pool(){const p=[]; TR.forEach(t=>t.MODS.forEach(m=>(t.EX[m.idx]||[]).forEach((q,i)=>{if(q.dom) p.push({tid:t.id,m:m.idx,i,d:q.dom})}))); return p}
function pickSim(n){
  const P=pool(); const r=seeded('sim'+Date.now()); const by={}; P.forEach(x=>(by[x.d]=by[x.d]||[]).push(x));
  Object.values(by).forEach(a=>a.sort(()=>r()-.5));
  const ds=Object.keys(by).map(Number).sort(); const out=[]; let k=0;
  while(out.length<Math.min(n,P.length)){const d=ds[k++%ds.length]; if(by[d].length) out.push(by[d].pop()); if(ds.every(x=>!by[x].length)) break}
  return out.sort(()=>r()-.5);
}
const qOf=it=>TRK[it.tid].EX[it.m][it.i];
let simTimer=null, simPos=0;
function renderSim(){
  const v=$('#v-simulado'); clearInterval(simTimer);
  const c=SIM.cur;
  if(c && !c.done){ return renderSimRun() }
  const P=pool(); const dc={}; P.forEach(x=>dc[x.d]=(dc[x.d]||0)+1);
  const hist=SIM.hist.slice(-8).reverse();
  v.innerHTML=`<div class="page-head"><div class="crumbs"><a href="#inicio">Início</a><span>/</span><span>Simulado CCST</span></div><h1>Simulado CCST Networking</h1>
    <p class="lead">Questões no formato da prova 100-150, sorteadas das duas trilhas e distribuídas pelos seis domínios do blueprint. Sem correção durante a prova: o resultado sai no final, por domínio, com explicação e o item para revisar.</p></div>
    <div class="about"><div class="frame">
      <h3>Como funciona</h3>
      <ul><li><b>${SIMN} questões</b> em <b>${SIMMIN} minutos</b>, como a prova (tempo oficial: 50 minutos).</li><li>Dá para pular, marcar para revisar e voltar antes de entregar.</li><li>Questões de "escolha duas" só contam se as duas estiverem certas, como na prova.</li><li>A Cisco não publica a nota de aprovação; use <b>80%</b> como meta de segurança.</li></ul>
      <div class="actions" style="margin-top:14px"><button class="btn" id="simGo" type="button">Começar o simulado ▸</button><button class="btn ghost" id="simQuick" type="button">Versão curta (20 questões, 25 min)</button></div>
    </div><div class="frame"><h3>Banco de questões</h3><div class="dom-rows">${Object.entries(DOMAINS).map(([d,n])=>`<div class="dom-row"><span>${d}.0 ${esc(n)}</span>${seg((dc[d]||0)/Math.max(...Object.values(dc),1))}<em>${dc[d]||0}</em></div>`).join('')}</div>
    ${hist.length?`<h3 style="margin-top:18px">Seus últimos simulados</h3><table class="hist"><tr><th>Data</th><th>Acertos</th><th>%</th></tr>${hist.map(h=>`<tr><td>${new Date(h.end).toLocaleString('pt-BR',{dateStyle:'short',timeStyle:'short'})}</td><td>${h.ok}/${h.n}</td><td>${Math.round(h.ok/h.n*100)}%</td></tr>`).join('')}</table>`:''}
    </div></div>
    ${c&&c.done?`<div style="margin-top:22px"><button class="btn ghost" id="simLast" type="button">Ver o resultado do último simulado</button></div>`:''}`;
  const start=(n,min)=>{SIM.cur={id:Date.now(),start:Date.now(),dur:min*60000,items:pickSim(n),ans:{},flag:{},done:false}; simPos=0; save(); renderSimRun()};
  $('#simGo').addEventListener('click',()=>start(SIMN,SIMMIN));
  $('#simQuick').addEventListener('click',()=>start(20,25));
  const l=$('#simLast'); if(l) l.addEventListener('click',()=>renderSimResult());
}
function simLeft(){const c=SIM.cur; return Math.max(0,c.start+c.dur-Date.now())}
function fmt(ms){const s=Math.ceil(ms/1000); return pad(Math.floor(s/60))+':'+pad(s%60)}
function renderSimRun(){
  const v=$('#v-simulado'); const c=SIM.cur; const N=c.items.length; simPos=Math.min(simPos,N-1);
  const it=c.items[simPos]; const q=qOf(it); const t=TRK[it.tid];
  v.innerHTML=`<div class="frame sim-top"><div><div class="label">Simulado CCST · questão ${simPos+1} de ${N}</div><div class="sim-dots" id="dots"></div></div><div style="display:flex;gap:10px;align-items:center"><span class="clock" id="clock">${fmt(simLeft())}</span><button class="btn sm" id="simEnd" type="button">Entregar</button></div></div>
   <div id="simq"></div>
   <div class="sim-nav"><button class="btn ghost" id="prev" type="button" ${simPos?'':'disabled'}>◂ Anterior</button><button class="btn ghost" id="flag" type="button">${c.flag[simPos]?'Desmarcar revisão':'Marcar para revisar'}</button><button class="btn" id="next" type="button">${simPos<N-1?'Próxima ▸':'Revisar e entregar'}</button></div>`;
  const dots=$('#dots');
  dots.innerHTML=c.items.map((x,j)=>`<button type="button" data-j="${j}" class="${c.ans[j]!=null?'ans':''}${c.flag[j]?' flag':''}${j===simPos?' cur':''}" aria-label="Questão ${j+1}">${j+1}</button>`).join('');
  dots.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{simPos=+b.dataset.j; renderSimRun()}));
  $('#simq').appendChild(examQ(q,simPos));
  $('#prev').addEventListener('click',()=>{simPos--; renderSimRun(); window.scrollTo(0,0)});
  $('#next').addEventListener('click',()=>{ if(simPos<N-1){simPos++; renderSimRun(); window.scrollTo(0,0)} else confirmEnd()});
  $('#flag').addEventListener('click',()=>{c.flag[simPos]=!c.flag[simPos]; save(); renderSimRun()});
  $('#simEnd').addEventListener('click',confirmEnd);
  clearInterval(simTimer);
  simTimer=setInterval(()=>{const l=simLeft(); const el=$('#clock'); if(!el){clearInterval(simTimer);return} el.textContent=fmt(l); el.classList.toggle('low',l<5*60000); if(l<=0){clearInterval(simTimer); finishSim()}},1000);
}
function confirmEnd(){
  const c=SIM.cur; const open=c.items.length-Object.keys(c.ans).filter(k=>c.ans[k]!=null).length;
  const v=$('#simq'); const box=document.createElement('div'); box.className='frame q'; box.style.marginTop='14px';
  box.innerHTML=`<b>Entregar o simulado?</b><span>${open?`Ainda há ${open} questão(ões) sem resposta; elas contam como erro.`:'Todas as questões foram respondidas.'}</span><div class="actions"><button class="btn" type="button" id="yes">Entregar agora</button><button class="btn ghost" type="button" id="no">Continuar</button></div>`;
  v.appendChild(box); box.scrollIntoView({behavior:'smooth'});
  $('#yes',box).addEventListener('click',finishSim); $('#no',box).addEventListener('click',()=>box.remove());
}
function examQ(q,j){
  const c=SIM.cur; const v=c.ans[j];
  const el=document.createElement('div'); el.className='frame q';
  el.innerHTML=qHead(q,j+1)+exhibit(q)+'<div class="body"></div>';
  const body=$('.body',el);
  const set=val=>{c.ans[j]=val; save(); const d=$(`#dots [data-j="${j}"]`); if(d) d.classList.toggle('ans',val!=null)};
  if(q.t==='mc'||q.t==='ms'){
    const multi=q.t==='ms', k=q.k||2; const opts=shuffled(q.o,c.id+'-'+j);
    body.innerHTML=`<div class="opts">${opts.map(([tx,orig],n)=>`<button type="button" class="opt" data-o="${orig}">${multi?'<span class="box"></span>':''}<span class="l">${'ABCDEFGH'[n]}</span><span>${esc(tx)}</span></button>`).join('')}</div>${multi?`<span class="sync">selecione ${k}</span>`:''}`;
    const btns=[...body.querySelectorAll('.opt')]; const sel=new Set(multi?(v||[]):(v!=null?[v]:[]));
    const paint=()=>btns.forEach(b=>b.classList.toggle('sel',sel.has(+b.dataset.o)));
    btns.forEach(b=>b.addEventListener('click',()=>{const o=+b.dataset.o;
      if(multi){ if(sel.has(o)) sel.delete(o); else{ if(sel.size>=k) return; sel.add(o)} set(sel.size?[...sel].sort((a,b)=>a-b):null) }
      else{ sel.clear(); sel.add(o); set(o) } paint()}));
    paint();
  } else {
    const fields=fieldsOf(q);
    body.innerHTML=`<div class="fields">${fields.map((f,n)=>{const id=`s-${j}-${n}`; const ctl=f.ch?`<select id="${id}"><option value="">Escolha…</option>${shuffled(f.ch,c.id+'-'+j+'-'+n).map(([x])=>`<option>${esc(x)}</option>`).join('')}</select>`:`<input id="${id}" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="${esc(f.ph||'')}">`; return `<div class="field"><label for="${id}">${esc(f.l)}</label>${ctl}</div>`}).join('')}</div>`;
    const ctls=[...body.querySelectorAll('input,select')];
    ctls.forEach((x,n)=>{x.value=(v||[])[n]||''; x.addEventListener('input',()=>{const vals=ctls.map(y=>y.value); set(vals.some(y=>y.trim())?vals:null)}); x.addEventListener('change',()=>{const vals=ctls.map(y=>y.value); set(vals.some(y=>y.trim())?vals:null)})});
  }
  return el;
}
function finishSim(){
  clearInterval(simTimer); const c=SIM.cur; if(!c||c.done) return renderSimResult();
  c.done=true; c.end=Date.now(); const byDom={}; let ok=0;
  c.items.forEach((it,j)=>{const q=qOf(it); const g=grade(q,c.ans[j]); c.res=c.res||{}; c.res[j]=g; if(g) ok++; const b=byDom[it.d]=byDom[it.d]||{n:0,ok:0}; b.n++; if(g) b.ok++});
  SIM.hist.push({id:c.id,end:c.end,n:c.items.length,ok,byDom}); SIM.hist=SIM.hist.slice(-50); save(); renderSimResult();
}
function renderSimResult(){
  const v=$('#v-simulado'); const c=SIM.cur; if(!c) return renderSim();
  const h=SIM.hist.find(x=>x.id===c.id)||{n:c.items.length,ok:0,byDom:{}}; const p=Math.round(h.ok/h.n*100);
  v.innerHTML=`<div class="page-head"><div class="crumbs"><a href="#inicio">Início</a><span>/</span><a href="#simulado" id="toSim">Simulado CCST</a><span>/</span><span>Resultado</span></div><h1>Resultado do simulado</h1></div>
   <div class="about"><div class="frame"><div class="label">Acertos</div><div class="big-score">${p}%</div><p>${h.ok} de ${h.n} questões. ${p>=80?'Acima da meta de 80%: bom sinal para a prova.':'Abaixo da meta de 80%: revise os domínios com menor resultado.'}</p>
     <div class="actions"><button class="btn" id="again" type="button">Novo simulado</button></div></div>
   <div class="frame"><h3>Por domínio do blueprint</h3><div class="dom-rows">${Object.entries(DOMAINS).filter(([d])=>h.byDom[d]).map(([d,n])=>{const b=h.byDom[d]; return `<div class="dom-row"><span>${d}.0 ${esc(n)}</span>${seg(b.ok/b.n,b.ok/b.n<.8?'ex':'')}<em>${b.ok}/${b.n}</em></div>`}).join('')}</div></div></div>
   <div class="sec-head" style="margin-top:26px"><div><div class="label">Correção</div><h2>Questão por questão</h2></div></div><div id="rev" style="display:grid;gap:14px"></div>`;
  const rev=$('#rev');
  c.items.forEach((it,j)=>{
    const q=qOf(it), t=TRK[it.tid], ok=c.res&&c.res[j];
    const el=document.createElement('div'); el.className='frame q '+(ok?'ok':'bad');
    let ans='';
    if(q.t==='mc') ans=`<div class="fb ${ok?'ok':'bad'}"><b>${ok?'Correto':'Errado'}</b><span>Resposta: ${esc(q.o[0])}${!ok&&c.ans[j]!=null?` · você marcou: ${esc(q.o[c.ans[j]])}`:''}</span><span>${esc(q.e)}${refLink(t,q)}</span></div>`;
    else if(q.t==='ms') ans=`<div class="fb ${ok?'ok':'bad'}"><b>${ok?'Correto':'Errado'}</b><span>Respostas: ${q.o.slice(0,q.k||2).map(esc).join(' · ')}</span><span>${esc(q.e)}${refLink(t,q)}</span></div>`;
    else ans=`<div class="fb ${ok?'ok':'bad'}"><b>${ok?'Correto':'Errado'}</b><span>${fieldsOf(q).map(f=>esc(f.l)+': '+esc(shown(f))).join(' · ')}</span><span>${esc(q.e)}${refLink(t,q)}</span></div>`;
    el.innerHTML=qHead(q,j+1)+exhibit(q)+ans; bindRef(el); rev.appendChild(el);
  });
  $('#again').addEventListener('click',()=>{SIM.cur=null; save(); renderSim()});
}

/* ---------- sobre ---------- */
function renderAbout(){
  $('#stats2').innerHTML=TR.map(t=>statBox(t.MODS.length,'módulos · '+t.short)).join('')+statBox(TR.reduce((a,t)=>a+t.TOTALQ,0),'exercícios')+statBox(pool().length,'questões CCST');
}

/* ---------- sincronização (Firebase opcional) ---------- */
const Sync={on:false,user:null,doc:null,timer:null,applying:false,
  init(){
    const cfg=window.FIREBASE_CONFIG; const btn=$('#acctBtn');
    if(!cfg||!cfg.apiKey){btn.hidden=true; return}
    btn.hidden=false;
    const V='10.12.5', base=`https://www.gstatic.com/firebasejs/${V}/`;
    const load=src=>new Promise((ok,no)=>{const s=document.createElement('script'); s.src=base+src; s.onload=ok; s.onerror=no; document.head.appendChild(s)});
    load('firebase-app-compat.js').then(()=>Promise.all([load('firebase-auth-compat.js'),load('firebase-firestore-compat.js')])).then(()=>{
      firebase.initializeApp(cfg); this.auth=firebase.auth(); this.db=firebase.firestore(); this.on=true;
      this.auth.getRedirectResult().catch(()=>{});
      this.auth.onAuthStateChanged(u=>this.onUser(u));
    }).catch(()=>{btn.title='Não foi possível carregar o login'; this.paint()});
    btn.addEventListener('click',()=>this.menu());
  },
  paint(){
    const b=$('#acctBtn'); if(!b) return;
    if(this.user){b.innerHTML=(this.user.photoURL?`<img class="av" src="${esc(this.user.photoURL)}" alt="" referrerpolicy="no-referrer">`:'<span>●</span>')+'<span class="lbl">Conta</span>'; b.title='Conectado como '+(this.user.email||'')}
    else{b.innerHTML='<svg class="px" viewBox="0 0 7 7" fill="currentColor"><path d="M2 0h3v3H2zM1 4h5v1H1zM0 5h7v2H0z"/></svg><span class="lbl">Entrar</span>'; b.title='Entrar com Google para salvar o progresso na nuvem'}
  },
  menu(){
    if(!this.on){toast('O login não está disponível agora.'); return}
    if(!this.user){
      const p=new firebase.auth.GoogleAuthProvider();
      this.auth.signInWithPopup(p).catch(e=>{ if(e&&/popup|operation-not-supported/.test(e.code||'')) this.auth.signInWithRedirect(p); else toast('Não foi possível entrar: '+(e.message||e.code)) });
      return;
    }
    const old=$('#acctMenu'); if(old){old.remove();return}
    const m=document.createElement('div'); m.id='acctMenu'; m.className='frame'; m.style.cssText='position:absolute;right:0;top:calc(100% + 8px);padding:12px;display:grid;gap:8px;min-width:240px;z-index:9';
    m.innerHTML=`<b style="font-size:14px">${esc(this.user.displayName||'Conta Google')}</b><span class="sync on" style="font-size:12px"><i></i>${esc(this.user.email||'')} · progresso sincronizado</span><button class="btn ghost sm" type="button" id="out">Sair</button>`;
    $('#acctBtn').parentElement.appendChild(m);
    $('#out',m).addEventListener('click',()=>{this.auth.signOut(); m.remove()});
    setTimeout(()=>document.addEventListener('click',function h(e){if(!m.contains(e.target)&&e.target.closest('#acctBtn')==null){m.remove();document.removeEventListener('click',h)}}),0);
  },
  onUser(u){
    this.user=u; this.paint(); if(this.unsub){this.unsub(); this.unsub=null}
    if(!u){this.doc=null; return}
    this.doc=this.db.collection('progresso').doc(u.uid);
    this.doc.get().then(snap=>{ if(snap.exists) this.apply(snap.data()); this.push(true); toast('Progresso sincronizado com '+(u.email||'sua conta')+'.');
      this.unsub=this.doc.onSnapshot(s=>{ if(!s.metadata.hasPendingWrites && s.exists) this.apply(s.data()) });
    }).catch(e=>toast('Erro ao sincronizar: '+(e.code||e.message)));
  },
  apply(d){
    if(!d||!d.tracks) return; this.applying=true; let changed=false;
    TR.forEach(t=>{const a=ST[t.id], b=d.tracks[t.id]; if(!b) return;
      Object.keys(b.open||{}).forEach(k=>{if(!a.open[k]){a.open[k]=1; changed=true}});
      a.hl=a.hl||{}; Object.entries(b.hl||{}).forEach(([k,h])=>{const l=a.hl[k]; if(!l||(h.ts||0)>(l.ts||0)){a.hl[k]=h; changed=true}});
      Object.entries(b.ex||{}).forEach(([k,r])=>{const l=a.ex[k]; if(!l||(r.ts||0)>(l.ts||0)){a.ex[k]=r; changed=true}});
      if((b.exTs||0)>(a.exTs||0)){ Object.keys(a.ex).forEach(k=>{ if(!(k in (b.ex||{})) && (a.ex[k].ts||0)<b.exTs){delete a.ex[k]; changed=true} }); a.exTs=b.exTs }
      if((b.lastTs||0)>(a.lastTs||0)){a.last=b.last; a.lastTs=b.lastTs; changed=true}
      store(keyOf(t.id),a)});
    if(d.sim){const ids=new Set(SIM.hist.map(h=>h.id)); (d.sim.hist||[]).forEach(h=>{if(!ids.has(h.id)){SIM.hist.push(h); changed=true}}); SIM.hist.sort((a,b)=>a.end-b.end);
      if(d.sim.cur&&(!SIM.cur||d.sim.cur.id>SIM.cur.id||(d.sim.cur.id===SIM.cur.id&&d.sim.cur.done&&!SIM.cur.done))){SIM.cur=d.sim.cur; changed=true}
      store(SIMKEY,SIM)}
    this.applying=false;
    if(changed) route(true);
  },
  push(now){
    if(!this.doc||this.applying) return; clearTimeout(this.timer);
    const go=()=>{const tracks={}; TR.forEach(t=>tracks[t.id]=ST[t.id]);
      this.doc.set({v:1,tracks,sim:SIM,updated:firebase.firestore.FieldValue.serverTimestamp()}).catch(e=>toast('Erro ao salvar na nuvem: '+(e.code||e.message)))};
    if(now) go(); else this.timer=setTimeout(go,1500);
  }
};
function toast(msg){const t=document.createElement('div'); t.className='toast'; t.textContent=msg; document.body.appendChild(t); setTimeout(()=>t.remove(),4200)}

/* ---------- animação da rede ---------- */
const cv=$('#net'), cx=cv.getContext('2d'); cx.imageSmoothingEnabled=false;
const W=320,H=180; let C={};
function netColors(){const cs=getComputedStyle(root); ['ink','turq','amber','muted','sunk','edge','surface','ok'].forEach(k=>C[k]=cs.getPropertyValue('--'+k).trim()); drawNet(performance.now())}
const N=[{x:28,y:40,k:'pc',n:'PC A'},{x:28,y:122,k:'pc',n:'PC B'},{x:106,y:81,k:'sw',n:'switch'},{x:186,y:81,k:'rt',n:'roteador'},{x:262,y:36,k:'cl',n:'Internet'},{x:270,y:132,k:'sv',n:'servidor'}];
const L=[[0,2],[1,2],[2,3],[3,4],[3,5]];
const ROUTES=[
 {p:[0,2,3,4],c:'turq',log:'<b>PC A</b> → DNS 8.8.8.8 · UDP 53'},
 {p:[1,2,3,5],c:'amber',log:'<b>PC B</b> → servidor · TCP 443 (HTTPS)'},
 {p:[5,3,2,0],c:'amber',log:'<b>servidor</b> → PC A · resposta TCP'},
 {p:[1,2,0],c:'turq',log:'<b>PC B</b> → PC A · mesma rede, só o switch'},
 {p:[0,2,3,5],c:'turq',log:'<b>PC A</b> → servidor · ping (ICMP echo)'},
 {p:[0,2,3],c:'amber',log:'<b>PC A</b> → R1 · SSH (TCP 22) para configurar'},
];
function R(x,y,w,h,c){cx.fillStyle=c; cx.fillRect(Math.round(x),Math.round(y),w,h)}
function node(n){
  const x=n.x,y=n.y,ink=C.ink,t=C.turq;
  if(n.k==='pc'){R(x-11,y-10,22,15,ink);R(x-9,y-8,18,11,t);R(x-2,y+5,4,3,ink);R(x-7,y+8,14,2,ink)}
  if(n.k==='sw'){R(x-16,y-6,32,12,ink);for(let i=0;i<5;i++)R(x-13+i*6,y-1,3,3,t)}
  if(n.k==='rt'){R(x-14,y-6,28,12,ink);R(x-12,y-9,24,3,ink);R(x-8,y-2,3,3,t);R(x+5,y-2,3,3,t);R(x-9,y-17,2,8,ink);R(x+7,y-17,2,8,ink)}
  if(n.k==='cl'){cx.fillStyle=C.amber;[[0,0,30,10],[4,-5,22,6],[9,-9,12,5],[-3,4,36,6]].forEach(([a,b,w,h])=>cx.fillRect(x-15+a,y-3+b,w,h))}
  if(n.k==='sv'){R(x-9,y-14,18,28,ink);for(let i=0;i<3;i++){R(x-6,y-11+i*8,12,4,C.sunk);R(x+3,y-10+i*8,2,2,C.ok)}}
  cx.fillStyle=C.muted; cx.font='8px "Silkscreen", monospace'; cx.textAlign='center'; cx.fillText(n.n.toUpperCase(),x,y+(n.k==='sv'?24:20));
}
let rt=0,t0=0;
function drawNet(now){
  if(!C.ink) return;
  R(0,0,W,H,C.sunk);
  cx.fillStyle=C.edge; for(let x=0;x<W;x+=8) for(let y=0;y<H;y+=8) if((x+y)%16===0) cx.fillRect(x,y,1,1);
  L.forEach(([a,b])=>{const A=N[a],B=N[b]; const steps=Math.max(Math.abs(B.x-A.x),Math.abs(B.y-A.y))/2; for(let i=0;i<=steps;i+=2){const x=A.x+(B.x-A.x)*i/steps,y=A.y+(B.y-A.y)*i/steps; R(x,y,2,2,C.muted)}});
  N.forEach(node);
  const r=ROUTES[rt], dur=900, sg=Math.min(r.p.length-2,Math.floor((now-t0)/dur)), f=Math.min(1,((now-t0)%dur)/dur);
  const A=N[r.p[sg]],B=N[r.p[sg+1]]; const e=Math.round(f*8)/8;
  const px=A.x+(B.x-A.x)*e, py=A.y+(B.y-A.y)*e;
  R(px-4,py-4,8,8,C.ink); R(px-3,py-3,6,6,C[r.c]);
}
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
function loop(now){
  const r=ROUTES[rt];
  if(now-t0>900*(r.p.length-1)+500){rt=(rt+1)%ROUTES.length; t0=now; $('#netlog').innerHTML='&gt; '+ROUTES[rt].log}
  if(!$('#v-inicio').hidden) drawNet(now);
  requestAnimationFrame(loop);
}
$('#netlog').innerHTML='&gt; '+ROUTES[0].log;
netColors();
if(document.fonts&&document.fonts.ready) document.fonts.ready.then(()=>drawNet(performance.now()));
if(!reduce) requestAnimationFrame(n=>{t0=n;loop(n)}); else {t0=performance.now()-450; drawNet(performance.now())}
matchMedia('(prefers-color-scheme: dark)').addEventListener('change',netColors);

/* ---------- rotas ---------- */
function show(id){document.querySelectorAll('.view').forEach(v=>v.hidden=v.id!==id)}
function navCur(name){document.querySelectorAll('[data-nav]').forEach(a=>a.toggleAttribute('aria-current',a.dataset.nav===name)); document.querySelectorAll('[data-nav]').forEach(a=>{if(a.getAttribute('aria-current')==='') a.setAttribute('aria-current','page')})}
function setTrackNav(t){
  ctxTrack=t||null; const g=$('#navGloss'); g.hidden=!t; if(t) g.href='#t/'+t.id+'/glossario';
  const bt=$('#brandTrack'); bt.hidden=!t; if(t){bt.textContent=t.short; bt.href='#t/'+t.id}
  updMeter();
}
function route(soft){
  let h=decodeURIComponent(location.hash.slice(1))||'inicio';
  const legacy=h.match(/^m-(\d+)(-t-[\d-]+)?$/); if(legacy){location.replace('#t/fundamentos/'+h); return}
  if(h==='glossario'){location.replace('#t/fundamentos/glossario'); return}
  const keepScroll=soft===true;
  if(h==='sobre'){show('v-sobre'); setTrackNav(null); navCur('sobre'); renderAbout(); if(!keepScroll) window.scrollTo(0,0); return}
  if(h==='simulado'){show('v-simulado'); setTrackNav(null); navCur('simulado'); if(SIM.cur&&SIM.cur.done&&!soft) renderSimResult(); else if(!(soft&&SIM.cur&&!SIM.cur.done)) renderSim(); if(!keepScroll) window.scrollTo(0,0); return}
  const tm=h.match(/^t\/([\w-]+)(?:\/(.*))?$/);
  if(tm&&TRK[tm[1]]){
    const t=TRK[tm[1]], sub=tm[2]||''; setTrackNav(t);
    if(sub==='glossario'){show('v-glossario'); navCur('glossario'); renderGloss(t); if(!keepScroll) window.scrollTo(0,0); return}
    const mm=sub.match(/^m-(\d+)(?:-t-([\d-]+))?$/);
    if(mm){show('v-mod'); navCur(''); if(soft&&cur.t===t&&cur.m===+mm[1]){const m=t.MODS[cur.m-1]; $('#v-mod').querySelectorAll('.prose[data-k]').forEach(b=>HL.render(t,b)); refreshMod(t,m); renderEx(t,m); return} renderMod(t,+mm[1],mm[2]?mm[2].replace(/-/g,'.'):null); return}
    show('v-trilha'); navCur(''); renderTrack(t); if(!keepScroll) window.scrollTo(0,0); return;
  }
  show('v-inicio'); setTrackNav(null); navCur(''); renderHome(); netColors(); if(!keepScroll) window.scrollTo(0,0);
}
window.addEventListener('hashchange',()=>route());
Sync.init(); Sync.paint(); route(); updMeter();
})();
