from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        temp_list = []

        for word in words:
            # create a frequency map for each word
            freq_map = {}

            # loop through each character in the word
            for char in word:
                if char not in freq_map:
                    freq_map[char] = 1
                else:
                    freq_map[char] += 1
            temp_list.append(freq_map)

        # for each char of the first word, look at all of the rest of the sub dictionaries, and find the minumum
        # amount of occurrences for each char that is available in all of the sub dictionaries
        result = []
        temp_val = []

        for char in temp_list[0]:
            for sub_dict in temp_list:
                temp_val.append(sub_dict.get(char, 0))

            # if True, it means that the char is not appearing in all of the words
            if 0 not in temp_val:
                result.extend([char] * min(temp_val))

            # reset the list of value appereances for each character to collect again for the next char that appears in multiple words
            temp_val = []

        return result


#################
### Test case ###
#################

words = ["bella", "label", "roller"]

solution = Solution()
print(solution.commonChars(words=words))
