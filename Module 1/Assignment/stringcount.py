
sentence="perfect ? he is the perfect . perfect"
print("the original sentence is: "+sentence)
list_temp=sentence.split()
dict1={word:sentence.count(word) for word in list_temp}
print(dict1)