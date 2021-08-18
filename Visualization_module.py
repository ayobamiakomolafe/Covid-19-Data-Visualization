"This module produces the visual charts"


"""Total number of cases in each area from 2020-03-16 to 2020-11-01, the entire timeframe period of the whole dataset"""
def plot1(newCasesBySpecimenDate):
  import matplotlib.pyplot as plt
  newCasesBySpecimenDate.groupby('areaName')['Total cases'].sum().to_frame().plot(kind='line', figsize=(15,8) )
  plt.xlabel('AreaName')
  plt.ylabel('Total cases')
  plt.title('Total number of cases in each area from 2020-03-16 to 2020-11-01')
  plt.show()
  


    

"""Top 10 Areas with the highest number of cases from 2020-03-16 to 2020-11-01, the entire timeframe period of the whole dataset"""
def plot2(newCasesBySpecimenDate):
  import matplotlib.pyplot as plt
  newCasesBySpecimenDate.groupby('areaName')['Total cases'].sum().to_frame().\
  sort_values('Total cases', ascending=False).head(10).plot(kind='bar', figsize=(15,8))
  plt.xlabel('AreaName')
  plt.ylabel('Total cases')
  plt.title('Top 10 Areas with the highest number of cases from 2020-03-16 to 2020-11-01')
  plt.show()
  


"""Top 10 Areas with the lowest number of cases from 2020-03-16 to 2020-11-01, the entire timeframe period of the whole dataset"""
def plot3(newCasesBySpecimenDate):
  import matplotlib.pyplot as plt
  newCasesBySpecimenDate.groupby('areaName')['Total cases'].sum().to_frame().\
  sort_values('Total cases', ascending=False).tail(10).\
  plot(kind='bar', figsize=(15,8))
  plt.xlabel('AreaName')
  plt.ylabel('Total cases')
  plt.title('Top 10 Areas with the lowest of cases from 2020-03-16 to 2020-11-01')
  plt.show()

  

"""Pie chart showing Comparison of Total cases per month"""
def plot4(newCasesBySpecimenDate):
  import matplotlib.pyplot as plt
  newCasesBySpecimenDate.groupby('months')['Total cases'].sum().to_frame().plot(kind='pie',y='Total cases',autopct='%1.1f%%',figsize=(20,9) )
  plt.title('Pie chart showing Comparison of Total cases per month')
  plt.show()



"""Grouped Bar chart showing trends for Total newCases of people below age 59 and Total newCases of people above age 60 per month"""
def plot4(newCasesBySpecimenDate):
  import matplotlib.pyplot as plt
  newCasesBySpecimenDate.groupby('months').sum()[['newCasesBySpecimenDate-0_59',	'newCasesBySpecimenDate-60+']].plot(kind='bar',figsize=(15,8) )
  plt.xlabel('Months')
  plt.ylabel('Total cases')
  plt.title('Total newCases of people below age 59 and Total newCases of people above age 60 per month')
  plt.show()






"""Total number of cases reported each day from 2020-02 to 2020-11"""
def plot5(newCasesBySpecimenDate):
  import matplotlib.pyplot as plt
  newCasesBySpecimenDate[['date', 'Total cases']].set_index('date').plot(kind='line',figsize=(15,8))

  plt.xlabel('Dates')
  plt.ylabel('Total cases')
  plt.title('Total number of cases reported each day from 2020-02 to 2020-11')
  plt.show()



"""Top 5 Areas with the highest number of cases on 2020-10-26 the day with highest recorded case """
def plot6(newCasesBySpecimenDate):
  import matplotlib.pyplot as plt
  newCasesBySpecimenDate[newCasesBySpecimenDate['date']=='2020-10-26'].   \
  groupby('areaName')['Total cases'].sum().to_frame().reset_index().sort_values('Total cases', ascending=False)   \
  .set_index('areaName').head(5).plot(kind='barh', figsize=(10,7))
  
  plt.xlabel('Total cases')
  plt.ylabel('AreaName')
  plt.title('Top 5 Areas with the highest number of cases on 2020-10-26 the day with highest recorded case')
  plt.show()




"""Total number of cases reported each week from from 2020-03-16 to 2020-11-01, the entire timeframe period of the whole dataset"""
def plot7(newCasesBySpecimenDate):
  import matplotlib.pyplot as plt
  newCasesBySpecimenDate.groupby('weeks')['Total cases'].sum().plot(kind='area', figsize=(15,8))
  plt.xlabel('Weeks')
  plt.ylabel('Total cases')
  plt.title('Total number of cases reported each week')
  plt.show()




"""Total number of cases reported each week for People below age 59 and people above age 59 from 2020-03-16 to 2020-11-01, the entire timeframe period of the whole dataset"""
def plot8(newCasesBySpecimenDate):
  import matplotlib.pyplot as plt
  newCasesBySpecimenDate.groupby('weeks')['newCasesBySpecimenDate-0_59', 'newCasesBySpecimenDate-60+' ].sum().plot(kind='area', figsize=(15,8))
  plt.xlabel('Weeks')
  plt.ylabel('Total cases')
  plt.title('Total number of cases reported each week for People below age 59 and people above age 59')
  plt.show()

"""Donut chart showing comparison of total cases of people between age 0-59 and people above 60"""
def plot8b(newCasesBySpecimenDate):
    import matplotlib.pyplot as plt
    colors=['#FFA500', '#0000FF']
    labels=['Total cases age -0_59', 'Total cases age -60+']

    newCasesBySpecimenDate.sum().to_frame().reset_index().drop([0,3, 4, 5]).set_index('index').plot(kind='pie', y=0, colors=colors, labels=labels,autopct='%1.1f%%',figsize=(15,8))
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
      
    # Adding Circle in Pie chart
    fig.gca().add_artist(centre_circle)
    plt.title('Donut chart showing comparison of total cases of people between age 0-59 and people above 60')
    plt.show()




"""Total Number of cases recorded for each age group from 2020-03-16 to 2020-11-01, the entire timeframe period of the whole dataset"""
def plot9(df_age_groups):
  import matplotlib.pyplot as plt
  df_age_groups.sum().to_frame().drop(['months', 'areaName', 'weeks']).rename(columns={0:'Total cases'})\
  .plot(kind='bar',figsize=(15,8), color='black')

  plt.xlabel('Age-Range')
  plt.ylabel('Total cases')
  plt.title('Total Number of cases recorded for each age group')
  plt.show()




"""Boxplots showing the distribution counts of Total cases across age groups"""
def plot10(df_age_groups):
  import matplotlib.pyplot as plt
  df_age_groups.drop(['date','months', 'areaName', 'weeks'], axis=1).sum().to_frame().plot(kind='box', figsize=(15,8))
  plt.xlabel('Age-Range')
  plt.ylabel('Total cases')
  plt.title('Boxplots showing the distribution counts of Total cases across age groups')
  plt.show()
  
def plot10b(df_age_groups):
  import matplotlib.pyplot as plt
  df_age_groups.drop(['date','months', 'areaName', 'weeks'], axis=1).plot(kind='box',figsize=(15,8))
  plt.xticks(rotation=90)
  plt.xlabel('Age-Range')
  plt.ylabel('Total cases')
  plt.title('Boxplots of cases recorded for each age group')
  plt.show()



"""Total Number of Cases recorded for each age group per month"""
def plot12(df_age_groups):
  import matplotlib.pyplot as plt
  df_age_groups.groupby('months').sum().drop('weeks', axis=1).plot(kind='area', figsize=(15,8) )
  plt.xlabel('Months')
  plt.ylabel('Total cases')
  plt.title('Total Number of Cases recorded for each age group per month')
  plt.show()



def plot13(df_age_groups):
    import matplotlib.pyplot as plt
    """Proportion of each age group contribution in the Month with the higest case Using a waffle chart; 'The month with highest record of cases is 10-October'"""
  
    df_age_groups.groupby('months').sum().sum(axis=1).to_frame().idxmax()

    df_waffle=df_age_groups.groupby('months').sum().loc[10,:].to_frame().drop('weeks')
    df_waffle['perc']=(df_waffle[10]/df_waffle[10].sum()) * 100
    df_waffle.reset_index(inplace=True)

    age_groups= ['0_4:','10_14:', '15_19:', '20_24:', '25_29:','30_34:', '35_39:', '40_44:', '45_49:', '50_54:',\
                 '55_59:', '5_9:', '60_64:', '65_69:', '70_74:','75_79:', '80_84:', '85_89:', '90:']

    
    from pywaffle import Waffle
      

      # To plot the waffle Chart
    fig = plt.figure(
        FigureClass = Waffle,
        rows = 5,
        title={'label': 'Proportion of each age group contribution in October, the Month with the higest case', 'loc': 'left'},
        values = df_waffle.perc,
        labels = ['{} {:.1f}%'.format(k, v) for k, v in zip(age_groups,df_waffle.perc)], 
        legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(df_waffle.perc),'fontsize': 12, 'framealpha': 0},
        figsize=(40,10)
    )
    plt.show()



def plot14(df_cum_cases):
    import matplotlib.pyplot as plt
    """Cumulative cases per day across age ranges"""

    df_cum_cases['Total Cum cases']=df_cum_cases.sum(axis=1)
    df_cum_cases[['date', 'Total Cum cases']].set_index('date').plot(kind='line', figsize=(15,8))

    plt.xlabel('Date')
    plt.ylabel('Total cases')
    plt.title('Total Number of Cumulative cases per day across age ranges')
    plt.show()
