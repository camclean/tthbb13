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
    from TopTaggingVariables import *
    from TopSamples import files, ranges, fiducial_cuts, fiducial_cuts_topSizeCut08, fiducial_cuts_topSizeCut15, pairs
# Without CMSSW
else:
    from TMVAHelpers import variable, TMVASetup, doTMVA, plotROCs
    from PrepareRootStyle import myStyle
    from TopTaggingVariables import *
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
run_TMVA = True

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

    basepath = '/eos/uscms/store/user/camclean/TopTagEfficiency/Spring15/'
    file_name_sig  = basepath + files[sample_sig] + "-weighted.root"
    file_name_bkg   = basepath + files[sample_bkg] + "-weighted.root"

    li_methods      = ["Cuts"]

    combined_mass_Nsubjettiness_setups_ak08 = []

    combined_mass_Nsubjettiness_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                        "softdropz10b00Mass + ak08 #tau_{3}/#tau_{2}, R=0.8",
                                        [["Cuts","FitMethod=MC:Sigma=0.3:SampleSize=200000"]], 
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)],
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))    

    combined_mass_Nsubjettiness_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass"),
                                        "trimmedr2f3Mass + ak08 #tau_{3}/#tau_{2}, R=0.8",
                                        [["Cuts","FitMethod=MC:Sigma=0.3:SampleSize=200000"]], 
                                        [variable('ak08trimmedr2f3_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)], 
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmed2f3_mass"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))

    
    combined_mass_Nsubjettiness_filteredn3r2Btag_setups_ak08 = []

    combined_mass_Nsubjettiness_filteredn3r2Btag_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_filteredn3r2BtagCut"),
                                        "softdropz10b00Mass + ak08 #tau_{3}/#tau_{2}, filteredn3r2 b-tag > 0.814, R=0.8",
                                        [["Cuts"]], 
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)], 
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        extra_cut = "ak08filteredn3r2forbtag_btag > 0.814",
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))

    '''combined_mass_Nsubjettiness_filteredn3r2Btag_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_filteredn3r2BtagCut"),
                                        "trimmedr2f6Mass + ak08 #tau_{3}/#tau_{2}, filteredn3r2 b-tag > 0.814, R=0.8",
                                        [["Cuts"]], 
                                        [variable('ak08trimmedr2f6_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)], 
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        extra_cut = "ak08filteredn3r2forbtag_btag > 0.814",
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))

    combined_mass_Nsubjettiness_filteredn3r2Btag_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass_filteredn3r2BtagCut"),
                                        "trimmedr2f3Mass + ak08 #tau_{3}/#tau_{2}, filteredn3r2 b-tag > 0.814, R=0.8",
                                        [["Cuts"]], 
                                        [variable('ak08trimmedr2f3_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)], 
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        extra_cut = "ak08filteredn3r2forbtag_btag > 0.814",
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))

    combined_mass_Nsubjettiness_filteredn3r2Btag_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08filteredn3r2_mass_filteredn3r2BtagCut"),
                                        "filteredn3r2Mass + ak08 #tau_{3}/#tau_{2}, filteredn3r2 b-tag > 0.814, R=0.8",
                                        [["Cuts"]], 
                                        [variable('ak08filteredn3r2_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)], 
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        extra_cut = "ak08filteredn3r2forbtag_btag > 0.814",
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08filteredn3r2_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08filteredn3r2_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08filteredn3r2_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08filteredn3r2_mass_filteredn3r2BtagCut"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))'''
                                                                             
    combined_mass_Nsubjettiness_btag_setups_ak08 = []

    combined_mass_Nsubjettiness_btag_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_softdropBtagCut"),
                                        "softdropz10b00Mass + ak08 #tau_{3}/#tau_{2}, softdrop b-tag > 0.814, R=0.8",
                                        [["Cuts"]], 
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)], 
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        extra_cut = "ak08softdropz10b00forbtag_btag > 0.814",
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_softdropBtagCut"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_softdropBtagCut"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_softdropBtagCut"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_softdropBtagCut"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))
    
    combined_mass_Nsubjettiness_btag_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_trimmedr2f6BtagCut"),
                                        "softdropz10b00Mass + ak08 #tau_{3}/#tau_{2}, trimmedr2f6 b-tag > 0.814, R=0.8",
                                        [["Cuts"]], 
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)], 
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        extra_cut = "ak08trimmedr2f6forbtag_btag > 0.814",
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_trimmedr2f6BtagCut"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_trimmedr2f6BtagCut"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_trimmedr2f6BtagCut"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_trimmedr2f6BtagCut"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))
    
    '''combined_mass_Nsubjettiness_btag_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_cmsttBtagCut"),
                                        "softdropz10b00Mass + ak08 #tau_{3}/#tau_{2}, CMSTT b-tag > 0.814, R=0.8",
                                        [["Cuts"]], 
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)], 
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        extra_cut = "ak08cmstt_sj_btag > 0.814",
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_cmsttBtagCut"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_cmsttBtagCut"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_cmsttBtagCut"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_cmsttBtagCut"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))
    '''
    '''combined_mass_Nsubjettiness_btag_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_softdropBtagCut"),
                                        "trimmedr2f6Mass + ak08 #tau_{3}/#tau_{2}, softdrop b-tag > 0.814, R=0.8",
                                        [["Cuts"]], 
                                        [variable('ak08trimmedr2f6_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)], 
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        extra_cut = "ak08softdropz10b00forbtag_btag > 0.814",
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_softdropBtagCut"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_softdropBtagCut"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_softdropBtagCut"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_softdropBtagCut"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))
    
    combined_mass_Nsubjettiness_btag_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_trimmedr2f6BtagCut"),
                                        "trimmedr2f6Mass + ak08 #tau_{3}/#tau_{2}, trimmedr2f6 b-tag > 0.814, R=0.8",
                                        [["Cuts"]], 
                                        [variable('ak08trimmedr2f6_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)], 
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        extra_cut = "ak08trimmedr2f6forbtag_btag > 0.814",
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_trimmedr2f6BtagCut"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_trimmedr2f6BtagCut"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_trimmedr2f6BtagCut"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_trimmedr2f6BtagCut"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))

    combined_mass_Nsubjettiness_btag_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass_softdropBtagCut"),
                                        "trimmedr2f3Mass + ak08 #tau_{3}/#tau_{2}, softdrop b-tag > 0.814, R=0.8",
                                        [["Cuts"]], 
                                        [variable('ak08trimmedr2f3_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)], 
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        extra_cut = "ak08softdropz10b00forbtag_btag > 0.814",
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass_softdropBtagCut"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass_softdropBtagCut"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass_softdropBtagCut"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass_softdropBtagCut"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))
    
    combined_mass_Nsubjettiness_btag_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass_trimmedr2f6BtagCut"),
                                        "trimmedr2f3Mass + ak08 #tau_{3}/#tau_{2}, trimmedr2f6 b-tag > 0.814, R=0.8",
                                        [["Cuts"]], 
                                        [variable('ak08trimmedr2f3_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)], 
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        extra_cut = "ak08trimmedr2f6forbtag_btag > 0.814",
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass_trimmedr2f6BtagCut"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass_trimmedr2f6BtagCut"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass_trimmedr2f6BtagCut"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f3_mass_trimmedr2f6BtagCut"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))
    '''
    '''combined_mass_Nsubjettiness_btag_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_cmsttBtagCut"),
                                        "trimmedr2f6Mass + ak08 #tau_{3}/#tau_{2}, CMSTT b-tag > 0.814, R=0.8",
                                        [["Cuts"]], 
                                        [variable('ak08trimmedr2f6_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)], 
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        extra_cut = "ak08cmstt_sj_btag > 0.814",
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_cmsttBtagCut"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_cmsttBtagCut"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_cmsttBtagCut"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08trimmedr2f6_mass_cmsttBtagCut"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))
    '''
    combined_softdrop_topSize_minmass_setups_ak08 = []
    
    combined_softdrop_topSize_minmass_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_minmass"),
                                        "softdropz10b00Mass + CMSTT minMass, R=0.8",
                                        [["Cuts"]],
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV")],
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_minmass"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_minmass"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_minmass"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_minmass"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))

    combined_softdrop_topSize_minmass_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_minmass"),
                                        "softdropz10b00Mass + ak08 #tau_{3}/#tau_{2} + CMSTT minMass, R=0.8",
                                        [["Cuts"]], 
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)], 
                                        [],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_minmass"),
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_minmass"),
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_minmass"),
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : "{0}_{1}_{2}_topSize_NsubjettinessStd_Cuts".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_minmass"),
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))
    
    '''combined_softdrop_topSize_minmass_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_btag_NsubjettinessSoftdrop".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_minmass"),
                                        "softdropz10b00Mass + softdrop #tau_{3}/#tau_{2} + CMSTT minMass, R=0.8",
                                        ["Cuts"],
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV", extra_cut = "ak08softdropz10b00forbtag_btag > 0.814"),
                                         variable('ak08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV", extra_cut = "ak08softdropz10b00forbtag_btag > 0.814"),
                                         variable('ak08softdropz10b00_tau3/ak08softdropz10b00_tau2',"Softdrop Nsubjettiness", 0, 1, extra_cut = "ak08softdropz10b00forbtag_btag > 0.814")],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : name,
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))

    combined_softdrop_topSize_NsubjettinessStd_setups_ak08 = []
    
    combined_softdrop_topSize_NsubjettinessStd_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                        "softdropz10b00Mass + ak08 #tau_{3}/#tau_{2}, R=0.8",
                                        ["Cuts"], 
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1)], 
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : name,
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))

    combined_softdrop_topSize_NsubjettinessStd_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_topTagCuts"),
                                        "softdropz10b00Mass + ak08 #tau_{3}/#tau_{2} + CMSTT top tag cuts, R=0.8",
                                        ["Cuts"], 
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV", extra_cut = "(ak08cmstt_nSubJets >= 3) && (ak08cmstt_minMass > 50)"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1, extra_cut = "(ak08cmstt_nSubJets >= 3) && (ak08cmstt_minMass > 50)")], 
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : name,
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))

    combined_softdrop_topSize_NsubjettinessStd_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_btag_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass"),
                                        "softdropz10b00Mass + ak08 #tau_{3}/#tau_{2}, soft drop btag > 0.814, R=0.8",
                                        ["Cuts"],
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV", extra_cut = "ak08softdropz10b00forbtag_btag > 0.814"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1, extra_cut = "ak08softdropz10b00forbtag_btag > 0.814")],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : name,
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))

    combined_softdrop_topSize_NsubjettinessStd_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_CMSTTbtag_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_topTagCuts"),
                                        "softdropz10b00Mass + ak08 #tau_{3}/#tau_{2} + CMSTT top tag cuts, CMSTT btag > 0.814, R=0.8",
                                        ["Cuts"],
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV", extra_cut = "(ak08cmstt_nSubJets >= 3) && (ak08cmstt_minMass > 50 && (ak08cmstt_sj_btag > 0.814))"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1, extra_cut = "(ak08cmstt_nSubJets >= 3) && (ak08cmstt_minMass > 50 && (ak08cmstt_sj_btag > 0.814))")],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : name,
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))

    combined_softdrop_topSize_NsubjettinessStd_setups_ak08.append(TMVASetup("{0}_{1}_{2}_topSize_trimmedr2f6Btag_NsubjettinessStd".format(sample_sig, sample_bkg, "ak08softdropz10b00_mass_topTagCuts"),
                                        "softdropz10b00Mass + ak08 #tau_{3}/#tau_{2} + CMSTT top tag cuts, trimmedr2f6 btag > 0.814, R=0.8",
                                        ["Cuts"],
                                        [variable('ak08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV", extra_cut = "(ak08cmstt_nSubJets >= 3) && (ak08cmstt_minMass > 50 && (ak08trimmedr2f6forbtag_btag > 0.814))"),
                                         variable('ak08_tau3/ak08_tau2',"AK08 Nsubjettiness", 0, 1, extra_cut = "(ak08cmstt_nSubJets >= 3) && (ak08cmstt_minMass > 50 && (ak08trimmedr2f6forbtag_btag > 0.814))")],
                                        file_name_sig,
                                        file_name_bkg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bkg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bkg = "weight",
                                        draw_roc = DRAW_ROC,
                                        working_points = [{"file_name" : name,
                                                                             "eff" : 0.2,
                                                                             "name" : "20%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.4,
                                                                             "name" : "40%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.6,
                                                                             "name" : "60%"},
                                                                            {"file_name" : name,
                                                                             "eff" : 0.9,
                                                                             "name" : "90%"}]))


    
    '''
    '''with_btag_setups = []
    for setup in combined_setups:
        new_setup = deepcopy(setup)

        new_setup.name = setup.name + "_btag"
        new_setup.li_methods = ["Cuts"]
        new_setup.li_vars.append(variable.di['ak08_btag'])
        
        with_btag_setups.append(new_setup)

        '''
    if run_TMVA:
        #for setup in combined_mass_Nsubjettiness_filteredn3r2Btag_setups_ak08:
            #doTMVA(setup)
        #for setup in combined_mass_Nsubjettiness_btag_setups_ak08:
            #doTMVA(setup) 
        '''
        for setup in combined_topSize_minmass_setups_ak08:
            doTMVA(setup)
        for setup in combined_cmstt_NsubjettinessStd_setups_ak08:
            doTMVA(setup)
        for setup in combined_softdrop_NsubjettinessStd_setups_ak08:
            doTMVA(setup)
        for setup in combined_cmstt_topSize_NsubjettinessStd_setups_ak08:
            doTMVA(setup)  
        for setup in combined_softdrop_topSize_NsubjettinessStd_setups_ak08:
            doTMVA(setup)  
        for setup in combined_softdrop_NsubjettinessSoftdrop_setups_ak08:
            doTMVA(setup)  
        for setup in combined_softdrop_topSize_NsubjettinessSoftdrop_setups_ak08:
            doTMVA(setup)
        '''

    #plotROCs("ROC_WP_mass_NsubjettinessStd_filteredn3r2Btag_compare_" + pair_name, combined_mass_Nsubjettiness_filteredn3r2Btag_setups_ak08)
    #plotROCs("ROC_WP_mass_NsubjettinessStd_btag_compare_" + pair_name, combined_mass_Nsubjettiness_btag_setups_ak08)
    plotROCs("ROC_WP_softdropz10b00mass_NsubjettinessStd_btag_compare_" + pair_name, combined_mass_Nsubjettiness_btag_setups_ak08 + combined_mass_Nsubjettiness_filteredn3r2Btag_setups_ak08) 
    #plotROCs("ROC_WP_mass_NsubjettinessStd_compare_smoothed_" + pair_name, combined_mass_Nsubjettiness_setups_ak08)

    #plotROCs("ROC_WP_softdrop_topSize_NsubjettinessStd_minMass_compare_08_May_18_2015_" + pair_name + "_1p", combined_softdrop_topSize_minmass_setups_ak08 + combined_softdrop_topSize_NsubjettinessStd_setups_ak08)


