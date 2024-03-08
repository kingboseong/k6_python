
import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

image = pygame.image.load('./pcc_3e/chapter_12/adding_ship_image/images/ship.bmp')

rect = image.get_rect()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #QUIT = x버튼 = 화면 끔
            pygame.quit()
            sys.exit
            # raise SystemExit

#키보드 이벤트 동작 구현 / updates위치 -비행기의
    # Do logical updates here.
    # ...

#화면 색
    screen.fill("black")  # Fill the display with a solid color

#render 그래픽스(비행기, 적, 총알, 점수...)
    # Render the graphics here.
    # ...
    screen.blit(image, rect)

#flip() = 다시 while문으로 이동해서 계속 돈다. => 이를 통해서 비행기가 이동하게 만들어 준다. => 60fps형성됨.
#이동한 비행기의 모습을 그리고 flip해주는 것을 초당 60번씩 실행한다.
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)