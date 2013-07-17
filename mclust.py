import rpy2.robjects as R
import shutil
from rpy2.robjects.packages import importr
mclust = importr("mclust")


R.r('''
        g <- function(M, r, verbose=FALSE) {

        colnames(M) <- c("x", "y")
        t1 <- M[,"x"]

        t2 <- M[,"y"]

        C<-cbind(t2,t1)

        Mycolors_2 <- c("yellow1", "red3", "skyblue" )

        Mycolors_5 <- c("dodgerblue2", "red3", "green3" ,    "slateblue", "orange", "skyblue"  )

        Mycolors_10 <- c("dodgerblue2", "red3", "skyblue" ,    "slateblue", "orange", "skyblue1", "forestgreen" , "steelblue4", "darkgoldenrod1", "darkorchid4", "cornsilk4" )

        Mycolors_20 <- c("dodgerblue2", "cornsilk4", "slateblue", "steelblue4" ,   "orange", "red3" , "forestgreen" , "skyblue1", "darkgoldenrod1", "darkorchid4", "green3","deeppink2", "firebrick3", "darkseagreen3", "darkorange1", "coral1", "aquamarine2", "lightcyan3", "khaki", "greenyellow", "yellow1" )


#        faithfulNoiseInit <- sample(c(TRUE,FALSE),size=nrow(C), replace=TRUE,prob=c(5,1))

        png('temp.png')


        faithfulMclust <- Mclust(C, modelName = 'EII', G=1:r
#         , initialization = list(noise = faithfulNoiseInit)
        )

#        mclust2Dplot(data = C, what = "classification", identify = TRUE, colors =Mycolors_20, parameters = faithfulMclust$parameters, z = faithfulMclust$z)


        par <-faithfulMclust$parameters

        dev.off()
        MaxDist<- array(0, dim=faithfulMclust$G);
        SizeofC<-length(faithfulMclust$classification);
        for(i in 1:SizeofC) {
            index<-faithfulMclust$classification[i];

            dist<- sqrt((par$mean[1,index]- C[i,1])^2 + (par$mean[2,index] - C[i,2])^2)
            if( dist>  MaxDist[index] )
                MaxDist[index] = dist;
        }
        newList <- list( "means" = par$mean, "dist" = MaxDist)

        return(newList)

        }

''')


def getClusterInfo(checkIn, NumClust):
    r_g = R.globalenv['g']

    oneList = [];
    oneList.extend(checkIn['latitude']);
    oneList.extend(checkIn['longitude']);

    v = R.FloatVector(oneList)
    M = R.r['matrix'](v, ncol = 2);

    List = r_g(M,NumClust);
    DictMean = {'latitude': [], 'longitude': [], 'MaxDist': []}
    means = List[List.names.index('means')]
    meanNum = int(means.ncol);
    dist = List[List.names.index('dist')]
    for x in range(0, meanNum):
        DictMean['latitude'].append(means[x*2+1]);
        DictMean['longitude'].append(means[x*2]);
        DictMean['MaxDist'].append(dist[x]);

#    shutil.copy2('./temp.png', './static/temp.png')
#    print DictMean
    return DictMean

if __name__ == '__main__':
    M= {'latitude': [], 'longitude': []};
    M['latitude'] =  [1.1, 3.3, 5.5, 7.7, 9.9];
    M['longitude'] = [2.2, 4.4, 6.6, 8.8, 10.0];

    getClusterInfo(M,2);

