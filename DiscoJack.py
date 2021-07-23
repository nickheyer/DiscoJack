import asyncio
import discord
import random
from pprint import pprint
import sys
import os
from time import sleep
import re
import json

ini_json = os.path.join(os.path.dirname(__file__), f'ini_values.json')
ini = {}
try:
  with open(ini_json, "r") as ini_r:
    ini = json.load(ini_r)
except:
  ini['tok_val'] = input("Please enter your Discord API bot token here. \n")
  ini['allow_repl'] = input("Allow players to add $50 to their account when it hits zero? ('yes' or 'no') \n")
  ini['auth_user'] = [input("Please enter your full Discord username here (ex:'NastyNick#4212'). \n")]
  with open(ini_json, "w") as ini_w:
    json.dump(ini, ini_w)
TOKEN = ini['tok_val']
delay = 1

intents = discord.Intents.all()
client = discord.Client(intents = intents)
embed = discord.Embed() 

def rand_number(num):
  return random.randint(1, num)

score_board_txt = os.path.join(os.path.dirname(__file__), f'score_board.txt')
bank_file_dir = os.path.join(os.path.dirname(__file__), f'bank_file.json')
script_path = sys.path[0]



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
  current_player = message.author
  current_channel = message.channel.id
  global delay
  if message.author == client.user:
    return
  elif message.content.startswith("!c! set delay") and (f"{message.author.name}#{message.author.discriminator}") in ini['auth_user']:
    new_delay = message.content[13:].strip()
    try:
      if int(new_delay) >= 0 and int(new_delay) <= 10:
        delay = int(new_delay)
        await message.channel.send(f"Delay set to {delay}")
      else:
        await message.channel.send(f"Invalid input...")
    except:
      await message.channel.send("Invalid input...")
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
              if self.value == 11:
                return (f"{self.name} - 1/11")
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
        if sum(players_val) == 0 and ini['allow_repl'] == 'yes':
          await message.channel.send(f"It looks like your current balance is $0.")
          await asyncio.sleep(delay)
          await message.channel.send("Consider following the below GitHub while you enjoy this free $50. \nhttps://github.com/nickheyer")
          players_val.append(50)
        await message.channel.send(f"{message.author}'s current bankroll is ${sum(players_val)}. Let the games begin!")
        await asyncio.sleep(delay)
        while True:
            while True:
              await message.channel.send("How much would you like to bet?")
              await asyncio.sleep(delay)
              bet = await client.wait_for('message', check=lambda message: message.author == current_player and message.channel.id == current_channel)
              player_bet = bet.content
              try:
                if player_bet[0] == "$":
                  player_bet = player_bet[1:]
                ismoney = type(int(player_bet)) is int and int(player_bet)>0
                if ismoney == True:
                  break
                elif ismoney == False:
                  await message.channel.send("Invalid input...")
              except:
                await message.channel.send("That isn't money...")
                await asyncio.sleep(delay)
            if sum(players_val) >= int(player_bet):
              await message.channel.send(f"You bet: ${player_bet}")
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
              await message.channel.send("Drawing dealers cards...")
              await asyncio.sleep(delay)
              await message.channel.send(f"Dealers first card is {dealer_first}")
              await message.channel.send(file = dealer_first_face)
              await asyncio.sleep(delay)
              await message.channel.send(f"Dealer draws second card and places it face down...")
              await asyncio.sleep(delay)
              await message.channel.send(file = blank_card)
              await asyncio.sleep(delay)
              await message.channel.send(f"Dealer is showing `{dealer_first_val}`")
              await asyncio.sleep(delay) 
              if dealer_total == 21 and player_total != 21:
                await message.channel.send("Dealer flips their face down card...")
                await asyncio.sleep(delay)
                await message.channel.send(f"Dealers other card is {dealer_second}")
                await asyncio.sleep(delay)
                await message.channel.send(file = dealer_second_face)
                await asyncio.sleep(delay)
                await message.channel.send(f"Dealer is showing `{dealer_total}`")
                await asyncio.sleep(delay)
                players_val.append(-int(player_bet))
                await message.channel.send(f"`{dealer_total}` means dealer gets Blackjack! You lose ${player_bet} \nYour bankroll is ${sum(players_val)}")
                break
              await message.channel.send("Drawing players cards...")
              await asyncio.sleep(delay)
              await message.channel.send(f"Players first card is {player_first}")
              await message.channel.send(file = player_first_face)
              await asyncio.sleep(delay)
              await message.channel.send(f"Players second card is {player_second}")
              await message.channel.send(file = player_second_face)
              await asyncio.sleep(delay)
              await message.channel.send(f"Player is showing `{player_total}`")
              await asyncio.sleep(delay)
              cards_played = [player_first, player_second, dealer_first, dealer_second]
              hit_count = 0
              while player_total < 21:
                if hit_count == 0:
                  await message.channel.send("Would you like to hit, stand, or doubledown?")
                else:
                  await message.channel.send("Would you like to hit or stand?")
                player_choice = await client.wait_for('message', check=lambda message: message.author == current_player and message.channel.id == current_channel)
                if "hit" == player_choice.content.lower():
                  player_addit = random.randint(1,52)
                  for x in list_of_cards:
                    if x.number == player_addit and x not in cards_played:
                      player_addit = x
                      cards_played.append(x)
                      await message.channel.send(f"Player drew {x}") 
                      await message.channel.send(file = x.face)
                      await asyncio.sleep(delay)
                      #Converting Aces from 11 to 1 if an 11 would cause bust               
                      if player_first_val == 11 and (player_total + x.value) > 21:
                        player_first_val = 1
                        player_total +=  -10
                      if player_second_val == 11 and (player_total + x.value) > 21:
                        player_second_val = 1
                        player_total +=  -10
                      if player_total > 10 and x.value == 11:
                        player_total += 1
                        hit_count += 1
                      else:
                        player_total += x.value
                        hit_count += 1
                      await message.channel.send(f"Player total is now `{player_total}`")
                      await asyncio.sleep(delay)
                elif "doubledown" == player_choice.content.lower() and hit_count == 0  and (sum(players_val) >= (int(player_bet) * 2)):
                  player_bet = str(int(player_bet) * 2)
                  player_addit = random.randint(1,52)
                  for x in list_of_cards:
                    if x.number == player_addit and x not in cards_played:
                      player_addit = x
                      cards_played.append(x)
                      await message.channel.send(f"Player drew {x}") 
                      await message.channel.send(file = x.face)
                      await asyncio.sleep(delay)
                      #Converting Aces from 11 to 1 if an 11 would cause bust               
                      if player_first_val == 11 and (player_total + x.value) > 21:
                        player_first_val = 1
                        player_total += -10
                      if player_second_val == 11 and (player_total + x.value) > 21:
                        player_second_val = 1
                        player_total += -10
                      if player_total > 10 and x.value == 11:
                        player_total += 1
                        hit_count += 1
                      else:
                        player_total += x.value
                        hit_count += 1
                      await message.channel.send(f"Player total is now `{player_total}` and player bet is now ${player_bet}")
                      await asyncio.sleep(delay)
                      break
                  break
                elif "stand" == player_choice.content.lower():
                  break
                else:
                  await message.channel.send("Invalid input...")
                  await asyncio.sleep(delay)
                  pass
              if player_total == 21 and dealer_total != 21 and hit_count == 0:
                players_val.append(int(round(float(player_bet) * 1.5)))
                await message.channel.send(f"{player_total} means Blackjack! You win ${int(round(float(player_bet) * 1.5))} Your bankroll is ${sum(players_val)}")
                break            
              #Player bust condition
              if player_total > 21:
                await message.channel.send(f"`{player_total}` means you BUST. You lost ${player_bet}")
                await asyncio.sleep(delay)
                players_val.append(-int(player_bet))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}")
                break
              #Dealer flip
              await message.channel.send("Dealer flips their face down card...")
              await asyncio.sleep(delay)
              await message.channel.send(f"Dealers other card is {dealer_second}")
              await message.channel.send(file = dealer_second_face)
              await asyncio.sleep(delay)
              await message.channel.send(f"Dealer is showing `{dealer_total}`")
              await asyncio.sleep(delay)
              #Dealer additional draws to 17
              while dealer_total < 17:
                dealer_addit = random.randint(1,52)
                for x in list_of_cards:
                  if x.number == dealer_addit and x not in cards_played:
                    await message.channel.send(f"Dealers draws {x}")
                    cards_played.append(x)
                    await message.channel.send(file = x.face)
                    await asyncio.sleep(delay)                  
                    #Converting Aces from 11 to 1 if an 11 would cause bust
                    if dealer_first_val == 11 and (dealer_total + x.value) > 21:
                        dealer_first_val = 1
                        dealer_total += -10
                    if dealer_second_val == 11 and (dealer_total + x.value) > 21:
                        dealer_second_val = 1
                        dealer_total += -10
                    if dealer_total > 10 and x.value == 11:
                      dealer_total += 1
                    else:
                      dealer_total += x.value
                    await message.channel.send(f"Dealer's total is `{dealer_total}`")
                  else:
                    pass                     
              #Dealer bust condition
              if dealer_total > 21:
                await message.channel.send(f"`{dealer_total}` means dealer BUST. You win ${player_bet}")
                await asyncio.sleep(delay)
                players_val.append(int(player_bet))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}")
                break              
              #Dealer win condition
              elif dealer_total > player_total:
                await message.channel.send(f"`{dealer_total}` means dealer WINS, you lost ${player_bet}")
                await asyncio.sleep(delay)
                players_val.append(-int(player_bet))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}")
                break          
              elif dealer_total == player_total:
                await message.channel.send(f"`{dealer_total} `means PUSH, your bet has been returned back to you.")
                await asyncio.sleep(delay)
                await message.channel.send(f"Your bankroll is ${sum(players_val)}")    
                break          
              #Player win condition
              elif dealer_total < player_total:
                await message.channel.send(f"`{player_total}` means player WINS, you win ${player_bet}!")
                await asyncio.sleep(delay)
                players_val.append(int(player_bet))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}") 
                break            
              else:
                await message.channel.send(f"Invalid input...")
                break
            elif player_bet == "!c! stop":
              break
            else:
              await message.channel.send("You don't have enough money!")
              break 
        loaded_bnkfl_r[f"{message.author.name}#{message.author.discriminator}"] = [sum(players_val)]
      with open(bank_file_dir, "w") as bnkfldir:
        json.dump(loaded_bnkfl_r, bnkfldir)
  elif message.content.startswith("!c! roulette"):
    class RouletteWheel:
        def __init__(self, number):
          self.number = number
          self.face = (discord.File(f"{script_path}\\RouletteWheel\\{number}.png"))
        def __repr__(self):
          return (f"{self.number}")
    #Wheel slot instantiation
    wheel_0 = RouletteWheel(0)
    wheel_1 = RouletteWheel(1)
    wheel_2 = RouletteWheel(2)
    wheel_3 = RouletteWheel(3)
    wheel_4 = RouletteWheel(4)
    wheel_5 = RouletteWheel(5)
    wheel_6 = RouletteWheel(6)
    wheel_7 = RouletteWheel(7)
    wheel_8 = RouletteWheel(8)
    wheel_9 = RouletteWheel(9)
    wheel_10 = RouletteWheel(10)
    wheel_11 = RouletteWheel(11)
    wheel_12 = RouletteWheel(12)
    wheel_13 = RouletteWheel(13)
    wheel_14 = RouletteWheel(14)
    wheel_15 = RouletteWheel(15)
    wheel_16 = RouletteWheel(16)
    wheel_17 = RouletteWheel(17)
    wheel_18 = RouletteWheel(18)
    wheel_19 = RouletteWheel(19)
    wheel_20 = RouletteWheel(20)
    wheel_21 = RouletteWheel(21)
    wheel_22 = RouletteWheel(22)
    wheel_23 = RouletteWheel(23)
    wheel_24 = RouletteWheel(24)
    wheel_25 = RouletteWheel(25)
    wheel_26 = RouletteWheel(26)
    wheel_27 = RouletteWheel(27)
    wheel_28 = RouletteWheel(28)
    wheel_29 = RouletteWheel(29)
    wheel_30 = RouletteWheel(30)
    wheel_31 = RouletteWheel(31)
    wheel_32 = RouletteWheel(32)
    wheel_33 = RouletteWheel(33)
    wheel_34 = RouletteWheel(34)
    wheel_35 = RouletteWheel(35)
    wheel_36 = RouletteWheel(36)
    list_of_wheel_slots = [
      wheel_0,
      wheel_1,
      wheel_2,
      wheel_3,
      wheel_4,
      wheel_5,
      wheel_6,
      wheel_7,
      wheel_8,
      wheel_9,
      wheel_10,
      wheel_11,
      wheel_12,
      wheel_13,
      wheel_14,
      wheel_15,
      wheel_16,
      wheel_17,
      wheel_18,
      wheel_19,
      wheel_20,
      wheel_21,
      wheel_22,
      wheel_23,
      wheel_24,
      wheel_25,
      wheel_26,
      wheel_27,
      wheel_28,
      wheel_29,
      wheel_30,
      wheel_31,
      wheel_32,
      wheel_33,
      wheel_34,
      wheel_35,
      wheel_36
      ]
    spin_gif = (discord.File(f"{script_path}\\RouletteWheel\\optimized_sl_gif.gif"))
    with open(bank_file_dir, "r") as bnkfl_r:
      loaded_bnkfl_r = json.load(bnkfl_r)
      players_val = loaded_bnkfl_r[f"{message.author.name}#{message.author.discriminator}"]
      if sum(players_val) == 0 and ini['allow_repl'] == 'yes':
          await message.channel.send(f"It looks like your current balance is $0.")
          await asyncio.sleep(delay)
          await message.channel.send("Consider following the below GitHub while you enjoy this free $50.\nhttps://github.com/nickheyer")
          players_val.append(50)
          await asyncio.sleep(delay)
      await message.channel.send(f"{message.author}'s current bankroll is ${sum(players_val)}. Let the games begin!")
      await asyncio.sleep(delay)
      #The entire game must be in this while loop
      while True:
          #Bet Loop
          while True:
            await message.channel.send("How much would you like to bet?")
            await asyncio.sleep(delay)
            bet = await client.wait_for('message', check=lambda message: message.author == current_player and message.channel.id == current_channel)
            player_bet = bet.content
            try:
              if player_bet[0] == "$":
                player_bet = player_bet[1:]
              ismoney = type(int(player_bet)) is int and int(player_bet)>0
              if ismoney == True:
                break
              elif ismoney == False:
                await message.channel.send("Invalid input...")
            except:
              await message.channel.send("That isn't money...")
              await asyncio.sleep(delay)
          if sum(players_val) >= int(player_bet):
            await message.channel.send(f"You bet: ${player_bet}")
            possible_choices = [str(x) for x in range(37)]
            non_num_choices = ["red", "black", "odd", "even"]
            possible_choices.extend(non_num_choices)
            red_slots = [3,12,7,18,9,14,1,16,5,23,30,36,27,34,25,21,19,32]
            black_slots = [26,35,28,29,22,31,20,33,24,10,8,11,13,6,17,2,4,15]
            await message.channel.send("```Here are your choices: \n1. A number in range 0-36\n2. 'Red' or 'Black'\n3. 'Odd' or 'Even'```")
            r_table_msg = await message.channel.send(file = (discord.File(f"{script_path}\\RouletteWheel\\roulette_table.png")))
            await asyncio.sleep(delay)
            p_choice = await client.wait_for('message', check=lambda message: message.author == current_player and message.channel.id == current_channel and message.content in possible_choices)
            await asyncio.sleep(delay)
            await message.channel.send("Spinning wheel... no more bets!")
            await asyncio.sleep(1)
            await r_table_msg.delete()
            await message.channel.send(file = spin_gif, delete_after = 10.0)
            #Generating where the ball will land
            ball_lands = random.randint(0,36)
            for x in list_of_wheel_slots:
              if x.number == ball_lands:
                ball_lands = x
            await asyncio.sleep(10)
            await message.channel.send(file = ball_lands.face)
            await message.channel.send(f"The ball has landed on `{ball_lands}`")
            if p_choice.content.lower() not in non_num_choices:
              if int(p_choice.content) == ball_lands.number:
                await message.channel.send(f"The ball has landed on your number! You won ${int(player_bet)*34}")
                players_val.append(int(player_bet) * 34)
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}")
                break
              else:
                await message.channel.send(f"Unfortunately, the ball landed on a different number. You lost ${player_bet}")
                players_val.append(-int(player_bet))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}")
                break
            elif p_choice.content.lower() == "red":
              if ball_lands.number in red_slots:
                await message.channel.send(f"The ball has landed on a red number! You won ${player_bet}")
                players_val.append(int(player_bet))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}")
                break
              else:
                await message.channel.send(f"Unfortunately, the ball did not land on a red number. You lost ${player_bet}")
                players_val.append(-int(player_bet))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}")
                break  
            elif p_choice.content.lower() == "black":
              if ball_lands.number in black_slots:
                await message.channel.send(f"The ball has landed on a black number! You won ${player_bet}")
                players_val.append(int(player_bet))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}")
                break
              else:
                await message.channel.send(f"Unfortunately, the ball did not land on a black number. You lost ${player_bet}")
                players_val.append(-int(player_bet))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}") 
                break  
            elif p_choice.content.lower() == "even":
              if ball_lands.number % 2 == 0:
                await message.channel.send(f"The ball has landed on a even number! You won ${player_bet}")
                players_val.append(int(player_bet))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}")
                break
              else:
                await message.channel.send(f"Unfortunately, the ball did not land on an even number. You lost ${player_bet}")
                players_val.append(-int(player_bet))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}")
                break 
            elif p_choice.content.lower() == "odd":
              if ball_lands.number % 2 != 0:
                await message.channel.send(f"The ball has landed on a odd number! You won ${player_bet}")
                players_val.append(int(player_bet))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}")
                break
              else:
                await message.channel.send(f"Unfortunately, the ball did not land on an odd number. You lost ${player_bet}")
                players_val.append(-int(player_bet))
                await message.channel.send(f"Your bankroll is now ${sum(players_val)}") 
                break
          elif player_bet == "!c! stop":
            return
          else:
            await message.channel.send("You don't have enough money!")
            break 
      loaded_bnkfl_r[f"{message.author.name}#{message.author.discriminator}"] = [sum(players_val)]
    with open(bank_file_dir, "w") as bnkfldir:
      json.dump(loaded_bnkfl_r, bnkfldir)
  elif message.content.startswith("!c! scoreboard"):
    with open(bank_file_dir, "r") as bnkfl_r:
      bnkfile_dict = json.load(bnkfl_r)
    bnkfile_sort = [[yy,xx] for xx,yy in bnkfile_dict.items()]
    bnkfile_sort.sort(reverse = True)
    with open(score_board_txt, "w") as scrbrdtxt:
      count = 0
      scr_lst = ""
      for x,y in bnkfile_sort:
        count += 1
        scr_lst += (f"{count}. {y} : ${sum(x)}\n")
      scrbrdtxt.write(scr_lst)
    await message.channel.send(file = discord.File(f"{script_path}\\score_board.txt"))   
  elif message.content.startswith("!c! set money") and (f"{message.author.name}#{message.author.discriminator}") in ini['auth_user']:
    with open(bank_file_dir, "r") as bnkfl_r:
      tmp_values = json.load(bnkfl_r)
    while True:  
      if message.content[13:].strip() in tmp_values.keys():
        await message.channel.send(f"What should we set {message.content[13:].strip()}'s money to?")
        money_to_be_added = await client.wait_for('message',check=lambda message: message.author == current_player and message.channel.id == current_channel)
        if money_to_be_added.content[0] == "$":
          money_to_be_added.content = money_to_be_added.content[1:]
        try:
          tmp_values[message.content[13:].strip()] = [int(money_to_be_added.content)]
        except:
          await message.channel.send("That's not money...")
          break
        with open(bank_file_dir, "w") as bnkfl_w:
          json.dump(tmp_values, bnkfl_w)
        await message.channel.send(f"{message.content[13:].strip()}'s account value has been set to ${money_to_be_added.content}.")
        break
      else:
        await message.channel.send(f"{message.content[13:].strip()} is not a valid player, check '!c! scoreboard for all players associated with {client.user}'")
        break
  elif message.content.startswith("!c! add user") and (f"{message.author.name}#{message.author.discriminator}") in ini['auth_user']:
      added_user = message.content.strip()[13:]
      if (f"{message.author.name}#{message.author.discriminator}") in ini['auth_user']:
        if added_user in ini['auth_user']:
          await message.channel.send(f"{added_user} already in whitelisted users.")
        else:
          ini['auth_user'].append(added_user)
          with open(ini_json, "w") as ini_w:
            json.dump(ini, ini_w)
          await message.channel.send(f"{added_user} has been added to the whitelist.")
      else:
        await message.channel.send(f"Sorry! {added_user.strip()} is not approved for this.")
  elif message.content.startswith("!c! list users"):
      auth_user_rep = ""
      for x,y in enumerate(ini['auth_user']):
            auth_user_rep += (f'{x+1}. {y}\n')
      await message.channel.send(f"These users can access the player bank: \n```{auth_user_rep}```")
      
  elif message.content.startswith("!help") or message.content.startswith("!commands"):
    await message.channel.send('"!c! add user{add user here\}"\n"!c! list users"\n"!c! blackjack"\n"!c! roulette"\n"!c! set money {add user here\}"\n"!c! scoreboard"\n"!help"\n"!commands".')
  else:
    return


client.run(TOKEN)
