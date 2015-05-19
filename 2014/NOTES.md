
    # virtualenv
    workon petanque


    # first phase, use randomFromFoodle = True in team.py
    import team
    team.dumpFoodled()
    # copy paste edit (even later) into data/teams.csv



    import do

    # manual login on protournoi
    # sur la page du tournoi
    do.feedProtournoiInvitedTeams()
    
    # puis les alias mails
    do.gandi.login()
        # manual type passwd
    do.createTeamEmails()

