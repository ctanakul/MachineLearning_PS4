##Generating csv file q1.data for Weka trainibg

import random
import csv


def q1_gen():
    with open('q1.arff', 'wb') as csvfile:
        # datwriter = csv.writer(csvfile, delimiter=',',
        #                         quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        datwriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)

        # @relation
        datwriter.writerow(['@relation training'])
        datwriter.writerow([])

        # @999attributes
        for n in range(999):
            s = "@attribute 'a%d' numeric" %(n+1)
            # datwriter.writerow(["@attribute 'a%d' numeric"]) %n
            datwriter.writerow([s])
            n += 1

        # classified attribute
        datwriter.writerow(['@attribute quality {good', 'bad}'])
        datwriter.writerow([])

        # data header
        datwriter.writerow(['@data'])

        # data generator
        for row in range(500):
            a = [random.choice([0,1]) for i in range(1000)]
            a[0] = 1
            a[999] = 'good'
            datwriter.writerow(a)
        for row in range(500):
            b = [random.choice([0,1]) for i in range(1000)]
            b[0] = 0
            b[999] = 'bad'
            datwriter.writerow(b)

def q2_gen():
    ex_n = 10 #Even number
    att_n = 150 #150 abs_diff = 40%
    with open('q2_3.arff', 'wb') as csvfile:
        datwriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)

        # @relation
        datwriter.writerow(['@relation training'])
        datwriter.writerow([])

        # @999attributes
        for n in range(att_n - 1):
            s = "@attribute 'a%d' numeric" %(n+1)
            # datwriter.writerow(["@attribute 'a%d' numeric"]) %n
            datwriter.writerow([s])
            n += 1

        # classified attribute
        datwriter.writerow(['@attribute quality {good', 'bad}'])
        datwriter.writerow([])

        # data header
        datwriter.writerow(['@data'])

        # data generator
        for row in range(ex_n/2):
            a = [random.choice([0,1]) for i in range(att_n)]
            # a[0] = 1
            # a[54] = 0
            a[att_n - 1] = 'good'
            datwriter.writerow(a)
        for row in range(ex_n/2):
            b = [random.choice([0,1]) for i in range(att_n)]
            # b[0] = 0
            # b[37] = 1
            # b[98] = 0
            b[att_n - 1] = 'bad'
            datwriter.writerow(b)

def arff_conv_data(name):
    with open(name + '.data', 'wb') as csv_write:
        datwriter = csv.writer(csv_write, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        with open(name + '.arff', 'rb') as csv_read:
            reader = csv.reader(csv_read, delimiter=',')
            i = 0
            for row in reader:
                if row != []:
                    if (row[0])[0] != '@':
                        datwriter.writerow(row)

def main():
    arff_conv_data('q2_4')
if __name__=='__main__':
    main()
