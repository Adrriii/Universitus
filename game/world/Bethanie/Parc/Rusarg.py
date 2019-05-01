class Rusarg:
	def __init__(self):
		self.dialogue = {'': ["La direction du Guichet Unique ? Vous ne savez pas lire ? Elle est indiquée sur tous les panneaux aux alentours ! Débrouillez-vous. \nMais attention ! Les première année sont toujours les pires, et vous n'avez pas une bouille angélique. Je vous ai à l'oeil...", {}]}


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
		print(u"[36mRusarg:[37m ", end = '')
		for line in thinkingAbout[0].split('\n'):
			print(u"[37m"+line)
		print("")
		r = 1
		for choice,reponses in thinkingAbout[1].items():
			print(str(r)+": "+choice  )
			r += 1
