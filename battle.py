import random
from constants import MAX_ROUNDS, LOG_FILE
from classes import Person


def fight(participants):
    """
    Идет бой между "именами".

    Вот аргументы:
        participants (list[Person]): список персонажей (объекты классов
            Person, Warrior, Paladin).

    А после уже возвращает:
        Person: победитель. Думаю, как объединим все ок)
    """
    alive = participants[:]
    round_counter = 1
    log_lines = []

    def log(message):
        print(message)
        log_lines.append(message)

    while len(alive) > 1 and round_counter <= MAX_ROUNDS:
        attacker = random.choice(alive)

        # Защитник != атакующий, сперва чет не подумал об этом xD
        # листкомпрехеншион классная штука
        possible_defenders = [person for person in alive if person != attacker]
        defender = random.choice(possible_defenders)

        damage = defender.take_damage(attacker.base_attack)

        log(
            f"{attacker.name} бьет {defender.name} на {damage} урона"
        )

        if not defender.is_alive():
            log(f"{defender.name} повержен!")
            alive.remove(defender)

        round_counter += 1

    winner = alive[0] if alive else None
    log(f"Победитель: {winner.name}!")

    # Тут я сделал, чтобы в лог запись шла, можно будет потом отследить)
    with open(LOG_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(log_lines))

    return winner
