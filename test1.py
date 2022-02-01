
def permutations(string, found, step = 0):
    if step == len(string):
        if(string == ["n","o","e"]):
            found = True
            
        # we've gotten to the end, print the permutation
        print(string)
        

    for i in range(step, len(string)):
        if(found):
            break
        # copy the string (store as array)
        string_copy = [c for c in string]
        # swap the current index with the step
        string_copy[step], string_copy[i] =string_copy[i], string_copy[step]

        # recurse on the portion of the stringthat has not been swapped yet
        permutations(string_copy, found, step + 1)

found = False
print(permutations ('one', found))
print("found")

# word = "123"
# found = False
# step = 0

# while(not found):
#     step = 0
#     for i in range(step, len(word)):
#         string = [c for c in word]

#         string[step], string[i] = string[i], string[step]
#         step += 1

#         if(string == len(word)):
#             if(string == ["n","o","e"]):
#                 found = True
#             print(string)
        
       
            
        


