'''
269. Alien Dictionary
Hard

2629

515

Add to List

Share
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

 

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
Accepted
212,268
Submissions
624,935
'''
from collections import defaultdict 
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        vocab = set()
        last = words[0]
        vocab.update(last)
        graph = defaultdict(set)
        for i in range(1, len(words)):
            vocab.update(words[i])
            len_c = len(words[i])
            len_l = len(last)
            same = True
            for j in range(min(len_c, len_l)):
                if words[i][j] == last[j]:
                    continue
                else:
                    graph[words[i][j]].add(last[j])
                    same = False
                    break
            if same and len_c < len_l:
                return ""
            last = words[i]
        #print(graph)
        results = []
        states = defaultdict(int)
        valid = True
        def dfs(curr):
            if states[curr] > 0:
                if states[curr] != 2:
                    nonlocal valid
                    valid = False
                return

            states[curr] = 1
            for nxt in graph[curr]:
                dfs(nxt)
            results.append(curr)
            states[curr] = 2
        
        for w in vocab:
            dfs(w)
            if not valid:
                return ""
        if not results:
            return "".join(vocab)
        return "".join(results)
            