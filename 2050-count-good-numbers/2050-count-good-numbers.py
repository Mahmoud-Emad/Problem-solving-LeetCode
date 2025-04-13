class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def mod_pow(base, exponent):
            result = 1
            while exponent > 0:
                if exponent % 2 == 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exponent //= 2
            return result
        
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        
        return (mod_pow(5, even_positions) * mod_pow(4, odd_positions)) % MOD
