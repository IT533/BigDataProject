num = 100000
counter = 0
with open('./input/splitfile.txt', 'w') as fwrite:
    for line in open('./input/allfile.txt'):
        if counter > num:
            break
        fwrite.write(line)
        counter += 1
    fwrite.close()
