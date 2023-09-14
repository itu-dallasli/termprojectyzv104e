import math
import random
from tkinter import *
from tkinter.ttk import *
from character import *
import time
from music import *

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

###############
#LEVEL 1

def walk_around():
    f = [["Walk through mountain", walk_tru_mountain]]
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    animate_text_ch("You have seen a glorious mountain \n *Oh... This beautiful thing...*", f)

def check_stone():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    c = [["Walk around a bit.", walk_around], ["Stare at the glorious mountain", walk_tru_mountain]]
    animate_text_ch("The stone began to shine! \n *Sighs* *That is georgeous* \n Stone stopped after a while.", c)

def body_check():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    d = [["Walk around", walk_around], ["Touch more, squeeze the pus.", squeezepus]]
    animate_text_ch("You touched your injury and felt pain. You shouldn't touch anymore", d)
###########################

def squeezepus():
    animate_text("")
    a = [["Explore around a bit.", walk_around]]
    player.update_prop("hp", int(player.select_prop("hp")[0])-5)
    updateButtons()
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    animate_text_ch("Ouch!!! It is too painful, I have to stop touching. (Your health points decreased.)", a)

##########################33

def walk_tru_mountain():
    degistir("C:/Users/Emir/PycharmProjects/termProject/images/mountain.png")
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Walk to the town.", enter_town], ["Walk around the town", walk_around_town]]
    animate_text_ch("*It seems too far away. W-Wait, is that a town?*", a)

def walk_around_town():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Ask why is she there", talktogirl], ["Stay away and warn", saaw]]
    animate_text_ch("*Maybe I shouldn't enter that fast* \n You are watching town from a bit distance. \n A little girl pops up and scares you!", a)

def talktogirl():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Get to the town", enter_town2], ["Ask about skulls", ask_her]]
    animate_text_ch("*Breath scared, jump* Ohh!! You scared me. What are you trying to do?!?\nGirl: I am really sorry.. \n Y-you know I like to explore mushrooms and little \n dears and skulls..", a)

def ask_her():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Get to the town", enter_town2]]
    animate_text_ch("*Skulls??* What skulls kid?\nGirl: We are in a beaaauutiful town and it has a magical way \n You know...", a)

def saaw():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Go to the town", enter_town2], ["Ran away through the forest", gotoforest]]
    animate_text_ch("Stay away from me! *Breathes heavily*", a)

def gotoforest():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Ran to the town again" , enter_town2], ["Follow the voices!", follow_voices]]
    animate_text_ch("You ran into forest. \n Some weird stuff began to happen. \n !!!LOUD MOAN AND ROAR!!!", a)

def follow_voices():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Go to town", enter_town2], ["Pick up the leather piece", pick_up_the_leather]]
    animate_text_ch("*You followed the voices in a warned way.*\n*!!NOICES!!*\n*A sly fox moved in to the forest. \n *Ugh it was nothing but a fox.* \n There is a piece of useless leather.", a)

def pick_up_the_leather():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Get to the town", enter_town2], ["Walk around the town a bit.", walk_around_town2]]
    animate_text_ch("You picked the leather. *It stinks yikes!*\nShall I go, or...", a)

def walk_around_town2():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Enter town in an alerted way", enter_town2]]
    animate_text_ch("*Seems safe*\nYou scared me little kid.", a)

def talktogirl2():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Have a drink in tavern", enter_tavern], ["Visit blacksmith", go_blacksmith_wg]]
    animate_text_ch("Hey kid, tell me about town.\nLittle Girl: Our people, belongs to far far past. \n Celestial creatures has blessed us with power, peace and magic. \n People might seem ordinary but they are holy!. \n By the way... Shall I introduce you my uncle?", a)

def gotscared():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Ask her about the town.", talktogirl2 ], ["Ignore her.", ignore_girl]]
    animate_text_ch("You scared me little kid.", a)

def ignore_girl():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Go to the blacksmith.", go_blacksmith ], ["Explore the town", exp_town]]
    animate_text_ch("Let's talk later kid, I have things to do.", a)

def enter_town2():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Go to the blacksmith.", go_blacksmith_wg], ["Go to the tavern", enter_tavern]]
    animate_text_ch("People started to stare at you. \n *Who are they? Are they friendly?.. Should I leave?..*\nA blacksmith is working with Iron.", a)

def go_blacksmith():
    degistir("C:/Users/Emir/PycharmProjects/termProject/images/blacksmith.png")
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Look at the blacksmith", blacksmith_talks], ["Ask blacksmith something", understand_smt]]
    animate_text_ch("*Blacksmith looks nervous, stares at you*", a)

def enter_tavern():
    degistir("C:/Users/Emir/PycharmProjects/termProject/images/tavern.png")
    animate_text("You entered the tavern. \n It is too loud and someone is fighting.")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Have a drink.", have_drink], ["Exit and meet the blacksmith.", go_blacksmith_wg]]
    animate_text_ch("", a)

def have_drink():
    animate_text("You had a nice drink. \n *Tasty and cold.. That's what I need*")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    player.update_prop("hp", player.select_prop("hp")[0]+5)
    updateButtons()
    a = [["Meet with the blacksmith", go_blacksmith_wg]]

    animate_text_ch("Lets meet someone. (You feel chill. Your health point increased)", a)

def enter_town():
    animate_text("People started to stare at you. \n *Who are they? Are they friendly?.. Should I leave?..* \n A friendly kid pops up!")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Talk to the girl.", talktogirl2], ["Pretend afraid." , gotscared]]
    animate_text_ch("", a)

def exp_town():
    animate_text("*What a nice, peaceful town*")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Watch the blacksmith doing his job.", go_blacksmith]]
    animate_text_ch("*What a though blacksmith*", a)

def understand_smt():
    animate_text("What?! What do you want to understand!!? *Angrily*")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Why did I woke up in this woods?", confused_bs], ["Where am I?", little_pitty_town]]
    animate_text_ch("", a)

def little_pitty_town():
    animate_text("*Smiles in a pedant way*")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Visit the wizard.", go_wise_wizard]]
    animate_text_ch("You are in a little pitty town that is \nblessed with wise people and holiness.\n I would like to talk more but less talk work more.\nGo to the ugly wizard, I am sure he will tell more.", a)

def blacksmith_talks():
    animate_text("Then what are you looking at? *Curios and angrily*")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["I am confused and lost.", confused_bs], ["Your handcraft is awesome.", compliment_bs]]
    animate_text_ch("", a)

def compliment_bs():
    animate_text("*Blacksmith seems confused*\nBlacksmith: What do you want kid?")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["What is this town?", little_pitty_town], ["Who was the little girl?", askaboutgirl]]
    animate_text_ch("", a)

def confused_bs():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Go to wizard", go_wise_wizard], ["Ask about the little girl", askaboutgirl ]]
    animate_text_ch("I am busy. But you can visit the grouchy wizard huh..", a)

def askaboutgirl():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["She scared me a lot.", scared_me], ["She talked with me a bit about the town.", not_scared_me]]
    animate_text_ch("You: Who was this freak little girl?\nBlacksmith: Careful with your words!\nBlacksmith: She is my little girl. And why did you ask!?", a)

def not_scared_me():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Nothing is wrong sir.", go_wise_wizard]]
    animate_text_ch("I see... \nI would like to talk more but I'm afraid I can't. \nGo to the ugly wizard", a)

def scared_me():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Nothing is wrong sir.", go_wise_wizard]]
    animate_text_ch("I see nothing wrong you coward. I can't talk to you more. \nGo to the ugly wizard", a)

def go_blacksmith_wg():
    degistir("C:/Users/Emir/PycharmProjects/termProject/images/blacksmith.png")
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["I'm not here to harm.\n I'm looking for answers", what_answers], ["Am I strange?", yes_u_are]]
    animate_text_ch("You went to the blacksmith. He seems angry. \n *Sighs*\nThe little girl occurs instantly and freaks you again!\nGirl: Hello strangerr!!\n Blacksmith: Who is this stranger my little?!\nDon't talk to weird looking strangers.", a)

def yes_u_are():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Go to the big nosed wizard.", go_wise_wizard]]
    animate_text_ch("Blacksmith: Yes you are stranger. \n*Laughs underestimating*\nBlacksmith: You seem confused, go to the big o' wizard\nI'm sure he will open your mind.\nGirl: YES GO TO THE BIGNOSE WISARD!!", a)

def what_answers():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Who am I?", whoblacksmt], ["Where am I?", little_pitty_town]]
    animate_text_ch("What answers are you looking for?", a)

def whoblacksmt():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Go to the wizard.", go_wise_wizard]]
    animate_text_ch("I have no time to talk unfortunately.. BUT! \nGo talk to the ugly old wisard.\nGirl: YES GO TO THE BIG O' WIZARD!", a)

def go_wise_wizard():
    degistir("C:/Users/Emir/PycharmProjects/termProject/images/tuna.png")
    animate_text("Blacksmith: By the way... What was your name stranger?")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    keyboard_a()

def go_wise_wizard_main():
    animate_text(
        "When you approach the Wizard's door:\nYou saw strange noises coming from inside \n and you decided to check out.\nInside, there rats were screaming while the Wizard\nwas trying to boil them in the cauldron.")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Greet the wizard ", greet_wizard], ["What did you do ", what_did_you]]
    animate_text_ch("", a)

def greet_wizard():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["How do you know my name?\nWho am I?", who_i_am], ["I want to explore the mountain.", say_go_mountain]]
    animate_text_ch(f"The wizard gathered up and turned to you \n What are you doing around here, {username}?", a)

def what_did_you():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["I don't know who i am ", who_i_am], ["I have to go to the mountain ", say_go_mountain]]
    animate_text_ch("At the finish of the town, there is man named Tuna, \nrats raided his garden, 22 of them were killed,\nbut he could not finish\n he asked for help, I was casting a spell for him?\n So what are you doing around here?", a)

def who_i_am():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["No,I don't know anything", i_dont_know]]
    animate_text_ch("Do you really not know who you are?.\n *Looked Pointedly*", a)

def say_go_mountain():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["So can you help?", can_you_do], ["Why is there a curse?", why_spell]]
    animate_text_ch("Climbing the mountain is not an easy quest,\nEveryone shouldn't attempt in deed.\nThere is a curse at the entrance of the mountain,\n It must be removed and that is no safe.", a)

def why_spell():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["So, can you help?", can_you_do], ]
    animate_text_ch("Legends say that,\nThere were various beings in the mountain and the gate were placed by the\nGod himself to prevent them from coming down \nof the deep bottom mountain", a)

def can_you_do():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["No, I don't... ", i_dont_know], ]
    animate_text_ch("Opening the entrance might lead to a big extinction.\nDo you really not know who you are?\n*He looked pointedly*", a)

def i_dont_know():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Take that potion and give it to the Tuna. ", go_to_tuna], ]
    animate_text_ch("I know who you are. But before I tell you,\nhelp me finish these things.\nTake that potion and give it to the Tuna. \nI told him to accept you to his priority.\nBy the way, Tuna might be a little nervous", a)

def go_to_tuna():
    degistir("C:/Users/Emir/PycharmProjects/termProject/images/houseofwizard.png")
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Get in there", go_there], ]
    animate_text_ch("*You saw a hut over there.*\n*This must be the hut that the Wizard told.*", a)

def go_there():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["The magician sent me and asked me to give this potion to you.", give_potion], ["Calm down!why are you so nervous? ", calm_down]]
    animate_text_ch("As you approach, you saw a \nNervous-looking man, he must be Tuna.\nWhen he got close,\nHe yelled: What! Are you doing here?!\n*Angrily*", a)

def give_potion():
    animate_text("")  # healt -5
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Eat fruits ", eat_fruit], ["Don't eat fruits ", dont_eat_fruit]]
    animate_text_ch("'Give my thanks to the wizard,' he said. \n and offered you the fruits of his garden.", a)

def eat_fruit():
    animate_text("")  # healt -5
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Get inside the Wizard house.", go_inside]]
    animate_text_ch("After giving the elixir to the tuna, you set off to return to the wizard.\n After making some way, you fainted. \nApparently the Tuna gave you poisonous fruit \nAfter a while, you woke up exhausted and \nstarted making your way back to the wizard.", a)

def dont_eat_fruit():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Get inside the Wizard house", go_inside]]
    animate_text_ch("You doubted his manners and did not eat,\nthe fruits he gave to you. Then you went back to the Wizard.", a)

def calm_down():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Eat fruits.", eat_fruit], ["Don't eat fruits.", dont_eat_fruit]]
    animate_text_ch("Rats destroyed my good o' garden.\nNervous Tuna: 'Give my thanks to the wizard.'\n *Offers you the fruits of his garden.*", a)

def go_inside():
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Try to open your eyes", open_eyes]]
    animate_text_ch(f"Welcome again my lord... I- I mean my friend. \nSo you want me to enlight you huh?\n*Telekinesis the stone from your pocket*\n *Pushes it on your head..*\n{username}: UGH!!! H-Hurt... What is th.. Wher... Wh...\n*You fell down, passed out*", a)

def open_eyes():
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["See your fate", fate_choices]]
    animate_text_ch("You will understand everything.", a)

def our_weapon():
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Did I made this?", see_your_past]]
    animate_text_ch("A godly, majestic weapon has been crafted on your hands\n*You feel a lot pain*\n*You feel unbelievabely powerful*", a)

def see_your_past():
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["What am I supposed to do? \nI remember nothing", ask_wizard],["Give me my powers back!", want_powers]]
    animate_text_ch("Good O' Wizard: I suppose my lord *Hmmm interested noices* \n*Wizard told you that you are the most celestial being* \n*in this existence. And that you wanted to see what*\n*is it like to be a creature.*\n Ugly Ol' Wizard: Past, Present and Future is in your hands.", a)

def ask_wizard():
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Where should I start?", where_should_i_start],["Propose to getting to the mountain", lets_go_mount]]
    animate_text_ch("I suppose we will see this in the\nadventure of your destiny...\nIn deed, you made it, so... Ugh..", a)

def where_should_i_start():
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Propose to go together", lets_go_mount],["Salute the wizard and \n get to the road of mountain.", get_to_mountain]]
    animate_text_ch("Mountain stands there, lonely...", a)

def lets_go_mount():
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Show your respect and leave.\n Get to the mountain.", get_to_mountain]]
    animate_text_ch("My lord... I am nearly 4512 years ol'.\nI wouldn't make it... But\nthe mountain will show you the road.", a)

def want_powers():
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Get on the way of mountain.", get_to_mountain], ["Propose to go together.", lets_go_mount]]
    animate_text_ch("I am afraid I am just supposed to show\nyou the road and company with you on your destiny.\nBut I am sure, you will find out the way.", a)

def get_to_mountain():
    degistir("C:/Users/Emir/PycharmProjects/termProject/images/hills.png")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Enter dungeon",go_inside_dungeon], ["Go to the mystic forest", go_forest]]
    animate_text_ch("", a)

def start_game():
    play_usual_music()
    degistir("C:/Users/Emir/PycharmProjects/termProject/images/startgame.png")
    start_button.pack_forget()
    options_button.pack_forget()
    quit_button.pack_forget()
    title_label.pack_forget()
    props1.pack_forget()
    player_data = ('Player_1', 50, 5, 5, 5, 5, 0, 10, 10, 10, 10)
    re_insert_player(player_data)


    animate_text("Future...")
    time.sleep(1)
    animate_text("God...")
    time.sleep(1)
    a = [["Trip around", walk_around], ["Check the mystic stone on your hand", check_stone], ["Touch your injury", body_check]]
    animate_text_ch("What happened to me?.. I- I... I remember nothing... How?.. \n What is this shining thing?.. Wha--it is that blood?!", a)

#KÖYE GİT, KÖYLÜ QUESTLERİ, GRUBA KATILAN OYUNCU..
#SON BOSS KENDİMİZ OLUCAZ
#KÖYDEN BİRİNİN EPIC BİRİ OLMASI- GALADRIEL

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
        a = [["Go to the wizard", go_wise_wizard_main]]
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
    props1 = Listbox(window, bg='white', font=('Garamond', 15), cursor='dot', height=5, width=18)
    props1.insert(1, f"Strength: {player.select_prop('strength')[0]}")
    props1.insert(2, f"Stamina: {player.select_prop('stamina')[0]}")
    props1.insert(3, f"Intelligence: {player.select_prop('intelligence')[0]}")
    props1.insert(4, f"Celestial: {player.select_prop('celestial')[0]}")
    props1.insert(5, f"Health Points: {player.select_prop('hp')[0]}")
    props1.pack_configure(side="bottom", pady=30)

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
        our_weapon()

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

class BossFight:

    def __init__(self):
        self.window = Tk()
        self.window.title("Boss Fight")
        self.window.geometry("400x300")
        play_boss_music()
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
        return select_weapon()

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
            button.pack(side="left", padx=10)

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
                updateButtons()


                self.result_label.config(
                    text=f"Boss dealt {boss_attack} damage. Boss HP: {self.boss_hp}. Your HP: {self.player_hp}.")

                if self.boss_hp <= 0:
                    play_usual_music()
                    self.result_label.config(text="Congratulations! You defeated the boss!")
                    for widget in self.window.winfo_children():
                        if isinstance(widget, Button):
                            widget.config(state="disabled")
                            widget.pack_forget()
                    self.window.destroy()
                    for i in buttonss:
                        i.pack_forget()
                    updateButtons()
                    time.sleep(1)
                    a = [["Keep moving!", after_goblin]]
                    animate_text_ch("You are getting close...", a)

                elif self.player_hp <= 0:
                    self.result_label.config(text="Oh no! You were defeated by the boss.")
                    for widget in self.window.winfo_children():
                        if isinstance(widget, Button):
                            widget.config(state="disabled")
                            widget.pack_forget()
                    self.window.destroy()
                    updateButtons()
                    for i in buttonss:
                        i.pack_forget()
                    time.sleep(1)
                    a = [["Fight Back!", go_back]]
                    animate_text_ch("You have to focus!, Go back!", a)
                else:
                    self.choice = None
                    updateButtons()
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
                updateButtons()

        else:
            self.result_label.config(text="Please select a move.")
        self.window.mainloop()

class BossFight2:

    def __init__(self):
        self.window = Tk()
        self.window.title("Boss Fight")
        self.window.geometry("400x300")
        self.background_label = Label(window, image=background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        play_boss_music()
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
        return select_weapon()

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
            button.pack(side="left", padx=10)

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
                updateButtons()

                self.result_label.config(
                    text=f"Boss dealt {boss_attack} damage. Boss HP: {self.boss_hp}. Your HP: {self.player_hp}.")

                if self.boss_hp <= 0:
                    play_usual_music()
                    self.result_label.config(text="Congratulations! You defeated the boss!")
                    self.window.destroy()
                    for i in buttonss:
                        i.pack_forget()
                    updateButtons()
                    time.sleep(1)
                    a = [["HYDRA HAS BEEN DEFEATED!", after_hydra]]
                    animate_text_ch("You are getting close...", a)

                elif self.player_hp <= 0:
                    self.result_label.config(text="Oh no! You were defeated by the boss.")
                    for widget in self.window.winfo_children():
                        if isinstance(widget, Button):
                            widget.config(state="disabled")
                            widget.pack_forget()
                    self.window.destroy()
                    updateButtons()
                    for i in buttonss:
                        i.pack_forget()
                    time.sleep(1)
                    a = [["Fight Back To Hydra!", go_back2]]
                    animate_text_ch("You have to focus!, Go back!", a)
                else:
                    self.choice = None
                    updateButtons()
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
                updateButtons()

        else:
            self.result_label.config(text="Please select a move.")
        self.window.mainloop()

def go_back():
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Fight BACK!", BossFight]]
    animate_text_ch("", a)

def go_back2():
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Do not knuckle under \n against HYDRA!!!", BossFight2]]
    animate_text_ch("", a)

def go_inside_dungeon():
    degistir("C:/Users/Emir/PycharmProjects/termProject/images/moredungeon.png")
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Move on.", move_on],["Turn back and run\nthrough the forest.", go_forest]]
    animate_text_ch("You have entered to the dungeon.\n*WHAT A BIG GLOOMY DUNGEON!*", a)

def move_on():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Clean webs with the\nBright stone in your pocket", burn_it],["Clean webs by throwing your hand around", throw_hand]]#burn>+intellegience\throw hand >+power
    animate_text_ch("You started to trip inside the dungeon.\nThe walls were full of cobwebs.", a)

def burn_it():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Keep going.", keep_going]]
    animate_text_ch("You continued on your way by burning it.\n Up ahead, you heard a disgusting sound.", a)

def throw_hand():
    animate_text("")#hp-2,stamina-2
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Keep going.", keep_going]]
    animate_text_ch("While you were cleaning with your hand, one of the spiders \nbit you and it hurt a little. Up ahead, you heard a disgusting sound.", a)

def keep_going():
    degistir("C:/Users/Emir/PycharmProjects/termProject/images/goblin.png")
    animate_text("")  # hp-2,stamina-2
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["I know a treasure place inside the dungeon if \nYou don't bother me I will tell you", purpose_gold ],["I will give all of my food\nIf you don't touch me.", purpose_food ]]#gold need intelegience
    animate_text_ch("You went ahead and saw a large door, \nand when you opened the door, it lead to a large hall. \nYou saw a goblin inside and he hovered over you and said,\n*Squeeky Noises*\n'Give me a reason to not make you my dinner.'", a)

def purpose_gold():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["You saw a staircase on the opposite side of the hall.\n The beam of light reappeared and you followed the ladder up.\n When you put on the light, you saw a door that opened into \nthe Forest and I entered the Forest. ", keep_going_way]]
    animate_text_ch("The word 'gold' has fascinated him and \nHe started running towards the place you said.", a)

def purpose_food():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Fight with the GOBLIN!!", BossFight]]#fight here
    animate_text_ch("He attacked you\nGoblin: You willss bess myss foods!!", a)

def after_goblin():
    degistir("C:/Users/Emir/PycharmProjects/termProject/images/hills.png")
    animate_text("You saw a staircase on the opposite side of the hall.\n The beam of light reappeared and you followed the ladder up.\n When you put on the light, you saw a door that opened into \nthe Forest and I entered the Forest.")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Keep going",keep_going_way]]
    animate_text_ch("", a)

def go_forest():
    animate_text("You started walking down the path on the hills of the mountain.\n You saw that the road was cut off ahead that is getting to the other side.")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Try to jump ", try_jump],["Try to pass by using the woods around ", try_woods]]#wood>+intellegience\jump >+power
    animate_text_ch("", a)

def try_jump():
    animate_text("You jumped across, but you hurt your foot.\nYou moved on and heard an animal sound.\n*Nervous*")#hp-2,stamina-2
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Go after voices.", keep_going_forest]]
    animate_text_ch("", a)

def try_woods():
    animate_text("")#stamina-3
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Go after the voices.", keep_going_forest]]
    animate_text_ch("Cleverly, you crossed the other side by using woods.\nYou moved on and heard an animal sound.\n*It might be a deer?..*", a)

def keep_going_forest():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Get on your way.", keep_going_way], ["Talk to deer:\nI mean no harm ,I'm friendly", go_deer]]
    animate_text_ch("As you kept moving you realized it was\n a Millenia (half human-half deer) looking at you frightened.", a)

def go_deer():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Move on your way.", keep_going_way]]
    animate_text_ch("Millennia approached and gave you a health potion\n made from Pine resin to reward you for your friendly approach.", a)

def keep_going_way():
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Get in the forest", go_in_forest]]
    animate_text_ch("As you made your way into the forest, \nYou began to hear voices from the unknown.\nSaid '\n*TSSSSSSSSS*\n Come *TSSSSS* \nCome to victory'", a)

def go_in_forest():
    degistir("C:/Users/Emir/PycharmProjects/termProject/images/hydra.png")
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Attack to the HYDRA!!", BossFight2]]
    animate_text_ch("You went into the forest and suddenly you saw a\n!!?HYDRA!! in front of you.\n *TSSSSSS* He turned to you and said VICTORY SHALL MIIINE!'", a)

def after_hydra():
    degistir("C:/Users/Emir/PycharmProjects/termProject/images/hills.png")
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["How did I get here?", get_here],["Who are you?", who_you]]
    animate_text_ch("You woke up in a small hut saw.\n An angel waiting you to wake up. \n Ask: ", a)

def get_here():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["What happened to your wing?", who_you], ["What are you doing on this cursed mountain?", who_you]]
    animate_text_ch("I saw you lying next to the corpse of the invincible Hydra.\nI knew who you were at the second I saw you\nand I will do my best for you to reach your goal.", a)

def who_you():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["I can heal your wing.", heal_angel], ["Ask her to carry you to the top.", go_mountain_forest]]
    animate_text_ch("I was sent here on a mission. \nI fought with a Hydra in the jungle and it broke my wings \nDesperately and crucially.", a)

def heal_angel():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["Can you carry me to\nthe top of the mountain?", go_mountain_angel]]
    animate_text_ch("''Anor gwaith miruvaen, i'n lín nîn a' egor amon,\nlû bo naeth dôr a gwendeth golothram, tîr beraid i tharad \ndínen a amdir vi ben'\n *Angel starts to move her wing.*''\n\nAngel: Thank you my Lord.", a)

def go_mountain_forest():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["You reached the top and saw the Mighty ZEUS!", go_mountain_fight]]
    animate_text_ch("She said her wing was broken so she couldn't help.\n You came out of the hut and looked at the top of the mountain\n*SIGHS*\n *There isn't much left*.\nYou went through the hard roads on \nthe way to the top of the mountain.", a)

def go_mountain_angel():
    animate_text("")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    a = [["You reached the top and saw the Mighty ZEUS!", go_mountain_fight]]
    animate_text_ch("The angel took you up to the top of the mountain. \nShe said that she couldn't help you anymore\n*Saluted you and flew away.*", a)

class go_mountain_fight:

    def __init__(self):
        degistir("zeus.png")
        play_boss_music()
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
        self.boss_hp = 100


    def select_weapon(self):
        return select_weapon()

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
            button.pack(side="left", padx=10)

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
                updateButtons()

                self.result_label.config(
                    text=f"Boss dealt {boss_attack} damage. Boss HP: {self.boss_hp}. Your HP: {self.player_hp}.")

                if self.boss_hp <= 0:
                    play_usual_music()
                    self.result_label.config(text="???!")
                    for widget in self.window.winfo_children():
                        if isinstance(widget, Button):
                            widget.config(state="disabled")
                            widget.pack_forget()
                    self.window.destroy()
                    for i in buttonss:
                        i.pack_forget()
                    updateButtons()
                    time.sleep(1)
                    a = [["Everything has an end!", the_end]]
                    animate_text_ch("What is... Wh...", a)

                elif self.player_hp <= 0:
                    self.result_label.config(text="Oh no! You were defeated by the boss.")
                    for widget in self.window.winfo_children():
                        if isinstance(widget, Button):
                            widget.config(state="disabled")
                            widget.pack_forget()
                    self.window.destroy()
                    updateButtons()
                    for i in buttonss:
                        i.pack_forget()
                    time.sleep(1)
                    a = [["What happened?!. Everything..", the_end]]
                    animate_text_ch("What... Wh... W...", a)
                else:
                    self.choice = None
                    updateButtons()
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
                updateButtons()

        else:
            self.result_label.config(text="Please select a move.")
        self.window.mainloop()

def the_end():
    animate_text("Now what? You defeated the Zeus.\nBut what was the purpose?\n You were the Zeus himself that lost\n And fell apart.\n You have found yourself.\n Now you know what is it to be desperate.\n ...\n ...\nTHE END.\n eae")
    for i in buttonss:
        i.pack_forget()
    time.sleep(1)
    quit_button.pack()

if __name__ == "__main__":
    stop_music()
    background_image = PhotoImage(file="C:/Users/Emir/PycharmProjects/termProject/images/background.png")
    background_label = Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    props1 = Listbox(window, bg='white', font=('Garamond', 15), cursor='dot', height=5, width=18)
    props1.pack(side="bottom", pady=30)
    props1.insert(1, f"Strength: {player.select_prop('strength')[0]}")
    props1.insert(2, f"Stamina: {player.select_prop('stamina')[0]}")
    props1.insert(3, f"Intelligence: {player.select_prop('intelligence')[0]}")
    props1.insert(4, f"Celestial: {player.select_prop('celestial')[0]}")
    props1.insert(5, f"Health Points: {player.select_prop('hp')[0]}")
    props1.pack_configure(side="bottom", pady=30)

    icon_image = PhotoImage(file="C:/Users/Emir/PycharmProjects/termProject/images/icon.png")
    window.iconphoto(True, icon_image)

    title_label = Label(window, text="Road of Fate",  font=("Garamond", 32))
    title_label.pack(pady=50)

    label = Label(window, text="", font=("Garamond", 24))
    start_button = Button(window, text="Start", command=start_game)
    options_button = Button(window, text="Options", command=options)
    quit_button = Button(window, text="Quit", command=quit_game)


    menu_frame = Frame(window)
    menu_frame.pack()

    label.pack(pady=20)
    start_button.pack(pady=10)
    options_button.pack(pady=10)
    quit_button.pack(pady=10)

    window.mainloop()