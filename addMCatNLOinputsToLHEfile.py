import argparse
import fileinput
parser=argparse.ArgumentParser()
parser.add_argument('--lheFile',default='',help='lhe File where mcatnlo.inputs should be added')
parser.add_argument('--mcatnloInputs',default='',help='mcatnloInputs file which should be added')

args=parser.parse_args()
foundHeader=False
for line in fileinput.input(args.lheFile,inplace=1):
  if foundHeader:
    print '<!--'
    with open(args.mcatnloInputs) as mcatnloInputs:
      for mcatnloInput in mcatnloInputs:
        if not mcatnloInput.isspace() and not  mcatnloInput.startswith('#'):
          print mcatnloInput,
    print '-->'
    foundHeader=False
  if line.startswith('</header>'):
    foundHeader=True
  
  print line,

  
