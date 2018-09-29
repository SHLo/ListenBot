import sys
import random
import os.path

print (sys.argv)

# read the postive and negative corpus
my_path = os.path.abspath(os.path.dirname(__file__))
pos_path = os.path.join(my_path, "Positive.txt")
neg_path = os.path.join(my_path, "Negative.txt")
fp_positive = open(pos_path)
fp_negative = open(neg_path)
list_pos = fp_positive.read().splitlines()
list_neg = fp_negative.read().splitlines()

# start conversation
var = input("What's your name? ")
print ("How's today, " + str(var))

# continue conversation, user type "Bye" to end the while loop
while(var != "Bye"):
    var = input("Talk more? ^_^ (Say 'Bye' to end the conversation.) ")
    words=var.split()
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
