def longest_palindromic_substring(s):
    longest_palindrome=""
    if len(s)<2:
        return ""
    for i in range(len(s)):
        for j in range(i,len(s)):
            string=s[i:j+1]
            if string==string[::-1]:
                if len(string)>len(longest_palindrome):
                    longest_palindrome=string
    if len(longest_palindrome)<2:
        return ""
    return longest_palindrome
