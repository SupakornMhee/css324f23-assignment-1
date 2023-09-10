def initial_state():
    return (8, 0, 0)

def is_goal(s):
    a,b,c = s
    return a==4 and b==4

def successors(s):
    a,b,c = s
    #There is no use in calculating successors of emptyed and filled bottle since the question not allow any additional 
    #water(no filling) and total water have to remain the same as the initial state that mean no losing(emptying) any water
    #move between bottles
    ax,bx,cx = 8-a,5-b,3-c
    #a to b
    if a>bx>0 : yield ((a-bx,5,c),bx) 
    if bx>a>0 : yield ((0,b+a,c),a) 
    #a to c
    if a>cx>0 : yield ((a-cx,b,3),cx) 
    if cx>a>0 : yield ((0,b,c+a),a) 
    #b to a
    if b>ax>0 : yield ((8,b-ax,c),ax) 
    if ax>b>0 : yield ((a+b,0,c),b) 
    #b to c
    if b>cx>0 : yield ((a,b-cx,3),cx) 
    if cx>b>0 : yield ((a,0,c+b),b) 
    #c to a
    if c>ax>0 : yield ((8,b,c-ax),ax) 
    if ax>c>0 : yield ((a+c,b,0),c) 
    #c to b
    if c>bx>0 : yield ((a,5,c-bx),bx) 
    if bx>c>0 : yield ((a,b+c,0),c) 




