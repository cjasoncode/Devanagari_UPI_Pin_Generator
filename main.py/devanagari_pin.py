import regex as re
import time

def break_hindi_word(word):
    return re.findall(r'\X', word)  

time.sleep(2)
print("\n\n                   **************   WELCOME TO DEVANAGARI UPI PIN GENERATOR   **************\n\n")

def get_devanagari_number(char):
    if char == 'अ':
        return '31'
    elif char == 'आ':
        return '311'
    elif char == 'इ':
        return '5'
    elif char == 'ई':
        return '5'
    elif char == 'उ':
        return '3'
    elif char == 'ऊ':
        return '3'
    elif char == 'ए':
        return '1'
    elif char == 'ऐ':
        return '1'
    elif char == 'ओ':
        return '311'
    elif char == 'औ':
        return '311'
    elif char == 'क':
        return '9'
    elif char == 'ख':
        return '21'
    elif char == 'ग':
        return '1'
    elif char == 'घ':
        return '1'
    elif char == 'ङ':
        return '5'
    elif char == 'च':
        return '1'
    elif char == 'छ':
        return '8'
    elif char == 'ज':
        return '1'
    elif char == 'झ':
        return '51'
    elif char == 'ञ':
        return '01'
    elif char == 'ठ':
        return '0'
    elif char == 'ड':
        return '5'
    elif char == 'ढ':
        return '6'
    elif char == 'ण':
        return '01'
    elif char == 'त':
        return '7'
    elif char == 'थ':
        return '1'
    elif char == 'द':
        return '6'
    elif char == 'ध':
        return '1'
    elif char == 'न':
        return '7'
    elif char == 'प':
        return '4'
    elif char == 'फ':
        return '4'
    elif char == 'ब':
        return '9'
    elif char == 'भ':
        return '4'
    elif char == 'म':
        return '4'
    elif char == 'य':
        return '4'
    elif char == 'र':
        return '2'
    elif char == 'ल':
        return '1'
    elif char == 'व':
        return '9'
    elif char == 'श':
        return '21'
    elif char == 'ष':
        return '4'
    elif char == 'स':
        return '21'
    elif char == 'ह':
        return '5'
    elif char == 'ा':
        return '1'
    elif char == 'ि':
        return '1'
    elif char == 'ी':
        return '1'
    elif char == 'ो':
        return '1'
    elif char == 'ौ':
        return '1'
    elif char == 'ू':
        return '9'
    elif char =='ु':
        return '6'
    else:
        return None
 

allowed_matras = {'ा', 'ि', 'ी', 'ो', 'ौ','ु','ू'}

def process_word(word):
    number_representation = []
    unrecognized_characters = []

    for char in word:
        num = get_devanagari_number(char)
        if num:
            number_representation.append(num)
         
   
    for char in unrecognized_characters:
        print(f"{char}")

    return number_representation


time.sleep(2)
hindi_word = input("Enter a word in Devanagari ( उदाहरण : भारद्वाज , पर्व  ) :   ")
 
time.sleep(1.5)
if hindi_word.isdigit():
    print("\nError : Invalid Input. Please Enter Devanagari Word \n")
    exit()

elif hindi_word.isalpha():
    print("\nError : Invalid Input. Please Enter Devanagari Word \n")
    exit()

elif hindi_word.isascii():      
    print("\nError : Invalid Input. Please Enter Devanagari Word \n")
    exit()

else:
 

 characters = break_hindi_word(hindi_word)
 result = process_word(hindi_word)
 pin = "".join(result)



 characters = [char for char in hindi_word if char in allowed_matras or ('अ' <= char <= 'ह')]
 time.sleep(2)
 print(f"\nWord Sepration : {"   ".join(characters)}\n")
 print( "                  "+  "   ".join(result)+"\n")
 
 if   len(pin)==3:
      condition = pin*2
      time.sleep(2)
      print(f"\nYOUR DEVANAGARI UPI 6 DIGITS PIN IS HERE : {condition}\n")
      print(f"YOUR DEVANAGARI UPI 4 DIGITS PIN IS HERE : {condition[0:4]}\n\n")  
      
     
 else:    
      time.sleep(2)
      print(f"YOUR DEVANAGARI UPI 4 DIGITS PIN IS HERE : {pin[0:4]}\n")
      print(f"YOUR DEVANAGARI UPI 6 DIGITS PIN IS HERE : {pin[0:6]}\n\n")