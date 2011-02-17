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
"""Implements a Ball sprite which bounces of objects, via flip_x() and flip_y()
methods."""
import pygame
import movingsprite

class Ball(movingsprite.MovingSprite):
    def __init__(self,image):
        movingsprite.MovingSprite.__init__(self, image)
        self.direction = [3, 3]

    def update(self):
        movingsprite.MovingSprite.update(self)
        if self.rect.left < self.screen_rect.left or \
                self.rect.right > self.screen_rect.right:
                    self.flip_x()
        elif self.rect.top < self.screen_rect.top: 
            self.flip_y()
        elif self.rect.bottom > self.screen_rect.bottom:
            raise BallFallOutException

class BallFallOutException(Exception):
    pass
