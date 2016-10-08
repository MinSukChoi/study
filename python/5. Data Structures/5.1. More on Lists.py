'''
List용례
1. list.append(x) : 항목 추가. a[len(a):] = [x]
2. list.extend(L) : list를 추가. a[len(a):] = L
3. list.insert(i,x) : i번째 위치에 x삽입
4. list.remove(x) : 값이 x인 첫번째 항목. 삭제 없으면 에러.
5. list.pop([i]) : i번째 위치의 항목을 제거하고 그것을 리턴한다. 인자가 없을때는 마지막 항목을 리턴
6. list.clear() : 모든 항목 제거
7. list.index(x) : 값이 x인 첫번째 항목의 위치 리턴. 없으면 에러
8. list.count(x) : 값이 x인 항목의 개수
9. list.sort(key=None, reverse=False) : 정렬
10. list.reverse() : 항목 순서 반전
11. list.copy() : list의 shallow copy를 리턴한다. a[:]
'''

a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))

a.insert(2, -1)
a.append(333)
print(a)

print(a.index(333))
a.reverse()
print(a)
a.sort()
print(a)
print(a.pop())
print(a.copy())

# 5.1.1 Using List as Stacks
'''
push = append()
pop = pop()
'''
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)

# 5.1.2 Using Lists as Queues
'''
collections.deque를 사용
'''
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(type(queue), queue)

# 5.1.3 List Comprehensions
'''
특정한 상황에서 리스트 생성을 간결하게 함
'''

squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)

squares = list(map(lambda x: x ** 2, range(10)))

print(squares)

squares = [x ** 2 for x in range(10)]

print(squares)

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)

vec = [-4, -2, 0, 2, 4]
print([x * 2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

print([(x, x ** 2) for x in range(6)])

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])
t = []
for elem in vec:
    for num in elem:
        t.append(num)
print(t)

from math import pi

print([str(round(pi, i)) for i in range(1, 6)])

# 5.1.4. Nested List Comprehensions

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])
m = []
for i in range(4):
    temp = []
    for row in matrix:
        temp.append(row[i])
    m.append(temp)

print(m)

print(list(zip(*matrix)))
