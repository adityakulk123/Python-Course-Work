# this is a local socpe hwich is defined inside the function but cannot access out side 
'''
def display ():
   
    n=10
    print("inside:",n)

display()
print("outside:",n)
'''
# global variable decleare a key word called global 
'''
def display ():
    global n 
    n=10
    print("inside:",n)

display()
print("outside:",n)
'''
#Variables store data in memory and scope defines the specific region of a program where a variable is accessible. It dictates the visibility and lifetime of the variable within the source code. Variables are categorized into two primary scopes: Global and Local.

#Local Variables
#Local variables are defined inside a function and exist only during its execution. They cannot be accessed from outside the function.

# nonlocal key word hern we are using the they key the variable for only the its function purpose inside we can use the nonlocal declearation 
'''
def display():
    course="jfs"
    print("starting:",course)
    def update():
        #nonlocal course 
        course = "pfs"
        print("updated:",course)   
    update()
    print("final",course)

display()
'''
'''
s ="codegnan"
max = 10
print(max(s))
'''



