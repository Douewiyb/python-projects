import random
text = "the cat sat on the mat and the dog sat on the rug"
words = text.split()

model = {}
for i in range(len(words) - 1):
    current = words[i]
    nxt = words[i + 1]
    if current not in model:
        model[current] = []
    model[current].append(nxt)

model["rug"]=["<END>"]

word = "on"
sentence = word

for step in range(10):
    followers = model[word]
    word = random.choice(followers)
    if word =="<END>":
        break
    sentence = sentence + " " + word

print(sentence)
