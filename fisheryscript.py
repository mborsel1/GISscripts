import arcpy, sys, itertools

arcpy.env.workspace = r'W:\fishery\~\scals.gdb'

fields1 = ['gearqty', 'cnemarea', 'fzone', 'qdsq', 'tenmsq', 'crew', 'nanglers', 'port', \ 'totalquant', 'trip_days', 'day_fracti', 'gear_days', 'qtykept', 'qtydisc', 'mean_hp', \ 'sd_hp', 'mean_len', 'sd_len', 'mean_gtons', 'sd_gtons', 'size_fleet', 'anon_id', 'fdays']

fields2 = ['gearqty1', 'cnemare1', 'fzone1', 'qdsq1', 'tensmsq1', 'crew1', 'nangler1', \ 'port1', 'tquant1', 'tripdays1', 'dayfract1', 'geardays1', 'qtykept1', 'qtydisc1', \ 'mean_hp1', 'sd_hp1', 'mean_len1', 'sd_len1', 'mean_gton1', 'sd_gtons1', 'sizefleet1', \ 'anonid1', 'fdays1']

# add new fields of type LONG
for fc in arcpy.ListFeatureClasses():
for b in fields2:
arcpy.AddField_management(fc, b, "LONG")
# calculate LONG fields from STR fields
for fc in arcpy.ListFeatureClasses(): 
for a, b in itertools.izip(fields1, fields2):
try:
arcpy.CalculateField_management(fc, b, "!{}!".format(a), "PYTHON_9.3")
except:
pass
# delete all unnecessary string attributes
for fc in arcpy.ListFeatureClasses():
for a in fields1:
arcpy.DeleteField_management(fc, a)
