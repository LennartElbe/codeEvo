"""Take input directory and build a new directory which contains the solutions
but not the hiddenCode written by Professor Thiemann.
"""

import glob
import os
from datetime import date
import time

inputdir = 'log-20190927'
outputdir = 'StudentProblem'
# create output directory
if not os.path.isdir(outputdir):
    os.mkdir(outputdir)
# returns all directory paths for students
students = glob.glob(os.path.join(inputdir, '132*'))
problems = []
# iterate through every single student
for student in students:
    # find all python files for each student and return their paths
    files = glob.glob(student + '/*.py')
    # iterate through every python file
    for file in files:
        # get machine id
        # file is a string of the path to the python script
        # we need to split at '/' and a split at the '-'
        #problem number we are looking at
        dname = file.split('/')[1] # the student's ID in the path
        dname = dname.split('-')[1]
        # name of student's file
        fname = file.split('/')[2]
        #get content of file
        seperatedContent = []
        solution = ""
        hiddenCode = ""
        with open(file, 'r') as textfile:
            line = textfile.readline() # grab the first line
            while line: # while line variable is not empty string
                solution = solution + line # add line to our solution
                line = textfile.readline() # grab next line
                if line.startswith("## hidden"): # hidden code starting
                        line = textfile.readline()
                        while line:
                            if "sung Teil" in line: # hidden code done
                                break
                            else: # hidden code continues
                                hiddenCode = hiddenCode + line
                                line = textfile.readline()
                        continue

        seperatedContent.append(solution)
        seperatedContent.append(hiddenCode.strip())
        if not os.path.isdir(os.path.join(outputdir, dname)):  # StudentProblem/<student's ip>
                os.mkdir(os.path.join(outputdir, dname))
        problemPath = ''
        if (len(problems) == 0):
                problems.append(seperatedContent[1])
        #for i in problems:
        #    if (i == seperatedContent[1]):
        #        problemPath = os.path.join(outputdir, dname, str(problems.index(seperatedContent[1])))
        #    elif (i != seperatedContent[1]):
        #        problems.append(seperatedContent[1])
        #        problemPath = os.path.join(outputdir, dname, str(problems.index(seperatedContent[1])))
        if (seperatedContent[1] in problems):
            problemPath = os.path.join(outputdir, dname, str(problems.index(seperatedContent[1])+1))
        else:
            problems.append(seperatedContent[1])
            problemPath = os.path.join(outputdir, dname, str(problems.index(seperatedContent[1])+1))
        if not os.path.isdir(os.path.join(outputdir, "problems")):
            os.mkdir(os.path.join(outputdir, "problems"))
        if not os.path.isdir(problemPath):
            os.mkdir(problemPath)
        f = os.path.join(problemPath, fname)
        with open(f, 'w') as fp:
            fp.write(seperatedContent[0])
        # closed after with and modification time is the same
        Timestamp = os.path.getmtime(file)
        d = time.localtime(Timestamp)
        modTime = time.mktime(d)
        os.utime(f, (modTime, modTime))
for problem in problems:
    p = os.path.join(os.path.join(outputdir, "problems", str(problems.index(problem))))
    with open(p, 'w') as pp:
        pp.write(problem.strip())
