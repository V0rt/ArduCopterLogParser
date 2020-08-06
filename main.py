class Parser:

    def __init__(self):
        self.input = 'input.txt'
        self.output = 'output.txt'
        self.result = []
        self.last = 0

    def work(self):
        GPS = []
        BAT = []
        BARO = []
        ATT = []

        with open(self.input) as fp:
            print("open file " + self.input)
            line = fp.readline()

            # пропускаем начало
            while not line.find("ArduCopter") > 0:
                line = fp.readline()
            print("start")
            # далее построчно
            while line:

                if line.startswith("GPS") and not GPS:
                    data = self.splitstrip(line)
                    for i in (1, 3, 4, 7, 8, 9):
                        GPS.append(data[i])
                    # print(GPS)

                if line.startswith("BAT") and not BAT:
                    data = self.splitstrip(line)
                    BAT.append(data[2])
                    # print(BAT)

                if line.startswith("BARO") and not BARO:
                    data = self.splitstrip(line)
                    BARO.append(data[2])
                    # print(BARO)

                if line.startswith("ATT") and not ATT:
                    data = self.splitstrip(line)
                    ATT.append(data[3])
                    ATT.append(data[5])
                    # print(ATT)

                if GPS and BAT and BARO and ATT:
                    temp = []
                    temp.extend(GPS)
                    temp.extend(BAT)
                    temp.extend(BARO)
                    temp.extend(ATT)
                    GPS = []
                    BAT = []
                    BARO = []
                    ATT = []
                    print(temp)
                    self.result.append(temp)
                line = fp.readline()

            print("save " + str(len(self.result)) + " strings")

        # save result
        with open(self.output, 'w', newline='') as myfile:
            myfile.write("TimeUS,GMS,GWk,Lat,Lng,Alt,Volt,Alt,Roll,Pitch\r\n")
            for line in self.result:
                for i in line:
                    myfile.write(str(i) + ",")
                myfile.write("\n")
        print("done")


    def splitstrip(self, line):
        data = line.strip()
        data = line.split(",")
        data = [c.strip() for c in data]
        return data

parser = Parser()
parser.work()
