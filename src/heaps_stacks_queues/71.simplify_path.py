class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Transform an absolute path into its simplified canonical path.

        The rules of a Unix-style file system are as follows:
        - A single period '.' represents the current directory.
        - A double period '..' represents the previous/parent directory.
        - Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
        - Any sequence of periods that does not match the rules above should be treated as a valid directory or file name.
        For example, '...' and '....' are valid directory or file names.

        The simplified canonical path should follow these rules:
        - The path must start with a single slash '/'.
        - Directories within the path must be separated by exactly one slash '/'.
        - The path must not end with a slash '/', unless it is the root directory.
        - The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.

        Parameters
        ----------
        path : str
            Absolute path for a Unix-style file system.

        Returns
        -------
        str
            Return the simplified canonical path.

        Examples
        --------
        Example 1:
        Input: path = "/home/"
        Output: "/home"

        Explanation:
        The trailing slash should be removed.

        Example 2:
        Input: path = "/home//foo/"
        Output: "/home/foo"

        Explanation:
        Multiple consecutive slashes are replaced by a single one.

        Example 3:
        Input: path = "/home/user/Documents/../Pictures"
        Output: "/home/user/Pictures"

        Explanation:
        A double period ".." refers to the directory up a level (the parent directory).

        Example 4:
        Input: path = "/../"
        Output: "/"

        Explanation:
        Going one level up from the root directory is not possible.

        Example 5:
        Input: path = "/.../a/../b/c/../d/./"
        Output: "/.../b/d"

        Explanation:
        "..." is a valid name for a directory in this problem.
        """
        # split the original path string into a list of elements based on the forward slash
        path_split = path.split("/")
        # remove empty strings in list
        cleaned_list = [item for item in path_split if item]
        # actual stack
        stack = []

        for element in cleaned_list:
            try:
                # go back one if the element == ".."
                if element == "..":
                    stack.pop(-1)
                # stay in the same directory if element == "."
                elif element == ".":
                    pass
                else:
                    stack.append(element)
            # if there is no previous element, just continue, it means we are already at the beginning of the list
            except IndexError:
                continue
            # print(
            #     f"Element is: {element} | Cleaned List is: {cleaned_list} -> Stack: {stack}"
            # )

        # join the final list: the first element must always be the root directory
        return "/" + "/".join(stack)


#################
### TEST CASE ###
#################

path = "/a/./b/../../c/"

solution = Solution()
print(solution.simplifyPath(path=path))
