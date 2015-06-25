import socket # to get the hostname

'''
if socket.gethostname() == "t3ui12":
    basepath = '/scratch/gregor/'
else:
    basepath = '/Users/gregor/'
'''

basepath = '/eos/uscms/store/user/camclean/TopTagEfficiency/Spring15/'

files = {}

#files["zprime_m750"]      = "ntop_v18a_zprime_m750_1p_13tev-tagging"     
#files["zprime_m1000_1p"]     = "ntop_v20_drOriginal_decayingHadtop_zprime_m1000_1p_13tev_PU20bx25-tagging"     
#files["zprime_m1250"]     = "ntop_v18a_zprime_m1250_1p_13tev-tagging"     
#files["zprime_m2000_low"] = "ntop_v18_zprime_m2000_low_1p_13tev-tagging"     
#files["zprime_m2000_1p"]     = "ntop_v20_drOriginal_decayingHadtop_zprime_m2000_1p_13tev_PU20bx25-tagging"     
#files["zprime_m2000_10p"]     = "ntop_v20_drOriginal_decayingHadtop_zprime_m2000_10p_13tev_PU20bx25-tagging"
#files["zprime_m3000_1p"]     = "ntop_v20_drOriginal_decayingHadtop_zprime_m3000_1p_13tev_PU20bx25-tagging"     
#files["zprime_m3000_10p"]     = "ntop_v20_drOriginal_decayingHadtop_zprime_m3000_10p_13tev_PU20bx25-tagging"     
#files["zprime_m4000"]     = "ntop_v18b_zprime_m4000_1p_13tev-tagging"     

#files["zprime_m1000_1p_topSize"]     = "ntop_v28_topSize_drOriginal_decayingHadtop_zprime_m1000_1p_13tev_PU20bx25-tagging"     
#files["zprime_m1000_10p_topSize"]     = "ntop_v28_topSize_drOriginal_decayingHadtop_zprime_m1000_10p_13tev_PU20bx25-tagging"     
#files["zprime_m2000_low_1p_topSize"]     = "ntop_v28_topSize_drOriginal_decayingHadtop_zprime_m2000_low_1p_13tev_PU20bx25-tagging"     
#files["zprime_m2000_low_10p_topSize"]     = "ntop_v28_topSize_drOriginal_decayingHadtop_zprime_m2000_low_10p_13tev_PU20bx25-tagging"
#files["zprime_m2000_1p_topSize"]     = "ntop_v28_topSize_drOriginal_decayingHadtop_zprime_m2000_1p_13tev_PU20bx25-tagging"     
#files["zprime_m2000_10p_topSize"]     = "ntop_v28_topSize_drOriginal_decayingHadtop_zprime_m2000_10p_13tev_PU20bx25-tagging"
#files["zprime_m3000_1p_topSize"]     = "ntop_v28_topSize_drOriginal_decayingHadtop_zprime_m3000_1p_13tev_PU20bx25-tagging"     
#files["zprime_m3000_10p_topSize"]     = "ntop_v28_topSize_drOriginal_decayingHadtop_zprime_m3000_10p_13tev_PU20bx25-tagging"     

#files["qcd_300_470_topSize"] = "ntop_v28_topSize_drOriginal_decayingHadtop_qcd_pt_300_470_13tev_PU20bx25-tagging"
#files["qcd_470_600_topSize"] = "ntop_v28_topSize_drOriginal_decayingHadtop_qcd_pt_470_600_13tev_PU20bx25-tagging"
#files["qcd_600_800_topSize"] = "ntop_v28_topSize_drOriginal_decayingHadtop_qcd_pt_600_800_13tev_PU20bx25-tagging"
#files["qcd_800_1000_topSize"] = "ntop_v28_topSize_drOriginal_decayingHadtop_qcd_pt_800_1000_13tev_PU20bx25-tagging"
#files["qcd_1000_1400_topSize"] = "ntop_v28_topSize_drOriginal_decayingHadtop_qcd_pt_1000_1400_13tev_PU20bx25-tagging"

#files["qcd_170_300"] = "ntop_v18a_qcd_170_300_pythia8_13tev-tagging"
#files["qcd_300_470"] = "ntop_v20_drOriginal_decayingHadtop_qcd_pt_300_470_13tev_PU20bx25-tagging"
#files["qcd_470_600"] = "ntop_v20_drOriginal_decayingHadtop_qcd_470_600_pythia8_13tev-tagging"
#files["qcd_600_800"] = "ntop_v23_topSize_drOriginal_decayingHadtop_qcd_pt_600_800_13tev_PU20bx25-tagging"
#files["qcd_800_1000"] = "ntop_v20_drOriginal_decayingHadtop_qcd_pt_800_1000_13tev_PU20bx25-tagging"

#files["zprime_m750"]  = "ntop_v20_zprime_m750_1p_13tev-tagging"     
#files["zprime_m1250"] = "ntop_v20_zprime_m1250_1p_13tev-tagging"     
#files["zprime_m2000"] = "ntop_v8_zprime_m2000_1p_13tev-tagging"     
#files["qcd_170_300"]  = "ntop_v20_qcd_170_300_pythia8_13tev-tagging"
#files["qcd_470_600"]  = "ntop_v20_qcd_470_600_pythia8_13tev-tagging"
#files["qcd_800_1000"] = "ntop_v8_qcd_800_1000_pythia8_13tev-tagging"
#files["qcd_1000_1400"] = "ntop_v20_drOriginal_decayingHadtop_qcd_pt_1000_1400_13tev_PU20bx25-tagging"

files["zprime_m1250_1p_Spring15"]     = "ntop_v55_zprime_m1250_1p_13tev_spring15dr74_asympt25ns-tagging"     
files["zprime_m2000_low_1p_Spring15"]     = "ntop_v55_zprime_m2000_low_1p_13tev_spring15dr74_asympt25ns-tagging"     
files["zprime_m2000_1p_Spring15"]     = "ntop_v55_zprime_m2000_1p_13tev_spring15dr74_asympt25ns-tagging"     
files["zprime_m3000_1p_Spring15"]     = "ntop_v55_zprime_m3000_1p_13tev_spring15dr74_asympt25ns-tagging"     

files["qcd_470_600_Spring15"] = "ntop_v55_qcd_470_600_13tev_spring15dr74_asympt25ns-tagging"
files["qcd_600_800_Spring15"] = "ntop_v55_qcd_600_800_13tev_spring15dr74_asympt25ns-tagging"
files["qcd_800_1000_Spring15"] = "ntop_v55_qcd_800_1000_13tev_spring15dr74_asympt25ns-tagging"
files["qcd_1000_1400_Spring15"] = "ntop_v55_qcd_1000_1400_13tev_spring15dr74_asympt25ns-tagging"

weighted_files = {}
for k,v in files.iteritems():
    weighted_files[k] = basepath + v + "-weighted.root"
    print weighted_files[k]

pairs = { 
    #"pt-200-to-300" : ["zprime_m750", "qcd_170_300"],
    #"pt-300-to-470_1p"  : ["zprime_m1000_1p","qcd_300_470"],
    #"pt-470-to-600" : ["zprime_m1250", "qcd_470_600"],
    #"pt-800-to-1000_1p" : ["zprime_m2000_1p", "qcd_800_1000"],
    #"pt-800-to-1000_10p" : ["zprime_m2000_10p", "qcd_800_1000"],  
    #"pt-1000-to-1400_1p" : ["zprime_m3000_1p", "qcd_1000_1400"],
    #"pt-1000-to-1400_10p" : ["zprime_m3000_10p", "qcd_1000_1400"],  

    #"pt-300-to-470_1p_topSize"  : ["zprime_m1000_1p_topSize","qcd_300_470_topSize"],
    #"pt-300-to-470_10p_topSize"  : ["zprime_m1000_10p_topSize","qcd_300_470_topSize"],
    #"pt-600-to-800_1p_topSize" : ["zprime_m2000_low_1p_topSize", "qcd_600_800_topSize"],
    #"pt-600-to-800_10p_topSize" : ["zprime_m2000_low_10p_topSize", "qcd_600_800_topSize"],
    #"pt-800-to-1000_1p_topSize" : ["zprime_m2000_1p_topSize", "qcd_800_1000_topSize"],
    #"pt-800-to-1000_10p_topSize" : ["zprime_m2000_10p_topSize", "qcd_800_1000_topSize"],  
    #"pt-1000-to-1400_1p_topSize" : ["zprime_m3000_1p_topSize", "qcd_1000_1400_topSize"],
    #"pt-1000-to-1400_10p_topSize" : ["zprime_m3000_10p_topSize", "qcd_1000_1400_topSize"],  

    "pt-470-to-600_Spring15" : ["zprime_m1250_1p_Spring15", "qcd_470_600_Spring15"],
    "pt-600-to-800_Spring15" : ["zprime_m2000_low_1p_Spring15","qcd_600_800_Spring15"],
    "pt-800-to-1000_1p_Spring15" : ["zprime_m2000_1p_Spring15", "qcd_800_1000_Spring15"],
    "pt-1000-to-1400_1p_Spring15" : ["zprime_m3000_1p_Spring15", "qcd_1000_1400_Spring15"],
    }

# [Minimal pT, Maximal pT, |eta|]
ranges = {
        #"zprime_m750"      : [201, 299],
        #"zprime_m1000_1p"     : [301, 469],
        #"zprime_m1250"     : [471, 599], 
        #"zprime_m2000_low" : [601, 799],
        #"zprime_m2000_1p"     : [801, 999],
        #"zprime_m2000_10p"     : [801, 999],
        #"zprime_m3000_1p"     : [1001, 1399], 
        #"zprime_m3000_10p"     : [1001, 1399],
        #"zprime_m4000"     : [1401, 1799],

        #"zprime_m1000_1p_topSize"     : [301, 469,   2.4, 0.8, "ca15"],
        #"zprime_m1000_10p_topSize"     : [301, 469,   2.4, 0.8, "ca15"],
        #"zprime_m2000_low_1p_topSize" : [601, 799,   2.1, 0.6, "ca08"],
        #"zprime_m2000_low_10p_topSize" : [601, 799,   2.1, 0.6, "ca08"],
        #"zprime_m2000_1p_topSize"     : [801, 999,   1.5, 0.6, "ca08"],
        #"zprime_m2000_10p_topSize"     : [801, 999,   1.5, 0.6, "ca08"],
        #"zprime_m3000_1p_topSize"     : [1001, 1399,  1.5, 0.6, "ca08"], 
        #"zprime_m3000_10p_topSize"     : [1001, 1399, 1.5, 0.6, "ca08"],

        #"qcd_170_300_topSize"      : [201, 299, 2.4, 0.8, "ca15"],
        #"qcd_300_470_topSize"      : [301, 469, 2.4, 0.8, "ca15"],
        #"qcd_470_600_topSize"      : [471, 599, 2.1, 0.6, "ca08"],
        #"qcd_600_800_topSize"      : [601,799,   2.1, 0.6, "ca08"],  
        #"qcd_800_1000_topSize"     : [801, 999,   1.5, 0.6, "ca08"],
        #"qcd_1000_1400_topSize"    : [1001, 1399, 1.5, 0.6, "ca08"],

        "zprime_m1250_1p_Spring15"     : [471, 599, 2.1, 0.6, "ak08"],
        "zprime_m2000_low_1p_Spring15" : [601, 799,   2.1, 0.6, "ak08"],
        "zprime_m2000_1p_Spring15"     : [801, 999,   1.5, 0.6, "ak08"],
        "zprime_m3000_1p_Spring15"     : [1001, 1399,  1.5, 0.6, "ak08"], 
        
        "qcd_470_600_Spring15"      : [471, 599, 2.1, 0.6, "ak08"],
        "qcd_600_800_Spring15"      : [601,799,   2.1, 0.6, "ak08"],  
        "qcd_800_1000_Spring15"     : [801, 999,   1.5, 0.6, "ak08"],
        "qcd_1000_1400_Spring15"    : [1001, 1399, 1.5, 0.6, "ak08"],
        }


#top size = min delta R between true top and its constituents
topSizeCut08 = 0.6 #CA (R = 0.8)
topSizeCut15 = 0.8 #CA (R = 1.5)
fiducial_cuts = {}
fiducial_cuts_topSizeCut08 = {}
fiducial_cuts_topSizeCut15 = {}
for k,v in ranges.iteritems():
    fiducial_cuts[k] = "((pt>{0})&&(pt<{1})&&(fabs(eta)<{2}))".format(v[0], v[1], v[2])
    fiducial_cuts_topSizeCut08[k] = "((pt>{0})&&(pt<{1})&&(fabs(eta)<{2})&&(top_size<{3}))".format(v[0], v[1], v[2], v[3])
    fiducial_cuts_topSizeCut15[k] = "((pt>{0})&&(pt<{1})&&(fabs(eta)<{2})&&(top_size<{3}))".format(v[0], v[1], v[2], v[3])
    
    #print "Standard fiducial cuts:", fiducial_cuts[k]
    #print "CA08 top size fiducial cuts:", fiducial_cuts_topSizeCut08[k]
    #print "CA15 top size fiducial cuts:", fiducial_cuts_topSizeCut15[k]
    
    
