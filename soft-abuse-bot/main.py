reactions = {
    666: "Oh. You worship the dark lord too? Respect.",
    69: "Very mature. I'm rolling my eyes...",
    7: "Oh, so you’re that person."
}

try:
    answer = input("Hey there, little shit. Are you a boy or a girl? (Boy/Girl) ").lower()
except ValueError:
    character_gender = "helicopter"
    print("So... a helicopter, whatever.")
if answer == "boy":
    character_gender = "stinky pig"
    print("I see, another stinky pig, huh?")
elif answer == "girl":
    character_gender = "crazy lunatic"
    print("So... a crazy lunatic, probably.")
else:
    character_gender = "helicopter"
    print("Let's just say you're a helicopter.")
while True:
    try:
        num = int(input(f"And what's your favourite number, {character_gender}? "))
        break
    except ValueError:
        print("That's not a fucking number, moron.")
        try:
            num = int(input("Tell me what your favourite number is. An actual number this time, please: "))
            break
        except ValueError:
            print("I'm starting to think you don't know what a number is.")
            exit()
if num in reactions:
    print(reactions[num])
    exit()
else:
    print(f"Oh! {num}! That's my favourite number, too.")

answer = input("Can you even believe that?! (Yes/No) ").lower()
if answer == "yes": print("HA! Got you! That's not my favourite number.\nI can't believe you fell for that!\nMy favourite number is " + str(num - 1))
elif answer == "no": print("You are no fun at all.")
else:
    print("Huh...?")
    exit()
