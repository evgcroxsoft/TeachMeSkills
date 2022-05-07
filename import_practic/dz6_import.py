def animals_list():
    animal_list = []
    i = 1
    while True:
        animal = input(f'Enter {i} first animal: ')
        animal_list.append(animal)
        i = i+1
        if i == 4:
            break
    return animal_list