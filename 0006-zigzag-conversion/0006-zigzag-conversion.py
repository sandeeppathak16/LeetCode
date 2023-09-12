class Solution:
    def convert(self, s: str, numRows: int) -> str:

        help_dic = defaultdict(list)
        d = True
        r = 0

        for i in range(len(s)):
            help_dic[r].append(s[i])
            if d:
                r+=1
            else:
                r-=1

            if r == numRows - 1:
                d = False

            elif  r == 0:
                d = True

        ans = ''

        for key in help_dic:
            ans += ''.join(help_dic[key])
        
        return ans



            

        