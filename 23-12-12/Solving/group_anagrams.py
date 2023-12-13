# https://leetcode.com/problems/group-anagrams/
from typing import List


class solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for word in strs:
            s = ''.join(sorted(word))
            if s in a:
                a[s].append(word)
            else:
                a[s] = [word]
        result = list(a.values())
        return result


s1 = solution()
print(s1.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
