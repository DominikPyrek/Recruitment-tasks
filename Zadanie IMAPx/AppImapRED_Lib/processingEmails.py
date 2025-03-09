def processingEmails():
    try:
        from .login import login
        from .fetchMailIds import fetch
        from dotenv import load_dotenv
        import email, os

        load_dotenv()

        save_to = os.getenv("save_to")
        session = login()
        mes_ids = fetch(session)

        for mes_id in mes_ids:
            _, msg_data = session.fetch(mes_id, '(RFC822)')

            for response in msg_data:
                #Getting the subject of email
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    subject = msg["Subject"]
                    if isinstance(subject, bytes):
                        subject = subject.decode()
                    #Checking if email has a file attached to it
                    if msg.get_content_maintype() == 'multipart':
                        for part in msg.walk():
                            if part.get_content_maintype() == 'multipart':
                                continue
                            if part.get('Content-Disposition') is None:
                                continue
                            
                            filename = part.get_filename()
                            #writing attachment and text file with subject
                            if filename:
                                filepath_file = os.path.join(save_to, filename)
                                try:
                                    with open(filepath_file, 'wb') as f:
                                        f.write(part.get_payload(decode=True))
                                except Exception as e:
                                    print(f"Couldn't write the file {filename}, Error:{e}")

                                filepath_subject = os.path.join(save_to, subject)
                                try: 
                                    with open(filepath_subject, "w") as f:
                                        f.write(subject)
                                except Exception as e:
                                    print(f"Couldn't write the subject {subject}, Error:{e}")        

                                #sending email to OLD-RED folder
                                folder_to_send_to_on_email = os.getenv("folder_to_send_to_on_email")
                                session.copy(mes_id, folder_to_send_to_on_email)
                                session.store(mes_id, '+FLAGS', '\\Deleted')
    except Exception as e:
        print(f"Error with email handling: {e}")
    finally:
        session.logout()