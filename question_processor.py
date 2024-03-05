
QAs = []

def GetQAs():
    lines = []
    with open('QAs.txt','r') as file:
        for line in file:
            if line.strip():
                lines.append(line.strip())

    for i in range(0,len(lines),2):
        QAs.append((lines[i],lines[i+1]))


    print(QAs)
    return QAs
