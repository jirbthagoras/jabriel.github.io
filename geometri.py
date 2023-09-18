
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
    jarijari = float(input("Masukkan jari jari segitga "))
    total = 3.14 * jarijari ** 2
    print("PI X {} X {} = {}".format(jarijari, jarijari, total))

while True:

    select = input("pilih jenis bengun datar yang ingin dihitung luasnya = \n A. Persegi \n B. Persegi panjang \n C. Segitiga \n D. Lingkaran \n")
    if select == "A":
        persegi()
    elif select == "B":
        persegiPanjang()
    elif select == "C":
        segitiga()
    elif select == "D":
        lingkaran()
        

    maulagigak = input("Mau hitung lagi? Yes/No = \n")

    if maulagigak == "Yes":
        pass
    elif maulagigak == "No":
        break
