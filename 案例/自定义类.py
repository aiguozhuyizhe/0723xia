#自己组装一个类
from types import MethodType
class A():
    pass

def say(self):
    print("Saying.....")
class B():
    def say(self):
        print("Saying.....")
#方法1
say(5)
#方法2
A.say=say
a=A()
a.say()
#方法3
b=B()
b.say()
#方法4
a=A()
a.say=MethodType(say,A)
a.say()