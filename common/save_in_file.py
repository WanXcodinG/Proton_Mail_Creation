import csv
from settings import csv_delimiter
import os

class FileHandling:
    '''File handling'''
    def __init__(self,filename,headers):
        self.filename= filename
        self.headers = headers
    def create_new_file(self):
        with open(self.filename, 'a', newline='') as csvfile:
            if csvfile.tell() == 0: 
                writer = csv.DictWriter(csvfile, delimiter=csv_delimiter,fieldnames=self.headers)
                writer.writeheader()


    def add_to_file(self,data:list):
        if os.path.exists(self.filename):
            with open(self.filename, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, delimiter=csv_delimiter,fieldnames=self.headers)
                if isinstance(data, (tuple,list)):  # If input is a list, convert it to a dictionary
                    formatted_data = [{self.headers[i]: data[i] for i in range(len(data))}]
                elif isinstance(data, dict):  # If input is already a dictionary
                    formatted_data = [data]
                writer.writerows(formatted_data)


    @staticmethod
    def one_line_write(filename,data):
        with open(filename,'a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow([data])

    @staticmethod     
    def one_line_read(filename):
        data = []
        if os.path.exists(filename):
            with open(filename,'r',newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(row[0])
        return data or None
    
    def filter_data(self,compare:list=None):
        compare = compare or []
        data = []
        with open(self.filename,'r',newline='') as csvfile:
            reader= csv.DictReader(csvfile,delimiter=csv_delimiter,fieldnames=self.headers)
            next(reader)
            for row in reader:
                address= row[self.headers[0]]
                password = row[self.headers[1]]
                if address and (address not in compare):
                    data.append((address.strip(),password.strip()))
        return data            