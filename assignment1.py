def areAnagrams(string_one, string_two):
    if len(string_one) != len(string_two):
        return False
    
    for character in string_one:
        if character not in string_two:
            break
        string_two = string_two.replace(character, "", 1)
        
    return len(string_two) == 0
    
if __name__  == "__main__":
    str1 = "cars"
    str2 = "scar"
    print(f'Are anagrams ( {str1}  - {str2} )? =  {areAnagrams(str1,str2)}')