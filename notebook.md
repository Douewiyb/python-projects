## 2026-11-24
**Tried:** I tried building a simple neuron and running it.
**What happened:** it worked successfully with a voltage, input current, threshold, leak and a spike count.
voltage=0
input current=5
threshold=4
spikes=6
leak=0.5
steps/rounds=20
spike triggered every 3 steps in a 20 step run
**Next:** The next step would be to build a voltage-over-time graph.

**Tried:** I tried building a graph for the firing rate for my neuron.
**What happened:**It was successful and the graph was complete from a input current of 0-10
input currents 0-4: 0 spikes
input currents 5: 6 spikes
input currents 6-7: 10 spikes
input currents 8-10: 20 spikes
The voltage, leak, threshold and steps were all untouched except for the current input obviously.
The graph showed essentially a staircase with sharp upward bumps.
**Next:** The next step would be turning my neuron into a neuron class so two neurons can talk to eachother.