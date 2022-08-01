counter = 0
characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

open_file = open("wordList.txt", "w")

for i in characters:
    for j in characters:
        for k in characters:
            for l in characters:
                guess = f"{i}{j}{k}{l}"
                open_file.write(guess)
                open_file.write("\n")
                counter+=1

print(f"WordList of {counter} password created")
                


