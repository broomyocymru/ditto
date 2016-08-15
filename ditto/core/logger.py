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
    ditto_logger = logging.getLogger('ditto-cli')
    msg = str(msg)

    if ditto_logger.mask_values is not None and msg is not None:
        for to_mask in ditto_logger.mask_values:
            msg = msg.replace(to_mask, "****")

    ditto_logger.info(Fore.GREEN + msg, *args, **kwargs)


def vlog(msg, *args, **kwargs):
    ditto_logger = logging.getLogger('ditto-cli')

    if ditto_logger.isEnabledFor(logging.DEBUG):
        msg = str(msg)

        if ditto_logger.mask_values is not None and msg is not None:
            for to_mask in ditto_logger.mask_values:
                msg = msg.replace(to_mask, "****")

        ditto_logger.debug(Fore.CYAN + msg, *args, **kwargs)


def json(json):
    pp = pprint.PrettyPrinter(indent=4)
    log(pp.pformat(json))


def vjson(json):
    ditto_logger = logging.getLogger('ditto-cli')

    if ditto_logger.isEnabledFor(logging.DEBUG):
        pp = pprint.PrettyPrinter(indent=4)
        vlog(pp.pformat(json))


def error(msg, *args, **kwargs):
    ditto_logger = logging.getLogger('ditto-cli')
    msg = str(msg)

    if ditto_logger.mask_values is not None and msg is not None:
        for to_mask in ditto_logger.mask_values:
            msg = msg.replace(to_mask, "****")

    ditto_logger.info(Fore.RED + msg, *args, **kwargs)


def warn(msg, *args, **kwargs):
    ditto_logger = logging.getLogger('ditto-cli')
    msg = str(msg)

    if ditto_logger.mask_values is not None and msg is not None:
        for to_mask in ditto_logger.mask_values:
            msg = msg.replace(to_mask, "****")

    ditto_logger.info(Fore.YELLOW + msg, *args, **kwargs)


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





