people = [ 
    {"name":"rehan","city":"porbandar"},
    {"name":"mukhtar","city":"porbandar"},
    {"name":"raj","city":"surat"}
]
#without using lambda
def f(people):
    return people["name"]
people.sort(key = f)
#now using lambda
people.sort(key = lambda people : people["name"])
 
print(people)