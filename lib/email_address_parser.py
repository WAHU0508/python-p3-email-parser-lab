# your code goes here!
import re
class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses
    def parse(self):
        comma = re.compile(r'[,\s]+')
        email_list = comma.split(self.email_addresses)
        sorted_emails = sorted(email_list)
        pattern = re.compile(r'\b[A-z]+@+[A-z]+\.+[A-z]+\b')
        return [email for email in sorted_emails if pattern.findall(email)]
    
print(EmailAddressParser("talk@talk.com who john.jones@flatironschool.com alexa@amazon.com what").parse())