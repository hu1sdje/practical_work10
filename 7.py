with open('input.txt', 'r') as f:
    lines = f.readlines()

with open('input.txt', 'w') as f:
    for line in lines:
        if '100' not in line:
            f.write(line)