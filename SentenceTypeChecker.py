"""
    In this code if the user enter some sentence then it will check its type and when any user type "end" then
    the program terminates and gives all the sentences with "?" or "." marks at the end and all the first letter 
    of the sentences are capitalized and joined
"""
def sentence_maker(phrase):
    interogatives = ("how","what","why","whose","when","whose","whom")
    capitalized = phrase.capitalize()
    if phrase.startswith(interogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []

while True:
    user_input = input("Type Something: ")
    if user_input == "end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))