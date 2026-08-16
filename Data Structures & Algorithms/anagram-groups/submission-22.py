class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            temp = [1] * 26
            for a in word:
                temp[ord(a) - ord('a')]+=1
            d[tuple(temp)].append(word)
        return list(d.values())