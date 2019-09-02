my_dictionary = {
    0: 'th', 1: 'st', 2: 'nd', 3: 'rd', 4: 'th',
    5: 'th', 6: 'th', 7: 'th', 8: 'th', 9: 'th',
    10:'th'
}

def find_number(num):
    last_number = abs(num) % 10
    return str(num) + my_dictionary[last_number]

print(find_number(50))
print(find_number(54))
print(find_number(22))
print(find_number(-100))
print(find_number(98765432))
print(find_number(19))
print(find_number(1))
print(find_number(8763))
print(find_number(3))
print(find_number(4))
print(find_number(20))

