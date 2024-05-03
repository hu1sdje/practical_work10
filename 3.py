with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('output.txt', 'w') as f:
    for line in lines:
        f.write(line[0])