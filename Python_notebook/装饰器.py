类的内置装饰器
类的成员函数第一个参数称为self，类的实例的指针
1、@staticmethod  类静态方法
使一个成员函数变成    静态成员方法，可以在类不进行实例化的情况下被调用

类的对象直接调用成员函数时，会隐形的传递一个参数self指向该对象；如果某个成员函数不需要self参数，则可以使用该装饰器修饰

2、@classmethod   类方法
与成员函数的区别在于所接收的第一个参数不是self，而是cls（当前类的具体类型），即可以直接使用通过类名直接调用该方法

3、@property   属性方法
将一个成员函数变成类的一个只读属性（即成员变量），如果想设置类的成员变量，则可以通过装饰器的内置方法 setter修饰set方法
                                
