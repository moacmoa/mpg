#!/bin/env python

from requests import session
import json
from time import sleep
import os

saison="2018"
mpgdir=os.path.join(os.environ["HOME"], ".mpg")
datadir=os.path.join(mpgdir, "data")
if not os.path.isdir(mpgdir):
	os.mkdir(mpgdir)
if not os.path.isdir(datadir):
	os.mkdir(datadir)

s=session()
url="https://api.monpetitgazon.com/stats/championship/1"
print("getting : "+url)
http=s.get(url)
sleep(1)
players=json.loads(http.text)

for player in players:
	id=player["id"].split("_")[1]
	#print(player)
	prenom=player["firstname"]
	if not prenom:
		prenom=""
	nom=player["lastname"]
	if not nom:
		nom=""
	club=player["club"]
	if not club:
		club=""
	print("{} {} ({})".format(prenom.encode("utf-8"), nom.encode("utf-8"), club.encode("utf-8")))
	
	url="https://api.monpetitgazon.com/stats/player/{}?season={}".format(id, saison)
	print("getting : "+url)
	http=s.get(url)
	sleep(1)
	with open(os.path.join(datadir, id+".json"), "w") as f:
		f.write(http.text.encode("utf-8"))
	#print(json.loads(http.text))
