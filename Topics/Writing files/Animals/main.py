# read animals.txt
# and write animals_new.txt
# animals = ['rabbit\n', 'cat\n', 'turtle\n']
animals_list = []
animals_file = open('animals.txt', 'r', encoding='utf-8')
for animal in animals_file:
    animals_list.append(animal.replace('\n', ''))
animals_file.close()
animals_str = ' '.join(animals_list)
animals_new = open('animals_new.txt', 'w', encoding='utf-8')
animals_new.write(animals_str)
animals_new.close()

