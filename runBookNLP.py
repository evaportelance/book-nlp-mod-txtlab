## By Eva Portelance - June 17, 2017
## Usage: runBookNLP.py <directorynameforbooks>
import os , sys 

datadir = sys.argv[1]
for filename in os.listdir(datadir):
    if filename.endswith('.txt'):
        command = './runjava novels/BookNLP -doc '+datadir+'/'+filename+' -printHTML -p data/output/'+filename+'.result'+' -tok data/tokens/'+filename+'.tokens.csv -f'
        os.system(command)

