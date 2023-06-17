from colorama import Fore, Style
import random

njfr = random.randint(450,550)
njhr = random.randint(3000,3500)

gsfr = random.randint(850,1050)
gshr = random.randint(1400,2000)

ftfr = random.randint(275,325)
fthr = random.randint(5000,6000)

hlfr = random.randint(150,200)
hlhr = random.randint(2200,3200)
hlpr = random.randint(375,525)

mgfr = random.randint(325,400)
mghr = random.randint(2250,2750)
mgpr = random.randint(100,150)

chlst = {

    "Ninja" : {
    "Power": njfr,
    "Hp" : njhr,
    "Heal": 0,
    "Dodge": "%25",
    "Name" : "Ninja"
    },

    "Gunsmith" : {
    "Power": gsfr,
    "Hp" : gshr,
    "Heal": 0,
    "Dodge": "%16",
    "Name" : "Gunsmith"
    },

    "Fighter" : {
    "Power": ftfr,
    "Hp" : fthr,
    "Heal": 0,
    "Dodge": "%14",
    "Name" : "Fighter"
    },

    "Healer" : {
    "Power": hlfr,
    "Hp" : hlhr,
    "Heal":hlpr,
    "Dodge": "%9",
    "Name" : "Healer"
    },

    "Magician" : {
    "Power": mgfr,
    "Hp" : mghr,
    "Heal":mgpr,
    "Dodge": "%33",
    "Name" : "Magician"
    }
}

lgt = [chlst['Gunsmith'],chlst['Fighter'],chlst['Healer'],chlst['Ninja'],chlst['Magician']]

def hit(shooter,shot):
    shot["Hp"] -= shooter["Power"]

def can(given,received):
    received["Hp"] += given["Heal"]

clo = (Fore.WHITE + Style.BRIGHT)
clorst = (Fore.RESET + Style.RESET_ALL)

print(clo + """
                                    Welcome to My Python War Game o7

1) 1 Vs 1
2) 1 Vs 2
3) 2 Vs 2
4) Character Skills
Q) Quit
""" + clorst)

choic = input("Enter the Transaction Number : ")

if choic == "1":
    print(clo + """

    Select Your Character

N)Ninja
G)Gunsmith
F)Fighter
H)Healer
M)Magician  

    """ + clorst)
    choicS = input("Enter the Transaction Number : ").lower()

    if choicS == "n":
        print("\nOur war begins")
        chrt = random.choice(lgt)
        while True:
            input(f"Press {Style.BRIGHT}'enter'{clorst} for to new round! ")
            print(f"{clo}-{clorst}"*25)
            if random.randint(1,3) == 1:
                print(f"{Fore.CYAN}Dodge {chrt['Name']}{clorst}")
            else:
                hit(chlst['Ninja'],chrt)
            if random.randint(1,4) == 1:
                print(f"{Fore.CYAN}Dodge Ninja{clorst}")
            else:
                hit(chrt,chlst['Ninja'])
            print(f"{Fore.GREEN}Ninja's Health:{clorst}",chlst['Ninja']["Hp"])
            print(f"{Fore.GREEN}{chrt['Name']}'s Health:{clorst}",chrt["Hp"])
            if chlst['Ninja']["Hp"] < 0:
                print(f"\n{Fore.YELLOW}{chrt['Name']} Win{clorst}")
                break
            elif chrt["Hp"] < 0:
                print(f"\n{Fore.YELLOW}Ninja Win{clorst}")
                break
            if chrt["Hp"] and chlst['Ninja']["Hp"] < 0:
                print(f"\n{Fore.MAGENTA}Ninja and {chrt['Name']} shot at the same time, Draw{clorst}")
                break
            else:
                print(f"{clo}-{clorst}"*25)
    elif choicS == "g":
        print("\nOur war begins")
        chrt = random.choice(lgt)
        while True:
            input(f"Press {Style.BRIGHT}'enter'{clorst} for to new round! ")
            print(f"{clo}-{clorst}"*25)
            if random.randint(1,3) == 1:
                print(f"{Fore.CYAN}Dodge {chrt['Name']}{clorst}")
            else:
                hit(chlst['Gunsmith'],chrt)
            if random.randint(1,4) == 1:
                print(f"{Fore.CYAN}Dodge Gunsmith{clorst}")
            else:
                hit(chrt,chlst['Gunsmith'])
            print(f"{Fore.GREEN}Gunsmith's Health:{clorst}",chlst['Gunsmith']["Hp"])
            print(f"{Fore.GREEN}{chrt['Name']}'s Health:{clorst}",chrt["Hp"])
            if chlst['Gunsmith']["Hp"] < 0:
                print(f"\n{Fore.YELLOW}{chrt['Name']} Win{clorst}")
                break
            elif chrt["Hp"] < 0:
                print(f"\n{Fore.YELLOW}Gunsmith Win{clorst}")
                break
            if chrt["Hp"] and chlst['Gunsmith']["Hp"] < 0:
                print(f"\n{Fore.MAGENTA}Gunsmith and {chrt['Name']} shot at the same time, Draw{clorst}")
                break
            else:
                print(f"{clo}-{clorst}"*25)
    elif choicS == "f":
        print("\nOur war begins")
        chrt = random.choice(lgt)
        while True:
            input(f"Press {Style.BRIGHT}'enter'{clorst} for to new round! ")
            print(f"{clo}-{clorst}"*25)
            if random.randint(1,3) == 1:
                print(f"{Fore.CYAN}Dodge {chrt['Name']}{clorst}")
            else:
                hit(chlst['Fighter'],chrt)
            if random.randint(1,4) == 1:
                print(f"{Fore.CYAN}Dodge Fighter{clorst}")
            else:
                hit(chrt,chlst['Fighter'])
            print(f"{Fore.GREEN}Fighter's Health:{clorst}",chlst['Fighter']["Hp"])
            print(f"{Fore.GREEN}{chrt['Name']}'s Health:{clorst}",chrt["Hp"])
            if chlst['Fighter']["Hp"] < 0:
                print(f"\n{Fore.YELLOW}{chrt['Name']} Win{clorst}")
                break
            elif chrt["Hp"] < 0:
                print(f"\n{Fore.YELLOW}Fighter Win{clorst}")
                break
            if chrt["Hp"] and chlst['Fighter']["Hp"] < 0:
                print(f"\n{Fore.MAGENTA}Fighter and {chrt['Name']} shot at the same time, Draw{clorst}")
                break
            else:
                print(f"{clo}-{clorst}"*25)
    elif choicS == "h":
        print("\nOur war begins")
        chrt = random.choice(lgt)
        while True:
            input(f"Press {Style.BRIGHT}'enter'{clorst} for to new round! ")
            print(f"{clo}-{clorst}"*25)
            if random.randint(1,3) == 1:
                print(f"{Fore.CYAN}Dodge {chrt['Name']}{clorst}")
            else:
                hit(chlst['Healer'],chrt)
            if random.randint(1,4) == 1:
                print(f"{Fore.CYAN}Dodge Healer{clorst}")
            else:
                hit(chrt,chlst['Healer'])
            print(f"{Fore.GREEN}Healer's Health:{clorst}",chlst['Healer']["Hp"])
            print(f"{Fore.GREEN}{chrt['Name']}'s Health:{clorst}",chrt["Hp"])
            if chlst['Healer']["Hp"] < 0:
                print(f"\n{Fore.YELLOW}{chrt['Name']} Win{clorst}")
                break
            elif chrt["Hp"] < 0:
                print(f"\n{Fore.YELLOW}Healer Win{clorst}")
                break
            if chrt["Hp"] and chlst['Healer']["Hp"] < 0:
                print(f"\n{Fore.MAGENTA}Healer and {chrt['Name']} shot at the same time, Draw{clorst}")
                break
            else:
                print(f"{clo}-{clorst}"*25)
    elif choicS == "m":
        print("\nOur war begins")
        chrt = random.choice(lgt)
        while True:
            input(f"Press {Style.BRIGHT}'enter'{clorst} for to new round! ")
            print(f"{clo}-{clorst}"*25)
            if random.randint(1,3) == 1:
                print(f"{Fore.CYAN}Dodge {chrt['Name']}{clorst}")
            else:
                hit(chlst['Magician'],chrt)
            if random.randint(1,4) == 1:
                print(f"{Fore.CYAN}Dodge Magician{clorst}")
            else:
                hit(chrt,chlst['Magician'])
            print(f"{Fore.GREEN}Magician's Health:{clorst}",chlst['Magician']["Hp"])
            print(f"{Fore.GREEN}{chrt['Name']}'s Health:{clorst}",chrt["Hp"])
            if chlst['Magician']["Hp"] < 0:
                print(f"\n{Fore.YELLOW}{chrt['Name']} Win{clorst}")
                break
            elif chrt["Hp"] < 0:
                print(f"\n{Fore.YELLOW}Magician Win{clorst}")
                break
            if chrt["Hp"] and chlst['Magician']["Hp"] < 0:
                print(f"\n{Fore.MAGENTA}Magician and {chrt['Name']} shot at the same time, Draw{clorst}")
                break
            else:
                print(f"{clo}-{clorst}"*25)
        
elif choic == "2":
    print("BB Daha Sonra Tekrar Bekleriz...")
elif choic == "3":
    print("BB Daha Sonra Tekrar Bekleriz...")
elif choic == "4":
    print("Character Skills:\n")
    print(f"{clo}Ninja;\n {Fore.YELLOW}Power = {chlst['Ninja']['Power']}\n {Fore.GREEN}Hp = {chlst['Ninja']['Hp']}\n {Fore.RED}Heal = {chlst['Ninja']['Heal']}\n {Fore.CYAN}Dodge = {chlst['Ninja']['Dodge']}\n")
    print(f"{clo}Gunsmith;\n {Fore.YELLOW}Power = {chlst['Gunsmith']['Power']}\n {Fore.GREEN}Hp = {chlst['Gunsmith']['Hp']}\n {Fore.RED}Heal = {chlst['Gunsmith']['Heal']}\n {Fore.CYAN}Dodge = {chlst['Gunsmith']['Dodge']}\n")
    print(f"{clo}Fighter;\n {Fore.YELLOW}Power = {chlst['Fighter']['Power']}\n {Fore.GREEN}Hp = {chlst['Fighter']['Hp']}\n {Fore.RED}Heal = {chlst['Fighter']['Heal']}\n {Fore.CYAN}Dodge = {chlst['Fighter']['Dodge']}\n")
    print(f"{clo}Healer;\n {Fore.YELLOW}Power = {chlst['Healer']['Power']}\n {Fore.GREEN}Hp = {chlst['Healer']['Hp']}\n {Fore.RED}Heal = {chlst['Healer']['Heal']}\n {Fore.CYAN}Dodge = {chlst['Healer']['Dodge']}\n {clorst}")
elif choic == "Q" or choic == "q":
    print("BB Daha Sonra Tekrar Bekleriz...")
    quit()  

    # Dodge mekanigini düzelt dıştan çek
    # Heal basma muhabettini coz 
    