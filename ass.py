#bi3d 3dd 4 ali mwgoda fi al list 

def count_no (list1):
    counter =0
    for num  in list1 :
        if num ==4:
            counter +=1
    return counter
print(count_no([1,2,3,4,4,5,4,4,4]))



def check_no ( num , numbers):
    if num %numbers !=0:
            return 'true'
    else:
            return 'flase'
 
print(check_no(5,20))




def max_min_no (list2):
    max =list2[0]
    min=list2[0]
    for num2 in list2:
        if num2>max:
            max=num2
        elif num2<min:
            min=num2
    return max , min           
print(max_min_no([1,2,3,5,10,12]))


def intersection_2list (list3,list4):
    for num3 in list3:
        for num4 in list4:
            if num3 == num4:
                return 'true'
            else:
                return 'false'
print(intersection_2list([2,52,56,5],[1,3,55,59,65]))



#Write a Python function to calculate the factorial of a number
#  (a non-negative integer). The function accepts the number from the user
def factorial(ss):
    if ss==1:
        return 1
    else:
        return ss * factorial(ss-1)
ss=int(input('enter number'))

print(factorial(ss))




#Write a Python function to check whether a number is in a given range.
### The range is from 3 to 11

def check_number_in (num6):
    
    if num6 in range(3,12):
        return'true'
    else:
        return'false'
print(check_number_in(5))


### Write a  program to create the multiplication table (from 1 to 10) of a number.

# 
'''def multiplication(num11):
    for mx in range(1,11):
        return num11*mx
print(multiplication(5))'''

mm=int(input('enter no'))
for mx in  range(1,11):
    print(mm,'*',mx,'=',mm*mx)

#### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, 
# but returns the greater if one or both numbers are odd

def check (num5,num6):
    if num5%2==0 and num6%2==0 : 
        if num5>num6:
            return num6
        elif num5< num6:
            return num5
    elif num5%2!=0 or num6%2!=0:
        if num5>num6:
            return num5
        elif num5< num6:
            return num6
        else :
            return num6
print(check(2,4))
print(check(2,5))







