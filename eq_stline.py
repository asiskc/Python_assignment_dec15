def solve_for_y(x_values):
    m, c = 45, 0.5

    for x in x_values:
        y = m*x + c
        print("Value of y for m = 45, c = 0.5 and x = {:.2f} is {:.2f}.".format(x, y))


x_value = [1, 2.3, 5.6, 7, 78]
solve_for_y(x_value)