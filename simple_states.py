"""
Simple State Machine Library
"""

class machine:
    def __init__(self):
        self.states = []
        self.state_names = []

    def add_state(self,newState):
        self.states.append(newState)
        try:
            self.state_names.append(newState.name)
        except:
            print("Error code 1: state has no attribute 'name'")

    def list_states(self):
        count = 0
        for i in self.states:
            count += 1
            print(f"State {count}: {i.name}")

    def describe_state(self,req):
        if(req not in self.state_names):
            print("Error code 2: state does not exist in current machine")
        else:
            pos = self.state_names.index(req)
            self.states[pos].view_properties()
    


class state:
    def __init__(self,name):
        self.name = name
        self.switch_condition = None
        self.switch_variable = None
        self.attributes = ["name: " + name]
        self.switch_cases = {}

    def view_properties(self):
        for i in self.attributes:
            print(i)
    
    def add_function(self, function_name):
        self.function = function_name
        self.attributes.append("function: " + str(function_name))
    
    def execute_function(self):
        self.function()

    def add_switch(self,newSwitch,switch_condition):
        try:
            switchName = newSwitch.name
            self.switch_cases[switchName] = newSwitch
            self.switch_condition = switch_condition
        except:
            print("Error code 1: state has no attribute 'name'")
            return
        self.attributes.append(f"switch case {len(self.switch_cases)}: \n   function {newSwitch} \n     condition {self.switch_condition}")
            
def foo():
    print("Bar")

def tom():
    print("Whoopsie")

container = machine()

A = state("A")
B = state("B")

A.add_function(foo)
B.add_function(tom)

container.add_state(A)
container.add_state(B)

container.list_states()
x = None

A.add_switch(B,lambda x: x == 3,True)
A.view_properties()
x = 3
A.view_properties()