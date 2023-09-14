import sqlite3

# Connect to the database
conn = sqlite3.connect('C:/Users/Emir/PycharmProjects/termProject/game_data.db')

conn.execute('''CREATE TABLE IF NOT EXISTS inventory
                  (player_name TEXT, name TEXT, quantity INTEGER, description TEXT,
                   FOREIGN KEY(name) REFERENCES players(name))''')
# Create a table to store player data
conn.execute('''CREATE TABLE IF NOT EXISTS players
             (name TEXT NOT NULL,
             hp INTEGER NOT NULL,
             stamina INTEGER NOT NULL,
             strength INTEGER NOT NULL,
             intelligence INTEGER NOT NULL,
             celestial INTEGER NOT NULL,
             level INTEGER NOT NULL,
             risk INTEGER NOT NULL,
             exc INTEGER NOT NULL,
             friendly INTEGER NOT NULL,
             peaceful INTEGER NOT NULL);''')

conn.commit()
conn.close()
#Health, Stamina, Strength, Sight, Intelligence, Mystic...
#Risk, Excitement, Friendly, Peaceful

class Player:
    def __init__(self, name, hp=50, stamina=5, strength=5, intelligence=5, celestial=5, level=0, risk=10, exc=10, friendly=10, peaceful=10):
        self.name = name
        self.hp = hp
        self.level = level
        self.stamina = stamina
        self.strength = strength
        self.intelligence = intelligence
        self.celestial = celestial
        self.risk = risk
        self.exc = exc
        self.friendly = friendly
        self.peaceful = peaceful

    #Update the user in the database
    def update_prop(self, new_prop, value):
        conn = sqlite3.connect('C:/Users/Emir/PycharmProjects/termProject/game_data.db')
        conn.execute(f"UPDATE players SET {new_prop} = ? WHERE name = ?", (int(value) , self.name))
        conn.commit()
        conn.close()

    #Fetch the wanted property and its value
    def select_prop(self, new_prop):
        conn = sqlite3.connect('C:/Users/Emir/PycharmProjects/termProject/game_data.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT {new_prop} from players WHERE name = ?", (self.name,))
        prop = cursor.fetchone()
        conn.commit()
        conn.close()
        return prop

    #Just incase deleting
    def delete(self):
        conn = sqlite3.connect('C:/Users/Emir/PycharmProjects/termProject/game_data.db')
        conn.execute("DELETE from players WHERE name = ?", (self.name,))
        conn.commit()
        conn.close()

class InventoryItem:
    def __init__(self, player_name, name, quantity, description):
        self.player_name = player_name
        self.name = name
        self.quantity = quantity
        self.description = description

#Function to fetch a player's data

#Fetching item with player
def fetch_player_data(name):
    cursor.execute("SELECT name FROM players WHERE name = ?", (name,))
    player_name = cursor.fetchone()

    if player_name:
        cursor.execute("SELECT name, quantity, description FROM inventory WHERE name = ?", (name,))
        inventory_data = cursor.fetchall()

        inventory_items = []
        for item in inventory_data:
            name, quantity, description = item
            inventory_items.append(InventoryItem(name, quantity, description))

        return Player(player_name[0])
    else:
        return None

conn = sqlite3.connect('C:/Users/Emir/PycharmProjects/termProject/game_data.db')
cursor = conn.cursor()

# Define the player data
player_data = ('Player_1', 50, 5, 5, 5, 5, 0, 10, 10, 10, 10)

# Check if the player already exists
cursor.execute("SELECT 1 FROM players WHERE name = ?", (player_data[0],))
existing_player = cursor.fetchone()
name = "Player_1"
player = fetch_player_data(name)

if not existing_player:
    cursor.execute("INSERT OR IGNORE INTO players (name, hp, stamina, strength, intelligence, celestial, level, risk, exc, friendly, peaceful) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",player_data)
    conn.commit()
    conn.close()
    print("Player inserted successfully")
else:
    conn.close()
    print("Player already exists")


# Insert the player if they do not exist
def re_insert_player(data):
    conn = sqlite3.connect('C:/Users/Emir/PycharmProjects/termProject/game_data.db')
    cursor = conn.cursor()
    player.delete()
    cursor.execute("INSERT OR IGNORE INTO players (name, hp, stamina, strength, intelligence, celestial, level, risk, exc, friendly, peaceful) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    conn.commit()
    conn.close()
    print("Player inserted successfully")



def select_weapon():
    conn = sqlite3.connect('C:/Users/Emir/PycharmProjects/termProject/game_data.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT name from inventory WHERE quantity = ?", (100,))
    prop = cursor.fetchone()
    conn.commit()
    conn.close()
    return prop[0]

# Sample inventory item
item1 = InventoryItem('Player_1', 'Sword', 1, 'A powerful weapon')

def InsertItem(item):
    conn = sqlite3.connect('C:/Users/Emir/PycharmProjects/termProject/game_data.db')

    cursor = conn.cursor()
    # Check if the items are already owned
    cursor.execute("SELECT 1 FROM inventory WHERE player_name = ? AND name = ?", (item.player_name, item.name))
    existing_item1 = cursor.fetchone()

    # Insert the items if they are not already owned
    if not existing_item1:
        cursor.execute("INSERT OR IGNORE INTO inventory (player_name, name, quantity, description) VALUES (?, ?, ?, ?)", (item.player_name, item.name, item.quantity, item.description))
        conn.commit()
        print(f"{item.name} inserted successfully")
        return True
    else:
        print(f"{item.name} already owned")
        return False
    conn.close()











