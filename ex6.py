# trings can contain any number of variables that are in your Python script. Remember that a variable is any line of code where you set a name = (equal) to a value. In the code for this exercise,
# types_of_people = 10 creates a variable named types_of_people and sets it = (equal) to 10. You
# can put that in any string with {types_of_people}. You also see that I have to use a special type of
# string to ”format”; it’s called an ”f-string” and looks like this:
# f ”some s t u f f here { a v a ri abl e }”
# f ”some other s t u f f { anothervar }”
# Python also has another kind of formatting using the .format() syntax which you see on line 17. You’ll
# see me use that sometimes when I want to apply a format to an already created string, such as in a loop.
# We’ll cover that more later.

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# string inside a string
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said : {x}")
print(f"I also said : '{y}'")

hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."
print(w + e)