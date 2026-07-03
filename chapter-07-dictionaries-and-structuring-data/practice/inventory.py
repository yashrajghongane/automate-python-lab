# The Scenario
# You are building the inventory system for a text-based video game.
# Players can have bags of items.
# Shops sell items.
# You need to process text commands to clean up data.

# 1. Dictionary containing lists (Item categories)
shop_items = {
    "weapons": ["sword", "bow"],
    "potions": ["health_potion", "mana_potion"],
    "misc": ["rope", "torch"]
}

# 2. Nested Dictionary (Player Stats and Inventory)
players = {
    "player_1": {
        "name": "Alice",
        "gold": 150.756,
        "bag": ["sword", "health_potion"]
    },
    "player_2": {
        "name": "Bob",
        "gold": 45.20,
        "bag": ["rope"]
    }
}

print("=== STARTING THE GAME TRACKER ===")

# --- TASK 1: String Splitting & Manual Cleaning ---
# A player typed a message. Let's clean the punctuation manually.
raw_chat = "I want a sword, bow and a rope"

print("\n--- Task 1: Cleaned Chat Words ---")
# TODO: Use .split() on raw_chat to turn it into a list of words.
# Loop through that list and print each word.
for word in raw_chat.split():
    word = word.strip(',.!?')
    print(word)


# --- TASK 2: Add Player 3 All-At-Once ---
print("\n--- Task 2: Adding Player 3 ---")
# TODO: Add "player_3" to the 'players' dictionary. 
# Give them a name: "Charlie", gold: 100.00, and an empty bag: []
players["player_3"] = {"name": "Charlie", "gold": 100.00, "bag": []}


# --- TASK 3: Using setdefault() ---
print("\n--- Task 3: Setting a Default Guild ---")
# TODO: Use the .setdefault() method on player_1's dictionary to add 
# a "guild" key with the value "DragonSlayers". 
# (Since player_1 doesn't have a guild, it will add it!)
# Print player_1's dictionary to confirm it worked.
players["player_1"].setdefault("guild","DragonSlayers")
print(players["player_1"])


# --- TASK 4: Nested Loops & Formatting ---
print("\n--- Task 4: Player Leaderboard ---")
# TODO: Loop through 'players' using .items()
# Print each player's name and their gold formatted to 2 decimal places (:.2f)
# Inside that loop, write a smaller loop to print every item inside their 'bag' list.

for player,stat in players.items():
    print(f"{stat['name']} has {stat['gold']:.2f} gold. ")
    print(f"This are the items inside the players bag: ")
    for item in stat["bag"]:
        print(end=" ")
        print(item)
    print()