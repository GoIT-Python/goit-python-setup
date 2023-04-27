import os


def parse(path):
    fname = []
    for root, _, f_names in os.walk(path):
        for f in f_names:
            fname.append(os.path.join(root, f))
    return fname
