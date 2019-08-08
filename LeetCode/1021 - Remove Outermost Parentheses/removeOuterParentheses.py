class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        outermost = None
        length = len(S)
        i = 0
        cur = []
        stack = []
        while i < length:
            if S[i] == "(":
                stack.append("(")
                if len(stack) > 1:
                    cur.append("(")

            else:
                stack.pop()
                if len(stack) > 0 :
                    cur.append(")")
                
            i += 1
        return "".join(cur)