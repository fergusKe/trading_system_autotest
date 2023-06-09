# ！ /usr/bin/python3
# coding-utf-8
# @Time: 2022/12/7 17:14
# @Author: LYH

import ddddocr


class OcrIdentify:
    def __init__(self):
        self.ocr = ddddocr.DdddOcr()

    def identify(self, pic_path):
        with open(pic_path, 'rb') as f:
            image = f.read()
        res = self.ocr.classification(image)
        return res


if __name__ == '__main__':
    print(OcrIdentify().identify("test.png"))
