
import time

class TrieNode:
    def __init__(self, value = None) -> None:
        self.value = value
        self.child = {}
        self.eos = False

class SolutionTrietree:
    def __init__(self) -> None:
        self.root = TrieNode()
        self.buffer = []

    def insertion(self, word) -> None:
        currNode = self.root

        for i in range(len(word)):
            character = word[i]
            if currNode.eos:
                self.buffer.append((word, word[i:]))
            if character not in currNode.child:
                currNode.child[character] = TrieNode(character)
            currNode = currNode.child[character]
        currNode.eos = True

    def is_compounded(self, record) -> bool:
        currNode = self.root
        temp = []
        suffix = record[1]
        for i in range(len(suffix)):
            character = suffix[i]
            if currNode.eos:
                temp.append((record[0], suffix[i:]))
            if character not in currNode.child:
                self.buffer.extend(temp)
                return False
            currNode = currNode.child[character]
        if not currNode.eos:
            self.buffer.extend(temp)
        return currNode.eos

    def longest_compounded_word(self) -> tuple:
        longest, second_longest = '', ''
        for record in self.buffer:
            if ((len(record[0]) > len(second_longest)) and self.is_compounded(record)):
                if (len(longest) < len(record[0])):
                    longest, second_longest = record[0], longest
                else:
                    second_longest = record[0]
        return (longest, second_longest)
   

if __name__ == '__main__':
    begin = time.time()
    trie = SolutionTrietree()
    with open('path/to/input/file.txt') as f:
        for line in f.readlines():
            trie.insertion(line.strip())
    longest, second_longest = trie.longest_compounded_word()
    end = time.time()
    print('Longest Compounded Word: ', longest)
    print('Second Longest Compounded Word: ', second_longest)
    print(f'Execution time: {(end - begin)*1000} milliseconds')
