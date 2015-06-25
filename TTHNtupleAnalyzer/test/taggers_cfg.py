#a simple test config to run on a ttbar sample
#used for scram b runtests (automatic testing)
from TTH.TTHNtupleAnalyzer.Taggers_cfg import *

process.source.fileNames = cms.untracked.vstring([
        
        #'/store/mc/Spring14miniaod/ZPrimeToTTJets_M3000GeV_W300GeV_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/141029_PU40bx50_PLS170_V6AN2-v1/20000/4C8962B1-0562-E411-A372-008CFA064778.root',
        #'/store/user/chmclean/ZPrimeToTTJets_M3000GeV_W30GeV_Tune4C_13TeV-madgraph-tauola/miniAOD_ZPrimeToTTJets_M3000GeV_W30GeV_11_24_2014/92bfc1aa0ef8c674e0edabb945b19298/miniAOD-prod_PAT_100_1_PVX.root',
        #'/store/mc/Spring14miniaod/ZPrimeToTTJets_M3000GeV_W30GeV_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/141029_PU40bx50_PLS170_V6AN2-v1/20000/7ADFFAC4-0762-E411-AA40-001E6739BB01.root',
        '/store/mc/Phys14DR/ZPrimeToTTJets_M3000GeV_W30GeV_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/746BDDDC-3568-E411-BAA1-3417EBE2F0DF.root'
        #'/store/mc/Phys14DR/ZPrimeToTTJets_M1000GeV_W100GeV_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0A8831C7-8D6F-E411-A892-0025904B130A.root'
        #'/store/user/chmclean/ZPrimeToTTJets_M3000GeV_W30GeV_Tune4C_13TeV-madgraph-tauola/miniAOD_ZPrimeToTTJets_M3000GeV_W30GeV_11_24_2014/92bfc1aa0ef8c674e0edabb945b19298/miniAOD-prod_PAT_100_1_PVX.root'
#    'file:///scratch/gregor/TTbarH_HToBB_M-125_13TeV_pythia6_MiniAOD.root',
#    'file:///scratch/gregor/TTJets_MSDecaysCKM_central_Tune4C_13TeV_MiniAOD.root'
#    'file:///scratch/gregor/Phys14DR_ZPrimeToTTJets_M2000GeV_W20GeV_Tune4C_13TeV.root'
#    'file:///scratch/gregor/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8.root'
#     'file:///scratch/gregor/QCD_Pt-300to470_TuneZ2star_13TeV_pythia6.root'
])

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(50) )
#process.TFileService.fileName = "ttbar_step1_decayingHadtops_PHYS14_ZPrime_M3000GeV_W30GeV_4_13_2015.root"
process.TFileService.fileName = "crab_ntop_v25_topSize_drOriginal_decayingHadtop_zprime_m3000_1p_13tev_PU20bx25_output_1_bTagNoPUPPI.root"
