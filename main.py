import os
import ast
import importlib
import importlib.util
import sys
import time

from src.controller import Controller
from src.screen_capturer import WindowCapture
from src.game_loop import GameLoop


cap = WindowCapture("Firefox")

def main():
    routes = {
        "1": start_game,
        "2": show_contributions,
        "3": exit
    }
    routes[menu()]()


def menu():
    while True:
        print("Choose an option:")
        print("1. Start Game")
        print("2. Show Contributions")
        print("3. Exit")
        print("-"*50)
        selection = input("Enter your selection: ")
        if selection in ["1", "2", "3"]:
            return selection
        else:
            print("Invalid selection")


def start_game():
    (p1, p2) = select_players()
    game_loop = GameLoop(p1, p2)
    game_loop.idle_loop()
    

def select_players():
    contributions: dict[str, type] = get_contributions()
    print("Select Player 1:")
    p1 = display_players(contributions)
    print("Select Player 2:")
    p2 = display_players(contributions)
    return (p1, p2)


def get_contributions():
    """
    Gets all the contributions from the contributions dir.
    Assumes each directory has a main.py file with an 'action' function.
    
    Returns:
        Dict: {directory_name: action_function}
    """  
    players = {}
    dir = 'contributions'
    if os.path.exists(dir):
        for bot in os.listdir(dir):
            bot_path = os.path.join(dir, bot)
            if os.path.isdir(bot_path):
                main_file_path = os.path.join(bot_path, 'main.py')
                if os.path.exists(main_file_path):
                    # Load the module
                    spec = importlib.util.spec_from_file_location(f"{bot}_main", main_file_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    # Get the action function from the module
                    if hasattr(module, 'action'):
                        players[bot] = module.action
                    else:
                        print(f"Warning: {bot} directory has no action function.")
    
    return players


def display_players(contributions: dict[str, type]):
    while True:
        for i, k in enumerate(contributions.keys()):
            print(f"{i} - {k}")

        choice = input("Enter your selection: ")
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice < len(contributions):
                break
        else:
            print("Invalid selection")

    key = list(contributions.keys())[choice]
    return contributions[key]


def show_contributions():
    print("Showing contributions...")


def exit():
    print("Exiting...")
    sys.exit()


if __name__ == "__main__":
    main()
