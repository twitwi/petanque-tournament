

- archived 2014
- kept all pythons
- redone a data directory
  - (outside for email privacy and it contains a config in `__init__.py`)
  - put the csv from foodle
  - curated it and added other people
- checked that the team emails still exist (they forward to remi@heeere.com)
- `sudo pip install selenium --upgrade`

Generation of teams

- in team.py
  - set the number of teams (range(1,9) for 8 teams)
  - set randomFromFoodle to True
  - iterate with changing the seed (in `data/__init__.py`) and doing `python -c "import team ; team.dumpFoodled()"`
  - then save the output to `data/teams.csv` and switch the boolean to False again

Update of email aliases

```
python
>>> import do
>>> do.gandi.login()
>>> do.createTeamEmails()
```

Protournoi setup: manually this year

Fill in the framapad, need pretty list of teams

```
python
>>> import do
>>> do.printTeams()
```

Sending emails to teams

- preview: `do.sendInitialMailToTeams()`
- after previewing (in the same way), need to edit `tools.py`
- then: `do.sendInitialMailToTeams(True)`

