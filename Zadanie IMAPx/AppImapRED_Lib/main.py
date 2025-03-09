from login import login
from fetchMailIds import fetch
from dotenv import load_dotenv
import email, os
load_dotenv()

save_to = os.getenv("save_to")

session = login()
mes_ids = fetch(session)

for mes_id in mes_ids:
    _, msg_data = session.fetch(mes_id, '(RFC822)')
    for response in msg_data:

        if isinstance(response, tuple):
            
            msg = email.message_from_bytes(response[1])
            subject = msg["Subject"]

            if isinstance(subject, bytes):
                subject = subject.decode()

            if msg.get_content_maintype() == 'multipart':
                for part in msg.walk():
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue

                    filename = part.get_filename()
                    if filename:
                        filepath_file = os.path.join(save_to, filename)
                        with open(filepath_file, 'wb') as f:
                            f.write(part.get_payload(decode=True))
                        filepath_subject = os.path.join(save_to, subject)
                        with open(filepath_subject, "w") as f:
                            f.write(subject)
                        session.copy(mes_id, "OLD-RED")
                        session.store(mes_id, '+FLAGS', '\\Deleted')

            
