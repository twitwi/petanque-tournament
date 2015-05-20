
import data as cfg
import hashlib
import random
import tools

randomFromFoodle = False

teams = [ '%02d' % i for i in range(1,9)] # 1 to 9 inclusive

users = []
teamUsers = {}

if randomFromFoodle:
    usersCSV = tools.readCSVTable('data/foodle.csv')
    users = [ (t[0], t[1]) for t in usersCSV ]
    random.seed(cfg.seed + 100)
    random.shuffle(users)
    groupedUsers = tools.distributeInGroups(users, len(teams))
    
    for i in range(len(teams)):
        t = teams[i]
        teamUsers[t] = filter(None, list(groupedUsers[i]))
    def dumpFoodled():
        for t in teams:
            for u in teamUsers[t]:
                print(u"{};{};{}".format(t, u[0], u[1]))
else:
    teamsCSV = tools.readCSVTable('data/teams.csv')
    users = [ (t[1], t[2]) for t in teamsCSV ]
    random.seed(cfg.seed + 100)
    for t in teams:
        teamUsers[t] = []
    for t in teamsCSV:
        teamUsers[t[0]] += [(t[1], t[2])]

def teamToBase(t):
    return 'team-'+t

def teamToEmail(t):
    return teamToBase(t)+'@'+cfg.emailDomain

def teamUserAliases(t):
    return [u[0] for u in teamUsers[t]]

def teamUserEmails(t):
    return [u[1] for u in teamUsers[t]] + [cfg.adminEmail]

def teamToProTournoi(t):
    return 'car'+teamToBase(t)

def teamToPasswd(t):
    return hashlib.sha1(cfg.salt+t+cfg.salt).hexdigest()[0:8]

def teamContext(t):
    pass
