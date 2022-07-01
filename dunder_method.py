'''mahic or Dunder method is special method start and end '__' happen from class
in certian action '''

#'__add__ happen in operator add to number and concatinat if 
# exist string ,list,tuple
                    #example
X=10
print(X.__add__(5))
#__sub__(self, other)  happen in operator subb to number
#__mul__(self, other) happen in operator nultiplication to number
#__truediv__(self, other) happen in operator divaided to number (lazm ykon 3dd s7ii7) return nateg al asma float
#__floordiv__(self, other)  happen in operator divaided to number (lazm ykon 3dd s7ii7) return nateg al asma integer
#__pow__(self, other[, modulo]) happen in operator power to number return x**y
X=10
print(X.__sub__(5))
print(X.__mul__(5))
print(X.__truediv__(20))
print(X.__floordiv__(20))
print(X.__pow__(2))


class noha:
    def __init__(self,Ali):
        self.Ali=Ali
        
    def __getattr__(self,name):#lw al attrubute msh mwgood ystd3i da w yzher al messege di
        return 'ali not exist  `{}`.'.format(str(name))
    def __setattr__(self,name, value) :
        self.__dict__[name] = value.lower()#bistd3i lma nd5l al value in attrubite of class
    def __delattr__(self,name) :
        del self.__dict__[name]
        return 'deleting  `{}`.'.format(str(name))
    def __unicode__(self):#biwa7d al no3
        return self.name
    
        
        
 
ha= noha('Ali')
print(ha.mohmod)
print(ha.Ali)
print(type(ha.Ali))

#__str__() change integer to string
class vehicle():
    def __init__(self,speed,color):
        self.color =color
        self.speed=speed
    def what_color(self):
        print('my color is:'+self.color)
    def drive(self):
        print('driving with speed:'+ str(self.speed))#change speed to string
    
hundai = vehicle (100,"red")
hundai.drive()
hundai.what_color()
print(hundai.color)


#__new__ new of object and called before __init__ method
class Employee:
    def __new__(cls):
        print ("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst
    def __init__(self):
        print ("__init__ magic method is called")
        self.name='Satya' 

#__ge__ used with >= operator and return true or false
class distance:
    def __init__(self, x=None,y=None):
        self.ft=x
        self.inch=y
    def __ge__(self, x):
        val1=self.ft*12+self.inch
        val2=x.ft*12+x.inch
        if val1>=val2:
            return True
        else:
            return False
d1=distance(2,1)
d2=distance(4,10)
print(d2>=d1)


#__eq__(self, other) ==operator return true or false
#__lt__ (self, other)< operator return true or false
#__le__(self, other) <=operator return true or false
#__ne__(self, other) !=operator return true or false

class Compare:
    def __init__(self, a):
        self.a = a
    def __eq__(self, object2):
        return self.a == object2.a
    def __lt__(self, object3):
        return self.a < object3.a
    def __le__(self, object4):
        return self.a <= object4.a
    def __ne__(self, object5):
        return self.a != object5.a
a=Compare(5)
b=Compare(5)
print(a==b)
print(a<b)
print(a<=b)
print(a!=b)








#__del__ delete  method
class sss:
    b = 5
    def func(self):
        print('Hello')
print(sss)
del sss
#print(sss)#error becouse class deleted

#__getitem__ return items
class A:
    def __init__(self, item):
        self.item = item
    def __getitem__(self, index):
        return self.item[index]
a = A([5, 2, 3])
print(f"First item: {a[0]}")
print(f"Second item: {a[1]}")
print(f"Third item: {a[2]}")

#size of return size of an object
w =[1, 2]
print(w.__sizeof__())

#__repr__ return string

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        rep = 'Person(' + self.name + ',' + str(self.age) + ')'
        return rep
person = Person("sevo", 21)
print(repr(person))

#To get called on right bitwise shift with assignment 
class Data:
    def __lshift__(self, other):
        return '42'
x = Data()
y = Data()
x <<= y
print(x)











