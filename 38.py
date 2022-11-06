class Solution:
    def countAndSayRecursive(self, n: int, depth: int, sayString: str) -> str:
        if depth == n:
            return sayString

        return self.countAndSayRecursive(n, depth + 1, self.say(sayString))

    def countAndSay(self, n: int) -> str:
        depth = 1
        return self.countAndSayRecursive(n, depth, "1")

    def countAndSay2(self, n: int) -> str:
        if n == 1:
            return "1"
        sayString = self.countAndSay2(n - 1)
        return self.say(sayString)

    def say(self, s: str):
        count = 1
        res = ""
        for i in range(len(s)):
            if i + 1 >= len(s):
                res += str(count) + s[i]
                break

            if s[i] == s[i + 1]:
                count += 1
            else:
                res += str(count) + s[i]
                count = 1
        return res


s = Solution()
print(s.countAndSay(1))
print(s.countAndSay(2))
print(s.countAndSay(3))
print(s.countAndSay2(4))
# print(s.say("3322251"))
