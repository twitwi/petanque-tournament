
import gandi
import protournoi
import tools
from team import *

def createTeamEmails():
    for t in teams:
        userEmails = teamUserEmails(t)
        gandi.setForward(teamToBase(t), "\n".join(userEmails))

def printAllTeamAliases():
    print(",".join([ teamToEmail(t) for t in teams ]))
        

def createProtournoiUsers():
    for t in teams:
        name = teamToProTournoi(t)
        email = teamToEmail(t)
        passwd = teamToPasswd(t)
        protournoi.createNewUser(name, email, passwd)

def feedProtournoiInvitedTeams():
    for t in teams:
        people = u"{}: {}".format(t, u" / ".join(teamUserAliases(t)))
        print(people)
        protournoi.invite(people)
    protournoi.submitInvites()

def printTeams():
    for t in teams:
        base = teamToBase(t)
        email = teamToEmail(t)
        people = [ u"  - '{}' <{}>".format(*u) for u in teamUsers[t] ]
        print(email)
        print("\n".join(people))

def sendInitialMailToTeams(reallySend = False):
    for t in teams:
        base = teamToBase(t)
        email = teamToEmail(t)
        people = [ u"  - '{}' <{}>".format(*u) for u in teamUsers[t] ]
        subject = cfg.prefix(t)+"Welcome!"
        msg = [
            "Welcome to the petanque tournament!",
            "",
            "You are "+base+" and you have an email alias "+teamToEmail(t)+" that corresponds to your team, composed of:",
            ] + people + [
                "",
                # "In addition to its email alias, your team also has an account on http://www.protournoi.fr",
                # "   user: "+teamToProTournoi(t),
                # "   pass: "+teamToPasswd(t)
                ""
            ]
        users = [email]
        if reallySend:
            tools.mail(email, users, subject, msg)
        else:
            print("\n".join(msg))



# reload(data) ; reload(team) ; reload(do) ; do.printTeams()
