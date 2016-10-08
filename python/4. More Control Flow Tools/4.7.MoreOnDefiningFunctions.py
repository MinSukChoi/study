# 다양한 개수의 인자를 가진 함수를 정의하는 것도 가능하다.

# 4.7.1 Default Argument Values
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


# 4.7.2. Keyword Arguments
# keyword argument를 사용하여 보다 유동적인 argument입력이 가능하다
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "! ")


parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000, action='VOOOOOM')
parrot(action='VOOOOM', voltage=1000000)
parrot('a million', 'bereft of life', 'jump')
parrot('thousand', state='pushing up the daisies')


# *argument : a tuple containing the positional arguments beyond the formal parameter list 리스트 형태로 받음
# **keywords : a dictionary containing all keyword arguments except for those corresponding to a formal parameter. 정규 인자에 없는 값을 받음
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's Very runny, sir.", "It's really very, VERY runny , sir.", shopkeeper="Michael Palin",
           client="John Cleese", sketch="Cheese Shop Sketch")


# 4.7.3. Arbitrary Argument Lists
# 인자의 갯수가 랜덤한 함수에 대해서 사용이 가능하지만 tuple때문에 잘 사용되지는 않는다
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


def concat(*args, sep='/'):
    return sep.join(args)


print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep='.'))

# 4.7.4 Unpacking Argument Lists
# 인자는 list나 tuple로 정의되어 있을 때, 분리된 인자에 대한 수행을 한번에 하고자 할때
print(list(range(3, 6)))
args = [3, 6]
print(list(range(*args)))


def parrot2(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts throught is.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot2(**d)


# 4.7.5. Lambda Expressions
# 간단한 익명의 함수를 lambda keyword를 사용하여 정의하는 것이 가능하다
# 문법적으로 하나의 expression으로 제한된다
def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
print(f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

# 4.7.6. Documentation Strings
'''
1. 첫번째 줄은 짧고 간결한 객체의 목적을 설명 (객체의 이름이나 타입을 직접적으로 인용하지 않는다)
2. 첫번째 줄은 대문자로 시작하여 마침표를 찍는다.
3. 두번째 줄은 빈칸으로 채운다(내용이 여러줄일 경우)
4. 다음 내용은 함수의 용례 또는 부작용에 대해 기술
5. indentation을 맞춰준다
'''


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


print(my_function.__doc__)

# 4.7.7 Function Annotations
'''
Function Annotations은 유저 정의 함수에 대해 완전히 선택적인 정보를 포함한다
__annotation__에 저장되며 함수에는 아무 영향을 미치지 않는다
'''


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotaions:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


f('spam')
