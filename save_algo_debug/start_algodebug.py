# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2021 ifm electronic gmbh, CSR
#
# THE PROGRAM IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND.
#

from ifmO3r.ifm3dTiny.utils.recorder import record as ad_record
from ifmO3r.ifm3dTiny import Device
import argparse
import logging

status_logger = logging.getLogger(__name__)


def configure_head(ip, port, conf):
    dev = Device(ip=ip, port=port)
    try:
        dev.config_from_json_file(conf)
    except Exception as e:
        status_logger.error(e)
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="ip address of VPU", default="192.168.0.69")
    parser.add_argument("--timeout", help="timeout to be used in the get function", default=3.0, type=float)
    parser.add_argument("--numSeconds", help="number of seconds to be recorded (default: record until CTRL-C)",
                        default=None, type=int)
    parser.add_argument("--loglevel", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    parser.add_argument("--filename",
                        help="target filename. If not given, a file will be created in the current directory.",
                        default=None)
    parser.add_argument("--portIndices", help="VPU ports to be recorded.", default=[2], nargs="*")
    parser.add_argument("--conf", help="head configuration via json file, default is config.json in the cwd",
                        default=None, type=str)
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    port3D = []
    port2D = []
    if args.conf is not None:
        for cid in args.portIndices:
            if 0 <= int(cid) <= 1:
                port2D.append(int(50020 + int(cid)))
            if 2 <= int(cid) <= 5:
                port3D.append(int(50010 + int(cid)))

    if port3D:
        for port in port3D:
            if configure_head(ip=args.ip, port=port, conf=args.conf):
                status_logger.info("imager successfully configured at port: {port} with json-config: {conf}".format(
                    port=port3D, conf=args.conf))
            else:
                status_logger.info("imager  configuration at port: {port} with json-config: {conf} failed".format(
                    port=port3D, conf=args.conf))

    try:
        ad_record(ip=args.ip, timeout=args.timeout, numberOfSeconds=args.numSeconds, filename=args.filename, cameras=[int(cid) for cid in args.portIndices], )
    except Exception as e:
        status_logger.error(e)


if __name__ == "__main__":
    main()

