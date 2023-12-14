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
RED = '\033[31m'
RESET = '\033[0m'


def generate(amount: int) -> list:
    moves = choices(sides, k=amount)
    for i, side in enumerate(moves):
        if moves[i - 1] == side:
            new_side = choice(sides)
            while new_side == side:
                new_side = choice(sides)
            moves[i] = new_side
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


def help() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    true = True
    while true:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{GREEN}Help{RESET}\n\n{BLUE}lb{RESET} - show top 5 times\n{BLUE}avg{RESET} - show average of all times\n{BLUE}avg5{RESET} - show average of last 5 times\n{BLUE}avg12{RESET} - show average of last 12 times\n{BLUE}help{RESET} - show this help\n{BLUE}exit{RESET} - exit help\n')
        cmd = input(f'{GREEN}Command >{RESET} ')
        if cmd == 'exit':
            os.system('cls' if os.name == 'nt' else 'clear')
            true = False
        elif cmd == 'avg':
            os.system('cls' if os.name == 'nt' else 'clear')
            with open('times.json', 'r') as file:
                data = load(file)
            print(f'Average: {BLUE}{round(sum([formatted_to_seconds(time["f_time"]) for time in data]) / len(data), 3)}{RESET}')
            while input(f'\nPress {GREEN}enter{RESET} to continue') != '':
                pass
        elif cmd == 'avg5':
            os.system('cls' if os.name == 'nt' else 'clear')
            with open('times.json', 'r') as file:
                data = load(file)
            last_five = sorted(data, key=lambda x: x['timestamp'])[-5:]
            for i, time in enumerate(last_five):
                print(f'{BLUE}{i + 1}.{RESET} {time["f_time"]} - {GREEN}{time["scramble"]}{RESET}')
            print(f'\nAverage: {BLUE}{round(sum([formatted_to_seconds(time["f_time"]) for time in last_five]) / len(last_five), 3)}{RESET}')
            while input(f'\nPress {GREEN}enter{RESET} to continue') != '':
                pass
        elif cmd == 'avg12':
            os.system('cls' if os.name == 'nt' else 'clear')
            with open('times.json', 'r') as file:
                data = load(file)
            last_twelve = sorted(data, key=lambda x: x['timestamp'])[-12:]
            for i, time in enumerate(last_twelve):
                print(f'{BLUE}{i + 1}.{RESET} {time["f_time"]} - {GREEN}{time["scramble"]}{RESET}')
            print(f'\nAverage: {BLUE}{round(sum([formatted_to_seconds(time["f_time"]) for time in last_twelve]) / len(last_twelve), 3)}{RESET}')
            while input(f'\nPress {GREEN}enter{RESET} to continue') != '':
                pass
        elif cmd == 'lb':
            os.system('cls' if os.name == 'nt' else 'clear')
            with open('times.json', 'r') as file:
                data = load(file)
            for i, time in enumerate(sorted(data, key=lambda x: x['time'])[:5]):
                print(f'{BLUE}{i + 1}.{RESET} {time["f_time"]} - {GREEN}{time["scramble"]}{RESET}')
            while input(f'\nPress {GREEN}enter{RESET} to continue') != '':
                pass
        elif cmd == 'help':
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'{RED}Invalid command: {cmd}{RESET}')


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
            sleep(0.001)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{GREEN}{scramble}{RESET}\nType {BLUE}help{RESET} to see more options or press {BLUE}enter{RESET} to continue\n\n{WOB}{formatted}{RESET}')

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
        while go != '' and go != 'help' :
            go = input()

        if go == 'help':
            help()


if __name__ == '__main__':
    main()
