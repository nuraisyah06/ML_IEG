# set uses()
# set is modifiedable (add, edit and delete)
# set is unordered (does not retain)
# set is not indexed
# set does not allowed duplicate

x = {10, 20, 30, 10, 40, 50, 20, 60, 70}
print(x)

# to retrieve the item one by one
for i in x:
    print(i)
    
#modified the set
fruits = {"apple", "orange", "durian"}
print(fruits)
fruits.add("mango")
print(fruits)

# to delete an item in the set
fruits.remove("orange")
print(fruits)

# pop, to randomly remove an item 
fruits.pop()
print(fruits)

print("-" * 50)

fruits = ["apple", "orange", "apple", "mango", "banana", "apple"]
uniquefruit = set(fruits)
print(uniquefruit)

print("-" * 50)

overseafruit = {"apple", "orange", "banana", "mango", "grape"}
localfruit = {"durian", "rambutan", "cempedak", "banana", "mangosteen"}
print(overseafruit.union(localfruit))
print(overseafruit.intersection(localfruit))
print(overseafruit.difference(localfruit))
print(localfruit.difference(overseafruit))

print("-" * 50)

favfruit = {"durian", "rambutan", "mangosteen"}
print(favfruit.issubset(localfruit))
print(localfruit.issuperset(favfruit))
print(favfruit.isdisjoint(overseafruit))

print("-" * 50)

emailcontent = """Phishing is a type of online scam that targets consumers 
by sending them an e-mail that appears to be from a well-known source 
an internet service provider, a bank, or a mortgage company, for example. 
It asks the consumer to provide personal identifying information. 
Then a scammer uses the information to open new accounts, or invade the 
consumer is existing accounts. There are several tips that consumers 
can follow to avoid phishing scams, such as not responding to e-mails 
or pop-up messages that ask for personal or financial information.
"""

words = emailcontent.split()
print(len(words))

uniquewords = set(words)
print(len(uniquewords))
print(uniquewords)

cleanword = []
for word in words:
    word = word.replace(",", "")
    word = word.replace(".", "")
    word = word.lower()
    cleanword.append(word)
    
uniquewords = set(cleanword)
print(len(uniquewords))

print(uniquewords)

commonword = {"is", "or", "of", "so", "by", "how", "when", "it", "on", "the", "into", "a",
              "to", "is", "are", "what", "be", "i", "you", "more", "and", "can", "an"}

uniquewords = uniquewords.difference(commonword)
print(uniquewords)
print(len(uniquewords))

spamwords = {"phising", "spam", "tricked", "security", "criminals", "scammer", "scams"}
totalspamwords = uniquewords.intersection(spamwords)
print(len(totalspamwords))