# ListenBot
In this lab you will practice Python basics covered in the class to create a simple chatbot. 

# Step 0: Install Python and set up your development environment
Go to https://www.python.org/ and click on Downloads > Python 3.7.0 (should automatically detect your operating system). Follow instructions to install Python after you download.

Open a Terminal and check your Python version using the commands $ python --version and $ python3 --version. Make sure at least one of these is consistent with the version you downloaded. Then use the command $ python3 to start the interactive Python console. Try a few commands from class to see that it works as expected.

Next choose an IDE and set it up.

The simplest option is using a text editor, such as Sublime, to write your code and use a terminal window to run them.
The instructor will be trying PyCharm this quarter.
Alternatives include Eclipse with PyDev, LiClipse, and Anaconda, among others.
If you are having trouble, talk to the instructor or TAs first thing during the lab to sort things out as soon as possible so you can get started on the actual lab. You can also try Google Cloud instructions for setting up your Python development environments, which takes a slightly different route.

# Step 1: Create project/folder and add data
Create a new project in your IDE (or a folder on your system) named "lab-1". To keep the submission simple in this lab you will write all your Python code in one file named chatbot.py. Create this file in lab-1/.

# Step 2: Barebones interactive chatbot
Inside chatbot.py You will first create a simple interactive loop between user input and program output. Before entering the loop, your program should prompt the user to request their input (e.g. "Hi, how can I help you?"). At each iteration of the loop, the program should take user input (typed onto the terminal pressing 'Enter' at the end) and then output simple meta information about that input (e.g. "You entered X letters and Y words"). Also add a way to exit the loop; for example, if the user types "Bye" the loop should end and your program should halt after a final prompt to the user to acknowledge that the interaction has ended.

# Step 3: Simple ListenBot
Next you will upgrade your chatbot to be a "good listener." Do not worry about deleting or overwriting things you did in the previous step. Before entering into the interactive loop, your chatbot should ask the user's name and remember it throughout the chat. It should also prompt the user to talk about something (e.g. "How was your day, Maya?" As part of the loop, the chatbot should analyze the user's input and decide whether to give a positive, negative, or neutral response. To analyze the input, make a fixed list of positive and negative words and determine the number of positive and negative words that occur in the user's input. Your list of positive and negative words do not have to be too long, just enough to showcase a simple conversation. Optionally you can download the lists linked above and load them into your program.

The chatbot should respond based on the number of positive and negative words in the user's input. Your chatbot should have at least two different responses of each type and should alternate between responses, e.g.:

Positive responses: "Great" "Cool"
Negative responses: "That sucks" "Bummer"
Neutral responses: "Hmm.." "I see"
As before, there should be at least one way to end the conversation. You can make the ways to end the conversation known to the user in your earlier prompt or some where during the conversation.

# Step 4: Improved ListenBot
Now test your chatbot yourself and optionally with a peer. Based on breakdowns or awkwardness in these tests choose one additional improvement and implement it. Make sure you add a comment in your code to describe the improvement.

# (Optional) Step 5: ListenBot with Sentiment Analysis
If you have extra time you can upgrade the sentiment analysis (deciding whether user sentence is positive, negative, or neutral) using a Google Web Service. Download get_sentiment.py, inspect it, and import it into your program. Currently the get_sentiment() function returns a boolean. You will need to change it so it returns one of three things (positive, negative, neutral). You might want to check out the sentiment analysis web service documentation. Then update your chatbot to use the get_sentiment() function. 

If you complete this part of the lab, be sure to keep the earlier version of the sentiment analysis (Step 3) in chatbot.py as the default and add a comment to explain how to try the upgraded version.  Also submit get_sentiment.py or transfer its content into chatbot.py for submitting the lab.

# Step 6: Submit your code on Canvas
Complete this lab by submitting your chatbot.py script on Canvas, by Oct 2 Tuesday, 11:59pm. We will test your chatbot with a simple dialog to verify that:

It asks for the user's name and demonstrates that it remembers the name
Responds appropriately to a clearly positive, negative, and neutral statement
Has a way of ending the chat
We will inspect the code in addition to the interaction to make sure that an improvement was implemented for Step 4. See Canvas for a grading rubric.
