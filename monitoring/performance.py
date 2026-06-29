import time


class PerformanceMonitor:

    def measure(self, func):

        async def wrapper(*args, **kwargs):

            started = time.perf_counter()

            result = await func(
                *args,
                **kwargs,
            )

            return {
                "elapsed": time.perf_counter() - started,
                "result": result,
            }

        return wrapper
