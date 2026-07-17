import os
import pandas as pd

class Machine:
    def __init__(self, name):
        self.name = name
        self.read = []
        self.write = []

    def load(self):
        machine_path = os.path.join("sources", self.name)
        for test_type in os.listdir(machine_path):
            test_type_path = os.path.join(machine_path, test_type)
            for test in os.listdir(test_type_path):
                test_path = os.path.join(test_type_path, test)
                filename = f"agg-{test_type}_bw.log"
                df = pd.read_csv(os.path.join(test_path, filename), header=None)
                if test_type == "read":
                    self.read.append(df)
                elif test_type == "write":
                    self.write.append(df)
