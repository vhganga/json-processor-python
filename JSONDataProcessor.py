import json
from datetime import datetime
from dateutil.parser import parse

def readJSONData(data):
    for instance in data['Instances']:
        print(instance)

def determine_number_of_instances(data):
    print("Number of Instances: "+str(len(data['Instances'])))


def list_environments(data):
    envList = []
    for instance in data['Instances']:
        instanceData= instance['InstanceData']
        curEnv = instanceData['Environment']
        if curEnv in envList:
            continue
        else:
            envList.append(curEnv)
    print("Environments are "+str(envList))

def get_average_host_uptime(data):
    totalUpTime=0.0
    for instance in data['Instances']:
        instanceData= instance['InstanceData']
        launchTimeStamp= instanceData['LaunchTime']
        launchTimeStampFormatted= parse(launchTimeStamp)#datetime.strptime(launchTimeStamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        print("Launch Timestamp "+str(launchTimeStampFormatted))

        currentTimeStamp= datetime.utcnow()
        print("current Timestamp in UTC "+str(currentTimeStamp))
        difference = currentTimeStamp - launchTimeStampFormatted
        totalUpTime = totalUpTime + difference
    averageUpTime = totalUpTime/30
    print("Average Host Uptime is: "+str(averageUpTime))


f = open('TestData.json')
data = json.load(f)
#readJSONData(data)
determine_number_of_instances(data)
list_environments(data)
#get_average_host_uptime(data)