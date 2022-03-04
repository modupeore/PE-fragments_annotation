#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main():

    bed_input = open(sys.argv[1],'r')

    ALLSIZES = []
    for line in bed_input:
        line = line.strip('\n').split('\t')
        size = int(line[2]) - int(line[1])
        ALLSIZES.append(size)

    df = pd.DataFrame({'Value':ALLSIZES})

    medians = df["Value"].median()
    maximum = df["Value"].max()
    means = df["Value"].mean()
    quantile3 = float(df["Value"].quantile([.75]))
    minimum = df["Value"].min()
    quantile1 = float(df["Value"].quantile([.5]))
    nobs = "Q2 = " + str(round(medians,2))
    nobs_max = "maximum = " + str(maximum)
    nobs_mean = "mean = " + str(round(means,2))
    nobs_min = "minimum = " + str(minimum)
    nobs_q1 = "Q1 = " + str(round(quantile1,2))
    nobs_q3 = "Q3 = " + str(round(quantile3,2))

    bbox = dict(boxstyle ="round", fc ="0.8")
    arrowprops = dict(
        arrowstyle = "-", color = 'black',
        connectionstyle = "angle, angleA = 0, \
        angleB = 90, rad = 10")

    ax = sns.violinplot(x=df["Value"], palette="pastel")
    ax.annotate(nobs_q1, xy = (quantile1,0), xytext=(quantile1,-0.3),
                bbox=bbox, arrowprops=arrowprops,
                size='small', weight='semibold')
    ax.annotate(nobs, xy = (medians,0), xytext=(medians,-0.2),
                bbox=bbox, arrowprops=arrowprops,
                size='small', weight='semibold')
    ax.annotate(nobs_q3, xy = (quantile3,0), xytext=(quantile3,-0.1),
                bbox=bbox, arrowprops=arrowprops,
                size='small', weight='semibold')
    ax.annotate(nobs_min, xy = (minimum,0), xytext=(minimum,0.3),
                bbox=bbox, arrowprops=arrowprops,
                size='small', weight='semibold')
    ax.annotate(nobs_mean, xy = (means,0), xytext=(means,0.2),
                bbox=bbox, arrowprops=arrowprops,
                size='small', weight='semibold')
    ax.annotate(nobs_max, xy = (maximum,0), xytext=(maximum,0.1),
                bbox=bbox, arrowprops=arrowprops,
                size='small', weight='semibold', ha='right')
    ax.set_title("Life Expectancy By Country",size='larger',weight='bold')
    ax.set_xlabel("Fragments sizes (bp)")

    plt.tick_params(left = False)
    plt.savefig("nameoffile.png")

if __name__ == "__main__":
    main()
