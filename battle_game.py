from random import randint
import sys
import time

# Player variables:
PLAYER_HEALTH = 50
NUM_POTIONS = 3

# NPC variables:
NPC_HEALTH = 50

def player_attack(health): # Function that applies damage to the player
    attack = randint(5, 10)
    health = health - attack
    return (health, attack)

def npc_attack(health): # Function that applies damage to the NPC
    attack = randint(5, 15)
    health = health - attack
    return (health, attack)

def take_potion(health, potions): # Function that increases the player's health when taking a potion
    potion = randint(15, 50)
    health = health + potion
    potions -= 1
    return (health, potions, potion)

while True:
    user_choice = input("\nDo you want to attack (1) or take a potion (2)? ")

    if not user_choice.isdigit():
        print("Incorrect input!")
        continue

    user_choice = int(user_choice)
    if not user_choice in [1, 2]:
        print("Incorrect input!")
        continue

    if user_choice == 1:
        (NPC_HEALTH, PLAYER_ATTACK) = player_attack(NPC_HEALTH)
        (PLAYER_HEALTH, NPC_ATTACK) = npc_attack(PLAYER_HEALTH)
        print(f"\nYou inflicted {PLAYER_ATTACK} damage to the enemy!")
        print(f"The enemy inflicted {NPC_ATTACK} damage to you!")
        if PLAYER_HEALTH >= 0 and NPC_HEALTH >= 0:
            print(f"\nYou have {PLAYER_HEALTH} health points left!")
            print(f"The enemy has {NPC_HEALTH} health points left!")

        elif PLAYER_HEALTH <= 0:
            print(f"\nYou have {0} health points left!")
            print(f"The enemy has {NPC_HEALTH} health points left!")
            print("\nYou lost!")
            time.sleep(60)
            sys.exit()

        elif NPC_HEALTH <= 0:
            print(f"\nYou have {PLAYER_HEALTH} health points left!")
            print(f"The enemy has {0} health points left!")
            print("\nYou won!")
            time.sleep(60)
            sys.exit()

    else:
        if NUM_POTIONS == 0:
            print("You have no more potions!")
            continue

        else:
            (PLAYER_HEALTH, NUM_POTIONS, POTION) = take_potion(PLAYER_HEALTH, NUM_POTIONS)
            (PLAYER_HEALTH, NPC_ATTACK) = npc_attack(PLAYER_HEALTH)
            print(f"You recovered {POTION} health points! ({NUM_POTIONS} potions left!)")
            print(f"The enemy inflicted {NPC_ATTACK} damage to you!")
            print(f"\nYou now have {PLAYER_HEALTH} health points!")
            print(f"The enemy has {NPC_HEALTH} health points left!")

    print("\n")
    print("-" * 50)
