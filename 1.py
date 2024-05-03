with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    print(text)
with open('output.txt', 'w+') as f:
    print(f.write(text.upper()), file=f)
