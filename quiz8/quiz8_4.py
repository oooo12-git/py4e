msg = '''This automatic notification
You can modify
    From louis@media.berkeley.edu Fri Jan 4
    Return-Path: postmaster@collab.sakaiproject.org
    Received: from murder (mail.umich.edu)'''
words = msg.split()
email_address = []
for word in words : 
    if '@' in word :
        email_address.append(word)

print(email_address)