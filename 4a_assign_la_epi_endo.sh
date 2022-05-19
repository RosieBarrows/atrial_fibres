#!/bin/bash

clear

CARPFOLDER="home/rb21/Software/CARPentry_KCL_latest/bin/"

echo "Make new folder"
cmd="mkdir /data/Dropbox/Segmentations/2016111001EP/final_heart/LA_endo_fch/fibres_inc_uvc"
eval $cmd

fibres_mshPath="/data/Dropbox/Segmentations/2016111001EP/final_heart/LA_endo_fch"
fibres_mshName_endo="/endo/LA_endo_um_shift_fibres_corrected"
output_folder="/data/Dropbox/Segmentations/2016111001EP/final_heart/LA_endo_fch/fibres_inc_uvc"
fibres_output_name="LA_endo"

la_mshPath="/data/Dropbox/Segmentations/2016111001EP/final_heart/surfaces_UVC_LA/la/uvc"
la_mshName="la_shift"
la_output_name="LA_vol"

UVCpath="/data/Dropbox/Segmentations/2016111001EP/final_heart/surfaces_UVC_LA/la/uvc/la.uvc_rho_e.dat"

fibres_mshName_epi="/epi/LA_endo_um_shift_fibres_corrected"

echo "Generating surface element centres..."
cmd="GlElemCenters -m ${fibres_mshPath}/${fibres_mshName_endo} -o ${output_folder}/${fibres_output_name}_ECs.pts"
echo $cmd
eval $cmd  

echo "Generating volume element centres..."
cmd="GlElemCenters -m ${la_mshPath}/${la_mshName} -o ${output_folder}/${la_output_name}_ECs.pts"
echo $cmd
eval $cmd  

echo "Loop over volume elements and assign best fibre direction based on UVCs"
cmd="python epi_endo_loop.py ${fibres_mshPath}/${fibres_mshName_endo} ${la_mshPath}/${la_mshName} ${output_folder} ${output_folder}/${fibres_output_name}_ECs.pts ${output_folder}/${la_output_name}_ECs.pts ${UVCpath} ${fibres_mshPath}/${fibres_mshName_epi}"
echo $cmd
eval $cmd  




