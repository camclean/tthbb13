#branch file for METree.hh

#uses branch classes from headergen
from TTH.TTHNtupleAnalyzer.headergen import *

#uses toptagger branches
from TTH.TTHNtupleAnalyzer.toptagger_branches import *

#notify headergen that we want to copy the branches from the input tree to the output tree
for b in process:
	b.needs_copy = True

#for x in ["pt", "eta", "phi", "m", "id"]:
#	process += [Dynamic1DArray("gen_lepton_{0}".format(x), "float", "nLep", "NMAXLEPTONS")]
#	process += [Dynamic1DArray("gen_jet_{0}".format(x), "float", "nJet", "NMAXLEPTONS")]
process += [Scalar("mW", "float")]
