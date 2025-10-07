class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for i in magazine:
            letters[i] = 1 if letters.get(i) is None else letters[i] + 1

        for i in ransomNote:
            if letters.get(i, 0) > 0:
                letters[i] -= 1
            else:
                return False
        return True
