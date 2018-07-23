#应用场景：
#对变量出了普通的三种操作，还想增加一些附加的操作，那么可以通过property来实现
class A():
    def __init__(self):
        self.name =  "xiaojia"
        self.age =18

    #此功能，是对类变量进行读取曹组偶的时候应该执行的函数功能
    def fget(self):
        print("我被读取了")
        return self._name
    #模拟的是对变量进行写操作的时候执行的功能
    def fset(self,name):
        print("我被写入了，但是还可以做好多事情")
        self.name = "你好:"+name
    #模拟删除变量的时候进行给的操作
    def fdel(self):
        pass
    #property的四个参数顺序是固定的
    #第一个参数代表读取的时候调用的函数
    #第二个参数代表写入的时候需要调用的函数
    #第三个是删除
    name2=property(fget,fset,fdel,"这是一个property例子")
a=A()
print(a.name)

print(a.name2)
