import os


def way(path):
    tree = os.walk(path)
    for root, dirs, files in tree:
        for name in files:
            fullname = os.path.join(name, root)
            size = os.path.getsize(fullname)
            ww = name.rstrip('/n')
            kl = ['Kb', 'Mb', 'Gb', 'B']
            human_size = size / 1024.0
            of = round(human_size, 2)
            if of < 1:
                er = of * 100
                print(('{:35s} {:10} {}'.format(ww, int(er), kl[3])))
            elif of < 1000:
                print(('{:35s} {:10} {}'.format(ww, of, kl[0])))
            elif of > 1000:
                print(('{:35s} {:10} {}'.format(ww, of, kl[1])))
            elif of > 1000000:
                print(('{:35s} {:10} {}'.format(ww, of, kl[2])))

way(input('Enter the way'))