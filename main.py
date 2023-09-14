from tkinter.ttk import *
from character import *
import simpleaudio as sa
import keyboard
import time
import math
from tkinter import *
import random

window = Tk()
window.title("Road of Fate")
window.geometry("800x800")
window.resizable(width=False, height=False)

def animate_text(text):
    def display_text():
        label.config(text=text[:current_char[0]], font="Garamond")
        if current_char[0] <= len(text):
            window.after(delay, display_text)
            current_char[0] += 1
        else:
            time.sleep(0.5)

    current_char = [0]
    delay = 25  # Adjust the delay between characters here (in milliseconds)
    display_text()

def animate_text_ch(text, ch_lst):
    def display_text():
        label.config(text=text[:current_char[0]], font="Garamond")
        if current_char[0] <= len(text):
            window.after(delay, display_text)
            current_char[0] += 1
        else:
            time.sleep(0.5)
            show_choices(ch_lst)

    current_char = [0]
    delay = 25  # Adjust the delay between characters here (in milliseconds)
    display_text()

def options():
    # Add code for options menu
    return

def show_choices(ls):
    ch_num = ls
    buttons = []
    global buttonss
    buttonss = []

    for i in range(len(ch_num)):
        buttons.append(ch_num[i])

    for i in buttons:
        i = Button(window, text= i[0], command= i[1])
        buttonss.append(i)
        i.pack(pady= 50)
        time.sleep(0.05)

def get_to_mountain():
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Fight!",BossFight]]
    animate_text_ch("", a)

def start_game():
    degistir("startgame.png")
    start_button.pack_forget()
    options_button.pack_forget()
    quit_button.pack_forget()
    title_label.pack_forget()

    animate_text("Future...")
    time.sleep(1)
    animate_text("God...")
    time.sleep(1)
    a = [["Fight!", BossFight]]
    animate_text_ch("What happened to me?.. I- I... I remember nothing... How?.. \n What is this shining thing? Is that blood?!", a)

#KÖYE GİT, KÖYLÜ QUESTLERİ, GRUBA KATILAN OYUNCU..
#SON BOSS KENDİMİZ OLUCAZ
#KÖYDEN BİRİNİN EPIC BİRİ OLMASI- GALADRIEL

def pause(a):
    while True:
        if keyboard.KEY_DOWN:
            a

def keyboard_a():

    def button_click(letter):
        current_text = label_text.get()
        label_text.set(current_text + letter)

    def submit_input():
        current_text = label_text.get()
        print("Input:", current_text)
        global username
        username = current_text
        keyboard_frame.pack_forget()
        clear_button.pack_forget()
        ok_button.pack_forget()
        label.pack_forget()
        a = [["Go to the wizard", ]]
        animate_text_ch("", a)

    def clear_input():
        label_text.set("")

    label_text = StringVar()
    label = Label(window, textvariable=label_text, font=("Garamond", 24))
    label.pack(pady=20)

    keyboard_frame = Frame(window)
    keyboard_frame.pack(pady=10)

    button_rows = [
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
        ["Z", "X", "C", "V", "B", "N", "M"]
    ]

    for row in button_rows:
        row_frame = Frame(keyboard_frame)
        row_frame.pack()

        for letter in row:
            button = Button(row_frame, text=letter, width=4, command=lambda l=letter: button_click(l))
            button.pack(side="left", padx=5)

    ok_button = Button(window, text="OK", width=10, command=submit_input)
    ok_button.pack(pady=10)

    clear_button = Button(window, text="Clear", width=10, command=clear_input)
    clear_button.pack(pady=10)

def updateButtons():
    props = Listbox(window, bg='white', font=('Garamond', 15), cursor='dot', height=5, width=18)
    props.insert(1, f"Strength: {player.select_prop('strength')[0]}")
    props.insert(2, f"Stamina: {player.select_prop('stamina')[0]}")
    props.insert(3, f"Intelligence: {player.select_prop('intelligence')[0]}")
    props.insert(4, f"Celestial: {player.select_prop('celestial')[0]}")
    props.insert(5, f"Health Points: {player.select_prop('hp')[0]}")
    props.pack(side="bottom", pady=30)

def quit_game():
    window.destroy()

def degistir(a):
    # Yeni arka plan görselini yükleyin
    yeni_gorsel = PhotoImage(file=a)
    background_label.configure(image=yeni_gorsel)
    background_label.image = yeni_gorsel

def fate_choices():
    topics = [
        "Force",
        "Life",
        "Nature",
        "Choices",
        "Live",
    ]

    options = [
        ["Leviathaxe", "Daggers and Elven Bow", "Sorcerers Blessed Necklace"],
        ["Work hard", "Work smart", "More pain more gain"],
        ["Sky", "Earth", "Underworld"],
        ["Decision", "Uncertainity", "Risk"],
        ["Less and lot", "More and empty", "Peaceful"],
    ]

    def submit():
        global selected_options
        selected_options = []
        for i in range(len(topics)):
            selected_option = topic_vars[i].get()
            selected_options.append(selected_option)
        print("Selected options:", selected_options)
        item4 = InventoryItem('Player_1', options[0][int(selected_options[0])], 100, f'The wingman of the {username}')
        InsertItem(item4)
        frame.pack_forget()
        submit_button.pack_forget()

    frame = Frame(window)
    frame.pack(pady=50)

    topic_vars = []

    for i in range(len(topics)):
        var = IntVar()  # Create an IntVar for each topic
        topic_vars.append(var)

        topic_frame = Frame(frame, borderwidth=1, relief="solid")  # Add border attributes
        topic_frame.pack(side="left", padx=10)

        topic_label = Label(topic_frame, text=topics[i])
        topic_label.pack()

        for j in range(len(options[i])):
            option_var = Radiobutton(topic_frame, text=options[i][j], value=j, variable=var)
            option_var.pack(anchor="w")

    submit_button = Button(window, text="Submit", command=submit)
    submit_button.pack(pady=20)

global boss1
boss1 = ["goblin", 20]


class BossFight:
    def __init__(self):
        self.window = Tk()
        self.window.title("Boss Fight")
        self.window.geometry("400x300")

        self.weapon = self.select_weapon()
        self.moves = []
        self.choice = None

        self.next_button = Button(self.window, text="Next", command=self.show_moves)
        self.next_button.pack(pady=10)

        self.result_label = Label(self.window, text="")
        self.result_label.pack()

        self.player_hp = int(player.select_prop("hp")[0])
        self.boss_hp = 50

    def select_weapon(self):
        return "Sorcerers Blessed Necklace"

    def show_moves(self):
        self.next_button.config(text="Attack", command=self.start_attack)

        if self.weapon == "Leviathaxe":
            self.moves = ["Throw", "Defend", "Taunt", "Hurl"]
        elif self.weapon == "Daggers and Elven Bow":
            self.moves = ["Slash", "Dodge and Strike", "Evade", "Poison"]
        elif self.weapon == "Sorcerers Blessed Necklace":
            self.moves = ["Fireball", "Ice Blast", "Heal", "Shield"]

        global buttons
        buttons = []
        for i, move in enumerate(self.moves):
            button = Button(self.window, text=move, command=lambda index=i: self.select_move(index))
            buttons.append(button)
            button.pack()

    def select_move(self, index):
        self.choice = self.moves[index]
        self.moves.pop(index)

        for widget in self.window.winfo_children():
            if isinstance(widget, Button):
                widget.config(state="disabled")

        self.next_button.config(state="normal")

    def start_attack(self):
        if self.choice:
            if self.choice != "Heal":
                result = f"You performed {self.choice} with your {self.weapon}!"
                self.result_label.config(text=result)

                boss_damage = random.randint(5, 10) + math.floor(
                    float(player.select_prop("strength")[0]) / 4) + math.floor(
                    float(player.select_prop("stamina")[0]) / 5)
                self.boss_hp -= boss_damage

                boss_attack = random.randint(10, 15) - math.floor(
                    float(player.select_prop("strength")[0]) / 4) - math.floor(
                    float(player.select_prop("stamina")[0]) / 5)
                self.player_hp -= boss_attack
                player.update_prop("hp", self.player_hp)
                props.pack_forget()


                self.result_label.config(
                    text=f"Boss dealt {boss_attack} damage. Boss HP: {self.boss_hp}. Your HP: {self.player_hp}.")

                if self.boss_hp <= 0:
                    self.result_label.config(text="Congratulations! You defeated the boss!")
                    for widget in self.window.winfo_children():
                        if isinstance(widget, Button):
                            widget.config(state="disabled")
                            widget.pack_forget()
                    self.window.destroy()
                    props.pack_forget()
                    time.sleep(1)
                    a = [["Keep moving!", you_won]]
                    animate_text_ch("You are getting close...", a)

                elif self.player_hp <= 0:
                    self.result_label.config(text="Oh no! You were defeated by the boss.")
                    for widget in self.window.winfo_children():
                        if isinstance(widget, Button):
                            widget.config(state="disabled")
                            widget.pack_forget()
                    self.window.destroy()
                    props.pack_forget()
                    for i in buttonss:
                        i.pack_forget()
                    time.sleep(1)
                    a = [["Fight Back!", go_back]]
                    animate_text_ch("You have to focus!, Go back!", a)
                else:
                    self.choice = None
                    props.pack_forget()
                    for i in buttons:
                        i.pack_forget()
                    self.show_moves()
            else:
                result = f"You performed {self.choice} and healed yourself!"
                self.result_label.config(text=result)

                heal = random.randint(5, 10) + math.floor(float(player.select_prop("strength")[0]) / 4) + math.floor(float(player.select_prop("stamina")[0]) / 5)
                self.choice = None
                for i in buttons:
                    i.pack_forget()
                self.show_moves()
                self.player_hp += heal
                player.update_prop("hp", self.player_hp)
                props.pack_forget()

        else:
            self.result_label.config(text="Please select a move.")

        self.window.mainloop()

def you_won():
    pass

def go_back():
    pass

if __name__ == "__main__":
    background_image = PhotoImage(file="background.png")
    background_label = Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    icon_image = PhotoImage(file="icon.png")
    window.iconphoto(True, icon_image)

    title_label = Label(window, text="Road of Fate",  font=("Garamond", 32))
    title_label.pack(pady=50)

    label = Label(window, text="", font=("Garamond", 24))
    start_button = Button(window, text="Start", command=start_game)
    options_button = Button(window, text="Options", command=options)
    quit_button = Button(window, text="Quit", command=quit_game)
    roj = Button(window, text="roj", command=quit_game)

    props = Listbox(window, bg='white', font=('Garamond', 15), cursor='dot', height=5, width=18)
    props.insert(1, f"Strength: {player.select_prop('strength')[0]}")
    props.insert(2, f"Stamina: {player.select_prop('stamina')[0]}")
    props.insert(3, f"Intelligence: {player.select_prop('intelligence')[0]}")
    props.insert(4, f"Celestial: {player.select_prop('celestial')[0]}")
    props.insert(5, f"Health Points: {player.select_prop('hp')[0]}")
    props.pack(side="bottom", pady=30)

    menu_frame = Frame(window)
    menu_frame.pack()

    label.pack(pady=20)
    start_button.pack(pady=10)
    options_button.pack(pady=10)
    quit_button.pack(pady=10)

    window.mainloop()