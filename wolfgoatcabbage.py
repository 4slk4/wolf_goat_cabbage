from search import *

class WolfGoatCabbage(Problem):
    def __init__(self):
        self.initial = frozenset({'F', 'G', 'W', 'C'})
        self.goal = frozenset()


    def goal_test(self, state):
        return state == self.goal
    
    def result(self, state, action):
        new_state = set(state)
        action = set(action)
        if 'F' in new_state:
            return frozenset(new_state.difference(action))
        return frozenset(new_state.union(action))
    
    def actions(self, state):
        temp_state = set(state)
        valid_actions = []
        num = len(temp_state)
        
        if num > 0:
            if num == 4:
                valid_actions.append({'F','G'})
            if num == 2:
                valid_actions.append({'F'})
                valid_actions.append({'F','G'})
            if num == 1 or num == 3:
                if num == 1:
                    temp_state = set(self.initial).difference(temp_state)
               
                if 'W' in temp_state and 'C' in temp_state:
                    valid_actions.append({'F'})

                temp_state.remove('F')
                while (temp_state):
                    ele = temp_state.pop()
                    valid_actions.append({'F'}.union(set(ele)))
        return valid_actions

            
if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    print(breadth_first_graph_search(wgc).solution())
    print(depth_first_graph_search(wgc).solution())
