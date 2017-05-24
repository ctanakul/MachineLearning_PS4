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
    ex_n = 1000 #Even number
    att_n = 20 #150 abs_diff = 40%
    with open('q2_1.arff', 'wb') as csvfile:
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
        datwriter.writerow(['@attribute quality {a', 'b', 'c', 'd', 'e', 'f}'])
        datwriter.writerow([])

        # data header
        datwriter.writerow(['@data'])

        # data generator
        for index,row in enumerate(range(ex_n)):
            a = [random.choice([0,1,2,3,4,5]) for i in range(att_n)]
            # if index < 250:
            #     a[0] = 0
            #     a[1] = 0
            #     a[2] = 0
            # elif index < 500:
            #     a[0] = 0
            #     a[1] = 1
            #     a[2] = 1
            # elif index < 750:
            #     a[0] = 1
            #     a[1] = 0
            #     a[2] = 1
            # else:
            #     a[0] = 1
            #     a[1] = 1
            #     a[2] = 0
            # a[54] = 0
            if index < 20:
                print a[0] + a[1]
            if a[0] + a[1] >= 7:
                a[att_n - 1] = 'a'
            elif a[0] + a[1] >= 6:
                a[att_n - 1] = 'b'
            elif a[0] + a[1] >= 5:
                a[att_n - 1] = 'c'
            elif a[0] + a[1] >= 4:
                a[att_n - 1] = 'd'
            elif a[0] + a[1] >= 3:
                a[att_n - 1] = 'e'
            else:
                a[att_n - 1] = 'f'
            datwriter.writerow(a)
        # for index,row in enumerate(range(ex_n/2)):
        #     b = [random.choice([0,1]) for i in range(att_n)]
        #     if index < 20:
        #         b[0] = 0
        #         b[1] = 1
        #         b[2] = 0
        #     elif index < 40:
        #         b[0] = 1
        #         b[1] = 1
        #         b[2] = 1
        #     else:
        #         b[0] = 1
        #         b[1] = 0
        #         b[2] = 0
        #     # b[0] = 0
        #     # b[37] = 1
        #     # b[98] = 0
        #     b[att_n - 1] = 'bad'
        #     datwriter.writerow(b)

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
    q2_gen()
    arff_conv_data('q2_1')
if __name__=='__main__':
    main()
