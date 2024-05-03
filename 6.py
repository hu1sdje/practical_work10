with open('input.txt', 'r', encoding='utf-8') as f:
    n = f.readline()
    lines = f.readlines()
    print(len(lines))

with open('output.txt', 'w') as f:
    if int(n) == len(lines):
        f.write('YES')
    else:
        f.write('NO')