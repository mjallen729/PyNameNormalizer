'''
Given a list of names, outputs a txt file of normalized names and a txt file of
unnormalized names.

Both files will appear in the results folder. The number in the filename 
signifies how recently the file was created, larger numbers are more recent.

Make sure you set the ignore_whitespace value below
'''

# Ignore extra spaces at beginning or end of a name that is otherwise normal?
# Ex: ' Sean Kim  ' would be considered normalized if True, unnormalized if False
ignore_whitespace = False


from normalizer import normalize
import time

name_file = open('one_name_per_line.txt')
name_list = list()

for name in name_file:
    name_list.append(name)

name_file.close()

if __name__ == '__main__':
    norm, unnorm = normalize(name_list, not ignore_whitespace)

    try:
        timestamp = round(time.time())
        with open(f'results/normalized_{timestamp}.txt', 'w') as file:
            for name in norm:
                # Add a newline character after each item
                file.write(f'{name}\n')

        with open(f'results/unnormalized_{timestamp}.txt', 'w') as file:
            for name in unnorm:
                # Add a newline character after each item
                file.write(f'{name}\n')

    except FileNotFoundError:
        print(f"Error: Could not create file")

    finally:
        print('DONE!')