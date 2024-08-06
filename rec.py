#Recursion  is a method where the solution to a problem depends on solutions to smaller instances of the same problem.
#Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

#Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.



def show(i):
    if i<=0:
        return
    print(i)
    show(i-1)
    
show(10)


#call stack is used in recursion to store the function call.

#Recursion is a common mathematical and programming concept. 
# It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.


def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("End of the function")

show(4)

#fact in recursion  #factorial of a number
def factorial(a):
    if a==1:
        return 1
    else:
        return a*factorial(a-1)
    
print(factorial(5))




