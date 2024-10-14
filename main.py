print('''WELCOME TO UR MUM'S ADVENTURE GAME!!!!!!!
created by the mighty heydon''')

# ---------------------------
import random
import time

living_status = 1 # 1 is alive 0 is dead 0.5 is zombie like
cultivate_chance = 0
stats_strength = 0
stats_realm = 0 
stats_wealth = 0
power_type = "neutral"
time_power = 5
# ---------------------------
character_name = str(input('''what do u want ur name to be?
'''))
time.sleep(2.0)
print("PEASANT (friendly) : ", character_name,'''ur finally awake!
you've been asleep for 10 years!! the world has changed since you've last been awake''')

time.sleep(5.0)

choice_1 = input('''you have woken up from your coma.
The world has changed in your absence and you are currently a low-life mortal.
You have 2 choices from the inheritence your parents have given you.
a) mortal life
b) immortal cultivation
''')

time.sleep(4.0)

if choice_1.lower() == "a":
    print('''you have chosen... mortal life''')
    time.sleep(1)
    print("ibsfr thats lowkey boring.")
    time.sleep(1)
    print('''you live a boring and uneventful life until you die at the ripe old age of 40
due to the shockwaves of a fight among immortals''')
    living_status = 0
    quit()
# END 

if choice_1.lower() == "b":
    power_type = input('''IMMORTAL (cannot determine) : you have chosen... IMMORTAL CULTIVATION
what path do you want to travel on?
a) time path
b) space path
c) blood
d) mind
''')
    if power_type.lower() == "a":
        power_type = "time"
    if power_type.lower() == "b":
        power_type = "space"
    if power_type.lower() == "c":
        power_type = "blood"
    if power_type.lower() == "d":
        power_type = "mind"
    else:
        print("you have failed to answer and died due to the backlash of summoning an immortal")
        living_status = 0
        quit()

time.sleep(5)

choice_daily = input('''what do u want to do now?
[cultivate,explore,kys or engage in thievery]
''')

if choice_daily.lower() == "cultivate" :
    print("nerd")
    print('''Immortal : Immortal ranks are in this order :
100 is Realm 1 Immortal
200 is Realm 2 Immortal
300 is Realm 3 Immortal
500 is Realm 4 Immortal
1000 is Realm 5 Immortal
after realm 5, you are not qualified to know.''')
    cultivate_chance = random.randrange(1,100)
    stats_realm = cultivate_chance + stats_realm
    time.sleep(5)
    print("you have cultivated to",stats_realm)
    cultivate_chance = 0

elif choice_daily.lower() == "explore":
    print("REALM 3 GUARD (neutral) : your realm is currently too low to explore but I'll let u go")
    print("you encounter a REALM 1 Wild Boar! 100/100 HP (enemy)")
    fight_choice = input("fight? y/n")
    if fight_choice.lower() == "y" :
        print('''you could not manage to cross realms to fight and as a result... 
you died to the REALM 1 Wild Boar''')
        if power_type == "time":
            print("due to your time power, you have been reborn.")
        else:
            living_status = 0
            quit()
    else:
        print("you took too long and died 💀☠️☠️")
        if power_type == "time":
            print("due to your time power, you have been reborn. don't make the same mistake again!")
            time_power = time_power - 1

elif choice_daily.lower() == "kys":
    print("you decided this decision was too overwhelming and exploded your soul")
    living_status = 0
    quit()





elif living_status == 0:
    print("you are currently a ghost.")

















































































