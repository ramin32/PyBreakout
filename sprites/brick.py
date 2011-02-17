#############################################################################
#
# Ramin Rakhamimov (C) 2008
# ramin32@gmail.com
# http://www.ramrak.net 
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANconstants.Y WARRANTconstants.Y; without even the implied warranty of
# MERCHANTABILITconstants.Y or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# constants.You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
#############################################################################

import pygame
import constants
import movingsprite

class Brick(movingsprite.MovingSprite):
    def __init__(self, image, ball, position):
        movingsprite.MovingSprite.__init__(self, image, position)
        self.ball = ball

    def update(self):
        if self.rect.colliderect(self.ball.rect):
            if self.ball.rect.midleft[constants.X] > self.rect.top or \
                    self.ball.rect.midleft[constants.X] < self.rect.bottom:
                        self.ball.flip_y()
            else:
                self.ball.flip_x()
            self.kill()

def get_bricks(screen, ball, brick_images):
    brick_group = pygame.sprite.Group()

    images_size = len(brick_images)
    if images_size <= 0:
        return brick_group

    # All images are the same size, so are their dimensions.
    width = brick_images[0].get_width()
    height = brick_images[0].get_height()

    start_across = screen.get_width() * .20
    end_across = screen.get_width() * .80
    start_down = screen.get_height() * .05
    end_down = screen.get_height() * .40

    count = 0

    for x in xrange(start_across,end_across,width + 50):
        for y in xrange(start_down, end_down, height + 50):
                sprite = Brick(brick_images[count], ball, [x, y]) 
                count += 1
                if count == images_size:
                    count = 0;

                brick_group.add(sprite)

    return brick_group
