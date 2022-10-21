def main():
    x = float(input("What's x? "))
    y = float(input("What's z? "))

    z = round(x + y)

    print("The addition of x and y is " f"{z:,}")
    print ("x squared is", square(x))

def square(n):
    # return n ** 2
    return pow(n, 2)

if __name__ == "__main__":
    main()

