# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. It can 
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and 
#     a string, and returns the result of applying the converter to the 
#     input string. This replaces all occurrences of the match used to 
#     build the converter, with the replacement.  It keeps doing 
#     replacements until there are no more opportunities for replacements.


        

def converter(string, match, replacement):
    start = string.find(match)
    while start>=0:
        string = string[:start] + replacement + string[start+len(match):]
        start = string.find(match)
    return string
        
    

print converter("aaaaabaaaa", "aba", "b")
#should be "ab"
#replace any occurence of match in string to replacement
#replace any occurence of "aba" in "aaaaabaaaa" to "b"
