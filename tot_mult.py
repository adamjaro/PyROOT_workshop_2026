#!/usr/bin/env python3

import mplhep as hep
import matplotlib.pyplot as plt

from ROOT import RDataFrame

#_____________________________________________________________________________
def main():

    #dataframe attached to the tree in the file
    df = RDataFrame("detector_tree", "out.root")

    #total multiplicity 'tot_mult' as a hits and tracks sum
    df = df.Define("tot_mult", "nhits+tracks_npoints.size()")

    #filtering here

    #histograms for the tot_mult column
    hall = df.Histo1D(("hall", "", 60, 0, 60), "tot_mult")
    #Histo1D for the selection

    #fill the histograms, the dataframe is processed here
    hall = hall.GetValue()
    #selected histo here

    #mplhep histograms here

    #make the plot
    plt.show()

#_____________________________________________________________________________
if __name__ == "__main__":

    main()

