#1
import re
txt = "abb ab a"
x = re.findall("a{1}d*", txt)

#2
import re

def match_string(input_string):
    pattern = r'a(bb|bbb)'
    if re.search(pattern, input_string):
        return True
    else:
        return False
test_string = "abbbb"
print(match_string(test_string)) 

#3
import re

input_string = "my_variable_name is_lorem_ipsum and another_example"
pattern = r'\b[a-z]+_[a-z]+\b'
matches = re.findall(pattern, input_string)
print(matches)     

#4
import re
input_string = "This is a Sample String with Multiple Sequences of Upper and Lower Case letters like This is Another Sample."
matches = re.findall(r'[A-Z][a-z]+', input_string)
print(matches)       

#5
import re
text = "ABcd Efgh Ijk"
pattern = r"[A-Z][a-z]+"
matches = re.findall(pattern, text)
print(matches)        

#6
import re

input_string = "This, is a sample. input string"
output_string = re.sub(r'[ ,.]', ':', input_string)
print(output_string)        

#7
import re
def upper(a):
    return a.group(0).upper()[1::]
s = input()
print(re.sub("_[a-z]",upper,s))       

#8
import re

strs = input()
x = re.split('[A-Z]+', strs)
print(x)     


#9
import re

def insert_spaces(text):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', text)
input_text = "ThisIsAExampleStringWithCamelCase"
result = insert_spaces(input_text)
print(result)        


#10
import re

def camel_to_snake(input_string):
    output_string = re.sub('([a-z0-9])([A-Z])', r'\1_\2', input_string).lower()
    return output_string
input_string = "camelCaseStringExample"
snake_case_output = camel_to_snake(input_string)
print(snake_case_output)