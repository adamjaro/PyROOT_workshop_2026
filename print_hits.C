
#if !defined(__CLING__) || defined(__ROOTCLING__)

#include <iostream>
#include "TTree.h"

using namespace std;

#endif

void print_hits(TTree *t) {

  cout << "Hi from print_hits" << endl;

  Int_t nh;
  t->SetBranchAddress("nhits", &nh);

  for(int i=0; i<7; i++) {
    t->GetEntry(i);
    cout << i << " " << nh << endl;
  }
}


