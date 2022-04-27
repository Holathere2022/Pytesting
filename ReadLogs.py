import csv
import time
def logreader(logFile):
    with open(logFile, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            timestamp       = time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime((int(row['timeStamp'])/1000))) 
            label           = row['label']
            responseCode   = row['responseCode']
            responseMessage    = row['responseMessage']
            failureMessage     = row['failureMessage']

            if responseCode != "200":
                print(label + "," + responseCode + "," + responseMessage + "," + failureMessage + "," + timestamp)


if __name__ == "__main__":
    logreader(r"C:\tmp\Python_exercises_QA_Engr (5)\Updated_Python_exercises_QA_Engr\Jmeter_log1.jtl")
    
