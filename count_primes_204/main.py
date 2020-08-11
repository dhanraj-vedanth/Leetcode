class Solution:
    def countPrimes(self, n: int) -> int:
        """
        For each number less than n
        - Iterate from 2 to n/2 
        - If any of those numbers can divide n -> not prime
        - Else prime
        This exceeds time limit though
        # result = []
        # count = 0
        # for each_number in range(n):
        #     if each_number > 1:
        #         for test_number in range(2, each_number):
        #             if (each_number % test_number == 0):
        #                 break
        #         else:
        #             count += 1 
        # return count
        Sieve of Eratosthenes method
        very intuitive!
        """
        res = 0
        primes = [True] * (n)
        primes[0] = primes[1] = False
        prime_num = 2
        while(prime_num * prime_num <= n):
            if primes[prime_num] is True:
                for each_num in range(prime_num*2, n, prime_num):
                    primes[each_num] = False
            prime_num += 1
        for each in primes:
            if each:
                res += 1
        return res

