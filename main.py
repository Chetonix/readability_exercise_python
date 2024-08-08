with open("./data/text1.txt", "r") as f:
    text = f.read()

words = len(text.split())
sentences = text.count('.') + text.count('!') + text.count('?')
letters = 0
for letter in text:
    if letter.isalpha():
        letters += 1

L = (letters / words) * 100
S = (sentences / words) * 100

X = round(0.0588 * L - 0.296 * S - 15.8)

#print(X)

if(X < 1):
    print("Before Grade 1");
elif (X >= 16):
    print("Grade 16+");
else:
    print("Grade", X);