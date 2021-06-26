import re

p = re.compile("ca.e") 
# .(ca.e) : a character > care, cafe, case(o) / caffe (x)
# ^(^de) : start of strings > desk, destination(o) / fade (x)
# $(se$) : end of strings > case, base(o) / face (x)

def print_match(m):
    if m : 
        print("m.grounp() : ", m.group())
        print("m.string : ", m.string)
        print("m.start() : ", m.start()) # start index that matches the character
        print("m.end() : ", m.end()) # endS index that matches the character
        print("m.span() : ", m.span())# (start index, end index) that matches the character
    else :
        print("not matching")

# m = p.match("careless") # match : check the given characters from the beginning
# print_match(m)
# m = p.search("good care") # search : check if the characters matche in the given characters
# print_match(m)
list = p.findall("careless cafe") # findall : change all that matches the character to a list
# print_match(m)
print(list)