import os
import pandas as pd

Q540VJ_read, Q540VJ_write, T480_read, T480_write, PB650G1_read, PB650G1_write = [], [], [], [], [], []
for machine in os.listdir("sources"):
    machine_path = os.path.join("sources", machine)
    for test_type in os.listdir(machine_path):
        test_type_path = os.path.join(machine_path, test_type)
        for test in os.listdir(test_type_path):
            test_path = os.path.join(test_type_path, test)
            if machine == "Q540VJ":

                if test_type == "read":
                    Q540VJ_read.append(pd.read_csv(os.path.join(test_path, "agg-read_bw.log"), header=None))
                elif test_type == "write":
                    Q540VJ_write.append(pd.read_csv(os.path.join(test_path, "agg-write_bw.log"), header=None))

            elif machine == "T480":
                if test_type == "read":
                    T480_read.append(pd.read_csv(os.path.join(test_path, "agg-read_bw.log"), header=None))
                elif test_type == "write":
                    T480_write.append(pd.read_csv(os.path.join(test_path, "agg-write_bw.log"), header=None))

            elif machine == "PB650G1":
                if test_type == "read":
                    PB650G1_read.append(pd.read_csv(os.path.join(test_path, "agg-read_bw.log"), header=None))
                elif test_type == "write":
                    PB650G1_write.append(pd.read_csv(os.path.join(test_path, "agg-write_bw.log"), header=None))
            
            else:
                print("An expected datasource is missing OR an unexpected datasource exists where it shouldn't\nPlease check the (sub)directories for anomolies!")
                quit()

