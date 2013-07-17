from __future__ import division
import tornado.web
import tornado.escape
import time
import sys, traceback
import threading
import read
import mclust
import random

class dictDefine:

    checkInLimit = 3000;
    previousUserID = -1;

    def __init__(self):
        self.GeoInformation = {};
        self.friends = {};

    def readFile(self):
        read.twoFile(self.GeoInformation,self.friends);


myDict = dictDefine();

response_CA = {'latitude': [], 'longitude': []}
class ThreadClass(threading.Thread):
    def run(self):
        myDict.readFile();
        time.sleep(1000000)
        print "time out....."


def sample(oneDict):
    size = len(oneDict['latitude']);
    ClusterDataset = {'latitude': [], 'longitude': []};
    prob =dictDefine.checkInLimit/size;
    for number in oneDict['latitude']:
        if (random.random()<prob):
            ClusterDataset['latitude'].extend(  oneDict['latitude'][number] );
            ClusterDataset['longitude'].extend( oneDict['longitude'][number]);
    return ClusterDataset

def InitCluster(ID, clusterNum):
    intID = int(ID);
    num_clust = int(clusterNum);

    if(intID == -1):
        print "can not find the previous ID";
        sys.exit(0);

    size =len(myDict.GeoInformation[intID]['latitude']);
    ClusterDataset = {};
    if(size>dictDefine.checkInLimit):
        ClusterDataset = sample(myDict.GeoInformation[intID])
    else:
        ClusterDataset = myDict.GeoInformation[intID];

    return mclust.getClusterInfo(ClusterDataset,num_clust);


def individual(ID):
    intID = int(ID);
    return myDict.GeoInformation[intID];


def friends(ID):
    ID = int(ID);
    response = {'latitude': [], 'longitude': []}
    friendList = myDict.friends[ID];
    for number in friendList:
        if number in myDict.GeoInformation:
            response['latitude'].extend(  myDict.GeoInformation[number]['latitude']);
            response['longitude'].extend( myDict.GeoInformation[number]['longitude']);

    return response;


def getFriendsID(ID):
    ID = int(ID);
    return myDict.friends[ID];


class HVCNextHandler(tornado.web.RequestHandler):
    def post(self):
        current = tornado.escape.json_decode(self.request.body)
        human = current;

        print human['data']
        print human['func']
#        print myDict.GeoInformation[1];
        if human['func'] == 1:
                response = individual(human['data']);
                response2 = getFriendsID(human['data'])
                response['friends'] = response2;
                response['myOwn'] = int(human['data']);

        if(human['func'] == 4):
            response = InitCluster(myDict.previousUserID, human['data']);
        else:
            myDict.previousUserID = int(human['data']);
#        print response;

        print "finish response"
        self.write(tornado.escape.json_encode(response))

