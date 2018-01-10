import random

##this program simulates a random walk using the montecarlo approach

## we are to find the longest random walk that can be taken so that at the end
## we are 4 blocks or less from the origin


## first version of the function

def random_walk(n):
    """returns the co-ordinates after n blocks of random walk"""
    x,y = 0,0
    for i in range(n):
        step = random.choice(['N','S','E','W'])
        if step == 'N':
            y+=1
        elif step == 'S':
            y-=1
        elif step == 'E':
            x+=1
        else:
            x-=1
    return (x,y)

# for i in range(0,25):
#    walk = random_walk(22)
#    print walk, "  distance from home :", abs(walk[0])+abs(walk[1])


## Second function that is shorter

def random_walk_2(n):
    """returns the co0ordinates after n blocks of random walks"""
    x,y=0,0
    for i in range(n):
        dx,dy = random.choice([(0,1), (0,-1),(1,0) ,(-1,0)])
        x+= dx
        y+= dy
    return (x,y)

for i in range(31):
    walk = random_walk_2(12)
    print walk, "the distance from home :", abs(walk[0])+ abs(walk[1])

## calculating the percentage of random walks in the range of 1 to 31 that are 4 blocks or
## less from the origin to avoid spending on cab

no_of_walks = 10000
walk_length = 31

for i in range(31):
    no_transport = 0 # if it is greater than 4, you will have to take a ride back home
    for j in range(no_of_walks):
        x,y = random_walk_2(i)
        distance = abs(x)+abs(y)
        if distance <=4:
            no_transport+=1
    no_transport_percentage = float(no_transport)/no_of_walks
    print ("walk size =", i, "percentage of no transport = ",100*no_transport_percentage)



