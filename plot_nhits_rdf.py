#!/usr/bin/env python3

from ROOT import RDataFrame, TCanvas, gROOT

#_____________________________________________________________________________
def main():

    gROOT.SetBatch()

    #canvas to save after plotting
    can = TCanvas("can", "can")

    #dataframe attached to the tree in the file
    df = RDataFrame("detector_tree", "out.root")

    #Histo1D call here

    #save the plot
    can.SaveAs("hits_rdf.pdf")

#_____________________________________________________________________________
if __name__ == "__main__":

    main()

