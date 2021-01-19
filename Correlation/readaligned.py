import numpy as np
import array as arr
import matplotlib.pyplot as plt
import pandas as pd
import csv
import datetime as dt


def lookup(date_pd_series, format=None):
    """
    This is an extremely fast approach to datetime parsing.
    For large data, the same dates are often repeated. Rather than
    re-parse these, we store all unique dates, parse them, and
    use a lookup to convert all dates.
    """
    dates = {date:pd.to_datetime(date, format=format) for date in date_pd_series.unique()}
    return date_pd_series.map(dates)

#print('df csv written')
print('reading in data')
df =pd.read_csv(r"C:\\Users\\LENOVO\\Desktop\\PIRE_research\\research_codes\\correlation_plots\\SMT&LMT_filter_aligned.csv", header=0)

# C:\Users\LENOVO\Desktop\PIRE_research\research_codes\correlation_plots\SMT&LMT_filter_aligned.csv
# C:\Users\LENOVO\Desktop\All_align.csv

df = df[df['tauLMT'].notna()]
#df = df[df['tauSMT'].notna()]
#df = df[df['dateLMT'].notna()]

df['dateLMT'] = lookup(df['dateLMT'], format='%Y-%m-%dT%H:%M:%S')

df.set_index('dateLMT', inplace=True)

print(df.head)

#df =pd.read_csv('All_align.csv', header=0)

#df['dateLMT'] = lookup(df['dateLMT'], format='%Y-%m-%dT%H:%M:%S')

#df.set_index('dateLMT', inplace=True)
#print(df.head())

df[df['tauLMT'] > 1.0] = 1.0
#df[df['tau12M'] > 1.0] = 1.0
#df[df['tauAPEX'] > 1.0] = 1.0
df[df['tauSMT'] > 1.0] = 1.0  #or df['val'].cip_upper(thres)

df[df['tauLMT'] < 0.02] = 0.0
#df[df['tau12M'] < 0.02] = 0.0
#df[df['tauAPEX'] < 0.02] = 0.0
df[df['tauSMT'] < 0.02] = 0.0

df[df['tauLMT']!=-1]
#df = df[df['tauAPEX'] != -1]
df = df[df['tauSMT'] != -1]
#df = df[df['tau12M'] != -1]

#df = df[df['tauAPEX'] != 1.0]
df = df[df['tauSMT'] != 1.0]
#df = df[df['tau12M'] != 1.0]
df = df[df['tauLMT'] != 1.0]

#df = df[df['tauAPEX'] != 0.0]
df = df[df['tauSMT'] != 0.0]
#df = df[df['tau12M'] != 0.0]
df = df[df['tauLMT'] != 0.0]

#for i in range(len(df['tauLMT'])):
#	if 
#df[df.between_time('02:00', '12:00')]
#df = df[for i in df.index :df.index[i] dt.time(hour=2), dt.time(hour=12))]

#df.loc[for s in night_times_list: %s,"tauLMT", "tauSMT"]


"""Filter for local night time only, convert Mount 9pm-5am to utc 4am-12pm   CPT 9-5 to utc 2-10"""

print('filtered values')
print(df.tail(), df.head())


nightly_list=[]
nightly_LMT_maxs=[]
nightly_LMT_mins=[]
nightly_SMT_maxs=[]
nightly_SMT_mins=[]

#adjust to first nightly range
#diff = (df.index[-1] - df.index[0]).days
night_start = df.index[0].date()
night_iterate = night_start
night_end = df.index[-1].date()
iterate_days = dt.timedelta(days=1)
#print(diff)


night_LMT_block = []
night_SMT_block = []
nightly_index = []
i=0
for i in range(len(df.index)-1):
        
        night_LMT_block +=  [df['tauLMT'][i]]
        night_SMT_block +=  [df['tauSMT'][i]]
                
        
        if df.index[i+1] == df.index[-1]:
            night_SMT_block +=  [df['tauSMT'][i+1]]
            night_LMT_block += [df['tauLMT'][i+1]]
        if df.index[i+1].date() != night_iterate:
            
            #print(night_block[0], night_block[0][1], "\n", night_block[:][1])
            nightly_LMT_maxs += [max(night_LMT_block)]#, [max(night_block[:][2])]]
            nightly_LMT_mins += [min(night_LMT_block)]#, [min(night_block[:][2])]]
            
            nightly_SMT_maxs += [max(night_SMT_block)]#, [max(night_block[:][2])]]
            nightly_SMT_mins += [min(night_SMT_block)]#,
            nightly_index += [df.index[i]]
            night_LMT_block.clear()
            night_SMT_block.clear()
            night_iterate = night_iterate + iterate_days
        
        
print(len(nightly_LMT_maxs), len(nightly_index))   
	#print(df[i])
	#if df.index[i].date == night_start : nightly_list+=[df.index[i], df['Tau'][i]]
	#print()
def nearest(items, pivot):
    dif=np.abs(items-pivot)
    mindif=np.amin(dif)
    return mindif, np.where(dif==mindif)

def autocorrelate(timeseries, max_lag_increment=False):
    """
    Returns autocorrelation values at lag increments.
    Input: a single timeseries object
    optional: max_lag_increment
    Output: Array of lags, Array of normalized autocorrelation values.
    """
    return crosscorr(timeseries, timeseries, max_lag_increment)


def crosscorr(datax, datay, lag=0):
    """ Lag-N cross correlation.
    Parameters
    ----------
    lag : int, default 0
    datax, datay : pandas.Series objects of equal length

    Returns
    ----------
    crosscorr : float
    """
    return datax.corr(datay.shift(lag))


#create dataframes

#df_maxs = pd.DataFrame(list(zip(nightly_LMT_maxs, nightly_SMT_maxs, nightly_index)),
 #                      columns = ['LMT', 'SMT', 'Date'])
#df_mins = pd.DataFrame(list(zip(nightly_LMT_mins, nightly_SMT_mins, nightly_index)), 
  #                     columns =['LMT', 'SMT', 'Date'])
#df_maxs.set_index('Date', inplace=True)
#df_mins.set_index('Date', inplace=True)

#3 graphs at time lag spik for LMT and SMT

#diff, end_date=nearest(df_maxs.index, (df_maxs.index[0]+dt.timedelta(days=365)))
#print("end_date index:", end_date[0][0],type(end_date[0][0]))

#print(df_maxs.index[0], type(df_maxs.index[0]), df_maxs.index[end_date[0][0]], len(df_maxs.index[:end_date[0][0]]))

  # crosscorr index and func call code
#minshifts=[]
#for i in range(-len(df.index[:end_date[0][0]]), len(df.index[:end_date[0][0]])) : 
#	minshifts+=[((df.index[i] - df.index[0]).total_seconds() / 60.0)]
	#if i%1000 ==0: print(i)

#index = range(-len(df_maxs.index[:end_date[0][0]]), len(df_maxs.index[:end_date[0][0]]))
#new_index=[]
  
#for i in index: new_index += [i*5]

#LMT_SMT_lagged_max = [crosscorr(df_maxs['LMT'], df_maxs['SMT'], lag=i) for i in range(-end_date[0][0], end_date[0][0])] #crosscorrelate(df['tauLMT'], df['tauSMT'])
#LMT_SMT_lagged_min = [crosscorr(df_mins['LMT'], df_mins['SMT'], lag=i) for i in range(-end_date[0][0], end_date[0][0])] #crosscorrelate(df['tauLMT'], df['tauSMT'])

#APEX_SMT_lagged = [crosscorr(df['tauAPEX'], df['tauSMT'], lag=i) for i in range(end_date[0][0])]
#LMT_APEX_lagged = [crosscorr(df['tauLMT'], df['tauAPEX'], lag=i) for i in range(end_date[0][0])]
#SMT_12M_lagged = [crosscorr(df['tauSMT'], df['tau12M'], lag=i) for i in range(end_date[0][0])]
#LMT_12M_lagged = [crosscorr(df['tauLMT'], df['tau12M'], lag=i) for i in range(end_date[0][0])]
#APEX_12M_lagged = [crosscorr(df['tauAPEX'], df['tau12M'], lag=i) for i in range(end_date[0][0])]
print("cross-correlated values")

#, finding max and min to plot")

#diff_1, min_index = nearest(LMT_SMT_lagged,min(LMT_SMT_lagged))
#diff_2, max_index = nearest(LMT_SMT_lagged,max(LMT_SMT_lagged))
#print(df.index[min_index[0][0]], df.index[max_index[0][0]])


#plotting cross corrs
#print(size(df.index[:end_date[0][0]]))
#plt.plot(new_index ,LMT_SMT_lagged_max,'c', label='LMT&SMT maxs')
#plt.plot(new_index ,LMT_SMT_lagged_min,'r', label='LMT&SMT mins')
#plt.plot( df.index[:end_date[0][0]],APEX_SMT_lagged,'g',label='APEX&SMT')
#plt.plot( df.index[:end_date[0][0]],LMT_APEX_lagged,'y',label='LMT&APEX')
#plt.plot(df.index[:end_date[0][0]],SMT_12M_lagged, 'm',label='SMT&12M')
#plt.plot(df.index[:end_date[0][0]],LMT_12M_lagged, 'c',label='LMT&12M')
#plt.plot(df.index[:end_date[0][0]],APEX_12M_lagged, 'k',label='APEX&12M')


#plt.plot( df.index[min_index[0][0]-100:min_index[0][0]+100],df['tauLMT'][min_index[0][0]-100:min_index[0][0]+100],'g',label='LMT')
#plt.plot( df.index[:end_date[0][0]],df['tauSMT'][:end_date[0][0]],'y',label='SMT')
#plt.scatter(nightly_index, nightly_LMT_mins,  alpha = .75, s=3, label='LMT mins')#marker = 'o',markersize = 2.2,label='SMT')
#plt.scatter(nightly_index, nightly_LMT_maxs,  alpha = .75, s=3, label='LMT maxs')
#plt.plot(nightly_index, nightly_LMT_mins, label='LMT mins')


plt.scatter(nightly_index, nightly_SMT_mins,  alpha = .75, s=3, label='SMT mins')#marker = 'o',markersize = 2.2,label='SMT')
plt.scatter(nightly_index, nightly_SMT_maxs,  alpha = .75, s=3, label='SMT maxs')
#plt.plot(nightly_index, nightly_SMT_mins, label='SMT mins')
#check alignment and utc time
#percintile plots perhaps


#try to plot at max and min shifts
#at those peeks




plt.title('SMT') #"SMT & LMT nightly mins")   #'%s' % str(df.index[0][0])+'-'+str(df.index[end_date[0][0]]))
plt.legend(loc='lower left')
plt.ylabel('Optical Depth')
plt.xlabel('Dates')  #Minutes shift from 2013-10-16@8:59am')
#Time shift(from start date 2013-10-16)')

#locs, labels = plt.xticks()
#new_labels=[0, 20000, 40000, 60000, 80000, 100000, 120000, 140000]
#new_labels0=[]
#print(labels, type(labels[0]))
#for label in new_labels: new_labels0+=[(((int(label)/365)/24)/12)*5] 

#plt.xticks(locs, new_labels0)
#plt.savefig('crosscorr_(5mins).png', dpi=300, bbox_inches='tight')
plt.show()


#
##plt.plot(LMTtau,SMTtau,'bo',markersize=0.2)
#plt.hist2d(LMTtau,APEXtau,bins=100,range=((0,1),(0,1)))
#plt.xlabel('APEX tau')
#plt.ylabel('12M tau')
#plt.axis([0,1,0,1])
#
#plt.show()
		
"""
#
import corner
#
fig1=corner.corner(df.values,labels=["tauLMT","tau12M","tauAPEX","tauSMT"],show_titles=True, plot_datapoints=False, plot_contours=True, levels=(0.68,0.95), title_kwargs={"fontsize": 10})
#
fig1.savefig('cornerplotALL_sparse.pdf')


df_corr=df.corr()
print(df_corr.head())
#
#
#
data = df_corr.values
fig = plt.figure()
ax=fig.add_subplot(111)

##
#adjust for crosscorrelation heatmaps between each telescope pair***
##

heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
fig.colorbar(heatmap)
ax.set_xticks(np.arange(data.shape[1]) + .5, minor=False)
ax.set_yticks(np.arange(data.shape[0]) +.5, minor=False)
ax.invert_yaxis()
ax.xaxis.tick_top()
#
column_labels = df_corr.columns
row_labels = df_corr.index
#
ax.set_xticklabels(column_labels)
ax.set_yticklabels(row_labels)
#
plt.xticks(rotation=90)
heatmap.set_clim(-1,1)
plt.tight_layout()
#fig.savefig('All_corr_plot')
plt.show()
"""