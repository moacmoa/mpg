#!/bin/env python
import os
from classes.Player import Player
import json

mpgdir=os.path.join(os.environ["HOME"], ".mpg")
datadir=os.path.join(mpgdir, "data")
txtfile=os.path.join(mpgdir, "mpg.txt")

files=os.listdir(datadir)

players=[]
for f in files:
	with open(os.path.join(datadir, f)) as tmp:
		players.append(Player(json.loads(tmp.read())))
	
lines="nom\tnom\tclub\tposition\tbuts\tavg\tet\tl5%\tl5\tl5avg\tl5et\tcote\n"	
for p in players:
	sPresence=""
	for e in p.getLastFivePresence():
		if e:
			sPresence+="X"
		else:
			sPresence+="o"
			
	line="{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
		p.lastname.encode("utf-8"),
		p.getPrenomNom(),
		p.club,
		p.getPosition(),
		str(p.stats["sumGoals"]).replace(".", ","),
		#str(p.stats["avgRate"]).replace(".", ","),
		str(round(p.allAverage, 2)).replace(".",","),
		str(round(p.allStdDev, 2)).replace(".",","),
		str(p.getLastFivePercent()).replace(".", ","),
		sPresence,
		str(round(p.lastFiveAverage, 2)).replace(".",","),
		str(round(p.lastFiveStdDev, 2)).replace(".",","),
		str(p.quotation).replace(".", ",")
	)
	
	lines+=line+"\n"

print(lines)
with open(txtfile, "w") as f:
	f.write(lines)
