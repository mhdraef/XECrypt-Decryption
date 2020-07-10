from collections import Counter

# You can change this value depending on what you know about the text, if its the english alphabet you can keep it as
# 'e' or ' '

character = 'e'

# Loading the File

encryptedText = ""

print("Enter name of encrypted file with extension:")
fname = input()

try:
    with open(fname, "r") as f:
        for line in f.readlines():
            encryptedText += line.rstrip()
except IOError:
    print("Cannot find the specified file")
    exit()

fullSplit = encryptedText.split('.')
fullSplit.remove('')  # Remove the first empty element

# Group three elements and sum them (a character is made up of three elements)

encCharacters = []

for i in range(0, len(fullSplit), 3):

    encCharacter = (fullSplit[i:i+3])
    encCharacter = [int(i) for i in encCharacter]
    encCharacter = sum(encCharacter)
    encCharacters.append(encCharacter)

# Next, we try to figure out the password. We count occurrence of each character. As pointed out by Edgar Allen Poe, the
# letter 'e' is the most common character in the english alphabet. So going by this, we assume that the most common
# character in our encrypted text is 'e'.

count = Counter(encCharacters)

commonChars = [char for char, char_count in count.most_common()]

for i in range(len(commonChars)):

    common = commonChars[i]
    password = common - ord(character)  # You can change this character at the beginning

    decCharacters = [int(x - password) for x in encCharacters]

    if min(decCharacters) < 0 or max(decCharacters) > 127:
        continue

    for char in decCharacters:
        print(chr(char), end='')

    print("\n\nPassword: " + str(password))

    print("\nWould you like to try decrypting again (y/n)?")

    choice = input()

    while choice not in ['y', 'n']:
        choice = input()

    if choice == 'n':
        print("Text successfully decrypted!")
        exit()

print("Not able to decrypt the text, try changing the value of the common character")
