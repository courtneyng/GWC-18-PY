friends = ["Camille", "Sarah", "Jade", "Aadiba", "Aishe"]
onepiece = ["Luffy", "Zoro", "Nami", "Usopp", "Sanji", "Chopper", "Robin", "Frankie", "Brook"]
friend = "RajabButt"
two = [friends, onepiece]

print(*friends) #list w/o brackets and commas
print(friends) #list with brackets and commas but also quotes

for name in friends: #print vertically (all names)
    print(name)

print(len(friends))
print("Camille" in friends) #checks

print(friends[0])
for i in range(len(friends)):
    #print(friends[i]) #this just prints names vertically
    print(i)

for letter in friend: #print single letters down
    print(letter)

print(len(friend))
for group in two:
    for name in group:
        print(name)
        
