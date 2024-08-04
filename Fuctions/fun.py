#Fuctions in python is a block of statements that perform a specific task.

#parameters are the values that are passed to the function when it is called  and they are assigned to the variables
#arguments are the values that are passed to the function when it is called  and they are assigned to the parameters
#function are used to remove redundancy of code.
def calculate_sum(a,b):
    
    sum = a+b
    print("The sum of the two numbers is: ",sum)
    return sum

calculate_sum(10,20)
calculate_sum(20,30)#calling the function
calculate_sum(30,40)#calling the function



def calc_sum(a,b): #function definition with parameters
    return a+b
sum = calc_sum(10,20) #function call with arguments
print(sum)



def print_me():
    print("Hello  World")
    
output = print_me()
print(output) #None is returned because the function does not return anything


#average of numbers

def average(a,b,c):
    avg = (a+b+c)/3
    return avg

print(average(1,2,3))

def calc_avg(a,b,c):

    sum = a + b + c
    avg = sum/3
    return avg
print(calc_avg(10,20,30))



    