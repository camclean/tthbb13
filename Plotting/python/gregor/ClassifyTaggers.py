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

import ROOT

# Our support Code
# With CMSSW
if "CMSSW_VERSION" in os.environ.keys():
    from TTH.Plotting.Helpers.TMVAHelpers import variable, TMVASetup, doTMVA, plotROCMultiple
    from TTH.Plotting.Helpers.PrepareRootStyle import myStyle
    from TTH.Plotting.gregor.TopTaggingVariables import *
    from TTH.Plotting.gregor.TopSamples import files, ranges, fiducial_cuts, fiducial_cuts_topSizeCut08, fiducial_cuts_topSizeCut15, pairs
# Without CMSSW
else:
    from TTH.Plotting.python.Helpers.TMVAHelpers import variable, TMVASetup, doTMVA, plotROCMultiple
    from TTH.Plotting.python.Helpers.PrepareRootStyle import myStyle
    from TTH.Plotting.python.gregor.TopTaggingVariables import *
    from TTH.Plotting.python.gregor.TopSamples import files, ranges, fiducial_cuts, fiducial_cuts_topSizeCut08, fiducial_cuts_topSizeCut15, pairs

ROOT.gROOT.SetStyle("myStyle")
ROOT.gROOT.ForceStyle()


########################################
# Configuration
########################################
run_TMVA = True

# We want to make single-variable ROC curves
# so first create a list of variables and then send them individually to TMVA
    
def create_setups(li_vars):
    li_TMVAs = []
    for v in li_vars:
        name = "{0}_{1}_{2}".format(sample_sig, sample_bkg, v.name)
        name = name.replace("/","_")
        li_TMVAs.append( TMVASetup( name,
                                    v.pretty_name,
                                    li_methods, 
                                    [v],
                                    file_name_sig,
                                    file_name_bg,
                                    fiducial_cut_sig = fiducial_cuts[sample_sig],
                                    fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                    weight_sig = "weight",
                                    weight_bg  = "weight",
                                    ))
    return li_TMVAs

'''def create_setups08(li_vars):
    li_TMVAs = []
    for v in li_vars:
        name = "{0}_{1}_{2}".format(sample_sig, sample_bkg, v.name)
        name = name.replace("/","_")
        li_TMVAs.append( TMVASetup( name,
                                    v.pretty_name,
                                    li_methods, 
                                    [v],
                                    file_name_sig,
                                    file_name_bg,
                                    fiducial_cut_sig = fiducial_cuts[sample_sig],
                                    fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                    weight_sig = "weight",
                                    weight_bg  = "weight",
                                    ))
    return li_TMVAs

def create_setups15(li_vars):
    li_TMVAs = []
    for v in li_vars:
        name = "{0}_{1}_{2}".format(sample_sig, sample_bkg, v.name)
        name = name.replace("/","_")
        li_TMVAs.append( TMVASetup( name,
                                    v.pretty_name,
                                    li_methods, 
                                    [v],
                                    file_name_sig,
                                    file_name_bg,
                                    fiducial_cut_sig = fiducial_cuts[sample_sig],
                                    fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                    weight_sig = "weight",
                                    weight_bg  = "weight",
                                    ))
    return li_TMVAs

def create_setups_topSize08(li_vars):
    li_TMVAs = []
    for v in li_vars:
        name = "{0}_{1}_{2}_topSize".format(sample_sig, sample_bkg, v.name)
        name = name.replace("/","_")
        li_TMVAs.append( TMVASetup( name,
                                    v.pretty_name,
                                    li_methods, 
                                    [v],
                                    file_name_sig,
                                    file_name_bg,
                                    fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                    fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                    weight_sig = "weight",
                                    weight_bg  = "weight",
                                    ))
    return li_TMVAs
'''
def create_setups_topSize15(li_vars):
    li_TMVAs = []
    for v in li_vars:
        name = "{0}_{1}_{2}_topSize".format(sample_sig, sample_bkg, v.name)
        name = name.replace("/","_")
        li_TMVAs.append( TMVASetup( name,
                                    v.pretty_name,
                                    li_methods, 
                                    [v],
                                    file_name_sig,
                                    file_name_bg,
                                    fiducial_cut_sig = fiducial_cuts_topSizeCut15[sample_sig],
                                    fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                    weight_sig = "weight",
                                    weight_bg  = "weight",
                                    ))
    return li_TMVAs

def create_setups_topTagCuts(li_vars):
    li_TMVAs = []
    for v in li_vars:
        name = "{0}_{1}_{2}_topTagCuts".format(sample_sig, sample_bkg, v.name)
        name = name.replace("/","_")
        li_TMVAs.append( TMVASetup( name,
                                    v.pretty_name,
                                    li_methods, 
                                    [v],
                                    file_name_sig,
                                    file_name_bg,
                                    fiducial_cut_sig = fiducial_cuts[sample_sig],
                                    fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                    weight_sig = "weight",
                                    weight_bg  = "weight",
                                    ))
    return li_TMVAs

'''def create_setups_topTagCuts15(li_vars):
    li_TMVAs = []
    for v in li_vars:
        name = "{0}_{1}_{2}_topTagCuts".format(sample_sig, sample_bkg, v.name)
        name = name.replace("/","_")
        li_TMVAs.append( TMVASetup( name,
                                    v.pretty_name,
                                    li_methods, 
                                    [v],
                                    file_name_sig,
                                    file_name_bg,
                                    fiducial_cut_sig = fiducial_cuts[sample_sig],
                                    fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                    weight_sig = "weight",
                                    weight_bg  = "weight",
                                    ))
    return li_TMVAs
'''
def create_setups_topTagCuts_topSize08(li_vars):
    li_TMVAs = []
    for v in li_vars:
        name = "{0}_{1}_{2}_topTagCuts_topSize".format(sample_sig, sample_bkg, v.name)
        name = name.replace("/","_")
        li_TMVAs.append( TMVASetup( name,
                                    v.pretty_name,
                                    li_methods, 
                                    [v],
                                    file_name_sig,
                                    file_name_bg,
                                    fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                    fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                    weight_sig = "weight",
                                    weight_bg  = "weight",
                                    ))
    return li_TMVAs

def create_setups_topTagCuts_topSize15(li_vars):
    li_TMVAs = []
    for v in li_vars:
        name = "{0}_{1}_{2}_topTagCuts_topSize".format(sample_sig, sample_bkg, v.name)
        name = name.replace("/","_")
        li_TMVAs.append( TMVASetup( name,
                                    v.pretty_name,
                                    li_methods, 
                                    [v],
                                    file_name_sig,
                                    file_name_bg,
                                    fiducial_cut_sig = fiducial_cuts_topSizeCut15[sample_sig],
                                    fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                    weight_sig = "weight",
                                    weight_bg  = "weight",
                                    ))
    return li_TMVAs

# end of create_setups

to_process  = pairs.keys()

for k in to_process:
    print "doing", k
    
    pair_name = k
    pair = pairs[pair_name]
    
    #pair_name = "pt-600-to-800_1p_topSize"
    #pair_name = "pt-300-to-470_1p"
    #pair_name = "pt-1000-to-1400_10p"
    #pair = pairs[pair_name]

    sample_sig = pair[0]
    sample_bkg = pair[1]

    basepath = '/eos/uscms/store/user/camclean/TopTagEfficiency/PHYS14_PU20_BX25/ntop_v20_drOriginal_decayingHadtop_13tev_PU20bx25/'
    file_name_sig  = basepath + files[sample_sig] + "-weighted.root"
    file_name_bg   = basepath + files[sample_bkg] + "-weighted.root"

    li_methods      = ["Cuts"]

    mass_setups_15 = create_setups(mass_vars_15)
    mass_setups_topSize_15 = create_setups_topSize15(mass_vars_15)
    mass_setups_topTagCuts_15 = create_setups_topTagCuts(mass_vars_topTagCuts_15)
    mass_setups_topTagCuts_topSize_15 = create_setups_topTagCuts_topSize15(mass_vars_topTagCuts_15)

    softdrop_mass_setups_15 = create_setups(softdrop_mass_vars_15)
    softdrop_mass_setups_topSize_15 = create_setups_topSize15(softdrop_mass_vars_15)
    softdrop_mass_setups_topTagCuts_15 = create_setups_topTagCuts(softdrop_mass_vars_topTagCuts_15)
    softdrop_mass_setups_topTagCuts_topSize_15 = create_setups_topTagCuts_topSize15(softdrop_mass_vars_topTagCuts_15)

    tau_setups_15  = create_setups(tau_vars_15)
    tau31_setups_15  = create_setups(tau31_vars_15)
    tagger_setups_15 = create_setups(tagger_vars_15)
    all_setups_15 = create_setups(all_vars_15)

    mass_setups_08 = create_setups(mass_vars_08)
    mass_setups_topSize_08 = create_setups_topSize08(mass_vars_08)
    mass_setups_topTagCuts_08 = create_setups_topTagCuts(mass_vars_topTagCuts_08)
    mass_setups_topTagCuts_topSize_08 = create_setups_topTagCuts_topSize08(mass_vars_topTagCuts_08)

    softdrop_mass_setups_08 = create_setups(softdrop_mass_vars_08)
    softdrop_mass_setups_topSize_08 = create_setups_topSize08(softdrop_mass_vars_08)
    softdrop_mass_setups_topTagCuts_08 = create_setups_topTagCuts(softdrop_mass_vars_topTagCuts_08)
    softdrop_mass_setups_topTagCuts_topSize_08 = create_setups_topTagCuts_topSize08(softdrop_mass_vars_topTagCuts_08)

    tau_setups_08  = create_setups(tau_vars_08)
    tau31_setups_08  = create_setups(tau31_vars_08)
    tagger_setups_08 = create_setups(tagger_vars_08)
    all_setups_08 = create_setups(all_vars_08)
    
    btag_setups = create_setups(btag_vars)
    
    good_setups = create_setups(good_vars)
    
    cmstt_setups = create_setups(cmstt_vars)
    sd_setups = create_setups(sd_vars)
    
    all_setups = all_setups_08 + all_setups_15 + btag_setups
    
    mass_setups = mass_setups_08 + mass_setups_15
    tau_setups = tau_setups_08 + tau_setups_15
    tagger_setups = tagger_setups_08 + tagger_setups_15
    
    good_setups_200_300 = create_setups(good_vars_200_300)
    good_setups_470_600 = create_setups(good_vars_470_600)
    good_setups_800_1000 = create_setups(good_vars_800_1000)

    combined_setups_15 = []
    
    combined_setups_15.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "CMSTT15_combined"),
                                        "CMSTT (topMass, minMass) R=1.5",
                                        ["Cuts"], 
                                        [variable('ca15cmstt_topMass', "CMSTT topMass (R=1.5)", 0., 600, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)"),
                                         variable('ca15cmstt_minMass', "CMSTT minMass (R=1.5)", 0., 400, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_setups_15.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca15filtered_mass_minmass"),
                                        "CMSTT (filteredMass, minMass) R=1.5",
                                        ["Cuts"], 
                                        [variable('ca15filtered_mass', "filtered m (R=1.5)", 0, 1000, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)"),
                                         variable('ca15cmstt_minMass', "CMSTT minMass (R=1.5)", 0., 400, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))
    
    combined_setups_15.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca15pruned_mass_minmass"),
                                        "CMSTT (prunedMass, minMass) R=1.5",
                                        ["Cuts"], 
                                        [variable('ca15pruned_mass', "pruned m (z=0.1, r=0.5, R=1.5)", 0, 1000, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)"),
                                         variable('ca15cmstt_minMass', "CMSTT minMass (R=1.5)", 0., 400, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))
    
    combined_setups_15.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca15newpruned_mass_minmass"),
                                        "CMSTT (newprunedMass, minMass) R=1.5",
                                        ["Cuts"], 
                                        [variable('ca15newpruned_mass', "pruned m (z=0.05, r=0.5, R=1.5)", 0, 1000, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)"),
                                         variable('ca15cmstt_minMass', "CMSTT minMass (R=1.5)", 0., 400, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))
    
    combined_setups_15.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca15trimmedr2f3_mass_minmass"),
                                        "CMSTT (trimmedr2f3Mass, minMass) R=1.5",
                                        ["Cuts"], 
                                        [variable('ca15trimmedr2f3_mass', "trimmed m (r=0.2, f=0.03, R=1.5)", 0, 500, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)"),
                                         variable('ca15cmstt_minMass', "CMSTT minMass (R=1.5)", 0., 400, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))
    
    combined_setups_15.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca15trimmedr2f6_mass_minmass"),
                                        "CMSTT (trimmedr2f6Mass, minMass) R=1.5",
                                        ["Cuts"], 
                                        [variable('ca15trimmedr2f6_mass', "trimmed m (r=0.2, f=0.06, R=1.5)", 0, 500, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)"),
                                         variable('ca15cmstt_minMass', "CMSTT minMass (R=1.5)", 0., 400, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))
    
    combined_setups_15.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca15softdropz10b00_mass_minmass"),
                                        "CMSTT (softdropz10b00Mass, minMass) R=1.5",
                                        ["Cuts"], 
                                        [variable('ca15softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=1.5)", 0, 500, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)"),
                                         variable('ca15cmstt_minMass', "CMSTT minMass (R=1.5)", 0., 400, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))
    
    combined_setups_15.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca15softdropz15b20_mass_minmass"),
                                        "CMSTT (softdropz15b20Mass, minMass) R=1.5",
                                        ["Cuts"], 
                                        [variable('ca15softdropz15b20_mass', "softdrop m (z=0.15, #beta=2, R=1.5)", 0, 500, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)"),
                                         variable('ca15cmstt_minMass', "CMSTT minMass (R=1.5)", 0., 400, unit = "GeV",extra_cut = "(ca15cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_setups_08 = []
    '''
    combined_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "CMSTT08_combined"),
                                        "CMSTT (topMass, minMass) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08cmstt_topMass', "CMSTT topMass (R=0.8)", 0., 600, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08filtered_mass_minmass"),
                                        "CMSTT (filteredMass, minMass) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08filtered_mass', "filtered m (R=0.8)", 0, 1000, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08pruned_mass_minmass"),
                                        "CMSTT (prunedMass, minMass) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08pruned_mass', "pruned m (z=0.1, r=0.5, R=0.8)", 0, 1000, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))
    
    combined_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08newpruned_mass_minmass"),
                                        "CMSTT (newprunedMass, minMass) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08newpruned_mass', "pruned m (z=0.05, r=0.5, R=0.8)", 0, 1000, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))
                                        
    combined_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08trimmedr2f3_mass_minmass"),
                                        "CMSTT (trimmedr2f3Mass, minMass) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08trimmedr2f3_mass', "trimmed m (r=0.2, f=0.03, R=0.8)", 0, 500, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))
    
    combined_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08trimmedr2f6_mass_minmass"),
                                        "CMSTT (trimmedr2f6Mass, minMass) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08trimmedr2f6_mass', "trimmed m (r=0.2, f=0.06, R=0.8)", 0, 500, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))
                                        '''
    combined_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz10b00_mass_minmass_nsubjCut"),
                                        "CMSTT (softdropz10b00Mass, minMass, Nsubjets >= 3) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz10b00_mass_minmass"),
                                        "CMSTT (softdropz10b00Mass, minMass) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz10b00_mass_nsubjets_minmassCut"),
                                        "CMSTT (softdropz10b00Mass, Nsubjets, minMass > 50) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV",extra_cut = "(ca08cmstt_minMass > 50)"),
                                         variable('ca08cmstt_nSubJets', "CMSTT Nsubjets (R=0.8)",0 ,6,extra_cut = "(ca08cmstt_minMass > 50)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz10b00_mass_nsubjets"),
                                        "CMSTT (softdropz10b00Mass, Nsubjets) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ca08cmstt_nSubJets', "CMSTT Nsubjets (R=0.8)", 0, 6)], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz10b00_mass_minmass_nsubjets"),
                                        "CMSTT (softdropz10b00Mass, minMass, Nsubjets) R=0.8",
                                        ["Cuts"],
                                        [variable('ca08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV"),
                                         variable('ca08cmstt_nSubJets', "CMSTT Nsubjets (R=0.8)", 0, 6)],
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    '''
    combined_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz15b20_mass_minmass"),
                                        "CMSTT (softdropz15b20Mass, minMass) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08softdropz15b20_mass', "softdrop m (z=0.15, #beta=2, R=0.8)", 0, 500, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))
'''

    combined_softdrop_setups_08 = []

    combined_softdrop_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz10b00_mass_minmass_nsubjCut"),
                                        "CMSTT (softdropz10b00Mass, minMass, Nsubjets >= 3) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_softdrop_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz10b00_mass_minmass"),
                                        "CMSTT (softdropz10b00Mass, minMass) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_softdrop_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz10b00_mass_nsubjets_minmassCut"),
                                        "CMSTT (softdropz10b00Mass, Nsubjets, minMass > 50) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV",extra_cut = "(ca08cmstt_minMass > 50)"),
                                         variable('ca08cmstt_nSubJets', "CMSTT Nsubjets (R=0.8)",0 ,6,extra_cut = "(ca08cmstt_minMass > 50)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_softdrop_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz10b00_mass_nsubjets"),
                                        "CMSTT (softdropz10b00Mass, Nsubjets) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ca08cmstt_nSubJets', "CMSTT Nsubjets (R=0.8)", 0, 6)], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_softdrop_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz10b00_mass_minmass_nsubjets"),
                                        "CMSTT (softdropz10b00Mass, minMass, Nsubjets) R=0.8",
                                        ["Cuts"],
                                        [variable('ca08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV"),
                                         variable('ca08cmstt_nSubJets', "CMSTT Nsubjets (R=0.8)", 0, 6)],
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_softdrop_topSize_setups_08 = []

    combined_softdrop_topSize_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz10b00_mass_minmass_nsubjCut"),
                                        "CMSTT (softdropz10b00Mass, minMass, Nsubjets >= 3) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV",extra_cut = "(ca08cmstt_nSubJets >= 3)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_softdrop_topSize_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz10b00_mass_minmass"),
                                        "CMSTT (softdropz10b00Mass, minMass) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_softdrop_topSize_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz10b00_mass_nsubjets_minmassCut"),
                                        "CMSTT (softdropz10b00Mass, Nsubjets, minMass > 50) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV",extra_cut = "(ca08cmstt_minMass > 50)"),
                                         variable('ca08cmstt_nSubJets', "CMSTT Nsubjets (R=0.8)",0 ,6,extra_cut = "(ca08cmstt_minMass > 50)")], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_softdrop_topSize_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz10b00_mass_nsubjets"),
                                        "CMSTT (softdropz10b00Mass, Nsubjets) R=0.8",
                                        ["Cuts"], 
                                        [variable('ca08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ca08cmstt_nSubJets', "CMSTT Nsubjets (R=0.8)", 0, 6)], 
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))

    combined_softdrop_topSize_setups_08.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "ca08softdropz10b00_mass_minmass_nsubjets"),
                                        "CMSTT (softdropz10b00Mass, minMass, Nsubjets) R=0.8",
                                        ["Cuts"],
                                        [variable('ca08softdropz10b00_mass', "softdrop m (z=0.10, #beta=0, R=0.8)", 0, 500, unit = "GeV"),
                                         variable('ca08cmstt_minMass', "CMSTT minMass (R=0.8)", 0., 400, unit = "GeV"),
                                         variable('ca08cmstt_nSubJets', "CMSTT Nsubjets (R=0.8)", 0, 6)],
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts_topSizeCut08[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))


    combined_setups = []

#combined_setups.append(TMVASetup("{0}_{1}_{2}".format(sample_sig, sample_bkg, "HTT_combined"),
#                                 "HTT (m, f_{W}, #Delta R)",
#                                 ["Cuts"], 
#                                 [variable.di['looseMultiRHTT_mass'],
#                                  variable.di['looseMultiRHTT_fW'],
#                                  variable.di['looseMultiRHTT_Rmin-looseMultiRHTT_RminExpected']],                               
#                                 file_name_sig,
#                                 file_name_bg,
#                                 fiducial_cut_sig = fiducial_cuts[sample_sig],
#                                 fiducial_cut_bg  = fiducial_cuts[sample_bkg],
#                                 weight_sig = "weight",
#                                 weight_bg = "weight"))
#
    
    '''
    combined_setups.append(TMVASetup("{0}_{1}_800_to_1000_mass_tau".format(sample_sig, sample_bkg),
                                        "softdrop m + #tau_{3}/#tau_{2} (R=0.8)",
                                        ["Cuts"], 
                                        [variable.di['ca08softdrop_mass'],
                                         variable.di['ca08_tau3/ca08_tau2']],
                                        file_name_sig,
                                        file_name_bg,
                                        fiducial_cut_sig = fiducial_cuts[sample_sig],
                                        fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                        weight_sig = "weight",
                                        weight_bg = "weight"))


    combined_setups.append(TMVASetup("{0}_{1}_470_to_600_mass_tau".format(sample_sig, sample_bkg),
                                  "trimmed m + #tau_{3}/#tau_{2} (R=0.8)",
                                  ["Cuts"], 
                                  [variable.di['ca08trimmed_mass'],
                                  variable.di['ca08_tau3/ca08_tau2']],
                                  file_name_sig,
                                  file_name_bg,
                                  fiducial_cut_sig = fiducial_cuts[sample_sig],
                                  fiducial_cut_bg  = fiducial_cuts[sample_bkg],
                                  weight_sig = "weight",
                                  weight_bg = "weight"))


#combined_setups.append(TMVASetup("{0}_{1}_200_to_300_mass_tau".format(sample_sig, sample_bkg),
#                                  "trimmed m + #tau_{3}/#tau_{2} (R=1.5)",
#                                  ["Cuts"], 
#                                 [variable.di['ca15trimmed_mass'],
#                                  variable.di['ca15_tau3/ca15_tau2']],
#                                  file_name_sig,
#                                  file_name_bg,
#                                  fiducial_cut_sig = fiducial_cuts[sample_sig],
#                                  fiducial_cut_bg  = fiducial_cuts[sample_bkg],
#                                  weight_sig = "weight",
#                                  weight_bg = "weight"))
#

#combined_setups.append(TMVASetup("{0}_{1}_200_to_300_mass_tau_qvol".format(sample_sig, sample_bkg),
#                                  "trimmed m + #tau_{3}/#tau_{2} + Q-vol (R=1.5)",
#                                  ["Cuts"], 
#                                 [variable.di['ca15trimmed_mass'],
#                                  variable.di['ca15_tau3/ca15_tau2'],
#                                  variable.di['ca15_qvol'],
#                              ],
#                                 file_name_sig,
#                                 file_name_bg,
#                                 fiducial_cut_sig = fiducial_cuts[sample_sig],
#                                 fiducial_cut_bg  = fiducial_cuts[sample_bkg],
#                                 weight_sig = "weight",
#                                 weight_bg = "weight"))
#




#combined_setups.append(TMVASetup("08_combined",
#                                 "softdrop m + #tau_{3}/#tau_{2} (R=0.8)",
#                                 ["Cuts"], 
#                                 [variable.di['ca08_tau3/ca08_tau2'],
#                                  variable.di['ca08softdrop_mass']],
#                                 file_name_sig,
#                                 file_name_bg,
#                                 fiducial_cut_sig = fiducial_cuts[sample_sig],
#                                 fiducial_cut_bg  = fiducial_cuts[sample_bkg],
#                                 weight_sig = "weight",
#                                 weight_bg = "weight"))
#


    with_btag_setups = []
    for setup in combined_setups:
        new_setup = deepcopy(setup)

        new_setup.name = setup.name + "_btag"
        new_setup.li_methods = ["Cuts"]
        new_setup.li_vars.append(variable.di['ca08_btag'])
        
        with_btag_setups.append(new_setup)

        '''
    if run_TMVA:
        '''for setup in combined_setups_15:
            doTMVA(setup)
        plotROCMultiple("ROC_mass15_minmass_" + pair_name + "_1p", combined_setups_15)
        '''
        #for setup in combined_setups_08:
        #    doTMVA(setup)
        #plotROCMultiple("ROC_mass08_minmass_" + pair_name + "_1p", combined_setups_08)
        #for setup in softdrop_mass_setups_08:
        #    doTMVA(setup)
        #for setup in softdrop_mass_setups_topTagCuts_08:
        #    doTMVA(setup)
        '''
        for setup in mass_setups_topTagCuts_15:
            doTMVA(setup)
        plotROCMultiple("ROC_mass15_topTagCuts_" + pair_name + "_1p", mass_setups_topTagCuts_15)
        for setup in mass_setups_topTagCuts_08:
             doTMVA(setup)
        for setup in mass_setups_std_15:
            doTMVA(setup)
        for setup in mass_setups_std_08:
            doTMVA(setup)

#plotROCMultiple("ROC_good", [setup_08_combined, setup_cmstt_combined, setup_htt_combined] + good_setups + btag_setups)

#plotROCMultiple("ROC_mass", mass_setups)
#plotROCMultiple("ROC_tau", tau_setups)
#plotROCMultiple("ROC_tagger", tagger_setups + [setup_htt_combined, setup_cmstt_combined])
#
#plotROCMultiple("ROC_good", [setup_08_combined, setup_htt_combined, setup_cmstt_combined]+good_setups + btag_setups)
#plotROCMultiple("ROC_withb", combined_setups + with_btag_setups)
#plotROCMultiple("ROC_" + pair_name, good_setups_200_300 + combined_setups)
#plotROCMultiple("ROC_" + pair_name, good_setups_470_600 + combined_setups)
#plotROCMultiple("ROC_sd_" + pair_name, sd_setups)
        plotROCMultiple("ROC_mass08_topTagCuts_" + pair_name, mass_setups_topTagCuts_08)
        plotROCMultiple("ROC_mass15_std_" + pair_name, mass_setups_std_15)
        plotROCMultiple("ROC_mass08_std_" + pair_name, mass_setups_std_08)
        '''
    plotROCMultiple("ROC_softdropz10b00_mass08_" + pair_name, combined_setups_08 + softdrop_mass_setups_08 + softdrop_mass_setups_topTagCuts_08)
