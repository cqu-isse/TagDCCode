# coding=gbk
for i in range(1,11203033):
    body = open("/data0/docker/lican/Cooking/Body/Body(raw)/Body%d.txt"%(i),'r').read()
    print(body)
    
    filename = "/data0/docker/lican/Cooking/Body/Body(html)/Body%ld.html"%i  
    print(i)
 
    with open(filename,'w') as f: # ���filename�����ڻ��Զ������� 'w'��ʾд���ݣ�д֮ǰ������ļ��е�ԭ�����ݣ�
        f.write(body)
     
       
 


