"""



"""
def main():
    DecodeWord()




# Your code goes here.

def DecodeWord():

    word = ""
    #variable word para que sea una nueva palabra la que se imprima al final.

    #encodedWord = "WBLARF8TTS"
    #encodedWord = "L8KAOUL"
    encodedWord = "E8N8N8"
    # encodedWord = "8TRA8DY T8LA"
    # encodedWord = "8TT LHA TILLTA LIMAS"
    # encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
    # encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"

    # encodedWord = "UUHO"  		#Used for Bonus
    # encodedWord = "EOUUUUOUU" 	#Used for Bonus
    for letter in encodedWord:
        if letter == "L":

            word = word + "T"
        #Usar word y add la letra correcta a la palabra
        elif letter == "T":
            word = word + "L"
        elif letter == "8":
            word = word + "A"
            #print("A")
        elif letter == "B":
            word = word +"A"
            #print("A")
        elif letter == "A":
            word = word+"E"
            #print("E")
        elif letter == "E":
            word = word+"B"
            #print("B")
        else:
            #print(letter)
            word = word + letter

    print(word)
    #imprimir la nueva palabra con las letras correctas. 




#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.
if __name__ == "__main__":
	main()
