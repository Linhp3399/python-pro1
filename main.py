numer={
    "mama": 1234456,
    "tata": 1111111,
    "babcia": 658988,
}
word = input("kogo numer chcesz otrzymać(małe litery)")
if word in numer.keys():
    print(word, numer[word])
else:
    print("nie ma przypisanego do tego numeru")

