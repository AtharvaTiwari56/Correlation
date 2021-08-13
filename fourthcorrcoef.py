import csv, numpy

def getDataSource(path):
    size_tv = []
    watch_time = []
    with open(path) as f:
        readerboy = csv.DictReader(f)
        for thing in readerboy:
            size_tv.append(float(thing['Coffee in ml']))
            watch_time.append(float(thing['sleep in hours']))

    return{'x': size_tv, 'y': watch_time}

def getCorrelation(datasource):
    correlation = numpy.corrcoef(datasource['x'], datasource['y'])
    print('Correlation between size of tv and amount of time spent watching: \n', correlation[0, 1])

def main():
    path = 'fourth.csv'
    datasource = getDataSource(path)
    getCorrelation(datasource)

main()