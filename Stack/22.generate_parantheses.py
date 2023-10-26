class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        soln = []
        
        def gen(opened, canopen, canclose, paran):
            if opened==0 and canopen==0 and canclose==0:
                soln.append(paran)
                return
            if canclose==0:
                return
            
            if opened:
                if canopen:
                    gen(opened+1,canopen-1,canclose,paran+'(')
                if canclose:
                    gen(opened-1,canopen,canclose-1,paran+')')
            else:
                if canopen:
                    gen(opened+1,canopen-1,canclose,paran+'(')
                    
        gen(0,n,n,'')
        return soln