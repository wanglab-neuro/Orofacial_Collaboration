# Orofacial_Collaboration

This repository is a directory of code and data repositories of the orofacial U19.

## Code and Document Repositories
* **Kleinfeld Lab**
    * [Active Brain Atlas Repo](https://github.com/ActiveBrainAtlas/MouseBrainAtlas_dev)
    * [In Depth Description of Active Atlas Pipeline Scripts and Outputs](https://github.com/ActiveBrainAtlas/MouseBrainAtlas_dev/blob/master/doc/running_scripts.md#preprocess-setup)
    * [Yoav Freund: Shapeology Project](https://github.com/yoavfreund/shapeology_code) using low-D manifolds to define shape descriptors.
* **Wang Lab**
   * [Wang lab: shared files](https://github.com/wanglab-duke/Orofacial_U19_Shared_Files)
* **Karel Lab**
   * [Karel lab: Mesoscale Activity Map Github](https://github.com/mesoscale-activity-map)
   * [Karel lab: Mesoscale Activity Map pipeline document](https://docs.google.com/document/d/1oyQkLSiOoIO6xXY3yD5Y3h6RRNo_RuHU13DBsSPUKOc/edit#heading=h.3njo67guvukt)

## Datajoint Schemas

* [Datajoint Interface Repo](https://github.com/ActiveBrainAtlas/Datajoint_Interface) contains code and documentation for workflows using the DataJoint server and API. The major users of Data are Alex Newberry and Conrad Foo in the Kleinfeld Lab, and Vincent Provosto in the Wang Lab.
   * [Active Atlas Schema](https://github.com/ActiveBrainAtlas/Orofacial_Collaboration/blob/master/atlas_project/README.md)
   * [Conrad Schema](https://github.com/ActiveBrainAtlas/Orofacial_Collaboration/blob/master/atlas_project/Conrad_Schema.md)
   * [Vincent Schema](https://github.com/wanglab-duke/Orofacial_U19_Shared_Files)
  
## Data Repositories

### Atlas Project
* [UCSD Active Brain Atlas S3 raw data bucket](https://s3.console.aws.amazon.com/s3/buckets/mousebrainatlas-rawdata/?region=us-east-1&tab=overview)
   * Bucket name: `s3://mousebrainatlas-rawdata`
* [UCSD Active Brain Atlas S3 data bucket](https://s3.console.aws.amazon.com/s3/buckets/mousebrainatlas-data/?region=us-east-1&tab=overview)  
   * Bucket name: `s3://mousebrainatlas-data`
   * Example lossless images: `s3://mousebrainatlas-data/CSHL_data_processed/MD585/MD585_prep2_lossless/`
* UCSD Active Brain Atlas birdstore storage (Kleinfeld Lab local server)
   * Raw Data: `/nfs/birdstore-brainbucket1/Active_Atlas_Data/[SCANNER_NAME]/`
   * Processed Data: `/nfs/birdstore-brainbucket1/Active_Atlas_Data/data_root/CSHL_data_processed/`
   
## Demos

### Atlas Project
* [Annotation Software Video Demonstrations on Dropbox](https://www.dropbox.com/sh/ug683gbt50h41bt/AABHvQPstbbvla6zoLz0JQU4a?dl=0)
