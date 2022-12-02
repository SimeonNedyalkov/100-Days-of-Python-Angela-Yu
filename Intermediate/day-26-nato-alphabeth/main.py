import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")
go1 = True

new_dict = {row["letter"]:row["code"] for (index, row) in df.iterrows()}
def gen_phonetic():
    ask = input("Type a name: ").upper()
    try:
        nato = [new_dict[letter] for letter in ask]

    except KeyError:
        while KeyError:
                print("Sorry, only letters in the alphabet please!")
                gen_phonetic()
    else:
        print(nato)
gen_phonetic()


