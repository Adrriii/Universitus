class A_Grid:
	def __init__(self):
		self.dialogue = {'1': ["Bienvenue dans le monde magique de la programmation Adri ! Ici tu apprendras à te servir d'un pouvoir extrêment rare : l'Unixité. \nC'est une compétence que seuls les plus grands informagiciens peuvent maîtriser, mais grâce à ton parcours dans cette école tu sauras surement révéler ton potentiel ! \nPour commencer, je vais t'apprendre à te téléporter d'un endroit à un autre. Pour cela, utilise la commande `cd <destination>`, par exemple : `cd Parc`. Je t'attends là-bas !", {}, "SetDialogueChoice('A_Grid', ['3'])"], '2': ['Très bien! Comme tu peux le voir en bas, il y a marqué "Universitus/Accueil". C\'est ce qui indique ton emplacement dans le monde. \nJe te propose de t\'adresser à monsieur Argus Rusarg afin qu\'il te dise où te rendre pour ton inscription. \n Utilise la commande ls pour afficher tes possibilités.\n Pour lui parler, utilise la commande `talk Rusarg.py`. Oui, son extension est .py, comme toutes les entités de ce monde.', {}], '3': ['Rebonjour !', {}], '4': ["C'est bien ! Bon, je retourne à Bethanie pour accueillir les prochaines élèves. Viens me voir si tu as besoin d'aide !", {}]}


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
