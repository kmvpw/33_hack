import random

from conc import THING_NAMES


class Thing:
    """Базовый класс экипировки."""

    def __init__(self, name, hp, protection, attack_damage):
        self.name = name
        self.hp = hp
        self.protection = protection
        self.attack_damage = attack_damage


class Person:
    """Базовый класс персонажа."""

    def __init__(self, name, hp, attack_damage, protection):
        self.name = name
        self.full_hp = hp
        self.hp_now = hp
        self.attack_damage = attack_damage
        self.protection = protection
        self.things = []

    def set_things(self, things):
        """Принимает список вещей и экипирует их на персонажа."""
        self.things = things
        for thing in things:
            self.full_hp += thing.hp
            self.attack_damage += thing.attack_damage
            self.protection += thing.protection

    def take_damage(self, attack_damage):
        """Метод нанесения урона."""
        final_protection = self.protection
        damage_taken = attack_damage - (attack_damage * final_protection)
        if damage_taken < 0:
            damage_taken = 0
        self.hp_now -= damage_taken
        if self.hp_now < 0:
            self.hp_now = 0
        return damage_taken


class Paladin(Person):
    """Класс Paladin, hp и protection увеличены вдвое."""

    def __init__(self, name, hp, attack_damage, protection):
        super().__init__(
            name=name,
            hp=hp * 2,
            attack_damage=attack_damage,
            protection=protection * 2
        )


class Warrior(Person):
    """Класс Warrior, attack_damage увеличен вдвое."""

    def __init__(self, name, hp, attack_damage, protection):
        super().__init__(
            name=name,
            hp=hp,
            attack_damage=attack_damage * 2,
            protection=protection
        )


things_pool = []
for i in range(10):
    name = THING_NAMES[i] if i < len(THING_NAMES) else f"thing-{i + 1}"
    thing = Thing(
        name=name,
        hp=random.randint(1, 50),
        protection=round(random.uniform(0.01, 0.10), 3),
        attack_damage=random.randint(1, 20)
    )
    things_pool.append(thing)
things_pool.sort(key=lambda x: x.protection)

# print("=== СПИСОК СОЗДАННЫХ И ОТСОРТИРОВАННЫХ ВЕЩЕЙ ===")
# for t in things_pool:
#     print(
#         f'Название: {t.name:25} - Защита: {t.protection * 100:.1f}%'
#         f'({t.protection}) - Атака: +{t.attack_damage:<3} | HP: +{t.hp}'
#     )
# print("--------------------------------------------------------------------\n")
