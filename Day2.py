## Day2 is for listing
from numpy import sort
from pyparsing import WordStart
from sklearn.neighbors import KNeighborsTransformer


colors = ['red', 'blue', 'green']
print(colors[0])
print(colors[1])

b = colors
squares = [1, 4, 9, 16]
sum = 0

for num in squares:
    sum += num
print(sum)

list = ['a', 'b', 'c']
if 'a' in list:
    print('yay')

for i in range(100):
    print(i)


i = 0
while i < len(a):
    print(a[i])
    i = i + 2

list = ['larry', 'curly', 'moe']
list.append('shemp')
list.insert(0, 'xxx')
list.extend(['yyy', 'zzz'])
list.index('curly')
list.remove('curly')
# list.sort()
list.pop(1)

list = ['a', 'b', 'c', 'd']
print(list[1:-1])   ## ['b', 'c']
list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print(list)         ## ['z', 'c', 'd']


1%2 == 1//2

words = 'words'
words[0] == 'w'

a = [(1,2,3),(1)]
a[0][1]

a[0] == a[1]