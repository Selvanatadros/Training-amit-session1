from unicodedata import name
from unittest import result


def lesser_of_two_evens (a,b):
    if a%2==0 and b%2==0 : 
        if a>b:
            return b
        elif a< b:
            return a
    elif a%2!=0 or b%2!=0:
        if a>b:
            return a
        elif a< b:
            return b
        else :
            return b
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))



def animal_crackers(text):
    ss=text.split()
    if ss[0][0]==ss[1][0]:
            print ('true')
    else :
            print('false')
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


def makes_twenty (num1,number2):
    sum =int(num1+number2)
    if sum ==20 or number2==20 or num1 ==20:
        return('true')
    else:
        return('false')
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))



'''def old_macdonald(name1):
    result=''
    for ss in range(len(name1)):
        if ss==0 or ss==3:
            result +=name1[ss].capatalize()
        else:
            result +=name1[ss]
    print (result)
print(old_macdonald('macdonald'))'''

'''def almost_there (number):
    if number in range (90,111) or number in range(190,211):
        print ('true')
    else:
        print('false')

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))'''

def has_33(nums):
    result=False
    for nn in range(len(nums)-1):
        
        if nums[nn:nn+2]==[3,3]:
            return'true'
        
    return result
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


def paper_doll(name1):
    result=''
    for nn in name1:
        for nm in range(3):
            result+=nn
    return result
print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

def blackjack(a,b,c):
    sum=a+c+b
    if sum<=21:
        return sum
    elif a==11 or b==11 or c==11:
        return sum-10
    elif sum >21:
        return 'bust'
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))


def summer_69(arr):
    sum=0
    for num in arr:
        if num in range(6,10):
            continue
        else:
            sum=sum+num
    return sum
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))

def count_primes(num):
    count=0
    for ss in range (2,num+1):
        pri=True
        for n in range (2,num):
            if (ss%n==0):
                pri=False
                break
        if pri:
            count+=1
    return count
print(count_primes(100)) 
    
















