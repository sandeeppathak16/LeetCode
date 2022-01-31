class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s_list = list(s.split(' '))
        num_list = []
        print(s_list)
        
        res = True
        
        for letter in s_list:
            if letter.isdigit():
                num_list.append(int(letter))
        
        print(num_list)
                
                
        for i in range(len(num_list)-1):
            if num_list[i]<num_list[i+1]:
                continue 
            else:
                res = False
                break
        return res