class StatsBuilder:
    def __init__(self, counts):
        self.counts = counts
        self.prefix_counts = self._build_prefix_counts()

    def _build_prefix_counts(self):
        """Build the prefix counts

        The prefix counts are the number of numbers less than or equal to the given number
        """
        
        max_number = max(self.counts.keys())
        prefix_counts = [0] * (max_number + 1)

        for number in range(1, max_number + 1):
            prefix_counts[number] = prefix_counts[number - 1] + self.counts[number]

        return prefix_counts

    def less(self, number: int):
        """Return the number of numbers less than the given number"""
        if number == 0:
            return 0
        return self.prefix_counts[number - 1]

    def between(self, lower: int, upper: int):
        """Return the number of numbers between the given numbers"""
        upper_index = min(upper, len(self.prefix_counts) - 1)
        lower_index = min(lower - 1, len(self.prefix_counts) - 1)

        if lower > 0:
            return self.prefix_counts[upper_index] - self.prefix_counts[lower_index]
        return self.prefix_counts[upper_index]

    def greater(self, number: int):
        """Return the number of numbers greater than the given number"""
        total_numbers = sum(self.counts.values())
        return total_numbers - self.prefix_counts[number]
