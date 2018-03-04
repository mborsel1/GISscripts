# treecount

I scripted a tool in ArcMap that could be run through the ModelBuilder interface or in a standalone fashion.  Its purpose is to summarize the number of trees within a specified distance of a building that have certain attributes.  It accomplishes this by copying the building layer, counting the number of trees within a specified distance of a building, and then updating the copied building layer’s attribute table with those counts.  The tool is called TreeCount.  
	TreeCount asks for six parameters, five as inputs and one as an output.  The five inputs are workspace environment, building layer (polygons), tree layer (points), buffer distance, and tree characteristic of interest.  The output is the location of where the copied and updated building layer should be saved.  In its current state, the user has the choice of three tree characteristics:  tree condition, tree location, and tree pit.  In the code, each choice corresponds to a list of field names that will be added to the new building layer upon execution.  The tool was designed to work with NYC Open Data’s building footprint data and tree census data which are available for the five boroughs.  However, I believe the strength of this tool is that with very little manipulation, it can be altered to accept many different configurations.  For example, the tree characteristics and their lists of field names can easily be changed to allow for different or more options.  
	The following describes how the code works – examples are below each step in parantheses: 


1. The user selects all input and output parameters.
(User selects “workspace” = Workspace,  “building” = Building Layer, “tree” = Tree Layer, “20 feet” = Buffer Distance, “Tree Pit” = Tree Characteristic, and “~/newbuilding.shp” = Output Location.)
2. First, the tool creates a feature layer from the tree point layer.  It then copies the building layer and makes that a feature layer.  This will be the specified output.
(Copy “building”, save to “~/newbuilding.shp”.)
3. The tool will identify which code block should be executed via an if-statement that corresponds to the tree characteristic input.  
(Selected characteristic is “Tree Pit”)
4. It will then add the list of fields for that characteristic to the attribute table of the new building layer; this is accomplished via a for-statement.  
(Tree Pit corresponds to how a tree is planted in the ground.  Add fields from the list that reflects that choice to “newbuilding”.  The new fields are “Sidewalk”, “Continuous”, and “Lawn”.)
5. It then moves into another for-statement, this time nested within a with-statement utilizing the SearchCursor function.  The tool will select each building footprint one-by-one using the building’s unique identifier.  
(Select “newbuilding” polygons by unique identifier “FID”.)
6. Based on the selected building, it will then select all tree points within the specified buffer of the building.
(Select points from “tree” that are within “20 feet” of the single selected building in “newbuilding”.  For example, four tree points are within 20 feet of the first building polygon and will be selected.)
7. It will then update an empty list with every selected point’s value in the field corresponding to the selected tree characteristic.  
(The “tree” field that corresponds with “Tree Pit” is called “SITE”.  The four selected tree points have SITE values of 3, 3, 1, and 2 which are added to the empty list.
8. It enters another for-loop, this time utilizing the UpdateCursor function.  This loop will update the new building layer’s new fields based on the counts of each point with a specified value.  It does this using several if-else-statements.
(For the selected building polygon in “newbuilding”, update the added fields “Sidewalk”, “Continuous”, and “Lawn”.  In the list, if the count of values that equal 1 is greater than zero, add that count to the field “Sidewalk”.  If equal to 2 or 3, add that count to the field “Continuous” or “Lawn”, respectively.  If the count is equal to 0, update the corresponding field with the value of 0.)
9. Finally, the loop updates all rows to reflect the changes.  
(At this point, the code selects the next building polygon based on “FID” and repeats the process.)
10. Steps 5 through 9 will repeat until all building polygons have been iterated through.  The code will complete and add the new building layer to the display.
