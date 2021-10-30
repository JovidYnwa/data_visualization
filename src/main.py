# importing matplotlib module 
import datetime
import matplotlib.pyplot as plt
import json
import pandas as pd
from numpy import array

class Plots:
    '''The purpose of this class is drawing plots
    '''

    def parse_json_frame(self, path: str, column_name: str)-> array:
        with open(path, 'r') as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        return df[column_name].values
    
    def save_plot(self, plot_name: str):
        now = datetime.datetime.now()
        date_time = now.strftime('%Y%m%d%H%M%S')
        return plt.savefig(f'./plots/{date_time}_{plot_name}')

    def draw_plots(self, path: str, column_x: str, column_y:  str):
        x = self.parse_json_frame(path, column_x)
        y = self.parse_json_frame(path, column_y)
        plt.xlabel(column_x)
        plt.ylabel(column_y)
        plt.plot(x,y)
        title_name = f'{column_x}_{column_y}'
        plt.title(title_name)
        self.save_plot(title_name)
        return plt.show()  


#obj1= Plots()
#print(obj1.draw_plots('./dataframes/deviation.json', 'max','min'))
