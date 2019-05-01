class Stupidix:
	def __init__(self):
		self.dialogue = {'': ["OHHHH, toi aussi tu as terminé ton inscription à l'universitus ?? AHAHAHAH je le savais !! Maintenant depeche toi de me rejoindre dans la grande salle pour la ceremonie ... Nous sommes deja en retard !! SERPYTHON 4 EVER <3", {}], '1': ["AHAHA tu as trouvé la grande salle GG <3 ! Allons-y let's go c'est parti l'ami, nous allons y assister je sais qu'on va y arriver !! Ou allons nous ?? A SERPYTHON <3"]}


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
		print(u"[36mStupidix:[37m ", end = '')
		for line in thinkingAbout[0].split('\n'):
			print(u"[37m"+line)
		print("")
		r = 1
		for choice,reponses in thinkingAbout[1].items():
			print(str(r)+": "+choice  )
			r += 1
