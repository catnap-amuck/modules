import fibo


def hello():
    print("hello")

# print(__name__)

def main():
    fibo.fib(5)

# underscore can be referred to as dunder
# if __name__ == "main":
if __name__ == "__main__":
    main()

# fibo.fib(5)