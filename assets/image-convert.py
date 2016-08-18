import os
from PIL import Image


def all_files(dirname):
    for (root, _, files) in os.walk(dirname):
        for fn in files:
            yield os.path.join(root, fn)


def convert_image(file):
    img = Image.open(file)
    print(os.path.splitext(file)[0] + '.jpg')
    img.save(os.path.splitext(file)[0] + '.jpg')
    os.remove(file)


def main():
    fns = []
    for fn in all_files('.'):
        if os.path.splitext(fn)[1] == '.png':
            fns.append(fn)

    for fn in fns:
        convert_image(fn)

if __name__ == '__main__':
    main()
