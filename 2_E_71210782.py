#untuk mencari huruf tengah
def huruftengah(word):
    bagi=len(word)//2
    
    #rumus if dan and
    if (len(word)%2==0) and ((len(word)/2)%2==0):
        return word[(bagi)//2 : ((bagi)//2)*-1]
    elif (len(word)%2==0) and ((len(word)/2)%2!=0):
        return word[((bagi)//2)+1 : (((bagi)//2)+1)*-1]
    else:
        return word[(((bagi)+1)//2) : (((bagi)+1)//2)*-1]

#hasil dengan print
word= str(input("Masukkan kata :"))
print("Huruf tengah pada kata" ,word ,"adalah" ,huruftengah(word))
