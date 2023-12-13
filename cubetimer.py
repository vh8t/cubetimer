import os
import sys
from json import dump, load
from time import sleep
from threading import Thread
from datetime import datetime
from random import choice, choices, randint

sides = ['R', 'L', 'U', 'D', 'F', 'B']
modifiers = ['', '', '\'', '2']
GREEN = '\033[32m'
WOB = '\033[7m'
BLUE = '\033[34m'
RESET = '\033[0m'


def generate(amount: int) -> list:
    moves = choices(sides, k=amount)
    for i, side in enumerate(moves):
        while moves[i - 1] == side:
            moves[i - 1] = choice(sides)
    for i in range(len(moves)):
        moves[i] += choice(modifiers)
    return moves


def format_time(start_time: datetime, stop_time: datetime) -> str:
    delta = stop_time - start_time
    minutes, seconds = divmod(delta.seconds, 60)
    return f'{minutes:02d}:{seconds:02d}.{delta.microseconds // 1000:03d}'


def formatted_to_seconds(formatted: str) -> float:
    minutes, seconds = formatted.split(':')
    minutes = int(minutes)
    seconds = float(seconds)
    return minutes * 60 + seconds


def main() -> None:
    if not os.path.exists('times.json'):
        with open('times.json', 'w') as file:
            dump([], file)

    running = True
    while running:
        os.system('cls' if os.name == 'nt' else 'clear')
        scramble = ' '.join(generate(randint(20, 25)))

        print(f'{GREEN}{scramble}{RESET}\nPress {BLUE}enter{RESET} to start timer\n\n{WOB}00:00.000{RESET}')

        while input() != '':
            pass

        start_time = datetime.now()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{GREEN}{scramble}\n{RESET}Press {BLUE}enter{RESET} to stop timer\n')

        thread = Thread(target=lambda: input())
        thread.start()

        while thread.is_alive():
            formatted = format_time(start_time, datetime.now())
            print(f'\r{WOB}{formatted}{RESET}', end='')
            sys.stdout.flush()
            sleep(0.01)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{GREEN}{scramble}{RESET}\nType {BLUE}lb{RESET} to see your top 5 times or press {BLUE}enter{RESET} to continue\n\n{WOB}{formatted}{RESET}')

        with open('times.json', 'r') as file:
            data = load(file)

        with open('times.json', 'w') as file:
            new_data = {
                'scramble': scramble,
                'f_time': formatted,
                'time': formatted_to_seconds(formatted),
                'timestamp': datetime.now().timestamp()
            }
            data.append(new_data)
            dump(data, file, indent=2)

        go = input()
        while go != '' and go != 'lb':
            go = input()

        if go == 'lb':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'{GREEN}{scramble}{RESET}\n{BLUE}Top 5 times{RESET}\n')
            for i, time in enumerate(sorted(data, key=lambda x: x['time'])[:5]):
                print(f'{i + 1}. {time["f_time"]} - {time["scramble"]}')

            print(f'\nPress {BLUE}enter{RESET} to continue')
            while input() != '':
                pass


if __name__ == '__main__':
    main()