class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        com_dic=dict(Counter(words[0]))
        
        
        for word in words:
            nxt=dict(Counter(word))
            for x in com_dic:
                if x in nxt:
                    com_dic[x]=min(com_dic[x], nxt[x])
                else:
                    com_dic[x]=0
                    
        res=[]
        for x in com_dic:
            res.extend([x]*com_dic[x])
            
        return res
        