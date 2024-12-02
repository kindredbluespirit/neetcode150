class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        
        freq_s, freq_t = {}, {}
        for i in range(n):
            # j = n-1-i
            # if j < i:
            #     return True
            # if s[i] != t[j]:
            #     return False
        
            if s[i] in freq_s:
                freq_s[s[i]] += 1
            else:
                freq_s[s[i]] = 1
            
            if t[i] in freq_t:
                freq_t[t[i]] += 1
            else:
                freq_t[t[i]] = 1      

        for key in freq_s.keys():
            if key not in freq_t.keys() or freq_s[key] != freq_t[key]:
                return False
        
        return True
            
