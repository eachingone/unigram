# -*- coding: utf-8 -*-
"""
信息191郑依晴  19119121
"""
import os
import time


#-----读取txt文本-------
def read_txt(path):
    with open(path,'r',encoding='utf8')as f:
        lines=f.read()
    #删除一些无关的字符
    lines  = lines.replace(' ','')
    lines  = lines.replace('\u3000','')
    lines  = lines.replace('\n','')
    lines  = lines.replace('\xa0','')
    return lines

#----输出list-----
def write_txt(path,list1):
    with open(path,'w',encoding='utf8')as f:
        for item in list1:
            f.write(str(item)+'\n')
    f.close
 

#-----遍历文件夹，输出含所有路径的列表-----
def fun(path):
    fileArray = []
    for root,dirs,files in os.walk(path):
    #其中，root为根目录路径，dirs是root路径下的目录列表，files为root路径下的文件列表
        for f in files:
            eachpath = str(root+'/'+f)
            fileArray.append(eachpath)
    return fileArray

#----一元分词-----
def unigram(txt,list0):
    dict1={}
    
    for key in list0:
        dict1[key]=dict1.get(key, 0) + 1
    
    #排序
    list1_1 = sorted(dict1.items(),key = lambda x:x[1],reverse = True) #建立列表进行降序排序

    return list1_1 


#----二元分词-----
def bigram(txt,list0):
    dict2 = {}
    list2=[]
    
    #-----建立二元字典-----
    for i in range(len(list0)-1):  #0到len（wordlist）-2
        diword=list0[i]+list0[i+1]
        list2.append(diword)
        dict2[diword] = 0
 
    #给二元字典放value
    for key in list2:
        dict2[key]=dict2.get(key, 0) + 1
       
    #----rank排序-----
    list2_2 = sorted(dict2.items(),key = lambda x:x[1],reverse = True) #建立列表进行降序排序
    return list2_2

   
#----三元分词-----
def trigram(txt,list0):
    dict3 = {}
    list3=[]
    
    #-----建立三元字典-----
    for i in range(len(list0)-2):
        diword=list0[i]+list0[i+1]+list0[i+2]
        list3.append(str(diword))
        dict3[diword] = 0
    #给三元字典放value
    for key in list3:
        dict3[key]=dict3.get(key, 0) + 1
    
    #-----rank排序-----
    list3_3 = sorted(dict3.items(),key = lambda x:x[1],reverse = True) #建立列表进行降序排序
    return list3_3

#------主函数------
def main():
    start=time.time()
    #---声明路径----
    path1=r"cnl人民日报数据20201109"
    path2_1="result//一元分词result.txt"   
    path2_2="result//二元分词result.txt"
    path2_3="result//三元分词result.txt"
    
    txt=''
    allpath=fun(path1)  #所有目录下的路径均存放在列表allpath里
    for everypath in allpath:  #这一部分用时1s
        txt+=read_txt(everypath)
    
    #先把所有的一元文本装入列表，作为一个文本单个分词的预处理
    #处理后list0里存放的就是单个的字
    list0=[]      
    for word in txt:
        list0.append(word)
    
    #---开始时间---
    end0=time.time()
    #-----分别处理一元，二元，三元分词----- 
    list1=unigram(txt,list0)
    write_txt(path2_1,list1)
    
    end1=time.time()
    print("一元分词运行时间为"+str(end1-end0)+"s\n")  
    
    list2=bigram(txt,list0)
    write_txt(path2_2,list2)
    
    end2=time.time()
    print("二元分词运行时间为"+str(end2-end1)+"s\n")   
    
    list3=trigram(txt,list0)
    write_txt(path2_3,list3)
    
    end3=time.time()
    print("三元分词运行时间为"+str(end3-end2)+"s\n")
    
    #-----结束时间-----
    end=time.time()
    print("整个程序运行时间为"+str(end-start)+"s\n")
    



if __name__=="__main__":
    main()
