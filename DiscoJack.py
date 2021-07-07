import discord
import random
from pprint import pprint
import sys
import os
from time import sleep
import re
import json

TOKEN = "ENTER YOUR TOKEN HERE"

intents = discord.Intents.all()
client = discord.Client(intents = intents)
embed = discord.Embed() 

def rand_number(num):
  return random.randint(1, num)

score_board_txt = os.path.join(os.path.dirname(__file__), f'score_board.txt')
allowed_persons_dir = os.path.join(os.path.dirname(__file__), f'whitelisted.txt')
bank_file_dir = os.path.join(os.path.dirname(__file__), f'bank_file.json')
script_path = sys.path[0]


with open(allowed_persons_dir, "a") as instance_2:
  instance_2.write("")
with open(score_board_txt, "a") as instance_3:
  instance_3.write("")


@client.event
async def on_ready():
  print("Bot is ready to party, logged in as {0.user}.".format(client))
  try:
    with open(bank_file_dir, "r") as bnkfl_dict_r:
      bnkfl_val = json.load(bnkfl_dict_r)
    with open(bank_file_dir,"w") as bnkfl:
      bnk_val = bnkfl_val
      for guild in client.guilds:
          for member in guild.members:
            if (f"{member.name}#{member.discriminator}") not in bnk_val.keys() and member.bot == False:
              bnk_val[f"{member.name}#{member.discriminator}"] = [100]
      json.dump(bnk_val, bnkfl)
  except:
    with open(bank_file_dir,"w") as bnkfl_w:
      bnk_val = {}
      for guild in client.guilds:
          for member in guild.members:
            if (f"{member.name}#{member.discriminator}") not in bnk_val.keys() and member.bot == False:
              bnk_val[f"{member.name}#{member.discriminator}"] = [100]
      json.dump(bnk_val, bnkfl_w)

@client.event
async def on_message(message):
  with open(allowed_persons_dir, "r") as listed_users:
    allowed_users = listed_users.read()
  if message.author == client.user:
    return
  elif message.content.startswith("!c! blackjack"):
      #For BlackJack functionality
      class Cards:
            def __init__(self, name, number, value, face):
              self.name = name
              self.number = number
              self.value = value
              if face == "🃁":
                self.face = (discord.File(f"{script_path}\\Cards\\AD.png"))
              elif face == "🃂":
                    self.face = (discord.File(f"{script_path}\\Cards\\2D.png"))
              elif face == "🃃":
                    self.face = (discord.File(f"{script_path}\\Cards\\3D.png"))
              elif face == "🃄":
                    self.face = (discord.File(f"{script_path}\\Cards\\4D.png"))
              elif face == "🃅":
                    self.face = (discord.File(f"{script_path}\\Cards\\5D.png"))
              elif face == "🃆":
                    self.face = (discord.File(f"{script_path}\\Cards\\6D.png"))
              elif face == "🃇":
                    self.face = (discord.File(f"{script_path}\\Cards\\7D.png"))
              elif face == "🃈":
                    self.face = (discord.File(f"{script_path}\\Cards\\8D.png"))
              elif face == "🃉":
                    self.face = (discord.File(f"{script_path}\\Cards\\9D.png"))
              elif face == "🃊":
                    self.face = (discord.File(f"{script_path}\\Cards\\10D.png"))
              elif face == "🃋":
                    self.face = (discord.File(f"{script_path}\\Cards\\JD.png"))
              elif face == "🃍":
                    self.face = (discord.File(f"{script_path}\\Cards\\QD.png"))
              elif face == "🃎":
                    self.face = (discord.File(f"{script_path}\\Cards\\KD.png"))
            def __repr__(self):
              return (f"{self.name} - {self.value}")
      #CARD DEFINITIONS
      #Diamonds
      ace_of_diamonds = Cards("Ace of Diamonds", 1, 11, "🃁")
      two_of_diamonds = Cards("Two of Diamonds", 2, 2, "🃂")
      three_of_diamonds = Cards("Three of Diamonds", 3, 3, "🃃")
      four_of_diamonds = Cards("Four of Diamonds", 4, 4, "🃄")
      five_of_diamonds = Cards("Five of Diamonds", 5, 5, "🃅")
      six_of_diamonds = Cards("Six of Diamonds", 6, 6, "🃆")
      seven_of_diamonds = Cards("Seven of Diamonds", 7, 7, "🃇")
      eight_of_diamonds = Cards("Eight of Diamonds", 8, 8, "🃈")
      nine_of_diamonds = Cards("Nine of Diamonds", 9, 9, "🃉")
      ten_of_diamonds = Cards("Ten of Diamonds", 10, 10, "🃊")
      jack_of_diamonds = Cards("Jack of Diamonds", 11, 10, "🃋")
      queen_of_diamonds = Cards("Queen of Diamonds", 12, 10, "🃍")
      king_of_diamonds = Cards("King of Diamonds", 13, 10, "🃎")
      #Clubs
      ace_of_clubs = Cards("Ace of Clubs", 14, 11, "🃁")
      two_of_clubs = Cards("Two of Clubs", 15, 2, "🃂")
      three_of_clubs = Cards("Three of Clubs", 16, 3, "🃃")
      four_of_clubs = Cards("Four of Clubs", 17, 4, "🃄")
      five_of_clubs = Cards("Five of Clubs", 18, 5, "🃅")
      six_of_clubs = Cards("Six of Clubs", 19, 6, "🃆")
      seven_of_clubs = Cards("Seven of Clubs", 20, 7, "🃇")
      eight_of_clubs = Cards("Eight of Clubs", 21, 8, "🃈")
      nine_of_clubs = Cards("Nine of Clubs", 22, 9, "🃉")
      ten_of_clubs = Cards("Ten of Clubs", 23, 10, "🃊")
      jack_of_clubs = Cards("Jack of Clubs", 24, 10, "🃋")
      queen_of_clubs = Cards("Queen of Clubs", 25, 10, "🃍")
      king_of_clubs = Cards("King of Clubs", 26, 10, "🃎")
      #Hearts
      ace_of_hearts = Cards("Ace of Hearts", 27, 11, "🃁")
      two_of_hearts = Cards("Two of Hearts", 28, 2, "🃂")
      three_of_hearts = Cards("Three of Hearts", 29, 3, "🃃")
      four_of_hearts = Cards("Four of Hearts", 30, 4, "🃄")
      five_of_hearts = Cards("Five of Hearts", 31, 5, "🃅")
      six_of_hearts = Cards("Six of Hearts", 32, 6, "🃆")
      seven_of_hearts = Cards("Seven of Hearts", 33, 7, "🃇")
      eight_of_hearts = Cards("Eight of Hearts", 34, 8, "🃈")
      nine_of_hearts = Cards("Nine of Hearts", 35, 9, "🃉")
      ten_of_hearts = Cards("Ten of Hearts", 36, 10, "🃊")
      jack_of_hearts = Cards("Jack of Hearts", 37, 10, "🃋")
      queen_of_hearts = Cards("Queen of Hearts", 38, 10, "🃍")
      king_of_hearts = Cards("King of Hearts", 39, 10, "🃎")
      #Spades
      ace_of_spades = Cards("Ace of Spades", 40, 11, "🃁")
      two_of_spades = Cards("Two of Spades", 41, 2, "🃂")
      three_of_spades = Cards("Three of Spades", 42, 3, "🃃")
      four_of_spades = Cards("Four of Spades", 43, 4, "🃄")
      five_of_spades = Cards("Five of Spades", 44, 5, "🃅")
      six_of_spades = Cards("Six of Spades", 45, 6, "🃆")
      seven_of_spades = Cards("Seven of Spades", 46, 7, "🃇")
      eight_of_spades = Cards("Eight of Spades", 47, 8, "🃈")
      nine_of_spades = Cards("Nine of Spades", 48, 9, "🃉")
      ten_of_spades = Cards("Ten of Spades", 49, 10, "🃊")
      jack_of_spades = Cards("Jack of Spades", 50, 10, "🃋")
      queen_of_spades = Cards("Queen of Spades", 51, 10, "🃍")
      king_of_spades = Cards("King of Spades", 52, 10, "🃎")
      list_of_cards = [
      #Diamonds
      ace_of_diamonds,
      two_of_diamonds,
      three_of_diamonds,
      four_of_diamonds,
      five_of_diamonds,
      six_of_diamonds,
      seven_of_diamonds,
      eight_of_diamonds,
      nine_of_diamonds,
      ten_of_diamonds,
      jack_of_diamonds,
      queen_of_diamonds,
      king_of_diamonds,
      #Clubs
      ace_of_clubs,
      two_of_clubs,
      three_of_clubs,
      four_of_clubs,
      five_of_clubs,
      six_of_clubs,
      seven_of_clubs,
      eight_of_clubs,
      nine_of_clubs,
      ten_of_clubs,
      jack_of_clubs,
      queen_of_clubs,
      king_of_clubs,
      #Hearts
      ace_of_hearts,
      two_of_hearts,
      three_of_hearts,
      four_of_hearts,
      five_of_hearts,
      six_of_hearts,
      seven_of_hearts,
      eight_of_hearts,
      nine_of_hearts,
      ten_of_hearts,
      jack_of_hearts,
      queen_of_hearts,
      king_of_hearts,
      #Spades
      ace_of_spades,
      two_of_spades,
      three_of_spades,
      four_of_spades,
      five_of_spades,
      six_of_spades,
      seven_of_spades,
      eight_of_spades,
      nine_of_spades,
      ten_of_spades,
      jack_of_spades,
      queen_of_spades,
      king_of_spades
      ]
      blank_card = (discord.File(f"{script_path}\\Cards\\gray_back.png"))
      with open(bank_file_dir, "r") as bnkfl_r:
        loaded_bnkfl_r = json.load(bnkfl_r)
        players_val = loaded_bnkfl_r[f"{message.author.name}#{message.author.discriminator}"]
        await message.channel.send(f"{message.author}'s current bankroll is ${sum(players_val)}. Let the games begin! ('!c! bj stop' to end session)") ; sleep(1)
        while True:
            await message.channel.send("How much would you like to bet?")
            bet = await client.wait_for('message')
            try:
              if bet.content[0] == "$":
                bet.content = bet.content[1:]
              ismoney = type(int(bet.content)) is int
            except:
              await message.channel.send("That isn't money...") ; sleep(3)
              break
            if sum(players_val) >= int(bet.content) and ismoney == True:
              await message.channel.send(f"You bet: ${bet.content}")
              #Generating dealer cards
              dealer_first = random.randint(1,52)
              for x in list_of_cards:
                if x.number == dealer_first:
                  dealer_first = x
                  dealer_first_val = x.value
                  dealer_first_face = x.face
                else:
                  pass
              dealer_second = random.randint(1,52)
              for x in list_of_cards:
                if x.number == dealer_second:
                  dealer_second = x
                  dealer_second_val = x.value
                  dealer_second_face = x.face
                else:
                  pass
              #Contingency for dealer double aces on first draw
              while dealer_first_val == dealer_second_val and dealer_first_val == 11 or dealer_first == dealer_second:
                dealer_first = random.randint(1,52)
                for x in list_of_cards:
                  if x.number == dealer_first:
                    dealer_first = x
                    dealer_first_val = x.value
                    dealer_first_face = x.face
                  else:
                    pass
                dealer_second = random.randint(1,52)
                for x in list_of_cards:
                  if x.number == dealer_second:
                    dealer_second = x
                    dealer_second_val = x.value
                    dealer_second_face = x.face
                  else:
                    pass  
              dealer_total = dealer_first_val + dealer_second_val
              #Generating player cards
              player_first = random.randint(1,52)
              for x in list_of_cards:
                if x.number == player_first:
                  player_first = x
                  player_first_val = x.value
                  player_first_face = x.face
                else:
                  pass
              player_second = random.randint(1,52)
              for x in list_of_cards:
                if x.number == player_second:
                  player_second = x
                  player_second_val = x.value
                  player_second_face = x.face
                else:
                  pass   
              #Contingency for player double aces on first draw
              while (player_first_val == player_second_val and player_first_val == 11) or player_first == player_second or player_first == dealer_first or player_first == dealer_second or player_second == dealer_first or player_second == dealer_second:
                player_first = random.randint(1,52)
                for x in list_of_cards:
                  if x.number == player_first:
                    player_first = x
                    player_first_val = x.value
                    player_first_face = x.face
                  else:
                    pass
                player_second = random.randint(1,52)
                for x in list_of_cards:
                  if x.number == player_second:
                    player_second = x
                    player_second_val = x.value
                    player_second_face = x.face
                  else:
                    pass  
              player_total = player_first_val + player_second_val
              await message.channel.send("Drawing dealers cards...") ; sleep(2)
              await message.channel.send(f"Dealers first card is {dealer_first}")
              await message.channel.send(file = dealer_first_face) ; sleep(3)
              await message.channel.send(f"Dealer draws second card and places it face down...") ; sleep(2)
              await message.channel.send(file = blank_card) ; sleep(1)
              await message.channel.send(f"Dealer is showing {dealer_first_val}") ; sleep(3)  
              if dealer_total == 21 and player_total != 21:
                await message.channel.send("Dealer flips their face down card...") ; sleep(2)
                await message.channel.send(f"Dealers other card is {dealer_second}") ; sleep(2)
                await message.channel.send(file = dealer_second_face) ; sleep(3)
                await message.channel.send(f"Dealer is showing {dealer_total}") ; sleep(2)
                players_val.append(-int(bet.content))
                await message.channel.send(f"{dealer_total} means dealer gets Blackjack! You lose ${bet.content} \nYour bankroll is ${sum(players_val)}")
                break
              await message.channel.send("Drawing players cards...") ; sleep(2)
              await message.channel.send(f"Players first card is {player_first}")
              await message.channel.send(file = player_first_face) ; sleep(2)
              await message.channel.send(f"Players second card is {player_second}")
              await message.channel.send(file = player_second_face) ; sleep(2)
              await message.channel.send(f"Player is showing {player_total}") ; sleep(3)
              cards_played = [player_first, player_second, dealer_first, dealer_second]
              while player_total < 21:
                await message.channel.send("Would you like to hit or stand?")
                player_choice = await client.wait_for('message')
                if "hit" in player_choice.content.lower():
                  player_addit = random.randint(1,52)
                  for x in list_of_cards:
                    if x.number == player_addit and x not in cards_played:
                      player_addit = x
                      cards_played.append(x)
                      await message.channel.send(f"Player drew {x}") 
                      await message.channel.send(file = x.face); sleep(3)
                      #Converting Aces from 11 to 1 if an 11 would cause bust
                      if player_total > 10 and x.value == 11:
                        player_total += 1
                      else:
                        player_total += x.value
                      await message.channel.send(f"Player total is now {player_total}") ; sleep(3)
                    else:
                      pass
                elif "stand" in player_choice.content.lower():
                  break
                else:
                  await message.channel.send("Invalid input...") ; sleep(2)
                  pass
              if player_total == 21 and dealer_total != 21:
                players_val.append(int(round(float(bet.content) * 1.5)))
                print(f"{player_total} means Blackjack! You win ${int(round(float(bet.content) * 1.5))} Your bankroll is ${sum(players_val)}")
                break              
              #Player bust condition
              if player_total > 21:
                await message.channel.send(f"{player_total} means you BUST. You lost ${bet.content}") ; sleep(1)
                players_val.append(-int(bet.content))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}")
                break
              #Dealer flip
              await message.channel.send("Dealer flips their face down card...") ; sleep(2)
              await message.channel.send(f"Dealers other card is {dealer_second}")
              await message.channel.send(file = dealer_second_face) ; sleep(3)
              await message.channel.send(f"Dealer is showing {dealer_total}") ; sleep(3)
              #Dealer additional draws to 17
              while dealer_total < 17:
                dealer_addit = random.randint(1,52)
                for x in list_of_cards:
                  if x.number == dealer_addit and x not in cards_played:
                    await message.channel.send(f"Dealers draws {x}")
                    cards_played.append(x)
                    await message.channel.send(file = x.face) ; sleep(2)
                    await message.channel.send(f"Dealer's total is {dealer_total + x.value}")
                    #Converting Aces from 11 to 1 if an 11 would cause bust
                    if dealer_total > 10 and x.value == 11:
                      dealer_total += 1
                    else:
                      dealer_total += x.value
                  else:
                    pass                     
              #Dealer bust condition
              if dealer_total > 21:
                await message.channel.send(f"{dealer_total} means dealer BUST. You win ${bet.content}") ; sleep(1)
                players_val.append(int(bet.content))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}")
                break              
              #Dealer win condition
              elif dealer_total > player_total:
                await message.channel.send(f"{dealer_total} means dealer WINS, you lost ${bet.content}") ; sleep(1)
                players_val.append(-int(bet.content))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}")
                break          
              elif dealer_total == player_total:
                await message.channel.send(f"{dealer_total} means PUSH, your bet has been returned back to you.") ; sleep(1)
                await message.channel.send(f"Your bankroll is ${sum(players_val)}")    
                break          
              #Player win condition
              elif dealer_total < player_total:
                await message.channel.send(f"{player_total} means player WINS, you win ${bet.content}!") ; sleep(1)
                players_val.append(int(bet.content))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}") 
                break            
              else:
                await message.channel.send(f"Invalid input...")
                break
            elif bet.content == "!c! bj stop":
              break
            else:
              await message.channel.send("You don't have enough money!")
              break 
        loaded_bnkfl_r[f"{message.author.name}#{message.author.discriminator}"] = [sum(players_val)]
      with open(bank_file_dir, "w") as bnkfldir:
        json.dump(loaded_bnkfl_r, bnkfldir)
  elif message.content.startswith("!c! scoreboard"):
    with open(bank_file_dir, "r") as bnkfl_r:
      bnkfile_dict = json.load(bnkfl_r)
    with open(score_board_txt, "w") as scrbrdtxt:
      count = 0
      scr_lst = ""
      for x,y in bnkfile_dict.items():
        count += 1
        scr_lst += (f"{count}. {x} : ${sum(y)}\n")
      scrbrdtxt.write(scr_lst)
    await message.channel.send(file = discord.File(f"{script_path}\\score_board.txt"))   
  elif message.content.startswith("!c! set money") and message.author.name in allowed_users:
    with open(bank_file_dir, "r") as bnkfl_r:
      tmp_values = json.load(bnkfl_r )  
    await message.channel.send(f"How much money would you like to give {message.content[13:]}?")
    money_to_be_added = await client.wait_for('message')
    if money_to_be_added.content[0] == "$":
      money_to_be_added.content = money_to_be_added.content[1:]
    try:
      tmp_values[message.content[13:].strip()] = [int(money_to_be_added.content)]
    except:
      await message.channel.send("That's not money...")
    with open(bank_file_dir, "w") as bnkfl_w:
      json.dump(tmp_values, bnkfl_w)
    await message.channel.send(f"${money_to_be_added.content} has been added to {message.content[13:].strip()}'s account.")
  elif message.content.startswith("!c! add user") and message.author.name in allowed_users:
      added_user = message.content.strip()[12:]
      with open(allowed_persons_dir, "a") as users:
        users.write(f"\n{added_user.strip()}")
      await message.channel.send(f"{added_user.strip()} has been appended to allowed persons.")
  elif message.content.startswith("!c! list users"):
      await message.channel.send(f"These users can access the player bank: \n{allowed_users}")
  elif message.content.startswith("!help") or message.content.startswith("!commands"):
    await message.channel.send('"!c! add user{add user here\}"\n"!c! list users"\n"!c! blackjack"\n"!c! set money {add user here\}"\n"!c! scoreboard"\n"!help"\n"!commands".')
  else:
    return


client.run(TOKEN)
