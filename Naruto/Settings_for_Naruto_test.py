import random
from colorama import Fore, Back, Style

count_arr = 0
count_arr1 = 0
count_arr2 = 0
# Basick class
class Ninja:
    damage_shuriken = 50
    damage_kunai = 20

    # method for throw shuriken
    def shuriken(self, thrower, person):

        if (thrower.name == 'Sasuke') or (thrower.name == 'Itachi') or (thrower.name == 'Shisui'):
            self.add_to_chance = 4
            self.damage_shuriken = 75
            person.chance += self.add_to_chance  # change proc case we have to do 50%,but chance=1
        else:
            self.add_to_chance = 1
            self.damage_shuriken = 50
            person.chance += self.add_to_chance

        if not how_more_chance(person): #if person dont missed from shuriken
            person.chance = person.chance - self.add_to_chance  # remove chance for standart chance(1)
            person.health -= self.damage_shuriken
            return f'{person.health}hp have {person.name}'
        else:
                # if you don't hit
                person.chance = person.chance - self.add_to_chance  # remove chance for standart chance(1)
                return 'You was missed'

    # method for hit with kunai
    def kunai(self, enemy):
        damage_kunai = 20
        enemy.health -= damage_kunai
        return f'{enemy.health}hp have {enemy.name}'
######################################################################
# classes for clans#
class Uchiha(Ninja):
    # Information about


    name_clan = 'UCH'

    name_clan_jutsu1 = 'sharingan'

    chakra_clan_jutsu1 = 450

    damage_clan_jutsu1 = '50%,3 step'

    working_sharingan = False

    # method for use sharingan
    def sharingan(self, user, person):  # this is method do 50% точности enemy for 3 step

        if have_chakra(user.chakra, self.chakra_clan_jutsu1):  # if chakra more or equal chakra_clan_jutsu
            user.chakra -= self.chakra_clan_jutsu1
            person.chance = 2
            self.working_sharingan = True
            return f'sharingan using...'  # in begin it is red background,in end
            # it is remove red background
        else:
            return f'I cant, this is technik need-{self.chakra_clan_jutsu1} chakra!'


#####################################################################
# Other#
class MangekyoSharingan(Uchiha):
    fixation = 0

    use_amaterasu = False
    use_susano = None
    susano_live = True
    armor_for_susano = 0

    damage_clan_jutsu2 = 250
    damage_clan_jutsu3 = 'armor'
    damage_clan_jutsu4 = 3000

    name_clan_jutsu2 = 'amaterasu'
    name_clan_jutsu3 = 'susano'
    name_clan_jutsu4 = "Indra's Arrow"

    chakra_clan_jutsu2 = 350
    chakra_clan_jutsu3 = 500
    chakra_clan_jutsu4 = 2000

    # clan_jutsu2
    def amaterasu(self, user, person):
        if have_chakra(user.chakra,self.chakra_clan_jutsu2):
            person.health -= self.damage_clan_jutsu2
            self.use_amaterasu = True
            return f'{person.health}hp have {person.name}'
        else:
            return f'I cant, this is technik need-{self.chakra_clan_jutsu2} chakra!'

    # clan_jutsu3
    def susano(self, user):
        if self.use_susano:
            return f"I'm already in susano"
        if have_chakra(user.chakra, self.chakra_clan_jutsu3):
                user.chakra -= self.chakra_clan_jutsu3
                self.use_susano = True
                self.armor_for_susano = 1000
                self.fixation = user.health
                user.health += self.armor_for_susano
                return f"{Fore.WHITE}{Back.BLUE}YES!I'M IN SUSANO!{Style.RESET_ALL}"
        else:
            return f'I cant, this is technik need-{self.chakra_clan_jutsu3} chakra!'

    ##############################################################################################################
    # jutsu_susano

    # clan_jutsu4
    def indra_arrow(self, user, person):
        if self.use_susano:
            if have_chakra(user.chakra, self.chakra_clan_jutsu4):
                user.chakra -= self.chakra_clan_jutsu4
                person.health -= self.damage_clan_jutsu4
                return f'arrow flew!--->n{person.health}hp have {person.name}'

            else:
                return f'I cant, this is technik need-{self.chakra_clan_jutsu3} chakra!'

    #################################################################################################################
    def tsukiemi(self):
        pass

    def kotoamacukami(self):
        pass

    def full_susano(self):
        pass

    def camui(self):
        pass

    def meteor(self):
        pass


class Rinnengan:
    def shinratensei(self):
        pass

    def robot(self):
        pass

    def soul(self):
        pass

    def mosters(self):
        pass

    def eatchakra(self):
        pass

    def gedomazo(self):
        pass

    def limbo(self):
        pass

    def teleport(self):
        pass

    def double_power(self):
        pass


class RineSharingan(Uchiha):
    def mugen_cukiemi(self):
        pass

    def teleport_izmerenia(self):
        pass


###############################################################
# classes for ninja#
class Naruto(Ninja):
    # information about
    name = 'Naruto'
    name_clan = f'UZU'
    health = 1250
    chakra = 8000
    chance = 1

    chakra_jutsu1 = 300
    chakra_jutsu2 = 700
    chakra_jutsu3 = 450

    damage_jutsu1 = 500
    damage_jutsu2 = 'enemy chance hit me 1/8000(1step)'
    damage_jutsu3 = 450

    name_jutsu1 = 'rasengan'
    name_jutsu2 = 'clone_jutsu'
    name_jutsu3 = 'rasensuriken'

    working_clone_jutsu = False

    # method for jutsu - 'rasengan'
    def rasengan(self, user, person):

        if have_chakra(user.chakra, self.chakra_jutsu1):  # if chakra more or equal chakra_jutsu
            self.chakra -= self.chakra_jutsu1
            person.health -= self.damage_jutsu1
            return f'{person.health}hp have {person.name}'
        else:
            return f'I cant, this is technik need-{self.chakra_jutsu1} chakra!'

    # method for clone_jutsu
    def clone_jutsu(self, user, person):

        if have_chakra(user.chakra, self.chakra_jutsu2):
            self.working_clone_jutsu = True
            self.chakra -= self.chakra_jutsu2
            self.working_clone_jutsu = True
            person.chance += 8000
            return f'I did my clone!'
        else:
            return f'I cant,this is technik need-{self.chakra_jutsu2} chakra!'

    def rasensuriken(self, user, person):

        if have_chakra(user.chakra, self.chakra_jutsu3):
            self.chakra -= self.chakra_jutsu3
            person.health -= self.damage_jutsu3
            return f'{person.health}hp have {person.name}'
        else:
            return f'I cant, this is technik need-{self.chakra_jutsu3} chakra!'

    # method for return jutsu to person1_this_is()
    def return_jutsu(self):
        return (f'''        3){self.name_jutsu1}-{self.damage_jutsu1}damage-{self.chakra_jutsu1}chakra
            4){self.name_jutsu2}-{self.damage_jutsu2}-{self.chakra_jutsu2}chakra
            5){self.name_jutsu3}-{self.damage_jutsu3}-{self.chakra_jutsu3}chakra''')

    # method for return clan jutsu to person1_this_is()
    def clan_return_jutsu(self):
        return False


class Sasuke(MangekyoSharingan, Rinnengan):
    # Information about
    name = 'Sasuke'
    health = 1000
    chakra = 5500
    chance = 1

    damage_shuriken = 75


    chakra_jutsu1 = 165

    name_jutsu1 = 'chidori'
    name_jutsu2 = 'sharingan'

    damage_jutsu1 = 320

    # method for jutsu - 'chidori'
    def chidori(self, user, person):

        if have_chakra(user.chakra, self.chakra_jutsu1):  # if chakra more or equal chakra_jutsu
            person.health -= self.damage_jutsu1
            return f'{person.health}hp have {person.name}'
        else:
            return f'I cant, this is technik need-{self.chakra_jutsu1} chakra!'

    # method for return jutsu to person1_this_is()
    def return_jutsu(self):
        return f'''        3){self.name_jutsu1}-{self.damage_jutsu1}damage-{self.chakra_jutsu1}chakra'''

    # method for return clan jutsu to person1_this_is()
    def clan_return_jutsu(self):
        if not self.use_susano:
            return (f'''4){self.name_clan_jutsu1}-{self.damage_clan_jutsu1}-{self.chakra_clan_jutsu1}chakra
        5){self.name_clan_jutsu2}-{self.damage_clan_jutsu2}damage,100постепенно 2 шага - {self.chakra_clan_jutsu2}chakra
        6){self.name_clan_jutsu3}-{self.damage_clan_jutsu3}(1000)-{self.chakra_clan_jutsu3}chakra''')
        elif self.use_susano:
            return (f'''4){self.name_clan_jutsu1}-{self.damage_clan_jutsu1}-{self.chakra_clan_jutsu1}chakra
        5){self.name_clan_jutsu2}-{self.damage_clan_jutsu2}damage,100постепенно 2 шага - {self.chakra_clan_jutsu2}chakra
        6){self.name_clan_jutsu3}-{self.damage_clan_jutsu3}damage-{self.chakra_clan_jutsu3}chakra
        7){self.name_clan_jutsu4}-{self.damage_clan_jutsu4}damage-{self.chakra_clan_jutsu4}chakra''')


#######################################################################
# functions for game#

# main function for game
def person1_this_is_(person_1, person_2):
    # for color,and описание
    print(f'''({person_1.name_clan}){person_1.name}- chance({person_1.chance})
    Health - {person_1.health} 
    Chakra - {person_1.chakra} 
        Basic:
            1)Shuriken-{person_1.damage_shuriken},
            2)Kunai-{person_1.damage_kunai}
        Jutsu:''')

    print(f'    {person_1.return_jutsu()}')  # return описание about jutsu

    if  person_1.clan_return_jutsu():
        print(f'''Clan jutsu:
        {person_1.clan_return_jutsu()}''')
    else:
        pass
    # for use jutsu
    jutsu = int(input('Enter that you choose - '))

    # if person - Sasuke
    if person_1.name == 'Sasuke':
        if jutsu == 1 and how_more_chance(person_1):
            print(person_1.shuriken(person_1, person_2))
        elif jutsu == 2 and how_more_chance(person_1):
            print(person_1.kunai(person_2))
        elif jutsu == 3 and how_more_chance(person_1):
            print(person_1.chidori(person_1, person_2))
        elif jutsu == 4:
            print(person_1.sharingan(person_1, person_2))
        elif jutsu == 5 and how_more_chance(person_1):
            print(person_1.amaterasu(person_1,person_2))
        elif jutsu == 6:
            print(person_1.susano(person_1))
        elif jutsu == 7 and how_more_chance(person_1):
            print(person_1.indra_arrow(person_1, person_2))

        # if person - Naruto
    elif person_1.name == 'Naruto':
        if jutsu == 1 and how_more_chance(person_1):
            print(person_1.shuriken(person_1, person_2))
        elif jutsu == 2 and how_more_chance(person_1):
            print(person_1.kunai(person_2))
        elif jutsu == 3 and how_more_chance(person_1):
            print(person_1.rasengan(person_1, person_2))
        elif jutsu == 4:
            print(person_1.clone_jutsu(person_1, person_2))
        elif jutsu == 5 and how_more_chance(person_1):
            print(person_1.rasensuriken(person_1, person_2))
    '''If jutsu and chance will be true - use jutsu(and print result)'''


# function for know how more chance hit
def how_more_chance(person_1):
    if random.randint(1, person_1.chance) == 1:  # if from (1....chance) will be 1,than ->
        return True     #IF HITTED
    else:
        return False    #IF MISSED


# function for is live for know hwo win
def is_live(person_1):
    if person_1.health <= 0:
        return True


# function for use jutsu for a step
def have_jutsu(person_1, person_2):
    global count_arr
    global count_arr1
    global count_arr2
 # for skill 'sharingan',case it will be go only 3 steps
 # 1)
    if hasattr(person_1, 'working_sharingan'):
        if person_1.working_sharingan:
            count_arr += 1
            if count_arr == 4:
                person_2.chance = 1
                count_arr = 0
                person_1.working_sharingan = False
 # for skill 'clone_jutsu' case it will be go only 1 step
 # 1)

    if hasattr(person_1, 'working_clone_jutsu'):
        if person_1.working_clone_jutsu:
            count_arr1 += 1
            if count_arr1 == 2:
                person_1.chance = 1
                count_arr1 = 0
                person_1.working_clone_jutsu = False
 # for amaterasu
 # 1)
    if hasattr(person_1, 'use_amaterasu'):
        if person_1.use_amaterasu:
            count_arr2 += 1
            if count_arr2 <= 2:
                person_2.health -= person_1.damage_clan_jutsu2 - 150
                print(f'{Fore.WHITE}{Back.BLACK}Amaterasu:-150hp{Style.RESET_ALL}')
            elif count_arr2 > 2:
                count_arr2 = 0
                person_1.use_amaterasu = False
                print('Amaterasu was expired')

 # for susano
 # 1)
    if hasattr(person_1, 'use_susano'):
        if person_1.use_susano:
            print(f'[SUS]')
            if person_1.health <= person_1.fixation:
                person_1.use_susano = False
        elif  person_1.use_susano==False:
            print(f'SUSANO broke')

# function for check chakra
def have_chakra(chakra, chakra_need):
    if chakra >= chakra_need:
        return True
    else:
        return False

def return_in_procent(person):
    if person.chance==1:
        return f'100%'
    else:
        procent = f'{100-(1 / person.chance*100)}+%'
        return procent