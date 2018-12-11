#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os

import types

import string

import json

class Muncher():

    def __init__(self):
        self.affix = "/root/FlaskProj/out.aff"
	self.aff = "/root/FlaskProj/temp.aff"

    def unmunch(self, wordList):

        with open(self.affix, "r") as f:

            lines = f.readlines()

        filtered_lines = lines[1:]

        with open(self.aff, "w") as w:

            w.write(''.join(filtered_lines))

        with open(self.aff, "r") as r:

            # count the number of lines

            count = -1

            for count, line in enumerate(open(self.aff, 'rU')):
                pass

            count += 1

            # count now equals to 3

            # print count

            line = r.readlines()

            # print len(line)

            i = 0

            j = 0

            test = []

            content = []

            content4 = []

            content3 = []

            content5 = []

            for l in line:

                l = " ".join(l.split())

                # print l

                length = len(l.split())

                # print l

                test1 = []

                for i in range(length):
                    test1.append(l.split()[i])

                # print test1

                if test1[3].isdigit() or test1[0] == "SET":

                    continue

                else:

                    content.append(l)

            # This helps divide words to characters

            # content = list(l.strip(" "))

            print "This is content, all the input affix: "

            # print test

            print content

            # working on th fifth row

            content5 = [i.split(' ')[4] for i in content]

            fifth_row = [x for x in content5 if not (x == "")]

            # fifth_row gives the presituation of root word

            print "The fifth row is "

            print fifth_row

            # working on the fourth row

            content4 = [i.split(' ')[3] for i in content]

            fourth_row = [x for x in content4 if not (x.isdigit())]

            # fourth_row is a list giving all the SFX added in the suffix

            print "The fourth row is "

            print fourth_row

            # working on the third row

            content3 = [i.split(' ')[2] for i in content]

            third_row = [x for x in content3 if not (x == "Y")]

            # third_row is a list giving all the SFX stripped in the suffix

            print "The third row is "

            print third_row

            # working on the second row

            content2 = [i.split(' ')[1] for i in content]

            second_row = [x for x in content2 if not (x == "Y")]

            # second_row is a list giving the kind of affix

            print "The second row is "

            print second_row

            # working on the first row

            content1 = [i.split(' ')[0] for i in content]

            first_row = [x for x in content1 if not (x == "Y")]

            # first_row is a list giving if its SFX or PFX in the suffix

            print "The third row is "

            print first_row



        lines = wordList

        # start comparing:

        length_list = []

        for t in range(len(fourth_row)):
            length_list.append(len(fourth_row[t]))

        print "This is how many characters are there in each added suffix"

        print length_list

        # when the suffix's length longer than word itself, it will output index out of range

        result = []

        all = []

        for l in lines:

            # l = l.replace("\n", "")

            all.append(l)

            result.append(l)

            print l

            check = 1

            for j in range(len(length_list)):

                # print type(l[-(length_list[j]+1):]) is types.StringType

                # print type(fourth_row[j]) is types.StringType

                if len(l) < len(fourth_row[j]):

                    print " insufficient length!"

                    pass

                else:

                    print l + " compare to " + fourth_row[j]

                    portion = l[-(length_list[j]):].replace("\n", "")

                if portion == fourth_row[j] and check == 1:

                    result.remove(l)

                    check = 0

                    print "yes"

                else:

                    print portion + "'s suffix does not equal to " + fourth_row[j]

        print "All the root word founds are: " + str(result)

        number = []

        forms = []

        temp = []

        for l in range(len(result)):

            t = 1

            print result[l]

            # for each paradigm word

            for j in range(len(all)):

                print "This is all: " + str(all[j])

                # for each random word

                for s in range(len(content)):

                    # for each affix rule

                    if all[j][-len(fourth_row[s]):] == fourth_row[s] and all[j][:-len(fourth_row[s])] + third_row[
                        s].rstrip(string.digits) == result[l]:

                        t = t + 1

                        temp.append(all[j])

                        print "!!!!!" + str(all[j][:-len(fourth_row[s])]) + " + " + str(
                            third_row[s].rstrip(string.digits)) + " = " + str(result[l])



                    else:

                        print "*****" + str(fourth_row[s]) + str(all[j][:-len(fourth_row[s])] + third_row[s])
            temp = list(set(temp))
            number.append(len(temp))

            forms.append(temp)

            temp = []

        print number

        print forms


        tempObj = {}

        newList = []

        for r in range(len(result)):
            tempObj["root"] = result[r]
            tempObj["score"] = number[r]
            tempObj["slots"] = forms[r]
            newList.append(tempObj)
            tempObj = {}



        myResult = {"candidate_words": newList}
	print myResult


        return myResult



