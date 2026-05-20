class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        index = 0
        keys_map_s = {}
        keys_map_t = {}
        while index < len(s):
            if s[index] not in keys_map_s:
                keys_map_s[s[index]] = t[index]

            if t[index] not in keys_map_t:
                keys_map_t[t[index]] = s[index]
            
            index += 1

        new_string_arr_s = []
        new_string_arr_t = []

        for letter in s:
            new_string_arr_s.append(keys_map_s[letter])

        for letter in t:
            new_string_arr_t.append(keys_map_t[letter])
        
        new_string_s = "".join(new_string_arr_s)
        new_string_t = "".join(new_string_arr_t)
        if new_string_s != t or new_string_t != s: return False
        else: return True