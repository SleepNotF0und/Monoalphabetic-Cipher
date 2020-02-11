import random
while True:
    ch = int(input("Press 1 for Encrypt Or 2 for Decrypt:-\n"))

    if ch == 1:
        text = input("Text:").lower()

        alpha = [a for a in range(97,123)]

        charactrize=[]
        for al in alpha:
            charactrize.append(chr(al))
        charactrize.append(' ')

        key =[]
        shuffled = random.sample(alpha,len(alpha))
        for sh in shuffled:
            key.append(chr(sh))
        key.append(' ')

        print("\n============================================")
        print("            !!!Encrypted!!!                   ")
        for tx in text:
            print(key[charactrize.index(tx)],end="")
        print("\n============================================")
        print("Using Key:",key,"\n")

    elif ch == 2:
        text = input("text:").lower()
        key = eval(input("Key:"))

        alpha = [a for a in range(97,123)]

        charactrize=[]
        for al in alpha:
            charactrize.append(chr(al))
        charactrize.append(' ')
    
        print("\n============================================")
        print("               !!!Decrypted!!!                ")
        for tx in text:
            print(charactrize[key.index(tx)],end="")
        print("\n============================================\n")