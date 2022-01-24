class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        list_map = map(str, num) 
        new_num=''
        new_num = new_num.join(list_map)
        new_num = int(new_num)
        new_num +=k
        
        new_list = [int(c) for c in str(new_num)]
        
        return new_list
        