class Solution:
    def reverseWords(self, s: str) -> str:
        i=0
        words=[]
        n=len(s)

        while i<n:
            if s[i]!=" ":
                j=i
                while j<n and s[j]!=" ":
                    j+=1
                words.append(s[i:j])
                i=j
            else:
                i+=1
        words.reverse()
        return " ".join(words)


    
        
        
