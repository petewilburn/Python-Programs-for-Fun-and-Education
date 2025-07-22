# LeetCode 5. Longest Palindromic Substring - Optimized Solutions

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Main optimized solution using center expansion.
        Time: O(n²), Space: O(1).
        """
        if not s:
            return ""
        
        start = 0
        max_len = 1
        
        def expand(l: int, r: int) -> int:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        for i in range(len(s)):
            len1 = expand(i, i)      # odd length
            len2 = expand(i, i + 1)  # even length
            cur_max = max(len1, len2)
            
            if cur_max > max_len:
                max_len = cur_max
                start = i - (cur_max - 1) // 2
        
        return s[start:start + max_len]

class SolutionCompact:
    def longestPalindrome(self, s: str) -> str:
        """
        Ultra-compact solution with minimal variable names.
        Time: O(n²), Space: O(1).
        """
        if not s: return ""
        st, ml = 0, 1
        def ex(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]: l, r = l-1, r+1
            return r - l - 1
        for i in range(len(s)):
            cm = max(ex(i, i), ex(i, i+1))
            if cm > ml: st, ml = i - (cm-1)//2, cm
        return s[st:st+ml]

class SolutionDP:
    def longestPalindrome(self, s: str) -> str:
        """
        Alternative using dynamic programming approach.
        Time: O(n²), Space: O(n²).
        """
        n = len(s)
        if n < 2:
            return s
        
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1
        
        # Single characters are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Check for 2-character palindromes
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2
        
        # Check for palindromes of length 3 and more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_len = length
        
        return s[start:start + max_len]

# Test cases for verification
if __name__ == "__main__":
    solutions = [Solution(), SolutionCompact(), SolutionDP()]
    test_cases = [
        ("babad", ["bab", "aba"]),  # Multiple valid answers
        ("cbbd", ["bb"]),
        ("racecar", ["racecar"]),
        ("a", ["a"]),
        ("ac", ["a", "c"])
    ]
    
    for sol in solutions:
        print(f"\nTesting {sol.__class__.__name__}:")
        for s, expected in test_cases:
            result = sol.longestPalindrome(s)
            status = "✓" if result in expected else "✗"
            print(f"  {status} '{s}' → '{result}' (expected one of {expected})")
