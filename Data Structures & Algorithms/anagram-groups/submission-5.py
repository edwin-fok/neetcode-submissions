class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        chars_per_word = {}
        index = 0

        for str in strs:
            current_chars = [0] * 26
            for char in str:
                position = ord(char) - ord("a")
                current_chars[position] += 1
            
            key = tuple(current_chars)

            if chars_per_word.get(key) is None:
                chars_per_word[key] = index
                output.append([str])
                index += 1
            else:
                output_index = chars_per_word.get(key)
                output[output_index].append(str)
        
        return output