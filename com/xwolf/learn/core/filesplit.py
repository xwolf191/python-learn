
"""
超大文件切割

@author xwolf

"""
import os
import time

class filesplit:

    def __init__(self):
        pass

    def split(self, path):

        """
        大文件切割
        :return:
        """
        num = 0
        fnum = 0
        start = time.time()
        for t in os.listdir(path):
            filename = os.path.join(path, t)
            dataPath = os.path.join(path, filename+"_data")
            if not os.path.exists(dataPath):
                os.mkdir(dataPath)
            fname = os.path.join(dataPath, t+"-%d") % fnum
            fw = open(fname, 'w', encoding="utf8")
            fd = open(filename, encoding="utf8")
            for line in fd:
                line = line.strip()
                num = num + 1
                if line:
                    if num > 1000000:
                        num = 0
                        fw.close()
                        fnum = fnum + 1
                        fname = os.path.join(dataPath, t+"-%d") % fnum
                        fw = open(fname, 'w')
                    fw.write(line + '\n')
            fw.close()
            end = time.time()
            print("文件分割完成,耗时{}s".format(end-start))


if __name__ == '__main__':
    f = filesplit()
    f.split("C:\\Users\\Administrator\\Downloads\\logs")
