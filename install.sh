#!/bin/bash
klist -s
rc=$?
if [[ $rc != 0 ]] ; then
echo "kerberos credentials missing"
    klist -c
    exit $rc
fi
mcatnlo2lhe=$PWD
cd $CMSSW_BASE/src  
addpkg GeneratorInterface/LHEInterface
addpkg GeneratorInterface/MCatNLOInterface
cd GeneratorInterface/LHEInterface
patch -p1  < $mcatnlo2lhe/lheWriter.patch
cd $CMSSW_BASE/src
scram b -j 4
cd $CMSSW_BASE
git@github.com:fhoehle/LHEprocessing.git
pkgs=(
  "LHEprocessing ./ ./install.sh"
)
 
function getGitPackage {
  if [ -d "$1" ]; then
  echo "updating "$1
    cd $1
    git fetch
  else
    echo "installing "$1
    git clone git@github.com:fhoehle/$1.git
    cd $1
  fi
}
function installMyGitPackages {
  pkgs=$1[@]
  cd $CMSSW_BASE
  for idx in ${!pkgs[*]}; do
    cd $CMSSW_BASE/`echo ${pkgs[$idx]} | awk '{print $2}'`
    getGitPackage `echo ${pkgs[$idx]} | awk '{print $1}'`
    if [ "X`echo ${pkgs[$idx]} | awk '{print $3}'`" != "X" ]; then
      echo "${pkgs[$idx]} installing subpackage with additional command "`echo ${pkgs[$idx]} | awk '{print $3}'`
      eval `echo ${pkgs[$idx]} | awk '{print $3}'`
    fi
    if [ "X`echo ${pkgs[$idx]} | awk '{print $4}'`" != "X" ]; then
      echo "${pkgs[$idx]}: using specific tag: "
      git checkout `echo ${pkgs[$idx]} | awk '{print $4}'`
    fi
    cd $CMSSW_BASE
  done
}
installMyGitPackages pkgs
