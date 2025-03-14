import pygame
import pygame as pg
import random

width = 700
height = 450
FPS = 60
background_color = (255, 255, 255)

x_direction = 0
y_direction = 0
player_speed = 2

images_dict = {
    'bg': pg.image.load('img/Background.png'),
    'player': {
        'rear': pg.image.load('img/cab_rear.png'),
        'left': pg.image.load('img/cab_left.png'),
        'right': pg.image.load('img/cab_right.png'),
        'front': pg.image.load('img/cab_front.png'),
    },
    'hole': pg.image.load('img/hole.png'),
    'hotel': pg.transform.scale(pg.image.load('img/hotel.png'),(80, 80)),
    'pas': pg.image.load('img/passenger.png'),
    'screen': pg.image.load('img/screenshot.jpg'),
    't_bg': pg.transform.scale(pg.image.load('img/taxi_background.png'), (80, 45))

}

player_view = 'rear'
player_rect = images_dict['player'][player_view].get_rect()
player_rect.x = 300
player_rect.y = 300

hotel_positions = [
    (60, 30),
    (555, 30),
    (60, 250),
    (555, 250)
]

parking_img = images_dict['t_bg']
parking_rect = parking_img.get_rect()
parking_rect.x, parking_rect.y = hotel_positions[0][0], hotel_positions[0][1] + 80

# Місця для спавну пасажира біля готелів
passenger_spawn_positions = [
    (60, 120),  # Біля першого готелю
    (555, 120),  # Біля другого готелю
    (60, 370),  # Біля третього готелю
    (555, 370)   # Біля четвертого готелю
]

# Випадкове розміщення пасажира
passenger_position = random.choice(passenger_spawn_positions)
passenger_rect = images_dict['pas'].get_rect()
passenger_rect.topleft = passenger_position

pg.init()
screen = pg.display.set_mode([width, height])

timer = pg.time.Clock()

run = True
while run:
    timer.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys_klav = pg.key.get_pressed()
    if keys_klav[pg.K_RIGHT]:
        x_direction = 1
        player_view = 'right'
    elif keys_klav[pg.K_LEFT]:
        x_direction = -1
        player_view = 'left'
    elif keys_klav[pg.K_UP]:
        y_direction = -1
        player_view = 'rear'
    elif keys_klav[pg.K_DOWN]:
        y_direction = 1
        player_view = 'front'

    player_rect.x += player_speed * x_direction
    player_rect.y += player_speed * y_direction
    x_direction = 0
    y_direction = 0

    # Перевірка на межі екрану:
    if player_rect.x < 0:
        player_rect.x = 0
    elif player_rect.x > width - player_rect.width:
        player_rect.x = width - player_rect.width

    if player_rect.y < 0:
        player_rect.y = 0
    elif player_rect.y > height - player_rect.height:
        player_rect.y = height - player_rect.height

    screen.fill(background_color)
    screen.blit(images_dict['bg'], (0, 0))

    for position in hotel_positions:
        hotel_rect = images_dict['hotel'].get_rect()
        hotel_rect.topleft = position
        screen.blit(images_dict['hotel'], hotel_rect)

    # Малюємо пасажира
    screen.blit(images_dict['pas'], passenger_rect)

    screen.blit(parking_img, parking_rect)
    screen.blit(images_dict['player'][player_view], player_rect)

    pygame.display.flip()

pygame.quit()
