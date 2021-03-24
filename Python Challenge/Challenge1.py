#http://www.pythonchallenge.com/pc/def/map.html
import string

def Ceasar_Cypher(Input_String, Shift):
    Input_String = str(Input_String.upper())
    Output_String = ""
    for i in range(0, len(Input_String)):
        if (ord(Input_String[i]) < 91) and (ord(Input_String[i]) > 64):
            Current_Character = ord(Input_String[i])
            if Current_Character == 91-Shift:
                Current_Character = 61+Shift
            Current_Character += Shift
            Output_String += chr(Current_Character)
        else:
            Output_String += Input_String[i]
    return Output_String

def Alphabet_Shift(Shift):
    String = "abcdefghijklmnopqrstuvwxyz"
    Temp = 0
    New_String = ""
    for i in range(0,26):
        if (ord(String[i])+ Shift) > 122:
            Temp = ord(String[i]) - 26
        else:
            Temp = ord(String[i])
        New_String += chr(Temp + Shift)
    return New_String

def Ceasar_Cypher_MakeTrans(Input_String,Shift):
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz", Alphabet_Shift(Shift))
    print(Input_String.translate(table))

def Run():
    shift = int(input("What is the key:"))
    Ceasar_Cypher_MakeTrans(input("Input jumbled text: "), shift)