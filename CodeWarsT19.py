"""
Given a string, you have to return a string 
in which each character (case-sensitive) is repeated once.

double_char("String") ==> "SSttrriinngg"

double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

double_char("1234!_ ") ==> "11223344!!__  "

"""

def double_char(s):

    s = list(s)

    res_list = []
    res_str = ""

    for i in s:
        for j in i:
            res_list.append(j)
            res_list.append(j)

    for i in range(len(res_list)):
        res_str = res_str + res_list[i]

    return res_str

