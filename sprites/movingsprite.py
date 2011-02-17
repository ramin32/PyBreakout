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
"""A base class for moving sprites."""
import pygame
import constants

class MovingSprite(pygame.sprite.Sprite):
    def __init__(self, image, position=[0,0]):
        pygame.sprite.Sprite.__init__(self)
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.image = image 
        self.rect = image.get_rect().move(position)
        self.direction = [0,0]

    def update(self):
        self.rect.move_ip(self.direction)

    def flip_x(self):
        self.direction[constants.X] = -self.direction[constants.X]

    def flip_y(self):
        self.direction[constants.Y] = -self.direction[constants.Y]

