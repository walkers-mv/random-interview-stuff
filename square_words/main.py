

class Solution:
    def wordSquares(self, words):
        def getPrefixes(prefix):
            if prefix in prefixes:
                return prefixes[prefix]
            prefixes[prefix] = []
            for word in words:
                if word.startswith(prefix):
                    prefixes[prefix].append(word)
            return prefixes[prefix]

        def backtrack(idx, curr):
            nonlocal result
            if len(curr)== len(curr[0]):
                result.append(list(curr))
                return

            prefix = "".join([word[idx] for word in curr])
            for candidate in getPrefixes(prefix):
                curr.append(candidate)
                backtrack(idx+1, curr)
                curr.pop()

        prefixes = {}
        result = []
        for word in words:
            backtrack(1, [word])

        return result
    
word_list = ['ball', 'lady', 'wall', 'area', 'lead']
for ix, solution in enumerate(Solution().wordSquares(word_list)):
    print(f"solution_{ix}")
    print("\n".join(solution))
    print()