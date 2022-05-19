##################################################################################################
READ ME
##################################################################################################
Pipeline for putting atrial fibres on a four chamber mesh (using version of CemrgApp designed for meshes with necessary veins).

--------------------------------------------------------------------------------------------------
Before running the pipeline you must:
- Have surfaces with endo and epi fibres from CemrgApp (likely to be called Labelled_Endo and Labelled_Epi). Both endo and epi fibres are mapped onto the endo surface. 
- If the .lon fibres are not in the correct format, run the 1_prepare_fibres.sh script to correct. Check that a vtk of the surfaces can be opened in paraview.
- Move the vtk files into a folder called "LA_endo_fch" or "RA_endo_fch" inside the "final_heart" folder i.e the one containing the myocardium mesh and folders containing the LA/RA UVCs. 
- Within these folders, have separate endo and epi folders.
- Rename the surfaces i.e. LA_endo_cemrg
- Copy the LA endo surface from the surfaces_UVC_LA folder (i.e. one of the epi_endo_CC.part* surfaces) and rename it La_endo_um

The following files should now be present within the "final_heart" folder (LA_endo example but also LA_epi, RA_endo and RA_epi):
- /LA_endo_fch/endo/LA_endo_cemrg.vtk
- /LA_endo_fch/endo/LA_endo_um.vtk

- You must also know the transformation that has been applied to the segmentation during the meshing stage. Find the origin of the smooted segmentation by loading the .nrrd file in itksnap and looking in tools --> image info. Remember to x1000 to move from mm to um.

Finally, the UVC solution that will be used to compute the normal direction through the surface mesh is defined on the nodes, but must be defined on the elements here. Use meshtool interpolate node2elem to create la.uvc_rho_e.dat. 

--------------------------------------------------------------------------------------------------
MAIN PIPELINE
- Within the 2a_transfrom_CemrgApp_fibres_endo.sh script, change the transformation that is being applied. 
- Run 2a_transform_CemrgApp_fibres_endo.sh
- Repeat for 2b, 2c, 2d and 2f - but remember that each of these contains the transformation that must be changed. It would be best to edit these scripts to give the transformation as an input. 
- Beware that 2e and 2f require the path to the surfaces_UVC_LA/la/uvc folder to be given (i.e. the path to the volume mesh) and will create la_shift in this folder. Consider changing this. 

- The CemrgApp atrial fibres pipeline required a large part of the lower atria to be removed when the mitral/tricuspid valve was cropped. No fibres will be mapped to this area. 
- Run 3a_add_fibres_atria.sh to loop over the default fibres (1 0 0) and replace them with the nearest non-deafult fibres.
- Run 3b, 3c and 3d.

- The epi and endo fibres are both mapped to the endo. We must assign appropriate fibres directions to each element within the volume mesh. 
- Open 4a_assign_la_epi_endo.sh and ensure the paths to the volume mesh and the UVC solution      (defined on the elements!) are correct. Repeat for 4b_assign_la_epi_endo.sh. 
- Run 4a_assign_la_epi_endo.sh
- Run 4b_assign_la_epi_endo.sh
- To visualise results at this stage, .pts and .elem files from surfaces_UVC_LA/la/uvc/la_shift will need to be copied into the folder to create the vtk.

- CemrgApp only provides fibre directions, not sheet directions. 
- Run 5a_find_sheet.sh
- Run 5b_find_sheet.sh

- The sheet directions created by 5a and 5b should be normalised and orthognal to the fibre directions. 
- Run 6a_check_orthogonals.py (python not .sh!) to check they are orthogonal. 
- This script will also concatenate the fibres and sheet directions. 
- Check la_fibres.lon to ensure this looks sensible (i.e. header = 2 / 6 columns / norm = 1)
- Repeat with 6b_check orthogonals.py

- Finally, the four chamber mesh must be tranformed to the same space as the fibres and the new fibres must be inserted. 
- Run 7_transform_myocardium.sh.
- Delete myocardium_AV_FEC_BB_w_la_fib files are these are irrelevant but keep _shift files for comparison with CT in future. 

--------------------------------------------------------------------------------------------------
THINGS TO CHECK:
- Fibres are not your friend. Check again in myocardium_AV_FEC_BB_w_full_fib.lon to make sure nothing looks suspicious (i.e. header = 2 / 6 columns / norm = 1).
- Visualise the fibres and make sure they point in sensible directions. 
- Visualise a small selection of fibres and sheets (use arrows) in both the LA and RA and make sure they look like they could be 90 deg from one another. 

--------------------------------------------------------------------------------------------------
FINALLY:
- Move the myocardium_AV_FEC_BB_w_full_fib files into your sims_folder.
- Pray to a higher power.
