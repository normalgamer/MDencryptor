'''

Python Encryptor, by normalgamer
github.com/normalgamer

Encrypts a string using its md5 hash, which then gets appended to the file

'''


import hashlib

characters  = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']


message     = "aaaaa"
encodedText = " "
decodedText = " "
MD5Numbers  = ""

def encode(string):
    
    global encodedText
    global message
    global MD5Numbers
    
    encodedText = ""
    
    md5 = hashlib.md5(string.encode())
    md5 = md5.hexdigest()
    
    for char in md5:
        MD5Numbers = MD5Numbers + str(ord(char))
    
    string = string.lower()
    
    charNumber=0
    for char in string:
        if char in characters:
            x = characters.index(char)
            if(charNumber==len(MD5Numbers)):
                charNumber=0    
                i = MD5Numbers[charNumber]
                encodedText = encodedText+characters[x+int(i)]
            else:
                i = MD5Numbers[charNumber]
                encodedText = encodedText+characters[x+int(i)]
                
        else:
            encodedText = encodedText+char
            
        charNumber = charNumber+1
        
    encodedText = encodedText + md5
    
    
def decode(string):
    # Global variables
    global encodedText
    global decodedText
    global message
    global MD5Numbers
    
    decodedText = ""
    MD5Numbers  = ""
    
    # Recover MD5 hash from string
    md5 = string[-32:]
    #print("DEBUG MD5="+md5)
    
    for char in md5:
        MD5Numbers = MD5Numbers + str(ord(char))
    
    string = string.replace(md5,"")
    
    charNumber=0
    for char in string:
        if char in characters:
            x = characters.index(char)
            if(charNumber==len(MD5Numbers)):
                charNumber=0
                i = MD5Numbers[charNumber]
                decodedText = decodedText+characters[x-int(i)]
            else:
            
                i = MD5Numbers[charNumber]
                decodedText = decodedText+characters[x-int(i)]
                
        else:
            decodedText = decodedText+char
        
        charNumber = charNumber+1
    


encode(message)

input()
print("Encrypted text:  " + encodedText)
input()
decode(encodedText)
print("Decrypted text:  " + decodedText)
input()