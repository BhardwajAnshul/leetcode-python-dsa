class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:    
        if endWord not in wordList:
            return 0
        maps = {}
        for word in [beginWord, *wordList]:
            for i in range(len(word)):
                f_word = word[:i] + ' ' + word[i+1:]
                if f_word not in maps:
                    maps[f_word] = set()
                maps[f_word].add(word)

        maps = {k: v for (k,v) in maps.items() if len(v)>1}
        if not maps:
            return 0
        new_maps = {}
        for (k, v) in maps.items():
            for word in v:
                if word not in new_maps:
                    new_maps[word] = []
                if word!=k:
                    new_maps[word].append(v)

        if endWord not in new_maps:
            return 0

        start = 0
        words = set([beginWord])
        while True:
            new_list = set()
            for w in words:
                lists = new_maps[w]
                for l in lists:
                    new_list.update(set(l))

            if endWord not in new_list:
                start+=1
                words = new_list - words
                if start > len(wordList):
                    return 0
            else:
                break
        return start+2

        