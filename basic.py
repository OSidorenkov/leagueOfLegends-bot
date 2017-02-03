import random

from cassiopeia import riotapi

riotapi.set_region("RU")
riotapi.set_api_key("RGAPI-d7fc0ab5-b9d4-4342-9e05-088c4efa727a")

summoner = riotapi.get_summoner_by_name("Barichpock")
print("{name} is a level {level} summoner on the RU server.".format(name=summoner.name, level=summoner.level))

champions = riotapi.get_champions()
random_champion = random.choice(champions)
print("He enjoys playing LoL on all different champions, like {name}.".format(name=random_champion.name))

challenger_league = riotapi.get_challenger()
best_na = challenger_league[0].summoner
print("He's much better at writing Python code than he is at LoL. He'll never be as good as {name}.".format(name=best_na.name))