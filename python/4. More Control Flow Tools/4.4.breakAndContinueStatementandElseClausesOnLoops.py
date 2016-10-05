'''
else cluase
1. Loop : break가 일어나지 않았을 때 실행
2. try : exception이 일어나지 않았을 때 실행
'''
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through with finding a factor
        print(n, 'is a prime number')

'''
Continue clause
C와 비슷하게 동작
'''
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
