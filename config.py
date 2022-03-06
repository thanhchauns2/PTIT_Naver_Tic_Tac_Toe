# screen config

screen_size = (800, 800)
screen_color = (160, 160, 160)

# board config
# 0 = ô đang trống, 1 = X, -1 = O

border_thickness = 1
square_size = 40

# tic-tac config

X_color = (0, 0, 128)
O_color = (255,0,0)
tic_tac_thickness = 6
from_border = 9

# analyze points
connect_five1 = 1e18
connect_multiple_four1 = 1e9 + 500
connect_four_has_obstacles1 = 500
connect_four1 = 1e9
connect_multiple_three1 =  1e7
connect_three_has_obstacles1 = 400
connect_three1 = 5000
connect_multiple_two1 = 300
connect_two_has_obstacles1 = 50
connect_two1 = 200

connect_five2 = 1e18
connect_multiple_four2 = 1e8
connect_four_has_obstacles2 = 500
connect_four2 = 1e9
connect_multiple_three2 =  1e6
connect_three_has_obstacles2 = 400
connect_three2 = 1e6
connect_multiple_two2 = 10
connect_two_has_obstacles2 = 2
connect_two2 = 5

# text config

win_text = "Congratulations! You win."
lose_text = "You Lost. Try Again?"
text_size = 60
text_color = (249, 248, 113)
text_font = 'freesansbold.ttf'