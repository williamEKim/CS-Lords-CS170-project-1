class Node: 
    def __init__(self, state, parent=None, action=None, g=0):
        self.state, self.parent, self.action, self.g = state, parent, action, g
        assert not callable(state), f"Node got a callable for state: {state}" 

    def path(self):
        node, pathBack = self, []
        while node:
            pathBack.append(node)   
            node = node.parent
        return list(reversed(pathBack))
    