#!/usr/bin/python
import logging
import sys

blivet_log = logging.getLogger("blivet")

def set_up_logging():
    """ Configure the blivet logger to use /tmp/blivet.log as its log file. """
    blivet_log.setLevel(logging.DEBUG)
    program_log = logging.getLogger("program")
    program_log.setLevel(logging.DEBUG)
    handler = logging.FileHandler("/tmp/blivet.log")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s,%(msecs)03d %(levelname)s %(name)s: %(message)s")
    handler.setFormatter(formatter)
    blivet_log.addHandler(handler)
    program_log.addHandler(handler)

virt_set_up_logging()
instert at line 20
import blivet
b=blivet.Blivet()
b.reset()

sdc=b.devicetree.getDeviceByName("sdc")
sdd=b.devicetree.getDeviceByName("sdd")
disks=[sdc,sdd]

for i in disks:
  b.recursiveRemove(i)

add by branch twuVirt
for i in disks:
  b.initializeDisk(i)

factory = blivet.devicefactory.LVMFactory(b, 550, disks, mountpoint = "/l1", fstype="ext4", name="rt", container_name="zkvm0001")
factory.configure()

b.doIt()
add by branch twuVirt
