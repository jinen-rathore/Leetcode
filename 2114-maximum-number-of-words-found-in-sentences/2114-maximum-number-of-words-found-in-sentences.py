class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        split_sentences = []
        for s in sentences:
            split_sentences.append(s.split(" "))
        
        max_words = 0
        
        for s in split_sentences:
            max_words = max(len(s), max_words)
        return max_words