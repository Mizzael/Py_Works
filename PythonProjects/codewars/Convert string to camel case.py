# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

# Example
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

def to_camel_case(text):
    if text == '' or text == ' ':
        pass
    else:
        # for index in range(len(text)):
        # if text[index] == '_':
        #     char = text[index+1]
        #     char.Upper()
        #     text.replace(index+1, char)
        return text


print(to_camel_case('hola_mundo'))
