result = ''
message = ''
choice = ''
def encrypt():
    global result
    message = input('\nEnter message for encryption:==>\n')
    for i in range(0, len(message)):
        result = result + chr(ord(message[i]) + 2)

    print('\nyour encrypted message==>\n',result + '\n')
    result = ''
    return result
def decrypt():
    
    global result
    message = input('\nEnter message for decryption:==>\n')
    for i in range(0, len(message)):
        result = result + chr(ord(message[i]) - 2)

    print('\nyour decrypted message==>\n',result + '\n\n')
    result = ''
    return result

while choice != 0:

     choice = input('select your choice\n 1.==> encrypt message:\n 2.==> decrypt message:\n=>')
     if choice =='1':
        encrypt()
         
     if choice == '2':
        decrypt()    
     else:
        print('\nexit\n')

