dic = {
    "Ranjit": "Human Being",
    "Steel": "Is a type of metal"
}

# print(dic["Ranjit"])
# print(dic["Steel"])

dic2 = {
    1: "Ranjit",
    2: "Warren Buffet",
    3: "Elon Musk",
    4: "Steve Jobs",
    5: "Tesla"
}

dic3 = {
    1: "Ranjit",
    2: "Warren Buffet",
    3: "Elon Musk",
    5: "Tesla"
}

# for i in range(len(dic2)):
#     print(dic2.keys())

for i in dic2:
    print(dic2[i])

dict1 = {
    "name": "Ranjit", "age": 34, "eligible": True
}

# print(dict1)
# print(dict1["name"])        # This will throw an error if the element was not there in the dict1
# print(dict1.get("age"))     # get method will not throw any error if the element was not there in the dict1
# print(dict1.keys())         # Means on which you have set the values like name, age and eligible
# print(dict1.values())       # This will print the values you have set along with the name, age and eligible
# print(dic2.keys())

# for i in dict1.keys():      # This will print which values you have set
#     print(f"The value set for the key is {i} is {dict1[i]}")

# for key, value in dict1.items():        # This method is used to print the key and values of all the elements of the dict1
#     print(f"The value corresponding to the key {key} is {value}")

