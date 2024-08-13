from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
import time

FTP_PORT = 2121

#Formato para ruta en linux

FTP_USER1 = 'lpr'
FTP_PASSWORD1 = 'lpr.3659'
FTP_DIRECTORY1 = '/home/victor/ftp'

#Formato para ruta en windows

#FTP_USER2 = 'lpr_garaxe'
#FTP_PASSWORD2 = 'lpr.3659'
#FTP_DIRECTORY2 = 'C:/2'


class MyHandler(FTPHandler):

    def on_connect(self):
        print ("%s:%s connected" % (self.remote_ip, self.remote_port))

    def on_disconnect(self):
        # do something when client disconnects
        pass

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


def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER1, FTP_PASSWORD1, FTP_DIRECTORY1, perm='elradfmwMT')
    #authorizer.add_user(FTP_USER2, FTP_PASSWORD2, FTP_DIRECTORY2, perm='elradfmwMT')

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = 'Servidor FTP Listo'
    handler.passive_ports = range(60000, 65535)

    address = ('0.0.0.0', FTP_PORT)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()
    
    
if __name__ == "__main__":
    main()