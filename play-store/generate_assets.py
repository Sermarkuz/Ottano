#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT=Path(__file__).resolve().parent/"assets"
OUT.mkdir(parents=True,exist_ok=True)
REG="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def ft(n,b=False): return ImageFont.truetype(BOLD if b else REG,n)

DARK="#111827"; DARK2="#1B2736"; GOLD="#FFD34E"; BLUE="#1464D2"; GREEN="#55D88B"
PAPER="#F4F6F8"; INK="#17202A"; MUTED="#66727D"; WHITE="#FFFFFF"

# Google Play icon 512x512
im=Image.new("RGBA",(512,512),DARK); d=ImageDraw.Draw(im)
d.rounded_rectangle((24,24,488,488),radius=110,fill=DARK2)
d.rounded_rectangle((120,95,330,390),radius=42,fill=GOLD)
d.rounded_rectangle((155,135,295,235),radius=24,fill=WHITE)
d.ellipse((190,165,215,190),fill=DARK); d.ellipse((235,165,260,190),fill=DARK)
d.arc((190,175,260,225),20,160,fill=DARK,width=10)
d.rounded_rectangle((165,285,285,345),radius=15,fill=DARK)
d.text((225,315),"95",font=ft(34,True),fill=GOLD,anchor="mm")
d.line((330,170,380,170,405,220,405,320),fill=WHITE,width=18,joint="curve")
d.rounded_rectangle((375,110,430,180),radius=16,fill="#E5482F")
d.rounded_rectangle((100,385,350,420),radius=12,fill=WHITE)
d.polygon([(345,90),(365,125),(345,150),(325,125)],fill=GREEN)
im.save(OUT/"icon-512.png",optimize=True)

# Feature graphic 1024x500
im=Image.new("RGB",(1024,500),DARK); d=ImageDraw.Draw(im)
for x in range(0,1024,64): d.line((x,0,x,500),fill="#1A2433",width=1)
for y in range(0,500,64): d.line((0,y,1024,y),fill="#1A2433",width=1)
d.text((70,80),"OTTANO",font=ft(76,True),fill=WHITE)
d.text((70,165),"Gold",font=ft(56,True),fill=GOLD)
d.text((70,245),"Prezzi carburanti, mappa e simulatore",font=ft(28),fill="#D7DEE7")
d.text((70,285),"Open data MIMIT · Italia",font=ft(22),fill="#9FB8D0")
for i,(lab,val,col) in enumerate([("MIN","1,829",GREEN),("MEDIANA","1,914",GOLD),("MAX","2,099","#FF8A7A")]):
    x=550+i*145
    d.rounded_rectangle((x,110,x+125,260),radius=22,fill="#151B1F",outline="#344151",width=2)
    d.text((x+62,145),lab,font=ft(15,True),fill="#AEB8B3",anchor="mm")
    d.text((x+62,205),val,font=ft(34,True),fill=col,anchor="mm")
    d.text((x+62,235),"€/L",font=ft(14),fill="#AEB8B3",anchor="mm")
d.line((590,350,760,320,900,390),fill=BLUE,width=10)
for px,py,label in [(590,350,"A"),(760,320,"€"),(900,390,"B")]:
    d.ellipse((px-24,py-24,px+24,py+24),fill=WHITE)
    d.text((px,py),label,font=ft(22,True),fill=DARK,anchor="mm")
d.text((70,390),"Scegli l'auto. Confronta. Risparmia.",font=ft(30,True),fill=WHITE)
im.save(OUT/"feature-graphic-1024x500.png",optimize=True)

def base(title,subtitle):
    im=Image.new("RGB",(1080,1920),PAPER); d=ImageDraw.Draw(im)
    d.rectangle((0,0,1080,185),fill=DARK)
    d.text((60,52),"OTTANO",font=ft(52,True),fill=WHITE)
    d.text((270,56),"Gold",font=ft(38,True),fill=GOLD)
    d.ellipse((920,62,942,84),fill=GREEN); d.text((955,73),"LIVE",font=ft(18,True),fill="#D9E1EA",anchor="lm")
    d.text((60,220),title,font=ft(48,True),fill=INK); d.text((60,280),subtitle,font=ft(26),fill=MUTED)
    return im,d

# Screenshot 1
im,d=base("Trova il prezzo migliore","Dati MIMIT, mappa e confronto immediato")
d.rounded_rectangle((60,350,1020,860),radius=28,fill="#DDE3DE")
for x in range(100,1000,160): d.line((x,370,x-70,830),fill="#C2CBC4",width=8)
for y in range(430,840,120): d.line((80,y,1000,y-50),fill="#C2CBC4",width=6)
for x,y,val,col in [(250,550,"1,829",GREEN),(520,470,"1,879",GOLD),(760,600,"1,949","#F2B705"),(860,760,"2,019","#FF8A7A")]:
    d.ellipse((x-60,y-60,x+60,y+60),fill=col,outline=WHITE,width=6)
    d.text((x,y-5),val,font=ft(25,True),fill=DARK,anchor="mm"); d.text((x,y+28),"€/L",font=ft(14,True),fill=DARK,anchor="mm")
d.rounded_rectangle((60,900,1020,1220),radius=28,fill=DARK2)
for i,(lab,val,col) in enumerate([("Più basso","1,829",GREEN),("Mediana","1,914",GOLD),("Più alto","2,099","#FF8A7A")]):
    x=95+i*305; d.rounded_rectangle((x,955,x+265,1155),radius=22,fill="#151B1F")
    d.text((x+25,990),lab,font=ft(21),fill="#AEB8B3"); d.text((x+25,1050),val,font=ft(42,True),fill=col)
d.text((60,1320),"Confronta migliaia di impianti",font=ft(40,True),fill=INK)
d.text((60,1380),"Ordina per prezzo, distanza o costo reale.",font=ft(28),fill=MUTED)
im.save(OUT/"screenshot-1-prices.png",optimize=True)

# Screenshot 2
im,d=base("La tua auto conta","Oltre 380 modelli e motorizzazioni")
d.rounded_rectangle((60,360,1020,860),radius=28,fill=WHITE,outline="#DCE3EA",width=3)
d.text((100,420),"Marca",font=ft(23,True),fill=MUTED)
d.rounded_rectangle((100,465,980,565),radius=18,fill="#F8FAFC",outline="#CBD5E1",width=2)
d.text((140,515),"Abarth",font=ft(32,True),fill=INK,anchor="lm")
d.text((100,620),"Modello",font=ft(23,True),fill=MUTED)
d.rounded_rectangle((100,665,980,765),radius=18,fill="#F8FAFC",outline="#CBD5E1",width=2)
d.text((140,715),"595 Competizione 180",font=ft(31,True),fill=INK,anchor="lm")
d.text((100,815),"Consumo indicativo: 6,9 L/100 km",font=ft(25),fill=MUTED)
d.rounded_rectangle((60,930,1020,1310),radius=30,fill=DARK2)
d.text((100,990),"Costo stimato",font=ft(27),fill="#AEB8B3"); d.text((100,1060),"€ 13,20",font=ft(58,True),fill=GOLD)
d.text((100,1140),"ogni 100 km",font=ft(26),fill=WHITE); d.line((100,1205,970,1205),fill="#344151",width=2)
d.text((100,1250),"12.000 km/anno",font=ft(24),fill="#AEB8B3"); d.text((970,1250),"€ 1.584",font=ft(28,True),fill=WHITE,anchor="ra")
d.text((60,1410),"Dal pieno al costo annuale",font=ft(40,True),fill=INK)
d.text((60,1470),"La simulazione usa prezzo e consumo insieme.",font=ft(27),fill=MUTED)
im.save(OUT/"screenshot-2-auto.png",optimize=True)

# Screenshot 3
im,d=base("Lungo il percorso","Cerca distributori senza perdere la strada")
d.rounded_rectangle((60,360,1020,1220),radius=28,fill="#DDE3DE")
d.line((120,1080,260,900,390,940,560,760,720,690,930,470),fill=WHITE,width=34)
d.line((120,1080,260,900,390,940,560,760,720,690,930,470),fill=BLUE,width=12)
for x,y,label in [(140,1080,"A"),(930,470,"B")]:
    d.ellipse((x-40,y-40,x+40,y+40),fill=BLUE,outline=WHITE,width=5); d.text((x,y),label,font=ft(30,True),fill=WHITE,anchor="mm")
for x,y,val in [(390,940,"1,84"),(650,715,"1,79"),(820,585,"1,88")]:
    d.rounded_rectangle((x-70,y-40,x+70,y+40),radius=22,fill=WHITE); d.text((x,y),val,font=ft(23,True),fill=INK,anchor="mm")
d.text((60,1320),"Percorso A → B",font=ft(40,True),fill=INK)
d.text((60,1380),"Filtra gli impianti entro il corridoio scelto.",font=ft(27),fill=MUTED)
im.save(OUT/"screenshot-3-route.png",optimize=True)

# Screenshot 4
im,d=base("Dati sempre aggiornabili","Aggiornamento online o importazione manuale")
d.rounded_rectangle((60,360,1020,760),radius=28,fill=WHITE,outline="#DCE3EA",width=3)
d.text((100,420),"Centro dati Ottano",font=ft(38,True),fill=INK)
d.rounded_rectangle((100,500,980,600),radius=50,fill=BLUE); d.text((540,550),"Aggiorna dal MIMIT",font=ft(30,True),fill=WHITE,anchor="mm")
d.text((100,665),"Dataset corrente: 23.931 impianti",font=ft(27,True),fill=INK)
d.rounded_rectangle((60,830,1020,1300),radius=28,fill="#F8FAFC",outline="#91A4B7",width=4)
d.text((540,950),"↑",font=ft(82,True),fill=BLUE,anchor="mm")
d.text((540,1050),"Carica i tuoi CSV",font=ft(38,True),fill=INK,anchor="mm")
d.text((540,1110),"prezzi + anagrafica MIMIT",font=ft(26),fill=MUTED,anchor="mm")
d.text((540,1185),"CSV o CSV.GZ",font=ft(24,True),fill=BLUE,anchor="mm")
d.text((60,1420),"Controllo nelle tue mani",font=ft(40,True),fill=INK)
d.text((60,1480),"I file scelti restano nel contesto dell'app.",font=ft(27),fill=MUTED)
im.save(OUT/"screenshot-4-data.png",optimize=True)

print("Generated:",", ".join(x.name for x in OUT.glob("*.png")))
