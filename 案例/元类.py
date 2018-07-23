#元类是类，元类的写法是固定的，必须继承自type
#元类一般命名以MetaClass结尾
class xjMetaClass(type):
    #注意以下写法
    def __new__(cls,name,bases,attrs):
        #自己的业务处理
        print("哈哈哈，我是元类")
        attrs['id']='000000'#属性
        attrs['addr']="明溪"#属性
        return  type.__new__(cls,name,bases,attrs)

#元类定义玩就可以使用，使用注意写法
class Teacher(object,metaclass=xjMetaClass):
    pass



t=Teacher()
print(t.id,t.addr)