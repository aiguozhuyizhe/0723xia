#先定义类应该具有的成员函数
class A():
    pass
def say(self):
         print("Saying....")

def talk(self):
    print("talking....")

#用Type来创建一个类
#BName是类的名字，A是父类名，注意a后面的逗号一定要，然后是dict，键值对
B= type("BName",(A,),{"class_say":say,"class_talk":talk})

#然后可以像正常访问一样使用

b=B()
b.class_say()
b.class_talk()