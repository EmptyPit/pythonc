import os


def way(path):
    tree = os.walk(path)
    for root, dirs, files in tree:
        for name in files:
            fullname = os.path.join(name, root)
            #a = fullname.rstrip('/n')
            # always give meaningful names to variables and functions
            s = os.path.getsize(fullname)
            ww = name.rstrip('/n')
            kl = ['Kb', 'Mb', 'Gb', 'B']
            ol = s / 1024.0
            of = round(ol, 2)
            if of < 1:
                er = of * 100
                print(('{:35s} {:10} {}'.format(ww, int(er), kl[3])))
            elif of < 1000:
                print(('{:35s} {:10} {}'.format(ww, of, kl[0])))
            elif of > 1000:
                print(('{:35s} {:10} {}'.format(ww, of, kl[1])))
            elif of > 1000000:
                print(('{:35s} {:10} {}'.format(ww, of, kl[2])))

# make script accept path from user
way('/home/andrii/')

