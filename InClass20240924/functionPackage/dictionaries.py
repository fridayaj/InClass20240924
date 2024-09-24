# dictionaries.py

def demo():
    """
    Demonstrate basic dictionary stuff
    """
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)
    
    
    # Iterate over the dictionary by key
    for key in myDictionary.keys():
        print(key)

    # iterate by value
    for item in myDictionary.items():
        print(item)

    # Iterate by value
    for value in myDictionary.values():
        print(value)

    # Add a key/value pair to the dictionary
    myDictionary["Michigan State"] = "Spartans"

    print(len(myDictionary))

    # Cause an exception. Add try/except logic to handle this
    try:
        print(myDictionary["Ohio State"])
    except:
        # We end up here if an exception is thrown
        print("Ohio State is an invalid key")

    # Remove Xavier by key and print the entire dictionary
    myDictionary.pop("Xavier")
    for value in myDictionary.values():
        print(value)

    # Create another dictionary called newTeams.
    # Add several key/value pairs
    # Combine that with myDictionary and print the results

    newTeams = {"Houston":"Cougars" , "Miami":"Red Hawks", "Ohio":"BobCats"}
    for key in newTeams.keys():
        myDictionary[key] = newTeams[key]
    print(myDictionary)
