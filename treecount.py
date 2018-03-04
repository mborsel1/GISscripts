import arcpy
import os
import sys
import string

#workspace
arcpy.env.workspace = wspace = arcpy.GetParameterAsText(0)

#buildings
layer = arcpy.GetParameterAsText(1)

#trees
trees = arcpy.GetParameterAsText(2)

#buffer building to search
buffer = arcpy.GetParameterAsText(3)

#tree field interested in - tree condition, tree location, or tree pit
tf = arcpy.GetParameterAsText(4)

#output file
output = arcpy.GetParameterAsText(5)

#make feature layers to reference
treelayer = arcpy.MakeFeatureLayer_management(trees, trees + ".lyr")
templayer = arcpy.CopyFeatures_management(layer, "in_memory")
fc = arcpy.MakeFeatureLayer_management(templayer, output)

#arcpy.DisperseMarkers_cartography(treelayer, "1 Point", "EXPANDED")

condit = ["Excellent", "Good", "Poor", "Dead", "Shaft", "Stump", "Empty"]
loc = ["Front", "Side", "Rear", "Median", "Other"]
pit = ["Sidewalk", "Continuous", "Lawn"]

def countfunc():
	if tf == "Tree Condition":
		#add fields
		for a in condit:
			arcpy.AddField_management(fc, a, "SHORT")		

		with arcpy.da.SearchCursor(fc, ["FID"]) as fcrows:
			for a in fcrows:
				
				#iterate through each row
arcpy.SelectLayerByAttribute_management(fc, "NEW_SELECTION", \ "FID={}".format(a[0]))
				
				#select trees in treelayer within buffer distance of row object
arcpy.SelectLayerByLocation_management(treelayer, \ "WITHIN_A_DISTANCE", fc, buffer, "NEW_SELECTION")
			
				#add values from TREECONDIT for selected trees to list
				tlrows = arcpy.da.SearchCursor(treelayer, "TREECONDIT")
				list1 = []
				for tlrow in tlrows:
					list1.append(int(tlrow[0]))
						
#count number of appearances of a number in list and add it to correct field in fc
				fcrows1 = arcpy.da.UpdateCursor(fc, condit)
				for fcrow1 in fcrows1:
					if list1.count(1) > 0:
						fcrow1[0] = list1.count(1)
					else:
						fcrow1[0] = 0
					if list1.count(2) > 0:
						fcrow1[1] = list1.count(2)
					else:
						fcrow1[1] = 0
					if list1.count(3) > 0:
						fcrow1[2] = list1.count(3)
					else:
						fcrow1[2] = 0
					if list1.count(4) > 0:
						fcrow1[3] = list1.count(4)
					else:
						fcrow1[3] = 0
					if list1.count(5) > 0:
						fcrow1[4] = list1.count(5)
					else:
						fcrow1[4] = 0
					if list1.count(6) > 0:
						fcrow1[5] = list1.count(6)
					else:
						fcrow1[5] = 0
					if list1.count(7) > 0:
						fcrow1[6] = list1.count(7)
					else:
						fcrow1[6] = 0
					fcrows1.updateRow(fcrow1)
arcpy.SelectLayerByAttribute_management(fc, \ "CLEAR_SELECTION")
	elif tf == "Tree Location":
		for a in loc:
			arcpy.AddField_management(fc, a, "SHORT")
		
		with arcpy.da.SearchCursor(fc, ["FID"]) as fcrows:
			for a in fcrows:				
arcpy.SelectLayerByAttribute_management(fc, "NEW_SELECTION", \ "FID={}".format(a[0]))
arcpy.SelectLayerByLocation_management(treelayer, \ "WITHIN_A_DISTANCE", fc, buffer, "NEW_SELECTION")
				
				tlrows = arcpy.da.SearchCursor(treelayer, "TREELOCATI")
				list1 = []
				for tlrow in tlrows:					
					list1.append(int(tlrow[0]))		

				fcrows1 = arcpy.da.UpdateCursor(fc, loc)
				for fcrow1 in fcrows1:
					if list1.count(1) > 0:
						fcrow1[0] = list1.count(1)
					else:
						fcrow1[0] = 0
					if list1.count(2) > 0:
						fcrow1[1] = list1.count(2)
					else:
						fcrow1[1] = 0
					if list1.count(3) > 0:
						fcrow1[2] = list1.count(3)
					else:
						fcrow1[2] = 0
					if list1.count(6) > 0:
						fcrow1[3] = list1.count(6)
					else:
						fcrow1[3] = 0	
					list2 = []
					list2.append(list1.count(4))
					list2.append(list1.count(7))
					list2.append(list1.count(8))
					list2.append(list1.count(9))
					fcrow1[4] = sum(list2)
		
					fcrows1.updateRow(fcrow1)
arcpy.SelectLayerByAttribute_management(fc, \ "CLEAR_SELECTION")
	else:
		for a in pit:
			arcpy.AddField_management(fc, a, "SHORT")
	
		with arcpy.da.SearchCursor(fc, ["FID"]) as fcrows:
			for a in fcrows:			
arcpy.SelectLayerByAttribute_management(fc, "NEW_SELECTION", \ "FID={}".format(a[0]))
arcpy.SelectLayerByLocation_management(treelayer, \ "WITHIN_A_DISTANCE", fc, buffer, "NEW_SELECTION")
		
				tlrows = arcpy.da.SearchCursor(treelayer, "SITE")
				list1 = []
				for tlrow in tlrows:			
					list1.append(int(tlrow[0]))		

				fcrows1 = arcpy.da.UpdateCursor(fc, pit)
				for fcrow1 in fcrows1:
					if list1.count(1) > 0:
						fcrow1[0] = list1.count(1)
					else:
						fcrow1[0] = 0
					if list1.count(2) > 0:
						fcrow1[1] = list1.count(2)
					else:
						fcrow1[1] = 0
					if list1.count(3) > 0:
						fcrow1[2] = list1.count(3)
					else:
						fcrow1[2] = 0
					fcrows1.updateRow(fcrow1)
arcpy.SelectLayerByAttribute_management(fc, \ "CLEAR_SELECTION")

countfunc()
