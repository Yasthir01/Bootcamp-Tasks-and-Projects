#An SMS Simulation


class Email:


    def __init__(self, email_contents, from_address, has_been_read, is_spam):
        """Initialize the attributes"""
        self.from_address = from_address
        self.has_been_read = False
        self.is_spam = False
        self.email_contents = email_contents


    def mark_as_read(self):
        """Change has_been_read to True"""
        self.has_been_read = True


    def mark_as_spam(self):
        """Change is_spam to True"""
        self.is_spam = True


    def add_email(self, new_email):
        self.inbox.append(new_email)


    def get_count(self):
        """Returns the number of messages in the store"""
        return len(inbox)


    def get_email(self, index):
        """returns the contents of an email in the list"""
        inbox[index].mark_as_read()
        return inbox[index].email_contents
    

    def get_unread_emails(self):
        """Return a list of all the emails that haven't been read"""
        unread = []
        for email in inbox:
            if email.has_been_read == False:
                unread.append(email)
        return unread 


    def get_spam_emails(self):
        """Return a list of all the emails that have been marked as spam"""
        spam = []
        for email in inbox:
            if email.is_spam == True:
                spam.append(email)
        return spam 


    def delete(self, index):
        """Deletes an email in the inbox"""
        del inbox[index]

 
inbox = []  # this is where all the emails will be stored

user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/quit?")
    if user_choice == "read":
        user_input = input("Enter index of email to read: ")
        email_content = get_email(user_input)
        print(email_content)

    elif user_choice == "mark spam":
        user_input = input("Enter index of email to mark as spam: ")
        inbox[user_input].mark_as_spam()

    elif user_choice == "send":
        content = input("Enter your message: ")
        add_email(content)

    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
