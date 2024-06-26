

def return_evens(numbers):
    return [num for num in numbers if num % 2 == 0]

def make_exclamation(sentences):
    return [sentence + "!" for sentence in sentences]

print(return_evens([0, 1, 3, 5, 7, 8, 9]))
print(make_exclamation([ "I like computers!","I require coffee!","Live long and prosper!"]))
