for line in open('./input/0301/1.txt', 'r'):
    new_line = ''
    for c in line:
        if c == '\t':
            new_line += ','
        else:
            new_line += c
    print(new_line)
