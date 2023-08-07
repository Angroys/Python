import string

def climbStairs( n: int) -> int:
        memo = {}
        return helper(n, memo)
    
def helper(n: int, memo: dict[int, int]) -> int:
    if n == 0 or n == 1:
        return 1
    if n not in memo:
        memo[n] = helper(n-1, memo) + helper(n-2, memo)
    return memo[n]

def isPalindromeString(s: str) -> bool:
        
        all_symbols = list(string.printable)
        symbols_only = [symbol for symbol in all_symbols if not symbol.isalnum() and not symbol.isspace()]
        symbols_only.append(" ")

        for i in symbols_only:
            s = s.replace(i, "")

        return s.lower() == s[::-1].lower()

isPalindromeString("A man, a plan, a canal: Panama")