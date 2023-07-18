class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self, ):
        return f"{self.sender} says to {self.receiver}: {self.content}. " \
               f"Sent: {self.is_sent}"


emails_list = []
command = input()

while command != 'Stop':
    current_sender, current_receiver, current_content = command.split()
    current_email = Email(current_sender, current_receiver, current_content)
    emails_list.append(current_email)
    command = input()

emails_to_send = input().split(', ')
emails_to_send = [int(el) for el in emails_to_send]

for position in emails_to_send:
    emails_list[position].send()

for email in emails_list:
    print(email.get_info())





