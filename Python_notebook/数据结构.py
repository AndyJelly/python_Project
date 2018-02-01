tuple  元组  不可变的对象immutable  iterable
name_tuple= ('Andy1','Andy2')
name_tuple[0] = 'Andy3'   不可行

tuple拆包
name_tuple= ('Andy1','Andy2',23,'dhkjh','uenj')
name,*other = name_tuple
other
['Andy2', 23, 'dhkjh', 'uenj']

tuple与list比较
1、不可变 mutable,编译时就可以将值确定
2、可以作为dict的key值，即可hash

namedtuple   类似与类的用法，代码更加简洁
from collections import namedtuple
User = namedtuple("user",['name','age','height'])
user_tuple = ('Andy',23,180)
user = User(*user_tuple,edu = 'master')  可以使用一个tuple生成一个namedtuple
#user= User(name= 'Andy',age=29,height=180)
print(user.name,user.age,user.height)

user_dict  =  { 
    'name' :'Andy',
    'age' : 28,
    'height':190
}
#可以使用dict构造出一个namedtuple
user2 = User(**user_dict,edu = 'master')


defaultdict   C语言实现，效率很高
from collections import defaultdict
user_dict ={}
users = ['Andy1','Andy2','Andy2','Andy1','Andy3','Andy2']
#dafault_dict = defaultdict(int)
for user in users:
    if user not in user_dict:
        user_dict[user] = 1
    else:
        user_dict[user] +=1
                                    #或者设置默认值，user为key，0为Value，效率更高，少做一次查询
                                    user_dict.setdefault(user,0)
    user_dict[user] +=1
                                #使用有默认值得dict
                                        dafault_dict[user] +=1
print (user_dict)
{'Andy1': 2, 'Andy2': 3, 'Andy3': 1}

defaultdict中嵌套dict
def gen_default():
    return {
        'name':'',
        'num' : 0
          }
dafault_dict = defaultdict(gen_default)
print (dafault_dict['group'])
{'name': '', 'num': 0}


deque  双端队列  线程安全的，list不是线程安全的
list 的pop函数，从尾部进行弹出
append将数据加到队列的尾部
appendleft  将数据加到队列头部
from collections import deque
user_deque = deque(['Andy1','Andy2','Andy3','Andy4'])
user_deque.appendleft('Andy8')
print(user_deque)
copy 浅拷贝数据
from collections import deque
user_deque = deque(['Andy1',['Andy2','Andy3'],'Andy4'])
user_deque2 = user_deque.copy()
user_deque2[1].append('Andy8')
print(user_deque)
print(user_deque2)
对于队列中包含列表类型的数据，copy之后对拷贝之后的数据的修改，将会改变原来的数据
使用python自带的copy进行深拷贝
from collections import deque
import copy
user_deque = deque(['Andy1',['Andy2','Andy3'],'Andy4'])
user_deque2 = copy.deepcopy(user_deque)
user_deque2[1].append('Andy8')
print(user_deque)
print(user_deque2)
extend 扩展，或者说合并两个deque，返回值为None，在当前的确中进行修改
insert 在指定位置插入值


Counter统计出现次数
from collections import Counter
users = ['Andy1','Andy2','Andy2','Andy1','Andy3','Andy2']
user_counter = Counter(users)
print(user_counter)
Counter({'Andy2': 3, 'Andy1': 2, 'Andy3': 1})
user_counter = Counter('userjdajdoqj[slaios')#也可以直接统计字符串
print(user_counter)
Counter({'s': 3, 'j': 3, 'd': 2, 'a': 2, 'o': 2, 'u': 1, 'e': 1, 'r': 1, 'q': 1, '[': 1, 'l': 1, 'i': 1})

update   追加需要统计的内容
user_counter = Counter('userjdajdoqj[slaios')
user_counter.update('jfogiwjfo')
print(user_counter)
#也可以直接update一个Counter
user_counter2 = Counter('jfogiwjfo')
user_counter.update(user_counter2)

most_common        取出出现次数最多的  top n的问题
print(user_counter.most_common(2))

OrderedDict  顺序指的是添加的先后顺序
python2中dict默认是无序的，python3中默认是有序的
popitem  将会把key，value都弹出
pop 只会返回value，参数必须传入key
move_to_end  将指定的key对应的值，放到dict最后


ChainMap  链接两个dict，可以直接使用一个for循环，遍历两个map
对于两个dict中相同的key，只会返回其中的一个
from collections import ChainMap
user_dict1 = {'a': 'Andy1','b':'Andy2'}
user_dict2 = {'b': 'Andy3','c':'Andy4'}
chain_map = ChainMap(user_dict1,user_dict2)
for key,value in chain_map.items():
    print(key,value)
c Andy4
b Andy2
a Andy1
