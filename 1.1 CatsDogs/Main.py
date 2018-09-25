import os
import random


def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]
    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if 'dog' in path:
        return 0.5 + random.random() / 2
    return random.random() / 2


def process_dir(path):
    dir_list, file_list = get_dirs_and_files(path)

    cat_list = []
    dog_list = []

    # Your code goes here
    if len(dir_list) > 0:
        for d in range(len(dir_list)):
            cat_pictures, dog_pictures = process_dir(path + '/' + dir_list[d])
            for j in range(len(cat_pictures)):
                cat_list.append(cat_pictures[j])
            for k in range(len(dog_pictures)):
                dog_list.append(dog_pictures[k])
    for d in range(len(file_list)):
        if classify_pic(path + '/' + file_list[d]) >= 0.5:
            dog_list.append(path + '/' + file_list[d])
        else:
            cat_list.append(path + '/' + file_list[d])

    return cat_list, dog_list


def main():
    start_path = './'  # current directory

    cats_files, dogs_files = process_dir(start_path)

    # Loop to print
    if len(cats_files) > 1:
        for i in range(len(cats_files)):
            print(cats_files[i])
    else:
        print('there are no available cats to adopt! ')
    if len(dogs_files) > 1:
        for j in range(len(dogs_files)):
            print(dogs_files[j])
    else:
        print('There are no available dogs to adopt!')


main()
