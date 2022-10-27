import pygame, math

pygame.init()

window_height = 500
window_width = 460
window = pygame.display.set_mode((window_height, window_width), pygame.NOFRAME)

# the buttons for the shop MENU
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.over = False

    def draw(self, window, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(window, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('fos.ttf', 60)
            text = font.render(self.text, 1, (255, 255, 255))
            window.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def playSoundIfMouseIsOver(self, pos, sound):
        if self.isOver(pos):
            if not self.over:
                beepsound.play()
                self.over = True
        else:
            self.over = False


white = (255, 255, 255)
# the numbers for the calcaltor
s_1s = button((0, 255, 0), 40, 80, 70, 70, '1')
s_2s = button((0, 255, 0), 150, 80, 70, 70, '2')
s_3s = button((0, 255, 0), 265, 80, 70, 70, '3')
s_4s = button((0, 255, 0), 40, 178, 70, 70, '4')
s_5s = button((0, 255, 0), 150, 178, 70, 70, '5')
s_6s = button((0, 255, 0), 265, 178, 70, 70, '6')
s_7s = button((0, 255, 0), 40, 273, 70, 70, '7')
s_8s = button((0, 255, 0), 150, 273, 70, 70, '8')
s_9s = button((0, 255, 0), 265, 273, 70, 70, '9')
s_0s = button((0, 255, 0), 40, 360, 70, 70, '0')

numbers = [s_1s, s_2s, s_3s, s_4s, s_5s, s_6s, s_7s, s_8s, s_9s, s_0s]

# the symbols!
d_1s = button((0, 255, 0), 385, 267, 70, 70, '+')
d_2s = button((0, 255, 0), 385, 167, 70, 70, '-')
d_3s = button((0, 255, 0), 265, 360, 70, 70, 'x')
d_4s = button((0, 255, 0), 385, 360, 70, 70, '÷')
d_5s = button((0, 255, 0), 150, 360, 70, 70, '=')
d_6s = button((0, 255, 0), 350, 95, 140, 50, 'C')

symbols = [d_1s, d_2s, d_3s, d_4s, d_5s, d_6s]

# the image of the cals
image = pygame.image.load("dn.png")
image = pygame.transform.scale(image, (image.get_width() - 80, image.get_height() - 80))


# redraw window
def redraw(inputtap):
    # draw all the numbers
    window.fill((52, 73, 94))
    window.blit(image, (-44, -110))

    inputtap.draw(window)


def Symbols():
    global user_input
    global python_input
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()

        mouseisover = True

        if d_1s.isOver(pos):
            user_input += "+"
            python_input += "+"
            if mouseisover:
                playso.play()
                mouseisover = False

        if d_2s.isOver(pos):
            user_input += "-"
            python_input += "-"
            if mouseisover:
                playso.play()
                mouseisover = False

        if d_3s.isOver(pos):
            user_input += "x"
            python_input += "*"
            if mouseisover:
                playso.play()
                mouseisover = False

        if d_4s.isOver(pos):
            user_input += "÷"
            python_input += "/"
            if mouseisover:
                playso.play()
                mouseisover = False

        if d_5s.isOver(pos):
            result = eval(python_input)
            python_input = ""
            user_input += f"={result}"
            if mouseisover:
                playso.play()
                mouseisover = False

        if d_6s.isOver(pos):
            print("C")
            python_input = ""
            user_input = ""
            if mouseisover:
                playso.play()
                mouseisover = False


def MOUSEOVERnumbers():
    global user_input
    global python_input
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()

        mouseisover = True

        if s_1s.isOver(pos):
            print("1")
            user_input += "1"
            python_input += "1"
            if mouseisover:
                playso.play()
                mouseisover = False

        if s_2s.isOver(pos):
            print("2")
            user_input += "2"
            python_input += "2"
            if mouseisover:
                playso.play()
                mouseisover = False

        if s_3s.isOver(pos):
            print("3")
            user_input += "3"
            python_input += "3"
            if mouseisover:
                playso.play()
                mouseisover = False

        if s_4s.isOver(pos):
            print("4")
            user_input += "4"
            python_input += "4"
            if mouseisover:
                playso.play()
                mouseisover = False

        if s_5s.isOver(pos):
            print("5")
            user_input += "5"
            python_input += "5"
            if mouseisover:
                playso.play()
                mouseisover = False

        if s_6s.isOver(pos):
            print("6")
            user_input += "6"
            python_input += "6"
            if mouseisover:
                playso.play()
                mouseisover = False

        if s_7s.isOver(pos):
            print("7")
            user_input += "7"
            python_input += "7"
            if mouseisover:
                playso.play()
                mouseisover = False

        if s_8s.isOver(pos):
            print("8")
            user_input += "8"
            python_input += "8"
            if mouseisover:
                playso.play()
                mouseisover = False

        if s_9s.isOver(pos):
            print("9")
            user_input += "9"
            python_input += "9"
            if mouseisover:
                playso.play()
                mouseisover = False

        if s_0s.isOver(pos):
            print("0")
            user_input += "0"
            python_input += "0"
            if mouseisover:
                playso.play()
                mouseisover = False

            # the main loop


run = True
user_input = ""
python_input = ""

while run:
    # input tap
    inputtap = button((0, 0, 0), 250, 40, 0, 0, f"{user_input}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        MOUSEOVERnumbers()

        Symbols()

    redraw(inputtap)
    pygame.display.update()

pygame.quit()