# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

nested_list = [[3,1,2], [5,0,4]]

result = flatten_and_sort(nested_list)

print(result)


# Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
    def __init__(self, max_speed,condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    # Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"

# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2

# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def flame_jet(self,other):
        other.condition = "trashed"



anakins_pod = AnakinsPod(max_speed=100, condition="new", price=150000)
print(f"Anakin's Pod: Speed = {anakins_pod.max_speed}, Condition = {anakins_pod.condition}, Price = {anakins_pod.price}")


anakins_pod.boost()
print(f"After boost, Anakin's Pod: Speed = {anakins_pod.max_speed}")


sebulbas_pod = SebulbasPod(max_speed=90, condition="used", price=130000)
print(f"Sebulba's Pod: Speed = {sebulbas_pod.max_speed}, Condition = {sebulbas_pod.condition}, Price = {sebulbas_pod.price}")


sebulbas_pod.flame_jet(anakins_pod)
print(f"After flame jet, Anakin's Pod Condition: {anakins_pod.condition}")


anakins_pod.repair()
print(f"After repair, Anakin's Pod Condition: {anakins_pod.condition}")
