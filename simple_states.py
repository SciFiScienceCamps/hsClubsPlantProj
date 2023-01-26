"""
Simple State Machine Library
"""

class machine:
    def __init__(self):
        self.states = []
        self.state_names = []
        self.cur_state = 0
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
    def run(self):
        if(len(self.states) < 1):
            print("Error code 3: Machine has no states")
        else:
            while(1):
                cur = self.states[self.cur_state]
                cur.execute_function()
                if(cur.switch_cases[cur.switch_var](cur.checkCondition())):
                    print("You did it")
                    self.cur_state = self.states.index(cur.go_to)
                else:
                    break


class state:
    def __init__(self,name):
        self.name = name
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

    def checkCondition(self):
        return input("New val: ")

    def add_switch(self,read_from,switch_expression,go_to):
        self.go_to = go_to
        self.switch_var = read_from
        self.switch_cases[read_from] = switch_expression