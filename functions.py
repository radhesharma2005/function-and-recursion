#functions is a block of statements that performs specific task
#syntax of function 
#def fun_name(para1,para2,..):
    #some work
    #return val
#function call
"""Syntax 
function_name(arg1,arg2,...)"""
#example
def sum(a,b):       #function declaration
    sum=a+b         #operation
    print(sum)      #prints the sum
    return sum   #return sum
sum(2,5)        #calling same function again
sum(6,7)        #calling same function again
sum(2,90)       #calling same function again

#correct table using function
def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = ",n*i)
for k in range(1,10):    
        n=int(input("Enter the number : "))
        table(n)

  #instead of following:
n=int(input("Enter the number : "))
table(n)
n=int(input("Enter the number : "))
table(n)
n=int(input("Enter the number : "))
table(n)


#avg of three number using function
def cal_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
flag='start'
while (flag!='stop'):
    for i in range(1,5):
        a=int(input("Enter the number a : "))
        b=int(input("Enter the number b : "))
        c=int(input("Enter the number c : "))
        cal_avg(a,b,c)
        flag=input("Do you want to repeat the loop (start/stop) : ")



#Function types
#Built-in functions  print(),type(),len(),input(),range()
print("Radheshyam",end=" ")
print("Sharma")         #end="\n"

#User defined function : Function that its logic is written by user and defined by user

#Q1) WAF to print the length of list(list is the parameter)

def  len_lis(list):
    list1=[2,4,5,6,7,90,23,56,67]
    print(len(list1))
len_lis(list)


#Q2) WAF to print list in a single line
nums=[34,23,67,89,12,56,90,88]
def print_list(list):
    for i in list:
        print(i,end=" ")
print_list(nums)

#WAF to find factorial of number n

def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
num=int(input("Enter the number : "))
cal_fact(num)

#convert usd to inr
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val, "USD =", inr_val, "INR")
n=int(input("Enter the amount : "))
converter(n)