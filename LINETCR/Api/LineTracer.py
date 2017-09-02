# -*- coding: utf-8 -*-

from .LineClient import LineClient
from types import *
from ..lib.curve.ttypes import OpType
from ..Net.LineServer import url


class LineTracer(object):
    OpInterrupt = {}
    client = None

    def __init__(self, client):
        if type(client) is not LineClient:
            raise Exception(
                "You need to set LineClient instance to initialize LineTracer")

        self.client = client
        self.client.endPoint(url.LONG_POLLING)

    def addOpInterruptWithDict(self, OpInterruptDict):
        """To add Operation with Callback function {Optype.NOTIFIED_INTO_GROUP: func}"""
        self.OpInterrupt.update(OpInterruptDict)

    def addOpInterrupt(self, OperationType, DisposeFunc):
        self.OpInterrupt[OperationType] = DisposeFunc

    def execute(self):
        try:
            operations = self.client.fetchOperation(self.client.revision, 10)
            #print "======================================================="
            # print operations
            #print "======================================================="
        except EOFError:
            return
        except KeyboardInterrupt:
            exit()
        except:
            return

        for op in operations:
            if op.type in self.OpInterrupt.keys():
                #print "======================================================="
                #print str(op.type) + "[" + str(op) + "]"
                #print "======================================================="
                self.OpInterrupt[op.type](op)

            self.client.revision = max(op.revision, self.client.revision)
