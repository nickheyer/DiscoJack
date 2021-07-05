# DiscoJack
A fun blackjack bot!

Based on the previously implemented blackjack logic found in "NICKS-GAMEZ", DiscoJack was born. Instead of a simple command-line-based text-response game, DiscoJack has given blackjack an interface. 

There are a few commands:
1. "!c! blackjack" summons DiscoJack for a game. 
2. "!c! bj stop" ends DiscoJack's game (if entered during your 'bet' prompt).
3. "!c! scoreboard" summons a .txt file of all players' current balances. This includes EVERYONE.
4. "!c! add user <user>" adds a user to the admin whitelist. 
5. "!c! list users" lists all users in admin whitelist.
6. "!c! set money <fullplayernameand#number>" sets the current balance of the specified player, can only be done by admin on whitelist. 
  
A few caveats: I wrote the functionality for this bot in about 12 hours. It's not perfect. Multiple simultaneous inputs are going to cause errors and require that the bot be restarted (just close the .py window and double click discojack.py again). Discord's API can also be finicky, sometimes a previous message will be recorded as an input when the following message was the intended input - this is the fault of Discord's API. 

To install and run the bot, you need to create a new application via (https://discord.com/developers/applications). Once you have a TOKEN provided to you by discord, you can replace "TOKEN GOES HERE" (check the beginning of DiscoPy.py) with your token. Following that, double-click DiscoPy.py and make sure you manually input your discord username into "whitelisted.txt". You should be good to go!

Message me on discord if you have any questions! ~ NastyNick#4212
