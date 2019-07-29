# shortcutter
Shortcuts are Javascript scripts wrapped in a binary property list. This script generates iOS Shortcuts by providing a .js file as an input, wrapping it in the necessary XML and then converting it to a binary property list. The output file should be named with a .shortcut extension if you want to run the file on a device and can be converted back to xml1 with plutil if you want to validate the contents prior to distribution. 

Note: Use python3, python2 seems to fail with the plists dump() function.

# Usage pattern 
python3 shortcutter.py [-h] [-o OUTPUT] -i INPUT

# Example
python3 shortcutter.py -i somefile.js -o outputName
or
python3 shortcutter.py -i somefile.js

# Help
You can check the script options with -h, the result will be the next:

optional arguments:
-h, --help show this help message and exit
-o OUTPUT, --output OUTPUT
The name of your plist file, default =
"java_script_file.shortcut"

required named arguments:
-i INPUT, --input INPUT
The java script file to insert into the plist file
