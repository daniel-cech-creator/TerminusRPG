#Made by Daniel Čech

import random, os, sys, time

class player:
    def __init__(self,hp,maxHp,coins,dmgMult,mana,maxMana,inventory,invSize):
        self.hp = hp
        self.maxHp = maxHp
        self.coins = coins
        self.dmgMult = dmgMult
        self.mana = mana
        self.maxMana = maxMana
        self.inventory = inventory
        self.invSize = invSize

class weapon:
    def __init__(self,name,dmg,cost,info,tag):
        self.name = azure(name)
        self.dmg = dmg
        self.cost = yellow(cost)
        self.info = blue(info)
        self.tag = tag

class consumable:
    def __init__(self,name,effect,cost,info,trigger,tag):
        self.name = azure(name)
        self.effect = green(effect)
        self.cost = yellow(cost)
        self.info = red(info)
        self.trigger = trigger
        self.tag = tag

class enemy:
    def __init__(self,name,hp,maxHp,dmg,loot):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.dmg = dmg
        self.loot = loot

    def __str__(self):
        return self.name

#=== /// TEXT COLOR /// ===#
def black(a):
    return (f"\033[30m{a}\033[0m")
def red(a):
    return (f"\033[31m{a}\033[0m")
def green(a):
    return (f"\033[32m{a}\033[0m")
def yellow(a):
    return (f"\033[33m{a}\033[0m")
def blue(a):
    return (f"\033[34m{a}\033[0m")
def purple(a):
    return (f"\033[35m{a}\033[0m")
def azure(a):
    return (f"\033[36m{a}\033[0m")
def white(a):
    return (f"\033[37m{a}\033[0m")

#=== /// TEXT BACKGROUND COLOR /// ===#
def blackbg(a):
    return (f"\033[40m{a}\033[0m")
def redbg(a):
    return (f"\033[41m{a}\033[0m")
def greenbg(a):
    return (f"\033[42m{a}\033[0m")
def yellowbg(a):
    return (f"\033[43m{a}\033[0m")
def bluebg(a):
    return (f"\033[44m{a}\033[0m")
def purplebg(a):
    return (f"\033[45m{a}\033[0m")
def azurebg(a):
    return (f"\033[46m{a}\033[0m")
def whitebg(a):
    return (f"\033[47m{a}\033[0m")

#Heals the player for the set value.
def playerHeal(n):
    player.hp += n

#Increases the players AP by the set value.
def manaUp(n):
    player.mana += n

#Increases the players inv size by the set value.
def invUp(n):
    player.invSize += n
    for _ in range(n):
        player.inventory.append("Empty")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Draws out inventory slots
def inventoryOpen():
    print(white("\n#*=== /// INVENTORY \\\\\ ===*#"))
    for i in range(player.invSize):
        item = player.inventory[i]
        if item == "Empty":
            print(f"Slot {i+1}:", white("Empty"))
        else:
            print(f"Slot {i+1}:", item.name)

#Make sures the stats don't surpass their maximum value
def maxStatCheck():
    if player.hp > player.maxHp:
        player.hp = player.maxHp
    if player.mana > player.maxMana:
        player.mana = player.maxMana

#draws a loading bar based lasting n seconds
def wait(n):
    anim = ["[-----]","[#----]","[##---]","[###--]","[####-]","[#####]",]
    for _ in range(1):
        for frame in anim:
            sys.stdout.write(f"\r{frame}")
            sys.stdout.flush()
            time.sleep(n/6)
    sys.stdout.write(f"   ")
    sys.stdout.flush()
    clear_terminal()

#=== /// WEAPONS \\\ ===#
#Name, DMG, Cost, Info
rusty_sword = weapon("Rusty Sword",14,50,"Old, rusty sword, Better than nothing.","weapon")
giant_hammer = weapon("Giant Hammer",31,89,"Giant sledgehammer weighing atleast for washing machines.","weapon")
old_pickaxe = weapon("Old Pickaxe",20,30,"An old pickaxe used by slaves in the Educanet corp.","weapon")
greatsword = weapon("Greatsword",28,68,"And old sword once used by the order of Dušek.","weapon")
empty_gun = weapon("Empty Gun",10,95,"An old gun once used by the nefarious Wisman gang.","weapon")
new_magic_wand = weapon("New Magic Wand",21,43,"I saw a photo you looked joyous...","weapon")
long_bow = weapon("Long Bow",20,54,"A wooden long bow handcrafted by unpaid Temu workers.","weapon")
#fencing_sword
#greed_dagger - gives coins after every hit
#vampire_blade - heals after every hit
#iron_fists
#battle_axe
#fish
#crystal_saber
#hell_fork
#shadow_edge - 2x dmg in Atrium
#star_splitter


#=== /// CONSUMABLES \\\ ===#
#Name, Effect, Cost, Info, Trigger (the assigned function)
lesser_heal_pot = consumable("Lesser Healing Potion","Heals the player for +20 HP.",35,"Consists mostly of Red40.",lambda: playerHeal(20),"consum")
great_heal_pot = consumable("Great Healing Potion","Heals the player for +42 HP",50,"Tastes like skittles and oil... and Red40.", lambda: playerHeal(42),"consum")
lesser_mana_pot = consumable("Lesser Mana Potion","Gives the player +2 Mana",42,"Smells like mouthwash.", lambda: manaUp(2),"consum")
great_mana_pot = consumable("Great Mana Potion","Gives the player +5 Mana",73,"Tastes like toothpaste with orange juice.", lambda: manaUp(5),"consum")
#lesser_crit_pot
#great_crit_pot
#lesser_regen_pot
#great_regen_pot
small_pocket = consumable("Small Pocket","Adds +1 inventory slot",84,"The knitting is pretty sloppy", lambda: invUp(1),"consum")
big_pocket = consumable("Big Pocket","Adds +2 inventory slot",84,"You could fit a chair in that", lambda: invUp(2),"consum")


#=== /// ENEMIES \\\ ===#
#Name, HP, MaxHP, DMG, Loot

#Basic enemies
goblin = enemy("Goblin",45,45,6,21)
skeleton = enemy("Skeleton",25,25,7,11)
brute = enemy("Brute",68,68,9,20)
wisman_gang_member = enemy("Wisman Gang Member", 40,40,9,30)
dusek_cultist = enemy("Order of Dušek Cultist",64,64,10,24)
gurt = enemy("Gurt",30,30,4,6)


#Mini-Bosses
matyas_janousek = enemy("Matyáš Janoušek",100,100,18,121)
moto_moto = enemy("Moto Moto",135,135,8,4)
dusek_acolyte = enemy("Order of Dušek Acolyte",114,114,17,130)

#Bosses
meat_wall = enemy("Meat Wall",187,187,4,217)

#Weapon IDs
weapons = {
    1: rusty_sword,
    2: giant_hammer,
    3: old_pickaxe,
    4: greatsword,
    5: empty_gun,
    6: new_magic_wand,
    7: long_bow
}
#Consumable IDs
consumables = {
    1: lesser_heal_pot,
    2: great_heal_pot,
    3: lesser_mana_pot,
    4: great_mana_pot
}
#Enemy IDs
enemies = {
    1: goblin,
    2: skeleton,
    3: brute,
    4: brute,
    5: dusek_cultist,
    6: gurt,
    7: matyas_janousek,
    8: moto_moto,
    9: dusek_acolyte,
}

floors = {
    1: "Basement",
    2: "Catacombs",
    3: "Labyrinth",
    4: "Atrium",
}

floorLootTable = {
    floors[1] 
}


chestLootTable = {
    empty_gun: 10,
    lesser_heal_pot: 25,
    great_heal_pot: 15,
    lesser_mana_pot: 20,
    great_mana_pot: 5,
    old_pickaxe: 5,
    greatsword: 5,
    new_magic_wand: 5,
    giant_hammer: 5,
    small_pocket: 5
}

clear_terminal()

print("#=== /// TERMINUS RPG \\\\\ ===#")
input("> ")
clear_terminal()
nameSet = False

while nameSet == False:
    clear_terminal()
    print(azure("Who are you..."))
    username = input("> ")

    clear_terminal()
    if username == "":
        username = "Unknown"
    print(azure(f"Are you sure? -"),green(username))
    print("0 = No")
    print("1 = Yes")
    choice = str(input("> "))

    if choice == "1":
        nameSet = True
    elif choice == "0":
        continue
    else:
        print(red("Invalid input!"))
        input()


player.hp = 100
player.maxHp = player.hp
player.coins = 0
player.dmgMult = 1
player.mana = 0
player.maxMana = 5
player.invSize = 5
player.inventory = []
for i in range(player.invSize):
    player.inventory.append("Empty")

equippedWeapon = weapons[1]
equippedConsum = consumables[2]
roomsCleared = 0
currentFloor = floors[1]
clear_terminal()

#=== /// MAIN GAMEPLAY LOOP \\\ ===#
while player.hp > 0:
    print(f"Floor: {currentFloor}\n")
    print(f"HP: {green(player.hp)}/{green(player.maxHp)}")
    print(f"Mana: {blue(player.mana)}/{blue(player.maxMana)}")
    print(f"Rooms cleared:",azure(roomsCleared))
    print(f"Gold:",yellow(player.coins))
    print(f"Equipped weapon: {equippedWeapon.name} - {red(f"{equippedWeapon.dmg} DMG")}")
    print("＿＿＿＿＿＿＿＿＿＿\n")
    print(azure("What will you do?"))
    print("1 = Go to next room | 2 = Inventory")
    choice = str(input("> "))

    if choice == "exit":
        exit()

    #Entering the next room
    if choice == "1":
        clear_terminal()
        wait(1)
        clear_terminal()

        #Chooses the room type
        
        roomType = random.randint(1,3)
        print("You entered the next room.")
        if roomType == 1:
            coinRoom = random.randint(1,5)
            if coinRoom in (1,2,3,4):
                print(azure(f"Just an empty room."))
                roomsCleared += 1
            else:
                print(azure(f"Empty room with a handful of coins on the floor."))
                receivedCoins = random.randint(5,16)
                player.coins += receivedCoins
                print(yellow(f"+{receivedCoins} coins."))
                roomsCleared += 1
            input()
        elif roomType == 2:
            print(red("There's an enemy blocking the way!"))
            input()
            

            #Battle Loop
            opponent = enemies[random.randint(1,2)]
            opponent.hp = opponent.maxHp
            clear_terminal()
        
            while player.hp > 0 and opponent.hp > 0:
                print(f"{username}'s HP: {player.hp}/{player.maxHp}")
                print(f"{opponent.name}'s HP: {opponent.hp}/{opponent.maxHp}\n")

                #Player Turn
                print("#=== /// PLAYER TURN \\\\\ ===#\n")
                print(azure("What will you do?"))
                print("1 = Attack | 2 = Inventory")
                choice = str(input("> "))
                

                if choice == "1":

                    dealtDMG = equippedWeapon.dmg * player.dmgMult
                    opponent.hp -= dealtDMG
                    print(f"\nYou've dealt {red(dealtDMG)} DMG.")
                    

                    #Enemy Turn
                    
                    if opponent.hp > 0:
                        print("\n#=== /// ENEMY TURN \\\\\ ===#\n")
                        player.hp -= opponent.dmg
                        print(f"The enemy dealt {opponent.dmg} DMG.")
                        
                    else:
                        print("The enemy died before it could attack back.")
                else:
                    print(red("Invalid input!"))
                input()

                clear_terminal()
            if player.hp > 0:
                
                print(yellow("You won!"))
                player.coins += opponent.loot
                roomsCleared += 1
            elif player.hp < 0:
                print(red("You lost!"))
            
            player.mana += 1
            if player.mana > player.maxMana:
                player.mana = player.maxMana
            input()
            
        elif roomType == 3:
            print(yellow("You found a treasure a chest!"))
            input()
            clear_terminal()

            #chest frame1
            print(r"""
    -Enter to open-
                  

      ..-------..
     //         \\
    ||====.-.====||
    ||   <=O=>   ||
    ||____'-'____||
    '-------------'
            """)
            
            loot = random.choices(list(chestLootTable.keys()), weights=list(chestLootTable.values()), k=1)[0]
            input()
            wait(0.5)
            clear_terminal()
            
            #chest frame2
            print(r"""
      .=='''''==.
      ||       || 
      ||       ||
      ||_______||  
     .'|       |'.
    ||====.-.====||
    ||   <=O=>   ||
    ||____'-'____||
    '-------------'           
            """)
            print(f"You found: {loot.name}")
            for i in range(len(player.inventory)):
                        if player.inventory[i] == "Empty":
                            player.inventory[i] = loot
                            break

            roomsCleared += 1
            input()

    #Opening inventory
    elif choice == "2":
        invOpen = True
        while invOpen == True:
            clear_terminal()
            inventoryOpen()
            print(azure("\nWhat will you do?"))
            print("1 = Back | 2 = Manage Inventory")
            choice = str(input("> "))

            #Go back
            if choice == "1":
                invOpen = False

            #Manage Inv
            elif choice == "2":
                clear_terminal()
                inventoryOpen()

                slotSelected = False
                invSlotAmount = len(player.inventory)
                print(azure("\nSelect slot number:"))
                choice = str(input("> "))
                if choice == "":
                    print(red("Invalid input!"))
                    input()
                    continue

                chosenIndex = (int(choice)-1)
                if player.inventory[chosenIndex]=="Empty":
                    print("Selected slot is empty.")
                    input()
                else:

                    selectedItem = player.inventory[chosenIndex]
                    print("\nSelected item:",selectedItem.name)


                    #WEAPON
                    if selectedItem.tag == "weapon":
                        print(red(f"{selectedItem.dmg} DMG"))
                        print(f"{red(selectedItem.info)}")
                        print(azure("\nWhat will you do?"))
                        print("1 = Back | 2 = Equip | 3 = Toss")

                        choice = str(input("> "))
                        if choice == "1":
                            continue
                        elif choice == "2":
                            player.inventory[chosenIndex] = equippedWeapon

                            currentWeapon = equippedWeapon
                            equippedWeapon = selectedItem
                        elif choice == "3":
                            print(f"\nAre you sure you want to throw {player.inventory[chosenIndex].name} away?")
                            print(f"1 = Yes | 2 = No")
                            choice = str(input("> "))
                            if choice == "1":
                                player.inventory[chosenIndex] = "Empty"
                            elif choice == "2":
                                continue
                            else:
                                print(red("Invalid Input!"))
                                input()
                            

                    
                    #CONSUM
                    elif selectedItem.tag == "consum":
                        print(f"{selectedItem.effect}")
                        print(f"{selectedItem.info}")
                        print(azure("\nWhat will you do?"))
                        print("1 = Back | 2 = Use | 3 = Toss")
                        choice = str(input("> "))

                        if choice == "1":
                            continue
                        elif choice == "2":
                            selectedItem.trigger()
                            maxStatCheck()
                            player.inventory[chosenIndex] = "Empty"
                        elif choice == "3":
                            print(f"\nAre you sure you want to throw {player.inventory[chosenIndex].name} away?")
                            print(f"1 = Yes | 2 = No")
                            choice = str(input("> "))
                            if choice == "1":
                                player.inventory[chosenIndex] = "Empty"
                            elif choice == "2":
                                continue
                            else:
                                print(red("Invalid Input!"))
                                input()

            else:
                print(red("Invalid Input!"))
                input()
    else:
        print(red("Invalid input!"))
        input()
    clear_terminal()

#-- TO-DO LIST --
#   Add new floors
#   Add sound effects / Music if possible

#SHOPKEEPER
#   -Every 15 rooms, there's a guaranteed encounter with the shopkeeper. He lets you buy from 5 randomly selected items
#   (based on the floor you're at)
#   (the shopkeeper's appearance will be determined by the floor you're on.)

#Different floors, which will get harder as the player progresses further. New enemies, new weapons, new items.
#   -Basement, Labyrinth, Catacombs, Atrium
#   -SPECIAL FLOORS
#       -Arena - A special floor which only consists of battles every turn.

#ROOM TYPES
#   -Empty room (Chance to find free gold)
#   -Battle room (Random enemy based on the floor)
#   -Treasure room (Gives you one random item based on the floor)
#   -Shop (Lets you spend your gold on randomly selected items)
#   -Archive (Let's you choose from three random spell scrolls)