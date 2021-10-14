names = ['Kate', 'Alexander', 'Oscar', 'Mary']

name_file = open('names.txt', 'w', encoding='utf-8')

# write the names on separate lines
for name in names:
    name_file.write(name + '\n')

name_file.close()
print(name_file)