```
Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def MyFirstfunction(name):
	'函数定义过程中的name是叫形参'
	#因为Ta只是一个形式，表示占据一个参数位置
	print('传递进来的' + name + '叫做实参，因为Ta是具体的参数值！')

	
>>> MyFirstfunction('小甲鱼')
传递进来的小甲鱼叫做实参，因为Ta是具体的参数值！
>>> MyFirstfunction()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    MyFirstfunction()
TypeError: MyFirstfunction() missing 1 required positional argument: 'name'
>>> MyFirstfunction._doc_
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    MyFirstfunction._doc_
AttributeError: 'function' object has no attribute '_doc_'
>>> 
MyFirstfunction
<function MyFirstfunction at 0x10d72e310>
>>> MyFirstfunction.__doc__
'函数定义过程中的name是叫形参'
>>> def MyFirstfunction(name):
	'函数定义过程中的name是叫形参'
	#因为Ta只是一个形式，表示占据一个参数位置
	print('传递进来的' + name + '叫做实参，因为Ta是具体的参数值！')

	
>>> MyFirstfunction('雷玉琼')
传递进来的雷玉琼叫做实参，因为Ta是具体的参数值！
>>> help(MyFirstFunction)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    help(MyFirstFunction)
NameError: name 'MyFirstFunction' is not defined
>>> help(MyFirstfunction)
Help on function MyFirstfunction in module __main__:

MyFirstfunction(name)
    函数定义过程中的name是叫形参

>>> print.__doc__
"print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)\n\nPrints the values to a stream, or to sys.stdout by default.\nOptional keyword arguments:\nfile:  a file-like object (stream); defaults to the current sys.stdout.\nsep:   string inserted between values, default a space.\nend:   string appended after the last value, default a newline.\nflush: whether to forcibly flush the stream."
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> def SaySome(name, words):
	print(name + '->' + words)

	
>>> SaySome('小甲鱼', '让变成改变世界！')
小甲鱼->让变成改变世界！
>>> SaySome('√让变成改变世界!', '小甲鱼')
√让变成改变世界!->小甲鱼
>>> SaySome('让变成改变世界!', '小甲鱼')
让变成改变世界!->小甲鱼
>>> SaySome(words='让变成改变世界!', name='小甲鱼')
小甲鱼->让变成改变世界!
>>> def SaySome(name='小甲鱼', words='让变成改变世界!'):
	print(name + '->' + words)

	
>>> SaySome()
小甲鱼->让变成改变世界!
>>> SaySome('苍井空')
苍井空->让变成改变世界!
>>> SaySome('苍井空', '5tggbaskjfg2fhj21549yifhfjzcx')
苍井空->5tggbaskjfg2fhj21549yifhfjzcx
>>> def test(*params)
SyntaxError: invalid syntax
>>> def test(*params):
	print('参数的长度是：', len(params));
	print('第二个参数是：', params[1]);

	
>>> test(1, '小甲鱼', 3.14, 5, 6, 7, 8)
参数的长度是： 7
第二个参数是： 小甲鱼
>>> def test(*params, exp):
	print('参数的长度是：', len(params), exp);
	print('第二个参数是：', params[1]);

	
>>> test(1, '小甲鱼', 3.14, 5, 6, 7, 8)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    test(1, '小甲鱼', 3.14, 5, 6, 7, 8)
TypeError: test() missing 1 required keyword-only argument: 'exp'
>>> test(1, '小甲鱼', 3.14, 5, 6, 7, exp = 8)
参数的长度是： 6 8
第二个参数是： 小甲鱼
>>> def test(*params, exp= 8):
	print('参数的长度是：', len(params), exp);
	print('第二个参数是：', params[1]);

	
>>> test(1, '小甲鱼', 3.14, 5, 6, 7, 8)
参数的长度是： 7 8
第二个参数是： 小甲鱼
>>> def hello():
	print('Hello FishC!')

	
>>> temp = hello()
Hello FishC!
>>> temp
>>> print(temp)
None
>>> type(temp)
<class 'NoneType'>
>>> def back():
	return [1, '小甲鱼', 3.14]

>>> back()
[1, '小甲鱼', 3.14]
>>> def back():
	return 1, '小甲鱼', 3.14

>>> back()
(1, '小甲鱼', 3.14)
>>> 
========================================== RESTART: /Users/maco/Desktop/Python/demo/bien.py ==========================================
请输入原价：100
请输入折扣率：8
打折后价格是： 800.0
>>> 
========================================== RESTART: /Users/maco/Desktop/Python/demo/bien.py ==========================================
请输入原价：100
请输入折扣率：0.8
打折后价格是： 80.0
>>> 
========================================== RESTART: /Users/maco/Desktop/Python/demo/bian.py ==========================================
请输入原价：100
请输入折扣率：0.8
这里试图打印全局变量old_price的值： 100.0
打折后价格是： 80.0
>>> cunut = 5
>>> def MyFun():
	cunut = 10
	print(10)

	
>>> MyFun()
10
>>> print(cunut)
5
>>> def MyFun():
	global cunut
	cunut = 10
	print(10)

	
>>> MyFun()'
SyntaxError: EOL while scanning string literal
>>> MyFun()
10
>>> print(cunut)
10
>>> def fun1():
	print('fun1()正在被调用...')
	def fun2():
		print('fun2()正在被调用...')
		fun2()

		
>>> fun1()
fun1()正在被调用...
>>> def fun1():
	print('fun1()正在被调用...')
	def fun2():
		print('fun2()正在被调用...')
	fun2()

	
>>> fun1()
fun1()正在被调用...
fun2()正在被调用...
>>> def Fun(x):
	def Fun(y):
		return x * y
	return FunY

>>> i = FunX(8)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    i = FunX(8)
NameError: name 'FunX' is not defined
>>> i = Fun(x)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    i = Fun(x)
NameError: name 'x' is not defined
>>> def FunX(x):
	def FunY(y):
		return x * y
	return FunY

>>> i = FunX(x)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    i = FunX(x)
NameError: name 'x' is not defined
>>> i = FunX(8)
>>> i
<function FunX.<locals>.FunY at 0x105ef8c10>
>>> type(i)
<class 'function'>
>>> i(5)
40
>>> FunX(8)(5)
40
>>> def Fun1():
	x = 5
	def Fun2():
		x *= x
		return x
	return Fun2

>>> Fun1()
<function Fun1.<locals>.Fun2 at 0x105ef8ca0>
>>> def Fun1():
	x = [5]
	def Fun2():
		x[0] *= x[0]
		return x[0]
	return Fun2()

>>> Fun1()
25
>>> def Fun1():
	x = [5]
	def Fun2():
		nonlocal x
		x *= x
		return x
	return Fun2()

>>> Fun1()
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    Fun1()
  File "<pyshell#106>", line 7, in Fun1
    return Fun2()
  File "<pyshell#106>", line 5, in Fun2
    x *= x
TypeError: can't multiply sequence by non-int of type 'list'
>>> def Fun1():
	x =5
	def Fun2():
		nonlocal x
		x *= x
		return x
	return Fun2()

>>> Fun1()
25
>>> def ds(x):
	return 2 * x + 1

>>> de(5)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    de(5)
NameError: name 'de' is not defined
>>> ds(5)
11
>>> lambda x : 2 * x + 1
<function <lambda> at 0x105ef8d30>
>>> g = lambda x : 2 * x + 1
>>> g(5)
11
>>> def add(x, y):
	return x + y

>>> add(3, 4)
7
>>> lambda x, y : x + y
<function <lambda> at 0x105ef8b80>
>>> g = lambda x, y : x + y
>>> g
<function <lambda> at 0x105ef84c0>
>>> g(3, 4)
7
>>> help(filter)
Help on class filter in module builtins:

class filter(object)
 |  filter(function or None, iterable) --> filter object
 |  
 |  Return an iterator yielding those items of iterable for which function(item)
 |  is true. If function is None, return the items that are true.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> filter(None, [1, 0, False, True])
<filter object at 0x105efe0d0>
>>> list(filter(None, [1, 0, False, True]))
[1, True]
>>> def add(x):
	return x % 2

>>> temp = range(10)
>>> show = filter(odd, temp)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    show = filter(odd, temp)
NameError: name 'odd' is not defined
>>> show = filter(add, temp)
>>> list(show)
[1, 3, 5, 7, 9]
>>> list(map(lambda x : x * 2, range(10)))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> def recursion():
	return recursion()

>>> recursion()
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    recursion()
  File "<pyshell#140>", line 2, in recursion
    return recursion()
  File "<pyshell#140>", line 2, in recursion
    return recursion()
  File "<pyshell#140>", line 2, in recursion
    return recursion()
  [Previous line repeated 1022 more times]
RecursionError: maximum recursion depth exceeded
>>> import sys
>>> sys.setrecursionlimit
<function setrecursionlimit at 0x108ced310>
>>> 

>>> sys.setrecursionlimit()
Traceback (most recent call last):
** IDLE Internal Exception: 
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/idlelib/run.py", line 327, in setrecursionlimit
    limit, = args
ValueError: not enough values to unpack (expected 1, got 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    sys.setrecursionlimit()
TypeError: setrecursionlimit() takes exactly one argument (0 given)
>>> sys.setrecursionlimit(1000000)
>>> sys.recursion(1000000)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    sys.recursion(1000000)
AttributeError: module 'sys' has no attribute 'recursion'
>>> recursion()

=========================================================== RESTART: Shell ===========================================================
>>> sys.setrecursionlimit(2000)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    sys.setrecursionlimit(2000)
NameError: name 'sys' is not defined
>>> sys.setrecursionlimit(1000000)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    sys.setrecursionlimit(1000000)
NameError: name 'sys' is not defined
>>> import sys
>>> sys.setrecursionlimit(1000000)
>>> recursion()
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    recursion()
NameError: name 'recursion' is not defined
>>> def recursion():
	return recursion()

>>> recursion()

=========================================================== RESTART: Shell ===========================================================
>>> 
```