import random

# list of roasts - for loop go soon need this!
high_jokes = ["Oga calm down, you dey fly go space?", "Too high! You wan guess MTN recharge card?", "My guy, bring am down like NEPA light!"]
low_jokes = ["You too small, add small jara!", "Too low, even your shoe pass am!", "Low like your data after TikTok!"]
win_jokes = ["You get brain sha!", "Ah! Wizard!", "Even my grandma no go guess like this!"]

try:
    file = open("best_score.txt", "r")
    best = int(file.read())
    file.close()
except:
    best = 100

while True:
    secret = random.randint(1, 20)
    guess = 0
    tries = 0
    
    print("\n🔥--- NEW GAME ---🔥")
    
    while guess != secret:
        guess = int(input("Guess 1-20: "))
        tries += 1
        
        if guess == secret:
            print(f"✅ CORRECT! Na {secret} be am!")
            print(random.choice(win_jokes)) # pick one random joke
            print(f"You use {tries} tries")
            
            if tries < best:
                print(f"🏆 NEW BEST! From {best} to {tries}!")
                best = tries
                open("best_score.txt", "w").write(str(best))
        elif guess > secret:
            print("📈 " + random.choice(high_jokes))
        else:
            print("📉 " + random.choice(low_jokes))
    
    again = input("\nPlay again? (y/n): ")
    if again == "n":
        print(f"Thanks! Your final best na {best} 🏆")
        break
