class PrimeGenerator:
    def primes_to_max(self, n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        composites = set()
        prime_list = []
        TWO = 2
        for num in range(TWO, n + 1):
            if is_prime[num]:
                prime_list.append(num)
                for multiple in range(num * TWO, n + 1, num):
                    is_prime[multiple] = False
                    composites.add(multiple)
        return prime_list
