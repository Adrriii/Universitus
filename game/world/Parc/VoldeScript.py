class VoldeScript:
	def __init__(self):
		self.HP = 1000
		self.dialogue = {}


	def talk(self,saidToHim):
		if not self.dialogue:
			print("*Fait des gestes avec ses bras*")
			print("Ce personnage ne peut apparemment pas parler.")
			return
		thinkingAbout = self.dialogue
		for listensTo in saidToHim:
			thinkingAbout = thinkingAbout[listensTo]
		print(thinkingAbout[0])
