def fib(n):
    """Print a Fibonacci series up to n."""  # docstring
    a, b = 0, 1
    while a < n:
        print(b, end=' ')
        a, b = b, a + b
    print()

fib(2000)

'''
docstring은 자동 레퍼런스 완성 등의 이점이 있기에 무조건 써주는 것이 좋다.

함수의 실행은 함수의 로컬변수를 위한 새로운 심볼테이블을 생성한다. 더 정확하게는 함수 안에서의 모든 변수 할당은 로컬 심볼 테이블에 값을 저장한다.
변수의 참조는 로컬 심볼테이블을 우선하고, 없을 때는 바로 상위 함수의 심볼테이블을 참조한다.
따라서, 전역변수는 함수 안에서 바로 할당될 수 없다.

함수 매개인자는 함수가 콜되었을때, 심볼테이블에 할당된다.
인자는 call by value를 통하여 할당된다.

함수의 정의는 함수의 이름을 현재 심볼테이블에 할당하는 것이다.
따라서, 변수에 함수의 할당이 가능하다.
'''

print(fib)
f=fib
f(100)

''' 리턴 값이 없는 함수라도 실제로는 None이라는 값을 반환한다. '''

print(f(0))

def fib2(n):
    """ Return a list containing Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a<n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)

'''
위 동작은 파이썬의 새로운 특징을 증명하고 있다.
return statement는 함수로부터의 값을 반환하고, return이 없는 것은 none을 반환한다.
'''