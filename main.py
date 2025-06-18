import pet_control
import os
import time
import json_control as json_control

def stat_bar(value):
    return "█" * value + "-" * (10 - value)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        while True:
            clear_console()
            print("🌟 Welcome to Terminal Tamagotchi! 🌟")
            print("------------------------------------")
            print("📁 What would you like to do?\n")
            print("  [1] 🐣 New Pet")
            print("  [2] 💾 Load Pet")
            print("  [3] 🗑️ Delete Pet\n")

            action = input("🔢 Enter the number of your choice:\n\n> ")

            if action == '1':
                clear_console()

                print("🐾 Let's adopt a pet!")
                name_input = input("📝 What will you name your new companion?\n\n> ")
                clear_console()

                print("🐾 Choose your pet type:\n")
                print("  [1] 🐱 Cat")
                print("  [2] 🐶 Dog")
                print("  [3] 🐢 Turtle\n")

                pet_type_input = input("🔢 Enter the number of your choice:\n\n> ")
                clear_console()

                if pet_type_input == "1":
                    pet_type = "Cat"
                    player_pet = pet_control.Pet(name_input, pet_type)
                    break
                elif pet_type_input == "2":
                    pet_type = "Dog"
                    player_pet = pet_control.Pet(name_input, pet_type)
                    break
                elif pet_type_input == "3":
                    pet_type = "Turtle"
                    player_pet = pet_control.Pet(name_input, pet_type)
                    break
                else:
                    print("❗ Invalid choice! Please enter 1, 2, or 3.")
                    time.sleep(1.5)
                    continue

            elif action == '2':
                clear_console()

                input_name = input("🐾 Enter the name of your pet:\n\n> ")
                clear_console()
                input_type = input("🐶 Enter your pet's type (e.g., Cat, Dog):\n\n> ")
                clear_console()

                pet_data = json_control.load_json(input_type, input_name)

                if pet_data is None:
                    input("\n🔙 Press Enter to return to the menu...")
                    continue

                player_pet = pet_control.Pet.from_dict(pet_data)

                if player_pet.alive == False:
                    print("It's dead stupid.")
                    input("\n🔙 Press Enter to return to the menu...")

                    file_path = f"{input_type}-{input_name}.json"
                
                    if os.path.exists(file_path):
                        os.remove(file_path)
                    
                    continue
                break

            elif action == '3':
                input_name = input("🐾 Enter the name of the pet:\n\n> ")
                clear_console()
                input_type = input("🐶 Enter the pet's type (e.g., Cat, Dog):\n\n> ")

                input_name = input_name.upper()
                input_type = input_type.upper()

                file_path = f"{input_type}-{input_name}.json"
                
                if os.path.exists(file_path):
                    os.remove(file_path)

                continue

           

        while True:
            status = player_pet.status()

            emoji = "🐱" if player_pet.pet_type == "Cat" else "🐶" if player_pet.pet_type == "Dog" else "🐢"
            print(f"{emoji} Your {player_pet.pet_type}, {player_pet.name}:\n")
            print(f"🍽️  Hunger:    {stat_bar(status[0])} ({status[0]})\n")
            print(f"💤  Energy:    {stat_bar(status[1])} ({status[1]})\n")
            print(f"🎉  Happiness: {stat_bar(status[2])} ({status[2]})\n")

            print("────────────────────────────────────")

            print("📋 What would you like to do?\n")
            print("  [1] 🍽️  Feed")
            print("  [2] 💤  Rest")
            print("  [3] 🎾  Play")
            print("  [4] ❌  Quit")
            print("────────────────────────────────────")

            action = input("🔢 Enter the number of your choice:\n\n> ")

            before = player_pet.status()

            if action == "1":
                player_pet.feed()
            elif action == "2":
                player_pet.rest()
            elif action == "3":
                player_pet.play()
            elif action == "4":
                json_control.upload_to_json(player_pet, player_pet.name, player_pet.pet_type)
                return

            player_pet.hunger = max(0, min(player_pet.hunger, 10))
            player_pet.energy = max(0, min(player_pet.energy, 10))
            player_pet.happiness = max(0, min(player_pet.happiness, 10))

            after = player_pet.status()

            if action == "1":
                print(f"\n✅ Pet Fed! (Hunger {before[0]} → {after[0]})")
            elif action == "2":
                print(f"\n✅ Pet Rested! (Energy {before[1]} → {after[1]}, Hunger {before[0]} → {after[0]})")
            elif action == "3":
                print(f"\n✅ Pet Played! (Happiness {before[2]} → {after[2]}, Energy {before[1]} → {after[1]}, Hunger {before[0]} → {after[0]})")

            time.sleep(0.5)

            player_pet.tick()

            if player_pet.hunger >= 10 or player_pet.energy <= 0:
                player_pet.alive = False
                clear_console()
                print("💀 What! You monster. You really let your digital pet die. Scum of the earth.")
                input("\nPress Enter to continue...")
                json_control.upload_to_json(player_pet, player_pet.name, player_pet.pet_type)
                break

            if player_pet.happiness <= 0:
                player_pet.alive = False
                clear_console()
                print("🏃‍♂️ What! You animal abuser. Your pet was so unhappy it ran away!")
                input("\nPress Enter to continue...")
                json_control.upload_to_json(player_pet, player_pet.name, player_pet.pet_type)
                break

            if player_pet.age >= 20:
                death_chance = random.randrange(0, 6)
                if death_chance == 5 or 6:
                    clear_console()
                    print(f"💀 Your {player_pet.pet_type}, {player_pet.name} died of old age!")
                    input("\nPress Enter to continue...")
                    json_control.upload_to_json(player_pet, player_pet.name, player_pet.pet_type)
                    break

                if death_chance == 5 or 6:
                    player_pet.alive = False
                    clear_console()
                    print(f"💀 No! Your {player_pet.pet_type}, {player_pet.name} just")
                    input("\nPress Enter to continue...")
                else:
                    pass
                    

            clear_console()

            if player_pet.age >= 4:
                import random
                random_action = random.randrange(0, 10)

                if random_action in [1, 2, 3, 4]:
                    pass
                if random_action in [5, 6]:

                    before = player_pet.status()

                    print(f"{player_pet.name} found a toy!")
                    player_pet.happiness += 2

                    player_pet.happiness = max(0, min(player_pet.happiness, 10))

                    after = player_pet.status()

                    print(f"\n✅ Pet Rested! (Energy {before[1]} → {after[1]}, Hunger {before[0]} → {after[0]})")


                if random_action == 7:
                    print(f"{player_pet.name} had a hard time sleeping!")

            

if __name__ == "__main__":
    main()
