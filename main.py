import random

from colorama import Fore, Style, init

from battle import fight
from classes import Paladin, Thing, Warrior
from constants import (
    MAX_BASE_ATTACK, MAX_BASE_DEFENSE, MAX_HP, MAX_THINGS_PER_PERSON,
    MIN_BASE_ATTACK, MIN_BASE_DEFENSE, MIN_HP, MIN_THINGS_PER_PERSON,
    NAMES, NUMBER_OF_PERSONS, NUMBER_OF_THINGS, THING_NAMES,
    MAX_ATTACK_BONUS, MAX_DEFENSE_PERCENT, MAX_HEALTH_BONUS,
    MIN_ATTACK_BONUS, MIN_DEFENSE_PERCENT, MIN_HEALTH_BONUS,
)

init(autoreset=True)


def generate_things(thing_count):
    """Создаю список вещей со случайными параметрами."""
    all_things = []
    for index in range(thing_count):
        if index < len(THING_NAMES):
            thing_name = THING_NAMES[index]
        else:
            thing_name = f"Вещь_{index + 1}"

        protection = random.uniform(MIN_DEFENSE_PERCENT, MAX_DEFENSE_PERCENT)
        attack_damage = random.randint(MIN_ATTACK_BONUS, MAX_ATTACK_BONUS)
        health_bonus = random.randint(MIN_HEALTH_BONUS, MAX_HEALTH_BONUS)

        thing = Thing(
            name=thing_name,
            hp=health_bonus,
            protection=protection,
            attack_damage=attack_damage
        )
        all_things.append(thing)

    all_things.sort(key=lambda item: item.protection)
    return all_things


def generate_persons(all_things, names_list):
    """Создаю воинов и паладинов, случайно экипирую их."""
    random.shuffle(names_list)
    persons_list = []

    warrior_count = random.randint(0, NUMBER_OF_PERSONS)
    paladin_count = NUMBER_OF_PERSONS - warrior_count

    # Генерация воинов
    for warrior_index in range(warrior_count):
        hit_points = random.randint(MIN_HP, MAX_HP)
        base_attack = random.randint(MIN_BASE_ATTACK, MAX_BASE_ATTACK)
        base_defense = random.uniform(MIN_BASE_DEFENSE, MAX_BASE_DEFENSE)
        if names_list:
            character_name = names_list.pop()
        else:
            character_name = f"Воин_{warrior_index}"
        warrior = Warrior(
            name=character_name,
            hp=hit_points,
            attack_damage=base_attack,
            protection=base_defense
        )
        persons_list.append(warrior)

    # Генерация паладинов
    for paladin_index in range(paladin_count):
        hit_points = random.randint(MIN_HP, MAX_HP)
        base_attack = random.randint(MIN_BASE_ATTACK, MAX_BASE_ATTACK)
        base_defense = random.uniform(MIN_BASE_DEFENSE, MAX_BASE_DEFENSE)
        if names_list:
            character_name = names_list.pop()
        else:
            character_name = f"Паладин_{paladin_index}"
        paladin = Paladin(
            name=character_name,
            hp=hit_points,
            attack_damage=base_attack,
            protection=base_defense
        )
        persons_list.append(paladin)

    for person in persons_list:
        things_to_wear = random.randint(
            MIN_THINGS_PER_PERSON, MAX_THINGS_PER_PERSON
        )
        selected_things = random.sample(
            all_things, min(things_to_wear, len(all_things))
        )
        person.set_things(selected_things)

    return persons_list


def display_person_stats(person):
    """Выводит подробную информацию о персонаже и его экипировке."""
    # Определяем класс персонажа
    if isinstance(person, Warrior):
        class_name = "Воин"
        class_color = Fore.CYAN
    elif isinstance(person, Paladin):
        class_name = "Паладин"
        class_color = Fore.MAGENTA
    else:
        class_name = "Персонаж"
        class_color = Fore.WHITE

    print(f"{class_color}{person.name} ({class_name}){Style.RESET_ALL}")
    print(f"  Здоровье: {person.hp_now} / {person.full_hp}")
    print(f"  Атака: {person.attack_damage}")
    print(f"  Защита: {person.protection:.2f}")
    if person.things:
        print("  Экипировка:")
        for thing in person.things:
            print(f"    - {thing.name} (бонус: +{thing.hp} HP, "
                  f"+{thing.attack_damage} атаки, "
                  f"+{thing.protection:.2f} защиты)")
    else:
        print("  Экипировка: отсутствует")
    print()


def main():
    print(Fore.BLUE + "=== ГЕНЕРАЦИЯ МИРА ===" + Style.RESET_ALL)
    print("Генерация вещей...")
    all_things = generate_things(NUMBER_OF_THINGS)
    print(f"Создано {len(all_things)} вещей.")

    print("Генерация армии...")
    army = generate_persons(all_things, NAMES.copy())
    print(f"Создано {len(army)} бойцов.\n")

    print(Fore.BLUE + "=== СОСТАВ УЧАСТНИКОВ ===" + Style.RESET_ALL)
    for person in army:
        display_person_stats(person)

    print(Fore.BLUE + "=== НАЧАЛО БИТВЫ ===" + Style.RESET_ALL)
    winner = fight(army)

    if winner:
        print(Fore.GREEN + f"\n=== АБСОЛЮТНЫЙ ПОБЕДИТЕЛЬ: {winner.name} ===")
    else:
        print(Fore.RED + "\n=== БОЙ НЕ СОСТОЯЛСЯ ===")


if __name__ == "__main__":
    main()
