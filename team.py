
import data as cfg
import hashlib
import random
import tools

teams = [ '%02d' % i for i in range(1,16)] # 1 to 15 inclusive
#teams = [ '%02d' % i for i in range(1,4)]

usersCSV = tools.readCSVTable('data/foodle.csv')
users = [ (t[0], 'NO'+t[1]) for t in usersCSV ]
random.seed(cfg.seed + 100)
random.shuffle(users)
groupedUsers = tools.distributeInGroups(users, len(teams))


teamUsers = {}
for i in range(len(teams)):
    t = teams[i]
    teamUsers[t] = filter(None, list(groupedUsers[i]))

def teamToBase(t):
    return 'team-'+t

def teamToEmail(t):
    return teamToBase(t)+'@'+cfg.emailDomain

def teamUserEmails(t):
    return [u[1] for u in teamUsers[t]] + [cfg.adminEmail]

def teamToProTournoi(t):
    return 'car'+teamToBase(t)

def teamToPasswd(t):
    return hashlib.sha1(cfg.salt+t+cfg.salt).hexdigest()[0:8]
