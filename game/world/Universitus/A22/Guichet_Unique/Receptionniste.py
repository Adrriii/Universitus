class Receptionniste:
	def __init__(self):
		self.dialogue = {'': ['Bonjour, Mr ...\n Quel est votre nom ?', {'Mon nom est Adri': ['Très bien Adri, Votre inscription est maintenant terminée, voici vos papiers, les autres vous attendent deja pour la ceremonie. Depechez vous ou le professeur Dumbleblin vous lancera un mauvais processort', {}]}]}


	def talk(self,saidToHim):
		if not self.dialogue:
			print("*Fait des gestes avec ses bras*")
			print("Ce personnage ne peut apparemment pas parler.")
			return
		thinkingAbout = self.dialogue
		next = self.dialogue
		for listensTo in saidToHim:
			thinkingAbout = next[listensTo]
			next = thinkingAbout[1]
		print(u"[36mReceptionniste:[37m ", end = '')
		for line in thinkingAbout[0].split('\n'):
			print(u"[37m"+line)
		print("")
		r = 1
		for choice,reponses in thinkingAbout[1].items():
			print(str(r)+": "+choice  )
			r += 1
