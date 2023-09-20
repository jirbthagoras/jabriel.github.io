import maskpass

play = True
player1 = 0
player2 = 0
checker2 = 0
checker3 = 0
checker4 = 0
player1_name = None
player2_name = None


def roundGanjil():

    array = ["W", "A", "S", "D"]
    global ronde
    checker1 = 0
    player1_1 = 0
    player2_1 = 0
    global player1
    global player2

    print("Mari mulai round {}, {} tebaklah direction {}!!\n".format(ronde, player1_name, player2_name))
    
    
    while checker1 == 0:
        player1_1 = maskpass.advpass(prompt= "{} masukkan directionmu! W/A/S/D? \n".format(player1_name), mask= "#")
        player2_1 = maskpass.advpass("{} masukkan directionmu! W/A/S/D? \n".format(player2_name), mask="#")

        if player1_1 not in array or player2_1 not in array:
            print("Masukkan direction yang valid!\n")
        elif player1_1 == player2_1:
            print("{} memilih {} dan {} memilih {}".format(player1_name, player1_1, player2_name, player2_1))
            print("{} menang!".format(player1_name))
            player1 += 1
            print("skor untuk saat ini adalah:\n {} = {} dan {} = {}".format(player1_name, player1, player2_name, player2))
            checker1 += 1
        elif player1_1 != player2_1:
            print("{} memilih {} dan {} memilih {}".format(player1_name, player1_1, player2_name, player2_1))
            print("{} menang!".format(player1_name))
            player2 += 1
            print("skor untuk saat ini adalah:\n {} = {} dan {} = {}".format(player1_name, player1, player2_name, player2))
            checker1 += 1

def roundGenap():

    array = ["W", "A", "S", "D"]
    global ronde
    checker1 = 0
    player1_1 = 0
    player2_1 = 0
    global player1
    global player2

    print("Mari mulai round {}, {} tebaklah direction {}!!\n".format(ronde, player2_name, player1_name))
    
    
    while checker1 == 0:
        player1_1 = maskpass.advpass(prompt= "{} masukkan directionmu! W/A/S/D? \n".format(player2_name), mask= "#")
        player2_1 = maskpass.advpass(prompt= "{} masukkan directionmu! W/A/S/D? \n".format(player1_name), mask= "#")

        if player1_1 not in array or player2_1 not in array:
            print("Masukkan direction yang valid!")
        elif player1_1 == player2_1:
            print("{} memilih {} dan {} memilih {}".format(player1_name, player1_1, player2_name, player2_1))
            print("{} menang!".format(player2_name))
            player2 += 1
            print("skor untuk saat ini adalah:\n {} = {} dan {} = {}".format(player1_name, player1, player2_name, player2))
            checker1 += 1
        elif player1_1 != player2_1:
            print("{} memilih {} dan {} memilih {}".format(player1_name, player1_1, player2_name, player2_1))
            print("{} menang!".format(player1_name))
            player1 += 1
            print("skor untuk saat ini adalah:\n {} = {} dan {} = {}".format(player1_name, player1, player2_name, player2))
            checker1 += 1
        
def again():
    global again1
    global checker2
    global player1
    global play
    global player1_name
    global player2
    global player2_name
    global checker4

    if again1 == "Yes":
        while checker2 == 0:
            again2 = str(input("Ingin main dengan skor sebelumnya? Y/N = "))
            if again2 != "Y" and again2 != "N":
                print("Masukkan input yang valid!")
            elif again2 == "N":
                player1 = None
                player1_name = None
                player2 = None
                player2_name = None
                checker2 += 1
            elif again2 == "Y":
                checker2 += 1

while play == "Y" or play == True:

    if player1_name == None:
        while checker3 == 0:
            play = str(input("Mau main Shadowboxing? Y/N = "))
            if play == "N":
                checker3 += 2
                checker4 = 0
                break
            elif play == "Y":
                checker3 += 1
                checker4 = 0
            else:
                print("Masukkan input yg valid!")
    elif player1_name != None:
        again1 = str(input("Game telah selesai! Apakah kalian ingin main lagi? Yes/No = "))
        again()

        while checker4 == 0:
            if again1 == "No":
                checker4 += 2
                break
            else:
                print("Masukkan input yang valid")
                checker4 += 1
            


    if checker3 == 2:
        break
    elif checker4 == 2:
        break

    if player1_name == None:
        player1_name = str(input("Masukkan nama player 1 = "))
        player2_name = str(input("Masukkan nama player 2 = "))

    if player1 > 0 and player2 > 0:
        print("Halo player {} dan player {} selamat datang kembali!".format(player1_name, player2_name))
        print("skor untuk saat ini: \n {} = {} dan {} = {}".format(player1_name, player1, player2_name, player2))
    elif player1 == 0 and player2 == 0:
        print("Halo player {} dan player {} nikmatilah permainan!\n".format(player1_name, player2_name))
        print("skor untuk saat ini masih {} dan {}!".format(player1, player2))

    
    for ronde in range(1, 8):
        if ronde % 2 != 0:
            roundGanjil()
        elif ronde % 2 == 0:
            roundGenap()
    
    if player1 > player2:
        print("{} menang! Dengan skor: ".format(player1_name))
        print("{} = {} dan {} = {}".format(player1_name, player1, player2_name, player2))
        print("{} adalah pengecut sial".format(player2_name))
    elif player1 < player2:
        print("{} menang! Dengan skor: ".format(player2_name))
        print("{} = {} dan {} = {}".format(player1_name, player1, player2_name, player2))
        print("{} adalah pengecut sial".format(player1_name))