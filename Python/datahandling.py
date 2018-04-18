import pandas
df_pd1 = pandas.read_table("PatientDATA1.txt")
df_pd2 = pandas.read_csv("PatientDATA2.txt")
pandas.to_datetime(df_pd2["VISIT"],format="%d-%m-%Y")
df_pd2["VISIT"]=pandas.to_datetime(df_pd2["VISIT"],format="%d-%m-%Y")
df_pd2["VISIT"].diff()
df_pd=df_pd1.merge(df_pd2,on='PATNO',how='inner')
df_pd[["PATNO","GENDER","HR","VISIT"]]
df_pd.loc[:,["PATNO","GENDER","HR","VISIT"]]
df_pd.iloc[:,[0,1,2,6]]
df_pd["AE"].value_counts()
pandas.crosstab(df_pd["AE"],df_pd["GENDER"])
df_pd.sample(3)
df_pd.sort_values("HR")
df_pd.sort_values("VISIT",ascending=True)
df_pd["GENDER"].str.upper()
Pdata_SBP_DBP=df_pd["SBP_DBP"].str.split("_",expand=True)
Pdata_SBP_DBP=Pdata_SBP_DBP.astype(int)
Pdata_SBP_DBP.columns=["SBP","DBP"]
df_pd_clean=pandas.concat([df_pd,Pdata_SBP_DBP],axis=1)
df_pd_clean.drop("SBP_DBP",axis=1,inplace=True)
df_pd["GENDER"].unique()
replace_dict={"m":"Male","F":"Female","feminin":"Female","Mal":"Male","M":"Male","Man":"Male"}
df_pd["GENDER_CLEAN"]=df_pd["GENDER"].replace(replace_dict)
df_pd["GENDER_CLEAN"].unique()
print('Maximumheartrate:',df_pd["HR"].max())
print('Minimumheartrate:',df_pd["HR"].min())
print('Meanheartrate:',df_pd["HR"].mean())
df_pd.loc[df_pd["HR"]<40,"HR"]=None
df_pd.loc[df_pd["HR"]>100,"HR"]=None
df_pd_clean.plot.bar("PATNO","HR")
df_pd_clean[["HR","SBP","DBP"]].plot.box()
from scipy import stats
stats.ttest_ind(df_pd_clean.loc[df_pd_clean['GENDER_CLEAN'] == 'Male', 'HR'],df_pd_clean.loc[df_pd_clean['GENDER_CLEAN'] == 'Female', 'HR'],nan_policy='omit')