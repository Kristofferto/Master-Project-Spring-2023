from spacepy import pycdf
import os
import pandas as pd
import numpy as np
import time

class SWARM_Data_Retrieval:
    def __init__(self, input_list):
        self.sat_name   = input_list[0]

        #Save the requested date globally
        self.start_year = str(input_list[1])
        self.start_month= str(input_list[2]).zfill(2)
        self.start_day  = str(input_list[3]).zfill(2)

        self.end_year = str(input_list[4])
        self.end_month= str(input_list[5]).zfill(2)
        self.end_day  = str(input_list[6]).zfill(2)
        #List containing the variables we are interested in saving
        self.array_list = ['Background_Ne', 'Foreground_Ne', 'Longitude', 'Ne', 'PCP_flag', 'Radius', 'Timestamp', 'Latitude']

        #Creating empty lists for the different variables defined in 'array_list'
        for name in self.array_list:
            exec(f'self.{name} = []')

        #Globally define counter for counting files read
        self.count = 0

        #Main directory for data storage
        self.dir_main   = 'SWARM_ABC_DATA/'

    def readfile(self, dir:str, file_name):
        ###Function that reads the file###
        cdf = pycdf.CDF(dir+file_name)
        #counting the files read
        self.count +=1
        print(f'Current number of files read: {self.count:4.0f}')

        #why dont you understand this
        for name in self.array_list:
            exec(f'{name} = cdf["{name}"][...]')

        #Appending values to the empty lists
        for name in self.array_list:
            exec(f'self.{name}.append({name})')


    def name_file(self, year, month, day):
        ###Function that names the file we want to read###
        file_name = f'SW_OPER_IPD{self.sat_name}IRR_2F_{year}{month}{day}T000000_{year}{month}{day}T235959_0301.cdf'
        return file_name


    def get_cdf(self, year, month, day):
        ###Function that checks if the requested file exists in the given directory###
        #Defining file name and path to said file
        self.file_name = self.name_file(year, month, day)
        file_exist = os.path.exists(self.dir_main + self.file_name)

        #The file is read if it exists
        if file_exist:
            return self.readfile(self.dir_main, self.file_name)
        #The user is warned when the requested file does not exist
        else:
            return print(f'###The file {self.file_name} does not exist ###')


    def data_chopper(self):
        ###Function to delete unnecessary data###
        #Removes measurements at latitudes lower than 77 (the polar cap)
        for name in self.array_list:
            exec(f'self.{name} = self.{name}[(self.Latitude >= 77) | (self.Latitude <= -77)]')


    def save_data(self):
        ###Function to save the data as binary numpy arrays###
        for name in self.array_list:
            exec(f'np.save("SWARM_{self.sat_name}_DATA/Data_{self.sat_name}_{name}", self.{name})')


    def run(self):
        ###Function to run the program###
        #Setting a start and end date for the dataframe
        start = pd.to_datetime(f'{self.start_day}/{self.start_month}/{self.start_year}', format = "%d/%m/%Y")
        end = pd.to_datetime(f'{self.end_day}/{self.end_month}/{self.end_year}', format = "%d/%m/%Y")
        dates = pd.date_range(start, end)

        #Reading through the requested files one date at a time
        for i in dates:
            year  = str(i.date().year)
            month = str(i.date().month).zfill(2)
            day   = str(i.date().day).zfill(2)
            df = self.get_cdf(year, month, day)

        #Merging the lists into arrays
        for name in self.array_list:
            exec(f'self.{name}= np.concatenate(self.{name})')

        #Deleting irrelevant data
        print('### The data is currently being trimmed down... ### \n')

        #self.data_chopper()

        #Saving the trimmed arrays for easier use later on
        print('### The data is currently being Stored... ### \n')
        self.save_data()


if __name__ == '__main__':

    #The chosen satellite and date to evaluate
    sat_name    = 'A'
    start_year  = 2014
    start_month = 7
    start_day   = 15

    end_year    = 2014
    end_month   = 7
    end_day     = 20

    input_list   = [sat_name, start_year, start_month, start_day, end_year, end_month, end_day]

    start_time = time.time()
    obj1 = SWARM_Data_Retrieval(input_list)
    obj1.run()

    end_time = time.time()
    print(f'Time elapsed for satellite {sat_name}: {end_time - start_time:.2f} s')
    print('The program is now finished.')

