# FieldSearcher
⚡Quickly find all values of a single categorical field in large JSON datasets!⚡
When you try to use the search function in VSCode to find the value of a categorical field in a large JSON file, you'll notice that the same values keep popping up repeatedly, which is quite frustrating. However, congratulations! By reading this, you have found the remedy.
# Step 1
The tutorial assumes that Python is already installed on the user's computer.
First, open the terminal in the folder where you need to perform the search and enter python json2ndjson.py. This step is to convert your JSON file into an NDJSON file, which will facilitate the FieldSearcher in locating fields.
Then, enter the full name of the JSON file you want to convert (including .json) to complete the conversion to NDJSON.
After completing this step, you will notice that a new NDJSON file has appeared in the folder (the filename will be based on your original JSON file).
# Step 2
In the terminal, enter python acts.py (this is the FieldSearcher itself). Then, input the full name of the NDJSON file you want to search (including .ndjson), and input the field you wish to find. Wait a few seconds, and the results will be saved to the JSON file it specifies.
# Step 3
Open the resulting JSON file with any compiler or editing software to view the results.
