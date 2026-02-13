#!/usr/bin/env python3

from ctypes import c_int, c_double

from ROOT import TFile, TTree, std, TF1, TF2

#_____________________________________________________________________________
def main():

    #output file and tree
    out = TFile("out.root", "recreate")
    tree = TTree("detector_tree", "detector_tree")

    #branch for number of forward hits, needs c_int
    nhits = c_int(0) # object of c_int initialized to 0
    tree.Branch("nhits", nhits, "nhits/I")

    #std::vector for track points (int) and eta (double)
    tracks_npoints = std.vector("int")()
    #vector for eta (double) to come here

    #track branches
    tree.Branch("tracks_npoints", tracks_npoints)
    #branch for eta here

    #Landau distribution for forward hits
    landau = TF1("landau", "TMath::Landau(x,[0],[1])", 0, 40)
    landau.SetParameters(4, 1) #initialize the [0] and [1] parameters

    #Poisson distribution for number of tracks in event
    ntrk = 6 # mean of 6
    poisson = TF1("poisson", "TMath::Power([0], Int_t(TMath::Floor(x)) )\
        *TMath::Exp(-[0])/TMath::Factorial( Int_t(TMath::Floor(x)) )", 0, 12*ntrk)
    poisson.SetParameter(0, ntrk) # set the mean as the only parameter

    #2D Gaussian for tracks eta and number of points, positive in y
    gauss2d = TF2("gauss2d", "TMath::Exp(-x*x-y*y)", -3, 3, 0, 3)

    #number of events to generate
    nev = 2000

    #event loop
    for iev in range(nev):

        #get number of hits in the event
        nhits.value = int(landau.GetRandom())

        tracks_npoints.clear()
        #clear for eta here

        #tracks nested loop by Poisson distribution
        for itrk in range(int(poisson.GetRandom())):

            pass

            #variables for pass-by-reference to come here

            #sets the eta and npoints by reference
            #gauss2d.GetRandom2(...

            #add the track parameters, scaled int for points
            #tracks_npoints.push_back(int(100*npoints.value))
            #push_back for eta here

        #fill the tree for the event
        tree.Fill()

    #write the tree and close
    tree.Write()
    out.Close()

#_____________________________________________________________________________
if __name__ == "__main__":

    main()

