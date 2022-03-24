
# Extra Credit.  Write Palindrome function using classes, must provide implementation of call.
# Must indicate where error occurs on front and back comparison.


class Palindrome:
    def __init__(self, word):
        self.word = word

    def pal_check(self):
        # self.word = str(self.word)
        # return self.word
        # do a while loop using len()
        x = len(self.word)
        while x > 0:
            if self.word[len(self.word)-(x-1)] == self.word[len(self.word)]:
                x = x - 1
                if x == 0:
                    answer = "yes"
                    return answer
            else:
                answer = "no"
                return answer


# response = (input("What word do you want to check: "))
# n = Palindrome(response)
# Palindrome.word = n
#
# print(Palindrome.pal_check(Palindrome.word))


# Working Palindrome Test
word = input("what word do you want to test?: ")
n = len(word)
m = 1
while n > 0:
    if word[(len(word) - n)] == word[len(word) - m]:
        n = n - 1
        m = m + 1

if n == 0:
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")






