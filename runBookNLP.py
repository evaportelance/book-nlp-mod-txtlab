## By Eva Portelance - June 20, 2017
## Usage: runBookNLP.py <directorynameforbooks>
import os , sys , csv

femPRP = {'she','herself', 'ms.','ms','miss','mrs.','mrs','madam','lady'}
masPRP = {'he','himself', 'mr.','mr','sir', 'mister','lord'}

datadir = sys.argv[1]
for filename in os.listdir(datadir):
    if filename.endswith('.txt'):
        command = './runjava novels/BookNLP -doc '+datadir+'/'+filename+' -printHTML -p data/output/'+filename+'.result'+' -tok data/tokens/'+filename+'.tokens.csv -f'
        os.system(command)



datadir = "data/tokens"
for filename in os.listdir(datadir):
    if filename.endswith('.csv'):
        table = []
        file = datadir+'/'+filename
        with open(file, encoding='utf-8', mode='r+') as f:
            for line in f:
                table.append(line.strip('\n').split('\t'))
        f.close()
        title = table[0]
        title.append('totalPRPgender')
        title.append('confidenceGender')
        table = table[1:]

        characters = []
        for line in table:
            if line[14] != '-1':
                if line[14] not in characters:
                    characters.append(line[14])

        genderCounts = []
        for c in characters:
            fem=0
            mas=0
            for line in table:
                if line[14] == c:
                    if line[9].lower() in femPRP:
                        fem+=1
                    elif line[9].lower() in masPRP:
                        mas+=1
            tot=fem+mas
            if fem > mas:
                ratio = fem/tot
            elif fem < mas:
                ratio = mas/tot
            else:
                ratio = 0.5
            genderCounts.append([c,[tot,ratio]])

        for line in table:
            if line[14] != '-1':
                found = False
                for c in genderCounts:
                    if c[0] == line[14]:
                        line.append(c[1][0])
                        line.append(c[1][1])
                        found = True
                if not found:
                    line.append(0)
                    line.append(0.5)
            else:
                line.append(0)
                line.append(0)
        with open(file, encoding='utf-8', newline='', mode='w') as f:
            writer = csv.writer(f)
            writer.writerow(title)
            writer.writerows(table)
        f.close()
