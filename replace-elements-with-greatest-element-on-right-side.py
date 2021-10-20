# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

def replaceElements(arr):
    # Pseudocode:
    # add -1 to the list
    # save the CURRENT greatest as arr[-1]
    # Iterating through the array from right to left
    #     append Greatest to the array
    #     save the NEW greatest elemenet if it is greater than the CURRENT greatest
    
    result = [-1]
    greatest = arr[-1]
    for i in arr[-2::-1]:
        result.insert(0, greatest)
        if i > greatest:
            greatest = i
    return result
        