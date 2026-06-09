import pullfiles
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def returnavg(lst):
    return ((pd.concat(lst))[1].mean()) / 1024
    # '.concat()' --> combine list of individual dataframes into one dataframe
    # '[x].mean()' --> find the average of column x


# def lineofbestfit(dataset):
#    return np.polyfit(dataset.index, dataset["bandwidth"], 1)


def writetest(testlist, graphcolor, staticcolor, devicename):
    finaltest = pd.concat(testlist, ignore_index=True)     # ------------------------------------------ ignore index so that index doesn't reset to 0
    finaltest.columns = ["time", "bandwidth", "col3", "col4", "col5"]
    finaltest["time"] = finaltest["time"] / 1000     # ------------------------------------------------ ms to s  | not really needed? can use it for later though if we do
    finaltest["bandwidth"] = finaltest["bandwidth"] / 1024     # -------------------------------------- KiB/S to MiB/S
    #finaltest.plot(y="bandwidth", color=graphcolor, alpha=0.2, label=f"{devicename}", ax=ax1)     # --- matplotlib auto assigns the x value to be the index
    finaltest["bandwidth"].rolling(window = 100).mean().plot(color=graphcolor, label=f"{devicename} Rolling Avg.", ax=ax1)
    ax1.axhline(y=returnavg(testlist), color=staticcolor, linestyle="--", label=f"{devicename} Static Avg")
    ax1.text(0, returnavg(testlist), f"{returnavg(testlist):.2f} MiB/s", color="black", va="bottom", fontsize=13)


def readtest(testlist, graphcolor, staticcolor, devicename):
    finaltest = pd.concat(testlist, ignore_index=True)     # ------------------------------------------ ignore index so that index doesn't reset to 0
    finaltest.columns = ["time", "bandwidth", "col3", "col4", "col5"]
    finaltest["time"] = finaltest["time"] / 1000     # ------------------------------------------------ ms to s  | not really needed? can use it for later though if we do
    finaltest["bandwidth"] = finaltest["bandwidth"] / 1024     # -------------------------------------- KiB/S to MiB/S
    #finaltest.plot(y="bandwidth", color=graphcolor, alpha=0.2, label=f"{devicename}", ax=ax2)     # --- matplotlib auto assigns the x value to be the index
    finaltest["bandwidth"].rolling(window=100).mean().plot(color=graphcolor, label=f"{devicename} Rolling Avg", ax=ax2)
    ax2.axhline(y=returnavg(testlist), color=staticcolor, linestyle="--", label=f"{devicename} Static Avg")
    ax2.text(0, returnavg(testlist), f"{returnavg(testlist):.2f} MiB/s", color="black", va="bottom", fontsize=13)


if __name__ == "__main__":

    #fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(28, 8))     # both graphs in same figure
    fig1, ax1 = plt.subplots(figsize=(14, 8))     # ------------ using this instead because i need two separate images
    fig2, ax2 = plt.subplots(figsize=(14, 8))
    # ax1 is for the write tests
    # ax2 is for the read tests
    
    writetest(pullfiles.Q540VJ_write, "teal", "aqua", "Q540VJ (WiFi 6E)")
    writetest(pullfiles.T480_write, "green", "lime", "T480 (WiFi 5)")
    writetest(pullfiles.PB650G1_write, "purple", "fuchsia", "PB650G1 (WiFi 4)")

    readtest(pullfiles.Q540VJ_read, "teal", "aqua", "Q540VJ (WiFi 6E)")
    readtest(pullfiles.T480_read, "green", "lime", "T480 (WiFi 5)")
    readtest(pullfiles.PB650G1_read, "purple", "fuchsia", "PB650G1 (WiFi 4)")


    ax1.legend()
    ax2.legend()
    
    ax1.set_xlabel("Index value")
    ax1.set_ylabel("Bandwidth (MiB/s)")
    ax2.set_xlabel("Index value")
    ax2.set_ylabel("Bandwidth (MiB/s)")

    plt.title("Reading/Writing to Cloud against Wi-Fi Version")
    ax1.set_title("Writing")
    ax2.set_title("Reading")
    #plt.savefig("output.png", dpi=300, bbox_inches="tight")  # both graphs in same figure
    fig1.savefig("write.png", dpi=300, bbox_inches="tight")
    fig2.savefig("read.png", dpi=300, bbox_inches="tight")
    plt.show()