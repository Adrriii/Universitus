class A_Grid:
	def __init__(self):
		self.dialogue = {'2': ['Très bien! Comme tu peux le voir en bas, il y a marqué "Universitus/Accueil". C\'est ce qui indique ton emplacement dans le monde. \nJe te propose de t\'adresser à monsieur Argus Rusarg afin qu\'il te dise où te rendre pour ton inscription. \nPour lui parler, utilise la commande `talk M.Rusarg.py`. Oui, son extension est .py, comme toutes les entités de ce monde.', {}], '1': ["Bienvenue dans le monde magique de la programmation ! Ici tu apprendras à te servir d'un pouvoir extrêment rare : l'Unixité. \nC'est une compétence que seuls les plus grands informagiciens peuvent maîtriser, mais grâce à ton parcours dans cette école tu sauras surement révéler ton potentiel ! \nPour commencer, je vais t'apprendre à te téléporter d'un endroit à un autre. Pour cela, utilise la commande `cd <destination>`, par exemple : `cd Accueil`. Je t'attends là-bas !", {}]}


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
		print(u"[36mA_Grid:[37m ", end = '')
		for line in thinkingAbout[0].split('\n'):
			print(u"[37m"+line)
		print("")
		r = 1
		for choice,reponses in thinkingAbout[1].items():
			print(str(r)+": "+choice  )
			r += 1
