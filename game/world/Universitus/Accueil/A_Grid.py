class A_Grid:
	def __init__(self):
		self.dialogue = {'': ["Bienvenue dans le monde magique de la programmation ! Ici tu apprendras à te servir d'un pouvoir extrêment rare : l'Unixité. \nC'est une compétence que seuls les plus grands informagiciens peuvent maîtriser, mais grâce à ton parcours dans cette école tu sauras surement révéler ton potentiel ! \nPour commencer, je vais t'apprendre à te téléporter d'un endroit à un autre. Pour cela, utilise la commande `cd <destination>`, par exemple : `cd Accueil`. Je t'attends là-bas !", {}]}


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
		print("A_Grid: "+thinkingAbout[0]+"\n")
		r = 1
		for choice,reponses in thinkingAbout[1].items():
			print(str(r)+": "+choice  )
			r += 1
