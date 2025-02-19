#1
import re
pattern = r'a*b*'
test = ["a", "ab", "abb", "aab", "b", "xyz"]
for s in test:
    if re.fullmatch(pattern,s):
        print(f"Match: {s}")


#2
import re
pattern = r'ab{2,3}'
test = ["abb", "abbb", "ab", "a", "abbbb"]
for s in test:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")
        
        
#3
import re
pattern = r'[a-z]+_[a-z]+'
test = ["hello_world", "helloWorld", "hello_world_test", "test_", "_test"]
for s in test:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")
