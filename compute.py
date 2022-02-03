# compute.py
#
# Author        :   David Weinberg
# Description   :   Programming Challenge for AnalyzeRe
# Date          :   2022-02-02
#
import sys, argparse


def output(n, mysum):
    """ Recursive function to generate output and track sum
    :param  n:  location in list of input
    :type n: int

    :param mysum: current sum
    :type mysum: float
    """

    # if we are at the end, print final sum and end recursion
    if (n >= len(myinput)):
        print ("{:.1f}".format(mysum))
        return

    # calc value
    value = myinput[n] - threshold
    
    # in case we are less then zero
    if (value < 0):
        value = 0

    # if we have reached the limit constraint
    if (value + mysum > limit):
        value = limit - mysum
        print ("{:.1f}".format(value))
        
        # print rest of list for efficiency (will all be zero)
        for i in range(n+1,len(myinput)):
            print ("0.0")

        # recurse one last time to print sum
        return output(len(myinput), mysum+value)        
               
    # otherwise, just print the value and recurse
    print ("{:.1f}".format(value))
    return output(n+1, mysum+value)


### MAIN ###
if __name__ == "__main__":
    # parse command-line arguments and cat'd file input
    parser =  argparse.ArgumentParser()    
    parser.add_argument('args', nargs=2)
    parser.add_argument('stdin', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    args = list(map(float, parser.parse_args().args))

    # globals to save memory, but can easily be passed in as function parameters
    myinput = list(map(float, parser.parse_args().stdin.read().splitlines()))
    threshold = args[0]
    limit = args[1]

    # check to ensure values in expected range
    if (threshold < 0 or threshold > 1000000000.0):
        sys.exit ("threshold must be between 0.0 and 1,000,000,000.0")
    
    if (limit < 0 or limit >  1000000000.0):
        sys.exit ("limit must be between 0.0 and 1,000,000,000.0")

    if (len(myinput) == 0):
        sys.exit ("input list is empty")

    # run recursive calculation
    output(0, 0)

    
