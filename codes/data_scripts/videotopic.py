import cv2
import pathlib
import glob
from sklearn.model_selection import train_test_split
import os
from joblib import Parallel,delayed

def main():
    vlist = list(map(lambda x: x.split('/')[-1], glob.glob('/mnt/sdb/duan/SR/data/gt/*')))
    test = list(map(lambda x: x.split('/')[-1], glob.glob('/mnt/sdb/duan/SR/testdata/SDR_540p/*')))
    train, val = train_test_split(vlist, test_size=0.01, random_state=42)

    gt_vpath = '/mnt/sdb/duan/SR/data/gt'
    input_vpath = '/mnt/sdb/duan/SR/data/input'
    train_gt_ppath = '/mnt/sdb/duan/EDVR/datasets/AI_4K/train/gt'
    train_input_ppath = '/mnt/sdb/duan/EDVR/datasets/AI_4K/train/input'
    val_gt_ppath = '/mnt/sdb/duan/EDVR/datasets/AI_4K/val/gt'
    val_input_ppath = '/mnt/sdb/duan/EDVR/datasets/AI_4K/val/input'
    test_input_ppath = '/mnt/sdb/duan/EDVR/datasets/AI_4K/test/gt'
    test_input_vpath = '/mnt/sdb/duan/SR/testdata/SDR_540p'
    def parallelvideotopic(x,mode):
        if mode == 'train':
            vpath = os.path.join(gt_vpath, x)
            ppath = os.path.join(train_gt_ppath, x.split('.')[0])

            videotopic(vpath, ppath)

            vpath = os.path.join(input_vpath, x)
            ppath = os.path.join(train_input_ppath, x.split('.')[0])
            videotopic(vpath, ppath)
        if mode == 'val':
            vpath = os.path.join(gt_vpath, x)
            ppath = os.path.join(val_gt_ppath, x.split('.')[0])
            videotopic(vpath, ppath)

            vpath = os.path.join(input_vpath, x)
            ppath = os.path.join(val_input_ppath, x.split('.')[0])
            videotopic(vpath, ppath)
        if mode == 'test':
            vpath = os.path.join(test_input_vpath, x)
            ppath = os.path.join(test_input_ppath, x.split('.')[0])
            videotopic(vpath, ppath)

    #Parallel(n_jobs=10)(delayed(parallelvideotopic)(x,mode='train') for x in train)
    #Parallel(n_jobs=10)(delayed(parallelvideotopic)(x,mode='val') for x in val)
    Parallel(n_jobs=10)(delayed(parallelvideotopic)(x,mode='test') for x in test)
        


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
        #a = cv2.resize(frame,(3840,2160))
    else:
        print('fal')
        rval = False
    while rval:
        path = os.path.join(ppath, str(c).zfill(6))
        cv2.imwrite(path + '.png', frame)
        rval, frame = videoCapture.read()
        # if rval:
        #     a = cv2.resize(frame,(3840,2160))
        
        c = c + 1
    videoCapture.release()
    print(size)
    print(fNUMS)
    print(fps)
    print(vpath)


if __name__ == "__main__":
    #main()
    videotopic('/mnt/sdb/duan/EDVR/codes/data_scripts/16536366.mp4','test_videotopic')
