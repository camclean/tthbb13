#!/usr/bin/env python
"""
Schedule the testing of different variable/method-sets with TMVA
"""

########################################
# Imports 
########################################

import pickle
import os
from copy import deepcopy
import multiprocessing as mp
import sys
sys.path.append('../Helpers')

import ROOT

# Our support Code
# With CMSSW
if "CMSSW_VERSION" in os.environ.keys():
    from TMVAHelpers import variable, TMVASetup, doTMVA, plotROCs
    from PrepareRootStyle import myStyle
    #from TopTaggingVariables import *
    from TopSamples import files, ranges, fiducial_cuts, fiducial_cuts_topSizeCut08, fiducial_cuts_topSizeCut15, pairs
# Without CMSSW
else:
    from TMVAHelpers import variable, TMVASetup, doTMVA, plotROCs
    from PrepareRootStyle import myStyle
    #from TopTaggingVariables import *
    from TopSamples import files, ranges, fiducial_cuts, fiducial_cuts_topSizeCut08, fiducial_cuts_topSizeCut15, pairs

myStyle.SetTitleXOffset(1.3)
myStyle.SetTitleYOffset(1.7)
myStyle.SetPadLeftMargin(0.19)
myStyle.SetPadBottomMargin(0.13)

ROOT.gROOT.SetStyle("myStyle")
ROOT.gROOT.ForceStyle()


########################################
# Configuration
########################################
DRAW_ROC = True
run_TMVA = False

to_process  = pairs.keys()
#to_process = ["pt-800-to-1000_1p_topSize"]
for k in to_process:
    print "doing", k
    
    pair_name = k
    pair = pairs[pair_name]
    
    #pair_name = "pt-800-to-1000_1p_topSize"
    #pair_name = "pt-300-to-470_1p"
    #pair_name = "pt-1000-to-1400_10p"
    #pair = pairs[pair_name]

    sample_sig = pair[0]
    sample_bkg = pair[1]

    basepath = 'root://cmseos.fnal.gov//store/user/camclean/TopTagEfficiency/80X/'
    file_name_sig  = basepath + files[sample_sig] + "-weighted.root"
    file_name_bkg   = basepath + files[sample_bkg] + "-weighted.root"

    li_methods      = ["Cuts"]

    combined_mass_Nsubjettiness_setups_ak08 = []
    
    combined_mass_Nsubjettiness_setups_ak08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                        "softdropz10b00Mass, R=0.8, Flat",
                                        [["Cuts","FitMethod=MC:Sigma=0.3:SampleSize=20000"]], 
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 100, 500, unit = "GeV")],
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        tree_name_sig    = "tree_topTag",
                                        tree_name_bkg    = "tree_topTag",
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC, 
                                        working_points = [{"file_name" : "{0}_{1}_{2}_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                                                             "eff" : 0.9,

                                                                             "name" : "90%"}]))    

    combined_mass_Nsubjettiness_setups_ak08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "NsubjettinessStd"),
                                        "ak08 #tau_{3}/#tau_{2}, R=0.8, Flat",
                                        [["Cuts","FitMethod=MC:Sigma=0.3:SampleSize=20000"]], 
                                        [variable('ak08softdropz10b00_tau32',"AK08 Nsubjettiness", 0, 1)],
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        tree_name_sig    = "tree_topTag",
                                        tree_name_bkg    = "tree_topTag",
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC, 
                                        working_points = [{"file_name" : "{0}_{1}_{2}_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd"),
                                                                             "eff" : 0.9,

                                                                             "name" : "90%"}]))    

    combined_mass_Nsubjettiness_setups_ak08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_NsubjettinessStd"),
                                        "softdropz10b00Mass + ak08 #tau_{3}/#tau_{2}, R=0.8, Flat",
                                        [["Cuts","FitMethod=MC:Sigma=0.3:SampleSize=20000"]], 
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 100, 500, unit = "GeV"),
                                         variable('ak08softdropz10b00_tau32',"AK08 Nsubjettiness", 0, 1)],
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        tree_name_sig    = "tree_topTag",
                                        tree_name_bkg    = "tree_topTag",
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC, 
                                        working_points = [{"file_name" : "{0}_{1}_{2}_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_NsubjettinessStd"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_NsubjettinessStd"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_NsubjettinessStd"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_NsubjettinessStd"),
                                                                             "eff" : 0.9,

                                                                             "name" : "90%"}]))
    
    combined_mass_Nsubjettiness_setups_ak08.append(TMVASetup("{0}_{1}_{2}_noWeight".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                        "softdropz10b00Mass, R=0.8",
                                        [["Cuts","FitMethod=MC:Sigma=0.3:SampleSize=20000"]], 
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 100, 500, unit = "GeV")],
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        tree_name_sig    = "tree_topTag",
                                        tree_name_bkg    = "tree_topTag",
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        draw_roc = DRAW_ROC, 
                                        working_points = [{"file_name" : "{0}_{1}_{2}_noWeight_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_noWeight_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_noWeight_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_noWeight_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                                                             "eff" : 0.9,

                                                                             "name" : "90%"}]))    

    combined_mass_Nsubjettiness_setups_ak08.append(TMVASetup("{0}_{1}_{2}_noWeight".format(sample_sig, sample_bkg, "NsubjettinessStd"),
                                        "ak08 #tau_{3}/#tau_{2}, R=0.8",
                                        [["Cuts","FitMethod=MC:Sigma=0.3:SampleSize=20000"]], 
                                        [variable('ak08softdropz10b00_tau32',"AK08 Nsubjettiness", 0, 1)],
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        tree_name_sig    = "tree_topTag",
                                        tree_name_bkg    = "tree_topTag",
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        draw_roc = DRAW_ROC, 
                                        working_points = [{"file_name" : "{0}_{1}_{2}_noWeight_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_noWeight_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_noWeight_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_noWeight_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd"),
                                                                             "eff" : 0.9,

                                                                             "name" : "90%"}]))    

    combined_mass_Nsubjettiness_setups_ak08.append(TMVASetup("{0}_{1}_{2}_noWeight".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_NsubjettinessStd"),
                                        "softdropz10b00Mass + ak08 #tau_{3}/#tau_{2}, R=0.8",
                                        [["Cuts","FitMethod=MC:Sigma=0.3:SampleSize=20000"]], 
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 100, 500, unit = "GeV"),
                                         variable('ak08softdropz10b00_tau32',"AK08 Nsubjettiness", 0, 1)],
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        tree_name_sig    = "tree_topTag",
                                        tree_name_bkg    = "tree_topTag",
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        draw_roc = DRAW_ROC, 
                                        working_points = [{"file_name" : "{0}_{1}_{2}_noWeight_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_NsubjettinessStd"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_noWeight_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_NsubjettinessStd"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_noWeight_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_NsubjettinessStd"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_noWeight_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_NsubjettinessStd"),
                                                                             "eff" : 0.9,

                                                                             "name" : "90%"}]))
    
    '''combined_fixedMass_Nsubjettiness_setups_ak08 = []
    for i_massMin in range(0,6):
        s_massMin = str(95+(i_massMin*5))
        #for i_massMax in range(0,13):
        #s_massMax = str(190+(i_massMax*5))
        cutVar1 = "ak08 #tau_{3}/#tau_{2}"
        cutVar2 = "M_{SD}"
        
        print "{0}, R=0.8 ({1} < {2} < 230 GeV)".format(cutVar1, s_massMin, cutVar2)

        combined_fixedMass_Nsubjettiness_setups_ak08.append(TMVASetup("{0}_{1}_{2}_{3}_230".format(sample_sig, sample_bkg, "NsubjettinessStd_ak08softdropz10b00_mass", s_massMin),
                                        "{0}, R=0.8, Flat ({1} < {2} < 230 GeV)".format(cutVar1, s_massMin, cutVar2),
                                        [["Cuts","FitMethod=MC:Sigma=0.3:SampleSize=20000"]], 
                                        [variable('ak08softdropz10b00_tau32',"AK08 Nsubjettiness", 0, 1)],
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        tree_name_sig    = "tree_topTag",
                                        tree_name_bkg    = "tree_topTag",
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        extra_cut = "ak08softdropz10b00_mass > {0} && ak08softdropz10b00_mass < 230".format(s_massMin),
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC, 
                                        working_points = [{"file_name" : "{0}_{1}_{2}_{3}_230_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd_ak08softdropz10b00_mass", s_massMin),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_{3}_230_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd_ak08softdropz10b00_mass", s_massMin),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_{3}_230_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd_ak08softdropz10b00_mass", s_massMin),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_{3}_230_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd_ak08softdropz10b00_mass", s_massMin),
                                                                             "eff" : 0.9,

                                                                             "name" : "90%"}]))    

        combined_fixedMass_Nsubjettiness_setups_ak08.append(TMVASetup("{0}_{1}_{2}_{3}_230_noWeight".format(sample_sig, sample_bkg, "NsubjettinessStd_ak08softdropz10b00_mass", s_massMin),
                                        "{0}, R=0.8 ({1} < {2} < 230 GeV)".format(cutVar1, s_massMin, cutVar2),
                                        [["Cuts","FitMethod=MC:Sigma=0.3:SampleSize=20000"]], 
                                        [variable('ak08softdropz10b00_tau32',"AK08 Nsubjettiness", 0, 1)],
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        tree_name_sig    = "tree_topTag",
                                        tree_name_bkg    = "tree_topTag",
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        extra_cut = "ak08softdropz10b00_mass > {0} && ak08softdropz10b00_mass < 230".format(s_massMin),
                                        draw_roc = DRAW_ROC, 
                                        working_points = [{"file_name" : "{0}_{1}_{2}_{3}_230_noWeight_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd_ak08softdropz10b00_mass", s_massMin),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_{3}_230_noWeight_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd_ak08softdropz10b00_mass", s_massMin),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_{3}_230_noWeight_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd_ak08softdropz10b00_mass", s_massMin),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_{3}_230_noWeight_Cuts".format(sample_sig, sample_bkg, "NsubjettinessStd_ak08softdropz10b00_mass", s_massMin),
                                                                             "eff" : 0.9,

                                                                             "name" : "90%"}]))'''


    if run_TMVA:
        #for setup in combined_mass_Nsubjettiness_setups_ak08:
        #    doTMVA(setup)                                           
        for setup in combined_fixedMass_Nsubjettiness_setups_ak08:
            doTMVA(setup)
    #if DRAW_ROC:
        #plotROCs("ROC_WP_softdropz10b00mass_Nsubjettiness_compare_" + pair_name, combined_mass_Nsubjettiness_setups_ak08) 
        #plotROCs("results/ROC/ROC_WP_fixedSoftdropz10b00mass_Nsubjettiness_compare_" + pair_name, combined_fixedMass_Nsubjettiness_setups_ak08)
    if DRAW_ROC:
        print len(combined_fixedMass_Nsubjettiness_setups_ak08)
        plotROCs("results/ROC/ROC_WP_fixedSoftdropz10b00massMin95to120Max230_Nsubjettiness_flat_compare_" + pair_name, combined_fixedMass_Nsubjettiness_setups_ak08)

