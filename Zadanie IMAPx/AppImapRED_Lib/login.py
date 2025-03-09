import imaplib
import os
from dotenv import load_dotenv

load_dotenv()

# Config
# Fetching all data from .env file for security reasons
username = os.getenv("username")
password = os.getenv("password")
imap_addres = os.getenv("IMAP")
imap_port = os.getenv("port")

# Connect and Auth
def login():
    imap_connect = imaplib.IMAP4_SSL(imap_addres, imap_port)
    imap_connect.login(username, password)
    imap_connect.select('inbox')
    return imap_connect

