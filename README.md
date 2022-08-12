# wiley_boardgame
Python Board Game

Objective and Rules:

The objective of the game is to start from safe place and progress around the board until you reach the winning position spot.

Players roll dice to decide moves, the dice consists of values 1-3.

When a player is in reach of the winning position, they require a perfect roll to move to winning position, any value greater than or less than will mean they maintain position.

When a player lands on a square that is the same value as another player, the player that was already on the position is killed and reset back to the safe place.


# Pseudo Code

Program Start

Initialise variable player_1_pos, player_2_pos to zero
Initialise game to true

While game is true
    
    player_1_pos, player_2_pos equal to dice_roll()

    call render_board(player_1_pos, player_2_pos)
        print board
    
    call update_board(player_1_pos, player_2_pos)

        initialise game_over to false
        
        if player killed
            player_x_pos is equal to zero
        
        update player position

        if player wins
            print result output
            game_over equal to true
        
        return player_1_pos, player_2_pos, game_over

    assign player_1_pos, player_2_pos, game from returned values of update_board

    if game
        continue loop
    else
        end loop

Program ends
