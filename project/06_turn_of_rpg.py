import random
from random import *
from time import sleep


class Object:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, target):
        print('{0}가 {1}을 공격했습니다.'.format(self.name, target.name))
        target.hp -= self.damage
        if target.hp <= 0:
            print('{0}을 죽였다!.'.format(target.name))
        else:
            print('{0}의 체력이 {1} 남았습니다.'.format(target.name, target.hp))


class Player(Object):

    def magic_attack(self, target):
        print('{0}가 {1}을 마법으로 공격합니다.'.format(self.name, target.name))
        print('{0}에게 50만큼의 데이지!'.format(target.name))
        target.hp -= 50
        if target.hp <= 0:
            print('{0}을 죽였다!'.format(target.name))
        else:
            print('{0}의 체력이 {1}만큼 남았습니다'.format(target.name, target.hp))


class Monster(Object):

    def rest(self):
        print('{0}이 대기했습니다'.format(self.name))

    def recovery(self):
        self.hp += 10
        print('{0}이 자신의 체력을 10 회복했습니다.'.format(self.name))


def createobjects():
    Warrior = Player('전사', 100, 10)

    Monsters = {}
    Monsters['미니고블린'] = Monster('미니고블린', 10, 10)
    Monsters['고블린'] = Monster('고블린', 30, 30)
    Monsters['슈퍼고블린'] = Monster('슈퍼고블린', 50, 50)
    return Warrior, Monsters


def show_info(Player, Monsters):
    print('\n-------------턴시작-------------')
    print('{0}의 현재 체력은 {1}입니다'.format(Player.name, Player.hp))
    for key, value in Monsters.items():
        print('{0}의 현재 체력은 {1}입니다'.format(value.name, value.hp))


def player_turn(Player, Monsters):
    print('\n-------------플레이어 턴-------------')
    command = input('공격? 마법? : ')
    target = input('누구를 공격하시겠습니까? : ')
    if command == '공격':
        Player.attack(Monsters[target])
    elif command == '마법':
        Player.magic_attack(Monsters[target])
    return Monsters



def monster_check(Monsters):
    deed_monster = []
    for key, value in Monsters.items():
        if value.hp <= 0:
            deed_monster.append(key)
    for i in deed_monster:
        del Monsters[i]
    if len(Monsters) <= 0:
        return Monsters, True
    else:
        return Monsters, False


def monster_turn(Player, Monsters):
    print('\n-------------몬스터 턴-------------')
    sleep(3)
    for key, value in Monsters.items():
        commands = ['rest', 'recovery', 'attack']
        command = choice(commands)
        if command == 'rest':
            value.rest()
        elif command == 'recovery':
            value.recovery()
        elif command == 'attack':
            value.attack(Player)
    return Player


def player_check(Player):
    if Player.hp <= 0:
        return True
    else:
        return False


Warrior, Monsters = createobjects()

while True:
    show_info(Warrior, Monsters)
    Monsters = player_turn(Warrior, Monsters)
    sleep(1)
    Monsters, mdead = monster_check(Monsters)
    if mdead:
        print('\n승리!!')
        break
    Warrior = monster_turn(Warrior, Monsters)
    pdead = player_check(Warrior)
    if pdead:
        print('\n패배')
        break
