# LeetCode 3. Longest Substring Without Repeating Characters - Optimized Solutions

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Main optimized solution using sliding window with hashmap.
        Time: O(n), Space: O(min(m,n)) where m is charset size.
        """
        char_map = {}
        max_len = start = 0
        
        for i, char in enumerate(s):
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            char_map[char] = i
            max_len = max(max_len, i - start + 1)
        
        return max_len

class SolutionCompact:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Ultra-compact solution with minimal variable names.
        Time: O(n), Space: O(min(m,n)).
        """
        d, m, l = {}, 0, 0
        for r, c in enumerate(s):
            if c in d and d[c] >= l:
                l = d[c] + 1
            d[c] = r
            m = max(m, r - l + 1)
        return m

class SolutionSet:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Alternative using set for character tracking.
        Time: O(n), Space: O(min(m,n)).
        """
        chars = set()
        l = max_len = 0
        
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            max_len = max(max_len, r - l + 1)
        
        return max_len

# Test cases for verification
if __name__ == "__main__":
    solutions = [Solution(), SolutionCompact(), SolutionSet()]
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("au", 2)
    ]
    
    for sol in solutions:
        print(f"\nTesting {sol.__class__.__name__}:")
        for s, expected in test_cases:
            result = sol.lengthOfLongestSubstring(s)
            status = "✓" if result == expected else "✗"
            print(f"  {status} '{s}' → {result} (expected {expected})")
