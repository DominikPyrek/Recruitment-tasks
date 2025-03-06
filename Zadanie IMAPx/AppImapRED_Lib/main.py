from login import login
from fetch import fetch
import email 

session = login()
messeges = fetch(session)

for msg in messeges:
    for response in msg:
        if type(response) is tuple:
            my_msg = email.message_from_bytes((response[1]))
            subject = my_msg['subject']
            if msg.get_content_type() == "multipart":
                for part in msg.walk():
                    if part.get_conten_type() == "multipart":
                        continue
                    if part.get('Content-Disposition') is None:
                        continue

                    file = part.get_filename()
                    if file:
                        filepath = os.path.join('/home/WebDevLinux/Pobrane/', file)
                        with open('/home/WebDevLinux/Pobrane/', 'wb') as f:
                            f.write(part.get_payload(decode=True))
