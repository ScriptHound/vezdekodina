Vezdekod meme bot.

How to deploy
Step one: install requirements.
```
python -m pip install -r requirements.txt
```

Step two: set up PostgreSQL cluster
```
sudo systemctl start postgresql
```

Step three: 
Write your DB credentials into .env and alembic.ini files. Check 
.env_example and alembic_example.ini files for help

Step four:
Run your bot
```
python main.py
```
