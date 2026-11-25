import matplotlib.pyplot as plt

def count_spikes(input_current):
    v=0
    threshold=4
    spike=0
    for step in range(20):
        v=v+input_current
        v=v*0.5
        if v >= threshold:
            spike+=1
            v=0.0
    return spike


counts=[]
currents=[0,1,2,3,4,5,6,7,8,9,10]

for current in currents:
    i=count_spikes(current)
    counts.append(i)

print(counts)

plt.plot(currents,counts)
plt.xlabel("currents")
plt.ylabel("firing rate")
plt.show()
