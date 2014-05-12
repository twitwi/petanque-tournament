
import csv
import smtplib
from email.mime.text import MIMEText
import data as cfg
from itertools import izip_longest


def readCSVTable(f):
    res = []
    with open(f, 'rb') as csvfile:
        r = csv.reader(csvfile, delimiter=';')
        for row in r:
            res += [[unicode(cell, 'utf-8') for cell in row]]
    return res

def mail(src, dsts, subject, contentLines):
    s = smtplib.SMTP(cfg.smtpHost, cfg.smtpPort)
    s.starttls()
    s.login(cfg.smtpLogin, cfg.smtpPass)

    content = "\n".join(contentLines)
    msg = MIMEText(content.encode('utf-8'), 'plain','utf-8')
    msg['Subject'] = subject
    msg['From'] = src
    msg['To'] = ', '.join(dsts)
    s.sendmail(src, dsts, msg.as_string())

    s.quit()
    # tools.mail('rem@heeere.com', ['team-01@heeere.com', 'team-04@heeere.com'], 'test mail 1', ['hello men', 'what is the issue dear?'])

def groupby_itertools(iterable, n, padvalue=None):
    return izip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

def distributeInGroups(iterable, nGroups):
    return zip(* list(groupby_itertools( iterable, nGroups )))
