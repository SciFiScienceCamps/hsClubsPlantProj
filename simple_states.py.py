#------------------------------------------------
#SciFi Science Camps State Machine Library
#
class state():
    def  __init__(self, state_name,state_function,state_switch = None,state_exit = None):
        self.name = state_name
        self.function = state_function
        self.switch = state_switch
        self.exit = state_exit
    
    def loop(self, state_param):
        if(state_param == self.exit):
            return False
        else:
            self.function(state_param)
            return True

def state_handler(states,param,cur):
    if cur.name not in states:
        print("Error code 1: state does not exist")
    else:
        result = cur.loop(param)
        if not result:
            return True
        else:
            return False

            
    
def funA(param):
    print(param)

def funB(param):
    print(param + " but new")

A = state("A", funA, "B", "to B")
B = state("B", funB, "A", "to A")

master_list = [A,B]
states = ["A","B"]

usr = input("Gimme: ")
cur = A
while not usr == "exit":
    run = state_handler(states,usr,cur)
    if run:
        cur  = master_list[states.index(cur.switch)]
    usr = input("Gimme: ")


