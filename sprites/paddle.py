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
"""Implements a Paddle class."""
import pygame
import constants
import movingsprite

class Paddle(movingsprite.MovingSprite):
    def __init__(self, image, ball):
        movingsprite.MovingSprite.__init__(self, image)
        self.ball = ball
        x = self.screen_rect.midbottom[constants.X] - self.rect.width/2
        y = self.screen_rect.bottom - self.rect.height
        position = [x, y]
        self.rect = self.rect.move(position)

    def update(self):
        movingsprite.MovingSprite.update(self)
        self.direction = [0, 0]
        if self.rect.left < self.screen_rect.left:
            self.rect.left = self.screen_rect.left
        elif self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right

        if self.rect.colliderect(self.ball.rect):
            self.ball.flip_y()
            self.ball.direction[constants.X] += self.get_area_hit(self.ball)

    def get_area_hit(self, ball):
        ball_x = ball.rect.midbottom[constants.X] 
        percentage = (float(ball_x) - self.rect.left)/self.rect.width
        if percentage < .20:
            return -2
        if percentage < .40:
            return -1
        if percentage < .60:
            return 0
        if percentage < .80:
            return 1
        return 2


    def set_move(self, move):
        self.direction[constants.X] = move

