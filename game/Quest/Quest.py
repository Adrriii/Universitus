import * from Character
import * from Event
import * from Condition

class Quest :
    def __init__(self) :
        self.initiator = Character()
        self.resolver = Character() 

        self.available = False

        self.onStart = Event()
        self.onResolve = Event()

        self.steps = [] #Quest[] needed to resolve the quest
        self.conditions = [] #Condition[]  needed to resolve the quest

        self.next = [] #Quest[] unlocked on resolve


    