import random

subjects = [
    "SRK", 
    "Virat Kholi",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A group of monkeys",
    "PM Modi",
    "Auto Rickshaw Driver from Dehli"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "at mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at ganga ghat",
    "during IPL Match",
    "at India Gate"
]


while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    print("Fake New Headline is ==>")
    print(f"BREAKING NEWS: {subject} {action} {place_or_thing}")
    
    print("Do you want to generate one more headline")
    choice = input("Enter your choice(yes/no): ")
    if choice.lower().strip() == "no":
        break

print("Thanks for using our services💓💓")