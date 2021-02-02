def show_messages(messages):
    """Display messages from the list"""
    for message in messages:
        print(f"{message} is available.")

def send_messages(messages, sentMessages):
    """Moves messages to new list once sent"""
    while messages:
        currentMessage = messages.pop()
        print(f"\nSending message: {currentMessage}")
        sentMessages.append(currentMessage)

def showSentMessages(sentMessages):
    """Shows messages that have been sent"""
    print("\nThese messages have been sent: ")
    for sentMessage in sentMessages:
        print(sentMessage)