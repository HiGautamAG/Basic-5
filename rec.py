#Recursion  is a method where the solution to a problem depends on solutions to smaller instances of the same problem.
#Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

#Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.



def show(i):
    if i<=0:
        return
    print(i)
    show(i-1)
    
show(10)


