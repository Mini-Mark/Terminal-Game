import keyboard
import random
import utils.area as area
import utils.game_object as game_object

# init area
mainArea = area.Area(topSpace=30)
mainArea.setTitleLabel("Enemy Evasion\n".center(mainArea.getWidth()))

enemyList = []
highscore = 0
mainArea.setActionLabel(f"Highscore : {highscore}\nEnemy : {len(enemyList)}\n")

turn = 0

# random player spawn
player = game_object.GameObject(
    "⛹", (random.randint(0, 48), random.randint(0, 13)))
mainArea.addObjectToArea(player)


mainArea.show()


def restart():
    global enemyList, turn, mainArea, player, highscore

    if (len(enemyList) - 1 > highscore):
        highscore = len(enemyList) - 1

    enemyList = []
    turn = 0
    mainArea.clear()
    mainArea.addObjectToArea(player)


# Main game play
while True:
    mainArea.setActionLabel(
        f"Highscore : {highscore}\nEnemy : {len(enemyList)}\n")
    # Player Movement
    keyInput = keyboard.read_key()

    if keyInput == 'esc':
        print("Exiting the game !")
        break
    elif keyInput == 'w':
        player.moveUp()
        if (player.getY() < 0):
            player.updatePosition(player.getX(), mainArea.getHeight())
    elif keyInput == 's':
        player.moveDown()
        if (player.getY() > mainArea.getHeight()):
            player.updatePosition(player.getX(), 0)
    elif keyInput == 'a':
        player.moveLeft()
        if (player.getX() < 0):
            player.updatePosition(mainArea.getWidth(), player.getY())
    elif keyInput == 'd':
        player.moveRight()
        if (player.getX() > mainArea.getWidth()):
            player.updatePosition(0, player.getY())

    # Enemy Follow Player
    if turn % 3 == 0:
        for i in enemyList:
            target_x, target_y = player.getX(), player.getY()

            if i.getX() > target_x and (i.getX() - 1, i.getY()) not in Enemy_positions:
                i.moveLeft()
            elif i.getX() < target_x and (i.getX() + 1, i.getY()) not in Enemy_positions:
                i.moveRight()

            if i.getY() > target_y and (i.getX(), i.getY() - 1) not in Enemy_positions:
                i.moveUp()
            elif i.getY() < target_y and (i.getX(), i.getY() + 1) not in Enemy_positions:
                i.moveDown()

            Enemy_positions = {(Enemy.getX(), Enemy.getY())
                               for Enemy in enemyList}

    if turn % 2 == 0:
        Enemy_x_range = list(range(0, 48))
        Enemy_y_range = list(range(0, 14))

        Enemy_x_range.remove(player.getX())
        Enemy_y_range.remove(player.getY())
        rand_x = random.sample(Enemy_x_range, 1)[0]
        rand_y = random.sample(Enemy_y_range, 1)[0]

        EnemyObj = game_object.GameObject("★", (rand_x, rand_y))
        mainArea.addObjectToArea(EnemyObj)

        enemyList.append(EnemyObj)

        Enemy_positions = {(Enemy.getX(), Enemy.getY())
                           for Enemy in enemyList}

    if (player.getX(), player.getY()) in Enemy_positions:
        deathIcon = game_object.GameObject(
            "ⓧ", (player.getX(), player.getY()))
        mainArea.addObjectToArea(deathIcon)

        mainArea.show()
        print("Game Over! You collided with a Enemy.\n")
        print("( Press any key to restart the game )\n")
        restart()
        
        keyboard.read_key()
        keyboard.read_key()

    else:
        mainArea.show()
        turn += 1
