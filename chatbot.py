import sys
import random
import os.path
import get_sentiment
from get_sentiment import get_sentiment

print (sys.argv)

# read the postive and negative corpus
my_path = os.path.abspath(os.path.dirname(__file__))
pos_path = os.path.join(my_path, "Positive.txt")
neg_path = os.path.join(my_path, "Negative.txt")
fp_positive = open(pos_path)
fp_negative = open(neg_path)
list_pos = fp_positive.read().splitlines()
list_neg = fp_negative.read().splitlines()

if (len(sys.argv)>1 and sys.argv[1] == '--g'):
    judge_sentiment_way = "google"
else:
    judge_sentiment_way = "default"

# start conversation
var = input("What's your name? ")
print ("How's today, " + str(var))

# continue conversation, user type "Bye" to end the while loop
while(var != "Bye"):
    var = input("Talk more? ^_^ (Say 'Bye' to end the conversation.) ")
    words=var.split()

    if(judge_sentiment_way == "default"):
        #process the score of sentiment
        postive_count = 0
        negative_count = 0
        for i in words:
            if i in list_pos:
                postive_count+=1
            if i in list_neg:
                negative_count+=1

        #calculate the sentiment score of the sentence
        sentiment_score = postive_count-negative_count

    elif(judge_sentiment_way == "google"):
        # google sentiment_score
        sentiment_score = get_sentiment(var)

    #response sentence
    postive = ['Great','Cool']
    negative = ['That sucks','Bummer']
    neutral = ['Hmm..','I see']


    if(sentiment_score>0):
        print(random.choice(postive))
    elif (sentiment_score<0):
        print(random.choice(negative))
    else:
        print(random.choice(neutral))
