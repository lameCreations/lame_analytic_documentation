import csv

class indexInfo(object):
        def __init__(self, description, index, usegroup):
             self.description = description
             self.index = index
             self.usegroup = usegroup
             
class sourcetypeInfo(object):
        def __init__(self, description, index, sourcetype, usegroup):
             self.description = description
             self.index = index
             self.sourcetype = sourcetype
             self.usegroup = usegroup            

class analyticInfo(object):
        def __init__(self, description, eventtypes, hosts, indexes, inputlookups, lookups, myapp, outputlookups, queries, sources, sourcetypes, urlField):
             self.description = description
             self.eventtypes = eventtypes
             self.hosts = hosts
             self.indexes = indexes
             self.inputlookups = inputlookups
             self.lookups = lookups
             self.myapp = myapp
             self.outputlookups = outputlookups
             self.queries = queries
             self.sources = sources
             self.sourcetypes = sourcetypes
             self.urlField = urlField
             


def addStyleSheet():
    styleString = "<style>#toc_container"
    append_text_to_file(file_path, styleString)
    
    styleString = '{background: #f9f9f9 none repeat scroll 0 0; border: 1px solid #aaa; display: table; font-size: 95%; margin: auto; padding: 20px; width: auto; }'
    append_text_to_file(file_path, styleString)
    
    styleString = '.toc_title {font-weight: 700; text-align: left; color: #034f84;}'
    append_text_to_file(file_path, styleString)
    
    styleString = ' #toc_container li, #toc_container ul, #toc_container ul li{list-style: outside none none !important;}'
    append_text_to_file(file_path, styleString)

    styleString = '.mainDiv {border: 1px solid lightblue; text-align: justify; margin: auto; width: 75%; padding: 20px;} '
    append_text_to_file(file_path, styleString)

    styleString = 'h1 {color: #034f84;}'
    append_text_to_file(file_path, styleString)

    styleString = 'h2 {color: #034f84;}'
    append_text_to_file(file_path, styleString)

    styleString = 'h3 {color: #034f84;}'
    append_text_to_file(file_path, styleString)

    styleString = '</style>'
    append_text_to_file(file_path, styleString)

def append_text_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text)
        file.write('\n')
        
def write_new_text_to_file(file_path):
    with open(file_path, "w") as file:
        #file.write(text)
        pass  # Empty block, no need to perform any operations

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

def addIndexInfo():
    indexFilePath = "/opt/splunk/etc/apps/lame_analytic_documentation/lookups/index_info.csv"
    indexCSV = read_csv_file(indexFilePath)

    i = 0

    while i < len(indexCSV):
        newIndex = indexInfo(indexCSV[i][0],indexCSV[i][1],indexCSV[i][2])
        ListOfIndex.append(newIndex)
        i += 1

    stCount = len(ListOfIndex)
    print(stCount)

    writeIndex = '<h1 id="indexes">1. Indexes - count: ' + str(stCount) + '</h1>'
    append_text_to_file(file_path, writeIndex)

    writeIndex = '<table width="100%" border=1>'
    append_text_to_file(file_path, writeIndex)    
    
    writeIndex = '<tr><td><b>Index Name</b></td><td><b>Index Description</b></td></tr>'
    append_text_to_file(file_path, writeIndex)   
    for nIndex in ListOfIndex:
        writeIndex = "<tr>"
        append_text_to_file(file_path, writeIndex)

        tempIndex = nIndex.index
        tempDetails = nIndex.description
        writeIndex = "<td>" + tempIndex + "</td><td>" + tempDetails + "</td>"
        append_text_to_file(file_path, writeIndex)

        writeIndex = "</tr>"
        append_text_to_file(file_path, writeIndex)

    writeIndex = '</table>'
    append_text_to_file(file_path, writeIndex)

    writeIndex = '<p><a href="#top">Back to top of page</a></p>'
    append_text_to_file(file_path, writeIndex)
    
def addSourceType():
    sourcetypeFilePath = "/opt/splunk/etc/apps/lame_analytic_documentation/lookups/sourcetype_info.csv"
    sourcetypeCSV = read_csv_file(sourcetypeFilePath)
    analtyicFilePath = "/opt/splunk/etc/apps/lame_analytic_documentation/lookups/analytics_info.csv"
    analtyicCSV = read_csv_file(analtyicFilePath)

    i = 0

    while i < len(sourcetypeCSV):
        newSourcetype = sourcetypeInfo(sourcetypeCSV[i][0],sourcetypeCSV[i][1],sourcetypeCSV[i][2],sourcetypeCSV[i][3])
        ListOfSourceType.append(newSourcetype)
        i += 1

    #stCount = ListOfSourceType.length
    stCount = ListOfSourceType.count

    i = 0
    while i < len(analtyicCSV):
        newAnalytic = analyticInfo(analtyicCSV[i][0],analtyicCSV[i][1],analtyicCSV[i][2],analtyicCSV[i][3],analtyicCSV[i][4],analtyicCSV[i][5],analtyicCSV[i][6],analtyicCSV[i][7],analtyicCSV[i][8],analtyicCSV[i][9],analtyicCSV[i][10],analtyicCSV[i][11])
        ListOfAnalytic.append(newAnalytic)
        i += 1

    writeSourcetype = '<h1 id="sourcetypes">2. Sourcetypes - count:' + str(stCount) + '</h1>'
    append_text_to_file(file_path, writeSourcetype)

    tempCounter = 0
    for nSourceType in ListOfSourceType:
        #print("Hello")
        if tempCounter != 0 :
             
            tempIndex = nSourceType.sourcetype
            
            tempDetails = nSourceType.description
                    
            writeSourcetype = '<h2>' + tempIndex + '</h2>'
            append_text_to_file(file_path, writeSourcetype)

            writeSourcetype = "<p><b>Sourcetype Description</b></p>"
            append_text_to_file(file_path, writeSourcetype)

            writeSourcetype = "<p>" + tempDetails + "</p>"
            append_text_to_file(file_path, writeSourcetype)

            for loopSourcetype in ListOfSourceType:
                if loopSourcetype.sourcetype == nSourceType.sourcetype:
                
                    analyticTemp = 0
                    for nAnalytic in ListOfAnalytic:
                        modSourceType = "sourcetype=" + nSourceType.sourcetype
                        if modSourceType == nAnalytic.sourcetypes:
                            if analyticTemp == 0:
                                subTable = "<h3>Analytic</h3>"
                                append_text_to_file(file_path, subTable)
                            
                            metric_description = nAnalytic.description
                            metric_query = nAnalytic.queries

                            subTable = "<h3>Description: " + nAnalytic.description + "</h3>"
                            append_text_to_file(file_path, subTable)

                            subTable = '<h3>' + metric_query + '</h3>'
                            append_text_to_file(file_path, subTable)

                            analyticTemp += 1

                                
                    
                        writeSourcetype = '</table>'
                        append_text_to_file(file_path, writeSourcetype)      

            
            writeSourcetype = '<p><a href="#top">Back to top of page</a></p>'
            append_text_to_file(file_path, writeSourcetype)     

        tempCounter += 1
ListOfIndex = []
ListOfSourceType = []
ListOfSource = []
ListOfAnalytic = []

file_path = "/opt/splunk/etc/apps/lame_analytic_documentation/appserver/static/CS_doc.htm"
#file_path = "/home/troy/Desktop/testFile.htm"
write_new_text_to_file(file_path)

webString = '<!DOCTYPE html>'
append_text_to_file(file_path, webString)

webString = '<html lang="en">'
append_text_to_file(file_path, webString)

webString = '<head>' 
append_text_to_file(file_path, webString)

addStyleSheet()

webstring = '</head>'
append_text_to_file(file_path, webString)

webString = '</html>'
append_text_to_file(file_path, webString)

webString = '<body><div class="mainDiv"><a name="top"></a><table><tr><td><div id="toc_container"><p class="toc_title">Table of Contents</p><ul class="toc_list"><li><a href="#indexes">1. Indexes</a></li><li><a href="#sourcetypes">2. Sourcetypes</a></li><li><a href="#sources">3. Sources</a></li></ul></div></td></tr></table>'
append_text_to_file(file_path, webString)

addIndexInfo()
addSourceType()

#add-source

webString = '</div></body>'
append_text_to_file(file_path, webString)

