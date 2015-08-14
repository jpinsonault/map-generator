from noise import snoise2

def generate_heightmap(freq, octaves):
    return [[int(snoise2(x / freq, y / freq, octaves) * 127.0 + 128.0) for x in range(256)] for y in range(256)]

