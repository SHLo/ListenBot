import sys
import random
import os.path
from get_sentiment_naive import get_sentiment_naive
from get_sentiment import get_sentiment

# Use "chatbot.py" to judge the sentiment in a Naive(default) way
# Use "chatbot.py -g" to call Google NLP API web service

if (len(sys.argv)>1 and sys.argv[1] == '-g'):
    get_score = get_sentiment
else:
    get_score = get_sentiment_naive

# start conversation
var = input("What's your name? ")
print ("How's today, " + str(var))

# continue conversation, user type "Bye" to end the while loop
while(var != "Bye"):
    var = input("Talk more? (Say 'Bye' to end the conversation.) ")
    sentiment_score = get_score(var)

    #response sentence
    postive = ['Great','Cool']
    negative = ['That sucks','Bummer']
    neutral = ['Hmm..','I see']

    #Judge the setiment
    if(sentiment_score>0):
        print(random.choice(postive))
    elif (sentiment_score<0):
        print(random.choice(negative))
    else:
        print(random.choice(neutral))
