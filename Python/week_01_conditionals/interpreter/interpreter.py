def main():
    expression()

def expression():
    e = input("What is the expression? Format it as x y z : ")
    x, y, z = e.split(" ")

    if y == "/" and z == "0":
        print("There is no division by zero! Try again 😥 ")
    else:
        r = result(x, y, z)
        print(f"{r:.1f}")

def result(x, y, z):
    return eval(f"{x} {y} {z}")

if __name__ == "__main__":
    main()