#membuat input untuk membuat angka random
import random

#membuat pilihan
def cekHasil(a):
    jawaban = 0
    inputansalah = False
    stringsoal = ""

    #jika pemilih memilih pilihan 1
    if a == "1":
        x1 = random.randint(20, 50)
        x2 = random.randint(20, 50)
        choice = random.choice(operasi)
        stringsoal = f"{x1} {choice} {x2}"
        print("Berapakah hasil dari ", x1, choice, x2)
        if choice == '-':
            jawaban = x1 - x2
        elif choice == '+':
            jawaban = x1 + x2
        elif choice == '/':
            jawaban = x1 / x2
        elif choice == '*':
            jawaban = x1 * x2
            
    #jika pemlih memilih pilihan 2
    elif a == "2":
        x1 = random.randint(20, 70)
        x2 = random.randint(20, 70)
        x3 = random.randint(20, 70)
        choice = random.choice(operasi)
        choice2 = random.choice(operasi)
        stringsoal = f"{x1} {choice} {x2} {choice2} {x3}"
        print("Berapakah hasil dari ", x1, choice, x2, choice2, x3)
        if choice == '-':
            if choice2 == '-':
                jawaban = x1 - x2 - x3
            elif choice2 == '+':
                jawaban = x1 - x2 + x3
            elif choice2 == '/':
                jawaban = x1 - x2 / x3
            elif choice2 == '*':
                jawaban = x1 - x2 * x3
        elif choice == '+':
            if choice2 == '-':
                jawaban = x1 + x2 - x3
            elif choice2 == '+':
                jawaban = x1 + x2 + x3
            elif choice2 == '/':
                jawaban = x1 + x2 / x3
            elif choice2 == '*':
                jawaban = x1 + x2 * x3
        elif choice == '/':
            if choice2 == '-':
                jawaban = x1 / x2 - x3
            elif choice2 == '+':
                jawaban = x1 / x2 + x3
            elif choice2 == '/':
                jawaban = x1 / x2 / x3
            elif choice2 == '*':
                jawaban = x1 / x2 * x3
        elif choice == '*':
            if choice2 == '-':
                jawaban = x1 * x2 - x3
            elif choice2 == '+':
                jawaban = x1 * x2 + x3
            elif choice2 == '/':
                jawaban = x1 * x2 / x3
            elif choice2 == '*':
                jawaban = x1 * x2 * x3

    #jika pemilih memilih pilihan 3
    elif a == "3":
        x1 = random.randint(20, 100)
        x2 = random.randint(20, 100)
        x3 = random.randint(20, 100)
        x4 = random.randint(20, 100)
        choice = random.choice(operasi)
        choice2 = random.choice(operasi)
        choice3 = random.choice(operasi)
        stringsoal = f"{x1} {choice} {x2} {choice2} {x3} {choice3} {x4}"
        print("Berapakah hasil dari ", x1, choice, x2, choice2, x3, choice3, x4)
        if choice == '-':
            if choice2 == '-':
                if choice2 == '-':
                    jawaban = x1 - x2 - x3 - x4
                elif choice2 == '+':
                    jawaban = x1 - x2 - x3 + x4
                elif choice2 == '/':
                    jawaban = x1 - x2 - x3 / x4
                elif choice2 == '*':
                    jawaban = x1 - x2 - x3 * x4
            elif choice2 == '+':
                if choice2 == '-':
                    jawaban = x1 - x2 + x3 - x4
                elif choice2 == '+':
                    jawaban = x1 - x2 + x3 + x4
                elif choice2 == '/':
                    jawaban = x1 - x2 + x3 / x4
                elif choice2 == '*':
                    jawaban = x1 - x2 + x3 * x4
            elif choice2 == '/':
                if choice2 == '-':
                    jawaban = x1 - x2 / x3 - x4
                elif choice2 == '+':
                    jawaban = x1 - x2 / x3 + x4
                elif choice2 == '/':
                    jawaban = x1 - x2 / x3 / x4
                elif choice2 == '*':
                    jawaban = x1 - x2 / x3 * x4
            elif choice2 == '*':
                if choice2 == '-':
                    jawaban = x1 - x2 * x3 - x4
                elif choice2 == '+':
                    jawaban = x1 - x2 * x3 + x4
                elif choice2 == '/':
                    jawaban = x1 - x2 * x3 / x4
                elif choice2 == '*':
                    jawaban = x1 - x2 * x3 * x4
        elif choice == '+':
            if choice2 == '-':
                if choice2 == '-':
                    jawaban = x1 + x2 - x3 - x4
                elif choice2 == '+':
                    jawaban = x1 + x2 - x3 + x4
                elif choice2 == '/':
                    jawaban = x1 + x2 - x3 / x4
                elif choice2 == '*':
                    jawaban = x1 + x2 - x3 * x4
            elif choice2 == '+':
                if choice2 == '-':
                    jawaban = x1 + x2 + x3 - x4
                elif choice2 == '+':
                    jawaban = x1 + x2 + x3 + x4
                elif choice2 == '/':
                    jawaban = x1 + x2 + x3 / x4
                elif choice2 == '*':
                    jawaban = x1 + x2 + x3 * x4
            elif choice2 == '/':
                if choice2 == '-':
                    jawaban = x1 + x2 / x3 - x4
                elif choice2 == '+':
                    jawaban = x1 + x2 / x3 + x4
                elif choice2 == '/':
                    jawaban = x1 + x2 / x3 / x4
                elif choice2 == '*':
                    jawaban = x1 + x2 / x3 * x4
            elif choice2 == '*':
                if choice2 == '-':
                    jawaban = x1 + x2 * x3 - x4
                elif choice2 == '+':
                    jawaban = x1 + x2 * x3 + x4
                elif choice2 == '/':
                    jawaban = x1 + x2 * x3 / x4
                elif choice2 == '*':
                    jawaban = x1 + x2 * x3 * x4
        elif choice == '/':
            if choice2 == '-':
                if choice2 == '-':
                    jawaban = x1 / x2 - x3 - x4
                elif choice2 == '+':
                    jawaban = x1 / x2 - x3 + x4
                elif choice2 == '/':
                    jawaban = x1 / x2 - x3 / x4
                elif choice2 == '*':
                    jawaban = x1 / x2 - x3 * x4
            elif choice2 == '+':
                if choice2 == '-':
                    jawaban = x1 / x2 + x3 - x4
                elif choice2 == '+':
                    jawaban = x1 / x2 + x3 + x4
                elif choice2 == '/':
                    jawaban = x1 / x2 + x3 / x4
                elif choice2 == '*':
                    jawaban = x1 / x2 + x3 * x4
            elif choice2 == '/':
                if choice2 == '-':
                    jawaban = x1 / x2 / x3 - x4
                elif choice2 == '+':
                    jawaban = x1 / x2 / x3 + x4
                elif choice2 == '/':
                    jawaban = x1 / x2 / x3 / x4
                elif choice2 == '*':
                    jawaban = x1 / x2 / x3 * x4
            elif choice2 == '*':
                if choice2 == '-':
                    jawaban = x1 / x2 * x3 - x4
                elif choice2 == '+':
                    jawaban = x1 / x2 * x3 + x4
                elif choice2 == '/':
                    jawaban = x1 / x2 * x3 / x4
                elif choice2 == '*':
                    jawaban = x1 / x2 * x3 * x4
        elif choice == '*':
            if choice2 == '-':
                if choice2 == '-':
                    jawaban = x1 * x2 - x3 - x4
                elif choice2 == '+':
                    jawaban = x1 * x2 - x3 + x4
                elif choice2 == '/':
                    jawaban = x1 * x2 - x3 / 4
                elif choice2 == '*':
                    jawaban = x1 * x2 - x3 * x4
            elif choice2 == '+':
                if choice2 == '-':
                    jawaban = x1 * x2 + x3 - x4
                elif choice2 == '+':
                    jawaban = x1 * x2 + x3 + x4
                elif choice2 == '/':
                    jawaban = x1 * x2 + x3 / x4
                elif choice2 == '*':
                    jawaban = x1 * x2 + x3 * x4
            elif choice2 == '/':
                if choice2 == '-':
                    jawaban = x1 * x2 / x3 - x4
                elif choice2 == '+':
                    jawaban = x1 * x2 / x3 + x4
                elif choice2 == '/':
                    jawaban = x1 * x2 / x3 / x4
                elif choice2 == '*':
                    jawaban = x1 * x2 / x3 * x4
            elif choice2 == '*':
                if choice2 == '-':
                    jawaban = x1 * x2 * x3 - x4
                elif choice2 == '+':
                    jawaban = x1 * x2 * x3 + x4
                elif choice2 == '/':
                    jawaban = x1 * x2 * x3 / x4
                elif choice2 == '*':
                    jawaban = x1 * x2 * x3 * x4
                    
    #jika pemilih memilih selain itu
    else:
        print("inputan salah")
        inputansalah = True
    if not inputansalah:
        jawabananda = float(input("Masukkan jawaban anda: "))
        if (jawaban == jawabananda or jawabananda == ("%.3f" % jawaban)):
            print("Jawaban anda benar !")
        else:
            print("Jawaban Anda Masih Salah")
            print("Hasil dari ", stringsoal, " = %.3f" % jawaban)

#Pengeoprasian bilangan
operasi = ['+','-','/','*']
print("======Program test aritmatika dasar======")
print("Pilihan level yang tersedia :")
print("1. Easy")
print("2. Medium")
print("3. Hard")
pilihan=str(input("Masukkan tingkatan yang ingin anda coba :"))
cekHasil(pilihan)
