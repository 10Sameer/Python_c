#  All captial except word with c
my_string = "This is college where we are learning about coding"

upper_string = my_string.upper()

upper_string_lambda = lambda x : x.upper()

def func_upper(word):
    if word.startswith("c"):
       a = word.title()
    else:
      a = word.upper()
    return a

splited_list = my_string.split( " ")
final_ans= list(map( func_upper, splited_list))
print(splited_list)
print(final_ans)
  

# New function
jpt_list= "This is the world where we live"
def func_jpt(word, index) :
    if index % 2 == 0:
        result_word = word.upper()
    else:
         result_word = word.title()
    return result_word

result = [func_jpt(word, index) for index, word in enumerate(jpt_list.split())]
print("-".join(result))
