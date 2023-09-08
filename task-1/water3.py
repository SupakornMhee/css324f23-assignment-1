def initial_state():
    return (8, 0, 0)

def is_goal(s):
    a,b,c = s
    return a==4 or b==4

def successors(s):
    a,b,c = s
    return []
