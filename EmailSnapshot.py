import easyimap as e
import pendulum
import yagmail


email_id = 'Your email address here'
password = 'Your password here'

# Creating an instance of easyimap object 
server = e.connect('imap.gmail.com', email_id, password)

# Using listids method to get 5 unread emails    
unread_emails = server.listids(5)

# Creating a new txt file and writing the current timestamp using pendulum module
with open('data.txt','w') as file:
    file.write(f"EMAILS: {pendulum.now()}\n")

# Reading the unread emails from the server and appending those to the txt file
for i in unread_emails:
    email = server.mail(i)
    content = f"\n{unread_emails.index(i)+1}.SUBJECT:{email.title}\nFROM:{email.from_addr}\nBODY:{email.body[0:50]}\n"
    with open('data.txt', 'a') as file:
        file.write(content)

# Sending the txt file contents as an email using yagmail module
with open('data.txt', 'r') as file:
    email_body=file.read()
    username1='Your email'
    password1='Your password'

    reciever = 'The reciever email here'
    subject = 'Compiled Email update'
    contents = content

    Email = yagmail.SMTP(user=username1, password=password1)
    Email.send(to=reciever, subject=subject, contents=email_body)
    print('email sent!')
