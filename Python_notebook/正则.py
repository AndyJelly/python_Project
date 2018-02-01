import re
re.compile(r'imooc\n')                                                r的作用就是使用原始字符串进行匹配，没有r，遇到\n就必须写成'\\n'
调用compile方法之后，就会生成一个PAttern的对象
_sre.SRE_Pattern，然后就可以进行Match和Search

Match从字符串的起始位置进行匹配


import re 
str = 'Imooc python'
print (str.startswith('imooc'))
pa = re.compile(r'imooc',re.I)                                #re.I表示不区分大小写
ma = pa.match(str)
if ma:
    print (ma.group())
else:
    print ('not match')

 pa = re.compile(r'(imooc)',re.I)                                        #正则表达式写成（）形式的，groups返回的是元组
 print (ma.groups())
('Imooc',)
 print (ma.groups()[0])
Imooc


以上是先生成一个Pattern的对象，然后调用Match进行匹配，
match(pattern, string, flags=0)
起始也可以直接使用Match进行匹配，即：
re.match(r'imooc',str)    这种情况下，每match一次，都会生成一个Pattern对象


search 匹配子串  只能匹配到第一个符合要求的结果

findall 可以找到所有的匹配结果  返回是一个列表

sub替换
sub(pattern, repl, string, count=0, flags=0)

str = 'hdah 678dd778dnkln'
info = re.sub(r'\d+','666',str)

repl还可以是一个函数，表示对match到的结果，进行一些操作，使用操作结果替换
import re 
str_sub = 'dhui678hdcuia0238'
def add_one(match):
    return str(int(match.group()) + 1)
sub_str = re.sub(r'\d+',add_one,str_sub)
print (sub_str)


split 分割  比字符串的分割更加灵活
str_split = 'immoc:C C++  JAVA,Python GO'
split_str = re.split(r':| |,',str_split)
print (split_str)

