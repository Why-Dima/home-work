def plural_form(num, form1, form2, form3):
    
    if 21 > num > 4 or num % 10 == 0:
        result = f'{num} {form3}'
    elif num == 1 or (num - 1) % 10 == 0:
        result = f'{num} {form1}'
    elif 5 > num > 1 or num % 10 == 2 or num % 10 == 3 or num % 10 == 4:
        result = f'{num} {form2}'

    return result

print(plural_form(534, 'яблоко', 'яблока', 'яблок'))
print(plural_form(9, 'студент', 'студента', 'студентов'))