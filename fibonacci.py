a=b=1
fib_sum = 0
list_fib = [a,b]
list_fib_two = []


while fib_sum < 10000000:#выводится должно последнее число после 10000000
    fib_sum = a + b
    a = b
    b = fib_sum
    list_fib.append(fib_sum)
    if int(fib_sum)% 2 == 0:#выводим последовательность из четных чисел
        list_fib_two.append(fib_sum)
        print(fib_sum)


print('Сумма всех четных элементов последовательности:', sum(list_fib_two))
print('Колчичество элементов в последовательности:', len(list_fib))
print('Предпоследний элемент последовательности:', list_fib[-2])

