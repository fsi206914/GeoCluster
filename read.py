#!/usr/bin/python
import pdb
import sys

class UserRead:
    """
    Read File from a user dataset-----------------
    """

    def __init__(self, a_path, a_ID):
        self.path = a_path;
        self.SelectedID = a_ID;

    def read(self):
        """

        """
        inRead = open( self.path);

        line = inRead.readline();
        count = 1;
        response = {'latitude': [], 'longitude': []}
        while line:
            words = line.split();
            if self.SelectedID != int(words[0]):
                line = inRead.readline();
                continue;
            latitude =words[2];
            longitude =words[3];
            double_latitude = float(latitude)
            double_longitude = float(longitude);

            response['latitude'].append(double_latitude);
            response['longitude'].append(double_longitude);

            count = count +1;
            line = inRead.readline();

        return response;


class twoFileRead:
    """
    Read File from a user dataset-----------------
    """

    def __init__(self, a_path, a_geo):
        self.path_edge = a_path;
        self.path_geo = a_geo;

    def read(self,GeoInformation,friends):
        """

        """
        inRead = open( self.path_edge);
        line = inRead.readline();

        while line:
            words = line.split();
            left =words[0];
            right =words[1];
            int_left = int(left)
            int_right = int(right);

            if int_left not in friends:
                friends[int_left] = [];

            friends[int_left].append(int_right);

            line = inRead.readline();

#        print friends[1];

        inRead = open( self.path_geo);
        line = inRead.readline();

        while line:
            words = line.split();
            ID = int(words[0]);
            if ID not in GeoInformation:
                GeoInformation[ID] = {'latitude':[], 'longitude':[]};

            latitude =float(words[2])
            longitude =float(words[3]);

            GeoInformation[ID]['latitude'].append(latitude);
            GeoInformation[ID]['longitude'].append(longitude);

            line = inRead.readline();
 #       print GeoInformation[0]
        print "finish read to memory"

def demo(readID):

    path = 'xaa.txt'
    text = UserRead(path, readID);
    return text.read( )

def twoFile(GeoInformation,friends):

#    path_edge = 'testEdge.txt'
#    path_geo = 'xaa.txt'
    path_edge = 'Gowalla_edges.txt'
    path_geo = 'Gowalla_totalCheckins.txt'

    text = twoFileRead(path_edge, path_geo);
    text.read(GeoInformation,friends);



if __name__ == '__main__':
    GeoInformation = {}
    friends = {}
    twoFile(GeoInformation,friends);


