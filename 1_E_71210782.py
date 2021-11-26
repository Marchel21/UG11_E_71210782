#print data
print("Menu Program yang tersedia")
print("1. pangkatkan angka")
print("2. akarkan bilangan")

#input rumus untuk memasukkan data
A = float(input("Masukkan pilihan yang dingginkan :"))
if A == 1:
    print("Masukkan angka yang ingin di Pangkatkan")
    x = float(input("Angka :"))
    print ("ingin memodifikasi akar ? (yes/no)")
    y = str(input(":"))
    if y == "yes":
        z = float(input("Masukkan nilai pangkat :"))
        xz = x ** z
        print ("Hasil dari " ,x ,"^" ,z ,"=" ,xz)
    elif y == "no":
        xz = x ** 2
        print ("Hasil dari" ,x ,"^2" ,"=" ,xz)
elif A == 2:
    print ("Masukkan angka yang ingin di akar")
    x = float(input("Angka :"))
    print ("ingin memodifikasi akar ? (yes/no)")
    c = str(input(": "))
    if c == "yes":
        z = float(input("Masukkan nilai akar : "))
        xz = x ** (1.0/z)
        print ("Hasil akar pangkat 2" ,z ,"dari" ,x ,"=" ,round(xz,2))
    elif c == "no":
        xz = x ** (1.0/2)
        print ("Hasil akar pangkat 2","dari" ,x, "=" ,round(xz,2))
