#!/usr/bin/env python
import os
from common.entities import pcapFile
from canari.maltego.message import UIMessage
from canari.framework import configure #, superuser

__author__ = 'catalyst256'
__copyright__ = 'Copyright 2014, sniffmypacketsv2 Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'catalyst256'
__email__ = 'catalyst256@gmail.com'
__status__ = 'Development'

__all__ = [
    'dotransform'
]

#@superuser
@configure(
    label='Open Wireshark',
    description='Open pcap file with Wireshark',
    uuids=[ 'sniffmypacketsv2.v2.open_pcap_wshark' ],
    inputs=[ ( '[SmP] - PCAP', pcapFile ) ],
    debug=True
)
def dotransform(request, response, config):
  pcap = request.value
  cmd = 'wireshark ' + pcap
  os.system(cmd)
  return response + UIMessage('Wireshark has closed!')

