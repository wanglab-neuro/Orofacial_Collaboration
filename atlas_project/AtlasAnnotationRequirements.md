# Atlas Annotation Project (AAP) Requirements
The goal of the atlas annotation project is to create a system for storing, viewing and annotating brain sections.

## Main features
* A web browser based visualization system based on Neuroglancer.
* Persistence back-end based on [DataJoint](https://datajoint.io/) dataflow system.
* System will be able to either as a local installation, in a particular lab, or as a web based installation, using AWS resources.


## Milestone 1 - Manual global alignment of reference atlas to new brain
Load an unprocessed brain.  
Add the reference atlas with affine procedures (translation, rotation, sheer) that are common to all landmarks.  
Display sections in 2-D with countours of landmarks and a 3-D representation.  
Translation by "grabbing" any landmark or by six "hot keys" (X="q","w"; Y="a","s"; Z="z","x"); sheer by six "hot keys"(DX="e","r"; DY="d","f"; DZ="c","v"); and rotation by six "hot keys"(pitch="t","y"; yaw="g","h"; rill="b","n").  
## Milestone 2 - Correction of alignment of reference atlas to new brain
Load a brain that has been processed for alignment with the reference atlas.   
Select a landmark for correction.  
Permit correction of contours or contour segments for individual slices.  
Correction tool must allow affine correction (translation, rotation, sheer) to the one landmark.  
Correction tool must allow distorion of the shape of the landmark; note suggested "inner/outer" circle tool.  
Display sections in 2-D with countours of landmarks and a 3-D representation.   
## Milestone 3 - Addition of new annotation by an expert anatomist
Load a brain.  
Add a new structure, which is labeled as a landmark.  
This is performed by drawing a contour to every relevant section in the stack of brain slices.  
Each successive section shows a shadow version of the previous contour for purposes of aiding the anatomist.  
As the contour is drawn in the projections that corresponds to the orientation of the slice, NeuroGlancer will calculate the surface and render it in 3-D. This must be accomplished, at least in an approximate way, instantaneously (i.e., < 20 ms).  
Upon completion of labeling, generate full 3-D (possibly with a delay to reflect communication and computational times) and display.  
Permit correction of contours or contour segments for individual slices. 
Permit notes per new structure.
## Milestone 4 - Labeling of markers
