Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: /Users/maco/Desktop/Python/demo/nihao.py ==============
请输入一个正整数：
Traceback (most recent call last):
  File "/Users/maco/Desktop/Python/demo/nihao.py", line 9, in <module>
    number = int(input('请输入一个正整数：'))
ValueError: invalid literal for int() with base 10: ''
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> def fab(n):
	n1 = 1
	n2 = 1
	n3 = 1

	
>>> 
=============================================== RESTART: /Users/maco/Documents/小兔崽子.py ===============================================
Traceback (most recent call last):
  File "/Users/maco/Documents/小兔崽子.py", line 20, in <module>
    result = fad(20)
NameError: name 'fad' is not defined
>>> 
=============================================== RESTART: /Users/maco/Documents/小兔崽子.py ===============================================
总共有6765对小兔崽子诞生！
>>> 
========================================== RESTART: /Users/maco/Desktop/Python/demo/小兔崽子2.py =========================================
总共有6765对小兔崽子诞生！
>>> 
========================================== RESTART: /Users/maco/Desktop/Python/demo/小兔崽子3.py =========================================
总共有6765对小兔崽子诞生！
>>> 
========================================== RESTART: /Users/maco/Desktop/Python/demo/小兔崽子3.py =========================================
总共有9227465对小兔崽子诞生！
>>> 
================================================ RESTART: /Users/maco/Documents/汉诺塔.py ===============================================
请输入汉诺塔的层数：
================================================ RESTART: /Users/maco/Documents/汉诺塔.py ===============================================
请输入汉诺塔的层数：3
x --> z
x --> y
z --> y
x --> z
y --> x
y --> z
x --> z
>>> 
================================================ RESTART: /Users/maco/Documents/汉诺塔.py ===============================================
请输入汉诺塔的层数：4
x --> y
x --> z
y --> z
x --> y
z --> x
z --> y
x --> y
x --> z
y --> z
y --> x
z --> x
y --> z
x --> y
x --> z
y --> z
>>> brand = ['李宁', '耐克', '阿迪达斯', '鱼c工作室']
>>> slogan = ['一切皆有可能', 'Just do it', 'Impossible is nothing', '让编程改变世界']
>>> print('鱼c工作室的口号是：', slogan[brand.index('鱼c工作室')])
鱼c工作室的口号是： 让编程改变世界
>>> dict1 = {'李宁':'一切皆有可能', '耐克':'Just do it','阿迪达斯':'Impossible is nothing', '鱼c工作室':'让编程改变世界'}
>>> print('鱼c工作室的口号是：', dicti1['鱼c工作室'])
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print('鱼c工作室的口号是：', dicti1['鱼c工作室'])
NameError: name 'dicti1' is not defined
>>> print('鱼c工作室的口号是：', dict1['鱼c工作室'])
鱼c工作室的口号是： 让编程改变世界
>>> dict2 = {1:'one', 2:'two', 3:'three'}
>>> dict2
{1: 'one', 2: 'two', 3: 'three'}
>>> dict2[2]
'two'
>>> dict3 = {}
>>> dict3
{}
>>> help(dict)
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the dict keys.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      
 |      If key is not found, default is returned if given, otherwise KeyError is raised
 |  
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |      
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> dict3 = dict((('F',70),('i',105), ('s',115), ('h',104), ('c',67)))
>>> dict3
{'F': 70, 'i': 105, 's': 115, 'h': 104, 'c': 67}
>>> dict4 = dict(小甲鱼='让编程改变世界', 苍井空='让AV征服所有宅男')
>>> dict4
{'小甲鱼': '让编程改变世界', '苍井空': '让AV征服所有宅男'}
>>> dict4['苍井空'] = '123456897'
>>> dict4
{'小甲鱼': '让编程改变世界', '苍井空': '123456897'}
>>> dict4['苍井空'] ='让AV征服所有宅男'
>>> dict4
{'小甲鱼': '让编程改变世界', '苍井空': '让AV征服所有宅男'}
>>> dict4 = dict(小甲鱼='1234', 苍井空='abc')
>>> dict4
{'小甲鱼': '1234', '苍井空': 'abc'}
>>> dict4 = dict(小甲鱼='abc', 苍井空='123')
>>> dict4
{'小甲鱼': 'abc', '苍井空': '123'}
>>> dict4 = dict(小甲鱼='abc', 苍井空='aaa')
>>> dict4
{'小甲鱼': 'abc', '苍井空': 'aaa'}
>>> dict4 = dict(a小甲鱼='abc', b苍井空='aaa')
>>> dict4
{'a小甲鱼': 'abc', 'b苍井空': 'aaa'}
>>> dict4 = dict(b小甲鱼='abc', a苍井空='aaa')
>>> dict4
{'b小甲鱼': 'abc', 'a苍井空': 'aaa'}
>>> dict4['b小甲鱼']='dudu'
>>> dict4
{'b小甲鱼': 'dudu', 'a苍井空': 'aaa'}
>>> dict4['a苍井空']='bbbb'
>>> dict4
{'b小甲鱼': 'dudu', 'a苍井空': 'bbbb'}
>>> help(dict)
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the dict keys.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      
 |      If key is not found, default is returned if given, otherwise KeyError is raised
 |  
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |      
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> dict4['爱迪生'] = '天才就是99%的汗水+1%灵感，但这1%的灵感远远比99%的汗水更重要、'
>>> dict4['爱迪生'] = '天才就是99%的汗水+1%灵感，但这1%的灵感远远比99%的汗水更重要'
>>> dict4
{'b小甲鱼': 'dudu', 'a苍井空': 'bbbb', '爱迪生': '天才就是99%的汗水+1%灵感，但这1%的灵感远远比99%的汗水更重要'}
>>> dict5 = {}
>>> dict5.fromkeys((1, 2, 3), 'Number')
{1: 'Number', 2: 'Number', 3: 'Number'}
>>> dict5.fromkeys((1, 2, 3), ('one', 'two', 'three'))
{1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'), 3: ('one', 'two', 'three')}
>>> dict5.fromkeys((1, 3), '数字')
{1: '数字', 3: '数字'}
>>> dict5 = dict5.fromkey(range(32), '赞')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    dict5 = dict5.fromkey(range(32), '赞')
AttributeError: 'dict' object has no attribute 'fromkey'
d
>>> i
>>> dict5 = dict5.fromkeys(range(32), '赞')
>>> dict5
{0: '赞', 1: '赞', 2: '赞', 3: '赞', 4: '赞', 5: '赞', 6: '赞', 7: '赞', 8: '赞', 9: '赞', 10: '赞', 11: '赞', 12: '赞', 13: '赞', 14: '赞', 15: '赞', 16: '赞', 17: '赞', 18: '赞', 19: '赞', 20: '赞', 21: '赞', 22: '赞', 23: '赞', 24: '赞', 25: '赞', 26: '赞', 27: '赞', 28: '赞', 29: '赞', 30: '赞', 31: '赞'}
>>> for eachKey in dict5.keys():
	print(eachKey)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
>>> for eachValue in dict1.values():
	print(eachValue)

	
一切皆有可能
Just do it
Impossible is nothing
让编程改变世界
>>> for eachValue in dict5.values():
	print(eachValue)

	
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
>>> for eachItem in dict5.items():
	print(eachItem)

	
(0, '赞')
(1, '赞')
(2, '赞')
(3, '赞')
(4, '赞')
(5, '赞')
(6, '赞')
(7, '赞')
(8, '赞')
(9, '赞')
(10, '赞')
(11, '赞')
(12, '赞')
(13, '赞')
(14, '赞')
(15, '赞')
(16, '赞')
(17, '赞')
(18, '赞')
(19, '赞')
(20, '赞')
(21, '赞')
(22, '赞')
(23, '赞')
(24, '赞')
(25, '赞')
(26, '赞')
(27, '赞')
(28, '赞')
(29, '赞')
(30, '赞')
(31, '赞')
>>> print(dict5[31])
赞
>>> print(dict5[32])
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print(dict5[32])
KeyError: 32
>>> dict5.get(32)
>>> print(dict5.get(32))
None
>>> dict5.get(32, '木有！')
'木有！'
>>> dict5.get(31, '木有！')
'赞'
>>> 31 in dict5
True
>>> 32 in dict5
False
>>> dict5
{0: '赞', 1: '赞', 2: '赞', 3: '赞', 4: '赞', 5: '赞', 6: '赞', 7: '赞', 8: '赞', 9: '赞', 10: '赞', 11: '赞', 12: '赞', 13: '赞', 14: '赞', 15: '赞', 16: '赞', 17: '赞', 18: '赞', 19: '赞', 20: '赞', 21: '赞', 22: '赞', 23: '赞', 24: '赞', 25: '赞', 26: '赞', 27: '赞', 28: '赞', 29: '赞', 30: '赞', 31: '赞'}
>>> dict5.clear()
>>> dict5
{}
>>> dict5 = {}
>>> a = {'姓名':'小甲鱼'}
>>> b = a
>>> b
{'姓名': '小甲鱼'}
>>> a = {}
>>> a
{}
>>> b
{'姓名': '小甲鱼'}
>>> a = b
>>> a
{'姓名': '小甲鱼'}
>>> b
{'姓名': '小甲鱼'}
>>> a.clear()
>>> a
{}
>>> b
{}
>>> dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> a = {1:'one', 2:'two', 3:'three'}
>>> b = a.copy()
>>> c = a
>>> c
{1: 'one', 2: 'two', 3: 'three'}
>>> a
{1: 'one', 2: 'two', 3: 'three'}
>>> b
{1: 'one', 2: 'two', 3: 'three'}
>>> id(a)
4413702976
>>> id(b)
4413595264
>>> id(c)
4413702976
>>> c[4] = 'four'
>>> c
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
>>> a
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
>>> b
{1: 'one', 2: 'two', 3: 'three'}
>>> a.pop(2)
'two'
>>> a
{1: 'one', 3: 'three', 4: 'four'}
>>> a.popitem()
(4, 'four')
>>> a
{1: 'one', 3: 'three'}
>>> a.setdefault('小白')
>>> a
{1: 'one', 3: 'three', '小白': None}
>>> a.setdefault(5, 'five')
'five'
>>> a
{1: 'one', 3: 'three', '小白': None, 5: 'five'}
>>> b = {'小白': '狗'}
>>> a.update(b)
>>> a
{1: 'one', 3: 'three', '小白': '狗', 5: 'five'}
>>> num = {}
>>> type(num)
<class 'dict'>
>>> unm2 = {1, 2, 3, 4, 5}
>>> type(num2)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    type(num2)
NameError: name 'num2' is not defined
>>> nnm2 = {1, 2, 3, 4, 5}
>>> num2 = {1, 2, 3, 4, 5}
>>> type(num2)
<class 'set'>
>>> num2 = {1, 2, 3, 4, 5, 5, 4, 3, 2}
>>> num2
{1, 2, 3, 4, 5}
>>> num2[2]
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    num2[2]
TypeError: 'set' object is not subscriptable
>>> set1 = set([1, 2, 3, 4, 5, 5, 4, 3, 2])
>>> set1 = set([1, 2, 3, 4, 5, 5])
>>> set1
{1, 2, 3, 4, 5}
>>> num1 = [1, 2, 3, 4, 5, 5, 3, 1, 0]
>>> temp = []
>>> for each in num1:
	if each not in temp:
		temp.append(each)

		
>>> temp
[1, 2, 3, 4, 5, 0]
>>> num1 = list(set(num1))
>>> num1
[0, 1, 2, 3, 4, 5]
>>> num2
{1, 2, 3, 4, 5}
>>> 1 in num2
True
>>> '1' in num2
False
>>> num2
{1, 2, 3, 4, 5}
>>> num2.add(6)
>>> num2
{1, 2, 3, 4, 5, 6}
>>> num2.remove(5)
>>> num2
{1, 2, 3, 4, 6}
>>> num3 = frozenset()
>>> num3 = frozenset([1, 2, 3, 4, 5])
>>> num3.add(0)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    num3.add(0)
AttributeError: 'frozenset' object has no attribute 'add'
>>> help(open)
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise OSError upon failure.
    
    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)
    
    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:
    
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
    
    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.
    
    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.
    
    'U' mode is deprecated and will raise an exception in future versions
    of Python.  It has no effect in Python 3.  Use newline to control
    universal newlines mode.
    
    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:
    
    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.
    
    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.
    
    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.
    
    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register or run 'help(codecs.Codec)'
    for a list of the permitted encoding error strings.
    
    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:
    
    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.
    
    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.
    
    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.
    
    A custom opener can be used by passing a callable as *opener*. The
    underlying file descriptor for the file object is then obtained by
    calling *opener* with (*file*, *flags*). *opener* must return an open
    file descriptor (passing os.open as *opener* results in functionality
    similar to passing None).
    
    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.
    
    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.

>>> help(dict)
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the dict keys.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      
 |      If key is not found, default is returned if given, otherwise KeyError is raised
 |  
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |      
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> open('1:\')
     
SyntaxError: EOL while scanning string literal
>>> f = open('1:\\record.txt')
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    f = open('1:\\record.txt')
FileNotFoundError: [Errno 2] No such file or directory: '1:\\record.txt'
>>> f = open('E:\\record.txt')
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    f = open('E:\\record.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'E:\\record.txt'
>>> ls
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> f = open('/Users/maco/Desktop/record.txt')
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    f = open('/Users/maco/Desktop/record.txt')
FileNotFoundError: [Errno 2] No such file or directory: '/Users/maco/Desktop/record.txt'
>>> f = open('/Users/maco/Desktop/record.txt')
>>> f
<_io.TextIOWrapper name='/Users/maco/Desktop/record.txt' mode='r' encoding='UTF-8'>
>>> f.read()
''
>>> f.read()
'\nPython 字典 popitem() 方法返回并删除字典中的最后一对键和值。\n如果字典已经为空，却调用了此方法，就报出 KeyError 异常。\n语法'
>>> f.read()
''
>>> f.close()
>>> f = open('/Users/maco/Desktop/record.txt')
>>> f.read(5)
'\nPyth'
>>> f.tell()
5
>>> f.seek(45, 0)
45
>>> f.readline()
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    f.readline()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa4 in position 0: invalid start byte
>>> f.close()
>>> f = open('/Users/maco/Desktop/record.txt')
>>> f.read()
'\nPython 字典 popitem() 方法返回并删除字典中的最后一对键和值。\n如果字典已经为空，却调用了此方法，就报出 KeyError 异常。\n语法\n如果字典已经为空，却调用了此方法，就报出 KeyError 异常。\n语法'
f
>>> f.seek(45, 0)
45
>>> f.readline()
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    f.readline()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa4 in position 0: invalid start byte
>>> f.seek(40, 0)
40
>>> f.readline()
'删除字典中的最后一对键和值。\n'
>>> f.seek(41, 0)
41
>>> f.readline()
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    f.readline()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x88 in position 0: invalid start byte
>>> f.seek(42, 0)
42
>>> f.readline()
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    f.readline()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 0: invalid start byte
>>> f = open('/Users/maco/Desktop/record.txt')
>>> f.seek(42, 0)
42
>>> f.readline()
'除字典中的最后一对键和值。\n'
>>> list(f)
['如果字典已经为空，却调用了此方法，就报出 KeyError 异常。\n', '语法\n', '如果字典已经为空，却调用了此方法，就报出 KeyError 异常。\n', '语法\n', 'Traceback (most recent call last):\n', '  File "<pyshell#174>", line 1, in <module>\n', '    f.readline()\n', '  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/codecs.py", line 322, in decode\n', '    (result, consumed) = self._buffer_decode(data, self.errors, final)\n', "UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 0: invalid start byte"]
>>> f.seek(0, 0)
0
>>> lines = list(f)
>>> for each_line in lines:
	print(each_line)

	
Python 字典 popitem() 方法返回并删除字典中的最后一对键和值。

如果字典已经为空，却调用了此方法，就报出 KeyError 异常。

语法

如果字典已经为空，却调用了此方法，就报出 KeyError 异常。

语法

Traceback (most recent call last):

  File "<pyshell#174>", line 1, in <module>

    f.readline()

  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/codecs.py", line 322, in decode

    (result, consumed) = self._buffer_decode(data, self.errors, final)

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 0: invalid start byte
>>> for each_line in lines:
	print(each_line)

	
Python 字典 popitem() 方法返回并删除字典中的最后一对键和值。

如果字典已经为空，却调用了此方法，就报出 KeyError 异常。

语法

如果字典已经为空，却调用了此方法，就报出 KeyError 异常。

语法

Traceback (most recent call last):

  File "<pyshell#174>", line 1, in <module>

    f.readline()

  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/codecs.py", line 322, in decode

    (result, consumed) = self._buffer_decode(data, self.errors, final)

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 0: invalid start byte
>>> f.seek(0, 0)
0
>>> for each_line in f:
	print(each_line)

	
Python 字典 popitem() 方法返回并删除字典中的最后一对键和值。

如果字典已经为空，却调用了此方法，就报出 KeyError 异常。

语法

如果字典已经为空，却调用了此方法，就报出 KeyError 异常。

语法

Traceback (most recent call last):

  File "<pyshell#174>", line 1, in <module>

    f.readline()

  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/codecs.py", line 322, in decode

    (result, consumed) = self._buffer_decode(data, self.errors, final)

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 0: invalid start byte
>>> f.write('I love Dudu')
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    f.write('I love Dudu')
io.UnsupportedOperation: not writable
>>> f = open('/Users/maco/Desktop/record.txt', 'w')
>>> 
>>> f.write('我爱爸爸妈妈')
6
>>> f.close()
>>> 
========================================= RESTART: /Users/maco/Desktop/Python/demo/dudu_hi.py ========================================
Traceback (most recent call last):
  File "/Users/maco/Desktop/Python/demo/dudu_hi.py", line 8, in <module>
    (role, line_spoken) = each_line.split(':', 1)
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
========================================= RESTART: /Users/maco/Desktop/Python/demo/dudu_hi.py ========================================
Traceback (most recent call last):
  File "/Users/maco/Desktop/Python/demo/dudu_hi.py", line 15, in <module>
    file_name_boy = 'boy_' + str(count) + '.txt'
NameError: name 'count' is not defined
>>> 
========================================= RESTART: /Users/maco/Desktop/Python/demo/dudu_hi.py ========================================
Traceback (most recent call last):
  File "/Users/maco/Desktop/Python/demo/dudu_hi.py", line 15, in <module>
    file_name_boy = 'boy_' + str(count) + '.txt'
NameError: name 'count' is not defined
>>> 
========================================= RESTART: /Users/maco/Desktop/Python/demo/dudu_hi.py ========================================
Traceback (most recent call last):
  File "/Users/maco/Desktop/Python/demo/dudu_hi.py", line 8, in <module>
    (role, line_spoken) = each_line.split(':', 1)
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
========================================= RESTART: /Users/maco/Desktop/Python/demo/dudu_hi.py ========================================
Traceback (most recent call last):
  File "/Users/maco/Desktop/Python/demo/dudu_hi.py", line 8, in <module>
    (role, line_spoken) = each_line.split(':', 1)
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
========================================= RESTART: /Users/maco/Desktop/Python/demo/dudu_hi.py ========================================
>>> import random
>>> secret = random.randint(1, 10)
>>> secret
4
>>> import os
>>> os.getcwd()
'/Users/maco/Desktop/Python/demo'
>>> os.getcwd('E:\\')
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    os.getcwd('E:\\')
TypeError: posix.getcwd() takes no arguments (1 given)
>>> os.chdir('E:\\')
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    os.chdir('E:\\')
FileNotFoundError: [Errno 2] No such file or directory: 'E:\\'
>>> os.chdir('/Users/maco/Desktop/Python/demo')
>>> os.getcwd()
'/Users/maco/Desktop/Python/demo'
>>> os.listdir('/Users/maco/Desktop/Python/demo')
['happy.py', 'score(分数).py', 'score2流程图   copy 2.drawio', '流程图.drawio', 'helloelse2.py', 'bien.py', 'bian.py', '.DS_Store', 'helloelse3.py', '汉诺塔.py', 'haha 2.py', 'helloelse.py', 'record.txt', 'dudu_hi.py', '嘟嘟.py', '小兔崽子1.py', 'haha.drawio', 'boy_1.txt', 'score-1.py', 'ok.py', '小兔崽子3.py', 'mama.py', 'test5.c', '循环流程图  .drawio', '小兔崽子2.py', 'holahola.py', 'nihao.py', '猜数游戏流程图 .drawio', 'haha.py', 'helloelse4.py', 'score流程图   copy.drawio', '温度转换流程图   .drawio', 'girl_1.txt']
>>> 
=========================================== RESTART: /Users/maco/Desktop/Python/demo/汉诺塔.py ==========================================
请输入汉诺塔的层数：3
Traceback (most recent call last):
  File "/Users/maco/Desktop/Python/demo/汉诺塔.py", line 10, in <module>
    hanoi(n, 'x', 'y', 'z')
  File "/Users/maco/Desktop/Python/demo/汉诺塔.py", line 5, in hanoi
    hanoj(n-1, x, z, y)#将前n-1个盘子从x移动到y上
NameError: name 'hanoj' is not defined
>>> 
=========================================== RESTART: /Users/maco/Desktop/Python/demo/汉诺塔.py ==========================================
请输入汉诺塔的层数：3
x --> z
x --> y
z --> y
x --> z
y --> x
y --> z
x --> z
>>> 
=========================================== RESTART: /Users/maco/Desktop/Python/demo/汉诺塔.py ==========================================
请输入汉诺塔的层数：4
x --> y
x --> z
y --> z
x --> y
z --> x
z --> y
x --> y
x --> z
y --> z
y --> x
z --> x
y --> z
x --> y
x --> z
y --> z
>>> os.mkdir('E:\\A')
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    os.mkdir('E:\\A')
NameError: name 'os' is not defined
>>> os.mkdir('A')
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    os.mkdir('A')
NameError: name 'os' is not defined
>>> import os
>>> os.getcwd()
'/Users/maco/Desktop/Python/demo'
>>> os.chidr('/Users/maco/Desktop/Python/demo')
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    os.chidr('/Users/maco/Desktop/Python/demo')
AttributeError: module 'os' has no attribute 'chidr'
>>> os.chdir('/Users/maco/Desktop/Python/demo')
>>> os.getcwd()
'/Users/maco/Desktop/Python/demo'
>>> os.listdir('/Users/maco/Desktop/Python/demo')
['happy.py', 'score(分数).py', 'score2流程图   copy 2.drawio', '流程图.drawio', 'helloelse2.py', 'bien.py', 'bian.py', '.DS_Store', 'helloelse3.py', '汉诺塔.py', 'haha 2.py', 'helloelse.py', 'record.txt', 'dudu_hi.py', '嘟嘟.py', '小兔崽子1.py', 'haha.drawio', 'boy_1.txt', 'score-1.py', 'ok.py', '小兔崽子3.py', 'mama.py', 'test5.c', '循环流程图  .drawio', '小兔崽子2.py', 'holahola.py', 'nihao.py', '猜数游戏流程图 .drawio', 'haha.py', 'helloelse4.py', 'score流程图   copy.drawio', '温度转换流程图   .drawio', 'girl_1.txt']
>>> os.mkdir('')