import plistlib
import os
import argparse

parser = argparse.ArgumentParser(description='Shortcutter tool')

parser.add_argument('-o', '--output', action='store', dest='output',
                    help='The name of your plist file, default = "java_script_file.shortcut"')
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-i', '--input', action='store', dest='input',
                    help='The java script file to insert into the plist file', required=True)

results = parser.parse_args()

bfileName = ""
sfileName = ""
if not results.output:
  output_file = results.input
  if output_file[-3:] == ".js":
    output_file = output_file[:-3]
    bfileName = output_file + ".shortcut"
    sfileName = output_file + ".shortcutXML"
else:
  output_file = results.output
  bfileName = output_file
  sfileName = output_file + "XML"

if os.path.exists(results.input):
  with open(results.input, 'r') as f:
    try:
      d = { 'WFWorkflowActions':[
                                  {'WFWorkflowActionIdentifier':'is.workflow.actions.runjavascriptonwebpage',
                                  'WFWorkflowActionParameters':{'WFJavaScript':f.read()}
                                  }
                                ],
            'WFWorkflowClientRelease':'2.0',
            'WFWorkflowClientVersion':'700',
            'WFWorkflowIcon':{'WFWorkflowIconGlyphNumber':59801,
                              'WFWorkflowIconImageData':b'',
                              'WFWorkflowIconStartColor':4292093695},
            'WFWorkflowImportQuestions':[],
            'WFWorkflowInputContentItemClasses':['WFWorkflowInputContentItemClasses'],
            'WFWorkflowTypes':['NCWidget','WatchKit','ActionExtension'],

              
          }
      with open(sfileName, 'wb') as fp:
        plistlib.dump(d, fp, fmt=plistlib.FMT_XML)
      with open(bfileName, 'wb') as fp:
        plistlib.dump(d, fp, fmt=plistlib.FMT_BINARY)

    except:
      print ("An error happened when trying to open the file")
else:
  print ("Could not open the js file")