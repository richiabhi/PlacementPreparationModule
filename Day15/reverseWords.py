import collections


class Solution:
    def reverseWords(self, string1: str) -> str:
        string1 = string1.strip()
        x = collections.deque()

        [x.appendleft(i) for i in string1.split()]
        reversed_string2 = " ".join(x)

        return reversed_string2
