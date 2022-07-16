class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        for i in range(len(s)):
            if (s[i] == "(") or (s[i] == "[") or (s[i] == "{"):
                q.append(s[i])
            elif not q:
                return False
            else:
                char = q.pop()
                if (s[i] == ")" and char != "(") or (s[i] == "}" and char != "{") or (s[i] == "]" and char != "["):
                    return False
        return len(q) == 0
