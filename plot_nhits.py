#!/usr/bin/env python3

from ROOT import TFile, TCanvas, gROOT, TH1D

#_____________________________________________________________________________
def main():

    gROOT.SetBatch()

    #canvas to save after plotting
    can = TCanvas("can", "can")

    #open the generated file and tree
    infile = TFile.Open("out.root")
    tree = infile.Get("detector_tree")

    #make the histogram
    hx = TH1D("hx", "hx", 40, 0, 40)

    #fill the histogram here

    #save the plot
    can.SaveAs("hits.pdf")

#_____________________________________________________________________________
if __name__ == "__main__":

    main()

