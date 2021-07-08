
#check the number is in given range
def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f'{num} is in range of low and high')
    else:
        print('not in range')

#check amount of upper and lower letters in the string
def up_low(string):
    upper_case = 0
    lower_case = 0
    for s in string:
        if s.isupper():
            upper_case += 1
        elif s.islower():
            lower_case += 1
        else:
            pass
    print(f'no of uppercase charactors = {upper_case}')
    print(f'no of lowercase charactors = {lower_case}')

#check the uique values in the list
def unique_list(lst):
    print(set(lst))
    return set(lst)

#multiply numbers in the list
def multiply(numbers):
    mulnum =1
    for n in numbers:
        mulnum = n*mulnum
    print(mulnum)
    
# check the string reverse word is equal to the word
def palindrome(s):
    s = s.replace(' ','')
    s == s[::-1] 

#ran_check(5,3,9) 
#up_low('My Name Is Deshan Amarathunga')
#unique_list([1,3,4,5,4,4,3,2,2,3,4,5,4,3,2])
#multiply([1,2,3,-4])
#palindrome('nurse run')