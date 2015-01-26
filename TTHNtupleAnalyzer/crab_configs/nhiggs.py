"""Manage ntuples for higgs-tagging (nhiggs)"""

#######################################
# Imports
######################################

import sys

from TTH.TTHNtupleAnalyzer.CrabHelpers import submit, status, kill, download, hadd


#######################################
# Configuration
#####################################

# Ntuple name/version and samples to include
name = "nhiggs"
version = "v4"
li_samples = [
#    "tth_hbb_13tev",
    "ttj_13tev"
]

cmssw_config_path = '/shome/gregor/TTH-73X/CMSSW/src/TTH/TTHNtupleAnalyzer/python/'
config_script_name = 'HiggsTaggers_cfg.py'
storage_path = '/scratch/gregor/'

#######################################
# Actual work
#####################################

# Decide what to do
actions = ["submit", "status", "kill", "download", "hadd"]

if not len(sys.argv) == 2:
    print "Invalid number of arguments"
    print "Usage: {0} {1}".format(sys.argv[0], "/".join(actions))
    sys.exit()

action = sys.argv[1]

if not action in actions:
    print "Invalid action"
    print "Usage: {0} {1}".format(sys.argv[0], "/".join(actions))
    sys.exit()

# Submit
if action == "submit":
    for sample_shortname in li_samples:
        submit(name,
               sample_shortname,  
               version,
               cmssw_config_path = cmssw_config_path,
               cmssw_config_script = config_script_name,
               blacklist = ["T1_US_FNAL"])

# Status
if action == "status":
    for sample_shortname in li_samples:
        status(name,
               sample_shortname,  
               version)

# Kill
if action == "kill":
    for sample_shortname in li_samples:
        kill(name,
               sample_shortname,  
               version)

# Download
elif action == "download":
    for sample_shortname in li_samples:
        download(name, sample_shortname, version, storage_path)    

# Hadd
elif action == "hadd":
    for sample_shortname in li_samples:
        hadd(name, sample_shortname, version, storage_path, "output_*.root", "")    

