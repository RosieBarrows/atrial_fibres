#!/bin/bash

clear

CARPFOLDER="home/rb21/Software/CARPentry_KCL_latest/bin/"

mshPath="/data/Dropbox/Segmentations/2016111001EP/final_heart/RA_endo_fch/epi"
mshName="RA_endo_um_shift_fibres"

echo "Generating elements centres..."
cmd="GlElemCenters -m ${mshPath}/${mshName} -o ${mshPath}/${mshName}_elem_centres.pts"
echo $cmd
eval $cmd  

echo "Find and loop over empty fibres..."
cmd="python fibres_loop.py ${mshPath}/${mshName}"
echo $cmd
eval $cmd

echo "creating elem file"
cmd="cp ${mshPath}/${mshName}.elem ${mshPath}/${mshName}_corrected.elem"
eval $cmd

echo "creating pts file"
cmd="cp ${mshPath}/${mshName}.pts ${mshPath}/${mshName}_corrected.pts"
eval $cmd

echo "Convert to vtk"
cmd="meshtool convert -imsh=${mshPath}/${mshName}_corrected -ifmt=carp_txt -omsh=${mshPath}/${mshName}_corrected -ofmt=vtk"
echo $cmd
eval $cmd
