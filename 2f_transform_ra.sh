#!/bin/bash

clear

FOLDER="/data/Dropbox/Segmentations/2016111001EP/final_heart/surfaces_UVC_RA/ra/uvc"
mshName="ra" 

echo "translating mesh"
cmd="perl /home/rb21/Software/cm2carp/bin/return_carp2original_coord.pl ${FOLDER}/${mshName}.pts 1 -59540 -252800 1229000 > ${FOLDER}/${mshName}_shift.pts"
eval $cmd

echo "creating shift.elem file"
cmd="cp ${FOLDER}/${mshName}.elem ${FOLDER}/${mshName}_shift.elem"
eval $cmd

echo "creating shift.lon file"
cmd="cp ${FOLDER}/${mshName}.lon ${FOLDER}/${mshName}_shift.lon"
eval $cmd

echo "generating default fibres with -op=1"
cmd="meshtool generate fibres -msh=${FOLDER}/${mshName}_shift -outmsh=${FOLDER}/${mshName}_shift -op=1"
eval $cmd

echo "converting carp to vtk"
cmd="meshtool convert -imsh=${FOLDER}/${mshName}_shift -ifmt=carp_txt -omsh=${FOLDER}/${mshName}_shift -ofmt=vtk"
eval $cmd 