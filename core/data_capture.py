from collections import defaultdict

from core.stats_builder import StatsBuilder


class DataCapture:
    def __init__(self):
        self.counts = defaultdict(int)

    def add(self, number: int):
        """Add a number to the data capture"""
        self.counts[number] += 1

    def build_stats(self):
        """Build the stats from the data capture"""
        return StatsBuilder(self.counts)
