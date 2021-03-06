import sys

import click
from ditto.core import stopwatch, logger, util, analytics, cache


class DittoContext(object):
    def __init__(self):
        self.return_error = False
        self.continue_processing = False
        self.verbose = False
        self.mask_values = []
        self.execute_state = True

        cache.setup()

        self.stopwatch_service = stopwatch.DittoStopwatch()

        # todo - make this dynamic from configs
        self.analytics_service = analytics.MockAnalytics()
        self.analytics_service.add_metric("ditto_args", sys.argv[1:])
        self.analytics_service.add_metric("session_uuid", cache.get_session_uuid())

    def set_return_error(self, val):
        self.return_error = val
        if not self.continue_processing:
            self.stop_clock()
            raise click.Abort()

    def split_clock(self):
        logger.ditto(">>> Ditto has been running for %s >>>" % self.stopwatch_service.split())

    def start_clock(self):
        self.stopwatch_service.start()

    def stop_clock(self):
        cache.cleanup()
        self.stopwatch_service.stop()

        duration = self.stopwatch_service.duration()
        self.analytics_service.add_metric("duration", ("%s" % duration))
        self.analytics_service.submit()

        logger.ditto("")
        logger.ditto(">>> Ditto took %s and finished at %s >>>" % (duration, util.timestamp()))
        logger.ditto("")

