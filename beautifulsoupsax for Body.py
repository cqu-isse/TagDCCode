# -*- coding: utf-8 -*-

import sys

reload(sys)

sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup

for i in range(1,105109):
        
    path = '/data0/docker/lican/English/Body/Body(raw)/Body%ld.html'%i
    with open(path, 'r') as f:
        Soup = BeautifulSoup(f.read(), 'lxml')
        bodys = Soup.select('p')
    Body = []
    for body in bodys:    
        Body.append(body.getText())
    print(i)
    B = " ".join(Body)
    print(B.encode('utf8'))
    

    
    
    filename = "/data0/docker/lican/English/Body/Bodybeautifulsoup/Body%ld.txt"%i     
    with open(filename,'w') as f: # ���filename�����ڻ��Զ������� 'w'��ʾд���ݣ�д֮ǰ������ļ��е�ԭ�����ݣ�
        f.write(B.encode('utf8'))
     
    