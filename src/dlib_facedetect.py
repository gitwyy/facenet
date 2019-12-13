"""
使用 dlib 工具包 提取人脸数据
"""
import argparse
import glob
import os
import sys

import cv2
import dlib


def main(args):
    im_floder = args.input_dir
    crop_im_path = args.output_dir
    im_floder_list = glob.glob('{}/*'.format(im_floder))
    detector = dlib.get_frontal_face_detector()
    idx = 0
    for idx_floder in im_floder_list:
        im_list = glob.glob('{}/*'.format(idx_floder))
        im_path = '{}/{}'.format(crop_im_path, "%03d" % idx)
        if not os.path.exists(im_path):
            # print("im_path not exists do mkdir ", im_path)
            os.mkdir(im_path)
        idx_im = 0
        for im_path in im_list:
            im_data = cv2.imread(im_path)
            dets = detector(im_data, 1)
            # print(dets)
            if dets.__len__() == 0:
                continue
            d = dets[0]
            x1 = d.left()
            y1 = d.top()
            x2 = d.right()
            y2 = d.bottom()

            x1 = int(x1 - (x2 - x1) * 0.05)
            x2 = int(x2 + (x2 - x1) * 0.05)
            y1 = int(y1 - (y2 - y1) * 0.3)
            y2 = y2

            im_crop_data = im_data[y1:y2, x1:x2]
            im_data = cv2.resize(im_crop_data, (160, 160))
            im_save_path = "{}/{}/{}_{}.jpg".format(crop_im_path, "%03d" % idx, "%03d" % idx, "%04d" % idx_im)
            print("crop save path : ", im_save_path)
            # cv2.imshow(im_save_path, im_data)
            # cv2.waitKey(0)
            cv2.imwrite(im_save_path, im_data)
            idx_im += 1
        idx += 1


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_dir', type=str,
                        help='输入数据路径，待提取图片路径', default='', required=True)
    parser.add_argument('--output_dir', type=str,
                        help='输出数据路径，处理完成图片路径', default='', required=True)
    return parser.parse_args(argv)


if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
