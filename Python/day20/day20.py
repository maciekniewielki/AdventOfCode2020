import re
from collections import Counter
import math


def parse(data):
    images = {}
    next_num = 0
    current_image = []
    for line in data:
        if line.startswith("Tile"):
            next_num = int(line.split()[1][:-1])
            continue
        if line == "":
            images[next_num] = current_image[:]
            current_image = []
            continue
        current_image.append(line)

    return images


def solve_1(images):
    all_hashes = []
    for i in images:
        all_hashes += get_side_hashes(images[i])

    c = Counter(all_hashes)
    side_hashes = [h for h, count in c.most_common() if count == 1]
    return side_hashes, [i for i in images if get_side_score(images[i], side_hashes) == 4]


def get_side_hashes(image):
    top = image[0]
    bottom = image[-1]
    left = ''.join([row[0] for row in image])
    right = ''.join([row[-1] for row in image])

    sides = [top, left, bottom, right]
    sides += [s[::-1] for s in sides]

    return [hash_side(s) for s in sides]


def get_side_score(image, side_hashes):
    hashes = get_side_hashes(image)
    score = 0
    for h in hashes:
        if h in side_hashes:
            score += 1
    return score


def hash_side(side):
    return int(side.replace("#", "1").replace(".", "0"), 2)


# IO
data = [line.rstrip() for line in open("input.txt").readlines()]
images = parse(data)

# 1st
most_side_hashes, corner_images = solve_1(images)
print(math.prod(corner_images))
