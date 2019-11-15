import glob
import os

def main():
    file = glob.glob('001_my_test/REDS4/*/*')
    for a in file:
        name = str(int(os.path.split(a)[1].split('.')[0]) + 1).zfill(6) + '.png'
        os.rename(a,os.path.join(os.path.split(a)[0],name))
        print(name)

if __name__ == "__main__":
    main()
