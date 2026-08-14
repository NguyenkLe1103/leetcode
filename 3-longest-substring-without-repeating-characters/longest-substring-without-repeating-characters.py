class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        longest= 0
        current_length = 0
        for right in range (len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])

            current_length = right - left + 1

            if current_length > longest:
                longest = current_length
        return longest
