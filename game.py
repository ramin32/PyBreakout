#!/usr/bin/env python

#############################################################################
#
# Ramin Rakhamimov (C) 2008
# ramin32@gmail.com
# http://www.ramrak.net 
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
#############################################################################
"""Runs the breakout game"""
try:
    import sys
    import os
    import time
    import pygame
    import sprites.ball
    import sprites.brick
    import sprites.paddle
except ImportError, err:
    print err
    sys.exit(2)


def init():
    pygame.init()

    # Initialize the screen
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.set_caption('Basic Pong')

    # Initialize input
    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)
    pygame.key.set_repeat(1, 1)

    return screen

def get_image(file_name):
    fullname = os.path.join('data', file_name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print >> sys.stderr, 'Cannot load image:', fullname
        sys.exit(1)
    image = image.convert_alpha()
    return image

def create_string(string, size, color):
    font_file_name = 'DejaVuSerif.ttf'
    fullname = os.path.join('data', font_file_name)
    try:
        font = pygame.font.Font(fullname, size)
    except pygame.error, message:
        print >> sys.stderr, 'Cannot load image:', fullname
        sys.exit(1)
    return font.render(string, False, color)

def kill_game(screen, string, size, color):
    string_image = create_string(string, size, color)
    x = (screen.get_width() - string_image.get_width())

    if x < 0: x = 0
    else: x /= 2
    screen.blit(string_image, (x, 50))
    pygame.display.flip()
    time.sleep(5)
    sys.exit(0)

def run_game_loop(screen, allsprites, brick_group, paddle):
    background = pygame.Surface(screen.get_size()).convert()
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    pygame.display.update()

    clock = pygame.time.Clock()
    while True:
        pygame.event.clear()
        clock.tick(90)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    sys.exit(0)
                elif event.key == pygame.K_LEFT:
                    paddle.set_move(-5)
                elif event.key == pygame.K_RIGHT:
                    paddle.set_move(5)
            if event.type == pygame.MOUSEMOTION:
                paddle.set_move(pygame.mouse.get_rel()[0] * 5)
        allsprites.clear(screen, background)       
        try:
            allsprites.update()
        except sprites.ball.BallFallOutException:
            kill_game(screen, "Game over! :(", 140, (255, 0 ,0))

        if len(brick_group.sprites()) == 0:
           kill_game(screen, "Good game! ;-)", 140, (0, 255, 0))
        
        updated_rects = allsprites.draw(screen)
        pygame.display.update(updated_rects)
        
def main():
    screen = init()

    ball = sprites.ball.Ball(get_image('ball.png') )
    paddle = sprites.paddle.Paddle(get_image('paddle.png'), ball)

    ball.rect.midbottom = paddle.rect.midtop

    brick_images = []
    brick_images.append(get_image('black_swirl_brick.png'))
    brick_images.append(get_image('red_swirl_brick.png'))
    brick_images.append(get_image('brown_swirl_brick.png'))

    brick_group = sprites.brick.get_bricks(screen, ball, brick_images)
    
    allsprites = [ball, paddle, brick_group]
    allsprites = pygame.sprite.RenderUpdates(allsprites)

    run_game_loop(screen, allsprites, brick_group, paddle)

if __name__ == '__main__':
    main()

