#!/usr/bin/env python3
# Qualcomm Sahara / Firehose Client (c) B.Kerler 2018-2020.
# Licensed under MIT License
"""
Usage:
    edl.py -h | --help
    edl.py [--vid=vid] [--pid=pid]
    edl.py [--loader=filename] [--memory=memtype]
    edl.py [--debugmode]
    edl.py [--gpt-num-part-entries=number] [--gpt-part-entry-size=number] [--gpt-part-entry-start-lba=number]
    edl.py [--memory=memtype] [--skipstorageinit] [--maxpayload=bytes] [--sectorsize==bytes]
    edl.py server [--tcpport=portnumber] [--loader=filename] [--debugmode] [--skipresponse] [--vid=vid] [--pid=pid] [--devicemodel=value]
    edl.py memorydump [--debugmode] [--vid=vid] [--pid=pid]
    edl.py printgpt [--memory=memtype] [--lun=lun] [--sectorsize==bytes] [--loader=filename] [--debugmode]  [--skipresponse] [--vid=vid] [--pid=pid]
    edl.py gpt <directory> [--memory=memtype] [--lun=lun] [--genxml] [--loader=filename]  [--skipresponse] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py r <partitionname> <filename> [--memory=memtype] [--sectorsize==bytes] [--lun=lun] [--loader=filename]  [--skipresponse] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py rl <directory> [--memory=memtype] [--lun=lun] [--sectorsize==bytes] [--skip=partnames] [--genxml]  [--skipresponse] [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py rf <filename> [--memory=memtype] [--lun=lun] [--sectorsize==bytes] [--loader=filename] [--debugmode]  [--skipresponse] [--vid=vid] [--pid=pid]
    edl.py rs <start_sector> <sectors> <filename> [--lun=lun] [--sectorsize==bytes] [--loader=filename] [--debugmode] [--skipresponse] [--vid=vid] [--pid=pid]
    edl.py w <partitionname> <filename> [--memory=memtype] [--lun=lun] [--sectorsize==bytes] [--skipwrite] [--skipresponse] [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid] [--devicemodel=value]
    edl.py wl <directory> [--memory=memtype] [--lun=lun] [--sectorsize==bytes] [--skip=partnames] [--skipresponse] [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid] [--devicemodel=value]
    edl.py wf <filename> [--memory=memtype] [--lun=lun] [--sectorsize==bytes] [--loader=filename] [--skipresponse] [--debugmode] [--vid=vid] [--pid=pid] [--devicemodel=value]
    edl.py ws <start_sector> <filename> [--memory=memtype] [--lun=lun] [--sectorsize==bytes] [--skipwrite] [--skipresponse] [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid] [--devicemodel=value]
    edl.py e <partitionname> [--memory=memtype] [--skipwrite] [--lun=lun] [--sectorsize==bytes] [--loader=filename] [--debugmode] [--skipresponse] [--vid=vid] [--pid=pid] [--devicemodel=value]
    edl.py es <start_sector> <sectors> [--memory=memtype] [--lun=lun] [--sectorsize==bytes] [--skipwrite] [--loader=filename] [--skipresponse] [--debugmode] [--vid=vid] [--pid=pid] [--devicemodel=value]
    edl.py ep <partitionname> <sectors> [--memory=memtype] [--skipwrite] [--lun=lun] [--sectorsize==bytes] [--loader=filename] [--debugmode] [--skipresponse] [--vid=vid] [--pid=pid] [--devicemodel=value]
    edl.py footer <filename> [--memory=memtype] [--lun=lun] [--loader=filename] [--debugmode] [--skipresponse] [--vid=vid] [--pid=pid]
    edl.py peek <offset> <length> <filename> [--loader=filename] [--debugmode] [--skipresponse] [--vid=vid] [--pid=pid]
    edl.py peekhex <offset> <length> [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py peekdword <offset> [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py peekqword <offset> [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py memtbl <filename> [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py poke <offset> <filename> [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py pokehex <offset> <data> [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py pokedword <offset> <data> [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py pokeqword <offset> <data> [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py memcpy <offset> <size> [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py secureboot [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py pbl <filename> [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py qfp <filename> [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py getstorageinfo [--loader=filename] [--memory=memtype] [--debugmode] [--skipresponse] [--vid=vid] [--pid=pid]
    edl.py setbootablestoragedrive <lun> [--loader=filename] [--debugmode] [--skipresponse] [--vid=vid] [--pid=pid]
    edl.py send <command> [--loader=filename] [--debugmode] [--skipresponse] [--vid=vid] [--pid=pid]
    edl.py xml <xmlfile> [--loader=filename] [--debugmode] [--skipresponse] [--vid=vid] [--pid=pid] [--devicemodel=value]
    edl.py rawxml <xmlstring> [--loader=filename] [--debugmode] [--skipresponse] [--vid=vid] [--pid=pid] [--devicemodel=value]
    edl.py reset [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py nop [--loader=filename] [--debugmode] [--vid=vid] [--pid=pid]
    edl.py modules <command> <options> [--memory=memtype] [--lun=lun] [--loader=filename] [--debugmode] [--skipresponse] [--vid=vid] [--pid=pid] [--devicemodel=value]
    edl.py qfil <rawprogram> <patch> <imagedir>

Description:
    server [--tcpport=portnumber]                                                # Run tcp/ip server
    printgpt [--memory=memtype] [--lun=lun]                                      # Print GPT Table information
    gpt <directory> [--memory=memtype] [--lun=lun]                               # Save gpt table to given directory
    r <partitionname> <filename> [--memory=memtype] [--lun=lun]                  # Read flash to filename
    rl <directory> [--memory=memtype] [--lun=lun] [--skip=partname]              # Read all partitions from flash to a directory
    rf <filename> [--memory=memtype] [--lun=lun]                                 # Read whole flash to file
    rs <start_sector> <sectors> <filename> [--lun=lun]                           # Read sectors starting at start_sector to filename
    w <partitionname> <filename> [--memory=memtype] [--lun=lun] [--skipwrite]    # Write filename to partition to flash
    wl <directory> [--memory=memtype] [--lun=lun]                                # Write all files from directory to flash
    wf <filename> [--memory=memtype] [--lun=lun]                                 # Write whole filename to flash
    ws <start_sector> <filename> [--memory=memtype] [--lun=lun] [--skipwrite]    # Write filename to flash at start_sector
    e <partitionname> [--memory=memtype] [--skipwrite] [--lun=lun]               # Erase partition from flash
    es <start_sector> <sectors> [--memory=memtype] [--lun=lun] [--skipwrite]     # Erase sectors at start_sector from flash
    ep <partitionname> <sectors> [--memory=memtype] [--skipwrite] [--lun=lun]    # Erase sector count from flash partition
    footer <filename> [--memory=memtype] [--lun=lun]                             # Read crypto footer from flash
    peek <offset> <length> <filename>                                            # Dump memory at offset with given length to filename
    peekhex <offset> <length>                                                    # Dump memory at offset and given length as hex string
    peekdword <offset>                                                           # Dump DWORD at memory offset
    peekqword <offset>                                                           # Dump QWORD at memory offset
    memtbl <filename>                                                            # Dump memory table to file
    poke <offset> <filename>                                                     # Write filename to memory at offset to memory
    pokehex <offset> <data>                                                      # Write hex string data at offset to memory
    pokedword <offset> <data>                                                    # Write DWORD to memory at offset
    pokeqword <offset> <data>                                                    # Write QWORD to memory at offset
    memcpy <offset> <size>                                                       # Copy memory from srcoffset with given size to dstoffset
    secureboot                                                                   # Print secureboot fields from qfprom fuses
    pbl <filename>                                                               # Dump primary bootloader to filename
    qfp <filename>                                                               # Dump QFPROM fuses to filename
    getstorageinfo                                                               # Print storage info in firehose mode
    setbootablestoragedrive <lun>                                                # Change bootable storage drive to lun number
    send <command>                                                               # Send firehose command
    xml <xmlfile>                                                                # Send firehose xml file
    rawxml <xmlstring>                                                           # Send firehose xml raw string
    reset                                                                        # Send firehose reset command
    nop                                                                          # Send firehose nop command
    modules <command> <options>                                                  # Enable submodules, for example: "oemunlock enable"
    qfil <rawprogram> <patch> <imagedir>                                         # Write rawprogram xml files
                                                                                 # <rawprogram> : program config xml, such as rawprogram_unsparse.xml or rawprogram*.xml
                                                                                 # <patch> : patch config xml, such as patch0.xml or patch*.xml
                                                                                 # <imagedir> : directory name of image files

Options:
    --loader=filename                  Use specific EDL loader, disable autodetection [default: None]
    --vid=vid                          Set usb vendor id used for EDL [default: -1]
    --pid=pid                          Set usb product id used for EDL [default: -1]
    --lun=lun                          Set lun to read/write from (UFS memory only) [default: None]
    --maxpayload=bytes                 Set the maximum payload for EDL [default: 0x100000]
    --sectorsize=bytes                 Set default sector size [default: 0x200]
    --memory=memtype                   Set memory type ("NAND", "eMMC", "UFS", "spinor")
    --skipwrite                        Do not allow any writes to flash (simulate only)
    --skipresponse                     Do not expect a response from phone on read/write (some Qualcomms)
    --skipstorageinit                  Skip storage initialisation
    --debugmode                        Enable verbose mode
    --gpt-num-part-entries=number      Set GPT entry count [default: 0]
    --gpt-part-entry-size=number       Set GPT entry size [default: 0]
    --gpt-part-entry-start-lba=number  Set GPT entry start lba sector [default: 0]
    --tcpport=portnumber               Set port for tcp server [default: 1340]
    --skip=partnames                   Skip reading partition with names "partname1,partname2,etc."
    --genxml                           Generate rawprogram[lun].xml
    --devicemodel=value                Set device model [default: ""]
"""

import os
import sys
import time
import logging
from docopt import docopt

args = docopt(__doc__, version='3')

default_ids = [
    [0x05c6,0x9008,-1],
    [0x05c6,0x900e,-1] ,
    [0x05c6,0x9025,-1],
    [0x1199,0x9062,-1],
    [0x1199,0x9070,-1],
    [0x1199,0x9090,-1],
    [0x0846,0x68e0,-1],
    [0x19d2,0x0076,-1]
]

from Library.utils import LogBase
from Library.usblib import usb_class
from Library.sahara import sahara
from Library.streaming_client import streaming_client
from Library.firehose_client import firehose_client
from Library.streaming import Streaming

print("Qualcomm Sahara / Firehose Client V3.2 (c) B.Kerler 2018-2021.")

class main(metaclass=LogBase):
    def doconnect(self,cdc, loop, mode, resp, sahara):
        while not cdc.connected:
            cdc.connected = cdc.connect()
            if not cdc.connected:
                sys.stdout.write('.')
                if loop >= 20:
                    sys.stdout.write('\n')
                    loop = 0
                loop += 1
                time.sleep(1)
                sys.stdout.flush()
            else:
                self.__logger.info("Device detected :)")
                try:
                    mode, resp = sahara.connect()
                    if mode == "" or resp == -1:
                        mode, resp = sahara.connect()
                except Exception as e:
                    if mode == "" or resp == -1:
                        mode, resp = sahara.connect()
                if mode == "":
                    self.__logger.info("Unknown mode. Aborting.")
                    cdc.close()
                    sys.exit()
                self.__logger.info(f"Mode detected: {mode}")
                break

        return mode, resp

    def exit(self,cdc):
        cdc.close()
        sys.exit()

    def parse_option(self,args):
        options={}
        for arg in args:
            if "--" in arg or "<" in arg:
                options[arg]=args[arg]
        return options

    def parse_cmd(self,args):
        cmd=""
        if args["server"]:
            cmd = "server"
        elif args["printgpt"]:
            cmd = "printgpt"
        elif args["gpt"]:
            cmd = "gpt"
        elif args["r"]:
            cmd = "r"
        elif args["rl"]:
            cmd = "rl"
        elif args["rf"]:
            cmd = "rf"
        elif args["rs"]:
            cmd = "rs"
        elif args["w"]:
            cmd = "w"
        elif args["wl"]:
            cmd = "wl"
        elif args["wf"]:
            cmd = "wf"
        elif args["ws"]:
            cmd = "ws"
        elif args["e"]:
            cmd = "e"
        elif args["es"]:
            cmd = "es"
        elif args["ep"]:
            cmd = "ep"
        elif args["footer"]:
            cmd = "footer"
        elif args["peek"]:
            cmd = "peek"
        elif args["peekhex"]:
            cmd = "peekhex"
        elif args["peekdword"]:
            cmd = "peekdword"
        elif args["peekqword"]:
            cmd = "peekqword"
        elif args["memtbl"]:
            cmd = "memtbl"
        elif args["poke"]:
            cmd = "poke"
        elif args["pokehex"]:
            cmd = "pokehex"
        elif args["pokedword"]:
            cmd = "pokedword"
        elif args["pokeqword"]:
            cmd = "pokeqword"
        elif args["memcpy"]:
            cmd = "memcpy"
        elif args["secureboot"]:
            cmd = "secureboot"
        elif args["pbl"]:
            cmd = "pbl"
        elif args["qfp"]:
            cmd = "qfp"
        elif args["getstorageinfo"]:
            cmd = "getstorageinfo"
        elif args["setbootablestoragedrive"]:
            cmd = "setbootablestoragedrive"
        elif args["send"]:
            cmd = "send"
        elif args["xml"]:
            cmd = "xml"
        elif args["rawxml"]:
            cmd = "rawxml"
        elif args["reset"]:
            cmd = "reset"
        elif args["nop"]:
            cmd = "nop"
        elif args["modules"]:
            cmd = "modules"
        elif args["memorydump"]:
            cmd = "memorydump"
        elif args["qfil"]:
            cmd = "qfil"
        return cmd

    def run(self):
        mode = ""
        loop = 0
        vid = int(args["--vid"], 16)
        pid = int(args["--pid"], 16)
        interface = -1
        if vid!=-1 and pid!=-1:
            portconfig = [[vid, pid, interface]]
        else:
            portconfig = default_ids
        if args["--debugmode"]:
            logfilename = "log.txt"
            if os.path.exists(logfilename):
                os.remove(logfilename)
            fh = logging.FileHandler(logfilename)
            self.__logger.addHandler(fh)
            self.__logger.setLevel(logging.DEBUG)
        else:
            self.__logger.setLevel(logging.INFO)

        cdc = usb_class(portconfig=portconfig,loglevel=self.__logger.level)
        saharahdl = sahara(cdc,loglevel=self.__logger.level)

        if args["--loader"] == 'None':
            self.__logger.info("Trying with no loader given ...")
            saharahdl.programmer = ""
        else:
            loader = args["--loader"]
            self.__logger.info(f"Using loader {loader} ...")
            saharahdl.programmer = loader

        self.__logger.info("Waiting for the device")
        resp = None
        cdc.timeout = 100
        mode, resp = self.doconnect(cdc, loop, mode, resp, saharahdl)
        if resp == -1:
            mode, resp = self.doconnect(cdc, loop, mode, resp, saharahdl)
            if resp == -1:
                self.__logger.error("USB desync, please rerun command !")
                sys.exit()
        # print((mode, resp))
        if mode == "sahara":
            if resp==None:
                if mode=="sahara":
                    print("Sahara in error state, resetting ...")
                    saharahdl.cmd_reset()
                    sys.exit(cdc)
            elif "mode" in resp:
                mode = resp["mode"]
                if mode == saharahdl.sahara_mode.SAHARA_MODE_MEMORY_DEBUG:
                    if args["memorydump"]:
                        time.sleep(0.5)
                        print("Device is in memory dump mode, dumping memory")
                        saharahdl.debug_mode()
                        sys.exit(cdc)
                    else:
                        print("Device is in streaming mode, uploading loader")
                        cdc.timeout = None
                        sahara_info = saharahdl.streaminginfo()
                        if sahara_info:
                            mode, resp = saharahdl.connect()
                            if mode == "sahara":
                                mode = saharahdl.upload_loader()
                                if "enprg" in saharahdl.programmer.lower():
                                    mode = "load_enandprg"
                                elif "nprg" in saharahdl.programmer.lower():
                                    mode = "load_nandprg"
                                elif mode!="":
                                    mode = "load_" + mode
                                if "load_" in mode:
                                    time.sleep(0.3)
                                else:
                                    print("Error, couldn't find suitable enprg/nprg loader :(")
                                    sys.exit(cdc)
                else:
                    print("Device is in EDL mode .. continuing.")
                    cdc.timeout = None
                    sahara_info = saharahdl.info()
                    if sahara_info:
                        mode, resp = saharahdl.connect()
                        if mode == "sahara":
                            mode = saharahdl.upload_loader()
                            if mode == "firehose":
                                if "enprg" in saharahdl.programmer.lower():
                                    mode = "enandprg"
                                elif "nprg" in saharahdl.programmer.lower():
                                    mode = "nandprg"
                            if mode != "":
                                if mode != "firehose":
                                    streaming = Streaming(cdc, saharahdl, self.__logger.level)
                                    if streaming.connect(1):
                                        print("Successfully uploaded programmer :)")
                                        mode = "nandprg"
                                    else:
                                        print("Device is in an unknown state")
                                        sys.exit(cdc)
                                else:
                                    print("Successfully uploaded programmer :)")
                            else:
                                print("No suitable loader found :(")
                                sys.exit(cdc)
                    else:
                        print("Device is in an unknown sahara state")
                        print("resp={0}".format(resp))
                        sys.exit(cdc)
            else:
                print("Device is in an unknown state")
                sys.exit(cdc)
        else:
            saharahdl.bit64 = True

        if mode == "firehose":
            cdc.timeout = None
            fh = firehose_client(args, cdc, saharahdl, self.__logger.level,print)
            cmd=self.parse_cmd(args)
            options=self.parse_option(args)
            if cmd!="":
                fh.handle_firehose(cmd,options)
        elif mode == "nandprg" or mode == "enandprg" or mode == "load_nandprg" or mode == "load_enandprg":
            sc = streaming_client(args, cdc, saharahdl, self.__logger.level,print)
            cmd = self.parse_cmd(args)
            options = self.parse_option(args)
            if "load_" in mode:
                options["<mode>"] = 1
            else:
                options["<mode>"] = 0
            sc.handle_streaming(cmd, options)
        else:
            self.__logger.error("Sorry, couldn't talk to Sahara, please reboot the device !")

        sys.exit(cdc)


if __name__ == '__main__':
    base=main()
    base.run()
