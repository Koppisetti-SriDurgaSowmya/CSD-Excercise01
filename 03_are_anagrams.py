import unittest

question_03 = """
An anagram I am

Given two strings s0 and s1, return whether they are anagrams of each other. Two words are anagrams when you can rearrange one to become the other. For example, “listen” and “silent” are anagrams.

Constraints:
- Length of s0 and s1 is at most 5000.

Example 1:

Input:
s0 = “listen”
s1 = “silent”

Output:
True

Example 2:

Input:
s0 = “bedroom”
s1 = “bathroom”

Output:
False
"""


# Implement the below function and run the program

def are_anagrams(word1, word2):
    for i in word1:
        if i not in word2:
            return False
    for i in word2:
        if i not in word1:
            return False
    return True


class TestAreAnagrams(unittest.TestCase):

    def test_1(self):
        self.assertEqual(are_anagrams('listen', 'silent'), True)

    def test_2(self):
        self.assertEqual(are_anagrams('“bedroom”', 'bathroom'), False)

    def test_3(self):
        self.assertEqual(are_anagrams('madam', 'madam'), True)

    def test_4(self):
        self.assertEqual(are_anagrams('dabc', 'akbc'), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
