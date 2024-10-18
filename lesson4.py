from random import randint, choice
class GameEntity:
    def __init__(self, name, health, damage):
         self.__name = name
         self.__health = health
         self.__damage = damage
     @property
    def name(self):
         return self.__name
     @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value
    @property
    def damage(self):
        return self.__damage
    @damage.setter
    def damage(self, value):
        self.__damage = value
    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'
class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None
    def choose_defence(self, heroes_list):
        random_hero = choice(heroes_list)
        self.__defence = random_hero.ability
    def attack(self, heroes_list):
        for hero in heroes_list:
            if hero.health > 0:
                if type(hero) == Berserk and self.__defence != hero.ability:
                    hero.blocked_damage = choice([5, 10])
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage
    @property
    def defence(self):
        return self.__defence
    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'
class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability
    @property
    def ability(self):
        return self.__ability
    def apply_super_power(self, boss, heroes_list):
        pass
    def attack(self, boss):
        boss.health -= self.damage
class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')
    def apply_super_power(self, boss, heroes_list):
        coeff = randint(2, 5)
        boss.health -= coeff * self.damage
        print(f'Warrior {self.name} hits critically {coeff * self.damage}.')
class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BOOST')
    def apply_super_power(self, boss, heroes_list):
        # TODO here will be implementation of boosting
        pass
class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_DAMAGE')
        self.__blocked_damage = 0
    def apply_super_power(self, boss, heroes_list):
        boss.health -= self.blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage} damages to boss.')
    @property
    def blocked_damage(self):
        return self.__blocked_damage
    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value
class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points
    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points
round_number = 0
def is_game_over(boss, heroes_list):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes_list:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False
def show_statistics(boss, heroes_list):
    print(f' ------------- ROUND {round_number} -------------')
    print(boss)
    for hero in heroes_list:
        print(hero)
def play_round(boss, heroes_list):
    global round_number
    round_number += 1
    boss.choose_defence(heroes_list)
    boss.attack(heroes_list)
    for hero in heroes_list:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes_list)
    show_statistics(boss, heroes_list)
def start_game():
    boss = Boss(name='Minotavr', health=1000, damage=50)
    warrior_1 = Warrior(name='Asterix', health=290, damage=10)
    warrior_2 = Warrior(name='Obelix', health=280, damage=15)
    magic = Magic(name='Alice', health=270, damage=5)
    berserk = Berserk(name='Guts', health=220, damage=10)
    doc = Medic(name='Doc', health=200, damage=5, heal_points=15)
    assistant = Medic(name='Junior', health=300, damage=5, heal_points=5)
    heroes_list = [warrior_1, doc, warrior_2, magic, berserk, assistant]
    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)
start_game()


class Hero:
    def __init__(self, health=100, attack=10):
        self.health = health
        self.attack = attack
        self.alive = True
        self.shield = False
        self.team = []

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False

    def give_damage_to_hero(self, target):
                if target.alive:
                    target.take_damage(self.attack)


class Witcher(Hero):
    def __init__(self):
        super().__init__()
        self.chance_to_revive = 1
        self.alive = True

    def attack(self, boss):
        pass

    def take_damage(self, damage):
        if self.alive:
            super().take_damage(damage)

    def revive_hero(self, hero):
        if not hero.alive and self.alive:
            hero.revive()
            self.take_damage(self.health)
            self.alive = False

class Hacker(Hero):
    def __init__(self, health_drain):
        super().__init__()
        self.health_drain = health_drain

    def attack(self, boss):
        pass

    def apply_health_drain(self, boss):
        if boss.health > 0:
            boss.take_damage(self.health_drain)
            self.give_damage_to_hero(boss)

class Golem(Hero):
    def __init__(self, health_boost):
        super().__init__()
        self.max_health = 2000
        self.health = self.max_health
        self.attack = 50

    def take_damage(self, damage):
        if damage > 0:
            reduced_damage = damage / 5
            super().take_damage(reduced_damage)

class Avrora(Hero):
    def __init__(self):
        super().__init__()
        self.invisible = False
        self.health_return = 0

    def go_invisible(self):
        self.invisible = True

        self.health_return = 0

    def end_invisibility(self):
        self.invisible = False


class Druid(Hero):
    def __init__(self):
        super().__init__()

    def summon_assistant(self):
        assistant = random.choice(["angel", "crow"])
        if assistant == "angel":
            self.summon_angel()
        else:
            self.summon_crow()

    def summon_angel(self):

        pass

    def summon_crow(self):

        pass

class Thor(Hero):
    def __init__(self, stun_chance):
        super().__init__()
        self.stun_chance = stun_chance

    def attack(self, boss):
        if random.random() < self.stun_chance:
            boss.stun()

class TrickyBastard(Hero):
    def __init__(self):
        super().__init__()
        self.fake_death = False

    def pretend_dead(self):
        self.fake_death = True
        self.health = 0

    def revive(self):
        self.fake_death = False
        self.health = 100

class Antman(Hero):
    def __init__(self, size_change):
        super().__init__()
        self.size = 1
        self.size_change = size_change

    def change_size(self):
        self.size += self.size_change
        self.health *= self.size
        self.attack *= self.size


class Deku(Hero):
    def __init__(self):
        super().__init__()
        self.attack_boost = 1.2

    def attack(self):
        chance = random.random()
        if chance < 0.5:
            self.attack *= 1.2
            self.health -= 10

class Kamikadze(Hero):
    def __init__(self):
        super().__init__()

    def sacrifice(self, boss):
        if random.random() < 1:
            boss.take_damage(self.health)
        else:
            boss.take_damage(self.health * 0.5)

class Samurai(Hero):
    def __init__(self):
        super().__init__()

    def throw_shuriken(self):
        if random.random() < 0.5:
            self.virus_attack()
        else:
            self.vaccine_attack()

    def virus_attack(self):

        pass

    def vaccine_attack(self):

        pass

class Bomber(Hero):
    def __init__(self):
        super().__init__(health = 100)

    def on_hero_death(self, boss):

        boss.take_damage(100)

class Reaper(Hero):
    def __init__(self):
        super().__init__()

    def check_health(self):
        if self.health < 30:
            self.attack *= 2
        elif self.health < 15:
            self.attack *= 3

class Spitfire(Hero):
    def __init__(self):
        super().__init__()
        self.aggression = 80

    def on_hero_death(self):
        self.attack += self.aggression

class King(Hero):
    def __init__(self):
        super().__init__()

    def summon_saitama(self):
        if random.random() < 0.1:

            pass

class Ludoman(Hero):
    def __init__(self):
        super().__init__()

    def roll_dice(self, boss, team):
        dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
        print(f"Dice rolled: {dice1} and {dice2}")
        if dice1 == dice2:
            damage = dice1 * dice2
            boss.take_damage(damage)
        else:
            teammate = random.choice(team)
            teammate.take_damage(dice1 + dice2)

class Avenger(Hero):
    def __init__(self, team = None):
        super().__init__()
        if team is None:
            team = []
        self.team = team

    def create_shield(self):
        if random.random() < 0.2:
            for hero in self.team:
                hero.shield = True

class Boss:
    def __init__(self):
        self.health = 1000

    def take_damage(self, damage):
        self.health -= damage
        print(f"Boss takes {damage} damage, remaining health: {self.health}")
