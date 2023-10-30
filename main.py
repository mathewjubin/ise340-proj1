import tkinter as tk
from tkinter import ttk
import random

# Create the character selection window
charWindow = tk.Tk()
charWindow.title("Character Selector")

# Create a label
label = tk.Label(charWindow, text="Select a character:")
label.pack()

# Create a list of characters
characters = ["Ahri", "Yasuo", "Darius", "Illaoi", "Jinx", "Nautilus"]

# Create a dropdown menu
selected_character = tk.StringVar(value=characters[0])
dropdown = ttk.Combobox(charWindow, textvariable=selected_character, values=characters)
dropdown.pack()
def start_game():
    def rollDiceAttack():
        global currentTower
        botRoll = random.randint(1,12)
        damage = int(rollText.get()) - botRoll
        if damage <= 0:
            damage = 0
        health["value"] -= 6.65*(damage)
        mainLabel1.config(text="You are currently at Tower " + str(currentTower) + "\nBot Rolled: " + str(botRoll) + "\nDamage Done: " + str(damage) + "\nHealth:" + str(int(health["value"]/(20/3))) + "/15")
        mainLabel1.pack()
        if(int(health["value"]) <= 0):
            if(currentTower==3):
                mainLabel1.config(text="You are winner")
                attackButton.destroy()
            else:
                mainLabel1.config(text="You have killed Tower " + str(currentTower) + ".")
                currentTower += 1
                health["value"] = 100

    global currentTower
    currentTower = 1
    mainWindow = tk.Tk()
    mainWindow.title("The game(TM)")
    mainWindow.geometry("400x200")
    mainLabel1 = tk.Label(mainWindow, text="You are currently at Tower 1\nHealth:15/15")
    mainLabel1.pack()
    health = ttk.Progressbar(mainWindow, length=200, mode='determinate')
    health["value"] = 100
    health.pack()

    button_frame = tk.Frame(mainWindow)
    button_frame.pack()

    rollText = tk.Entry(button_frame)
    rollText.pack()

    attackButton = tk.Button(button_frame, text="Attack",command=rollDiceAttack)
    attackButton.pack(side=tk.LEFT)

    button_frame.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    mainWindow.mainloop()


# Function to handle character selection and setting health
def select_character():
    selected = selected_character.get()
    if selected == "":
        return
    print(f"Selected character: {selected}")
    charWindow.destroy()
    health = 0
    match selected:
        case "Ahri":
            health = 8
        case "Darius":
            health = 8
        case "Yasuo":
            health = 10
        case "Illaoi":
            health = 10
        case "Jinx":
            health = 6
        case "Nautilus":
            health = 10
        case _:
            print()
    start_game()


# Create a button to trigger the selection
select_button = tk.Button(charWindow, text="Select", command=select_character)
select_button.pack()

# Start the GUI main loop
charWindow.mainloop()
