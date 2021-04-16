import Settings_for_Naruto_test as sfn
from colorama import Fore, Back, Style

# import pdb

# while person is not equal
while True:

    # ask hwo first player
    person_1 = int(
        input(f'Choose person 1){sfn.Naruto().name} 2){sfn.Sasuke.name} - '))

    # ask hwo second player
    person_2 = int(
        input(f'Choose person 1){sfn.Naruto().name} 2){sfn.Sasuke.name} - '))

    # if person equal return
    if person_2 == person_1:
        print('No, you cant use this person it taked,take other person)')
        continue
    else:
        break

if person_1 == 1:
    person_1 = sfn.Naruto()
if person_1 == 2:
    person_1 = sfn.Sasuke()
if person_2 == 1:
    person_2 = sfn.Naruto()
if person_2 == 2:
    person_2 = sfn.Sasuke()

# hwo play
print(f'1){person_1.name}\n2){person_2.name}')

# hwo hit first
print(f'Первым ходит - {person_1.name}')

# переменные for logic - 'while'
count_arr = 0
count_arr1 = 0
count_arr2 = 0
# process game
while True:

    # if person_1 die - exit
    if sfn.is_live(person_1):
        print(f'{person_2.name} win!!!')
        break

    # if person_1 have a jutsu
    sfn.have_jutsu(person_1, person_2)

    # step person_1
    sfn.person1_this_is_(person_1, person_2)

    # if person_2 die - exit
    if sfn.is_live(person_2):
        print(f'{person_1.name} win!!!')
        break

    # if person_2 have a jutsu
    sfn.have_jutsu(person_2,person_1)

    # step person_2
    sfn.person1_this_is_(person_2, person_1)
