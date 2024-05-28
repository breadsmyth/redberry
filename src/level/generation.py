import gzip
import json
from math import floor
from perlin_noise import PerlinNoise


def generate(seed):
    level = {
        'seed': seed,
        'block_dict': {1: 'base.dirt', 2: 'base.stone', 3: 'base.grass'},
        'chunks': {}}
    for chunk_x in range(8):
        for chunk_y in range(8):
            level['chunks'][f'{chunk_x},{chunk_y}'] = make_chunk(seed, chunk_x, chunk_y)
    
    return level


def make_chunk(seed, chunk_x, chunk_y):
    noise = PerlinNoise(octaves=8, seed=seed)
    chunk = {}

    for block_x in range(16):
        for block_y in range(16):
            hgt = noise([block_x/16 + chunk_x*16, block_y/16 + chunk_y*16])
            chunk[f'{block_x},{block_y}'] = floor(hgt * 5)
    
    return chunk
    

def save(level, filename):
    level_json = json.dumps(level)
    level_zip = gzip.compress(level_json.encode())
    with open(filename, 'wb') as file:
        file.write(level_zip)


def load(filename):
    with open(filename, 'rb') as file:
        level_zip = file.read()
    level_json = gzip.decompress(level_zip).decode()
    return json.loads(level_json)


def generate_test_level():
    level = {
        'seed': 0,
        'block_dict': {1: 'base.dirt', 2: 'base.stone', 3: 'base.grass'},
        'chunks': {

        '0,0': {'0,0,0': 1, '0,0,1': 2, '1,2,3': 3},
        '0,1': {'0,0,0': 1},
        '0,2': {'0,0,0': 1},
        '1,0': {'0,0,0': 1}}}
    
    return level
