class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if not s:
            return

        alpha = 0
        char_idx = []
        for i in range(len(s)):
            if s[i].isalpha():
                alpha += 1
                char_idx.append(i)

        if alpha == 0:
            return [s]

        combinations = 2**alpha
        max_len = len(str(format(combinations-1, 'b')))

        rex = []
        for i in range(combinations):
            b = list(str(format(i, 'b')))
            l_b = len(b)
            if l_b < max_len:
                b = ['0' for _ in range(max_len - l_b)] + b

            original = list(s)
            for cond, idx in zip(b, char_idx):
                cond = int(cond)
                if cond == 0:
                    continue
                else:
                    if s[idx].islower():
                        original[idx] = original[idx].upper()
                    else:
                        original[idx] = original[idx].lower()
            original = "".join(original)
            rex.append(original)

        return rex