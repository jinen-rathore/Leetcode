class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        
        # checking is str1 prefix and suffix both of str2 by using string slicing
        def isPrefixAndSuffix(str1, str2):
            return (str1 == str2[:len(str1)] and str1 == str2[-len(str1):])
        
        # iterating over the list words and checking each combination for isPrefixAndSuffix
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count
                