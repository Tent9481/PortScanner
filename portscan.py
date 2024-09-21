#!/usr/bin/python

from socket import *
import optparse
from threading import *
from termcolor import colored


def connScan(tgthost,tgtport):
        try:
                sock=socket(AF_INET,SOCK_STREAM)
                sock.connect((tgthost,tgtport))
                print(colored('[+] %d/port open' %tgtport,'green'))
        except:
                print(colored('[+] %d/port closed' % tgtport,'red'))
        finally:
                sock.close()

def portscan(tgthost,tgtports):
        try:
                tgtIP=gethostbyname(tgthost)
        except:
                print('Unknown Host %s' %tgthost)
        try: 
                tgtname=gethostbyaddr(tgtIp)
                print('[+] Scan Results for: ' + tgtname[0])
        except:
                print('[+] Scan Results for : ' + tgtIP)
        for tgtport in tgtports:
                t=Thread(target=connScan,args=(tgthost,tgtport))
                t.start()

def main():
        parser=optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target part>')
        parser.add_option('-H', dest='tgthost',type='string',help='Specify target host')
        parser.add_option('-P', dest='tgtport',type='int',help='Specify range of target ports')
        (options,args)=parser.parse_args()
        tgthost=options.tgthost
        tgtports=int(options.tgtport or 0)
        tgtport=[]
        for i in range(1,tgtports):
                tgtport.append(i)
        if(tgthost==None) or (tgtport[0]==None):
                print(parser.usage)
                exit(0)
        portscan(tgthost,tgtport)


if __name__ == '__main__':

        main()
