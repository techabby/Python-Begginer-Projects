print(
    f"""
        ╔══════════════════════════════════════════════════╗
        ║                 Hello,Abby                       ║
        ║      Welcome to Kaun Banega Crorepati (KBC)      ║
        ╚══════════════════════════════════════════════════╝
      """
)

Questions = [
    [
        "What does the acronym 'URL' stand for?",
        "Uniform Resource Locator",
        "Universal Registration of Links",
        "User Rights and Licenses",
        "Unit Revision Log",
        1,
    ],
    [
        "Which ocean is the largest on Earth?",
        "Southern Ocean",
        "Indian Ocean",
        "Pacific Ocean",
        "Atlantic Ocean",
        3,
    ],
    [
        "What is the term for a bowler taking three wickets in three consecutive deliveries?",
        "Hat Trick",
        "Trifecta",
        "Threefold Strike",
        "Triple Play",
        1,
    ],
    ["What is the currency of Japan?", "Yuan", "Won", "Yen", "Ringgit", 3],
    [
        "Who directed the film 'Inception'?",
        "Christopher Nolan",
        "Quentin Tarantino",
        "Kevin Fedge",
        "Steven Spielberg",
        1,
    ],
    [
        "Who was the first President of the United States?",
        "John Adams",
        "George Washington",
        "Abraham Lincoln",
        "Thomas Jefferson",
        2,
    ],
    [
        "Which programming language was developed by James Gosling at Sun Microsystems in the 1990s?",
        "Ruby",
        "Python",
        "C++",
        "Java",
        4,
    ],
    ["How many moons does the planet Venus have?", "2", "3", "5", "None", 4],
    [
        "What is the term for a sudden and intense feeling of fear or discomfort without an apparent cause?",
        "Phobia",
        "Panic attack",
        "Anxiety",
        "Depression",
        2,
    ],
    [
        "What is the purpose of a firewall in computer networks?",
        "Virus protection",
        "File storage",
        "Unauthorized Access Prevention",
        "Network speed optimization",
        3,
    ],
    [
        "Who developed the theory of relativity?",
        "Isaac Newton",
        "Albert Einstein",
        "Galileo Galilei",
        "Stephen Hawking",
        2,
    ],
    [
        "Which galaxy is the Milky Way closest to?",
        "Triangulum",
        " Pinwheel",
        "Whirlpool",
        "Andromeda",
        4,
    ],
    [
        "What is the primary neurotransmitter associated with feelings of pleasure and reward?",
        "Serotonin",
        "Dopamine",
        "GABA",
        "Endorphins",
        2,
    ],
    [
        "In cricket strategy, what does the term 'reverse sweep' refer to?",
        "Umpire Decision Review",
        "Bowling Technique",
        "Unorthodox Shot",
        "Fielding Position",
        3,
    ],
    [
        "Which chemical element is the lightest metal and is highly reactive with water?",
        "Sodium",
        "Potassium",
        "Lithium",
        "Rubidium",
        3,
    ],
]

Levels = [
    1000,
    2000,
    3000,
    5000,
    10000,
    20000,
    40000,
    80000,
    160000,
    320000,
    640000,
    1250000,
    2500000,
    5000000,
    10000000,
]
Money = 0

for i in range(0, len(Questions)):
    Question = Questions[i]
    print(f"\n\nQuestion for RS.{Levels[i]}\n")
    print(Question[0])
    print(f"A.{Question[1]}                      B.{Question[2]}")
    print(f"C.{Question[3]}                      D.{Question[4]}")

    Answer = int(input("Enter the option number(1-4): "))
    if Answer == Question[-1]:
        print(f"Congratulation! You won RS.{Levels[i]} for answering this question.")
        if i == 5:
            Money = 10000
        elif i == 10:
            Money = 320000
        elif i == 15:
            Money = 10000000
    else:
        print("I am Sorry,you gave the wrong answer.")
        break

print(f"The money you won is RS.{Money}")
