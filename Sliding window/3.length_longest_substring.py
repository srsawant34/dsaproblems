class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        mx = 0
        cache = set()
        for i in range(len(s)):
            while s[i] in cache:
                cache.remove(s[l])
                l+=1
            cache.add(s[i])
            mx = max(mx,i-l+1)
        return mx