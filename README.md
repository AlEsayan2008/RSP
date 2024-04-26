# **RSP(Rock, sccisors & paper) Game**:
____
This game is very poular game in the world.
You can see many people who playing rsp everywhere
____
## Gamerules:
____


### **First rule**:

> **Rock** is higher than **sccisors** and lower than **paper**

### **Second rule**:

>**Paper** is higher than **Rock** and lower than **paper**

### **Third rule**:

>**Sccisors is higher than **paper** and lower than **rock**
____

## What I used for writting this code:

>I want to mention that i use **Jupyter** lab & **VS code** for writting this repository:

# **Code Explanation** 
____
I use  keyword `import` for importin **random**, **json** and **logging** :

>This is the first **3** rows where i import this 3 **modules**:

```Python
import json
import random 
import logging
```

>I use **json** in order to use information from another files in my code:

In my code `def read_json(source: str):` is a function for reading information from another file:


```python
def read_json(source: str):   
    try:
        with open(source , "r", encoding="utf-8") as read_file:
            data = json.load(read_file)
        return data
    except FileNotFoundError:
        logging.error(f"{source} file not found")
        raise FileNotFoundError
```

I use `choice.json` file for writting this code:
which consist of this `dict`:

```json
{"choice": ["p", "r" , "s"]}
```
I give  statement **data** which is consist of **choice.json** information:
Also I give statement **rsp** which is equal to **choice.json's** file's dict's **key**

```python
data = read_json("RSP/choice.json")
rsp = data["choice"]

```

>After that I give function **def command()** which will return input from user:

```python
def command():
    return input("\nPlease enter command 'play' for playing.\n")
```
>Then I write **def you_win(your_choice, computer)** which consist of **your_choice** and **Computer** arguments:
>This function is return **True** if all conditions are true and checking all user winning variants:

```python
def you_win(your_choice, computer):
    if (your_choice == "r" and computer == "s") or (your_choice == "p" and computer == "r") or (your_choice == "s" and computer == "p"):
        return True
```

>After that I write the same things but only this function is checking all ties variants and return true if all conditions are true:
>This function I called **def its_tie(your_choice, computer):** which again have **your_choice** and **computer** arguments:

```python
def its_tie(your_choice, computer):
    if (your_choice == "r" and computer == "r") or (your_choice == "p" and computer == "p") or (your_choice == "s" and computer == "s"):
        return True
```

>After all this functions I write the general function of this project which I called **def play_rsp():** which is the algoritm of this code:


```python
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
```
>In first raw I give infinity loop **while True** for infinity play

```python
while True:
```
>After that I check the command **play** which help us to start play:

```python
if command().lower() == "play":
```

>After checking command I give **input()** which help user to write his choice:

```python
your_choice = input("\nEnter your choice\n")
```
>Then i check user choice accuracy:

```python

if your_choice == "r" or your_choice == "s" or your_choice == "p":
```

>After this checking I give computer choice using **random** module:

```python
computer = random.choice(rsp)
```

>Then next 6 raws I concentrate my functions **you_win(your_choice, computer)**, **its_tie(your_choice, computer)** for checking final results and **else** conditional statement which check all variant where user lose:
```python
if you_win(your_choice, computer):
                    print(f"You win. Computer choice is {computer}")
                elif its_tie(your_choice, computer):
                    print(f"It's a draw. Computer choice is {computer}") 
                else:
                    print(f"You lose. Computer choice is {computer}")

```
>Than I give again conditional statement **else** which print **Wrong choice!!!** if user write wrong choice:

```python
else:
    print("Wrong Choice !!!")
```

>Again I give conditional statement **else** which print **Wrong command!!!** if user write wrong command:

```python
 else:
            print("Command Error !!!")
```

>In final raw I called **play_rsp** function using this command and explanation is over:

```python
play_psp()
```

____
