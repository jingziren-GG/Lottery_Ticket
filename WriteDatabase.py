# -*- coding:utf-8 -*-
import json
import pymssql


def OpenJson(FileName):
    # 我的本地数据库sqlserver
    conn = pymssql.connect('127.0.0.1','账户','密码','库名')
    data = open(FileName,'r+')
    textlist = data.read().split(',\n')
    cursor = conn.cursor()

    for text in textlist[::-1]:
        if text:
            print(text)
            da = json.loads(text)
            # da['ball_data']
            # da['blue_ball']
            red = ''
            for x in da['red_ball'].split('-'):
                red += 'A' + str(x) + ','
            blue = 'B' + da['blue_ball']
            data = da['ball_data']
            seq = da['ball_sequence'] + '>' + da['blue_ball']
            # print(blue)
            # print(red)
            # print(data)
            # print(seq)
            if seq == '>':
                sql_red = ''
                sql_blue = ''
            else:
                sql_red = "insert into red_ball(Red_Blue,%speriods) values ('%s',1,1,1,1,1,1,%s)"%(red,seq,data)
                sql_blue = "insert into blue_ball(Red_Blue,%s,periods) values ('%s',1,%s)"%(blue,seq,data)
            print(sql_red)
            print(sql_blue)
            try:
                Sales_volums = da['sales_volums']
            except KeyError:
                Sales_volums = '0'
            try:
                All_Bouns = da['All_Bouns']
                if All_Bouns == '--':
                    raise KeyError
            except KeyError:
                All_Bouns = '0'
            try:
                Fir_NumShare = da['First_price_NumShare']
            except KeyError:
                Fir_NumShare = '0'
            try:
                Fir_Bonus = da['First_price_Bonus']
            except KeyError:
                Fir_Bonus = '0'
            try:
                Sec_NumShare = da['Second_price_NumShare']
            except KeyError:
                Sec_NumShare = '0'
            try:
                Sec_Bonus = da['Second_price_Bonus']
            except KeyError:
                Sec_Bonus = '0'
            try:
                Thi_Bonus = da['Third_price_Bonus']
            except KeyError:
                Thi_Bonus = '0'
            try:
                Four_Bonus = da['Fourth_price_Bonus']
            except KeyError:
                Four_Bonus = '0'
            try:
                Fif_Bonus = da['Fifth_price_Bonus']
            except KeyError:
                Fif_Bonus = '0'
            try:
                Six_Bonus = da['Sixth_price_Bonus']
            except KeyError:
                Six_Bonus = '0'
            sql_Vol = 'insert into Volums values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'%(Sales_volums,All_Bouns,Fir_NumShare,Fir_Bonus,Sec_NumShare,Sec_Bonus,Thi_Bonus,Four_Bonus,Fif_Bonus,Six_Bonus,data)
            print(sql_Vol)
            cursor = conn.cursor()
            cursor.execute(sql_red)
            cursor.execute(sql_blue)
            cursor.execute(sql_Vol)
            conn.commit()



    # print(text)


if __name__ == '__main__':
    OpenJson('xxx.json')
