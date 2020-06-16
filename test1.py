import math

message = "AKUU"
#key = "GYBNQKURP"
key="BCDF"
if int(math.sqrt(len(key)))==3:
    while len(message)%3!=0:
        message+="Z"
if int(math.sqrt(len(key)))==2:
    while len(message)%2!=0:
        message+="Z"

keyMatrix = [[0] * int(math.sqrt(len(key))) for i in range(int(math.sqrt(len(key))))]

messageVector = [[0] for i in range(len(message))]

hasil=list()

def getKeyMatrix(key):
    k = 0
    for i in range(int(math.sqrt(len(key)))):
        for j in range(int(math.sqrt(len(key)))):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

def encrypt(messageVector):
    for z in range(0,len(message),int(math.sqrt(len(key)))):
        mess=messageVector[z:z+int(math.sqrt(len(key)))]
        cipherMatrix = [[0] for i in range(len(message))]
        print(z)
        print(mess)
        for i in range(int(math.sqrt(len(key)))):
            for x in range(int(math.sqrt(len(key)))):
                cipherMatrix[i][0] += (keyMatrix[i][x]*mess[x][0])
                print(cipherMatrix[i][0],end=" ")
            print("")
            cipherMatrix[i][0] = cipherMatrix[i][0] % 26
            hasil.append(cipherMatrix[i][0])

def HillCipher(message, key):
    getKeyMatrix(key)

    for i in range(len(message)):
        messageVector[i][0] = ord(message[i]) % 65
    print(messageVector)
    encrypt(messageVector)
    print(hasil)
    CipherText = []
    for i in hasil:
        CipherText.append(chr(i + 65))

    print("Ciphertext: ", "".join(CipherText))

def main():
    HillCipher(message, key)
if __name__ == "__main__":
    main()

