'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word)==0: # base case. If  word is empty then the string will return 0.
        return 0
   
    if len(word)<2: #  # if the word has only 1 letter,  2 is the len('th')
        return 0
    # TBC

      # recursive case
    if word[:2] == 'th':
        return count_th(word[1:]) +1  # check if the first substring matches
    pass
    return count_th(word[1:])

    print(count_th('abcthabcth')) 