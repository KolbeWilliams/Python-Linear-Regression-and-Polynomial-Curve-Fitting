import numpy as np
import matplotlib.pyplot as plt

def get_values(label):
    values = []
    print(f'Enter {label} values for data and enter "done" when finished:')
    while True:
        user_input = input(f'Enter a {label} value: ')
        if user_input.lower().strip() == 'done':
            break
        try:
            values.append(float(user_input))
        except ValueError:
            print('Invalid input, please enter a numeric value or "done".')
    return values

x_values = get_values('x')
y_values = get_values('y')
x = np.array(x_values)
y = np.array(y_values)
try:
    slope_range_min = float(input('Enter the minimum value you want to test for the slope of the regression line: '))
    slope_range_max = float(input('Enter the maximum value you want to test for the slope of the regression line: '))
    slope_range_step = float(input('Enter the step for the slopes that you want to test: '))
    intercept_range_min = float(input('Enter the minimum value you want to test for the intercept of the regression line: '))
    intercept_range_max = float(input('Enter the maximum value you want to test for the intercept of the regression line: '))
    intercept_range_step = float(input('Enter the step for the intercepts that you want to test: '))
    if slope_range_step <= 0 or intercept_range_step <= 0:
        raise ValueError("Step sizes must be positive.")
except ValueError as e:
    print(f'Error: {e}')
    exit(1)

slopes = np.arange(slope_range_min, slope_range_max, slope_range_step)
intercepts = np.arange(intercept_range_min, intercept_range_max, intercept_range_step)
X, Y = np.meshgrid(slopes, intercepts) #Create Slope and Intercept arrays
Z = np.zeros(X.shape) #Initialize SSE array
for i in range(X.shape[0]): #Iterate through slopes
    for j in range(X.shape[1]): #Interate through intercepts
        model = X[i, j] * x + Y[i, j] #Create a model foe each slope, intercept pair
        sse = np.sum((model - y) ** 2) #Calculate SSE for each model
        Z[i, j] = sse #add each SSE to the SSE array
smallest_error = 1000000
for i in range(len(Z[0])):
    for j in range(len(Z[1])):
        if Z[i][j] < smallest_error:
            smallest_error = Z[i][j]
            best_slope = X[i][j]
            best_intercept = Y[i][j]
best_model = best_slope * x + best_intercept
print(f'The linear regression line for this set of data is: y = {best_slope:.2f}x + {best_intercept:.2f}')

fig = plt.figure() #Creates a figure for the 3D subplot
ax = fig.add_subplot(121, projection = '3d') #Create a 3D subplot
ax.plot_surface(X, Y, Z, cmap = 'viridis', alpha = 0.75) #Plot the graph
ax.scatter(best_slope, best_intercept, smallest_error, label = f'SSE = {smallest_error}\nŷ={best_slope:.2f}{best_intercept:.2f}', color = 'r')
ax.set_title('3D surface plot of SSE as a function of m and b')
ax.set_xlabel('X axis (slope)')
ax.set_ylabel('Y axis (y-Intercept)')
ax.set_zlabel('SSE')
ax.legend()
bx = fig.add_subplot(122) #Create a 2D subplot for best model
bx.scatter(x, y, label = 'Data Points', color = 'r') #Plot data points
bx.plot(x, best_model, label = f'y = {best_slope:.2f}x+{best_intercept:.2f}', color = 'b') #Plot regression line
bx.grid(True)
bx.set_title('Best Regression Line Found')
bx.set_xlabel('x-axis')
bx.set_ylabel('y-axis')
bx.legend(loc = 'best')
plt.tight_layout()
plt.show()