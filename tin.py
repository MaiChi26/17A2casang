Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dic_animals={1:"elephant",2:"dog",3:"duck",4:"bear",5:"ant"}
>>> print("length:",len(dic_animals))
length: 5
>>> print(type(dic_animals))
<class 'dict'>
>>> 
>>> convert_to_str = str(dic_animals)
>>> print(convert_to_str)
{1: 'elephant', 2: 'dog', 3: 'duck', 4: 'bear', 5: 'ant'}
>>> print(type(convert_to_str))
<class 'str'>
>>> # ví dụ 11.65
>>> d_animal={1:"elephant",2:"dog",3:"duck",4:"bear",5:"ant"}
>>> d_animal
{1: 'elephant', 2: 'dog', 3: 'duck', 4: 'bear', 5: 'ant'}
>>> type(d_animal)
<class 'dict'>
>>> ban_sao=d_animal.copy()
>>> 
>>> ban_sao
{1: 'elephant', 2: 'dog', 3: 'duck', 4: 'bear', 5: 'ant'}
>>> # yêus
>>> # yêu cầu chuyển các giá trị trong ban_sao thành chữ hoa?
>>> for i in ban_sao:
	ban_sao[i]=ban_sao[i].upper()
	print(i, ':', d_animal[i])

	
1 : elephant
2 : dog
3 : duck
4 : bear
5 : ant
>>> ban_sao
{1: 'ELEPHANT', 2: 'DOG', 3: 'DUCK', 4: 'BEAR', 5: 'ANT'}
>>> # bản gốc thì sao?
>>> d_animal
{1: 'elephant', 2: 'dog', 3: 'duck', 4: 'bear', 5: 'ant'}
>>> defxoa():
	
SyntaxError: invalid syntax
>>> # ví dụ 11.67
>>> list_1=["one","two","three","four"]
>>> d1=dict.fromkeys(list_1)
>>> # nội dung của d1 là gì?
>>> d1
{'one': None, 'two': None, 'three': None, 'four': None}
>>> d2=dict.fromkeys(list_1,15)
>>> d2
{'one': 15, 'two': 15, 'three': 15, 'four': 15}
>>> d1
{'one': None, 'two': None, 'three': None, 'four': None}
>>> d_animal
{1: 'elephant', 2: 'dog', 3: 'duck', 4: 'bear', 5: 'ant'}
>>> # muốn truy cập đến phân tử có key = 3 của d_animal?
>>> d_animal[3]
'duck'
>>> d_animal.get[3]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    d_animal.get[3]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> d_animal.get(3)
'duck'
>>> d_animal.get(7)
>>> print("phần tử có key=7 là",d_animal.get(7))
phần tử có key=7 là None
>>> # nhưng nếu lấy key=7 theo cách dùng chỉ số thì sao?
>>> d_animal[7]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    d_animal[7]
KeyError: 7
>>> # vậy cách truy cập chỉ số bằng get() KHÁC dùng chỉ số như thế nào?
