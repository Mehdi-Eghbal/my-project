def add(name,number):
        c=open("E:\phone book.txt","r")
        phonebookname=[]
        for i in c:
                b=i.split()
                phonebookname.append(b[0])
        if phonebookname.count(name)==0:
                a=open("E:\phone book.txt","a")
                a.write(name+'     '+str(number)+'\n')
                a.close()
                print(name,' with ',number,' is register to phone book')
        else:
                print(name,' is alredy registered in phone book')
def call(name):
        from time import time
        phonebooknumber=[]
        phonebookname=[]
        a=open("E:\phone book.txt","r")
        for i in a:
                b=i.split()
                phonebookname.append(b[0])
                phonebooknumber.append(b[1])
        if phonebookname.count(name)==0:
                print('there is no',name,'in phone book')
        else:
                t=time()
                print('calling ...')
                input('please Enter to end of calling !!!')
                t=time()-t
                print('duratin of your call to ',name,' =',t,'s')
                b=open("E:\call log.txt","a")
                b.write('duration calling to '+name+' is '+str(t)+'s'+'\n')
                b.close()
call('ali')