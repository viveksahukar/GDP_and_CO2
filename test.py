import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *

wdi = pd.read_csv('wdi_small_tidy_2015.csv')

# Extract relevant columns
wdi1 = wdi[['Country Name', 
            'Mortality rate, infant (per 1,000 live births)', 
           'GDP per capita (constant 2010 US$)']]


(ggplot(wdi1, aes(x='Mortality rate, infant (per 1,000 live births)', y='GDP per capita (constant 2010 US$)')) +
        geom_point()
)
   