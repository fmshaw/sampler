import pygame
import random
import code

s = pygame.display.set_mode((256,256))

tl = ((0,0), (255, 0, 0))
tr = ((255,0), (0, 255, 0))
bl = ((0,255), (0, 0, 255))
br = ((255,255), (0, 0, 0))

pts = (tl, tr, bl, br)

def dist(scoord, coord):
    (x1, y1), (x2, y2) = scoord, coord # unpack to ordinals
    dist2 = (x1 - x2) ** 2 + (y1 - y2) ** 2 # pythagoras: hypotenuse area of cartesian
    dist = dist2 ** 0.5 # pythag: sqrt hyp^2
    return dist # hypotenuse

def area(c1, c2, c3):
    (ax, ay), (bx, by), (cx, cy) = c1, c2, c3
    return abs((
        ax * (by - cy) +
        bx * (cy - ay) +
        cx * (ay - by)
        ) / 2.0)

def scale(factor, color):
    return [factor * x for x in color]

def simplex2d(x, y):
    p = (x, y)
    if x > y:
        (p1, c1), (p2, c2), (p3, c3) = tl, tr, br
    else:
        (p1, c1), (p2, c2), (p3, c3) = tl, bl, br
    area_tot = area(p1, p2, p3) + 1000 # + 1000 is a dirty cheat as scales don't add to 1.0

    area_p1 = area(p, p2, p3)
    area_p2 = area(p, p1, p3)
    area_p3 = area(p, p1, p2)

    s1 = area_p1 / (area_tot)
    s2 = area_p2 / (area_tot)
    s3 = area_p3 / (area_tot)
#s Ln#42    if (s1 + s2 + s3) > 1.0:
#        print sum([s1, s2, s3])
    c1 = scale(s1, c1)
    c2 = scale(s2, c2)
    c3 = scale(s3, c3)

    c = (
        int(c1[0] + c2[0] + c3[0]),
        int(c1[1] + c2[1] + c3[1]),
        int(c1[2] + c2[2] + c3[2]))

    return c

sample = simplex2d

def nk_samples(n):
    for i in range(n * 1000):
        x = random.random() * 256
        y = random.random() * 256
        s.fill(
            sample(x, y),
            ((x, y), (1, 1)))
    pygame.display.flip()

nk_samples(1)

code.interact(local=locals())

pygame.display.quit()

