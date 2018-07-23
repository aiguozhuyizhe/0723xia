class A():
    def __init__(self):
        self.name =  "haha"
        self.age =18


a=A()
# 属性的三种用法
#1， 赋值
#2  读取
#3 删除
a.name="xiaojia"#赋值
print(a.name)#读取
del a.name# 删除