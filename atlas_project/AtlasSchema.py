
## This version extracted from 
# Datajoint_Interface/project_schemas/atlas_schema_python_v3/creator_atlas_v3.ipynb
# On  07/10/2019

@schema
class Mouse(dj.Manual):
    definition = """
    mouse : char(18)                   # Name for lab mouse, max 8 chars
    -------
    date_of_birth  : date              # (date) the mouse's date of birth
    sex            : enum('M','F') # (M/F) either 'M' for male, 'F' for female
    genotype       : enum('C57','U')     # (Lookup) indicating the genotype
    weight         : double            # (int) weight of the mouse in grams. -1 if unknown
    bred           : varchar(20)       # (Str) Vendor where the mouse was bred (bred in house, \
    #purchased by vendor)
    """
    
@schema
class Perfusion(dj.Manual): # Everyone should be doing the same type of perfusion
    definition = """
    -> Mouse                        # One injection per mouse
    ----------
    injection_date  : date          # (date) what day was the injection performed
    post_fixation_condition_hours  : int   # (int) How long kept in fix (overnight)
    percent_sucrose_of_fix         : int   # (int) 10 or 20 percent for CSHL stuff

    date_frozen    : date     # (date) The date the brain was frozen
    date_sectioned : date     # (date) The date the brain was sectioned

    injection_type  : varchar(30)   # (Str) what kind of tracer/injection
    perfusion_lab   : varchar(30)   # (Str) Which lab perfused the mouse? This lab also kept the mouse
    
    assessment=''   : varchar(1000) # (Str) optional, qualitative assessment of injection
    """
    
@schema
class Injection(dj.Manual): # Viral injections
    definition = """
    -> Mouse                        # One injection per mouse
    injection_number : int          # iterative, how many injections have already been performed
    -------
    DK*injection_location, M-L  : double          # (medial-lateral coordinates) where was the injection performed
    DK*injection_location, R-C  : double          # (rostral-caudal coordinates) where was the injection performed
    DK*injection_location, D-V  : double          # (dorsal - medial coordinates) where was the injection performed    injection_date  : date          # (date) what day was the injection performed
    injection_type  : varchar(30)   # (Str) what kind of tracer/injection (flourescent?)
    injection_length: int           # UNSURE. Assumed: the length of time the virus was allowed to propagate
    
    assessment=''   : varchar(1000) # (Str) qualitative assessment of injection
    """
    
@schema
class Histology(dj.Manual):
    definition = """
    -> Mouse                        # One Histology per injection per mouse
    ------------
    region         : varchar(10)    # (Str) [UNSURE]
    thickness      : int            # (int) thickness of each slice in microns
    orientation    : enum('sagittal','coronal','horozontal')    # (Str) horizontal, sagittal, coronal
    counter_stain  : varchar(30)    # (Str) what stain was used on the brain (thionin or NeuroTrace)
    lab            : varchar(20)    # (Str) Which lab did the histology
    series         : enum('all','every other','unknown') # Every section OR alternate sections
    """
# AFTER sectioning, the reporter can either be directly visualized with fuorscence or needs to be 
#  amplified with immunostaining
# Hannah, with Axio Scanner, will manually select level of exposure to reduce saturation but make sure the 
#  the fluorescent molecules are visible
#    - add: CSHL_did_their_own_blackbox_preprocessing : True or False
# Assume calibration

@schema 
class Stack(dj.Manual):
    definition = """
    -> Histology            # One Histology per injection per mouse
    ------------
    stack_name       : varchar(10)   # (Str) unique designation for each mouse
    num_slices       : int           # (int) total number of histology slices
    num_valid_slices : int           # (int) total number of useable histology slices
    channels         : int           # (int) number of channels for each slice
    human_annotated  : boolean       # (bool) does this stack have human annotations

    planar_resolution_um : double    # (double) 0.325 for AxioScanner, 0.46 from CSHL
    section_thickness_um : double    # (double) typically 20um
    
    unique index (stack_name)   # Adds constraint, stack name must be unique accross brains
    """
