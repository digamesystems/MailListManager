import smtplib
from email.message import EmailMessage

# TODO move config and init_config to a separate file or environment variables
config = {}

def init_config():
    config['MAIL_SERVER'] ='smtp-mail.outlook.com'
    config['MAIL_PORT'] = 587
    config['MAIL_USER'] = 'john.price@digamesystems.com'
    config['MAIL_PASSWORD'] = 'Zena7fkl!'
    config['MAIL_USE_TLS'] = True
    config['MAIL_USE_SSL'] = False


def send_email(subject, sender, recipient, text_body, html_body=""):
    try:
        # Set the subject and body of the email
        body = text_body
        em = EmailMessage()
        em['From'] = sender # os.getenv('MAIL_USER')
        em['To'] = recipient
        em['Subject'] = subject
        em.html = text_body
        em.set_content(em.html, subtype='html')

        print("In send_email")
        print("  Subject: ", subject)
        print("  Sender: ", sender) 
        print("  Recipient: ", recipient)
        print("  Server: ", config["MAIL_SERVER"])   
        print("  User: ", config["MAIL_USER"])
        # Log in and send the email
        try:
            with smtplib.SMTP(config["MAIL_SERVER"], config["MAIL_PORT"]) as smtp:
                smtp.set_debuglevel(1)
                print('smtp: ', smtp.command_encoding )
                smtp.ehlo()
                smtp.starttls()
                smtp.login(config["MAIL_USER"], config["MAIL_PASSWORD"])
                smtp.sendmail(config["MAIL_USER"], recipient, em.as_string())     

        except Exception as e:
            print("Send Email Error: ", e)
            return str(e)
        
        print("Email sent successfully!")               

    except Exception as e:
        return  str(e)
    

if __name__ == "__main__":
    init_config()
    send_email("Test Subject", 
               "john.price.price@digamesystems.com",
               "john.price@digamesystems.com",  
               "<h1>hello.</h1>")
    
