from AppImapRED_Lib.processingEmails import processingEmails
import time
if __name__ == "__main__":
    while True:
        processingEmails()
        print("Emails Checked")
        time.sleep(60)

