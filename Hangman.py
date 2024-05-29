import random

words = [
    "abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure",
    "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", 
    "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", 
    "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", 
    "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", 
    "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", 
    "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", 
    "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", 
    "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", 
    "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", 
    "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", 
    "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", 
    "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", 
    "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", 
    "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", 
    "nightclub", "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", 
    "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", 
    "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", 
    "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", 
    "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", 
    "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", 
    "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", 
    "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", 
    "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", 
    "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", 
    "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", 
    "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", 
    "zilch", "zipper", "zodiac", "zombie"
]

def executioner(hangman, guess):
    display = ""
    for letter in hangman:
        if letter in guess:
            display += letter
        else:
            display += "_"
    return display            

def hangmangame():
    hangman = random.choice(words)
    guess = []
    attemps = 6
    
    print("Welcome to the HangMan game!")
    print("Try to save the HangMan by guessing the correct word")
    
    while attemps>0:
        print( executioner(hangman, guess))
        guess1 = input("Guess a letter: ").lower()
        
        if len(guess1) != 1 or not guess1.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess1 in guess:
            print("You've already guessed that letter.")
            continue
        
        guess.append(guess1)
        
        if guess1 not in hangman:
            attemps -=1
            print(f"Wrong guess! {attemps} attemps left! Don't let him die!")
        else:
            print("Awesome! He has a chance to live!")
        
        if all(letter in guess for letter in hangman):
            print(f"Hooray! The HangMan lives to hang another day! The word was '{hangman}'")
            break
        
    if attemps == 0:
        print(f"Oh no! He died! The word was {hangman}. Maybe you'll save him in the next life...")    

hangmangame()