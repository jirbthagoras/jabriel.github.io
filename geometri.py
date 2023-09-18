
def persegi():
    num = float(input("masukkan sisi pertama = \n"))
    total = num ** 2
    print("{} X {} = {}".format(num, num, total))

def persegiPanjang():
    num1 = float(input("masukkan panjang sisi pertama = "))
    num2 = float(input("masukkan panjang sisi kedua = "))
    total = num1 * num2
    print("{} X {} = {}".format(num1, num2, total))

def segitiga():
    tinggi = float(input("Masukkan tinggi segitiga = "))
    alas = float(input("Masukkan panjang alas segitiga = "))
    total = (tinggi * alas) / 2
    print("1/2 X {} X {} = {}".format(tinggi, alas, total))

def lingkaran():
    jarijari = float(input("Masukkan jari jari lingkaran "))
    total = 3.14 * jarijari ** 2
    print("PI X {} X {} = {}".format(jarijari, jarijari, total))

def pythagoras():
    select2 = input("Mau hitung sisi A, B, atau C?")
    if (select2 == "A"):
        B = int(input("Masukkan panjang sisi B = "))
        C = int(input("Masukkan panjang sisi C = "))
        total = (C ** 2 - B ** 2)
        total **= 1/2
        print("({} ** 2 - {} ** 2) ** 1/2 = {}".format(B, C, total))
    elif (select2 == "B"):
        A = int(input("Masukkan panjang sisi A = "))
        C = int(input("Masukkan panjang sisi C = "))
        total = (C ** 2 - B ** 2)
        total **= 1/2
        print("({} ** 2 - {} ** 2) ** 1/2 = {}".format(A, C, total))
    elif (select2 == "C"):
        A = int(input("Masukkan panjang sisi A = "))
        B = int(input("Masukkan panjang sisi B = "))
        total = (A ** 2 + B ** 2)
        total **= 1/2
        print("({} ** 2 + {} ** 2) ** 1/2 = {}".format(A, B, total))
    else:
        print("Input valid option!")


while True:
    select = input("pilih jenis bengun datar yang ingin dihitung luasnya = \n A. Persegi \n B. Persegi panjang \n C. Segitiga \n D. Lingkaran \n E. Pythagoras \n")
    if select == "A":
        persegi()
    elif select == "B":
        persegiPanjang()
    elif select == "C":
        segitiga()
    elif select == "D":
        lingkaran()
    elif select == "E":
        pythagoras()


    maulagigak = input("Mau hitung lagi? Yes/No = \n")

    if maulagigak == "Yes":
        pass
    elif maulagigak == "No":
        break
    else:
        break