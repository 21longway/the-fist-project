# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:44:45 2021

@author: 82420
"""
import os

filename='student.txt'

def main():
    while True:
        menu()
        choice=int(input('请选择'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定退出系统嘛？y/n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用')
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()
            

def menu():
    print('--------------学生信息管理系统---------------')
    print('-----------------功能菜单--------------------')
    print('\t 1.录入学生信息')
    print('\t 2.查找学生信息')
    print('\t 3.删除学生信息')
    print('\t 4.修改学生信息')
    print('\t 5.排序')
    print('\t 6.统计学生总人数')
    print('\t 7.显示所有学生信息')
    print('\t 0.退出')
    print('-------------------------------------------')
    
    
def insert():
    student_list=[]
    while True:
        id = input('请输入学生的ID(如1001)：')
        if not id:      #如果id为空
            break
        name = input('请输入学生的姓名：')
        if not name:    #如果name为空
            break
        
        try:
            english=int(input('请输入学生的english成绩：'))
            python=int(input('请输入学生的python成绩：'))
            java=int(input('请输入学生的java成绩：'))
        except:
            print('输入无效，请重新输入')
            continue
#将入录的学生信息保存在字典中
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
#将学生信息添加到列表中
        student_list.append(student)
        answer=input('是否继续输入？y/n \n')
        if answer=='y':
            continue
        else:
            break
    # 调用save函数
    save(student_list)
    print('学生信息入录完毕')
    
    
def save(lst):
    try:
        student_txt=open(filename,'a',encoding='utf-8')  #当以a模式打开时，只能写文件，而且是在文件末尾添加内容。
    except:
        student_txt=open(filename,'w',encoding='utf-8')  #当以w模式打开时，只能写文件，而且会直接将之前的数据给丢失。
    for item in lst:
        student_txt.write(str(item)+'\n')
    student_txt.close()
        
                
def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode = input('按id查找请输入1，按姓名查找请输入2')
            if mode == '1':
                id=input('请输入学生id：')
            elif mode =='2':
                name = input('请输入学生姓名：')
            else:
                print('您的输入有误，请重新输入')
                search()
            with open(filename,'r',encoding='utf-8')as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            student_query.append(d)
                    elif name!='':
                        if d['name']==name:
                            student_query.append(d)
            #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer=input('是否继续查询？y/n\n')
            if answer=='y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息')
            return
        
        
def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息，无数据显示')
        return
    #定义标题显示格式
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','python成绩','java成绩','总成绩'))
    #定义内容的显示格式
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int(item.get('java'))+int(item.get('python'))
                                 ))
                            
            
def delete():
    while True:
        student_id=input('请输入要删除的学生ID：')
        if student_id !='':
            if os.path.exists(filename):   #在系统中判断‘filename’文件是否存在
                with open(filename,'r',encoding='utf-8') as file:  #以只读方式打开文件
                    student_old=file.readlines()
            else:
                student_old=[]
                
        flag=False  #标记是否删除
        if student_old:
            with open(filename,'w',encoding='utf-8') as wfile:
                d={}
                for item in student_old:
                    d=dict(eval(item))  #将字符串转成字典
                    if d['id'] != student_id:
                        wfile.write(str(d)+'\n')
                    else:
                        flag = True
                if flag:
                    print(f'id为{student_id}的学生已被删除')  #f-string 格式化字符串常量
                else:
                    print(f'没有找到id为{student_id}的学生信息')
        else:
            print('无学生信息')
            break
        show()
        
        answer=input('是否继续删除？y/n\n')
        if answer=='y':
            continue
        else:
            break
            
            
def modify():
    show()
    if os.path.exists(filename):
         with open(filename,'r',encoding='utf-8') as rfile:
             student_old=rfile.readlines()
    else:
        return
    student_id=input('请输入学生的id:')
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息，可以修改')
                while True:
                    try:
                         d['name'] = input('输入学生姓名：')
                         d['english'] = input('输入学生english成绩：')
                         d['python'] = input('输入学生python成绩：')
                         d['java'] = input('输入学生java成绩：')
                    except:
                        print('输入错误，请重新输入')
                    else:
                        break
                    
                wfile.write(str(d)+'\n')
                print('修改成功')
            else:
                wfile.write(str(d)+'\n')
                
        answer=input('是否继续修改？y/n  \n')
        if answer=='y':
            modify()
        
        
def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_list=rfile.readlines()
        student_new=[]
        for item in student_list:
            d=dict(eval(item))
            student_new.append(d)     
    else:
        return
    
    asc_or_desc=input('请选择（0.升序 1.降序）：')
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode=input('请选择排序方式（1.按英语成绩 2.按python成绩 3.按java成绩 0.按总成绩）：')
    if mode=='1':
        student_new.sort(key=lambda x:int(x['english']),reverse=asc_or_desc_bool)
    elif mode=='2':
        student_new.sort(key=lambda x:int(x['python']),reverse=asc_or_desc_bool)
    elif mode=='3':
        student_new.sort(key=lambda x:int(x['java']),reverse=asc_or_desc_bool)
    elif mode=='0':
        student_new.sort(key=lambda x:int(x['english'])+int(x['python'])+int(x['java']),reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入！！！')
        sort()
    show_student(student_new)
    
           
def total():
    if os.path.exists(filename):
        with open (filename,'r',encoding='utf-8')as rfile:
            students=rfile.readlines()
            if students:
                print('一共有{}名学生。'.format(len(students)))
            else:
                
                print('还没有录入学生的信息')
    else:
        print('暂未保存数据信息')
        
        
        
        
def show():
    student_lst=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('暂未保存过数据')



if __name__=='__main__':
    main()
