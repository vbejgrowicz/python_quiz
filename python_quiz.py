easy_string = "A __1__ is a block of code that does a specific task and can be helpful when \nperforming repetitive tasks. The first __1__ of python that you typically learn is \nthe __2__ __1__, print(). However, you can also make a user-defined __1__ by using \nthe keyword __3__. The __4__ statement is used to exit a function, and can be \nused to pass an expression back to the caller."
medium_string = "A __1__ is a block of code that does a specific task and can be helpful when \nperforming repetitive tasks. The first __1__ of python that you typically learn is \nthe __2__ __1__, print(). However, you can also make a user-defined __1__ by using \nthe keyword __3__. The __4__ statement is used to exit a function, and can be \nused to pass an expression back to the caller. \n\nA __5__ can be used to store integers, decimals or characters. Values can be \nassigned to the __5__ using an equal sign and their names can contain numbers, letters, \nand underscores but they cannot contain __6__. The name should be short but descriptive \nto allow the code to be easily understood."
hard_string = "A __1__ is a block of code that does a specific task and can be helpful when \nperforming repetitive tasks. The first __1__ of python that you typically learn is \nthe __2__ __1__, print(). However, you can also make a user-defined __1__ by using \nthe keyword __3__. The __4__ statement is used to exit a function, and can be \nused to pass an expression back to the caller. \n\nA __5__ can be used to store integers, decimals or characters. Values can be \nassigned to the __5__ using an equal sign and their names can contain numbers, letters, \nand underscores but they cannot contain __6__. The name should be short but descriptive \nto allow the code to be easily understood. \n\nLoops allow a series of instructions to __7__ until it meets a specific condition. Types \nof loops include __8__ loops and for loops. __8__ loops allow us to run the instructions \nas long as the equality expression is True, and for loops allow us to iterate \nthrough a list until we reach the end. An important thing to remember when using __8__ \nloops is to remember to increment the count value to avoid entering an __9__ loop."
easy_ans = ["function", "built-in", "def", "return"]
medium_ans = ["function", "built-in", "def", "return", "variable", "spaces"]
hard_ans = ["function", "built-in", "def", "return", "variable", "spaces", "repeat", "while", "infinite"]
levels = ["easy", "medium", "hard"]
ans_key = {easy_string: easy_ans, medium_string: medium_ans, hard_string: hard_ans}
guesses_per_question = {easy_string: 5, medium_string: 3, hard_string: 2}

# takes the user's level input and returns the selected string as well as the allowed guess count based on the level selection
def user_level_selection():
    level_input = ""
    while level_input.lower().strip() not in levels:
        level_input = raw_input("Select a Level: Easy/Medium/Hard \n")
    if level_input.lower().strip() == "easy":
        selected_string = easy_string
    if level_input.lower().strip() == "medium":
        selected_string = medium_string
    if level_input.lower().strip() == "hard":
        selected_string = hard_string
    print("\nYou've chosen " + level_input.capitalize().strip() + "!")
    guesses = num_of_guesses(selected_string)
    return [selected_string, guesses]

# takes the selected string from user_level_selection and returns the number of guesses allowed
def num_of_guesses(selected_string):
    guesses = guesses_per_question[selected_string]
    print("You will be allowed " + str(guesses) + " incorrect guesses.\n")
    return guesses

# takes in answer string, guesses per question value, and current blank position and checks for correct answer
# returns true if correct and loops if incorrect until reaching guess per question value then returning False if out of guesses
def guessed_correctly(ans, allotted_guesses, num):
    guess_count = 0
    while guess_count < allotted_guesses:
        response = raw_input("What is the answer to " + str(num + 1) + " ? ")
        if response.lower().strip() == ans[num].lower():
            return True
        else:
            guess_count += 1
            if guess_count != allotted_guesses:
                print("That isn't the correct answer, you have " + str(allotted_guesses - guess_count) + " guesses left!\n")
    return False

# takes in current string, answer string and current blank position and returns the string with replaced answers
def string_replacement(string, ans, num):
    replaced_string = string.replace(". " + "__" + str(num + 1) + "__", ". " + ans[num].capitalize())
    replaced_string =  replaced_string.replace("__" + str(num + 1) + "__", ans[num])
    return replaced_string

# goes through the full quiz by incrementing through available blanks and prints the completed string when finished
def play_quiz():
    user_selection = user_level_selection()
    chosen_level_index = 0
    chosen_guess_index = 1
    selected_string = user_selection[chosen_level_index]
    allotted_guesses = user_selection[chosen_guess_index]
    index = 0
    ans = ans_key[selected_string]
    while index < len(ans):
        print "\n" + selected_string + "\n"
        if guessed_correctly(ans, allotted_guesses, index):
            selected_string = string_replacement(selected_string, ans, index)
            index += 1
        else:
            print("That isn't the correct answer, too many incorrect guesses!")
            return
    print selected_string + "\n"

play_quiz()
