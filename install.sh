#!/bin/bash
mcatnlo2lhe=$PWD
cd $CMSSW_BASE/src  
addpkg GeneratorInterface/LHEInterface
addpkg GeneratorInterface/MCatNLOInterface
cd GeneratorInterface/LHEInterface
patch -p1  < $mcatnlo2lhe/lheWriter.patch
cd $CMSSW_BASE/src
scram b -j 4
