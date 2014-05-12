
import gandi
import protournoi
import tools
from team import *

def createTeamEmails():
    for t in teams:
        userEmails = teamUserEmails(t)
        gandi.setForward(teamToBase(t), "\n".join(userEmails))


def createProtournoiUsers():
    for t in teams:
        name = teamToProTournoi(t)
        email = teamToEmail(t)
        passwd = teamToPasswd(t)
        protournoi.createNewUser(name, email, passwd)

def sendInitialMailToTeams():
    for t in teams:
        base = teamToBase(t)
        email = teamToEmail(t)
        people = [ u"  - '{}' <{}>".format(*u) for u in teamUsers[t] ]
        subject = cfg.prefix(t)+"Welcome!"
        msg = [
            "Welcome to the petanque tournament!",
            "",
            "You are "+base+" and you have an email alias "+teamToEmail(t)+" that you can use.",
            "Your team is composed of:",
            ] + people + [
                "",
                "In addition to its email alias, your team also has an account on http://www.protournoi.fr",
                "   user: "+teamToProTournoi(t),
                "   pass: "+teamToPasswd(t)
            ]
        users = [email]
        #print("\n".join(msg))
        tools.mail(email, users, subject, msg)
