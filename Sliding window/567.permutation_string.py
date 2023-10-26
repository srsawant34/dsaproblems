class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cache = {}
        for c in s1:
            if c in cache:
                cache[c]+=1
            else:
                cache[c]=1
        flag=0
        cachebkp = cache.copy()
        for c in s2:
            if c not in cache:
                if sum(cache.values())==0:
                    return True
                if flag==0:
                    continue
                else:
                    cache = cachebkp.copy()
            else:
                if cache[c]!=0:
                    print(cache,c)
                    cache[c]-=1
                flag=1

        for key,val in cache.items():
            if val:
                return False
        return True

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26