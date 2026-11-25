import random

def build_model(text):
    words=text.split()
    model= {}
    for i in range(len(words)-1):
        current=words[i]
        nxt=words[i+1]
        if current not in model:
            model[current]=[]
        model[current].append(nxt)
    return model



def generate(model, start, max_words):
    sentence = start
    word = start
    for step in range(max_words):
        if word not in model:
            break
        word=random.choice(model[word])
        sentence= sentence+" "+word
    return sentence
 
 
with open("story.txt") as f:
    text=f.read().lower().replace(",","").replace(".","")


model= build_model(text)
start=random.choice(list(model))
print(generate(model, start, 15))

print(build_model("the cat sat on the mat"))