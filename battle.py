import random
from typing import List, Optional

from colorama import Fore, Style, init

from classes import Person
from constants import LOG_FILE, MAX_ROUNDS

init(autoreset=True)


def fight(participants: List[Person]) -> Optional[Person]:
    """
    Проводим бой между участниками до одного победителя.

    Аргументы:
        participants (List[Person]): список объектов Person.

    Возвращаем:
        Optional[Person]: победитель или None.
    """
    alive_list: List[Person] = participants[:]
    round_counter: int = 1
    log_lines: List[str] = []

    def log_message(message: str, color: str = Fore.WHITE) -> None:
        colored_message = f"{color}{message}{Style.RESET_ALL}"
        print(colored_message)
        log_lines.append(message)

    while len(alive_list) > 1 and round_counter <= MAX_ROUNDS:
        attacker: Person = random.choice(alive_list)
        possible_defenders: List[Person] = [person for person in alive_list if person != attacker]
        defender: Person = random.choice(possible_defenders)

        damage: int = defender.take_damage(attacker.attack_damage)

        log_message(
            f"{attacker.name} бьет {defender.name} на {damage} урона",
            Fore.YELLOW
        )

        if defender.hp_now <= 0:
            log_message(f"{defender.name} повержен!", Fore.RED)
            alive_list.remove(defender)

        round_counter += 1

    winner: Optional[Person] = alive_list[0] if alive_list else None
    if winner:
        log_message(f"Победитель: {winner.name}!", Fore.GREEN)
    else:
        log_message("Бой не состоялся!", Fore.RED)

    with open(LOG_FILE, "w", encoding="utf-8") as log_file:
        log_file.write("\n".join(log_lines))

    return winner
