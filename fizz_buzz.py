summ = 0

for i in range(1000, 20000):
    if i % 3 == 0 and i % 5 == 0:
        summ = i + summ
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')

print(summ)