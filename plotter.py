'''
Andy Huang (ECE 160: Plotter)
'''

import matplotlib.pyplot as plt #I didnt instal it yet.

x_values = [] 
_y_values = []  

with open("data.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        try:
            x = float(parts[0])
            y = float(parts[1])
        except ValueError:
            continue
        x_values.append(x)
        _y_values.append(y)

n = len(x_values)
if n == 0:
    exit()


sum_x = 0
sum_y = 0
sum_xy = 0
sum_x2 = 0

for i in range(n):
    sum_x += x_values[i]
    sum_y += _y_values[i]
    sum_xy += x_values[i] * _y_values[i]
    sum_x2 += x_values[i] ** 2

denominator = n * sum_x2 - sum_x ** 2
if denominator == 0:
    exit()

m = (n * sum_xy - sum_x * sum_y) / denominator
b = (sum_y - m * sum_x) / n

print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")


plt.plot(x_values, _y_values, 'bo-', label='data')  

line_y = []
for x in x_values:
    line_y.append(m * x + b)

plt.plot(x_values, line_y, 'r-', label='best fit') 

plt.xlabel('x (Time (s))')
plt.ylabel('y (Measurement)')
plt.title('Best fit line.')
plt.legend()
plt.grid(True)
plt.show()
