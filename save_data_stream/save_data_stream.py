# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2021 ifm electronic gmbh, CSR
#
# ifm's support team provides code examples and helper scripts with the idea of accelerating the development process for customers.
# We do not guarantee that these scripts will be updated to reflect the lifecycle of ifm's various software packages.

from ifmO3r.ifm3dTiny import ImageLogger, FrameGrabber, ImageBuffer, Device
from ifmO3r.ifm3dTiny.utils.recorder import record as ad_record
import argparse
import logging

status_logger = logging.getLogger(__name__)


def configure_heads_from_json(conf, devs):
    # configure heads with config from json config files
    if conf is not None:
        for d in devs:
            if configure_head(d, conf):
                status_logger.info("imager successfully configured at port: {port} with json-config: {conf_file}".format(
                    port=d.id, conf_file=conf))
            else:
                status_logger.info("imager  configuration at port: {port} with json-config: {conf_file} failed".format(
                    port=d.id, conf_file=conf))

def configure_head(dev, conf):
    try:
        dev.config_from_json_file(conf)
    except Exception as e:
        status_logger.error(e)
    return True

def create_port_list_from_indices(portIndices):
    # create port lists from pid
    port3d = []
    port2d = []
    for p in portIndices:
        if 0 <= int(p) <= 1:
            port2d.append(int(50020 + int(p)))
        if 2 <= int(p) <= 5:
            port3d.append(int(50010 + int(p)))
    status_logger.debug("ports of 3D imagers: {}".format(port3d))
    status_logger.debug("ports of 2D imagers: {}".format(port2d))
    return port2d, port3d

def log_image_data(args, dev, fg, im):
    if args.type == "normal":
        # TODO: implement a ImageLogger based on more than one Buffer and Device
        # only use the first set of grabber, buffer and logger
        image_logger = ImageLogger(device=dev, frameGrabber=fg, imageBuffer=im)
        status_logger.info("start saving data stream to file")
        num_frames = image_logger.save_data_stream(streams=['o3r',], num_sensors=1, write_index=True, numSeconds=args.numSeconds, desc="example data set")
        status_logger.info("stop saving data stream to file")
        status_logger.info("{} frames saved".format(num_frames))
    elif args.type == "debug":
        #TODO
        try:
            ad_record(ip=args.ip, timeout=args.timeout, numberOfSeconds=args.numSeconds, filename=args.filename, cameras=[int(cid) for cid in args.portIndices], )
        except Exception as e:
            status_logger.error(e)
    else:
        status_logger.warning("Type of data unknown")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", help="The type of data to save (normal data stream or algo-debug data)", choices=["normal", "debug"], default="normal", type=str)
    parser.add_argument("--ip", help="ip address of VPU", default="192.168.0.69")
    parser.add_argument("--timeout", help="timeout to be used in the get function", default=3.0, type=float)
    parser.add_argument("--numSeconds", help="number of seconds to be recorded ", default=5, type=int)
    parser.add_argument("--loglevel", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    parser.add_argument("--filename",
                        help="target filename. If not given, a file will be created in the current directory.",
                        default=None)
    parser.add_argument("--portIndices", help="VPU ports to be recorded", default=[2], nargs="*")
    parser.add_argument("--conf", help="head configuration via json file, default is config.json in the cwd",
                        default=None, type=str)
    args = parser.parse_args()
    
    logging.basicConfig(level=args.loglevel)
    # log all argparse arguments
    status_logger.info(args)
    status_logger.debug("WARNING: this implementation only saves 3D data at the moment")

    port2d, port3d = create_port_list_from_indices(args.portIndices)

    # Build Devices, FrameGrabbers and ImageBuffers for supplied ports
    devs = [Device(ip=args.ip, port=port) for port in port3d]
    fgs = [FrameGrabber(dev) for dev in devs]
    ims = [ImageBuffer() for _ in enumerate(devs)]

    configure_heads_from_json(args.conf, devs)
    # Logging data for the first device. Add loop for multiple ports.
    log_image_data(args, devs[0], fgs[0], ims[0])



if __name__ == "__main__":
    main()
