from LinearEquation import LinearEquation


def main():
    a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

    linear_expr = LinearEquation(a, b, c, d, e, f)
    if linear_expr.is_solvable():
        print("x is", linear_expr.get_x(), "and y is", linear_expr.get_y())
    else:
        print("The equation has no solution")


main()
