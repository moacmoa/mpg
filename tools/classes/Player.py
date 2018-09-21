class Player():
	def __init__(self, dic):
		self.__dict__=dic
		self.club=self.club.encode("utf-8")
		if self.stats["avgRate"]=="-":
			self.stats["avgRate"]="0"
		self.setLastFiveDays()
		
	def setLastFiveDays(self):
		l5=self.stats["lastFiveRate"]
		mini=100
		for key, val in l5.iteritems():
			mini=min(mini, val["day"])
		
		self.last5Days=[]
		for i in range(len(l5)):
			self.last5Days.append(mini+i)

	def getLastFivePercent(self):
		lastfive=self.stats["lastFiveRate"]
		nbPlayed=0
		for key, value in lastfive.iteritems():
			if lastfive[key]["matchId"]!="-":
				nbPlayed+=1
		return(float(nbPlayed)/len(lastfive))
	
	def getLastFivePresence(self):
		ret=[]
		l5=self.stats["lastFiveRate"]
		for num in self.last5Days:
			if l5[str(num)]["matchId"]=="-":
				ret.append(False)
			else:
				ret.append(True)
		return(ret)
	
	def getLastFiveAverage(self):
		matches=self.stats["matches"]
		notes=[float(m["info"]["rate"]) for m in matches if m["day"] in self.last5Days]
		avg=0.
		if len(notes)>0:
			avg=sum(notes)/len(notes)
		return(avg)
			
	def getPrenomNom(self):
		prenom=self.firstname
		if not prenom:
			prenom=""
		nom=self.lastname
		if not nom:
			nom=""
		ret="{} {}".format(prenom.encode("utf-8"), nom.encode("utf-8")).strip()
		return(ret)
		
	def getPosition(self):
		tab=[None, "Gardien", "Defenseur", "Milieu", "Attaquant"]
		return(tab[self.position])
