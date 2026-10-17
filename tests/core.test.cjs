const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
function load(file){
 const html=fs.readFileSync(file,'utf8');
 for(const [,attrs,script] of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)) if(!/type=/.test(attrs)) new vm.Script(script);
 const core=html.split('/* ===== CORE (testabile senza DOM) ===== */')[1].split('/* ===== /CORE ===== */')[0];
 const ctx={module:{exports:{}}};vm.runInNewContext(core,ctx);return ctx.module.exports;
}
for(const file of ['ottano.template.html','ottano.html']){
 const c=load(file);
 const a='\uFEFFEstrazione del 2026-10-17\nidImpianto|Gestore|Bandiera|Tipo Impianto|Nome Impianto|Indirizzo|Comune|Provincia|Latitudine|Longitudine\n1||Test|Stradale|Test|Via|Bolzano|BZ|46,5|11,35\n2||Test|Stradale|Test|Via|Bolzano|BZ|46.51|11.36';
 const prices=rows=>'Estrazione del 2026-10-17\nidImpianto|descCarburante|prezzo|isSelf|dtComu\n'+rows.join('\n');
 const rows=['1|Benzina|1,500|1|16/10/2026 08:00:00','1|Benzina|1,900|1|17/10/2026 08:00:01','1|Benzina|1,800|1|17/10/2026 08:00:00','2|Benzina|2.100|1|17/10/2026 08:00','1|Idrogeno|0.7|1|17/10/2026 08:00','1|GPL|1.0|x|17/10/2026 08:00','1|Metano|Infinity|1|17/10/2026 08:00'];
 test(file+': fuel catalogue and car catalogue are separate',()=>{assert.equal(c.FUELS.length,9);assert.ok(c.FUELS.every(f=>f.k&&f.n));assert.ok(c.CARS.some(x=>x[0]==='Seat'));assert.ok(c.CARS.some(x=>x[0]==='Abarth'));});
 test(file+': latest price, comma decimals, BOM, real median, consistent history',()=>{
  for(const order of [rows,[...rows].reverse()]){
   const db=c.buildDB(a,prices(order),'test');assert.equal(db.stations.length,2);assert.equal(db.byId.get('1').pr.benzina.s.p,1.9);assert.equal(db.med.benzina,2);assert.equal(Object.keys(db.byId.get('1').pr).length,1);
   const day=c.parseDay(prices(order),db);assert.equal(c.dayPrice(day,0,'benzina','self'),1.9);
  }
 });
 test(file+': malformed dates and unknown products rejected',()=>{assert.equal(c.parseDt('31/02/2026 08:00'),0);assert.equal(c.parseDt('17/10/2026 24:00'),0);assert.equal(c.categorize('Idrogeno'),null);assert.equal(c.categorize('HVO Diesel'), 'hvo');assert.equal(c.decimal('1,875'),1.875);});
 test(file+': weighted measured consumption isolated by car, fuel and full-tank measurement',()=>{
  const e={fuel:'benzina',car:'A',full:true,l:30,km:500,p:2};
  const entries=[e,{...e,l:70,km:1000},{...e,fuel:'metano',l:999},{...e,car:'B',l:999},{...e,full:false,l:999},{l:999,km:10}];
  const m=c.diaryConsumption(entries,'benzina','A');assert.equal(m.count,2);assert.equal(m.distance,1500);assert.ok(Math.abs(m.value-100/15)<1e-10);assert.ok(Math.abs(m.cost100-200/15)<1e-10);assert.equal(c.diaryConsumption(entries,'elettrico','A').value,0);
 });
 test(file+': simulation quantity calculations',()=>{assert.equal(c.litriFor({simMode:'budget',budget:50},2),25);assert.equal(c.litriFor({simMode:'tank',tank:50,level:25},2),37.5);});
}
