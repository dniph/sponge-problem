sentence = "WHAT is UP my dude"

def sponge_case(sentence):
    new_word = ""
    index = 0 
    
    for word in sentence.split():
        for char in word:
            if index % 2 == 0:
                new_word += char.lower()
            else:
                new_word += char.upper()
            index +=1
        new_word += " "
    return new_word.strip()
    
print(sponge_case(sentence))


# # Test cases
# assert sponge_case("spongebob") == "sPoNgEbOb"
# assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
# assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
# assert sponge_case("E") == "e"
# assert sponge_case("e") == "e"

# print("All tests passed!")
# print("Discuss time and space complexity if there's time remaining")