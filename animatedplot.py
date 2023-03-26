"""
Model: GPT4
Prompt: 
Can you generate a pyplot for the following data: x = [1, 3, 5, 6, 8], y1 = [2, 3, 5, 18, 1], y2 = [3, 5, 6, 8, 1], y3 =
[5, 1, 2, 3, 4], y4 = [9, 7, 2, 3, 1]. I want y1, y2 to be in the same plot, but y3 is in another plot next to that plot, y4 is in
below. I want the legend of y1 to be ”bob”, y2 to be ”alice”, y3 to be ”bilbo”, y4 to be ”allie”. I want the x-axis to be
labeled with ”time” and y axis to be labeled with ”money”. I want to add a 10 %-40% random error bar to each curve,
through all times (including non-integers). I want smoothed curves to show the plot, and smoothed error bar. Do not
use linear interpolation, use smooth interpolation! I want to also add some small zig-zag to the smoothed curve to make
it look more real. I want to put a baseline as the mean of each line. I want to put a pie chart below indicating the
fraction of the four people in each time step. I also want an animation to show how the fractions are changing in the
pie chart in **continuous time**. Interpolate the missing fractions! I also want vertical line animation in other three
plots to match the pie chart. I want the fanciest plot. Please add as many fancy things as possible.
Here is a possible code to generate a pyplot for the following data, with some comments to explain the steps:
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.interpolate import make_interp_spline

print('please be patient - this takes a while to render')

# Data
x = [1, 3, 5, 6, 8]
y1 = [2, 3, 5, 18, 1]
y2 = [3, 5, 6, 8, 1]
y3 = [5, 1, 2, 3, 4]
y4 = [9, 7, 2, 3, 1]

# Interpolation for smooth curves
x_smooth = np.linspace(min(x), max(x), 300)
spl1 = make_interp_spline(x, y1, k=3)
spl2 = make_interp_spline(x, y2, k=3)
spl3 = make_interp_spline(x, y3, k=3)
spl4 = make_interp_spline(x, y4, k=3)
y1_smooth = spl1(x_smooth)
y2_smooth = spl2(x_smooth)
y3_smooth = spl3(x_smooth)
y4_smooth = spl4(x_smooth)

# Random error
error1 = np.random.uniform(0.1, 0.4, len(y1_smooth)) * y1_smooth
error2 = np.random.uniform(0.1, 0.4, len(y2_smooth)) * y2_smooth
error3 = np.random.uniform(0.1, 0.4, len(y3_smooth)) * y3_smooth
error4 = np.random.uniform(0.1, 0.4, len(y4_smooth)) * y4_smooth

# Baselines
baseline1 = np.mean(y1)
baseline2 = np.mean(y2)
baseline3 = np.mean(y3)
baseline4 = np.mean(y4)

# Create subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))


# Plot y1 and y2 in the first subplot
ax1.plot(x_smooth, y1_smooth, label="bob")
ax1.plot(x_smooth, y2_smooth, label="alice")
ax1.fill_between(x_smooth, y1_smooth - error1, y1_smooth + error1, alpha=0.2)
ax1.fill_between(x_smooth, y2_smooth - error2, y2_smooth + error2, alpha=0.2)
ax1.axhline(baseline1, linestyle='--', color='blue', alpha=0.5)
ax1.axhline(baseline2, linestyle='--', color='orange', alpha=0.5)
ax1.set_xlabel("time")
ax1.set_ylabel("money")
ax1.legend()

# Plot y3 in the second subplot
ax2.plot(x_smooth, y3_smooth, label="bilbo", color="green")
ax2.fill_between(x_smooth, y3_smooth - error3, y3_smooth + error3, color="green", alpha=0.2)
ax2.axhline(baseline3, linestyle='--', color='green', alpha=0.5)

ax2.set_xlabel("time")
ax2.set_ylabel("money")
ax2.legend()

# Plot y4 in the third subplot
ax3.plot(x_smooth, y4_smooth, label="allie", color="red")
ax3.fill_between(x_smooth, y4_smooth - error4, y4_smooth + error4, color="red", alpha=0.2)
ax3.axhline(baseline4, linestyle='--', color='red', alpha=0.5)
ax3.set_xlabel("time")
ax3.set_ylabel("money")
ax3.legend()

# Pie chart function
def update_pie(num):
    ax4.clear()
    fractions = [y1_smooth[num], y2_smooth[num], y3_smooth[num], y4_smooth[num]]
    ax4.pie(fractions, labels=["bob", "alice", "bilbo", "allie"], autopct="%1.1f%%")
    ax4.set_title("Fractions at time {:.2f}".format(x_smooth[num]))

# Initialize pie chart
update_pie(0)

# Animation function
def update(num):
	update_pie(num)
	for ax in (ax1, ax2, ax3):
		for line in ax.lines:
			if line.get_linestyle() == ":":
				line.remove()
		ax.axvline(x_smooth[num], linestyle=':', color='black', alpha=0.5)

# Create animation
ani = FuncAnimation(fig, update, frames=len(x_smooth), interval=50, blit=False)

# Show the plot
plt.tight_layout()
plt.show()


