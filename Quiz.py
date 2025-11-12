print("This is the super duper awesome quiz show!!")
# You have 3 lives and there are 8 questions and when you lose all the lives, you die
# You have 3 lives
# There are 8 questions
# If you loose all three lives, you die
lives = 3
print("You have 3 lives to start!")
print("How many stomaches does a cow have")
user_answer = input()
expected_answers = ["4", "four"]
if user_answer in expected_answers:
    print("Yay!!")
else:
    print("Not yay :(")
    lives = lives - 1

print("What do you call a group of owls?")
user_answer = input()
expected_answers = ["parliament", "a parliament"]
if user_answer in expected_answers:
    print("Woohoo!")
else:
    print("Not woohoo :(")
    lives = lives - 1

print("What is the only North American marsupial?")
user_answer = input()
expected_answers = ["opossum", "possum", "an opossum", "a possum"]
if user_answer in expected_answers:
    print("Yippe!")
else:
    print("Not yippe :(")
    lives = lives - 1

print("How many eyes does a honeybee have?")
user_answer = input()
expected_answers = ["5", "five"]
if user_answer in expected_answers:
    print("Wowie!")
else:
    print("Not wowie :(")
    lives = lives - 1

print(
    "What animal has fingerprints so similar to humans that they could contaminate a crime scene?"
)
user_answer = input()
expected_answers = ["koala", "a koala"]
if user_answer in expected_answers:
    print("Wonderful!")
else:
    print("Not wonderful :(")
    lives = lives - 1

print("What is the fastest marine animal?")
user_anser = input()
expected_answers = ["dolphin", "a dolphin"]
if user_answer in expected_answers:
    print("Amazing!")
else:
    print("Not amazing :(")
    lives = lives - 1

print("What bird lays the largest eggs?")
user_answer = input()
expected_answers = ["ostrich", "an ostrich"]
if user_answer in expected_answers:
    print("stupendous")
else:
    print("Not stupendous :(")
    lives = lives - 1

print("Which amphibian is known for regenerating lost body parts?")
user_answer = input()
expected_answers = ["axolotl", "an axolotl"]
if user_answer in expected_answers:
    print("Bravo!")
else:
    print("Not bravo :(")
    lives = lives - 1

if lives > 0:
    print("HOORAYYYYYY!!!!!!!")
else:
    print("NOT HOORAYYYYYYYYYYYYYYYYYYY")
