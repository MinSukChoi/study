# 다양한 개수의 인자를 가진 함수를 정의하는 것도 가능하다.

#4.7.1 Default Argument Values
'''
def ask_ok(prompt, retries=4, remainder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nope'):
            return False
        retries = retries -1
        if retries<0 :
            raise ValueError('invalid user response')
        print(remainder)

'''
'''
위 함수는 다양한 방법으로 콜할수 있다.)
초기 값은 함수 정의 부에서 구현된다.
'''
'''
ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
'''

'''
초기 값은 최초 한번만 적용된다.
'''
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))