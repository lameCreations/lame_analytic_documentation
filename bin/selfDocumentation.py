import csv

appFilePath = "lame_analytic_documentation"

class indexInfo(object):
        def __init__(self, description, index, usegroup):
             self.description = description
             self.index = index
             self.usegroup = usegroup

class dashboardInfo(object):
        def __init__(self, app, details, mitre, urlField):
            self.app = app
            self.details = details
            self.mitre = mitre
            self.urlField = urlField    

class savedSearchInfo(object):
        def __init__(self, actions, app, cron_schedule, details, mitre, title):
            self.actions = actions
            self.app = app
            self.cron_schedule = cron_schedule
            self.details = details
            self.mitre = mitre
            self.title = title    

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
             
class sourceInfo(object):
        def __init__(self, description, index, source, usegroup):
            self.description = description
            self.index = index
            self.source = source
            self.usegroup = usegroup

def addStyleSheet():
    styleString = "<style>#toc_container"
    append_text_to_file(file_path, styleString)
    
    styleString = '{background: #526D82 none repeat scroll 0 0; border: 1px solid #aaa; display: table; font-size: 95%; margin: auto; padding: 20px; width: auto; }'
    append_text_to_file(file_path, styleString)
    
    styleString = '.toc_title {font-weight: 700; text-align: left; color: #DDE6ED;}'
    append_text_to_file(file_path, styleString)
    
    styleString = ' #toc_container li, #toc_container ul, #toc_container ul li{list-style: outside none none !important;}'
    append_text_to_file(file_path, styleString)

    styleString = '.mainDiv {border: 2px solid white; text-align: justify; margin: auto; width: 75%; padding: 20px;} '
    append_text_to_file(file_path, styleString)

    styleString = 'h1 {color: #9DB2BF;}'
    append_text_to_file(file_path, styleString)

    styleString = 'h2 {color: #9DB2BF;}'
    append_text_to_file(file_path, styleString)

    styleString = 'h3 {color: #9DB2BF;}'
    append_text_to_file(file_path, styleString)

    styleString = 'td {color:#DDE6ED; padding: 5px; }'
    append_text_to_file(file_path, styleString)

    styleString = 'p {color: #DDE6ED;}'
    append_text_to_file(file_path, styleString)

    styleString = 'a {color: skyblue;}'
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
    indexFilePath = "/opt/splunk/etc/apps/" + appFilePath + "/lookups/index_info.csv"
    indexCSV = read_csv_file(indexFilePath)

    i = 0

    while i < len(indexCSV):
        newIndex = indexInfo(indexCSV[i][0],indexCSV[i][1],indexCSV[i][2])
        ListOfIndex.append(newIndex)
        i += 1

    stCount = len(ListOfIndex)
    print(stCount)

    writeIndex = '<h1 id="indexes">1. Indexes - Count: ' + str(stCount) + '</h1>'
    append_text_to_file(file_path, writeIndex)

    writeIndex = '<table width="100%" border=1>'
    append_text_to_file(file_path, writeIndex)    
    
    writeIndex = '<tr><td><b>Index Name</b></td><td><b>Index Description</b></td></tr>'
    append_text_to_file(file_path, writeIndex)  
    tempCount = 0 
    for nIndex in ListOfIndex:
        if tempCount!=0:
             
            writeIndex = "<tr>"
            append_text_to_file(file_path, writeIndex)

            tempIndex = nIndex.index
            tempDetails = nIndex.description
            writeIndex = "<td>" + tempIndex + "</td><td>" + tempDetails + "</td>"
            append_text_to_file(file_path, writeIndex)

            writeIndex = "</tr>"
            append_text_to_file(file_path, writeIndex)
        tempCount += 1

    writeIndex = '</table>'
    append_text_to_file(file_path, writeIndex)

    writeIndex = '<p><a href="#top">Back to top of page</a></p>'
    append_text_to_file(file_path, writeIndex)
    
def addDashboardInfo():
    indexFilePath = "/opt/splunk/etc/apps/" + appFilePath + "/lookups/dashboard_info.csv"
    indexCSV = read_csv_file(indexFilePath)

    i = 0

    while i < len(indexCSV):
        newDashboard = dashboardInfo(indexCSV[i][0],indexCSV[i][1],indexCSV[i][2],indexCSV[i][4])
        ListOfDashboard.append(newDashboard)
        i += 1

    stCount = len(ListOfIndex)
    print(stCount)

    writeIndex = '<h1 id="dashboards">4. Dashboards - Count: ' + str(stCount) + '</h1>'
    append_text_to_file(file_path, writeIndex)

    writeIndex = '<table width="100%" border=1>'
    append_text_to_file(file_path, writeIndex)    
    
    writeIndex = '<tr><td><b>app</b></td><td><b>URLField</b></td><td><b>Details</b></td><td><b>MITRE</b></td></tr>'
    append_text_to_file(file_path, writeIndex)  
    tempCount = 0 
    for nDashboard in ListOfDashboard:
        if tempCount!=0:
             
            writeIndex = "<tr>"
            append_text_to_file(file_path, writeIndex)

            tempUrlField = nDashboard.urlField
            tempDetails = nDashboard.details
            tempApp = nDashboard.app
            tempMitre = nDashboard.mitre
            writeIndex = "<td>" + tempApp + "</td><td>" + tempUrlField + "</td><td>" + tempDetails + "</td><td>" + tempMitre + "</td>"
            append_text_to_file(file_path, writeIndex)

            writeIndex = "</tr>"
            append_text_to_file(file_path, writeIndex)
        tempCount += 1

    writeIndex = '</table>'
    append_text_to_file(file_path, writeIndex)

    writeIndex = '<p><a href="#top">Back to top of page</a></p>'
    append_text_to_file(file_path, writeIndex)
    
def addSavedSearchInfo():
    indexFilePath = "/opt/splunk/etc/apps/" + appFilePath + "/lookups/savedsearch_info.csv"
    indexCSV = read_csv_file(indexFilePath)

    i = 0

    while i < len(indexCSV):
        newSavedSearch = savedSearchInfo(indexCSV[i][0],indexCSV[i][1],indexCSV[i][2],indexCSV[i][3],indexCSV[i][4],indexCSV[i][6])
        ListOfSavedSearch.append(newSavedSearch)
        i += 1

    stCount = len(ListOfSavedSearch)
    print(stCount)

    writeIndex = '<h1 id="dashboards">5. Saved Searches - Count: ' + str(stCount) + '</h1>'
    append_text_to_file(file_path, writeIndex)

    writeIndex = '<table width="100%" border=1>'
    append_text_to_file(file_path, writeIndex)    
    
    writeIndex = '<tr><td><b>Cron Schedule</b></td><td><b>Title</b></td><td><b>Details</b></td><td><b>MITRE</b></td><td><b>Actions</b></td></tr>'
    append_text_to_file(file_path, writeIndex)  
   
    tempCount = 0 
    for nSavedSearch in ListOfSavedSearch:
        if tempCount!=0:
             
            writeIndex = "<tr>"
            append_text_to_file(file_path, writeIndex)

            tempActions = nSavedSearch.actions
            tempTitle = nSavedSearch.title
            tempDetails = nSavedSearch.details
            tempCronSchedule = nSavedSearch.cron_schedule
            tempMitre = nSavedSearch.mitre
            writeIndex = "<td>" + tempCronSchedule + "</td><td>" + tempTitle + "</td><td>" + tempDetails + "</td><td>" + tempMitre + "</td><td>" + tempActions + "</td>"
            append_text_to_file(file_path, writeIndex)

            writeIndex = "</tr>"
            append_text_to_file(file_path, writeIndex)
        tempCount += 1

    writeIndex = '</table>'
    append_text_to_file(file_path, writeIndex)

    writeIndex = '<p><a href="#top">Back to top of page</a></p>'
    append_text_to_file(file_path, writeIndex)
    


def addSourceType():
    sourcetypeFilePath = "/opt/splunk/etc/apps/" + appFilePath + "/lookups/sourcetype_info.csv"
    sourcetypeCSV = read_csv_file(sourcetypeFilePath)
    analtyicFilePath = "/opt/splunk/etc/apps/" + appFilePath + "/lookups/analytics_info.csv"
    analtyicCSV = read_csv_file(analtyicFilePath)

    i = 0

    while i < len(sourcetypeCSV):
        newSourcetype = sourcetypeInfo(sourcetypeCSV[i][0],sourcetypeCSV[i][1],sourcetypeCSV[i][2],sourcetypeCSV[i][3])
        ListOfSourceType.append(newSourcetype)
        i += 1

    #stCount = ListOfSourceType.length
    stCount = len(ListOfSourceType)

    i = 0
    while i < len(analtyicCSV):
        newAnalytic = analyticInfo(analtyicCSV[i][0],analtyicCSV[i][1],analtyicCSV[i][2],analtyicCSV[i][3],analtyicCSV[i][4],analtyicCSV[i][5],analtyicCSV[i][6],analtyicCSV[i][7],analtyicCSV[i][8],analtyicCSV[i][9],analtyicCSV[i][10],analtyicCSV[i][11])
        ListOfAnalytic.append(newAnalytic)
        i += 1

    writeSourcetype = f'<h1 id="sourcetypes">2. Sourcetypes - Count: {stCount} </h1>'
    append_text_to_file(file_path, writeSourcetype)

    writeSourcetype = '<table width="100%" border=1>'
    append_text_to_file(file_path, writeSourcetype)

    writeSourcetype = '<tr>'
    append_text_to_file(file_path, writeSourcetype)

    writeSourcetype = '<td><b>Sourcetype</b></td><td><b>Index</b></td><td><b>Description/Queries</b></td>'
    append_text_to_file(file_path, writeSourcetype)

    writeSourcetype = '</tr>'
    append_text_to_file(file_path, writeSourcetype)

    tempCounter = 0
    for nSourceType in ListOfSourceType:
        #print("Hello")
        if tempCounter != 0 :
             
            tempSourceType = nSourceType.sourcetype
            tempIndex = nSourceType.index 
            tempDetails = nSourceType.description
                    
            writeSourcetype = '<tr><td>' + tempSourceType + '</td>'
            append_text_to_file(file_path, writeSourcetype)

            writeSourcetype = '<td>' + tempIndex + '</td>'
            append_text_to_file(file_path, writeSourcetype)

            writeSourcetype = "<td><p>" + tempDetails + "</p>"
            append_text_to_file(file_path, writeSourcetype)

            for loopSourcetype in ListOfSourceType:
                if loopSourcetype.sourcetype == nSourceType.sourcetype:
                
                    analyticTemp = 0
                    for nAnalytic in ListOfAnalytic:
                        modSourceType = "sourcetype=" + nSourceType.sourcetype
                        if modSourceType == nAnalytic.sourcetypes:
                            metric_description = nAnalytic.description
                            metric_query = nAnalytic.queries

                            subTable = '<p>' + metric_query + '</p>'
                            append_text_to_file(file_path, subTable)

                            analyticTemp += 1
            subTable = "</td>"
            append_text_to_file(file_path, subTable)

        subTable = '</tr>'
        append_text_to_file(file_path, subTable)
        tempCounter += 1
    print("You are writing Table")
    writeSourcetype = '</table>'
    print("You are finished writing table")
    append_text_to_file(file_path, writeSourcetype) 
    
    writeSourcetype = '<p><a href="#top">Back to top of page</a></p>'
    append_text_to_file(file_path, writeSourcetype) 

   

def addSourceInfo():
    sourceFilePath = "/opt/splunk/etc/apps/" + appFilePath + "/lookups/source_info.csv"
    sourceCSV = read_csv_file(sourceFilePath)

    i = 0

    while i < len(sourceCSV):
        newSource = sourceInfo(sourceCSV[i][0],sourceCSV[i][1],sourceCSV[i][2],sourceCSV[i][3])
        ListOfSource.append(newSource)
        i += 1

    stCount = len(ListOfSource)
    print(stCount)

    writeSource = '<h1 id="sources">3. Sources - Count: ' + str(stCount) + '</h1>'
    append_text_to_file(file_path, writeSource)

    writeSource = '<table width="100%" border=1>'
    append_text_to_file(file_path, writeSource)    
    
    writeSource = '<tr><td><b>Source Name</b></td><td><b>Source Description</b></td></tr>'
    append_text_to_file(file_path, writeSource)   
    tempCount = 0
    for nSource in ListOfSource:
        if tempCount!=0:
            writeSource = "<tr>"
            append_text_to_file(file_path, writeSource)

            tempSource = nSource.index
            tempDetails = nSource.description
            writeSource = "<td>" + tempSource + "</td><td>" + tempDetails + "</td>"
            append_text_to_file(file_path, writeSource)

            writeSource = "</tr>"
            append_text_to_file(file_path, writeSource)
        tempCount += 1
    writeSource = '</table>'
    append_text_to_file(file_path, writeSource)

    writeSource = '<p><a href="#top">Back to top of page</a></p>'
    append_text_to_file(file_path, writeSource)


ListOfIndex = []
ListOfSourceType = []
ListOfSource = []
ListOfAnalytic = []
ListOfDashboard = []
ListOfSavedSearch = []

file_path = "/opt/splunk/etc/apps/" + appFilePath + "/appserver/static/CS_doc.htm"

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

webString ='<body style="background-color:#27374D; font-family:Lucida Sans, Lucida Sans Regular, Lucida Grande, Lucida Sans Unicode, Geneva, Verdana, sans-serif";><div class="mainDiv"><a name="top"></a><table><tr><td><div id="toc_container"><p class="toc_title">Table of Contents</p><a style="padding:10px"; href="#indexes">1.Indexes</a><a style="padding:10px"; href="#sourcetypes">2.Sourcetypes</a><a style="padding:10px"; href="#sources">3.Summaries</a><a style="padding:10px"; href="#dashboards">4.Dashboards</a><a style="padding:10px"; href="#savedsearches">5.Saved Searches</a></div></td><h1 style="float:right; font-size: xxx-large; padding-right: 20px;">Reference Sheet</h1></tr></table>'
append_text_to_file(file_path, webString)

addIndexInfo()
addSourceType()
addSourceInfo()
addDashboardInfo()
addSavedSearchInfo()
#add-source

webString = '</div></body>'
append_text_to_file(file_path, webString)

