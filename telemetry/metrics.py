class MetricsCollector:

    def __init__(self):

        self.metrics = {}

    def increment(self, metric):

        self.metrics[metric] = (
            self.metrics.get(metric, 0) + 1
        )

    def snapshot(self):

        return self.metrics.copy()
