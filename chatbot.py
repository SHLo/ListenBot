import sys
import random
import os.path
from get_sentiment_naive import get_sentiment_naive
from get_sentiment import get_sentiment
from talk_jokes import talk_jokes

# Use "chatbot.py" to judge the sentiment in a Naive(default) way
# Use "chatbot.py -g" to call Google NLP API web service
# Improvement 1: add lower case function for user's input to judge the sentiment correctly
# Improvement 1: add talk_jokes function if the user's mood is not good

if (len(sys.argv)>1 and sys.argv[1] == '-g'):
    get_score = get_sentiment
else:
    get_score = get_sentiment_naive

# start conversation
name = input("What's your name? ")
print ("Let's talk, " + str(name))
var = input("How's today? "+ str(name)+" ")
negative_count = 0
response = "N"
# continue conversation, user type "Bye" to end the while loop
while(var != "Bye"):
    var = input("Talk more? " + str(name) + ". :) (Say 'Bye' to end the conversation.) ")
    sentiment_score = get_score(var)

    #bring happiness to negative user
    postive = ['Great','Cool']
    negative = ['That sucks','Bummer']
    neutral = ['Hmm..','I see']

    #Judge the setiment
    if(sentiment_score>0):
        print(random.choice(postive))
    elif (sentiment_score<0):
        print(random.choice(negative))
        negative_count+=1
        if(negative_count>1):
            talk_jokes()
            negative_count = 0
    else:
        print(random.choice(neutral))
    #response sentence
