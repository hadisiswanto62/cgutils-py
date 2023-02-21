from pathlib import Path

import lz4.block


def get_writer(filepath, mode, *args, **kwargs):
    if "r" in mode:
        raise ValueError(f"Invalid mode for writer '{mode}'")
    path = Path(filepath)
    create_basedir(filepath)
    return path.open(mode, *args, **kwargs)

def create_basedir(filepath: str):
    path = Path(filepath)
    if not path.parent.exists():
        path.parent.mkdir(parents=True)

def exist(filepath: str):
    path = Path(filepath)
    return path.exists()

def decompress(bytes):
    length = sum([
        (bytes[4 + i] & 0xFF) << 8 * i
        for i in range(4)
    ])
    return lz4.block.decompress(bytes[16:], length, True)
