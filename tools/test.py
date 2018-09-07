from classes.Player import Player
import json

with open("/home/og221675/.mpg/data/18574.json") as f:
	dic=json.loads(f.read())

p=Player(dic)

print(p.firstname)
print(len(p.stats["matches"]))
print(p.getLastFivePercent())
