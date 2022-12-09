class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # creating a empty dictionary for storting the keys and values
        d = {}
        # for every element present in strs
        for i in strs:
            # sorting the element values and making it string for comparision
            sorted_str = str(sorted(i))
            
            # if sorted string in dictionary then append the values to the dictionary
            if sorted_str in d:
                d[sorted_str].append(i)
            # else add the values as key value pairs in form of list
            else:
                d[sorted_str] = [i]
        # return the values as list
        return list(d.values())
            