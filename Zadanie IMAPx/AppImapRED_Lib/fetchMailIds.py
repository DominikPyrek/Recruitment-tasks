import email
# Fetching data from email with topic RED
def fetch(login):
    imap_connect = login
    _, data = imap_connect.search(None, 'SUBJECT "RED"')
    mails_ids = data[0].split()
    return mails_ids

