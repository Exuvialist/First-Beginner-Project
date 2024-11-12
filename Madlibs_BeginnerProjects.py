#credits to tech with tim for teaching me to make these kind of beginner projects :D
#make sure that "story.txt" and "story2.txt" file is in the same folder as this file

story_option = int(input("Which story do you want to select? (input 1 or 2) : "))

if story_option == 1:
    with open("story.txt", "r") as f:
        story = f.read()
if story_option == 2:
    with open("story2.txt", "r") as f:
        story = f.read()
else:
    with open("story1.txt", "r") as f:
        story = f.read()

words = set()
starting_words = -1

target_start = "<"
target_end = ">"

for i, char, in enumerate(story):
    if char == target_start:
        starting_words = i

    if char == target_end and starting_words != -1:
        word = story[starting_words: i + 1]
        words.add(word)
        starting_words = -1

answers = {}
for word in words:
    answer = input("Input a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)