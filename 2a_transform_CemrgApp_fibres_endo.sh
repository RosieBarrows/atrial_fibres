#!/bin/bash

clear

# ./transfrom_CemrgApp_fibres.sh /path/to/endo_um /path/to/CemrgApp_mesh

FOLDER="/data/Dropbox/Segmentations/2016111001EP/final_heart/LA_endo_fch/endo"
endo_um="LA_endo_um" 
cemrg_endo="/data/Dropbox/Segmentations/2016111001EP/final_heart/LA_endo_fch/endo/LA_endo_cemrg"

echo "converting vtk to carp"
cmd="meshtool convert -imsh=${FOLDER}/${endo_um} -ifmt=vtk -omsh=${FOLDER}/${endo_um} -ofmt=carp_txt"
eval $cmd 

echo "converting cemrg vtk to carp"
cmd="meshtool convert -imsh=${cemrg_endo} -ifmt=vtk -omsh=${cemrg_endo} -ofmt=carp_txt"
eval $cmd 

echo "translating mesh"
cmd="perl /home/rb21/Software/cm2carp/bin/return_carp2original_coord.pl ${FOLDER}/${endo_um}.pts 1 -59540 -252800 1229000 > ${FOLDER}/${endo_um}_shift.pts"
eval $cmd

echo "creating shift.elem file"
cmd="cp ${FOLDER}/${endo_um}.elem ${FOLDER}/${endo_um}_shift.elem"
eval $cmd

echo "creating shift.lon file"
cmd="cp ${FOLDER}/${endo_um}.lon ${FOLDER}/${endo_um}_shift.lon"
eval $cmd

echo "generating default fibres with -op=1"
cmd="meshtool generate fibres -msh=${FOLDER}/${endo_um}_shift -outmsh=${FOLDER}/${endo_um}_shift -op=1"
eval $cmd

echo "inserting meshdata from CemrgApp mesh onto 4 chamber mesh"
cmd="meshtool insert meshdata -imsh=${cemrg_endo} -msh=${FOLDER}/${endo_um}_shift -op=1 -outmsh=${FOLDER}/${endo_um}_shift_fibres"
eval $cmd 

echo "converting carp to vtk"
cmd="meshtool convert -imsh=${FOLDER}/${endo_um}_shift_fibres -ifmt=carp_txt -omsh=${FOLDER}/${endo_um}_shift_fibres -ofmt=vtk"
eval $cmd 