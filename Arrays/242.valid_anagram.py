class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        if len(s)!=len(t):
            return False
        for c in s:
            if c in smap:
                smap[c]+=1
            else:
                smap[c]=1
        for c in t:
            if c in smap:
                if smap[c]==0:
                    return False
                smap[c]-=1
            else:
                return False
        if sum(smap.values())==0:
            return True
        return False