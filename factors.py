import sys


def factorize(n):
    factors = []
    for i in range(2, n//2 + 1):
        if n % i == 0:
            factors.append((i, n//i))
            break
    return factors


def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            num = int(line.strip())
            factors = factorize(num)
            p, q = factors[0]
            print("{}={}*{}".format(num, p, q))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit(1)
    main(sys.argv[1])
