#!/bin/bash

clear

# ./transfrom_CemrgApp_fibres.sh /path/to/endo_um /path/to/CemrgApp_mesh

FOLDER="/data/Dropbox/Segmentations/2016111001EP/final_heart"
fchMesh="myocardium_AV_FEC_BB" 
la_fibMesh="/data/Dropbox/Segmentations/2016111001EP/final_heart/LA_endo_fch/fibres_inc_uvc/la_fibres"
ra_fibMesh="/data/Dropbox/Segmentations/2016111001EP/final_heart/RA_endo_fch/fibres_inc_uvc/ra_fibres"

echo "translating mesh"
cmd="perl /home/rb21/Software/cm2carp/bin/return_carp2original_coord.pl ${FOLDER}/${fchMesh}.pts 1 -59540 -252800 1229000 > ${FOLDER}/${fchMesh}_shift.pts"
eval $cmd

echo "creating shift.elem file"
cmd="cp ${FOLDER}/${fchMesh}.elem ${FOLDER}/${fchMesh}_shift.elem"
eval $cmd

echo "creating shift.lon file"
cmd="cp ${FOLDER}/${fchMesh}.lon ${FOLDER}/${fchMesh}_shift.lon"
eval $cmd

echo "inserting meshdata onto 4 chamber mesh"
cmd="meshtool insert meshdata -imsh=${la_fibMesh} -msh=${FOLDER}/${fchMesh}_shift -op=1 -outmsh=${FOLDER}/${fchMesh}_w_la_fib"
eval $cmd 

echo "inserting meshdata onto 4 chamber mesh"
cmd="meshtool insert meshdata -imsh=${ra_fibMesh} -msh=${FOLDER}/${fchMesh}_w_la_fib -op=1 -outmsh=${FOLDER}/${fchMesh}_w_full_fib"
eval $cmd 

echo "converting carp to vtk"
cmd="meshtool convert -imsh=${FOLDER}/${fchMesh}_w_full_fib -ifmt=carp_txt -omsh=${FOLDER}/${fchMesh}_w_full_fib -ofmt=vtk"
eval $cmd 