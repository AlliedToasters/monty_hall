from montyhall import MontyHall

no_games = int(input("how many games?"))
behavior = input("switch? y/n")
results = []
game_count = 0
while game_count < no_games:
    game = MontyHall()
    game.make_first_guess()
    game.open_first_door()
    if behavior == 'y':
        game.switch_door()
    else:
        pass
    results.append(game.evaluate_win())
    game_count += 1

print('you win {} games and lose {} games.'.format(results.count('win'), results.count('lose')))
