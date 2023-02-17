## Python Automation Project which Reads your Recent Emails, Creates a Summary of each email and then Sends that Summary back to you Compiled together in a Single Email.

### Description
This code reads the 5 most recent unread emails in your Gmail inbox, writes the details of these emails to a text file, and sends the contents of this text file to a recipient email address using Yagmail.

The script is built using Python 3 and makes use of the following external modules: easyimap, pendulum, and yagmail.

### Requirements
In order to run this script, you will need to have Python 3 installed on your computer. You will also need to install the following external modules using pip:

easyimap
pendulum
yagmail

### Usage
1. Open the script in your preferred Python environment.
2. Replace Your email address here and Your password here with your Gmail email address and password respectively.
3. Replace The reciever email here with the email address of the recipient to whom you want to send the compiled email update.
4. Save and run the script.
5. The script will write the details of the 5 most recent unread emails in your Gmail inbox to a text file named data.txt. It will then send the contents of this text file as an email to the recipient email address that you specified.

### Note
- If you are using 2-Step Verification in your Gmail account, you may need to generate an App Password to use in place of your regular password in the script.
- Make sure to keep your email and password safe and secure. It is recommended to use environment variables to store sensitive information rather than directly including them in the script.
