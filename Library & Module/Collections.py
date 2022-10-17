# My GitHub:  		GitHub.com/AliRezaJoodi

from Display import display

def Anagrams():
    from collections import defaultdict
    anagrams = defaultdict(list)
    ##anagrams = {"aet": ["123"]}
    anagrams["aet"].append("tea")
    anagrams["aet"].append("eat")
    anagrams["abt"].append("bat")
    anagrams["aet"].append("ate")
    anagrams["acr"].append("arc")
    anagrams["acr"].append("car")
    display("Anagrams:", anagrams)
    display("Anagrams:", list(anagrams.values()))
    
def words_counter():
    from collections import Counter
    words_list= ['red', 'blue', 'red', 'red', 'blue', 'yellow']
    display("Words List:", words_list)
    words_number_dict= dict(Counter(words_list))
    display("Words Number:", words_number_dict)

def main():
    Anagrams()
    

if __name__ == "__main__":
    main()
    
    
    