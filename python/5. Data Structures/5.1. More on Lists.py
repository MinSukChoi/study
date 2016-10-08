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
    squares.append(x**2)

print(squares)

squares = list(map(lambda x: x**2, range(10)))

print(squares)