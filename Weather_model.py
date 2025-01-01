def weathering_model():
    with open('input1.txt', 'r') as file:
        lines = file.readlines()
        a = float(lines[0])
        b = float(lines[1])
        c = float(lines[2])
        x = float(lines[3])

    y = a * x**2 + b * x + c
    print("\nVersion 3\n")
    print("Quadratic Weather Model")
    print(f"Equation: y={a}x^2+{b}x={c}")
    print(f"Prediction for x={x}: y={y}\n")

weathering_model()