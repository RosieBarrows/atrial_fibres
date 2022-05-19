#!/usr/bin/env bash
# Add fibres to carp mesh, then converrt to vtk
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
imesh=$1
fmesh=$2
omesh=$3
echo "[INFO] Moving fibres from $fmesh to $imesh"
echo "1" > $imesh.lon
cat $fmesh.lon >> $imesh.lon
echo "[INFO] Converting to vtk"
meshtool convert -imsh=$imesh -ifmt=carp_txt -omsh=$omesh -ofmt=vtk