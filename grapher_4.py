import csv
import argparse
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter


parser = argparse.ArgumentParser(
    prog='smart-dashboard grapher',
    description='graphs smart-dashboard data'
)

parser.add_argument('filename')
parser.add_argument('arg1')
parser.add_argument('arg2')
parser.add_argument('arg3')
parser.add_argument('arg4')

args = parser.parse_args()
print("Reading " + args.filename + "...")

time = []
series1 = []
series2 = []
series3 = []
series4 = []
index1 = -1
index2 = -1
index3 = -1
index4 = -1

with open(args.filename, newline='') as csvfile:
    filereader = csv.reader(csvfile)
    for i, row in enumerate(filereader):
        if i == 0:
            for (x, title) in enumerate(row):
                if title.find(args.arg1) != -1:
                    index1 = x
                elif title.find(args.arg2) != -1:
                    index2 = x
                elif title.find(args.arg3) != -1:
                    index3 = x
                elif title.find(args.arg4) != -1:
                    index4 = x
        else:
            series1.append(float(row[index1]))
            series2.append(float(row[index2]))
            series3.append(float(row[index3]))
            series4.append(float(row[index4]))
            time.append(float(row[0]) / 1000)

  

plt.plot(time, series1)
plt.plot(time, series2)
plt.plot(time, series3)
plt.plot(time, series4)
# plt.plot(time, [0] * len(time))
plt.title(f"{args.arg1}, {args.arg2}, {args.arg3}, {args.arg4}")
# fig, ax = plt.subplots()
# ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.show()

