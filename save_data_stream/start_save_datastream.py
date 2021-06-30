# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2021 ifm electronic gmbh, CSR
#
# THE PROGRAM IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND.

from ifmO3r.ifm3dTiny import ImageLogger, FrameGrabber, ImageBuffer, Device
import argparse
import logging

status_logger = logging.getLogger(__name__)


def configure_head(device, conf):
    try:
        device.config_from_json_file(conf)
    except Exception as e:
        status_logger.error(e)
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="ip address of VPU", default="192.168.0.69")
    parser.add_argument("--timeout", help="timeout to be used in the get function", default=3.0, type=float)
    parser.add_argument("--numSeconds", help="number of seconds to be recorded ", default=5, type=int)
    parser.add_argument("--loglevel", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    parser.add_argument("--filename",
                        help="target filename. If not given, a file will be created in the current directory.",
                        default=None)
    parser.add_argument("--portIndices", help="VPU ports to be recorded.", default=[2], nargs="*")
    parser.add_argument("--conf", help="head configuration via json file, default is config.json in the cwd",
                        default=None, type=str)
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    # log all argparse arguments
    status_logger.info(args)

    # create port lists from pid
    port3d = []
    port2d = []
    for cid in args.portIndices:
        if 0 <= int(cid) <= 1:
            port2d.append(int(50020 + int(cid)))
        if 2 <= int(cid) <= 5:
            port3d.append(int(50010 + int(cid)))
    status_logger.debug("ports of 3D imagers: {}".format(port3d))
    status_logger.debug("ports of 2D imagers: {}".format(port2d))

    # only save 3D data for the moment
    devs = [Device(ip=args.ip, port=port) for port in port3d]
    status_logger.debug("WARNING: this implementation only saves 3D data at the moment")

    # configure heads with config from json config files
    if args.conf is not None:
        for dev in devs:
            if configure_head(dev, conf=args.conf):
                status_logger.info("imager successfully configured at port: {port} with json-config: {conf}".format(
                    port=port3d, conf=args.conf))
            else:
                status_logger.info("imager  configuration at port: {port} with json-config: {conf} failed".format(
                    port=port3d, conf=args.conf))

    # build FrameGrabber and ImageBuffer
    fg = [FrameGrabber(dev) for dev in devs]
    im = [ImageBuffer() for _ in enumerate(devs)]

    # TODO: implement a ImageLogger based on more than one Buffer and Device
    # only use the first set of grabber, buffer and logger
    image_logger = ImageLogger(frameGrabber=fg[0], imageBuffer=im[0], device=devs[0])
    status_logger.info("start saving data stream to file")
    num_frames = image_logger.save_data_stream(streams=['o3r',], num_sensors=1, write_index=True, numSeconds=args.numSeconds, desc="example data set")
    status_logger.info("stop saving data stream to file")
    status_logger.info("{} frames saved".format(num_frames))


if __name__ == "__main__":
    main()
