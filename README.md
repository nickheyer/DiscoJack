# DiscoJack
A fun blackjack bot!

Based on the previously implemented blackjack logic found in "NICKS-GAMEZ", DiscoJack was born. Instead of a simple command-line-based text-response game, DiscoJack has given blackjack (and now roulette) an interface. 

## Prerequisites

- Python must be installed on your machine. [Click Here](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe) for 64-bit installer - During installation, make sure you select the option "Add Python to environmental variables"
- Discord API Key (https://discord.com/developers/applications) - READ [THIS](#further-notes)

## Installation Instructions

Clone
```
git clone https://github.com/nickheyer/DiscoJack
```

CD to Install Folder
```
cd where/you/cloned/discojack
```


Install Requirements
```
pip install -r requirements.txt
```

Run (Windows)
```
python.exe .\DiscoJack.py
```



There are a few commands:
1. "!c! blackjack" summons DiscoJack for a game of blackjack.
2. "!c! roulette" summons DiscoJack for a game of roulette. 
3. "!c! scoreboard" summons a .txt file of all players' current balances. This includes EVERYONE.
4. "!c! add user <user>" adds a user to the admin whitelist. 
5. "!c! list users" lists all users in admin whitelist.
6. "!c! set money <fullplayernameand#number>" sets the current balance of the specified player, can only be done by admin on whitelist. 
  


## Further Notes

- When inviting bot to channel, make sure you allow permissions as such (see below image). For the most part, the bot only requires text channel permissions, but I recommend granting admin permissions to account for further dev. 

![image](https://user-images.githubusercontent.com/60236014/181997169-4b7f3c1d-dc72-4ca2-83db-bcea56814bea.png)

![image](https://user-images.githubusercontent.com/60236014/181997296-0aa40040-34f0-4f56-ab87-34a396493417.png)

- For any other comments or questions, feel free to reach me on discord via NicholasHeyer#4212

