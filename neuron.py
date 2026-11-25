import matplotlib.pyplot as plt

v=0
input_current=3
threshold=4
spike=0
v_list=[]

for step in range(20):
    v=v+input_current
    v=v*0.5
    if v >= threshold:
        spike+=1
        v=0.0
    v_list.append(v)

print (v_list)
print (spike)

plt.plot(v_list)
plt.xlabel("time step")
plt.ylabel("voltage")
plt.show()