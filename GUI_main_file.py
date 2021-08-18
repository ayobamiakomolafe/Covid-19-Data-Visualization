print ('Hello User, This program creates visual plots from the specimenDate_ageDemographic-unstacked.csv dataset')
print ('========================================================================================')
print ("The Visual Charts will open in a new window, Note that you should close each figure to open the next chart")

print ('=============================================================================')
print ('Some charts take a while to load compared to others, Kindly wait. There are about 14 charts in All')
import data_preprocessing_module
import matplotlib.pyplot as plt
data_preprocessing_module.data_preprocessing('specimenDate_ageDemographic-unstacked.csv')
newCasesBySpecimenDate=data_preprocessing_module.newCasesBySpecimenDate_df
df_age_groups=data_preprocessing_module.age_groups_df
df_cum_cases=data_preprocessing_module.cum_cases_df
import Visualization_module
Visualization_module.plot1(newCasesBySpecimenDate)
Visualization_module.plot2(newCasesBySpecimenDate)
Visualization_module.plot3(newCasesBySpecimenDate)
Visualization_module.plot4(newCasesBySpecimenDate)
Visualization_module.plot5(newCasesBySpecimenDate)
Visualization_module.plot6(newCasesBySpecimenDate)
Visualization_module.plot7(newCasesBySpecimenDate)
Visualization_module.plot8(newCasesBySpecimenDate)
Visualization_module.plot8b(newCasesBySpecimenDate)

Visualization_module.plot9(df_age_groups)
Visualization_module.plot10(df_age_groups)
Visualization_module.plot10b(df_age_groups)

Visualization_module.plot12(df_age_groups)
Visualization_module.plot13 (df_age_groups)
Visualization_module.plot14(df_cum_cases)


