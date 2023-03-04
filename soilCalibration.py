import machine
import utime

def lowBoundCalibration(sensorPin, ledPin = 0, numSamples = 2000, sampleTime = 0.05):
    calibrationCount = 0
    readings = []
    returns= []
    if(ledPin != 0):
        ledPin.value(1)
    for i in range(numSamples):
        readings.append(sensorPin.value())
        utime.sleep(sampleTime)
    
    minRead = min(readings)
    maxRead = max(readings)
    average = sum(readings)/len(readings)
    
    readings = [minRead, maxRead, average]
    
    if(ledPin != 0):
        for i in range(5):
            ledPin.toggle()
            utime.sleep(0.1)
    
    return readings
        
        
        