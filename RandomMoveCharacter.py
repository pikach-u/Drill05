from pico2d import *
import random
import turtle

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
point = load_image('hand_arrow.png')

def MoveTo(p1, p2):
    pass

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

running = True
x, y = TUK_WIDTH//2, TUK_HEIGHT//2
frame = 0
dirX = 0
i = 0

p = (random.randint(100, 900), random.randint(100, 900))

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)

    #랜덤위치에 손이 표시 (p[0], p[1]) / (x, y)
    point.draw(p[0], p[1])

    # 캐릭터가 바라보는 방향이 이동 방향과 일치
    #if dirX >= 0:
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    # elif dirX < 0:
    #     character.clip_draw(frame * 100, 100, 100, 100, x, y)


    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    # 소년이 손을 따라감
    t = i/100
    x = (1 - t) * x + t * p[0]  # 1-t : t의 비율로 x1, x2를 섞는다 (더한다)
    y = (1 - t) * y + t * p[1]
    i+=1
    delay(0.05)

    # 손에 도착하면 손이 자동으로 랜덤 생성
    if(x == p[0] and y == p[1]):
        i=0
        dirX=0
        p = (random.randint(100, 900), random.randint(100, 900))
        # if x >= TUK_WIDTH//2 :
        #     dirX += 1
        # else:
        #     dirX -= 1



