import pet_control
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_console()
        print("Welcome to Terminal Tamagotchi\n----------------------")
        input("Click enter to continue...")
        clear_console()

        name_input = input("Name your new pet:\n")
        clear_console()

        print("Pick a pet type!\n1. Cat\n2. Dog\n3. Turtle")
        pet_type_input = input("----------------------\nEnter the type: ")
        clear_console()

        if pet_type_input == "1":
            pet_type = "Cat"
            break
        elif pet_type_input == "2":
            pet_type = "Dog"
            break
        elif pet_type_input == "3":
            pet_type = "Turtle"
            break
        else:
            print("Incorrect Pet type! Please give a number.")
            continue

    player_pet = pet_control.Pet(name_input, pet_type)

    while True:
        status = player_pet.status()

        print(f"Your {player_pet.pet_type}, {player_pet.name}:")
        print(f"Hunger: {status[0]}")
        print(f"Energy: {status[1]}")
        print(f"Happiness: {status[2]}")
        print(f"Age: {status[3]}")

        print("\n----------------------\n")

        action = input("Pick an action\n1. Feed\n2. Rest\n3. Play\n4.Quit\n\n")

        before = player_pet.status()

        if action == "1":
            player_pet.feed()
        elif action == "2":
            player_pet.rest()
        elif action == "3":
            player_pet.play()
        elif action == "4":
            return

        player_pet.hunger = max(0, min(player_pet.hunger, 10))
        player_pet.energy = max(0, min(player_pet.energy, 10))
        player_pet.happiness = max(0, min(player_pet.happiness, 10))

        after = player_pet.status()

        if action == "1":
            print(f"\nPet Fed! (Hunger {before[0]} → {after[0]})")
        elif action == "2":
            print(f"\nPet Rested! (Energy {before[1]} → {after[1]}, Hunger {before[0]} → {after[0]})")
        elif action == "3":
            print(f"\nPet Played! (Happiness {before[2]} → {after[2]}, Energy {before[1]} → {after[1]}, Hunger {before[0]} → {after[0]})")

        time.sleep(4)

        player_pet.tick()

        clear_console()

if __name__ == "__main__":
    main()
