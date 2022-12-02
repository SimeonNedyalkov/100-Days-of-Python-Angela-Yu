alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
morse_code_list=['*-','-***','-*-*','-**','*','**-*','--*','****','**','*---','-*-','*-**','--','-*','---','*--*','--*-','*-*','***','-','**-','***-','*--','-**-','-*--','--**']
your_word = input("Which word you want to convert to morsecode: ")
morse_code = ""

def find_letter():
    global morse_code
    for letter in your_word:
        for _ in alphabet_list:
            if letter == _:
                index = alphabet_list.index(letter)
                print(morse_code_list[index])
find_letter()
