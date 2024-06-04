import collections


class Solution:
    def ladderLength(self, beginword, endword, wordlist):
        if endword not in wordlist:
            return 0
        
        neighbors = collections.defaultdict(list)
        wordlist.append(beginword)
        for word in wordlist:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbors[pattern].append(word)
        
        visited = set([beginword])
        q = collections.deque([beginword])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endword:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiword in neighbors[pattern]:
                        if neiword not in visited:
                            visited.add(neiword)
                            q.append(neiword)
            res += 1
        return 0

bword = 'hit'
eword = 'cog'
wordlist = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

print(Solution().ladderLength(bword, eword, wordlist))

