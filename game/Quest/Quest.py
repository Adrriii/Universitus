from Quest.Event import Event
from Quest.Condition import Condition
from Quest.Conditions.EntityExistsCondition import EntityExistsCondition
from Quest.Conditions.PlaceExistsCondition import PlaceExistsCondition

class Quest :
    def __init__(self, filename) :
        with open("Quests/"+filename) as file:
            for line in file.readlines():
                parts = line.split(':')
                attr = parts.pop(0)
                left = "".join(parts)
                
                if(attr == "name"):
                    if(left != 'none'):
                        self.name = left
                    continue
                if(attr == "conditions"):
                    if(left != 'none'):
                        self.conditions = []
                        conditions = left.split('[')[1].split(']')[0]

                        for condition in conditions.split(','):
                            self.conditions.append(condition)
                    continue

    def evalConditions(self):
        evals = []
        for condition in self.conditions:
            invert = False
            toEval = condition

            sp = condition.split(' ')
            check = sp[0]
            if(check == "not"):
                invert = True
                sp.pop(0)
                toEval = "".join(sp)

            met = eval(toEval)().met()
            evals.append((not invert and met) or (invert and not met))
        print(evals)
        for ev in evals:
            if not ev:
                return False
        return True

            
    
