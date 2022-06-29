st = 'Print only the words that start with s in this sentence'
for str in st.split():
    if str[0]=='s':#print frist number start s
        print(str)


for i in range(0,11):
    if i%2==0: #print even number range 0 to 11
        print('even no{}'.format(i))
    


ss=[number for number in range (1,51) if number%3==0]
print(ss) #print no range 1 to 51  divisible by 3


st = 'Print every word in this sentence that has an even number of letters'
for str in st.split(): #bnmshi 3la kol klma lw7dha 
    if len(str)%2==0: # if no of string is even print even
        print('even!')


'''Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" 
instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of
both three and five print "FizzBuzz".'''

for i in range(1,101):
    if i%3==0: 
        print("fizz")
    elif i%5==0:
        print('buzz')
    elif i%3==0 and i%5==0:
        print('fizzbuzz')
    else:
        print('erro')


st = 'Create a list of the first letters of every word in this string'
st=[str [0] for str in st.split() ]#bna5d kol klma lw7dha w na5d awl 7arf no7to fi list
print (st)