# Fetching data from email with topic
def fetch(login):
    import email
    import os
    from dotenv import load_dotenv

    load_dotenv()
    imap_connect = login

    what_subject_to_search_for = os.getenv("what_subject_to_search_for")

    _, data = imap_connect.search(None, f'SUBJECT "{what_subject_to_search_for}"')
    mails_ids = data[0].split()
    return mails_ids
