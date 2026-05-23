import random
from constants import (
    MIN_DEFENSE_PERCENT, MAX_DEFENSE_PERCENT,
    MIN_ATTACK_BONUS, MAX_ATTACK_BONUS,
    MIN_HEALTH_BONUS, MAX_HEALTH_BONUS,
    MIN_HP, MAX_HP,
    MIN_BASE_ATTACK, MAX_BASE_ATTACK,
    MIN_BASE_DEFENSE, MAX_BASE_DEFENSE,
    NUMBER_OF_THINGS, NUMBER_OF_PERSONS,
    MIN_THINGS_PER_PERSON, MAX_THINGS_PER_PERSON,
    NAMES
)
from classes import Thing, Warrior, Paladin
from battle import fight


def generate_things(thing_count):
    """Создаю  количество вещей и сортирую их по защите."""
    things = []
    for idx in range(thing_count):
        defense = random.uniform(MIN_DEFENSE_PERCENT, MAX_DEFENSE_PERCENT)
        attack_bonus = random.randint(MIN_ATTACK_BONUS, MAX_ATTACK_BONUS)
        health_bonus = random.randint(MIN_HEALTH_BONUS, MAX_HEALTH_BONUS)
        thing = Thing(
            name=f"Вещь_{idx + 1}",
            defense_percent=defense,
            attack_bonus=attack_bonus,
            health_bonus=health_bonus
        )
        things.append(thing)
    things.sort(key=lambda item: item.defense_percent)
    return things


def create_person(person_class, name, hp, base_attack, base_defense):
    """Метод для создания воина или паладина."""
    return person_class(name, hp, base_attack, base_defense)


def generate_persons(all_things, names_list):
    """Создаю армию из кол-ва бойцов и одеваю их."""
    random.shuffle(names_list)
    persons = []
    warrior_count = random.randint(0, NUMBER_OF_PERSONS)
    paladin_count = NUMBER_OF_PERSONS - warrior_count

    # Генерация воинов
    for _ in range(warrior_count):
        hp = random.randint(MIN_HP, MAX_HP)
        attack = random.randint(MIN_BASE_ATTACK, MAX_BASE_ATTACK)
        defense = random.uniform(MIN_BASE_DEFENSE, MAX_BASE_DEFENSE)
        name = names_list.pop() if names_list else f"Воин_{_}"
        person = create_person(Warrior, name, hp, attack, defense)
        persons.append(person)

    # Генерация паладинов
    for _ in range(paladin_count):
        hp = random.randint(MIN_HP, MAX_HP)
        attack = random.randint(MIN_BASE_ATTACK, MAX_BASE_ATTACK)
        defense = random.uniform(MIN_BASE_DEFENSE, MAX_BASE_DEFENSE)
        name = names_list.pop() if names_list else f"Паладин_{_}"
        person = create_person(Paladin, name, hp, attack, defense)
        persons.append(person)

    # Экипировка
    for person in persons:
        things_to_wear = random.randint(
            MIN_THINGS_PER_PERSON, MAX_THINGS_PER_PERSON
        )
        selected = random.sample(
            all_things, min(things_to_wear, len(all_things))
        )
        person.set_things(selected)

    return persons


def main():
    print("Генерация вещей...")
    all_things = generate_things(NUMBER_OF_THINGS)
    print(f"Создано {len(all_things)} вещей.")
    print("Генерация армии...")
    army = generate_persons(all_things, NAMES.copy())
    print(f"Создано {len(army)} бойцов.")
    print("\n=== НАЧАЛО БИТВЫ ===\n")
    winner = fight(army)
    print(f"\n=== АБСОЛЮТНЫЙ ПОБЕДИТЕЛЬ: {winner.name} ===")


if __name__ == "__main__":
    main()
