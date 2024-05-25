import random

Quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Your time is limited, don't waste it living someone else's life. - Oprah Winfrey",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It's not about ideas. It's about making ideas happen. - Scott Belsky",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Do not wait to strike till the iron is hot, but make it hot by striking. - William Butler Yeats",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "Success is stumbling from failure to failure with no loss of enthusiasm. - Winston S. Churchill",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Your life does not get better by chance, it gets better by change. - Jim Rohn",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "I attribute my success to this: I never gave or took any excuse. - Florence Nightingale",
    "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it. - Jordan Belfort",
    "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
    "Success is not in what you have, but who you are. - Bo Bennett",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. - Steve Jobs",
    "If you are not willing to risk the usual, you will have to settle for the ordinary. - Jim Rohn",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack in will. - Vince Lombardi",
    "Opportunities don't happen. You create them. - Chris Grosser",
    "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "Success is not just about making money. It's about making a difference. - Unknown",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
]


def generate_quotes():
    Quote = random.choice(Quotes)
    return Quote


print(generate_quotes())
