convert MCatNLO output to LHE:
cmsRun convertMCatNLO2LHE_cfg.py inputFiles=file:MCatNLO_3_4_1/test/Linux/ttb.events outputFile=TT_MCatNLO_test.lhe mcatnloInputsFile=MCatNLO_3_4_1/test/MCatNLO.inputs

or provide iproc parameter

cmsRun convertMCatNLO2LHE_cfg.py inputFiles=file:MCatNLO_3_4_1/test/Linux/ttb.events outputFile=TT_MCatNLO_test.lhe iproc=-1706

add Mcatnlo.inputs to LHE file:

python  addMCatNLOinputsToLHEfile.py --lheFile TT_MCatNLO_test.lhe --mcatnloInputs test/MCatNLO.inputs
