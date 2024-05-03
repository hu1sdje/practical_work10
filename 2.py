with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('output.txt', 'w') as f:
    letter = input()
    for line in lines:
        print(line)
        if line.startswith(letter):
            f.write(line)
            print(lines)