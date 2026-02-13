#!/usr/bin/env python3

from ROOT import TFile, TCanvas, gROOT, RDataFrame, TF1, std

#_____________________________________________________________________________
def main():

    gROOT.SetBatch()

    #canvas to save after plotting
    can = TCanvas("can", "can")

    #input dataframe
    df = RDataFrame("detector_tree", "out.root")

    #make the histogram
    hx = df.Histo1D(("hx", "", 40, 0, 40), "nhits")

    #Landau distribution for the fit
    landau = TF1("landau", "[2]*TMath::Landau(x,[0],[1])", 0, 40)
    landau.SetParameters(4, 1, 4)

    #make the fit, option 'S' to save the results
    res_ptr = hx.Fit(landau, "S")

    #get TFitResult from TFitResultPtr
    res = res_ptr.Get()

    #print the help with method resolution order
    #help(res)

    #stringstream for fit results
    stream = std.stringstream()

    #one of the methods for fit results to come here

    #print the results
    print(stream.str())

    #draw the fit
    hx.Draw()

    #save the plot
    can.SaveAs("hits.pdf")

#_____________________________________________________________________________
if __name__ == "__main__":

    main()

