# Compress the String
# Write a program to do basic string compression. For a character 
# which is consecutively repeated more than once, 
# replace consecutive duplicate occurrences with the count of repetitions.

# Example:
# If a String has 'x' repeated 5 times, replace this "xxxxx" with "x5".
# The string is compressed only when the repeated character count is more than 1.

# Note :
# Consecutive count of every character in the input string is less than equal to 9.

# Input Format :
# The first and the only line of input contains a string(no spaces in between).

# Output Format :
# The only line of output print the compressed string.

# Note:
# Return the compressed string and hence, no need to print.

# Constraints :
# 0 <= |S| <= 10^7
# Where |S| represents the length of string, S.

# Sample Input 1 :
# aaabbccdsa
# Sample Output 1 :
# a3b2c2dsa

# Sample Input 2 :
# aaabbcddeeeee
# Sample Output 2 :
# a3b2cd2e5


str1 = input()
str2=''
i = 0
while i<len(str1):
    m = 0
    for j in range(i,len(str1)):
        if str1[j]==str1[i]:
            m +=1
        else:
            break
    if m >1:
        str2 += str1[i] + str(m)
    else:
        str2 += str1[i]
    i = i+m-1
    i+=1
print(str2)