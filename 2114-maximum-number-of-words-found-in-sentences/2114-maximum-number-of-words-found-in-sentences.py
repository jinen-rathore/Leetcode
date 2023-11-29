class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for s in sentences:
            spaces = 0
            for char in s:
                if char == " ":
                    spaces += 1
            max_words = max(max_words, spaces + 1)
        return max_words
#         split_sentences = []
#         for s in sentences:
#             split_sentences.append(s.split(" "))
        
#         max_words = 0
        
#         for s in split_sentences:
#             max_words = max(len(s), max_words)
#         return max_words
