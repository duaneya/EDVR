import cv2
import pathlib
import glob
from sklearn.model_selection import train_test_split
import os


def main():
    vlist = list(map(lambda x: x.split('/')[-1], glob.glob('/mnt/sdb/duan/SR/data/gt/*')))
    train, val = train_test_split(vlist, test_size=0.1, random_state=42)

    gt_vpath = '/mnt/sdb/duan/SR/data/gt'
    input_vpath = '/mnt/sdb/duan/SR/data/input'
    train_gt_ppath = '/mnt/sdb/duan/EDVR/datasets/AI_4K/train/gt'
    train_input_ppath = '/mnt/sdb/duan/EDVR/datasets/AI_4K/train/input'
    val_gt_ppath = '/mnt/sdb/duan/EDVR/datasets/AI_4K/val/gt'
    val_input_ppath = '/mnt/sdb/duan/EDVR/datasets/AI_4K/val/input'

    for x in train:

        vpath = os.path.join(gt_vpath, x)
        ppath = os.path.join(train_gt_ppath, x.split('.')[0])


        videotopic(vpath, ppath)

        vpath = os.path.join(input_vpath, x)
        ppath = os.path.join(train_input_ppath, x.split('.')[0])
        videotopic(vpath, ppath)

    for x in val:
        vpath = os.path.join(gt_vpath, x)
        ppath = os.path.join(val_gt_ppath, x.split('.')[0])
        videotopic(vpath, ppath)

        vpath = os.path.join(input_vpath, x)
        ppath = os.path.join(val_input_ppath, x.split('.')[0])
        videotopic(vpath, ppath)


def videotopic(vpath, ppath):

    videoCapture = cv2.VideoCapture(vpath)

    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fNUMS = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    if not os.path.exists(ppath):
        os.makedirs(ppath)
    c = 0
    if videoCapture.isOpened():
        rval, frame = videoCapture.read()
    else:
        print('fal')
        rval = False
    while rval:
        path = os.path.join(ppath, str(c).zfill(6))
        cv2.imwrite(path + '.jpg', frame)
        rval, frame = videoCapture.read()
        c = c + 1
    videoCapture.release()
    print(size)
    print(fNUMS)
    print(fps)
    print(vpath)


if __name__ == "__main__":
    main()
