#!/usr/bin/env cmsRun

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis') 
options.register ('iproc',
                   0,
                   VarParsing.multiplicity.singleton,
                   VarParsing.varType.int,
                   "IPROC parameter used in MCatNLO.inputs")
options.register ('mcatnloInputsFile','',VarParsing.multiplicity.singleton,VarParsing.varType.string,'MCatNLO.inputs file')
options.parseArguments()
if options.iproc == 0:
  import os.path as path
  if path.isfile(options.mcatnloInputsFile):
     with open (options.mcatnloInputsFile) as mcatnloInputs:
       for line in mcatnloInputs:
         if not line.startswith('#') and 'IPROC' in line:
           import re 
           options.iproc = int(re.match('^\ *IPROC\ *=\ *([^=\ #]*)[\ #]*.*',line).group(1))
           break
#  elif (open(options.inputFiles[0].lstrip('file:')).readline()).startswith('# comment block MCatNLO.inputs'):
#     with open (options.inputFiles[0]) as mcatnloInputs:
#       for line in mcatnloInputs:
#         if not line.startswith('#') and 'IPROC' in line:
#           import re
#           options.iproc = int(re.match('^\ *IPROC\ *=\ *([^=\ #]*)[\ #]*.*',line).group(1))
#           break
  if options.iproc == 0  or not isinstance(options.iproc,int):
    import sys
    sys.exit('cannot determine iproc parameter')
print 'IPROC ',options.iproc
import FWCore.ParameterSet.Config as cms

process = cms.Process("MCatNLO2LHE")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.source = cms.Source("MCatNLOSource",
	fileNames = cms.untracked.vstring('file:ttb.events'),
         processCode = cms.int32(-11361)
)
process.source.fileNames= options.inputFiles
process.source.processCode = int(options.iproc)
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'

process.writer = cms.EDAnalyzer("LHEWriter",
  ouputFile=cms.string('test.lhe')
)
process.writer.ouputFile = options.outputFile

process.outpath = cms.EndPath(process.writer)
