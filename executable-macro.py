#!/usr/bin/env python3

from ROOT import gROOT

def main():

    #equivalent to 'root -b' (batch mode)
    gROOT.SetBatch()

    #print a message
    print("Hello")

    #function call
    another_function(3)

def another_function(x):

    print("another_function called with:", x)

if __name__ == "__main__":

    main()


