# -*- coding: utf-8 -*-
import sys
import re
import rle


def main():
    plain = '000000200011111111223333333345555555556666666667788890'  # sample data
    print("元データ({0:4d}):{1}".format(len(plain), plain))

    r = rle.RLE()
    data = list(r.nchars(plain, 3))     # 3文字以上文字連長探索
    # 3文字以上文字連長ある場合
    if data:
        compressed = r.rle(plain, data)
        print("圧縮　　({0:4d}):{1}".format(len(compressed), compressed))
        # 文字が含まれている場合(a~i)
        if re.findall('[a-i]', compressed):
            uncompressed = r.unrle(compressed)
            print("解凍　　({0:4d}):{1}".format(len(uncompressed), uncompressed))
    else:
        print('3文字以上文字連長なし')
    return


if __name__ == "__main__":
    main()
    sys.exit()
