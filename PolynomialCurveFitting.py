import numpy as np
import matplotlib.pyplot as plt

def predictions(coefficients, exponents, x):
    num = 0
    for i in range(len(exponents)):
        num += coefficients[i] * x ** exponents[i]
    return num

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
x_min = float(input('Enter the minimum x-value on the graph: '))
x_max = float(input('Enter the maximum x-value on the graph: '))
y_min = float(input('Enter the minimum y-value on the graph: '))
y_max = float(input('Enter the maximum y-value on the graph: '))

A = np.zeros((len(x), len(x)))
B = y
for i in range(len(x)):
    for j in range(len(x)):
        A[i][j] = x[i] ** j #Create a matrix that holds the values of x^0, x^1, ..., x^len(x) - 1
coefficients = np.matmul(np.linalg.inv(A), B) #Multiply the matrix by a matrix of the y-values to get coefficients
print('Coefficients Used:', [f'{i:.5f}' for i in coefficients])
exponents = np.array([i for i in range(len(coefficients))])
testing_points = np.arange(x_min, x_max, 0.1) #Create testing points for curve fitting
model = np.array([predictions(coefficients, exponents, point) for point in testing_points]) #Create an array of y-values for the testing points

plt.scatter(x, y, label = 'training points', color = 'r')
plt.plot(testing_points, model, label = 'testing points', color = 'blue', marker = '*')
plt.title('Polynomial Curve Fitting')
plt.xlabel('x-axis')
plt.ylabel('y-asis')
plt.ylim(y_min, y_max)
plt.xlim(x_min, x_max)
plt.grid(True)
plt.legend(loc = 'best')
plt.show()
