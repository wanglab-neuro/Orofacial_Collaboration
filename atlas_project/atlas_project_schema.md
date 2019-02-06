## Graphical representation of current schema (common_atlas_v2)

Pipeline begins with relevant mouse metadata and a single key as the name. Each mouse can have multiple injections, and finally a single perfusion before the brain is extracted. The Histology field contains information about the slices made into the brain. These tables concern the preparation of the physical brain and the fields are agreed upon by those who actually prepare the brains, overseen by Beth Friedman. These tables all require manual input.

The following "BrainStack" table, and subtables "RawSlices" and "ProcessedSlices" encompass the computational side of the pipeline. "BrainStack" contains all needed metainformation on a stack before being entered into the atlas pipeline. The slice subtables contain information on where image files are stored on the cloud for easy retrieval.

![Image](images/atlas_schema_v2_long.png)

## All current stacks

Information on how to access all tables in the database as well as download all images from AWS S3 can be found [in this Jupyter Notebook.](https://github.com/ActiveBrainAtlas/Datajoint_Interface/blob/master/project_schemas/atlas_schema_python/Accessing%20Atlas%20Data_v2.ipynb)

Entries in all tables can be easily viewed by registered users using [Helium](http://ucsd-demo-helium.datajoint.io/login?from_user=alex&from_host=ucsd-demo-db.datajoint.io&from_path=%2Ftables%2Fcommon_u19_database%2Fbrain) hosted at `ucsd-demo-db.datajoint.io`.

## Table fields
