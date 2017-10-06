from games import (GameState, Game, Fig52Game, TicTacToe, query_player, random_player,
                        alphabeta_player, minimax_decision, alphabeta_full_search,
                        alphabeta_search)


if __name__ == '__main__':
  ttt = TicTacToe()
  
  print('Initial game state:')
  print(ttt.display(ttt.initial))
  
  for _ in range(10):
    print(ttt.play_game(alphabeta_player, random_player))
  
  
