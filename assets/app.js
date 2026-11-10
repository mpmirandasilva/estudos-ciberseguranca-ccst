/* Estudos de Cibersegurança · Certificação CCST — app de estudo (HTML, CSS e JS puros).
   Dados: window.TRACKS (um arquivo por trilha em /data). Progresso: localStorage por trilha,
   sincronizado com a conta Google quando o Firebase está configurado (firebase-config.js). */
(function(){
'use strict';
const TR=(window.TRACKS||[]).slice().sort((a,b)=>a.order-b.order);
const TRK={}; TR.forEach(t=>TRK[t.id]=t);
const CYDOM={1:'Princípios essenciais de segurança',2:'Conceitos básicos de segurança de rede',3:'Segurança de endpoints',4:'Avaliação de vulnerabilidades e riscos',5:'Tratamento de incidentes'};
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
/* ---------- trilhas reorganizadas: leva grifos, textos editados e progresso para a nova numeração (uma vez) ---------- */
const Reorg={busy:{},
  rmap(t,s){const M=t.MIG, one=x=>M.idmap[x]||M.modmap[x]||x;
    s=s.replace(/((?:ver )?(?:item|itens) )(\d+(?:\.\d+)+(?:(?:, | e )\d+(?:\.\d+)+)*)/g,(m,p,ids)=>p+ids.replace(/\d+(?:\.\d+)*/g,one));
    s=s.replace(/((?:ver )?(?:seção|seções|módulo|módulos) )(\d+(?:(?:, | e | a )\d+)*)(?![\d.])/g,(m,p,ids)=>p+ids.replace(/\d+/g,k=>M.modmap[k]||k));
    return s.replace(/vista na seção/g,'explicada na seção').replace(/visto na seção/g,'explicado na seção')},
  text(html){const d=document.createElement('div'); d.innerHTML=html; return HL.nodes(d).map(n=>n.data).join('')},
  segs(a,b){const out=[]; let i=0,j=0;
    while(i<a.length&&j<b.length){
      if(a[i]===b[j]){const s=i,u=j; while(i<a.length&&j<b.length&&a[i]===b[j]){i++;j++} out.push([s,i,u]); continue}
      let f=null; for(let d=1;d<=120&&!f;d++) for(let x=0;x<=d&&!f;x++){const y=d-x; if(i+x<a.length&&a.substr(i+x,10)===b.substr(j+y,10)) f=[x,y]}
      if(!f) break; i+=f[0]; j+=f[1]}
    return out},
  pos(seg,p,end){for(const [a,b,c] of seg) if(p>=a&&p<=b) return c+(p-a);
    if(end){let r=null; for(const [a,b,c] of seg) if(b<=p) r=c+(b-a); return r}
    for(const [a,b,c] of seg) if(a>=p) return c; return null},
  ranges(seg,add){return (add||[]).map(r=>({s:this.pos(seg,r.s,false),e:this.pos(seg,r.e,true)})).filter(r=>r.s!==null&&r.e!==null&&r.e>r.s)},
  hl(x,h){return {add:this.ranges(x.seg,h.add),off:(h.off||[]).map(i=>x.mk[i]).filter(i=>i>=0),ts:h.ts||0}},
  /* progresso de cada pessoa (tópicos lidos, respostas, último módulo) */
  prog(t,S){const M=t.MIG; if(!M||!S||(S.mv||1)>=M.v) return false;
    const o={}; Object.keys(S.open||{}).forEach(k=>(M.open[k]||[]).forEach(n=>o[n]=1)); S.open=o;
    const e={}; Object.entries(S.ex||{}).forEach(([k,r])=>{const n=M.ex[k]; if(n) e[n]=r}); S.ex=e;
    if(S.hl){const h={}; Object.entries(S.hl).forEach(([k,v])=>{const x=M.hl[k]; if(x&&v) h[x.to]=this.hl(x,v)}); S.hl=h}
    if(S.last) S.last=+(M.modmap[String(S.last)]||1);
    S.mv=M.v; return true},
  /* grifos e textos editados publicados pela dona do site (conteudo/<trilha>) */
  pending(t){const M=t.MIG; return !!M&&(((Pub.data[t.id]||{}).kv||{}).v||1)<M.v},
  conv(t,d){const M=t.MIG, k={}, lost=[];
    Object.entries(d||{}).forEach(([key,val])=>{
      if(key==='kv'||!val) return; const old=key.slice(1).replace(/_/g,'.'), x=M.hl[old];
      if(!x){lost.push(old); return}
      const o={ts:val.ts||Date.now()};
      if(typeof val.html==='string'){
        o.html=this.rmap(t,val.html);
        if(val.hl){const sg=this.segs(this.text(val.html),this.text(o.html)); o.hl={add:this.ranges(sg,val.hl.add),off:(val.hl.off||[]).slice()}}
      } else if(val.hl) o.hl=this.hl(x,val.hl);
      if(o.hl&&!o.hl.add.length&&!o.hl.off.length) delete o.hl;
      if(o.html!==undefined||o.hl) k[PK(x.to)]=o});
    return {k,lost}},
  /* enquanto a dona não abre o site, os visitantes já veem os grifos no lugar novo (só na tela) */
  cache:{},
  view(t){const js=Pub.last[t.id]; const c=this.cache[t.id]; if(c&&c.js===js) return c.k; const k=this.conv(t,Pub.data[t.id]).k; this.cache[t.id]={js,k}; return k},
  pub(t){const M=t.MIG; if(!this.pending(t)||!HL.enabled()||!Pub.loaded[t.id]||this.busy[t.id]||!Sync.db) return;
    this.busy[t.id]=true; const d=Pub.data[t.id]||{}, {k,lost}=this.conv(t,d);
    k.kv={v:M.v,ts:Date.now()};
    store(PKEY(t.id)+'-antes-v'+M.v,d);
    const ref=Sync.db.collection('conteudo'), FV=firebase.firestore.FieldValue;
    ref.doc(t.id+'-antes-v'+M.v).set({k:d,updated:FV.serverTimestamp()}).catch(()=>{})
      .then(()=>ref.doc(t.id).set({k,updated:FV.serverTimestamp()}))
      .then(()=>{this.busy[t.id]=false; Pub.data[t.id]=k; Pub.last[t.id]=JSON.stringify(k); store(PKEY(t.id),k); Pub.refresh(t); toast('Grifos e textos editados de '+t.short+' levados para a nova ordem do curso.'+(lost.length?' Sem lugar novo: '+lost.join(', ')+'.':''))})
      .catch(e=>{this.busy[t.id]=false; toast('Não foi possível ajustar os grifos à nova ordem: '+(e.code||e.message))});
  }
};
const ST={}; TR.forEach(t=>{ST[t.id]=Object.assign({open:{},ex:{},last:null,lastTs:0},load(keyOf(t.id))||{})});
TR.forEach(t=>{if(Reorg.prog(t,ST[t.id])) store(keyOf(t.id),ST[t.id])});
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
  const pi=$('#pvIco'); if(pi&&PV){pi.innerHTML=pixSvg(PV.ICON); const ph=PRV.hist[PRV.hist.length-1], pc=PRV.cur;
    $('#pvSub').textContent=pc&&!pc.done?`Rodada em andamento: ${Object.keys(pc.ans).length} de ${pc.order.length} respondidas.`:ph?`Última rodada: ${ph.ok}/${ph.n} (${Math.round(ph.ok/ph.n*100)}%) em ${new Date(ph.end).toLocaleDateString('pt-BR')}.`:`${PV.Q.length} questões da apostila, com correção comentada e índice de onde estudar cada assunto. A nota sai no final.`}
  const tm=TR.reduce((a,t)=>a+t.MODS.length,0), tt=TR.reduce((a,t)=>a+t.TOTALT,0), tq=TR.reduce((a,t)=>a+t.TOTALQ,0);
  $('#stats').innerHTML=[statBox(TR.length,'trilhas'),statBox(tm,'módulos'),statBox(tq,'exercícios'),statBox(Math.round(overall()*100)+'%','seu progresso')].join('');
  $('#tracks').innerHTML=TR.map(t=>{
    const x=trackTotals(t); const qok=x.k;
    return `<a class="frame track" href="#t/${t.id}">
      <div class="th"><div class="ico">${pixSvg(t.icon)}</div><div><div class="label">${esc(t.label)}</div><h3>${esc(t.title)}</h3></div></div>
      <p>${esc(t.desc)}</p>
      <div class="meta"><span class="chip">${t.MODS.length} módulos</span><span class="chip">${t.TOTALT} tópicos</span><span class="chip">${t.TOTALQ} exercícios</span>${t.HOURS?`<span class="chip" title="Tempo estimado de estudo: leitura dos tópicos e exercícios">≈ ${t.HOURS} h de estudo</span>`:''}</div>
      <div class="bars"><div><span>Tópicos ${x.o}/${t.TOTALT}</span>${seg(x.o/(t.TOTALT||1))}<em>${Math.round(x.o/(t.TOTALT||1)*100)}%</em></div>
      <div><span>Acertos ${qok}/${t.TOTALQ}</span>${seg(qok/(t.TOTALQ||1),'ex')}<em>${Math.round(qok/(t.TOTALQ||1)*100)}%</em></div></div>
      <span class="go">${x.o||x.a?'Continuar a trilha ▸':'Começar a trilha ▸'}</span></a>`}).join('');
  const last=TR.map(t=>({t,ts:ST[t.id].lastTs||0,m:ST[t.id].last})).filter(x=>x.m).sort((a,b)=>b.ts-a.ts)[0];
  const box=$('#continueBox');
  box.innerHTML=last?`<a class="btn" href="#t/${last.t.id}/m-${last.m}">Continuar: ${esc(last.t.short)}, módulo ${last.m} ▸</a><a class="btn ghost" href="#simulado">Simulado CCST</a>`
    :`<a class="btn" href="#t/${TR[0].id}">Começar pela trilha 1 ▸</a><a class="btn ghost" href="#simulado">Simulado CCST</a>`;
  const h=SIM.hist[SIM.hist.length-1];
  $('#simSub').textContent=h?`Último simulado: ${h.ok}/${h.n} (${Math.round(h.ok/h.n*100)}%) em ${new Date(h.end).toLocaleDateString('pt-BR')}.`:'Questões das trilhas de redes no formato da prova CCST Networking, com tempo e resultado por domínio do blueprint.';
}

/* ---------- trilha ---------- */
function renderTrack(t){
  const x=trackTotals(t);
  const v=$('#v-trilha');
  v.innerHTML=`<div class="crumbs"><a href="#inicio">Início</a><span>/</span><span>${esc(t.short)}</span></div>
   <div class="mod-head"><div class="frame big">${pixSvg(t.icon)}</div><div><div class="label">${esc(t.label)}</div><h1>${esc(t.title)}</h1></div></div>
   <p class="lead" style="margin:-6px 0 22px">${esc(t.desc)}${t.HOURS?`<br><span class="label" style="display:inline-block;margin-top:10px">Tempo estimado: cerca de ${t.HOURS} horas, entre leitura e exercícios</span>`:''}</p>
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
        ${m.intro?`<div class="frame intro prose" data-k="m${idx}" style="border-top:2px solid var(--edge)">${boxHtml(t,'m'+idx)}</div>`:''}
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
      <div class="card-b"><div><div class="prose" data-k="${x.num}">${boxHtml(t,x.num)}</div></div></div>`;
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

/* ---------- conteúdo publicado: edições e grifos da dona do site, visíveis para todos ----------
   Fica no Firestore em conteudo/<trilha> (leitura pública; só a conta ownerEmail grava).
   Cópia local em localStorage para abrir rápido e funcionar sem internet. */
const PKEY=id=>'redes-conteudo-'+id+'-v1';
const PK=k=>'k'+String(k).replace(/\./g,'_');
const Pub={data:{},loaded:{},last:{},
  init(db){
    TR.forEach(t=>db.collection('conteudo').doc(t.id).onSnapshot(snap=>{
      const d=(snap.exists&&snap.data().k)||{}; const js=JSON.stringify(d);
      this.loaded[t.id]=true;
      if(js!==this.last[t.id]){this.last[t.id]=js; this.data[t.id]=d; store(PKEY(t.id),d); this.refresh(t)}
      Migr.run();
    },()=>{}));
  },
  get(t,k){return ((Reorg.pending(t)?Reorg.view(t):this.data[t.id])||{})[PK(k)]||null},
  set(t,k,obj){
    const d=this.data[t.id]=this.data[t.id]||{}, key=PK(k), prev=d[key];
    if(!Sync.db||!Sync.user){toast('Sem conexão com a nuvem agora. Nada foi publicado; tente de novo em instantes.'); return Promise.resolve(false)}
    if(Reorg.pending(t)){toast('Aguarde um instante: os grifos estão sendo ajustados à nova ordem do curso.'); Migr.run(); return Promise.resolve(false)}
    if(obj){obj.ts=Date.now(); d[key]=obj} else delete d[key];
    this.last[t.id]=JSON.stringify(d); store(PKEY(t.id),d);
    const undo=()=>{if(prev) d[key]=prev; else delete d[key]; this.last[t.id]=JSON.stringify(d); store(PKEY(t.id),d)};
    const FV=firebase.firestore.FieldValue;
    return Sync.db.collection('conteudo').doc(t.id).set({k:{[key]:obj?obj:FV.delete()},updated:FV.serverTimestamp()},{merge:true})
      .then(()=>true).catch(e=>{undo(); toast('Não foi possível publicar: '+(e.code||e.message)); this.refresh(t); return false});
  },
  refresh(t){ if(Edit.box||cur.t!==t||$('#v-mod').hidden) return; $('#v-mod').querySelectorAll('.prose[data-k]').forEach(b=>paintBox(t,b)) }
};
TR.forEach(t=>{Pub.data[t.id]=load(PKEY(t.id))||{}; Pub.last[t.id]=JSON.stringify(Pub.data[t.id])});
function origHtml(t,k){
  if(/^m\d+$/.test(k)) return (t.MODS[+k.slice(1)-1]||{}).intro||'';
  const m=t.MODS[(t.topicMod[k]||0)-1]; const x=m&&m.topics.find(y=>y.num===k); return x?x.html:'';
}
function boxHtml(t,k){const p=Pub.get(t,k); return p&&typeof p.html==='string'?p.html:origHtml(t,k)}
function paintBox(t,b){b.innerHTML=boxHtml(t,b.dataset.k); HL.render(t,b)}
/* Leva para o site público os grifos que a dona tinha feito quando eles eram pessoais (uma vez só). */
const Migr={busy:{},run(){
  if(!HL.enabled()) return;
  TR.forEach(t=>Reorg.pub(t));
  TR.forEach(t=>{const S=ST[t.id]; if(Reorg.pending(t)||S.hlMig||!Pub.loaded[t.id]||Migr.busy[t.id]) return; Migr.busy[t.id]=true;
    const jobs=[]; Object.entries(S.hl||{}).forEach(([k,h])=>{ if(!h||(!(h.add||[]).length&&!(h.off||[]).length)||Pub.get(t,k)) return; jobs.push(Pub.set(t,k,{hl:{add:h.add||[],off:h.off||[]}})) });
    Promise.all(jobs).then(r=>{Migr.busy[t.id]=false; if(r.every(Boolean)){S.hlMig=1; save(t.id)} if(jobs.length) Pub.refresh(t)});
  });
}};
/* ---------- grifos (a dona grifa; todos veem) ---------- */
const HL={
  enabled(){const o=(window.FIREBASE_CONFIG||{}).ownerEmail; return !!(o&&Sync.user&&Sync.user.email&&Sync.user.email.toLowerCase()===o.toLowerCase())},
  get(t,k){const p=Pub.get(t,k), h=p&&p.hl; return h?{add:(h.add||[]).map(r=>({s:r.s,e:r.e})),off:(h.off||[]).slice()}:{add:[],off:[]}},
  put(t,k,h){const p=Pub.get(t,k)||{}, o={}; if(typeof p.html==='string') o.html=p.html; if(h.add.length||h.off.length) o.hl={add:h.add,off:h.off}; Pub.set(t,k,(o.html!==undefined||o.hl)?o:null)},
  nodes(root){const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode:n=>n.parentElement&&n.parentElement.closest('svg,.hl-foot')?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT}); const a=[]; let n; while((n=w.nextNode())) a.push(n); return a},
  render(t,box){
    const on=this.enabled(); document.body.classList.toggle('can-hl',on);
    const k=box.dataset.k, h=this.get(t,k), p=Pub.get(t,k), edited=!!(p&&typeof p.html==='string');
    box.querySelectorAll('mark.u').forEach(mk=>mk.replaceWith(...mk.childNodes)); box.normalize();
    box.querySelectorAll('mark:not(.u)').forEach((mk,i)=>{mk.dataset.b=i; mk.classList.toggle('off',h.off.includes(i))});
    h.add.forEach((r,j)=>this.wrap(box,r.s,r.e,j));
    let f=box.querySelector('.hl-foot'); if(f) f.remove();
    if(!on) return;
    f=document.createElement('div'); f.className='hl-foot';
    f.innerHTML=`<button type="button" class="btn ghost sm" data-a="edit">Editar texto</button>`
      +(edited?'<span>texto editado</span><button type="button" class="linkbtn" data-a="orig">voltar ao texto original</button>':'')
      +(h.add.length?'<button type="button" class="linkbtn" data-a="clear">apagar os grifos novos</button>':'')
      +(h.off.length?'<button type="button" class="linkbtn" data-a="restore">restaurar os grifos originais</button>':'');
    f.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{
      const a=b.dataset.a;
      if(a==='edit'){Edit.start(t,box); return}
      if(a==='orig'){ if(!b.dataset.ok){b.dataset.ok=1; b.textContent='confirmar: voltar ao original?'; setTimeout(()=>{if(b.isConnected){delete b.dataset.ok; b.textContent='voltar ao texto original'}},5000); return}
        Pub.set(t,k,null); paintBox(t,box); toast('Texto original restaurado.'); return}
      const x=this.get(t,k); if(a==='clear') x.add=[]; else x.off=[]; this.put(t,k,x); this.render(t,box)}));
    box.appendChild(f);
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
    if(!box||box.isContentEditable||!box.closest('#v-mod')||box.closest('.card:not(.open)')) return null;
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
    const check=()=>{if(!this.enabled()){this.hide();return} const i=this.selInfo(); if(!i){ if(this.ctx&&this.ctx.sel) this.hide(); return }
      const h=this.get(cur.t,i.box.dataset.k); const base=this.baseIn(i.box,i.s,i.e); const anyU=h.add.some(r=>r.e>i.s&&r.s<i.e);
      this.ctx={box:i.box,s:i.s,e:i.e,base,sel:true};
      this.showBar(i.rect,[['add','Grifar'],...((anyU||base.length)?[['del','Apagar grifo']]:[])]);};
    let tm=null; document.addEventListener('selectionchange',()=>{clearTimeout(tm); tm=setTimeout(check,matchMedia('(pointer:coarse)').matches?450:120)});
    document.addEventListener('click',e=>{
      if(e.target.closest('.hl-bar')) return;
      if(!this.enabled()){this.hide();return}
      const mk=e.target.closest('#v-mod .prose[data-k] mark'); const sel=getSelection(); if(mk&&mk.closest('.prose').isContentEditable) return;
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
/* ---------- editor de texto (só a dona) ---------- */
function cleanHtml(src){
  const d=document.createElement('div'); d.innerHTML=src;
  d.querySelectorAll('script,style,iframe,object,embed,link,meta,form,input,button,.hl-foot,.ed-bar').forEach(e=>e.remove());
  d.querySelectorAll('*').forEach(el=>{ const inSvg=!!el.closest('svg');
    [...el.attributes].forEach(a=>{const n=a.name.toLowerCase();
      if(n.startsWith('on')||n==='contenteditable'||n==='spellcheck'||(n.startsWith('data-')&&!inSvg)||(n==='style'&&!inSvg)) el.removeAttribute(a.name);
      else if(/(^|:)(href|src)$/.test(n)&&/^\s*(javascript|data):/i.test(a.value)) el.removeAttribute(a.name)});
    if(!inSvg&&el.tagName==='MARK') el.removeAttribute('class');
  });
  const ren=(sel,tag)=>d.querySelectorAll(sel).forEach(el=>{const n=document.createElement(tag); while(el.firstChild) n.appendChild(el.firstChild); el.replaceWith(n)});
  ren('b','strong'); ren('i','em');
  d.querySelectorAll('font').forEach(el=>el.replaceWith(...el.childNodes));
  d.querySelectorAll('span:not([class])').forEach(el=>{ if(!el.closest('svg')&&!el.closest('.flow')) el.replaceWith(...el.childNodes)});
  d.querySelectorAll('mark mark').forEach(el=>el.replaceWith(...el.childNodes));
  d.querySelectorAll('mark,strong,em').forEach(el=>{if(!el.textContent.trim()&&!el.querySelector('img,svg')) el.replaceWith(...el.childNodes)});
  [...d.childNodes].forEach(n=>{ if(n.nodeType===1&&n.tagName==='DIV'&&!n.className){const p=document.createElement('p'); while(n.firstChild) p.appendChild(n.firstChild); n.replaceWith(p)}
    else if(n.nodeType===3&&n.textContent.trim()){const p=document.createElement('p'); n.replaceWith(p); p.appendChild(n)} else if(n.nodeType===3) n.remove()});
  d.querySelectorAll('p').forEach(p=>{if(!p.textContent.trim()&&!p.querySelector('img,svg')) p.remove()});
  d.normalize(); return d.innerHTML.trim();
}
const Edit={box:null,t:null,k:null,bar:null,
  start(t,box){
    if(this.box) this.cancel(); HL.hide();
    this.t=t; this.box=box; this.k=box.dataset.k;
    box.querySelectorAll('.hl-foot').forEach(f=>f.remove());
    box.querySelectorAll('mark.off').forEach(mk=>mk.replaceWith(...mk.childNodes));
    box.querySelectorAll('mark').forEach(mk=>{mk.removeAttribute('class'); mk.removeAttribute('data-u'); mk.removeAttribute('data-b')});
    box.querySelectorAll('mark mark').forEach(mk=>mk.replaceWith(...mk.childNodes)); box.normalize();
    box.querySelectorAll('svg,figure,img').forEach(el=>el.setAttribute('contenteditable','false'));
    const bar=this.bar=document.createElement('div'); bar.className='ed-bar frame'; bar.setAttribute('role','toolbar'); bar.setAttribute('aria-label','Editar texto');
    bar.innerHTML=`<span class="ed-l">Editando</span>
      <button type="button" data-c="bold" title="Negrito (Ctrl+B)"><b>N</b></button>
      <button type="button" data-c="italic" title="Itálico (Ctrl+I)"><i>I</i></button>
      <button type="button" data-c="mark" class="ed-mk" title="Grifar o trecho selecionado">Grifar</button>
      <button type="button" data-c="unmark" title="Tirar o grifo do trecho selecionado">Tirar grifo</button>
      <button type="button" data-c="ul" title="Lista com marcadores">• Lista</button>
      <button type="button" data-c="undo" title="Desfazer (Ctrl+Z)">Desfazer</button>
      <span class="ed-sp"></span>
      <button type="button" data-c="cancel">Cancelar</button>
      <button type="button" data-c="save" class="ed-save">Salvar</button>`;
    bar.addEventListener('mousedown',e=>{if(e.target.closest('button')) e.preventDefault()});
    bar.addEventListener('click',e=>{const b=e.target.closest('button'); if(b) this.cmd(b.dataset.c)});
    box.parentNode.insertBefore(bar,box);
    box.contentEditable='true'; box.spellcheck=true; box.classList.add('editing');
    try{document.execCommand('defaultParagraphSeparator',false,'p')}catch(e){}
    box.addEventListener('paste',this.onPaste);
    box.focus(); bar.scrollIntoView({behavior:'smooth',block:'nearest'});
  },
  onPaste(e){e.preventDefault(); const tx=(e.clipboardData||window.clipboardData).getData('text/plain'); document.execCommand('insertText',false,tx)},
  inBox(){const sel=getSelection(); if(!sel||!sel.rangeCount) return null; const rg=sel.getRangeAt(0); return this.box.contains(rg.commonAncestorContainer)?rg:null},
  cmd(c){
    const box=this.box; if(!box) return;
    if(c==='save') return this.save(); if(c==='cancel') return this.cancel();
    if(c==='bold'||c==='italic'||c==='undo'){document.execCommand(c); return}
    if(c==='ul'){document.execCommand('insertUnorderedList'); return}
    const rg=this.inBox(); if(!rg||rg.collapsed){toast('Selecione o trecho primeiro.'); return}
    if(c==='mark'){ const s=HL.offset(box,rg.startContainer,rg.startOffset), e=HL.offset(box,rg.endContainer,rg.endOffset);
      HL.wrap(box,s,e,0); box.querySelectorAll('mark.u').forEach(m=>{m.removeAttribute('class'); m.removeAttribute('data-u')});
      box.querySelectorAll('mark mark').forEach(m=>m.replaceWith(...m.childNodes)); box.normalize(); getSelection().removeAllRanges(); return}
    if(c==='unmark'){ box.querySelectorAll('mark').forEach(m=>{if(rg.intersectsNode(m)) m.replaceWith(...m.childNodes)}); box.normalize(); return}
  },
  close(){const box=this.box; if(!box) return; box.removeEventListener('paste',this.onPaste); box.removeAttribute('contenteditable'); box.classList.remove('editing'); if(this.bar) this.bar.remove(); this.bar=null; this.box=null},
  cancel(){const t=this.t, box=this.box; this.close(); if(box) paintBox(t,box)},
  save(){
    const t=this.t, k=this.k, box=this.box;
    if(!box.textContent.trim()){toast('O texto ficou vazio. Use "Cancelar" ou escreva algo antes de salvar.'); return}
    const html=cleanHtml(box.innerHTML), orig=cleanHtml(origHtml(t,k)); const sv=this.bar&&this.bar.querySelector('.ed-save');
    if(sv){sv.disabled=true; sv.textContent='Salvando…'}
    Pub.set(t,k,html===orig?null:{html}).then(ok=>{
      if(ok){this.close(); paintBox(t,box); toast('Texto salvo e publicado no site.')}
      else if(sv){sv.disabled=false; sv.textContent='Salvar'}
    });
  }
};
addEventListener('beforeunload',e=>{if(Edit.box){e.preventDefault(); e.returnValue=''}});
addEventListener('hashchange',()=>{if(Edit.box) Edit.close()});


/* ---------- exercícios ---------- */
function renderEx(t,m){
  const box=$('#ex-box'); const qs=t.EX[m.idx]||[];
  const base=qs.map((q,i)=>[q,i]).filter(([q])=>!q.dom), cc=qs.map((q,i)=>[q,i]).filter(([q])=>q.dom);
  box.innerHTML=`<div class="ex-head"><div><div class="label">Fase final</div><h2>Exercícios do módulo ${m.idx}</h2><p>${cc.length?`${qs.length} questões: ${base.length} de fixação e ${cc.length} no estilo da prova CCST.`:`${qs.length} questões de fixação.`} Múltipla escolha corrige no clique; as demais, em "Verificar".</p></div>
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
function qHead(q,n){return `<div class="q-top"><span class="k">${pad(n)}</span><div class="txt">${esc(q.q)}</div><span class="kind">${kindOf(q)}</span>${q.dom?(q.cy?`<span class="kind ccst" title="Domínio ${q.dom} do blueprint CCST Cybersecurity: ${esc(CYDOM[q.dom])}">CCST Cyber ${q.dom}.0</span>`:`<span class="kind ccst" title="Domínio ${q.dom} do blueprint CCST Networking: ${esc(DOMAINS[q.dom])}">CCST ${q.dom}.0</span>`):''}</div>`}
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
function pool(){const p=[]; TR.forEach(t=>t.MODS.forEach(m=>(t.EX[m.idx]||[]).forEach((q,i)=>{if(q.dom&&!q.cy) p.push({tid:t.id,m:m.idx,i,d:q.dom})}))); return p}
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
    <p class="lead">Questões no formato da prova 100-150, sorteadas das trilhas de redes (1 e 2) e distribuídas pelos seis domínios do blueprint. Sem correção durante a prova: o resultado sai no final, por domínio, com explicação e o item para revisar.</p></div>
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

/* ---------- prova CCST Cybersecurity (trilha de teste) ----------
   Banco em window.PROVA (data/prova.js). Cada questão mostra a correção e "onde estudar" logo depois da resposta;
   a nota só aparece quando a rodada termina. Progresso em localStorage (PRKEY) e na nuvem (campo prova). */
const PV=window.PROVA||null, PRKEY='redes-prova-cyber-v1';
let PRV=Object.assign({hist:[],cur:null},load(PRKEY)||{});
function savePrv(){store(PRKEY,PRV); Sync.push()}
const PQ={}; if(PV) PV.Q.forEach(q=>PQ[q.n]=q);
function pvGrade(q,v){
  if(v==null) return false;
  if(q.t==='mc') return v===q.a[0];
  if(q.t==='ms') return Array.isArray(v)&&v.length===q.a.length&&q.a.every(x=>v.includes(x));
  return Array.isArray(v)&&q.f.every((f,j)=>v[j]===f.a);
}
function pvRefHtml(q){
  return `<div class="pv-refs"><div class="label">Onde estudar</div><ul>${q.refs.map(r=>{const x=PV.REFS[r]; if(!x) return '';
    return `<li><a href="#t/${x.t}/m-${x.m}-t-${x.num.replace(/\./g,'-')}" target="_blank" rel="noopener"><span class="chip">${esc(x.short)}</span> ${esc(x.num)} ${esc(x.title)}</a><span class="pv-mod">Trilha ${x.order} · módulo ${x.m}: ${esc(x.mt)}</span></li>`}).join('')}</ul></div>`;
}
function pvAnsText(q){
  if(q.t==='match') return q.f.map(f=>`${esc(f.l)} → <span class="pv-a">${esc(f.a)}</span>`).join('<br>');
  return q.a.map(i=>esc(q.o[i])).join(' · ');
}
function renderProva(){
  const v=$('#v-prova'); if(!PV){v.innerHTML='<p>Banco de questões indisponível.</p>'; return}
  const c=PRV.cur;
  if(c&&!c.done&&c.view!=='home') return renderProvaRun();
  const dc={}; PV.Q.forEach(q=>dc[q.d]=(dc[q.d]||0)+1);
  const hist=PRV.hist.slice(-8).reverse();
  const done=c?Object.keys(c.ans).length:0;
  v.innerHTML=`<div class="page-head"><div class="crumbs"><a href="#inicio">Início</a><span>/</span><span>Prova CCST Cybersecurity</span></div><h1>Prova CCST Cybersecurity</h1>
    <p class="lead">As ${PV.Q.length} questões da apostila, para treinar para a prova. Depois de cada resposta aparecem a correção, uma explicação e os tópicos das trilhas onde estudar o assunto. A nota só sai no final, com o resultado por domínio e um índice do que revisar.</p></div>
    <div class="about"><div class="frame">
      <h3>Como funciona</h3>
      <ul><li>Responda e confirme: a correção e o <b>onde estudar</b> aparecem na hora.</li><li>Os links abrem o tópico em outra aba, sem perder o lugar na prova.</li><li>Nada de nota parcial: o resultado aparece quando você termina (ou encerra) a rodada.</li><li>Questões de múltipla seleção só contam se todas as alternativas certas forem marcadas.</li></ul>
      <div class="actions" style="margin-top:14px">${c&&!c.done?`<button class="btn" id="pvCont" type="button">Continuar a rodada (${done}/${c.order.length}) ▸</button>`:''}
        <button class="btn${c&&!c.done?' ghost':''}" id="pvAll" type="button">Todas as ${PV.Q.length}, em ordem aleatória</button>
        <button class="btn ghost" id="pvSeq" type="button">Todas, na ordem da apostila</button>
        <button class="btn ghost" id="pvShort" type="button">Rodada curta: 50 sorteadas</button></div>
      ${c&&!c.done?'<p class="hint" style="margin-top:10px">Começar outra rodada descarta a atual.</p>':''}
    </div><div class="frame"><h3>Questões por domínio do exame</h3><div class="dom-rows">${Object.entries(PV.DOMAINS).map(([d,n])=>`<div class="dom-row"><span>${d}.0 ${esc(n)}</span>${seg((dc[d]||0)/Math.max(...Object.values(dc),1))}<em>${dc[d]||0}</em></div>`).join('')}</div>
    ${hist.length?`<h3 style="margin-top:18px">Suas últimas rodadas</h3><table class="hist"><tr><th>Data</th><th>Acertos</th><th>%</th></tr>${hist.map(h=>`<tr><td>${new Date(h.end).toLocaleString('pt-BR',{dateStyle:'short',timeStyle:'short'})}</td><td>${h.ok}/${h.n}</td><td>${Math.round(h.ok/h.n*100)}%</td></tr>`).join('')}</table>`:''}
    </div></div>
    ${c&&c.done?`<div style="margin-top:22px"><button class="btn ghost" id="pvLast" type="button">Ver o resultado da última rodada</button></div>`:''}`;
  const start=mode=>{
    let ord=PV.Q.map(q=>q.n); const r=seeded('pv'+Date.now());
    if(mode!=='seq') ord=ord.map(n=>[r(),n]).sort((a,b)=>a[0]-b[0]).map(x=>x[1]);
    if(mode==='short') ord=ord.slice(0,50);
    PRV.cur={id:Date.now(),start:Date.now(),order:ord,ans:{},pos:0,done:false}; savePrv(); renderProvaRun(); window.scrollTo(0,0)};
  $('#pvAll').addEventListener('click',()=>start('all'));
  $('#pvSeq').addEventListener('click',()=>start('seq'));
  $('#pvShort').addEventListener('click',()=>start('short'));
  const k=$('#pvCont'); if(k) k.addEventListener('click',()=>{delete PRV.cur.view; renderProvaRun()});
  const l=$('#pvLast'); if(l) l.addEventListener('click',()=>renderProvaResult());
}
function renderProvaRun(){
  const v=$('#v-prova'); const c=PRV.cur; const N=c.order.length; c.pos=Math.max(0,Math.min(c.pos||0,N-1));
  const n=c.order[c.pos], q=PQ[n], ans=c.ans[n], answered=ans!=null, total=Object.keys(c.ans).length;
  v.innerHTML=`<div class="frame sim-top pv-top"><div><div class="label">Prova CCST Cybersecurity · questão ${c.pos+1} de ${N} · respondidas ${total} de ${N}</div><div class="pv-prog">${seg(total/N)}<label>Ir para <input id="pvJump" type="number" min="1" max="${N}" value="${c.pos+1}" inputmode="numeric"></label></div></div><div style="display:flex;gap:10px;align-items:center"><button class="btn ghost sm" id="pvOut" type="button">Sair</button><button class="btn sm" id="pvEnd" type="button">Encerrar e ver a nota</button></div></div>
   <div class="frame q" id="pvQ"><div class="q-top"><span class="k">${pad(c.pos+1)}</span><div class="txt">${esc(q.q)}</div><span class="kind">${q.t==='ms'?'escolha '+q.a.length:q.t==='match'?(q.f.length>1?'associação':'complete'):'escolha 1'}</span><span class="kind ccst" title="${esc(PV.DOMAINS[q.d])}">Domínio ${q.d}</span></div><div class="body"></div><div id="pvFb"></div></div>
   <div class="sim-nav"><button class="btn ghost" id="pvPrev" type="button" ${c.pos?'':'disabled'}>◂ Anterior</button><button class="btn" id="pvOk" type="button" ${answered?'hidden':''} disabled>Responder</button><button class="btn" id="pvNext" type="button" ${answered?'':'hidden'}>${c.pos<N-1?'Próxima ▸':'Ver a nota ▸'}</button></div>`;
  $('#pvJump').addEventListener('change',e=>{const k=Math.max(1,Math.min(N,parseInt(e.target.value,10)||1)); c.pos=k-1; savePrv(); renderProvaRun()});
  const body=$('#pvQ .body'), okBtn=$('#pvOk'); let cur=null;
  if(q.t!=='match'){
    const multi=q.t==='ms'; const opts=shuffled(q.o,c.id+'-'+n);
    body.innerHTML=`<div class="opts">${opts.map(([tx,orig],k)=>`<button type="button" class="opt" data-o="${orig}">${multi?'<span class="box"></span>':''}<span class="l">${'ABCDEFGH'[k]}</span><span>${esc(tx)}</span></button>`).join('')}</div>${multi?`<span class="sync">selecione ${q.a.length}</span>`:''}`;
    const btns=[...body.querySelectorAll('.opt')]; const sel=new Set(answered?(multi?ans:[ans]):[]);
    const paint=()=>btns.forEach(b=>b.classList.toggle('sel',sel.has(+b.dataset.o)));
    if(!answered) btns.forEach(b=>b.addEventListener('click',()=>{const o=+b.dataset.o;
      if(multi){ if(sel.has(o)) sel.delete(o); else{ if(sel.size>=q.a.length) return; sel.add(o)} cur=sel.size===q.a.length?[...sel].sort((a,b)=>a-b):null }
      else{ sel.clear(); sel.add(o); cur=o } okBtn.disabled=cur==null; paint()}));
    paint();
    if(answered){ btns.forEach(b=>{const o=+b.dataset.o; b.disabled=true; if(q.a.includes(o)) b.classList.add('right'); else if(sel.has(o)) b.classList.add('wrong')}) }
  } else {
    body.innerHTML=`<div class="fields">${q.f.map((f,k)=>{const id=`pv-${n}-${k}`; return `<div class="field"><label for="${id}">${esc(f.l)}</label><select id="${id}"><option value="">Escolha…</option>${shuffled(q.ch,c.id+'-'+n+'-'+k).map(([x])=>`<option>${esc(x)}</option>`).join('')}</select></div>`}).join('')}</div>`;
    const sels=[...body.querySelectorAll('select')];
    if(answered){ sels.forEach((s,k)=>{s.value=ans[k]||''; s.disabled=true; s.closest('.field').classList.add(ans[k]===q.f[k].a?'ok':'bad')}) }
    else sels.forEach(s=>s.addEventListener('change',()=>{const vals=sels.map(x=>x.value); cur=vals.every(x=>x)?vals:null; okBtn.disabled=cur==null}));
  }
  const showFb=()=>{const a=c.ans[n]; const ok=pvGrade(q,a);
    $('#pvFb').innerHTML=`<div class="fb ${ok?'ok':'bad'}"><b>${ok?'Correto!':'Não foi dessa vez'}</b><span>${q.t==='match'?'Respostas:<br>':'Resposta: '}${pvAnsText(q)}</span><span>${esc(q.e)}</span></div>${pvRefHtml(q)}`};
  if(answered) showFb();
  okBtn.addEventListener('click',()=>{ if(cur==null) return; c.ans[n]=cur; savePrv(); renderProvaRun(); const fb=$('#pvFb'); if(fb) fb.scrollIntoView({behavior:'smooth',block:'nearest'}) });
  $('#pvNext').addEventListener('click',()=>{ if(c.pos<N-1){c.pos++; savePrv(); renderProvaRun(); window.scrollTo(0,0)} else finishProva() });
  $('#pvPrev').addEventListener('click',()=>{c.pos--; savePrv(); renderProvaRun(); window.scrollTo(0,0)});
  $('#pvOut').addEventListener('click',()=>{c.view='home'; renderProva(); delete c.view; window.scrollTo(0,0)});
  $('#pvEnd').addEventListener('click',()=>{
    const open=N-Object.keys(c.ans).length; const box=document.createElement('div'); box.className='frame q'; box.style.marginTop='14px';
    box.innerHTML=`<b>Encerrar a rodada e ver a nota?</b><span>${open?`Ainda faltam ${open} questão(ões); elas contam como erro.`:'Todas as questões foram respondidas.'}</span><div class="actions"><button class="btn" type="button" id="yes">Encerrar agora</button><button class="btn ghost" type="button" id="no">Continuar</button></div>`;
    v.appendChild(box); box.scrollIntoView({behavior:'smooth'});
    $('#yes',box).addEventListener('click',finishProva); $('#no',box).addEventListener('click',()=>box.remove());
  });
}
function finishProva(){
  const c=PRV.cur; if(!c) return renderProva(); if(c.done) return renderProvaResult();
  c.done=true; c.end=Date.now(); const byDom={}; let ok=0;
  c.order.forEach(n=>{const q=PQ[n]; const g=pvGrade(q,c.ans[n]); if(g) ok++; const b=byDom[q.d]=byDom[q.d]||{n:0,ok:0}; b.n++; if(g) b.ok++});
  PRV.hist.push({id:c.id,end:c.end,n:c.order.length,ok,byDom}); PRV.hist=PRV.hist.slice(-50); savePrv(); renderProvaResult(); window.scrollTo(0,0);
}
function renderProvaResult(){
  const v=$('#v-prova'); const c=PRV.cur; if(!c||!c.done) return renderProva();
  const h=PRV.hist.find(x=>x.id===c.id)||{n:c.order.length,ok:0,byDom:{}}; const p=Math.round(h.ok/h.n*100);
  const wrong=c.order.filter(n=>!pvGrade(PQ[n],c.ans[n]));
  // índice de estudo: tópicos ligados às questões erradas, agrupados por trilha
  const cnt={}; wrong.forEach(n=>PQ[n].refs.forEach(r=>{cnt[r]=(cnt[r]||0)+1}));
  const byT={}; Object.entries(cnt).forEach(([r,k])=>{const x=PV.REFS[r]; if(!x) return; (byT[x.t]=byT[x.t]||{x,items:[]}).items.push([x,k,r])});
  const idx=Object.values(byT).sort((a,b)=>a.x.order-b.x.order).map(g=>{g.items.sort((a,b)=>a[0].m-b[0].m||a[0].num.localeCompare(b[0].num,undefined,{numeric:true}));
    return `<div class="pv-idx"><h3>Trilha ${g.x.order} · ${esc(g.x.track)}</h3><ul>${g.items.map(([x,k])=>`<li><a href="#t/${x.t}/m-${x.m}-t-${x.num.replace(/\./g,'-')}" target="_blank" rel="noopener">${esc(x.num)} ${esc(x.title)}</a><span class="pv-mod">módulo ${x.m}: ${esc(x.mt)}</span>${k>1?`<em>${k} questões</em>`:''}</li>`).join('')}</ul></div>`}).join('');
  v.innerHTML=`<div class="page-head"><div class="crumbs"><a href="#inicio">Início</a><span>/</span><a href="#prova" id="toPv">Prova CCST Cybersecurity</a><span>/</span><span>Resultado</span></div><h1>Resultado da rodada</h1></div>
   <div class="about"><div class="frame"><div class="label">Nota</div><div class="big-score">${p}%</div><p>${h.ok} de ${h.n} questões. ${p>=80?'Acima de 80%: bom sinal para a prova.':'Abaixo de 80%: use o índice abaixo para revisar os assuntos que erraram.'}</p>
     <div class="actions"><button class="btn" id="pvAgain" type="button">Nova rodada</button>${wrong.length?`<button class="btn ghost" id="pvRedo" type="button">Refazer as erradas e em branco (${wrong.length})</button>`:''}</div></div>
   <div class="frame"><h3>Por domínio do exame</h3><div class="dom-rows">${Object.entries(PV.DOMAINS).filter(([d])=>h.byDom[d]).map(([d,n])=>{const b=h.byDom[d]; return `<div class="dom-row"><span>${d}.0 ${esc(n)}</span>${seg(b.ok/b.n,b.ok/b.n<.8?'ex':'')}<em>${b.ok}/${b.n}</em></div>`}).join('')}</div></div></div>
   ${wrong.length?`<div class="sec-head" style="margin-top:26px"><div><div class="label">O que revisar</div><h2>Índice de estudo</h2></div></div><p class="lead" style="margin-top:-6px">Os tópicos das trilhas ligados às questões que você errou, na ordem das trilhas.</p><div class="frame pv-index">${idx}</div>`:''}
   <div class="sec-head" style="margin-top:26px"><div><div class="label">Correção</div><h2>Questões erradas ou em branco</h2></div></div><div id="pvRev" style="display:grid;gap:14px"></div>`;
  const rev=$('#pvRev');
  if(!wrong.length) rev.innerHTML='<p class="lead">Nenhuma. Parabéns!</p>';
  wrong.forEach(n=>{const q=PQ[n]; const a=c.ans[n]; const el=document.createElement('div'); el.className='frame q bad';
    const mine=a==null?'em branco':q.t==='match'?q.f.map((f,j)=>esc(a[j]||'—')).join(' · '):(Array.isArray(a)?a:[a]).map(i=>esc(q.o[i])).join(' · ');
    el.innerHTML=`<div class="q-top"><span class="k">${pad(c.order.indexOf(n)+1)}</span><div class="txt">${esc(q.q)}</div><span class="kind ccst">Domínio ${q.d}</span></div><div class="fb bad"><b>Sua resposta: ${mine}</b><span>${q.t==='match'?'Respostas:<br>':'Resposta: '}${pvAnsText(q)}</span><span>${esc(q.e)}</span></div>${pvRefHtml(q)}`;
    rev.appendChild(el)});
  $('#pvAgain').addEventListener('click',()=>{PRV.cur=null; savePrv(); renderProva(); window.scrollTo(0,0)});
  const rd=$('#pvRedo'); if(rd) rd.addEventListener('click',()=>{PRV.cur={id:Date.now(),start:Date.now(),order:wrong,ans:{},pos:0,done:false}; savePrv(); renderProvaRun(); window.scrollTo(0,0)});
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
      firebase.initializeApp(cfg); this.auth=firebase.auth(); this.db=firebase.firestore(); this.on=true; Pub.init(this.db);
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
    m.innerHTML=`<b style="font-size:14px">${esc(this.user.displayName||'Conta Google')}</b><span class="sync on" style="font-size:12px"><i></i>${esc(this.user.email||'')} · progresso sincronizado</span>${HL.enabled()?'<span class="sync on" style="font-size:12px"><i></i>modo de edição ativo: grifar e editar textos</span>':''}<button class="btn ghost sm" type="button" id="out">Sair</button>`;
    $('#acctBtn').parentElement.appendChild(m);
    $('#out',m).addEventListener('click',()=>{this.auth.signOut(); m.remove()});
    setTimeout(()=>document.addEventListener('click',function h(e){if(!m.contains(e.target)&&e.target.closest('#acctBtn')==null){m.remove();document.removeEventListener('click',h)}}),0);
  },
  onUser(u){
    this.user=u; this.paint(); if(this.unsub){this.unsub(); this.unsub=null}
    if(Edit.box&&!HL.enabled()) Edit.cancel();
    if(!$('#v-mod').hidden&&cur.t) $('#v-mod').querySelectorAll('.prose[data-k]').forEach(b=>HL.render(cur.t,b));
    if(!u){this.doc=null; return}
    this.doc=this.db.collection('progresso').doc(u.uid);
    this.doc.get().then(snap=>{ if(snap.exists) this.apply(snap.data()); this.push(true); Migr.run(); toast('Progresso sincronizado com '+(u.email||'sua conta')+'.');
      this.unsub=this.doc.onSnapshot(s=>{ if(!s.metadata.hasPendingWrites && s.exists) this.apply(s.data()) });
    }).catch(e=>toast('Erro ao sincronizar: '+(e.code||e.message)));
  },
  apply(d){
    if(!d||!d.tracks) return; this.applying=true; let changed=false;
    TR.forEach(t=>{const a=ST[t.id], b=d.tracks[t.id]; if(!b) return; Reorg.prog(t,b);
      Object.keys(b.open||{}).forEach(k=>{if(!a.open[k]){a.open[k]=1; changed=true}});
      a.hl=a.hl||{}; Object.entries(b.hl||{}).forEach(([k,h])=>{const l=a.hl[k]; if(!l||(h.ts||0)>(l.ts||0)){a.hl[k]=h; changed=true}});
      Object.entries(b.ex||{}).forEach(([k,r])=>{const l=a.ex[k]; if(!l||(r.ts||0)>(l.ts||0)){a.ex[k]=r; changed=true}});
      if((b.exTs||0)>(a.exTs||0)){ Object.keys(a.ex).forEach(k=>{ if(!(k in (b.ex||{})) && (a.ex[k].ts||0)<b.exTs){delete a.ex[k]; changed=true} }); a.exTs=b.exTs }
      if((b.lastTs||0)>(a.lastTs||0)){a.last=b.last; a.lastTs=b.lastTs; changed=true}
      store(keyOf(t.id),a)});
    if(d.sim){const ids=new Set(SIM.hist.map(h=>h.id)); (d.sim.hist||[]).forEach(h=>{if(!ids.has(h.id)){SIM.hist.push(h); changed=true}}); SIM.hist.sort((a,b)=>a.end-b.end);
      if(d.sim.cur&&(!SIM.cur||d.sim.cur.id>SIM.cur.id||(d.sim.cur.id===SIM.cur.id&&d.sim.cur.done&&!SIM.cur.done))){SIM.cur=d.sim.cur; changed=true}
      store(SIMKEY,SIM)}
    if(d.prova){const ids=new Set(PRV.hist.map(h=>h.id)); (d.prova.hist||[]).forEach(h=>{if(!ids.has(h.id)){PRV.hist.push(h); changed=true}}); PRV.hist.sort((a,b)=>a.end-b.end);
      const r=d.prova.cur; if(r&&(!PRV.cur||r.id>PRV.cur.id||(r.id===PRV.cur.id&&(r.done&&!PRV.cur.done||Object.keys(r.ans||{}).length>Object.keys(PRV.cur.ans||{}).length)))){PRV.cur=r; changed=true}
      store(PRKEY,PRV)}
    this.applying=false;
    if(changed) route(true);
  },
  push(now){
    if(!this.doc||this.applying) return; clearTimeout(this.timer);
    const go=()=>{const tracks={}; TR.forEach(t=>tracks[t.id]=ST[t.id]);
      this.doc.set({v:1,tracks,sim:SIM,prova:PRV,updated:firebase.firestore.FieldValue.serverTimestamp()}).catch(e=>toast('Erro ao salvar na nuvem: '+(e.code||e.message)))};
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
  if(h==='prova'){show('v-prova'); setTrackNav(null); navCur('prova'); if(soft&&PRV.cur&&!PRV.cur.done) return; if(PRV.cur&&PRV.cur.done&&!soft) renderProvaResult(); else renderProva(); if(!keepScroll) window.scrollTo(0,0); return}
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
