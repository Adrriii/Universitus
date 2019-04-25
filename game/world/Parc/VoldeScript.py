class VoldeScript:
	def __init__(self):
		self.HP = 1000
		self.dialogue = {'': ["Qu'attends-tu pour te battre ?", {"Rien, je suis prêt à t'affronter.": ['Très bien, que le combat commence !', {}], 'Je ne suis pas encore prêt, attends un peu.': ['Ahahah, tu croyais vraiment avoir le choix ? Que le combat commence !', {}]}]}


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
		print("VoldeScript: "+thinkingAbout[0]+"\n")
		r = 1
		for choice,reponses in thinkingAbout[1].items():
			print(str(r)+": "+choice  )
			r += 1
