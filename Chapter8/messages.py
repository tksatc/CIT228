#def show_messages(messages):
 #   """Display messages from the list"""
  #  for message in messages:
   #     print(f"{message} is available.")

#def send_messages(messages, sentMessages):
 #   """Moves messages to new list once sent"""
  #  while messages:
   #     currentMessage = messages.pop()
    #    print(f"\nSending message: {currentMessage}")
     #   sentMessages.append(currentMessage)

#def showSentMessages(sentMessages):
 #   """Shows messages that have been sent"""
  #  print("\nThese messages have been sent: ")
   # for sentMessage in sentMessages:
    #    print(sentMessage)

#import message_activity
#from message_activity import show_messages
#from message_activity import showSentMessages as sm
import message_activity as messAct
#from message_activity import *

texts = ["TTYL", "Be home soon", "Got held up", "Will you pick up milk?"]
sentTexts = []

print("\n--------Available Messages--------")
messAct.show_messages(texts)
messAct.send_messages(texts[:], sentTexts)
messAct.showSentMessages(sentTexts)

print("\nTexts list contents: ", texts)
print("\nsentTexts list contents: ", sentTexts, "\n")
