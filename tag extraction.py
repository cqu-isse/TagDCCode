#!user/bin/env python3  
# -*- coding: gbk -*- 
import re
p1 = re.compile(r'[\w.#+/-]+')
for i in range(1,50001):
    print(i)
    raw_text = open("/data/lican/StackOverflowsmall/Tags/TagsRaw/Tags%ld.txt"%(i)).read().lower()    
    raw_words = re.findall(p1,raw_text)
    print(raw_words)
    filename = "/data/lican/StackOverflowsmall/Tags/Tags/Tags%ld.txt"%i   
    with open(filename,'w') as f: # ���filename�����ڻ��Զ������� 'w'��ʾд���ݣ�д֮ǰ������ļ��е�ԭ�����ݣ�
        f.write(" ".join(raw_words))
