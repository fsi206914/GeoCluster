#!/usr/bin/python
import pdb
import sys
import random

class UserRead:
    """
    Read File from a user dataset-----------------
    """

    def __init__(self, a_path,a_long, a_lati):
        self.path = a_path;
        self.longbound = a_long;
        self.latibound = a_lati;

    def read(self):
        """

        """
        inRead = open( self.path);
        outwrite = open('california_hundred.txt','w')
        line = inRead.readline();
        print self.longbound[0], self.longbound[1]
        print self.latibound[0], self.latibound[1]
        count = 0;
        while line:
            words = line.split();

            latitude =words[2];
            longitude =words[3];
            double_latitude = float(latitude)
            double_longitude = float(longitude);

            if (double_longitude < self.longbound[0] or  double_longitude > self.longbound[1] ):
                line = inRead.readline();
                continue;

            if (double_latitude < self.latibound[0] or  double_latitude > self.latibound[1] ):
                line = inRead.readline();
                continue;
            if (random.random()<0.01):
                outwrite.write(str(double_latitude)+" "+str(double_longitude) +"\r\n" );
#            count = count +1;
#            print count;
            line = inRead.readline();


def demo():

    path = 'Gowalla_totalCheckins.txt'
    latitude= [32.5, 41.0];
    longitude = [-124.0, -116];

    text = UserRead(path, longitude, latitude);
    text.read( )


if __name__ == '__main__':
    demo()


