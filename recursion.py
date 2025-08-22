#When a function recall itself repeatedly

def show(n):
    if (n == 0):  #base case: stops recursion when n becomes 0
        return
    print(n)     # prints the current value of n
    show(n-1)    #recursive call with a smaller value
n=int(input("Enter the value:"))
show(n)


#return n
def fact(n):
    if(n==0) or (n==1):
        return 1
    else:
        return n * fact(n-1)
n=int(input("enter the value: "))
print(fact(n))

#calling function till stop
def fact(n):
    if(n==0) or (n==1):
        return 1
    else:
        return n * fact(n-1)
radhe="start"
while radhe!="stop":
    n=int(input("enter the value: "))
    print(fact(n))
    flag=input("Do you want to repeat the function (start/stop)? : ")



#PRACTICE


#write a recursive function to calculate sum of first n natural numbers
def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1)+n
n=int(input("Enter the number : "))
print(cal_sum(n))

#write a recursive function to print all elements in list
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

city=["Mumbai","Pune","Kolhapur","Thane","Kalyan"]

print_list(city)