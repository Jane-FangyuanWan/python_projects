from prime_generator import PrimeGenerator


def test_primes_to_max():
    prime_gen = PrimeGenerator()
    primes = prime_gen.primes_to_max(20)

    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19]

    for prime in expected_primes:
        assert prime in primes
