
class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        self._insert(word, 0, self.trie)
        #print(self.trie)
        
    def _insert(self, word, i, trie):
        if word[i] not in trie:
            trie[word[i]] = {}
        if i == len(word) -1:
            if '*' not in trie[word[i]]:
                trie[word[i]]['*'] = '*'
        else:
            self._insert(word, i + 1, trie[word[i]])


    def search(self, word):
        return self._search(word, 0, self.trie)
    
    def _search(self, word, i, trie):
        if word[i] not in trie:
            return False
        if i == len(word) - 1:
            
            if word[i] in trie and '*' in trie[word[i]]:
                return True
            else:
                return False
        else:
            return self._search(word, i + 1, trie[word[i]])
            

    def startsWith(self, prefix):
        return self._startsWith(prefix, 0, self.trie)
        
    def _startsWith(self, word, i, trie):
        if word[i] not in trie:
            return False
        if i == len(word) - 1:
            if word[i] in trie:
                return True
            else:
                return False
        else:
            return self._startsWith(word, i + 1, trie[word[i]])
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)