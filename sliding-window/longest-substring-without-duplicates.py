class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # appeared = []

        start = 0
        end = 1
        longest = 0
        s_current = ""
        s_longest = ""

        for i, c in enumerate(s):

            while c in s_current:
                s_current = s_current[1:]
                start += 1
            
            s_current += c
            # end = i+1

        # for i, c in enumerate(s):

        #     if c in appeared:

        #         appeared = [c]
        #         start = i
        #         end = i+1
        #         continue
            
        #     appeared.append(c)
            end = i+1
            if longest < end - start:
                longest = end - start
                s_longest = s[start:end]
        
        return longest
