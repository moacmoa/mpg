class Player():
	def __init__(self, dic):
		self.__dict__=dic
		self.club=self.club.encode("utf-8")

	def getLastFivePercent(self):
		lastfive=self.stats["lastFiveRate"]
		nbPlayed=0
		for key, value in lastfive.iteritems():
			if lastfive[key]["matchId"]!="-":
				nbPlayed+=1
		return(float(nbPlayed)/len(lastfive))
			
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
