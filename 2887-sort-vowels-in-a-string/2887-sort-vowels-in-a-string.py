class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        
        vowel_list = []
        for c in s:
            if c in vowels:
                vowel_list.append(c)
        new_str = []
        vowels_str = sorted(vowel_list)
        i = 0

        for c in s:
            if c in vowels:
                new_str.append(vowels_str[i])
                i += 1
            else: 
                new_str.append(c)
        return "".join(new_str)