import os


def files(path: str) -> str:
    return os.path.join('files', os.path.basename(path))
