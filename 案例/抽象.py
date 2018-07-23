#在子类中实现功能，不在父类中实现

class Animal():
    def sayHello(self):#这个函数一定要有，但不用加功能，防止子类功能出错，这就叫抽象类
       pass

class  Dog(Animal):
    def sayHello(self):
      print("闻味道")
class Person(Animal):
    def sayHello(self):
       print("kiss me")


d=Dog()
d.sayHello()

p=Person()
p.sayHello()