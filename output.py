import csv


def read_devices():
    devices = {}
    with open('output.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            devices[row['device']] = row['status']
    return devices


def change_device(key, value):
    devices = read_devices()
    devices[key] = value
    with open('output.csv', 'w') as csvfile:
        csvfile.write("device,status\n")
        for key in devices:
            csvfile.write(key + "," + devices[key] + "\n")
def get_device(name):
    devices=read_devices()
    return devices[name]
