from cs50 import get_string

#get text input from user
text = get_string("Enter Text:\n")

#Varibles for sentences, word, and letters counter
sen = 0
wrd = 0
ltr = 0

#cycle thru text and count words and sentance and letters
for i in text:
    if i.isalpha():
        ltr += 1
    if i == "." or i == "!" or i == "?":
        sen += 1
    if i.isspace():
        wrd += 1
#Check to see if first char in string is a alpha
if text[0].isalpha():
    wrd += 1

#average number of letters per 100 words
L =   (ltr / wrd) *  100.00
#average number of sentences per 100 words
S =   (sen / wrd) *  100.00

#Coleman-Liau index
RL = (0.0588 * L) - (0.296 * S) - 15.8;
index = round(RL);


#Print results
if index >= 16:
    print("Grade 16+\n");
elif index < 1:
    print("Before Grade 1\n");
else:
    print(f"Grade {index}")