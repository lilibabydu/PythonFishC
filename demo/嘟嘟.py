if "小明" != "小姐姐":
    print("小明是小姐姐！")
else:
    print("小明不是小姐姐！")



a={1: 'one', 3: 'three', 4: 'four'}
a.popitem()
(4, 'four')
>>> a
{1: 'one', 3: 'three'}
>>> a.setdefault('小白')
>>> a
{1: 'one', 3: 'three', '小白': None}