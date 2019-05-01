class Dumbleblin:
	def __init__(self):
		self.HP = 10000
		self.dialogue = {'1': ["Stupidix Malfalse et Adri, venez vous asseoir devant s'il vous plait. Il est important de bien suivre cette présentation.", {}]}


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
		print(u"[36mDumbleblin:[37m ", end = '')
		for line in thinkingAbout[0].split('\n'):
			print(u"[37m"+line)
		print("")
		r = 1
		for choice,reponses in thinkingAbout[1].items():
			print(str(r)+": "+choice  )
			r += 1
