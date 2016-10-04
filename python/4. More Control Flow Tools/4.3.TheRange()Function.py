# 숫자 배열을 사용할 때 유용하게 사용할 수 있다
for i in range(5):
    print(i)

for i in range(5, 10):
    print(i, end=' ')
print()

for i in range(0, 10, 3):
    print(i, end=' ')
print()

for i in range(-10, -100, -30):
    print(i, end=' ')
print()

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i,a[i])


print(range(10)) #range는 list 처럼 동작하지만 사실 list가 아니다. 연속된 항목을 반환하는 객체로, 실제 생성하지 않아 메모리를 절약한다.
# Object is iterable means suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted.

# list() : iterable로부터 list를 만드는 함수
print(list(range(5)))