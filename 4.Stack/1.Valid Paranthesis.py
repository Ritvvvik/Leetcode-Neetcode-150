class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        valid = {'(':')',
                 '[':']',
                 '{':'}'}
        for ch in s:
            if ch in valid:
                stk.append(ch)
            else:
                if not stk: # if stack has no elements then False
                    return False
                top = stk.pop()

                if valid[top] != ch:  #'(' != ')'
                    return False
        
        return len(stk) == 0  #boolean expression that gives True or False