import os
import ast
import importlib
import importlib.util
import sys
import time

from src.controller import Controller
from src.screen_capturer import WindowCapture
from src.game_loop import GameLoop
from src.player import Player



def main():
    routes = {
        "1": start_game,
        "2": show_contributions,
        "3": exit,
    }
    routes[menu()]()


def menu():
    while True:
        print("Choose an option:")
        print("1. Start Game")
        print("2. Show Contributions")
        print("3. Exit")
        print("4. Controller Test")
        print("-"*50)
        selection = input("Enter your selection: ")
        if selection in ["1", "2", "3"]:
            return selection
        else:
            print("Invalid selection")


def start_game():
    (p1_func, p2_func) = select_players()
    controller1 = Controller(gamepad_id=1)
    controller2 = Controller(gamepad_id=2)
    p1 = Player(p1_func, controller1)
    p2 = Player(p2_func, controller2)
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
    Assumes each directory has a main.py file with 'action' and 'character_select' functions.
    
    Returns:
        Dict: {directory_name: {'action': action_function, 'character_select': character_select_function}}
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
                    
                    # Get both functions from the module
                    if hasattr(module, 'action') and hasattr(module, 'character_select'):
                        players[bot] = {
                            'action': module.action,
                            'character_select': module.character_select
                        }
                    else:
                        print(f"Warning: {bot} directory missing action or character_select function.")
    
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

def initiate_controller_test():
    try:
        p1 = Controller(gamepad_id=1)
        p2 = Controller(gamepad_id=2)
        p1.test_press_button("a")
        p2.test_press_button("a")
        p1.read()
        p2.read()
        time.sleep(1)
        p1.test_release_button("a")
        p2.test_release_button("a" )
        p1.read()
        p2.read()
        print("Controllers initialized successfully.")
    except Exception as e:
        print(f"Error initializing controllers: {e}")
        return

def show_contributions():
    print("Showing contributions...")


def exit():
    print("Exiting...")
    sys.exit()


if __name__ == "__main__":
    initiate_controller_test()
    main()
