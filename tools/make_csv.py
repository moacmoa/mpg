#!/bin/env python
import os
from classes.Player import Player
import json

mpgdir=os.path.join(os.environ["HOME"], ".mpg")
datadir=os.path.join(mpgdir, "data")
txtfile=os.path.join(mpgdir, "mpg.txt")

files=os.listdir(datadir)
print(len(files))

players=[]
for f in files:
	with open(os.path.join(datadir, f)) as tmp:
		players.append(Player(json.loads(tmp.read())))
	
lines="nom\tnom\tclub\tposition\tbuts\tmoyenne\tpercLast5\tcote\n"	
for p in players:
	line="{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
		p.lastname.encode("utf-8"),
		p.getPrenomNom(),
		p.club,
		p.getPosition(),
		str(p.stats["sumGoals"]).replace(".", ","),
		str(p.stats["avgRate"]).replace(".", ","),
		str(p.getLastFivePercent()).replace(".", ","),
		str(p.quotation).replace(".", ",")
	)
	
	lines+=line+"\n"

print(lines)
with open(txtfile, "w") as f:
	f.write(lines)
