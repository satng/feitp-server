import os
import sys

from multiprocessing import Process, current_process, freeze_support
import multiprocessing
from pyftpdlib import ftpserver


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




def note(format, *args):
    sys.stderr.write('[%s]\t%s\n' % (current_process().name, format%args))


def serve_forever(server):
    note('starting server')
    try:
        server.serve_forever()
    # Start a multi-threading ftpServer in 1 Process
    except KeyboardInterrupt:
        pass


def runpool(number_of_processes):
    # create a single server object -- children will each inherit a copy
    authorizer = ftpserver.DummyAuthorizer()
    authorizer.add_user('user', password="123456", homedir=os.getcwd() + "/REV", perm='elradfmw')
    # handler = YourHandler
    # If we use our logic
    handler = ftpserver.FTPHandler
    handler.tcp_no_delay = True
    handler.authorizer = authorizer
    address = ('192.168.203.167', 21)
    server = ftpserver.FTPServer(address, handler)

    # create child processes to act as workers
    for i in range(number_of_processes-1):
        Process(target=serve_forever, args=(server,)).start()

    # main process also acts as a worker
    serve_forever(server)


def main():

    NUMBER_OF_PROCESSES = multiprocessing.cpu_count()
    # Got the Server CPU number at Process Number
    print "number of CPU is %d" % NUMBER_OF_PROCESSES
    runpool(NUMBER_OF_PROCESSES)


if __name__ == '__main__':
    freeze_support()
    main()
    # this is a multi-process ftp Server which every process in every CPU
    # this is a multi-threading ftp Server which every process has many threading for a huge number of client
    # design by Qunfei wu in Shanghai
