from email.message import EmailMessage
import smtplib 

SSL_PORT = 587

gateway_domains = {
    'att' : '@mms.att.net',
	'tmobile' : '@tmomail.net',
	'verizon' : '@vtext.com',
	'sprint' : '@page.nextel.com',
    'shaw' : '@txt.shawmobile.ca', 
    'virgin' : '@vmobile.com',
    'rogers' : '@pcs.rogers.com'
}


def send_email(to, subject, body): 
    # bot gmail credentials 
    un = "cwlwebscrape@gmail.com" 
    pw = "xpqkzuwpnyskjvbe"

    message = EmailMessage()
    message['from'] = un
    message['to'] = to 
    message['subject'] = subject 
    message.set_content(body) 

    # initialize STMP server 
    with smtplib.SMTP('smtp.gmail.com', SSL_PORT) as smtp: 
        smtp.starttls() 
        smtp.login(un, pw)
        print('Sending Email to %s...' % to)
        smtp.send_message(message)
        print('Sent')


def parse_phone_number(number, carrier): 
    print('Parsing %s: %s' % (carrier, number))
    carr = carrier.lower()
    num = list(number) 
    num.append('@')
    if 'shaw' in carr: 
        num += list('txt.shawmobile.ca')
    elif 'at&t' in carr: 
        num += list('txt.att.net')
    elif 'virgin' in carr: 
        num += list('vmobl.com')
    elif 'verizon' in carr: 
        num += list('vtext.com')
    elif 't-mobile' in carr:
        num += list('tmomail.net')
    elif 'rogers' in carr: 
        num += list('pcs.rogers.com')
    else: 
        print('Error: %s is not supported' % carrier)
    return "".join(num)


if __name__ == '__main__': 
    # to = 'ngjustin2002@gmail.com'
    carrier = 'shaw'
    to = "1234567890"
    subject = 'Test' 
    body = 'Hello World'
    send_email(parse_phone_number(to, carrier), subject, body)