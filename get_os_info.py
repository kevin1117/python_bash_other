# coding=utf-8

from collections import OrderedDict
from collections import namedtuple
import os
import glob
import re

def cpuinfo():

    cpuinfo=OrderedDict()
    procinfo=OrderedDict()

    nprocs = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():

                cpuinfo['proc%s' % nprocs] = procinfo
                nprocs=nprocs+1

                procinfo=OrderedDict()
            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''

    return cpuinfo

def meminfo():

    meminfo=OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo


def netdevs():

    with open('/proc/net/dev') as f:
        net_dump = f.readlines()

    device_data={}
    data = namedtuple('data',['rx','tx'])
    for line in net_dump[2:]:
        line = line.split(':')
        if line[0].strip() != 'lo':
            device_data[line[0].strip()] = data(float(line[1].split()[0])/(1024.0*1024.0),
                                                float(line[1].split()[8])/(1024.0*1024.0))

    return device_data

def process_list():

    pids = []
    for subdir in os.listdir('/proc'):
        if subdir.isdigit():
            pids.append(subdir)

    return pids


dev_pattern = ['sd.*','xv*']

def size(device):
    nr_sectors = open(device+'/size').read().rstrip('\n')
    sect_size = open(device+'/queue/hw_sector_size').read().rstrip('\n')

    return (float(nr_sectors)*float(sect_size))/(1024.0*1024.0*1024.0)

def detect_devs():
    for device in glob.glob('/sys/block/*'):
        for pattern in dev_pattern:
            if re.compile(pattern).match(os.path.basename(device)):
                print('Device:: {0}, Size:: {1} GiB'.format(device, size(device)))


if __name__=='__main__':
    cpuinfo = cpuinfo()
    for processor in cpuinfo.keys():
        print(cpuinfo[processor]['model name'])

    meminfo = meminfo()
    print('Total memory: {0}'.format(meminfo['MemTotal']))
    print('Free memory: {0}'.format(meminfo['MemFree']))

    netdevs = netdevs()
    for dev in netdevs.keys():
        print('{0}: {1} MiB {2} MiB'.format(dev, netdevs[dev].rx, netdevs[dev].tx))


    pids = process_list()
    print('Total number of running processes:: {0}'.format(len(pids)))


    detect_devs()