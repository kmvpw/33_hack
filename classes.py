class Thing:
    """Базовый класс экипировки."""

    def __init__(self, name, hp, defense_percent, attack_damage):
        self.name = name
        self.hp = hp
        self.defense_percent = defense_percent
        self.attack_damage = attack_damage


class Person:
    """Базовый класс персонажа."""

    def __init__(self, name, hp, attack_damage, defense_percent):
        self.name = name
        self.full_hp = hp
        self.hp_now = hp
        self.attack_damage = attack_damage
        self.defense_percent = defense_percent
        self.things = []

    def set_things(self, things):
        """Принимает список вещей и экипирует их на персонажа."""
        self.things = things
        for thing in things:
            self.full_hp += thing.hp
            self.hp_now += thing.hp
            self.attack_damage += thing.attack_damage
            self.defense_percent += thing.defense_percent

    def take_damage(self, attack_damage):
        """Метод нанесения урона."""
        final_defense_percent = self.defense_percent
        damage_taken = attack_damage - (attack_damage * final_defense_percent)
        if damage_taken < 0:
            damage_taken = 0
        damage_taken = round(damage_taken, 2)
        self.hp_now -= damage_taken
        if self.hp_now < 0:
            self.hp_now = 0
        return damage_taken
    
    def is_alive(self):
        """Возвращает True, если персонаж жив, и False, если мертв."""
        return self.hp_now > 0


class Paladin(Person):
    """Класс Paladin, hp и protection увеличены вдвое."""

    def __init__(self, name, hp, attack_damage, defense_percent):
        super().__init__(
            name=name,
            hp=hp * 2,
            attack_damage=attack_damage,
            defense_percent=defense_percent * 2
        )


class Warrior(Person):
    """Класс Warrior, attack_damage увеличен вдвое."""

    def __init__(self, name, hp, attack_damage, defense_percent):
        super().__init__(
            name=name,
            hp=hp,
            attack_damage=attack_damage * 2,
            defense_percent=defense_percent
        )



# print("=== СПИСОК СОЗДАННЫХ И ОТСОРТИРОВАННЫХ ВЕЩЕЙ ===")
# for t in things_pool:
#     print(
#         f'Название: {t.name:25} - Защита: {t.defense_percent * 100:.1f}%'
#         f'({t.defense_percent}) - Атака: +{t.attack_damage:<3} | HP: +{t.hp}'
#     )
# print('--------------------------------------------------------------------\n')
