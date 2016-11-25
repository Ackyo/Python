#!/usr/bin/env python

import os
import sys

def execute_shell_cmd(cmd, ret_result = False):
    if ret_result:
        fd = os.popen(cmd)
        ret = fd.read()
        fd.close()
        return ret
    else:
        ret = os.system(cmd)
        if ret != 0:
            print 'failed cmd: ', cmd
            print 'return code is ', ret
            sys.exit(1)
