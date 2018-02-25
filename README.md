# pairs-of-words
Program finds most popular pairs of words in the text. 

# Input:
2 txt files. File with russian language text where the program will serach pairs and file which contains the list of incorrect words (words which are not needed in the search). Encoding used in these files, do we need to provide for case-insensitive or not, maximum distance between words for their ability to be in one pair and numberof most popular pairs of words we are going to see.

# Output:
List of the most popular pairs of words which are used in the same sentence. It is necessary to exclude all incorrect words from the list of most popular pairs. 

# Example of launching:
pairs.py -c -f text2.txt cp1251 10 -w wrong.txt
