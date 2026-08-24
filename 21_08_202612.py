Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> count = 1
>>> while count <= 5:
...     print(count)
...     count += 1
... 
...     
1
2
3
4
5
>>> print("Done!")
Done!
>>> count = 1
>>> while count <= 5:
... print(count)
SyntaxError: expected an indented block after 'while' statement on line 1
>>> cats = ["Tom","Whiskers","Luna"]
>>> 
>>> for cat in cats:
...     print(cat, "says meow")
... 
...     
Tom says meow
Whiskers says meow
Luna says meow
>>> for letter in "AI":
...     print(letter)
... 
...     
A
I
>>> cats = ['Tom', 'whiskers', 'luna']
>>> 
>>> for cat in cats:
...     print(cat, 'says meow')
... 
...     
Tom says meow
whiskers says meow
luna says meow
>>> for letter in 'AI'
SyntaxError: expected ':'
>>> for letter in 'AI':
...     print(letter)

    
A
I
numbers = [0,0,2,4,6,8]
while num in numbers:
    if num == 0:
        numbers.remove(0)
        print(numbers)

        
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    while num in numbers:
NameError: name 'num' is not defined. Did you mean: 'sum'?
for day in range(1,5):
    print("Day", day)

    
Day 1
Day 2
Day 3
Day 4
for num in range (1, 6):
    if num == 3:
        pass
    print(num)

    
1
2
3
4
5
for num in range (1, 6):
    if num == 3:
        continue
    print(num)

    
1
2
4
5
for num in [2,4,6,8]:
    if num % 2 != 0:
        break

    
else:
    
SyntaxError: invalid syntax
given numbers = [4, 9, 15, 22, 7, 3, 18]
SyntaxError: invalid syntax
numbers = [4, 9, 15, 22, 7, 3, 18]
for num in range (0, 30, 3):
    print(num)

    
0
3
6
9
12
15
18
21
24
27
