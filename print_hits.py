#!/usr/bin/env python3

import ROOT as rt
from ROOT import TFile, gROOT

#_____________________________________________________________________________
def main():

    gROOT.SetBatch()

    #open the file and get the tree
    infile = TFile.Open("out_2M.root")
    tree = infile.Get("detector_tree")

    #compile the .C macro
    gROOT.ProcessLine(".L print_hits.C+")

    #run the compiled function in .C,
    #passing the tree from here:
    rt.print_hits(tree)

#_____________________________________________________________________________
if __name__ == "__main__":

    main()



