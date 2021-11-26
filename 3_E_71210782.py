#print data
print ("=======Program Manipulasi String=======")
print ("Pilihan Menu :")
print ("1. Hitung kata")
print ("2. cek kata")
print ("3. ubah kata")

#input data
pilih = (input("Pilihan anda :"))
masukkan = (input("masukan kalimat/kata :"))
result = (masukkan.lower())

#jika memilih nomor 1
if pilih == "1":
    
    a = input("Masukkan kata yang ingin dihitung :")
    b = result.count (a)
    print("Terdapat sebanyak" ,b ,"kata" ,a ,"didalam string")

#jika memilih  nomor 2
elif pilih == "2":

    x = input("Masukkan kata yang ingin di cek :")
    c = x.upper()
    d = result.replace(x,c)
    if c not in result:
        print("Kata" ,c ,"tidak terdapat dalam string")
        print("String diubah menjadi :")
        print(d, x)
    else :
        print("kata",x ,"terdapat di dalam string")
        print("string diubah menjadi :")
        print(d)

#jika memilih nomor 3
elif pilih == "3":

    e = input("Masukkan kata yang ingin di ubah :")
    f = input("Masukkan kata pengganti :")
    
    print("Anda akan mengubah kata" ,e ,"menjadi" ,f ,"sebanak 1x")
    ganti = input("Apakah anda ingin mengubah total penggantian kata ? (yes/no) :")
    
    #jika penggguna memilih yes
    if ganti == "yes":
        g = int(input("Masukkan jumlah total penggantian :"))
        print("String berhasil diubha menjadi :")
        h = result.replace(e ,f ,g)
        print(h)

    #jika pengguna memilih no
    elif ganti == "no":
        g = 1
        print("String berhasil diubah menjadi")
        h = result.replace(e, f, g )
        print(h)
