# Atlas Annotation Project (AAP) Requirements
The goal of the atlas annotation project is to create a system for storing, viewing and annotating brain sections.

## Main features
* A web browser based visualization system based on Neuroglancer.
* Persistence back-end based on [DataJoint](https://datajoint.io/) dataflow system.
* System will be able to either as a local installation, in a particular lab, or as a web based installation, using AWS resources.

## DataJoint Schemas
   Can be found [here](https://github.com/ActiveBrainAtlas/Datajoint_Interface/blob/master/project_schemas/atlas_schema_python_v3/creator_atlas_v3.ipynb)

## Work-Flow

[LucidChart Diagrams](https://www.lucidchart.com/documents/embeddedchart/1c75b2c8-f864-4aae-b818-6416fc36d51c)

The sequence of steps 

1. Login
2. Select Brain from Brain Table. Initialize and track moving the files and tranformation to tiles.
3. Enter Neuroglancer using selected brain. Open the Control window.
  In a separate window called "Control", display information about the brain, allow entry of comments, select edit mode.
1. LogOut

## Milestones
We break the development of this project into milestones. The goal is to focus on one set of features at a time and proceed to the next stage once the previous stage is complete. Each milesone defines a "editing mode" that is selected through a button in the control panel.

### Milestone 1 - Manual global alignment of reference atlas to new brain 
Enables the user to perform a global alignment of the atlas to the brain. 

* Display sections in 2-D with countours of landmarks and a 3-D representation.  
* Translation by performing "click-and-deag" or by "hot keys": (X="q"(left),"w"(right); Y="a"(up),"s"(down); Z="z"(higher),"x"(lower); 
* Shear by six "hot keys"(DX="e","r"; DY="d","f"; DZ="c","v"); 
* Rotation by six "hot keys"(pitch="t","y"; yaw="g","h"; rill="b","n").  

### Milestone 2 - Correction of alignment of reference atlas to new brain
Enables the use to correct the alignment by performing local deformations at selected scales.

* Select a landmark for correction.  
* Permit correction of contours or contour segments for individual slices.  
* Correction tool must allow affine correction (translation, rotation, sheer) to the one landmark.  
* Correction tool must allow distorion of the shape of the landmark; note suggested "inner/outer" circle tool.  
* Display sections in 2-D with countours of landmarks and a 3-D representation.   

### Milestone 3 - Addition of new annotation by an expert anatomist 
Add a new structure, which is labeled as a landmark.  
This is performed by drawing a contour to every relevant section in the stack of brain slices.  
Each successive section shows a shadow version of the previous contour for purposes of aiding the anatomist.  
As the contour is drawn in the projections that corresponds to the orientation of the slice, NeuroGlancer will calculate the surface and render it in 3-D. This must be accomplished, at least in an approximate way, instantaneously (i.e., < 20 ms).  
Upon completion of labeling, generate full 3-D (possibly with a delay to reflect communication and computational times) and display.  
Permit correction of contours or contour segments for individual slices. 
Permit notes per new structure.
### Milestone 4 - Labeling of markers
