def main():
    hello()

    # Ask user for their name then Remove whitespace from str then capitalize user's name
    name = input("What's your name? ").strip().title()

    hello(name)

    # Say Hello to user
    # print(name)


def hello(to="world"):
    print("Hello,", to)

main()
