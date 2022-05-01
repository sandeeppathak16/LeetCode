#User function Template for python3

class Solution:

    def getSubstringWithEqual012(self, Str):
        # code here
        
        d={}
        d[(0, 0)]=1
        count=0
        zc, oc, tc = 0, 0, 0
        
        for s in Str:
            
            if s == '0':
                zc+=1
            elif s == '1':
                oc+=1
            else:
                tc+=1
            tmp=(zc-oc, zc-tc)
            
            if tmp not in d:
                count+=0
            else:
                count+=d[tmp]
                
                
            if tmp in d:
                d[tmp]=1+d[tmp]
            else:
                d[tmp]=1
        return count
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.getSubstringWithEqual012(Str))

# } Driver Code Ends