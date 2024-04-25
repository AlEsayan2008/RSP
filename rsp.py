#rsp game:
import random 

# r>s, r<p, s>p
Choice = {"rock": "r", "scissors": "s", "paper": "p"}
choice_variants = list(Choice.values())


def command():
    return input("\nPlease enter command 'play' for playing.\n")




def you_win(your_choice, computer):
    if (your_choice == "r" and computer == "s") or (your_choice == "p" and computer == "r") or (your_choice == "s" and computer == "p"):
        return True
   
def its_tie(your_choice, computer):
     if (your_choice == "r" and computer == "r") or (your_choice == "p" and computer == "p") or (your_choice == "s" and computer == "s"):
        return True



def play_rsp():
    if command().lower() == "play":
        if your_choice == "r" or your_choice == "s" or your_choice == "p":
            if you_win(your_choice, computer):
                print(f"You win.Computer choice is {computer}")
            elif its_tie(your_choice, computer):
                print(f"It's draw.Computer choice is {computer}") 
            else:
                print(f"You lose. Computer choice is {computer}")
        else:
            print("Wrong Choice !!!")
    else:
        print("CommandError !!!")



your_choice = input("\nEnter your choice\n")
computer = random.choice(choice_variants)    
play_rsp()
