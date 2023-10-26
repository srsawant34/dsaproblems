class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapp = {}
        soln = -1
        maxF = ['',-1]
        
        n = len(s)
        left,right = 0,1
        mapp[s[0]]=1
        while left<right and right<n:
            mapp[s[right]] = 1 + mapp.get(s[right],0)
            if maxF[1]<mapp[s[right]]:
                maxF = [s[right], mapp[s[right]]]
            
            while (right-left+1) - maxF[1]> k:
                mapp[s[left]]-=1
                left+=1
            
            soln = max(soln, right-left+1)
            right+=1
        return soln