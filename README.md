# New-York-City-Tree-Finder

The file trees.db is an SQLite database that contains an (abridged) census of all the trees in New York City. The database contains a single table called Trees. Each row corresponds to a single tree somewhere in New York. Among other things, this database contains columns detailing the species of the tree, the tree’s latitude and the tree’s longitude. (You can also see the data in the Excel file trees.csv: the column names in that file correspond exactly to the column names in SQLite database.)

The program asks the user to enter a Latitude and a Longitude and finds the closest tree to that point, and then print out the species of that tree, and the distance of that tree to the point. 
