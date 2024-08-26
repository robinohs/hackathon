import math
import os

import numpy
import pandas as pd
import psutil
from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler
from tqdm import tqdm
import time
from cpufreq import cpuFreq

# benchmark settings
MEASUREMENTS = range(0, 150)
ENERGY_FNAME = "energy-samples.csv"
CYCLES_FNAME = "cpu-samples.csv"


def test_function():
    math.factorial(100_000)


def sample_energy():
    try:
        os.remove(ENERGY_FNAME)
    except OSError:
        pass

    csv_handler = CSVHandler(ENERGY_FNAME)

    @measure_energy(handler=csv_handler)
    def measure_test():
        return test_function()

    print("Collect energy samples via RAPL")
    for _ in tqdm(MEASUREMENTS):
        measure_test()
    csv_handler.save_data()


def sample_cpu_cycles():
    data = []
    print("Collect cycle samples via hwcounter")
    for _ in tqdm(MEASUREMENTS):
        t1_start = time.process_time()
        test_function()
        cpu_time = time.process_time() - t1_start
        data.append([psutil.cpu_freq()[0], cpu_time])
    data = numpy.asarray(data)
    df = pd.DataFrame(data)
    df.rename(columns={0: "frequency", 1: "cpu_time"}, inplace=True)
    df.to_csv(CYCLES_FNAME, index=False, sep=";")


sample_energy()
sample_cpu_cycles()
