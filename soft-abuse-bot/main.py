import time
reactions = {
    666: "Oh,great! You worship the dark lord too. Respect.",
    69: "Wow, very mature. You exceeded my expectations with this one.",
    7: "... Get out."
}
print("Hey there, little shit. How's it?")
time.sleep(2)
print("Actually, I couldn't care less.")
time.sleep(2)
try:
    answer = input("Are you a boy or a girl? (Boy/Girl) ").lower()
except ValueError:
    character_gender = "Boeing AH-64 Apache"
    print("Right... Let's just say you're a helicopter.")
if answer == "boy":
    character_gender = "walking malfunction"
    print("I see, another NPC with opinions, huh?")
elif answer == "girl":
    character_gender = "unskippable cutscene"
    print("Got it. An unpatched bug with eyeliner. Cool.")
else:
    character_gender = "fail in the Matrix"
    print("Ah! A collective hallucination. That explains the vibes.")
time.sleep(2)
while True:
    try:
        num = int(input(f"So, my dear {character_gender}, what's your favourite number? "))
        break
    except ValueError:
        print("That's not a fucking number, you low-poly mob.")
        try:
            num = int(input("Tell me what your favourite number is. An actual number this time around, please: "))
            break
        except ValueError:
            print("I knew you were an idiot, but this is too much for me. I'm out of here.")
            exit()
if num in reactions:
    print(reactions[num])
    exit()
else:
    print(f"Oh my GOD! {num}! That's EXACTLY my favourite number, too!")
time.sleep(2)
answer = input("Can you even believe that?! (Yes/No) ").lower()
if answer == "yes": print(f"HA! Got you, idiot!\nMy favourite number is {num - 1}")
elif answer == "no": print("Gosh... You're the human equivalent of a loading screen. Bye.")
else:
    print("Huh...?")
    exit()
