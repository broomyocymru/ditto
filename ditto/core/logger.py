import logging
import pprint
from colorama import init, Fore
init()


def setup():
    ditto_logger = logging.getLogger('ditto-cli')
    ch = logging.StreamHandler()
    ditto_logger.addHandler(ch)

    if not hasattr(ditto_logger, 'mask_values'):
        ditto_logger.mask_values = []

    return ditto_logger


def log(msg, *args, **kwargs):
    return log_colour(msg, Fore.GREEN, *args, **kwargs)


def vlog(msg, *args, **kwargs):
    ditto_logger = logging.getLogger('ditto-cli')

    if ditto_logger.isEnabledFor(logging.DEBUG):
        return log_colour(msg, Fore.CYAN, *args, **kwargs)


def json(json):
    pp = pprint.PrettyPrinter(indent=4)
    return log(pp.pformat(json))


def vjson(json):
    ditto_logger = logging.getLogger('ditto-cli')

    if ditto_logger.isEnabledFor(logging.DEBUG):
        pp = pprint.PrettyPrinter(indent=4)
        vlog(pp.pformat(json))


def error(msg, *args, **kwargs):
    return log_colour(msg, Fore.RED, *args, **kwargs)


def warn(msg, *args, **kwargs):
    return log_colour(msg, Fore.YELLOW, *args, **kwargs)


def log_colour(msg, colour, *args, **kwargs):
    ditto_logger = logging.getLogger('ditto-cli')
    msg = str(msg)

    if ditto_logger.mask_values is not None and msg is not None:
        for to_mask in ditto_logger.mask_values:
            msg = msg.replace(to_mask, "****")

    colour_msg = colour + msg
    ditto_logger.info(colour_msg, *args, **kwargs)
    return colour_msg


def ditto(msg):
    ditto_logger = logging.getLogger('ditto-cli')
    ditto_logger.info(Fore.CYAN + msg)


def mask(val):
    ditto_logger = logging.getLogger('ditto-cli')
    ditto_logger.mask_values.append(val)


def get_masks():
    ditto_logger = logging.getLogger('ditto-cli')
    return ditto_logger.mask_values


def verbose():
    ditto_logger = logging.getLogger('ditto-cli')
    return ditto_logger.isEnabledFor(logging.DEBUG)





