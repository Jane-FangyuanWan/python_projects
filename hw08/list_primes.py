from prime_generator import PrimeGenerator


def main():
    n = int(input("Please input an integer: "))
    prime_gen = PrimeGenerator()
    primes = prime_gen.primes_to_max(n)
    for prime in primes:
        print(prime)


if __name__ == "__main__":
    main()
