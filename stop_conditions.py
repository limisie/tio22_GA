import time
from abc import ABC, abstractmethod


class StopCondition(ABC):
    def __init__(self):
        self.optimizer = None

    @abstractmethod
    def is_stop(self):
        pass


class StopAfterNIterations(StopCondition):
    def __init__(self, n):
        super().__init__()
        self.max_iters = n

    def is_stop(self):
        return self.optimizer.iteration >= self.max_iters


class StopAfterTime(StopCondition):
    def __init__(self, max_time=60):
        super().__init__()
        self.start_time = None
        self.max_time = max_time

    def is_stop(self):
        is_stop_condition_satisfied = False

        if not self.start_time:
            self.start_time = time.time()
        else:
            if time.time() >= self.start_time + self.max_time:
                is_stop_condition_satisfied = True
                self.start_time = None

        return is_stop_condition_satisfied


class StopWhenFit(StopCondition):
    def __init__(self, expected_fitness=100):
        super().__init__()
        self.expected_fitness = expected_fitness

    def is_stop(self):
        return self.optimizer.best_fitness >= self.expected_fitness
