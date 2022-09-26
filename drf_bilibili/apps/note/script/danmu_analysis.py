# -*- coding: utf-8 -*-

import pymysql
import jieba
from collections import Counter
from datetime import datetime

import re

def get_hot_words():
    def find_chinese(file):
        pattern = re.compile(r'[^\u4e00-\u9fa5]')
        chinese = re.sub(pattern, '', file)
        # print(chinese)
        return chinese

    def word_analysis(data,cid):
        # 词频统计
        result= dict(Counter(data))
        result = sorted(result.items(),key=lambda x: x[1], reverse=True)
        now=datetime.now().isoformat()[:10]
        add = (cid,now,now)
        limit = 10 #热词数量
        table="note_danmu_hotwords"

        for l in range(limit):
            data=(result[l]+add)
            print(data)
            sql = 'insert into %s (hot_word,num,cid,update_time,create_time) values (%s)' % (table,'%s,%s,%s,%s,%s')
            # sql2='insert into kol_info(rank,user_level,silence,fans_badge,birthday,role_type,title,des,is_type) values ()'
            curs.execute(sql, data)
            print('%s表插入数据' % table)
            db.commit()

    db = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='bili',
                              port=3306, charset='utf8mb4')

    curs = db.cursor()

    sql1 = '''select content,cid_id from note_danmu Limit 20'''  # sql语句
    curs.execute(sql1)
    row = curs.fetchall()  # 读取数据表内容，返回元祖类型,元祖的每个元素还是为元祖

    data = []
    last_cid=row[0][1]
    for i in row:
        cid=i[1]
        if cid != last_cid:
            word_analysis(data,last_cid)
            last_cid = cid
            data = []
        content=find_chinese(i[0])
        xx = ' '.join(jieba.cut(content))  # 每一段字符串进行分词
        yy = xx.split(' ')

        yy=filter(lambda y:len(y)>1,yy)
        data.extend(yy)
    else:
        word_analysis(data,cid)

if __name__ == '__main__':
    get_hot_words()



