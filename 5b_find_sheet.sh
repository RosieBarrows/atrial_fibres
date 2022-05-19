!#/bin/bash

clear

CARPFOLDER="home/rb21/Software/CARPentry_KCL_latest/bin/"

mshPath="/data/Dropbox/Segmentations/2016111001EP/final_heart/RA_endo_fch/fibres_inc_uvc"
mshName="fibres_from_uvc"
UVCs="/data/Dropbox/Segmentations/2016111001EP/final_heart/surfaces_UVC_RA/ra/uvc/ra.uvc_rho_e.dat"

echo "finding gradient of UVCs"
cmd="GlGradient -m ${mshPath}/${mshName} -S elem_ctr -t elem_ctr -d ${UVCs} -o ${mshPath}/fibres_from_uvc_grad"
eval $cmd

echo "Find rotation axes for surface normal to sheet direction"
cmd="python /data/Dropbox/scripts/atrial_fibres/find_axes.py ${mshPath}/${mshName} ${mshPath}/fibres_from_uvc_grad.ctr.grad.vec"
echo $cmd
eval $cmd

echo "creating elem file"
cmd="cp ${mshPath}/${mshName}.elem ${mshPath}/${mshName}_axis.elem"
eval $cmd

echo "creating pts file"
cmd="cp ${mshPath}/${mshName}.pts ${mshPath}/${mshName}_axis.pts"
eval $cmd

echo "Convert to vtk"
cmd="meshtool convert -imsh=${mshPath}/${mshName}_axis -ifmt=carp_txt -omsh=${mshPath}/${mshName}_axis -ofmt=vtk"
echo $cmd
eval $cmd

echo "Find and correct sheet direction"
cmd="python /data/Dropbox/scripts/atrial_fibres/correct_sheet.py ${mshPath}/${mshName} ${mshPath}/fibres_from_uvc_grad.ctr.grad.vec ${mshPath}/fibres_from_uvc_axis"
echo $cmd
eval $cmd

echo "creating elem file"
cmd="cp ${mshPath}/${mshName}.elem ${mshPath}/${mshName}_sheet.elem"
eval $cmd

echo "creating pts file"
cmd="cp ${mshPath}/${mshName}.pts ${mshPath}/${mshName}_sheet.pts"
eval $cmd

echo "Convert to vtk"
cmd="meshtool convert -imsh=${mshPath}/${mshName}_sheet -ifmt=carp_txt -omsh=${mshPath}/${mshName}_sheet -ofmt=vtk"
echo $cmd
eval $cmd