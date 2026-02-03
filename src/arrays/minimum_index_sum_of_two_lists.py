from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        Given two arrays of strings list1 and list2, find the common strings with the least index sum.
        A common string is a string that appeared in both list1 and list2.

        A common string with the least index sum is a common string such that
        if it appeared at list1[i] and list2[j] then i + j should be the minimum value
        among all the other common strings.

        Return all the common strings with the least index sum. Return the answer in any order.

        Parameters
        ----------
        list1 : List[str]
            Array of strings.
        list2 : List[str]
            Array of strings.

        Returns
        -------
        List[str]
            List of all the common strings with the least index sum. Return the answer in any order.

        Examples
        --------
        Example 1:
        Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
        Output: ["Shogun"]
        Explanation: The only common string is "Shogun".

        Example 2:
        Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
        Output: ["Shogun"]
        Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

        Example 3:
        Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
        Output: ["sad","happy"]
        Explanation: There are three common strings:
        "happy" with index sum = (0 + 1) = 1.
        "sad" with index sum = (1 + 0) = 1.
        "good" with index sum = (2 + 2) = 4.
        The strings with the least index sum are "sad" and "happy".
        """
        # convert the list to dictionary to hash map it and reduce the amount of iterations needed to loop through both lists
        dict_list2 = {word: val for val, word in enumerate(list2)}

        # dict to store word keys and index values
        # word_dict = {}
        # for idx, word in enumerate(list1):
        #     if word in dict_list2:
        #         # sum up the values from dictionary and idx
        #         word_dict[word] = dict_list2[word] + idx

        word_dict = {
            word: dict_list2[word] + idx  # if the word is found, sum up the indexes
            for idx, word in enumerate(list1)
            if word in dict_list2
        }

        return [k for k, v in word_dict.items() if v == min(word_dict.values())]


# Test cases
list1 = ["happy", "sad", "good"]
list2 = ["sad", "happy", "good"]

solution = Solution()
print(solution.findRestaurant(list1=list1, list2=list2))
