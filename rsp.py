import json
import random 
import logging



def read_json(source: str):   
    try:
        with open(source , "r", encoding="utf-8") as read_file:
            data = json.load(read_file)
        return data
    except FileNotFoundError:
        logging.error(f"{source} file not found")
        raise FileNotFoundError
    

data = read_json("RSP/choice.json")
rsp = data["choice"]



def command():
    return input("\nPlease enter command 'play' for playing.\n")

def you_win(your_choice, computer):
    if (your_choice == "r" and computer == "s") or (your_choice == "p" and computer == "r") or (your_choice == "s" and computer == "p"):
        return True

def its_tie(your_choice, computer):
    if (your_choice == "r" and computer == "r") or (your_choice == "p" and computer == "p") or (your_choice == "s" and computer == "s"):
        return True

def play_rsp():
    while True:
        if command().lower() == "play":
            your_choice = input("\nEnter your choice\n")
            if your_choice == "r" or your_choice == "s" or your_choice == "p":
                computer = random.choice(rsp)
                if you_win(your_choice, computer):
                    print(f"You win. Computer choice is {computer}")
                elif its_tie(your_choice, computer):
                    print(f"It's a draw. Computer choice is {computer}") 
                else:
                    print(f"You lose. Computer choice is {computer}")
            else:
                print("Wrong Choice !!!")
        else:
            print("Command Error !!!")

play_rsp()
