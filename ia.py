def ia(snake_corps, fruit_position, snake_position, change_direction, direction):    
    # if change_direction == 'haut' and direction == 'bas' and fruit_position[1] == snake_position[1]:
    #     snake_position[0] -= 10

    # if change_direction == 'bas' and direction == 'haut' and fruit_position[1] == snake_position[1]:
    #     snake_position[0] += 10

    # if change_direction == 'gauche' and direction == 'droite' and fruit_position[0] == snake_position[0]:
    #     snake_position[1] -= 10

    # if change_direction == 'droite' and direction == 'gauche' and fruit_position[0] == snake_position[0]:
    #     snake_position[1] += 10

    change_direction = mouvement(snake_position, fruit_position)
    
    for block in snake_corps[1:]:
        if (snake_position[0] == (block[0] - 10) and (block[1] - 40) < snake_position[1] < (block[1] - 10) and change_direction == 'droite') or (snake_position[0] == (block[0] + 10) and (block[1] - 40) < snake_position[1] < (block[1] - 10) and change_direction == 'gauche'):
            change_direction = 'haut'
            break

        elif (snake_position[0] == (block[0] - 10) and (block[1] + 40) < snake_position[1] < (block[1] + 10) and change_direction == 'droite') or (snake_position[0] == (block[0] + 10) and (block[1] + 40) < snake_position[1] < (block[1] + 10) and change_direction == 'gauche'):
            change_direction = 'bas'
            break

        elif (snake_position[1] == (block[1] + 10) and (block[0] + 40) < snake_position[0] < (block[0] + 10) and change_direction == 'haut') or (snake_position[1] == (block[1] - 10) and (block[0] + 40) < snake_position[0] < (block[0] + 10) and change_direction == 'bas'):
            change_direction = 'droite'
            break

        elif (snake_position[1] == (block[1] + 10) and (block[0] - 40) < snake_position[0] < (block[0] - 10) and change_direction == 'haut') or (snake_position[1] == (block[1] - 10) and (block[0] - 40) < snake_position[0] < (block[0] - 10) and change_direction == 'bas'):
            change_direction = 'gauche'
            break

    if (snake_corps[-1][0] == snake_corps[-2][0] and snake_corps[-1][1] > snake_corps[-2][1] and snake_position[1] == snake_corps[-1][1] - 20) or (snake_corps[-1][0] == snake_corps[-2][0] and snake_corps[-1][1] < snake_corps[-2][1] and snake_position[1] == snake_corps[-1][1] + 20) or (snake_corps[-1][1] == snake_corps[-2][1] and snake_corps[-1][0] > snake_corps[-2][0] and snake_position[0] == snake_corps[-1][0] - 20) or(snake_corps[-1][1] == snake_corps[-2][1] and snake_corps[-1][0] < snake_corps[-2][0] and snake_position[0] == snake_corps[-1][0] + 20):
        change_direction = mouvement(snake_position, fruit_position)
    
    if change_direction == 'haut' and direction != 'bas':
        direction = 'haut'

    if change_direction == 'bas' and direction != 'haut':
        direction = 'bas'

    if change_direction == 'gauche' and direction != 'droite':
        direction = 'gauche'

    if change_direction == 'droite' and direction != 'gauche':
        direction = 'droite'
    
    if direction == 'haut':
        snake_position[1] -= 10

    if direction == 'bas':
        snake_position[1] += 10

    if direction == 'gauche':
        snake_position[0] -= 10

    if direction == 'droite':
        snake_position[0] += 10
    return direction

def mouvement(snake_position, fruit_position):
    if snake_position[0] > fruit_position[0]:
        change_direction = 'gauche'
    if snake_position[0] < fruit_position[0]:
        change_direction = 'droite'
    if snake_position[1] > fruit_position[1]:
        change_direction = 'haut'
    if snake_position[1] < fruit_position[1]:
        change_direction = 'bas'
    
    return change_direction