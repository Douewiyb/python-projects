import random

def build_model2(text):
    words = text.split()
    model = {}
    for i in range(len(words)-2):
        key=words[i]+" "+words[i+1]
        if key not in model:
            model[key]=[]
        model[key].append(words[i+2])
    return model

print(build_model2("the cat sat on the mat"))

def generate2(model, w1, w2, max_words):
    sentence = w1 + " " + w2
    for step in range(max_words):
        key = w1 + " " + w2
        if key not in model:
            break
        follower = random.choice(model[key])
        sentence = sentence + " " + follower
        w1 = w2
        w2 = follower
    return sentence

model = build_model2("the cat sat on the mat")
print(generate2(model, "the", "cat", 10))

with open("story.txt") as f:
    text = f.read().lower().replace(",", "").replace(".", "")