try:
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        number_1 = int(lines[0])
        number_2 = int(lines[1])
        number_3 = int(lines[2])
        result = str(number_1 / number_2 + number_3)

except ValueError:
    result = 'data error'

except ZeroDivisionError:
    result = 'division by 0'

with open('output.txt', 'w') as f:
    f.write(result)

'''
with open('output.txt', 'w') as f:
    if lines[1] == 0:
        f.write('division by 0')
    elif not lines[0].isdigit() or not lines[1].isdigit() or not lines[2].isdigit():
        f.write('data error')
    else:
        f.write(str((int(lines[0]) / int(lines[1])) + int(lines[2])))
'''