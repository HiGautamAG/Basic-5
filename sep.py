print("I am a", end=" ") #seprators=""   #end is a keyword argument
print("Python Programmer")  #end is a keyword argument

# default parameters in python  #default parameters

def cal_grow(a=1,b=2):
    print(a*b)
    return a*b

cal_grow(2)


#waf to print a function of a list of numbers?

sweets = ["\nchocolate","candy","icecream","cake","biscuit"]  
bitters = ["bittergourd","karela","neem","fenugreek","spinach", "kale"]

def print_len(sweets):
    print(len(sweets))
    
print_len(sweets)
print_len(bitters)  


#waf to fun to print in alist in a single line.





sweets = ["\nchocolate","candy","icecream","cake","biscuit"]  
bitters = ["bittergourd","karela","neem","fenugreek","spinach", "kale"]

print(sweets[0], end=" ")
print(bitters[1], end=" ")

def print_list(list):
    for i in list:
        print(i, end=" ")
        
        
        
        
        
#factorial of a number

a = int(input("Enter a number: "))
def factorial(a):
    fact = 1
    for i in range(1,a+1):
        fact = fact*i
    return fact

print(factorial(a))


#waf to convert USD to INR?

def converter(usd_value):
    inr_value = usd_value*75
    print(usd_value,"usd=",inr_value,"inr") #usd to inr conversion
    
converter(10) #calling the function


#odd or even

def odd_even(a):
    if ( a%2==0):
        print("Even")
    else:
        print("Odd")
        
        print(odd_even(a))
       