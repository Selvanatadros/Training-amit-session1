
from pydoc import classname


def myFun(arg1, arg2, arg3):#bia5d akter mn variable lkn al kwargs lazm m3ah key
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = ("Geeks", "for", "Geeks")
myFun(*args)#* 3shan a5d 3dd mn al mot8irat
  
kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)

#abstraction
#  process of handling complexity by hiding unnecessary information from the user
#from abc import ABC  
#class ClassName(ABC):  


#encapsulation (private)
class rectangle:
    __length =0 #protected no
    __breadth=0
    def __init__(self):
        self.__length=5
        self.__breadth=3
        print(self.__length)#print al arkam ali gwa al fun minf3sh tba3t al 5arg al fun 3shan hia protected no
        print(self.__breadth)
rec =rectangle()
print(rec.__length)
print(rec.__breadth)
