# Tagger_cfg.py
# cmsRun configuration file for producing NTuples for Top & Higgs-Tagging Studies

import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing
import os
import sys
import socket

hostname = socket.gethostname()

options = VarParsing('analysis')
options.register ('skipEvents',
	0,
	VarParsing.multiplicity.singleton,
	VarParsing.varType.int,
	"Skip this number of events"
)

process = cms.Process("Demo")

# Necessary so we can import HiggsTaggers_cfg.py from ordinary python
# scripts and extract the fatjets
try:
   options.parseArguments()
except:
   pass

# Load some standard configuration files
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("RecoBTag.Configuration.RecoBTag_cff") # this loads all available b-taggers

# Load the necessary conditions 
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')


#enable debugging printout
if "TTH_DEBUG" in os.environ:
	process.load("FWCore.MessageLogger.MessageLogger_cfi")
	process.MessageLogger = cms.Service("MessageLogger",
		   destinations=cms.untracked.vstring('cout', 'debug'),
		   debugModules=cms.untracked.vstring('*'),
		   cout=cms.untracked.PSet(threshold=cms.untracked.string('INFO')),
		   debug=cms.untracked.PSet(threshold=cms.untracked.string('DEBUG')),

	)
else:
	process.load("FWCore.MessageService.MessageLogger_cfi")
	process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

process.source = cms.Source("PoolSource",
	# replace 'myfile.root' with the source file you want to use
	fileNames = cms.untracked.vstring([]),
	skipEvents = cms.untracked.uint32(options.skipEvents)
)


#####################################
# CHS + PUPPI
#####################################

from CommonTools.PileupAlgos.Puppi_cff import puppi
process.puppi = puppi
process.puppi.candName= cms.InputTag('packedPFCandidates')
process.puppi.vertexName= cms.InputTag('offlineSlimmedPrimaryVertices')


# Select candidates that would pass CHS requirements
# This can be used as input for HTT and other jet clustering algorithms
process.chs = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedPFCandidates"), cut = cms.string("fromPV"))


#####################################
# Ungroomed Fatjets
#####################################

from RecoJets.JetProducers.AnomalousCellParameters_cfi import *
from RecoJets.JetProducers.PFJetParameters_cfi import *
from RecoJets.JetProducers.CATopJetParameters_cfi import *

# Setup fatjet collections to store
li_fatjets_objects       = []
li_fatjets_branches      = []
li_ungroomed_fatjets_objects  = []
li_ungroomed_fatjets_branches = []

# First create the ungroomed fatjet collections
# These are the ones that get all the groomers applied to later on

# CA, R=0.8, pT > 200 GeV
fj_name = "ca08PFJetsCHS"
branch_name = 'ca08'
setattr(process, fj_name, cms.EDProducer(
        "FastjetJetProducer",
        PFJetParameters,
        AnomalousCellParameters,
        jetAlgorithm = cms.string("CambridgeAachen"),
        rParam       = cms.double(0.8),
        #useExplicitGhosts = cms.bool(True),
        #writeCompound = cms.bool(True),
        #jetCollInstanceName=cms.string("SubJets"),
   ))
getattr(process, fj_name).src = cms.InputTag("chs")
getattr(process, fj_name).jetPtMin = cms.double(200)
li_fatjets_objects.append(fj_name)
li_fatjets_branches.append(branch_name)
li_ungroomed_fatjets_objects.append(fj_name)
li_ungroomed_fatjets_branches.append(branch_name)

# CA, R=1.5, pT > 200 GeV
fj_name = "ca15PFJetsCHS"
branch_name = 'ca15'
setattr(process, fj_name, cms.EDProducer(
        "FastjetJetProducer",
        PFJetParameters,
        AnomalousCellParameters,
        jetAlgorithm = cms.string("CambridgeAachen"),
        rParam       = cms.double(1.5),
        #useExplicitGhosts = cms.bool(True),
        #writeCompound = cms.bool(True),
        #jetCollInstanceName=cms.string("SubJets"),
   ))
getattr(process, fj_name).src = cms.InputTag("chs")
getattr(process, fj_name).jetPtMin = cms.double(200)
li_fatjets_objects.append(fj_name)
li_fatjets_branches.append(branch_name)
li_ungroomed_fatjets_objects.append(fj_name)
li_ungroomed_fatjets_branches.append(branch_name)

'''# PUPPI: CA, R=0.8, pT > 200 GeV
fj_name = "ca08PFJetsPUPPI"
branch_name = 'ca08puppi'
setattr(process, fj_name, cms.EDProducer(
        "FastjetJetProducer",
        PFJetParameters,
        AnomalousCellParameters,
        jetAlgorithm = cms.string("CambridgeAachen"),
        rParam       = cms.double(0.8),
        #useExplicitGhosts = cms.bool(True),
        #writeCompound = cms.bool(True),
        #jetCollInstanceName=cms.string("SubJets"),
   ))
getattr(process, fj_name).src = cms.InputTag("puppi")
getattr(process, fj_name).jetPtMin = cms.double(200)
li_fatjets_objects.append(fj_name)
li_fatjets_branches.append(branch_name)
li_ungroomed_fatjets_objects.append(fj_name)
li_ungroomed_fatjets_branches.append(branch_name)

# PUPPI: CA, R=1.5, pT > 200 GeV
fj_name = "ca15PFJetsPUPPI"
branch_name = 'ca15puppi'
setattr(process, fj_name, cms.EDProducer(
        "FastjetJetProducer",
        PFJetParameters,
        AnomalousCellParameters,
        jetAlgorithm = cms.string("CambridgeAachen"),
        rParam       = cms.double(1.5),
        #useExplicitGhosts = cms.bool(True),
        #writeCompound = cms.bool(True),
        #jetCollInstanceName=cms.string("SubJets"),
   ))
getattr(process, fj_name).src = cms.InputTag("puppi")
getattr(process, fj_name).jetPtMin = cms.double(200)
li_fatjets_objects.append(fj_name)
li_fatjets_branches.append(branch_name)
li_ungroomed_fatjets_objects.append(fj_name)
li_ungroomed_fatjets_branches.append(branch_name)
'''
fj_name = "ca08PFJetsCHSforbtag"
branch_name = 'ca08forbtag'
setattr(process, fj_name, cms.EDProducer(
        "FastjetJetProducer",
        PFJetParameters,
        AnomalousCellParameters,
        jetAlgorithm = cms.string("CambridgeAachen"),
        rParam       = cms.double(0.8),
        useExplicitGhosts = cms.bool(True),
        writeCompound = cms.bool(True),
        jetCollInstanceName=cms.string("SubJets"),
   ))
getattr(process, fj_name).src = cms.InputTag("chs")
getattr(process, fj_name).jetPtMin = cms.double(200)
li_fatjets_objects.append(fj_name)
li_fatjets_branches.append(branch_name)
li_ungroomed_fatjets_objects.append(fj_name)
li_ungroomed_fatjets_branches.append(branch_name)

# CA, R=1.5, pT > 200 GeV
fj_name = "ca15PFJetsCHSforbtag"
branch_name = 'ca15forbtag'
setattr(process, fj_name, cms.EDProducer(
        "FastjetJetProducer",
        PFJetParameters,
        AnomalousCellParameters,
        jetAlgorithm = cms.string("CambridgeAachen"),
        rParam       = cms.double(1.5),
        useExplicitGhosts = cms.bool(True),
        writeCompound = cms.bool(True),
        jetCollInstanceName=cms.string("SubJets"),
   ))
getattr(process, fj_name).src = cms.InputTag("chs")
getattr(process, fj_name).jetPtMin = cms.double(200)
li_fatjets_objects.append(fj_name)
li_fatjets_branches.append(branch_name)
li_ungroomed_fatjets_objects.append(fj_name)
li_ungroomed_fatjets_branches.append(branch_name)

'''# PUPPI: CA, R=0.8, pT > 200 GeV
fj_name = "ca08PFJetsPUPPIforbtag"
branch_name = 'ca08puppiforbtag'
setattr(process, fj_name, cms.EDProducer(
        "FastjetJetProducer",
        PFJetParameters,
        AnomalousCellParameters,
        jetAlgorithm = cms.string("CambridgeAachen"),
        rParam       = cms.double(0.8),
        useExplicitGhosts = cms.bool(True),
        writeCompound = cms.bool(True),
        jetCollInstanceName=cms.string("SubJets"),
   ))
getattr(process, fj_name).src = cms.InputTag("puppi")
getattr(process, fj_name).jetPtMin = cms.double(200)
li_fatjets_objects.append(fj_name)
li_fatjets_branches.append(branch_name)
li_ungroomed_fatjets_objects.append(fj_name)
li_ungroomed_fatjets_branches.append(branch_name)

# PUPPI: CA, R=1.5, pT > 200 GeV
fj_name = "ca15PFJetsPUPPIforbtag"
branch_name = 'ca15puppiforbtag'
setattr(process, fj_name, cms.EDProducer(
        "FastjetJetProducer",
        PFJetParameters,
        AnomalousCellParameters,
        jetAlgorithm = cms.string("CambridgeAachen"),
        rParam       = cms.double(1.5),
        useExplicitGhosts = cms.bool(True),
        writeCompound = cms.bool(True),
        jetCollInstanceName=cms.string("SubJets"),
   ))
getattr(process, fj_name).src = cms.InputTag("puppi")
getattr(process, fj_name).jetPtMin = cms.double(200)
li_fatjets_objects.append(fj_name)
li_fatjets_branches.append(branch_name)
li_ungroomed_fatjets_objects.append(fj_name)
li_ungroomed_fatjets_branches.append(branch_name)
'''
process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck")

#####################################
# Groomed Fatjets
#####################################

for ungroomed_fj_name, ungroomed_branch_name in zip(li_ungroomed_fatjets_objects,
                                            li_ungroomed_fatjets_branches):

   ungroomed_fj = getattr(process, ungroomed_fj_name)

   name = 'filtered'
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
         useFiltering = cms.bool(True),
         nFilt = cms.int32(3),
         rFilt = cms.double(0.3),
         #useExplicitGhosts = cms.bool(True),
         #writeCompound = cms.bool(True),
         #jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)
   li_fatjets_branches.append(branch_name)
   
   name = 'pruned'
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
         cms.PSet(nFilt = cms.int32(99),
                  zcut = cms.double(0.1),
                  rcut_factor = cms.double(0.5)),
         usePruning = cms.bool(True),
         #useExplicitGhosts = cms.bool(True),
         #writeCompound = cms.bool(True),
         #jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)
   li_fatjets_branches.append(branch_name)
   
   name = 'newpruned'
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
      cms.PSet(nFilt = cms.int32(99),
               zcut = cms.double(0.05),
               rcut_factor = cms.double(0.5)),
      usePruning = cms.bool(True),
      #useExplicitGhosts = cms.bool(True),
      #writeCompound = cms.bool(True),
      #jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)
   li_fatjets_branches.append(branch_name)

   '''name = "trimmedr2f6forbtag"   
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
      useTrimming = cms.bool(True),
      rFilt = cms.double(0.2),
      trimPtFracMin = cms.double(0.06),
      useExplicitGhosts = cms.bool(True),
      writeCompound = cms.bool(True),
      jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)        
   li_fatjets_branches.append(branch_name)
   '''

   name = "trimmedr2f3"   
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
      useTrimming = cms.bool(True),
      rFilt = cms.double(0.2),
      trimPtFracMin = cms.double(0.03),
      #useExplicitGhosts = cms.bool(True),
      #writeCompound = cms.bool(True),
      #jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)        
   li_fatjets_branches.append(branch_name)

   name = "trimmedr2f6"   
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
      useTrimming = cms.bool(True),
      rFilt = cms.double(0.2),
      trimPtFracMin = cms.double(0.06),
      #useExplicitGhosts = cms.bool(True),
      #writeCompound = cms.bool(True),
      #jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)        
   li_fatjets_branches.append(branch_name)

   name = "trimmedr2f10"   
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
      useTrimming = cms.bool(True),
      rFilt = cms.double(0.2),
      trimPtFracMin = cms.double(0.1),
      #useExplicitGhosts = cms.bool(True),
      #writeCompound = cms.bool(True),
      #jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)        
   li_fatjets_branches.append(branch_name)

   name = "softdropz10b00"   
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
           useSoftDrop = cms.bool(True),
           zcut = cms.double(0.1),
           beta = cms.double(0.0),
           #useExplicitGhosts = cms.bool(True),
           #writeCompound = cms.bool(True),
           #jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)        
   li_fatjets_branches.append(branch_name)

   '''name = "softdropz10b10"
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
         useSoftDrop = cms.bool(True),
         zcut = cms.double(0.1),
         beta = cms.double(1.0),
         #useExplicitGhosts = cms.bool(True),
         #writeCompound = cms.bool(True),
         #jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)
   li_fatjets_branches.append(branch_name)
   
   name= "softdropz10b20"
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
         useSoftDrop = cms.bool(True),
         zcut = cms.double(0.1),
         beta = cms.double(2.0),
         #useExplicitGhosts = cms.bool(True),
         #writeCompound = cms.bool(True),
         #jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)
   li_fatjets_branches.append(branch_name)
   
   name = "softdropz15b00"   
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
           useSoftDrop = cms.bool(True),
           zcut = cms.double(0.15),
           beta = cms.double(0.0),
           #useExplicitGhosts = cms.bool(True),
           #writeCompound = cms.bool(True),
           #jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)        
   li_fatjets_branches.append(branch_name)
   '''
   name = "softdropz15b10"   
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
           useSoftDrop = cms.bool(True),
           zcut = cms.double(0.15),
           beta = cms.double(1.0),
           #useExplicitGhosts = cms.bool(True),
           #writeCompound = cms.bool(True),
           #jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)        
   li_fatjets_branches.append(branch_name)

   '''name = "softdropz15b20"   
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
           useSoftDrop = cms.bool(True),
           zcut = cms.double(0.15),
           beta = cms.double(2.0),
           #useExplicitGhosts = cms.bool(True),
           #writeCompound = cms.bool(True),
           #jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)        
   li_fatjets_branches.append(branch_name)

   name = "softdropz20b00"   
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
           useSoftDrop = cms.bool(True),
           zcut = cms.double(0.2),
           beta = cms.double(0.0),
           #useExplicitGhosts = cms.bool(True),
           #writeCompound = cms.bool(True),
           #jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)        
   li_fatjets_branches.append(branch_name)

   name = "softdropz20b10"
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
         useSoftDrop = cms.bool(True),
         zcut = cms.double(0.2),
         beta = cms.double(1.0),
         #useExplicitGhosts = cms.bool(True),
         #writeCompound = cms.bool(True),
         #jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)
   li_fatjets_branches.append(branch_name)
   
   name= "softdropz20b20"
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
         useSoftDrop = cms.bool(True),
         zcut = cms.double(0.2),
         beta = cms.double(2.0),
         #useExplicitGhosts = cms.bool(True),
         #writeCompound = cms.bool(True),
         #jetCollInstanceName=cms.string("SubJets"),
   ))
   li_fatjets_objects.append(fj_name)
   li_fatjets_branches.append(branch_name)

   name = "softdropz30b10"   
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
           useSoftDrop = cms.bool(True),
           zcut = cms.double(0.30),
           beta = cms.double(0.1),
           #useExplicitGhosts = cms.bool(True),
           #writeCompound = cms.bool(True),
           #jetCollInstanceName=cms.string("SubJets"),
           ))
   li_fatjets_objects.append(fj_name)        
   li_fatjets_branches.append(branch_name)

   name = "softdropz30b15"   
   fj_name = ungroomed_fj_name + name
   branch_name = ungroomed_branch_name + name
   setattr(process, fj_name, ungroomed_fj.clone(
           useSoftDrop = cms.bool(True),
           zcut = cms.double(0.30),
           beta = cms.double(0.15),
           #useExplicitGhosts = cms.bool(True),
           #writeCompound = cms.bool(True),
           #jetCollInstanceName=cms.string("SubJets"),
           ))
   li_fatjets_objects.append(fj_name)        
   li_fatjets_branches.append(branch_name)
   '''

#####################################
# Helpers: GetRadiusFromName / GetRadiusStringFromName
#####################################

def GetRadiusFromName(name):       
   if "08" in fj_name:
      return 0.8 
   elif "15" in fj_name:
      return 1.5
   else:
      print "Invalid jet radius!"
      sys.exit()

def GetRadiusStringFromName(name):        
   if "08" in fj_name:
      return "08"
   elif "15" in fj_name:
      return "15"
   else:
      print "Invalid jet radius!"
      sys.exit()


#####################################
# Shower Deconstruction
#####################################

li_fatjets_sds = []
for fj_name in li_fatjets_objects:
        
   # For Local Testing
   #sd_path = "../data/"
   # For Grid Submission
   sd_path = "src/TTH/TTHNtupleAnalyzer/data/"
        
   sd_fatjets = []
   #sd_fatjets = li_ungroomed_fatjets_objects
   
   r = GetRadiusStringFromName(fj_name)
   input_card = sd_path + "sd_input_card_{0}.dat".format(r)
   
   if fj_name in sd_fatjets:
        sd_name = fj_name + "SD"
        setattr(process, sd_name, cms.EDProducer("SDProducer",
                                                 FatjetName = cms.string(fj_name),
                                                 MicrojetCone = cms.double(0.2), 
                                                 InputCard = cms.string(input_card)))
        li_fatjets_sds.append(sd_name)
   else:
        li_fatjets_sds.append('None')


#####################################
# QJets
#####################################

# Qjets need a RNG
process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService")

li_fatjets_qvols = []
for i_fj, fj_name in enumerate(li_fatjets_objects):

   r = GetRadiusFromName(fj_name)           
        
   qvol_fatjets = li_ungroomed_fatjets_objects

   if fj_name in qvol_fatjets:

           qvol_name = fj_name + "QJetVolatility"

           setattr(process, qvol_name, cms.EDProducer("QjetsAdder",
                                                      src=cms.InputTag(fj_name),
                                                      zcut=cms.double(0.1),
                                                      dcutfctr=cms.double(0.5),
                                                      expmin=cms.double(0.0),
                                                      expmax=cms.double(0.0),
                                                      rigidity=cms.double(0.1),
                                                      ntrial = cms.int32(50),
                                                      cutoff=cms.double(10.0),
                                                      jetRad= cms.double(r),
                                                      jetAlgo=cms.string("CA"),
                                                      preclustering = cms.int32(50)))

           setattr(process.RandomNumberGeneratorService, qvol_name, cms.PSet(initialSeed = cms.untracked.uint32(i_fj),
                                                                             engineName = cms.untracked.string('TRandom3')))


           li_fatjets_qvols.append(qvol_name)

   else:
           li_fatjets_qvols.append('None')

#####################################
# CMS Top Tagger
#####################################

# CMS Top Tagger Jets
process.cmsTopTagCa08PFJetsCHS = cms.EDProducer(
        "CATopJetProducer",
        PFJetParameters,
        AnomalousCellParameters,
        CATopJetParameters.clone( jetCollInstanceName = cms.string("SubJets"),
                                  verbose = cms.bool(False),
                                  algorithm = cms.int32(1), # 0 = KT, 1 = CA, 2 = anti-KT
                                  tagAlgo = cms.int32(0), #0=legacy top
                                  useAdjacency = cms.int32(2), # modified adjacency
                                  centralEtaCut = cms.double(2.5), # eta for defining "central" jets
                                  sumEtBins = cms.vdouble(0,1600,2600), # sumEt bins over which cuts vary. vector={bin 0 lower bound, bin 1 lower bound, ...}
                                  rBins = cms.vdouble(0.8,0.8,0.8), # Jet distance paramter R. R values depend on sumEt bins.
                                  ptFracBins = cms.vdouble(0.05,0.05,0.05), # minimum fraction of central jet pt for subjets (deltap)
                                  deltarBins = cms.vdouble(0.19,0.19,0.19), # Applicable only if useAdjacency=1. deltar adjacency values for each sumEtBin
                                  nCellBins = cms.vdouble(1.9,1.9,1.9),
                                  ),
        jetAlgorithm = cms.string("CambridgeAachen"),
        rParam = cms.double(0.8),
        writeCompound = cms.bool(True)
    )
process.cmsTopTagCa08PFJetsCHS.src = cms.InputTag('chs')
process.cmsTopTagCa08PFJetsCHS.doAreaFastjet = cms.bool(True)
process.cmsTopTagCa08PFJetsCHS.jetPtMin = cms.double(200.0)

process.cmsTopTagCa15PFJetsCHS = cms.EDProducer(
        "CATopJetProducer",
        PFJetParameters,
        AnomalousCellParameters,
        CATopJetParameters.clone( jetCollInstanceName = cms.string("SubJets"),
                                  verbose = cms.bool(False),
                                  algorithm = cms.int32(1), # 0 = KT, 1 = CA, 2 = anti-KT
                                  tagAlgo = cms.int32(0), #0=legacy top
                                  useAdjacency = cms.int32(2), # modified adjacency
                                  centralEtaCut = cms.double(2.5), # eta for defining "central" jets
                                  sumEtBins = cms.vdouble(0,1600,2600), # sumEt bins over which cuts vary. vector={bin 0 lower bound, bin 1 lower bound, ...}
                                  rBins = cms.vdouble(0.8,0.8,0.8), # Jet distance paramter R. R values depend on sumEt bins.
                                  ptFracBins = cms.vdouble(0.05,0.05,0.05), # minimum fraction of central jet pt for subjets (deltap)
                                  deltarBins = cms.vdouble(0.19,0.19,0.19), # Applicable only if useAdjacency=1. deltar adjacency values for each sumEtBin
                                  nCellBins = cms.vdouble(1.9,1.9,1.9),
                                  ),
        jetAlgorithm = cms.string("CambridgeAachen"),
        rParam = cms.double(1.5),
        writeCompound = cms.bool(True)
    )
process.cmsTopTagCa15PFJetsCHS.src = cms.InputTag('chs')
process.cmsTopTagCa15PFJetsCHS.doAreaFastjet = cms.bool(True)
process.cmsTopTagCa15PFJetsCHS.jetPtMin = cms.double(200.0)

process.cmsTopTagCa08PFJetsPUPPI = cms.EDProducer(
        "CATopJetProducer",
        PFJetParameters,
        AnomalousCellParameters,
        CATopJetParameters.clone( jetCollInstanceName = cms.string("SubJets"),
                                  verbose = cms.bool(False),
                                  algorithm = cms.int32(1), # 0 = KT, 1 = CA, 2 = anti-KT
                                  tagAlgo = cms.int32(0), #0=legacy top
                                  useAdjacency = cms.int32(2), # modified adjacency
                                  centralEtaCut = cms.double(2.5), # eta for defining "central" jets
                                  sumEtBins = cms.vdouble(0,1600,2600), # sumEt bins over which cuts vary. vector={bin 0 lower bound, bin 1 lower bound, ...}
                                  rBins = cms.vdouble(0.8,0.8,0.8), # Jet distance paramter R. R values depend on sumEt bins.
                                  ptFracBins = cms.vdouble(0.05,0.05,0.05), # minimum fraction of central jet pt for subjets (deltap)
                                  deltarBins = cms.vdouble(0.19,0.19,0.19), # Applicable only if useAdjacency=1. deltar adjacency values for each sumEtBin
                                  nCellBins = cms.vdouble(1.9,1.9,1.9),
                                  ),
        jetAlgorithm = cms.string("CambridgeAachen"),
        rParam = cms.double(0.8),
        writeCompound = cms.bool(True)
    )
process.cmsTopTagCa08PFJetsPUPPI.src = cms.InputTag('puppi')
process.cmsTopTagCa08PFJetsPUPPI.doAreaFastjet = cms.bool(True)
process.cmsTopTagCa08PFJetsPUPPI.jetPtMin = cms.double(200.0)

process.cmsTopTagCa15PFJetsPUPPI = cms.EDProducer(
        "CATopJetProducer",
        PFJetParameters,
        AnomalousCellParameters,
        CATopJetParameters.clone( jetCollInstanceName = cms.string("SubJets"),
                                  verbose = cms.bool(False),
                                  algorithm = cms.int32(1), # 0 = KT, 1 = CA, 2 = anti-KT
                                  tagAlgo = cms.int32(0), #0=legacy top
                                  useAdjacency = cms.int32(2), # modified adjacency
                                  centralEtaCut = cms.double(2.5), # eta for defining "central" jets
                                  sumEtBins = cms.vdouble(0,1600,2600), # sumEt bins over which cuts vary. vector={bin 0 lower bound, bin 1 lower bound, ...}
                                  rBins = cms.vdouble(0.8,0.8,0.8), # Jet distance paramter R. R values depend on sumEt bins.
                                  ptFracBins = cms.vdouble(0.05,0.05,0.05), # minimum fraction of central jet pt for subjets (deltap)
                                  deltarBins = cms.vdouble(0.19,0.19,0.19), # Applicable only if useAdjacency=1. deltar adjacency values for each sumEtBin
                                  nCellBins = cms.vdouble(1.9,1.9,1.9),
                                  ),
        jetAlgorithm = cms.string("CambridgeAachen"),
        rParam = cms.double(1.5),
        writeCompound = cms.bool(True)
    )
process.cmsTopTagCa15PFJetsPUPPI.src = cms.InputTag('puppi')
process.cmsTopTagCa15PFJetsPUPPI.doAreaFastjet = cms.bool(True)
process.cmsTopTagCa15PFJetsPUPPI.jetPtMin = cms.double(200.0)

li_cmstt_objects = ['cmsTopTagCa08PFJetsCHS', 'cmsTopTagCa15PFJetsCHS', 'cmsTopTagCa08PFJetsPUPPI', 'cmsTopTagCa15PFJetsPUPPI']
li_cmstt_branches = ['ca08cmstt',              'ca15cmstt',              'ca08puppicmstt',           'ca15puppicmstt']

# CMS Top Tagger Infos
process.ca08CMSTopTagInfos = cms.EDProducer("CATopJetTagger",
                                            src = cms.InputTag("cmsTopTagCa08PFJetsCHS"),
                                            TopMass = cms.double(173),
                                            TopMassMin = cms.double(0.),
                                            TopMassMax = cms.double(250.),
                                            WMass = cms.double(80.4),
                                            WMassMin = cms.double(0.0),
                                            WMassMax = cms.double(200.0),
                                            MinMassMin = cms.double(0.0),
                                            MinMassMax = cms.double(200.0),
                                            verbose = cms.bool(False))

process.ca15CMSTopTagInfos = cms.EDProducer("CATopJetTagger",
                                            src = cms.InputTag("cmsTopTagCa15PFJetsCHS"),
                                            TopMass = cms.double(173),
                                            TopMassMin = cms.double(0.),
                                            TopMassMax = cms.double(250.),
                                            WMass = cms.double(80.4),
                                            WMassMin = cms.double(0.0),
                                            WMassMax = cms.double(200.0),
                                            MinMassMin = cms.double(0.0),
                                            MinMassMax = cms.double(200.0),
                                            verbose = cms.bool(False))

process.ca08puppiCMSTopTagInfos = cms.EDProducer("CATopJetTagger",
                                            src = cms.InputTag("cmsTopTagCa08PFJetsPUPPI"),
                                            TopMass = cms.double(173),
                                            TopMassMin = cms.double(0.),
                                            TopMassMax = cms.double(250.),
                                            WMass = cms.double(80.4),
                                            WMassMin = cms.double(0.0),
                                            WMassMax = cms.double(200.0),
                                            MinMassMin = cms.double(0.0),
                                            MinMassMax = cms.double(200.0),
                                            verbose = cms.bool(False))

process.ca15puppiCMSTopTagInfos = cms.EDProducer("CATopJetTagger",
                                            src = cms.InputTag("cmsTopTagCa15PFJetsPUPPI"),
                                            TopMass = cms.double(173),
                                            TopMassMin = cms.double(0.),
                                            TopMassMax = cms.double(250.),
                                            WMass = cms.double(80.4),
                                            WMassMin = cms.double(0.0),
                                            WMassMax = cms.double(200.0),
                                            MinMassMin = cms.double(0.0),
                                            MinMassMax = cms.double(200.0),
                                            verbose = cms.bool(False))


#####################################
#  HEPTopTagger
#####################################

li_htt_branches = []

for input_object in ["chs", "puppi"]:
   

   name = "looseMultiRHTT"
   if not input_object == "chs":
      name += input_object

   setattr(process, name, cms.EDProducer(
        "HTTTopJetProducer",
        PFJetParameters.clone( src = cms.InputTag(input_object),
                               doAreaFastjet = cms.bool(True),
                               doRhoFastjet = cms.bool(False),
                               jetPtMin = cms.double(100.0),
                               jetCollInstanceName = cms.string("SubJets"),
                           ),
        AnomalousCellParameters,
        multiR = cms.bool(True),
        algorithm = cms.int32(1),
        jetAlgorithm = cms.string("CambridgeAachen"),
        rParam = cms.double(1.5),
        mode = cms.int32(4),
        minFatjetPt = cms.double(200.),
        minCandPt = cms.double(200.),
        minSubjetPt = cms.double(30.),
        writeCompound = cms.bool(True),
        minCandMass = cms.double(0.),
        maxCandMass = cms.double(1000),
        massRatioWidth = cms.double(100.),
        minM23Cut = cms.double(0.),
        minM13Cut = cms.double(0.),
        maxM13Cut = cms.double(2.)))
   li_htt_branches.append(name)

   
   name = "softdropz20b10MultiRHTT"
   if not input_object == "chs":
      name += input_object

   setattr(process, name, cms.EDProducer(
        "HTTTopJetProducer",
        PFJetParameters.clone( src = cms.InputTag(input_object),
                               doAreaFastjet = cms.bool(True),
                               doRhoFastjet = cms.bool(False),
                               jetPtMin = cms.double(100.0),
                               jetCollInstanceName = cms.string("SubJets"),
                           ),
        AnomalousCellParameters,
        multiR = cms.bool(True),
        algorithm = cms.int32(1),
        jetAlgorithm = cms.string("CambridgeAachen"),
        rParam = cms.double(1.5),
        mode = cms.int32(4),
        minFatjetPt = cms.double(200.),
        minCandPt = cms.double(200.),
        minSubjetPt = cms.double(30.),
        writeCompound = cms.bool(True),
        minCandMass = cms.double(0.),
        maxCandMass = cms.double(1000),
        massRatioWidth = cms.double(100.),
        minM23Cut = cms.double(0.),
        minM13Cut = cms.double(0.),
        maxM13Cut = cms.double(2.),
        unclustering_pt = cms.bool(True),
        unclustering_R0 = cms.double(1.5),
        unclustering_beta = cms.double(1.0),
        unclustering_zcut = cms.double(0.2),
   ))
   li_htt_branches.append(name)


   
   for beta in [-2., -1., 0., 1.]:
   
      if beta < 0:
         beta_name = "minus{0:0>2}".format(int(abs(beta*10.)))
      else:
         beta_name = "{0:0>2}".format(int(beta*10.))
   
      name = "softdropz15b{0}MultiRHTT".format(beta_name)
      if not input_object == "chs":
         name += input_object

      setattr(process, name, cms.EDProducer(
           "HTTTopJetProducer",
           PFJetParameters.clone( src = cms.InputTag(input_object),
                                  doAreaFastjet = cms.bool(True),
                                  doRhoFastjet = cms.bool(False),
                                  jetPtMin = cms.double(100.0),
                                  jetCollInstanceName = cms.string("SubJets"),
                              ),
           AnomalousCellParameters,
           multiR = cms.bool(True),
           algorithm = cms.int32(1),
           jetAlgorithm = cms.string("CambridgeAachen"),
           rParam = cms.double(1.5),
           mode = cms.int32(4),
           minFatjetPt = cms.double(200.),
           minCandPt = cms.double(200.),
           minSubjetPt = cms.double(30.),
           writeCompound = cms.bool(True),
           minCandMass = cms.double(0.),
           maxCandMass = cms.double(1000),
           massRatioWidth = cms.double(100.),
           minM23Cut = cms.double(0.),
           minM13Cut = cms.double(0.),
           maxM13Cut = cms.double(2.),
           unclustering_pt = cms.bool(True),
           unclustering_R0 = cms.double(1.5),
           unclustering_beta = cms.double(beta),
           unclustering_zcut = cms.double(0.15),
      ))
      li_htt_branches.append(name)

      
#####################################
# NSubjettiness
#####################################

li_fatjets_nsubs = []

print "li_fatjets_objects: ", li_fatjets_objects

for fj_name in li_fatjets_objects:
   #if ("filtered" in fj_name) or ("pruned" in fj_name) or ("trimmed" in fj_name) or ("softdrop" in fj_name):
   if "forbtag" in fj_name:
      li_fatjets_nsubs.append("None")

   else:
      nsub_name = fj_name + "Njettiness"
      r = GetRadiusFromName(fj_name)
      
      setattr(process, nsub_name, cms.EDProducer("NjettinessAdder",
                                                 src=cms.InputTag(fj_name),
                                                 Njets=cms.vuint32(1,2,3),          # compute 1-, 2-, 3- subjettiness
                                                 # variables for measure definition : 
                                                 measureDefinition = cms.uint32( 0 ), # CMS default is normalized measure
                                                 beta = cms.double(1.0),              # CMS default is 1
                                                 R0 = cms.double(r),              # CMS default is jet cone size
                                                 Rcutoff = cms.double( -999.0),       # not used by default
                                                 # variables for axes definition :
                                                 axesDefinition = cms.uint32(6),    # CMS default is 1-pass KT axes
                                                 nPass = cms.int32(-999),             # not used by default
                                                 akAxesR0 = cms.double(-999.0)        # not used by default
                                                 ))
      li_fatjets_nsubs.append(nsub_name)
   #else:
   #   li_fatjets_nsubs.append("None")

print len(li_fatjets_objects), len(li_fatjets_nsubs)

li_cmstt_nsubs = []

for cmstoptag_name in li_cmstt_objects:
   nsub_name = cmstoptag_name + "Njettiness"
   r = GetRadiusFromName(cmstoptag_name)
   
   setattr(process, nsub_name, cms.EDProducer("NjettinessAdder",
                                              src=cms.InputTag(cmstoptag_name),
                                              Njets=cms.vuint32(1,2,3),          # compute 1-, 2-, 3- subjettiness
                                              # variables for measure definition : 
                                              measureDefinition = cms.uint32( 0 ), # CMS default is normalized measure
                                              beta = cms.double(1.0),              # CMS default is 1
                                              R0 = cms.double(r),              # CMS default is jet cone size
                                              Rcutoff = cms.double( -999.0),       # not used by default
                                              # variables for axes definition :
                                              axesDefinition = cms.uint32(6),    # CMS default is 1-pass KT axes
                                              nPass = cms.int32(-999),             # not used by default
                                              akAxesR0 = cms.double(-999.0)        # not used by default
                                              ))
   li_cmstt_nsubs.append(nsub_name)
   #else:
   #   li_cmstt_nsubs.append("None")

print len(li_cmstt_objects), len(li_cmstt_nsubs)

li_htt_nsubs = []

for heptoptag_name in li_htt_branches:
   nsub_name = heptoptag_name + "Njettiness"
   r = GetRadiusFromName(heptoptag_name)
   
   setattr(process, nsub_name, cms.EDProducer("NjettinessAdder",
                                              src=cms.InputTag(heptoptag_name),
                                              Njets=cms.vuint32(1,2,3),          # compute 1-, 2-, 3- subjettiness
                                              # variables for measure definition : 
                                              measureDefinition = cms.uint32( 0 ), # CMS default is normalized measure
                                              beta = cms.double(1.0),              # CMS default is 1
                                              R0 = cms.double(r),              # CMS default is jet cone size
                                              Rcutoff = cms.double( -999.0),       # not used by default
                                              # variables for axes definition :
                                              axesDefinition = cms.uint32(6),    # CMS default is 1-pass KT axes
                                              nPass = cms.int32(-999),             # not used by default
                                              akAxesR0 = cms.double(-999.0)        # not used by default
                                              ))
   li_htt_nsubs.append(nsub_name)
   #else:
   #   li_htt_nsubs.append("None")

print len(li_htt_branches), len(li_htt_nsubs)

#####################################
# b-tagging
#####################################
process.my_btagging = cms.Sequence()
# Add b-tagging information for all fatjets
li_fatjets_btags = []

for fatjet_name in li_fatjets_objects:
   if "forbtag" in fatjet_name:
   #if ("pruned" in fatjet_name) or ("trimmed" in fatjet_name) or ("softdrop" in fatjet_name):
      # Define the names
      impact_info_name          = fatjet_name + "ImpactParameterTagInfos"
      isv_info_name             = fatjet_name + "pfInclusiveSecondaryVertexFinderTagInfos"        
      csvv2_computer_name       = fatjet_name + "combinedSecondaryVertexV2Computer"
      csvv2ivf_name             = fatjet_name + "pfCombinedInclusiveSecondaryVertexV2BJetTags"        
      
      delta_r = GetRadiusFromName(fatjet_name)
      
      # Setup the modules
      setattr(process, 
              impact_info_name, 
              process.pfImpactParameterTagInfos.clone(
            primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
            candidates = cms.InputTag("packedPFCandidates"),
            jets = cms.InputTag(fatjet_name, "SubJets"),
            ))
      getattr(process, impact_info_name).explicitJTA = cms.bool(True)
      setattr(process,
              isv_info_name,                
              process.pfInclusiveSecondaryVertexFinderTagInfos.clone(
            extSVCollection               = cms.InputTag('slimmedSecondaryVertices'),
            trackIPTagInfos               = cms.InputTag(impact_info_name),                
            ))
      getattr(process, isv_info_name).useSVClustering = cms.bool(True)
      getattr(process, isv_info_name).jetAlgorithm = cms.string("CambridgeAachen")
      getattr(process, isv_info_name).rParam = cms.double(delta_r)
      if "PUPPI" in fatjet_name:
         if "ca08" in fatjet_name:
            getattr(process, isv_info_name).fatJets  =  cms.InputTag("ca08PFJetsPUPPI")
         elif "ca15" in fatjet_name:
            getattr(process, isv_info_name).fatJets  =  cms.InputTag("ca15PFJetsPUPPI")
      else:
         if "ca08" in fatjet_name:
            getattr(process, isv_info_name).fatJets  =  cms.InputTag("ca08PFJetsCHS")
         elif "ca15" in fatjet_name:
            getattr(process, isv_info_name).fatJets  =  cms.InputTag("ca15PFJetsCHS")
      getattr(process, isv_info_name).groomedFatJets  =  cms.InputTag(fatjet_name)

      setattr(process,
           csvv2_computer_name,
           process.candidateCombinedSecondaryVertexV2Computer.clone())

      setattr(process,
              csvv2ivf_name,
              process.pfCombinedInclusiveSecondaryVertexV2BJetTags.clone(
            tagInfos = cms.VInputTag(cms.InputTag(impact_info_name),
                                     cms.InputTag(isv_info_name)),
            jetTagComputer = cms.string(csvv2_computer_name,)
            ))
      
      # Add modules to sequence
      for module_name in [impact_info_name,
                          isv_info_name,              
                          csvv2ivf_name]:              
         process.my_btagging += getattr(process, module_name)
      
      # remember the module that actually produces the b-tag
      # discriminator so we can pass it to the NTupelizer
      li_fatjets_btags.append(csvv2ivf_name)
      
   else:
      li_fatjets_btags.append("None")
      
# end of loop over fatjets

print len(li_fatjets_objects), len(li_fatjets_btags)

# Add b-tagging information for all cmstt
li_cmstt_btags = []

for cmstt_name in li_cmstt_objects:
   #if "forbtag" in cmstt_name:
   #if ("pruned" in cmstt_name) or ("trimmed" in cmstt_name) or ("softdrop" in cmstt_name):
   # Define the names
   impact_info_name          = cmstt_name + "ImpactParameterTagInfos"
   isv_info_name             = cmstt_name + "pfInclusiveSecondaryVertexFinderTagInfos"        
   csvv2_computer_name       = cmstt_name + "combinedSecondaryVertexV2Computer"
   csvv2ivf_name             = cmstt_name + "pfCombinedInclusiveSecondaryVertexV2BJetTags"        
      
   delta_r = GetRadiusFromName(cmstt_name)
      
   # Setup the modules
   setattr(process, 
           impact_info_name, 
           process.pfImpactParameterTagInfos.clone(
         primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
         candidates = cms.InputTag("packedPFCandidates"),
         jets = cms.InputTag(cmstt_name, "SubJets"),
         ))
   getattr(process, impact_info_name).explicitJTA = cms.bool(True)
   setattr(process,
           isv_info_name,                
           process.pfInclusiveSecondaryVertexFinderTagInfos.clone(
         extSVCollection               = cms.InputTag('slimmedSecondaryVertices'),
         trackIPTagInfos               = cms.InputTag(impact_info_name),                
         ))
   getattr(process, isv_info_name).useSVClustering = cms.bool(True)
   getattr(process, isv_info_name).jetAlgorithm = cms.string("CambridgeAachen")
   getattr(process, isv_info_name).rParam = cms.double(delta_r)
   if "PUPPI" in cmstt_name:
      if "ca08" in cmstt_name:
         getattr(process, isv_info_name).cmstt  =  cms.InputTag("cmsTopTagCa08PFJetsPUPPI")
      elif "ca15" in cmstt_name:
         getattr(process, isv_info_name).cmstt  =  cms.InputTag("cmsTopTagCa15PFJetsPUPPI")
   else:
      if "ca08" in cmstt_name:
         getattr(process, isv_info_name).cmstt  =  cms.InputTag("cmsTopTagCa08PFJetsCHS")
      elif "ca15" in cmstt_name:
         getattr(process, isv_info_name).cmstt  =  cms.InputTag("cmsTopTagCa15PFJetsCHS")
   getattr(process, isv_info_name).groomedCmstt  =  cms.InputTag(cmstt_name)
   
   setattr(process,
           csvv2_computer_name,
           process.candidateCombinedSecondaryVertexV2Computer.clone())
   
   setattr(process,
           csvv2ivf_name,
           process.pfCombinedInclusiveSecondaryVertexV2BJetTags.clone(
         tagInfos = cms.VInputTag(cms.InputTag(impact_info_name),
                                  cms.InputTag(isv_info_name)),
         jetTagComputer = cms.string(csvv2_computer_name,)
         ))
      
   # Add modules to sequence
   for module_name in [impact_info_name,
                       isv_info_name,              
                       csvv2ivf_name]:              
      process.my_btagging += getattr(process, module_name)
      
   # remember the module that actually produces the b-tag
   # discriminator so we can pass it to the NTupelizer
   li_cmstt_btags.append(csvv2ivf_name)
      
   #else:
   #   li_cmstt_btags.append("None")
      
# end of loop over cmstt

print len(li_cmstt_objects), len(li_cmstt_btags)

'''# Add b-tagging information for all htt
li_htt_btags = []

for htt_name in li_htt_branches:
   #if "forbtag" in htt_name:
   #if ("pruned" in htt_name) or ("trimmed" in htt_name) or ("softdrop" in htt_name):
   # Define the names
   impact_info_name          = htt_name + "ImpactParameterTagInfos"
   isv_info_name             = htt_name + "pfInclusiveSecondaryVertexFinderTagInfos"        
   csvv2_computer_name       = htt_name + "combinedSecondaryVertexV2Computer"
   csvv2ivf_name             = htt_name + "pfCombinedInclusiveSecondaryVertexV2BJetTags"        
      
   delta_r = GetRadiusFromName(htt_name)
      
   # Setup the modules
   setattr(process, 
           impact_info_name, 
           process.pfImpactParameterTagInfos.clone(
         primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
         candidates = cms.InputTag("packedPFCandidates"),
         jets = cms.InputTag(htt_name, "SubJets"),
         ))
   getattr(process, impact_info_name).explicitJTA = cms.bool(True)
   setattr(process,
           isv_info_name,                
           process.pfInclusiveSecondaryVertexFinderTagInfos.clone(
         extSVCollection               = cms.InputTag('slimmedSecondaryVertices'),
         trackIPTagInfos               = cms.InputTag(impact_info_name),                
         ))
   getattr(process, isv_info_name).useSVClustering = cms.bool(True)
   getattr(process, isv_info_name).jetAlgorithm = cms.string("CambridgeAachen")
   getattr(process, isv_info_name).rParam = cms.double(delta_r)
   getattr(process, isv_info_name).htt  =  cms.InputTag(htt_name)
   getattr(process, isv_info_name).groomedHtt  =  cms.InputTag(htt_name)
   
   setattr(process,
           csvv2_computer_name,
           process.candidateCombinedSecondaryVertexV2Computer.clone())
   
   setattr(process,
           csvv2ivf_name,
           process.pfCombinedInclusiveSecondaryVertexV2BJetTags.clone(
         tagInfos = cms.VInputTag(cms.InputTag(impact_info_name),
                                  cms.InputTag(isv_info_name)),
         jetTagComputer = cms.string(csvv2_computer_name,)
         ))
      
   # Add modules to sequence
   for module_name in [impact_info_name,
                       isv_info_name,              
                       csvv2ivf_name]:              
      process.my_btagging += getattr(process, module_name)
      
   # remember the module that actually produces the b-tag
   # discriminator so we can pass it to the NTupelizer
   li_htt_btags.append(csvv2ivf_name)
      
   #else:
   #   li_htt_btags.append("None")
      
# end of loop over htt

print len(li_htt_branches), len(li_htt_btags)
'''

#####################################
# NTupelizer
#####################################

li_fatjets_use_subjets = []
for fj in li_fatjets_objects:
   #if ("pruned" in fj) or ("trimmed" in fj) or ("softdrop" in fj):
   if "forbtag" in fj:
      li_fatjets_use_subjets.append(1)
   else:
      li_fatjets_use_subjets.append(0)

print "!!!!!!!!!!!!!"
print "li_htt_branches: ", li_htt_branches
print "li_fatjets_branches: ", li_fatjets_branches
print "li_ungroomed_fatjets_branches: ", li_ungroomed_fatjets_branches
print "!!!!!!!!!!!!!"
print "!!!!!!!!!!!!!"
print ""

process.tthNtupleAnalyzer = cms.EDAnalyzer('TTHNtupleAnalyzer',
	isMC = cms.bool(True),
	vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
	muons = cms.InputTag("slimmedMuons"),
	electrons = cms.InputTag("slimmedElectrons"),
	taus = cms.InputTag("slimmedTaus"),
	jets = cms.InputTag("slimmedJets"),
	genjets = cms.InputTag("slimmedGenJets"),

	packed = cms.InputTag("packedGenParticles"),
	pruned = cms.InputTag("prunedGenParticles"),
	mets = cms.InputTag("slimmedMETs"),
	lhe = cms.InputTag("externalLHEProducer"),

        triggerIdentifiers = cms.vstring([]),
        triggerIdentifiersForMatching = cms.vstring([]),

        fatjetsObjects  = cms.vstring(li_fatjets_objects),
        fatjetsNsubs    = cms.vstring(li_fatjets_nsubs),
        fatjetsSDs      = cms.vstring(li_fatjets_sds),
        fatjetsBtags    = cms.vstring(li_fatjets_btags),
        fatjetsQvols    = cms.vstring(li_fatjets_qvols),
        fatjetsBranches = cms.vstring(li_fatjets_branches),
        fatjetsUsesubjets = cms.vint32(li_fatjets_use_subjets),                                           

        httObjects  = cms.vstring(li_htt_branches), # Using branch names also as object names
        httNsubs    = cms.vstring(li_htt_nsubs),
        #httBtags    = cms.vstring(li_htt_btags),
        httBranches = cms.vstring(li_htt_branches),                                           
       
        cmsttObjects  = cms.vstring(['cmsTopTagCa08PFJetsCHS', 'cmsTopTagCa15PFJetsCHS', 'cmsTopTagCa08PFJetsPUPPI', 'cmsTopTagCa15PFJetsPUPPI']),
        cmsttNsubs    = cms.vstring(li_cmstt_nsubs),
        cmsttBtags    = cms.vstring(li_cmstt_btags),
        cmsttInfos    = cms.vstring(['ca08CMSTopTagInfos',     'ca15CMSTopTagInfos'    , 'ca08puppiCMSTopTagInfos',  'ca15puppiCMSTopTagInfos']),
        cmsttBranches = cms.vstring(['ca08cmstt',              'ca15cmstt',              'ca08puppicmstt',           'ca15puppicmstt']),

	jetMult_min   = cms.untracked.int32(-99),
	jetPt_min     = cms.untracked.double(15.),
	muPt_min_     = cms.untracked.double(15.),
	elePt_min_    = cms.untracked.double(15.),
	tauPt_min_    = cms.untracked.double(15.),

	bits	  = cms.InputTag("TriggerResults","","HLT"),
	objects   = cms.InputTag("selectedPatTrigger"),
	prescales = cms.InputTag("patTrigger"),

	eleIdentifiers = cms.vstring([]),
	tauIdentifiers = cms.vstring([]),

        rho = cms.InputTag("fixedGridRhoAll"),
        jecFile = cms.FileInPath("Summer13_V4_DATA_UncertaintySources_AK5PFchs.txt")
)


process.TFileService = cms.Service("TFileService",
	fileName = cms.string(options.outputFile)
)


#####################################
# Schedule Algorithms
#####################################

process.p = cms.Path(process.chs)
process.p += process.puppi

# Schedule all fatjets
for fj_name in li_fatjets_objects:
   process.p += getattr(process, fj_name)

# Schedule QJet Volatility
for qvol_name in li_fatjets_qvols:
   if qvol_name == "None":
      continue
   else:
      process.p += getattr(process, qvol_name)       
                
# Schedule Shower Deconstruction
for sd_name in li_fatjets_sds:
   if sd_name == "None":
      continue
   else:
      process.p += getattr(process, sd_name)

# Schedule HEPTopTagger
for htt_name in li_htt_branches:
   process.p += getattr(process, htt_name)

# Schedule CMS Top Tagger, HEPTopTagger, b-tagging and Ntupelizer
for x in [process.cmsTopTagCa08PFJetsCHS,
          process.cmsTopTagCa15PFJetsCHS,
          process.cmsTopTagCa08PFJetsPUPPI,
          process.cmsTopTagCa15PFJetsPUPPI,
          process.ca08CMSTopTagInfos,
          process.ca15CMSTopTagInfos,
          process.ca08puppiCMSTopTagInfos,
          process.ca15puppiCMSTopTagInfos,
          process.my_btagging,
          #process.SimpleMemoryCheck,
  ]:
   process.p += x

# Schedule NSubjettiness
for nsub_name in li_fatjets_nsubs:
   if nsub_name == "None":
      continue
   else:
      process.p += getattr(process, nsub_name)
for nsub_name in li_cmstt_nsubs:
   process.p += getattr(process, nsub_name)
for nsub_name in li_htt_nsubs:
   process.p += getattr(process, nsub_name)

for y in [process.tthNtupleAnalyzer]: 
   process.p += y

if "TTH_DEBUG" in os.environ:
	process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
	process.printTree = cms.EDAnalyzer("ParticleListDrawer",
		maxEventsToPrint = cms.untracked.int32(-1),
		printVertex = cms.untracked.bool(True),
		src = cms.InputTag("prunedGenParticles")
	)
	process.p += process.printTree

print li_fatjets_branches
