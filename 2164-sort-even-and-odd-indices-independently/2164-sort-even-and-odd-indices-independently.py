class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_list=[]
        odd_list=[]
        
        for i in range(len(nums)):
            if i%2==0:
                even_list.append(nums[i])
            else:
                odd_list.append(nums[i])
                
        even_list.sort()
        odd_list.sort(reverse=True)
        j=k=0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=even_list[j]
                j+=1
            else:
                nums[i]=odd_list[k]
                k+=1
        return nums