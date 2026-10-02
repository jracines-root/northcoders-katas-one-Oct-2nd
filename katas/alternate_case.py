
# "Hello World!"
# ['h','e','l','l','o',' ', ]
        
def alternate_case(sentence):
    
    characters = []
    toggle_capital = True
    
    for char in sentence:
        
        if char.isalpha() == True: 
            if toggle_capital == True:
                new_char = char.upper()
                characters.append(new_char)
            if toggle_capital == False:
                new_char = char.lower()
                characters.append(new_char)
            
            toggle_capital = not toggle_capital 
        else:
            characters.append(char)
    
    return "".join(characters)   
        
            


# test cases 

print(f"Expected: 'HeLlO', Actual: {alternate_case('Hello')}")

print(f"Expected: 'HeLlO wOrLd', Actual: {alternate_case('Hello World!')}")