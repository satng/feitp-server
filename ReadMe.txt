
Notice,it's just for linux System only.

1.Python  2.6<= verison <= 2.7
because this server need multiprocess supported and pyftpdlib supported

More in detail
http://docs.python.org/library/multiprocessing.html     >2.6
http://code.google.com/p/pyftpdlib/                      2.4~2.7


2.Install 
$unzip pyftpdlib-0.6.0-By-Fei
$cd pyftpdlib-0.6.0-By-Fei
$python setup.py install

3.Run
You need config your FTP ,PORT,USER,PWD,DIR in FEITP-SERVER
Best high-Preformance user CPU Number * 2 for process

python FEITP-SERVER.py

###upload file in /REV dir###

4.DIY your logic
If you overwrite YourHandler Class, there are a lot of your logic you can do 

class YourHandler(ftpserver.FTPHandler):
    def on_login(self, username):
        # do something when user login
        pass

    def on_logout(self, username):
        # do something when user logs out
        pass
        
    def on_file_sent(self, file):
        # do something when a file has been sent
        pass

    def on_file_received(self, file):
        # do something when a file has been received
        pass
            
    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        pass

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        import os
        os.remove(file)
		
5.Hope could you like it
Link: wu.qunfei@gmail.com