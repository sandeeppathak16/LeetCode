class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        result={}
        
        
        for word in strs:
            key= ''.join(sorted(word))
            if key not in result:
                result[key]=[word]
            else:
                result[key].append(word)
        return result.values()
            