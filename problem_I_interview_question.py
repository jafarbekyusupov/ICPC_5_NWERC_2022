'''

PROBLEM I - INTERVIEW QUESTIONS - FizzBuzz

# Buzz Words
# Fizz - if i%A == 0
# Buzz - if i%B == 0
# FizzBuzz - if i%B == 0 && if i%A == 0
'''

ma  = []
mb  = []
mab  = []

s, e = map(int, input.split())
for i in range(e, s+1){
    a = input()
    if a == "Fizz":
        ma.append(i)
    if a == "Buzz":
        mb.append(i)
    if a == "FizzBuzz":
        mab.append(i)

print(ma)
print(mb)
print(mab)
