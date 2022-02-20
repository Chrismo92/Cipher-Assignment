import string
def encrypt(message , key, outputf):
     dictionary =  {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
     encrypted=''
     text=message.lower() # first covert the message to lower case
     for key in dictionary: # iterate over each letter in the message
        if   in string.ascii_lowercase: # only if the letter is an alphabet we encrypt
            ascii=ord(letter)+key # add the key to the ascii value
            if ascii>122: # if the ascii value is greater than that of 'z' we rotate
                encrypted+=chr(ascii-122+96)
            else:
                encrypted+=chr(ascii) # if the ascii value is less than 'z' we simply covert it to alphabet
        else:
            encrypted+=letter # else we keep it as it is

     return encrypted