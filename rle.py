# -*- coding: utf-8 -*-
import re


class RLE:

    # 文字連長探索メソッド
    @classmethod
    def nchars(cls, s, n):
        # 文字列 s に、同じ文字が n 個以上連続している部分文字列を見つける
        assert n > 0
        reg = re.compile("(.)\\1{%d,}" % (n - 1))  # カンマを取ると n 個ちょうどになる
        while True:
            m = reg.search(s)
            if not m:
                break
            yield m.group(0), len(m.group(0)), m.start(), m.end()   # 連長文字列,連長文字数,開始位置,終了位置
            s = s[m.end():]

    # 文字連長圧縮メソッド
    # index -> 文字蓮長圧縮処理の処理が終わった位置
    @classmethod
    def rle(cls, data, rle_data):
        result = data[0:rle_data[0][2]]
        index = int(rle_data[0][2])
        for i, rle_data_row in enumerate(rle_data):
            if rle_data_row[1] == 3:  # 同じ文字が3個ある場合(3=a)
                result = result + str(rle_data_row[0][0]) + 'a'
            elif rle_data_row[1] == 4:  # 同じ文字が4個ある場合(4=b)
                result = result + str(rle_data_row[0][0]) + 'b'
            elif rle_data_row[1] == 5:  # 同じ文字が5個ある場合(5=c)
                result = result + str(rle_data_row[0][0]) + 'c'
            elif rle_data_row[1] == 6:  # 同じ文字が6個ある場合(6=d)
                result = result + str(rle_data_row[0][0]) + 'd'
            elif rle_data_row[1] == 7:  # 同じ文字が7個ある場合(7=e)
                result = result + str(rle_data_row[0][0]) + 'e'
            elif rle_data_row[1] == 8:  # 同じ文字が8個ある場合(8=f)
                result = result + str(rle_data_row[0][0]) + 'f'
            elif rle_data_row[1] == 9:  # 同じ文字が9個ある場合(9=g)
                result = result + str(rle_data_row[0][0]) + 'g'
            elif rle_data_row[1] == 10:  # 同じ文字が10個ある場合(10=h)
                result = result + str(rle_data_row[0][0]) + 'h'
            elif rle_data_row[1] == 11:  # 同じ文字が11個ある場合(11=i)
                result = result + str(rle_data_row[0][0]) + 'i'
            index = index + int(rle_data_row[1])
            # 連長文字列が複数ある場合
            if len(rle_data) > i + 1:
                # 連長文字列が連続でない場合, 次の蓮長文字との間の文字を加える
                if rle_data[i + 1][2] > 0:
                    # rle_dataに次の蓮長文字との間の文字を加える(最初の蓮長文字の終了位置 ~ 次の蓮長文字の開始位置)
                    result = result + data[index:index + rle_data[i + 1][2]]
                    index = index + rle_data[i + 1][2]
        else:
            # 最後に蓮長文字列以外の値がある場合にそれを加える
            if len(data) > index:
                result = result + data[index:len(data)]
        return result

    # 文字連長回答メソッド
    @classmethod
    def unrle(cls, rle_data):
        for i in range(len(re.findall('[a-i]', rle_data))):  # rle_dataにa~hが含まれている個数分for文実行
            if 'a' in rle_data:  # rle_dataにaが含まれいる場合(同じ文字が3個ある場合[a=3])
                place = rle_data.index('a')  # aの文字がある位置(数字)
                converting_data = 3 * str(rle_data[rle_data.index('a') - 1])  # aの位置の前の文字を3連長文字列にする
                rle_data = rle_data[:place - 1] + converting_data + rle_data[place + 1:]  # 元の文字列の[_a]の部分を連長文字列にする
            elif 'b' in rle_data:  # rle_dataにbが含まれいる場合(同じ文字が4個ある場合[b=4])
                place = rle_data.index('b')  # bの文字がある位置(数字)
                converting_data = 4 * str(rle_data[rle_data.index('b') - 1])  # bの位置の前の文字を4連長文字列にする
                rle_data = rle_data[:place - 1] + converting_data + rle_data[place + 1:]  # 元の文字列の[_b]の部分を連長文字列にする
            elif 'c' in rle_data:  # rle_dataにcが含まれいる場合(同じ文字が5個ある場合[c=5])
                place = rle_data.index('c')  # cの文字がある位置(数字)
                converting_data = 5 * str(rle_data[rle_data.index('c') - 1])  # cの位置の前の文字を5連長文字列にする
                rle_data = rle_data[:place - 1] + converting_data + rle_data[place + 1:]  # 元の文字列の[_c]の部分を連長文字列にする
            elif 'd' in rle_data:  # rle_dataにdが含まれいる場合(同じ文字が6個ある場合[d=6])
                place = rle_data.index('d')  # dの文字がある位置(数字)
                converting_data = 6 * str(rle_data[rle_data.index('d') - 1])  # dの位置の前の文字を6連長文字列にする
                rle_data = rle_data[:place - 1] + converting_data + rle_data[place + 1:]  # 元の文字列の[_d]の部分を連長文字列にする
            elif 'e' in rle_data:  # rle_dataにeが含まれいる場合(同じ文字が7個ある場合[e=7])
                place = rle_data.index('e')  # eの文字がある位置(数字)
                converting_data = 7 * str(rle_data[rle_data.index('e') - 1])  # eの位置の前の文字を7連長文字列にする
                rle_data = rle_data[:place - 1] + converting_data + rle_data[place + 1:]  # 元の文字列の[_e]の部分を連長文字列にする
            elif 'f' in rle_data:  # rle_dataにfが含まれいる場合(同じ文字が8個ある場合[f=8])
                place = rle_data.index('f')  # fの文字がある位置(数字)
                converting_data = 8 * str(rle_data[rle_data.index('f') - 1])  # fの位置の前の文字を8連長文字列にする
                rle_data = rle_data[:place - 1] + converting_data + rle_data[place + 1:]  # 元の文字列の[_f]の部分を連長文字列にする
            elif 'g' in rle_data:  # rle_dataにgが含まれいる場合(同じ文字が9個ある場合[g=9])
                place = rle_data.index('g')  # gの文字がある位置(数字)
                converting_data = 9 * str(rle_data[rle_data.index('g') - 1])  # gの位置の前の文字を9連長文字列にする
                rle_data = rle_data[:place - 1] + converting_data + rle_data[place + 1:]  # 元の文字列の[_g]の部分を連長文字列にする
            elif 'h' in rle_data:  # rle_dataにhが含まれいる場合(同じ文字が10個ある場合[h=10])
                place = rle_data.index('h')  # hの文字がある位置(数字)
                converting_data = 10 * str(rle_data[rle_data.index('h') - 1])  # hの位置の前の文字を10連長文字列にする
                rle_data = rle_data[:place - 1] + converting_data + rle_data[place + 1:]  # 元の文字列の[_h]の部分を連長文字列にする
            elif 'i' in rle_data:  # rle_dataにiが含まれいる場合(同じ文字が11個ある場合[i=11])
                place = rle_data.index('i')  # iの文字がある位置(数字)
                converting_data = 11 * str(rle_data[rle_data.index('i') - 1])  # iの位置の前の文字を11連長文字列にする
                rle_data = rle_data[:place - 1] + converting_data + rle_data[place + 1:]  # 元の文字列の[_i]の部分を連長文字列にする
        return rle_data
