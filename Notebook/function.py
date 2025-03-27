import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

def plot_sounding(flightline, sounding, df, df_all):
    """
    Function to plot the location of selected sounding

    Parameters
    ----------
    flightline: integer
        input value either 101102 or 101201

    sounding: integer
        input value for chosen 101102:
        0 - 7420 
        input value for chosen 101201:
        7420 - 16261 for flight line 101201

    df: pd.dataframe 
        dataframe contains data from selected flight lines

    df_all: pd.dataframe
        dataframe contains data from all flight line

    Returns
    -------
    plots of chosen flight line and sounding location
    
    """


#    if flightline not in [101102, 101201]:
#    warnings.warn(
#        f"The flightline chosen is not selected for this study. Please choose either 101102 or 101201."
#    )

    # define useful dataframe
    df_selected=df[df["GA_Project"]==flightline]
    easting = df_selected["Easting"]
    northing = df_selected["Northing"]
    # z component Low Moment, High Moment 
    LM_Z=df_selected.iloc[:, 66:84]*1e-12
    HM_Z=df_selected.iloc[:, 84:107]*1e-12    
    # z component relative uncertainty Low Moment, High Moment
    RUNC_LM_Z=df_selected.iloc[:, 107:125]
    RUNC_HM_Z=df_selected.iloc[:, 125:148]
    #dataframe for the sounding
    station = df[sounding:sounding+1]
    station_lm_data = station.iloc[0, 66:84].to_numpy()*1e-12
    station_hm_data = station.iloc[0, 84:107].to_numpy()*1e-12
    station_lm_std = station.iloc[0, 148: 166].to_numpy()
    station_hm_std = station.iloc[0, 166: 189].to_numpy()
    
    # show selected station
    plt.scatter(df_all["Easting"], df_all["Northing"], s=0.5)
    #plt.plot(easting_flightline, northing_flightline, label=str(flightline), c="r")
    plt.plot(df["Easting"][0:7421], df["Northing"][0:7421], "r", label="101102")
    plt.plot(df["Easting"][7421:16262], df["Northing"][7421:16262], "orange", label="101201")
    plt.scatter(station["Easting"], station["Northing"], c="k", marker="*", label=f"Station {sounding}" , s=50)
    plt.xlabel('Easting (m)')
    plt.ylabel('Northing (m)')
    plt.legend()
    plt.show()
    
    # plot the processed data 
    fig, ax = plt.subplots(1, 2, figsize=(10,4))
    ax[0].semilogy(easting, LM_Z)
    ax[0].set_xlabel('Easting (m)')
    ax[0].set_title('Low Moment')
    ax[0].axvline(station.iloc[0, 18], c="r", label=f"Station {sounding}")
    ax[0].legend()
    ax[1].semilogy(easting, HM_Z)
    ax[1].set_xlabel('Easting (m)')
    ax[1].set_title('High Moment')
    ax[1].axvline(station.iloc[0, 18], c="r", label=f"Station {sounding}")
    ax[1].legend()
    plt.tight_layout()

    return

def get_sounding_df(flightline, sounding, df):
    """
    Function to extract selected sounding from df

    Parameters
    ----------
    flightline: integer
        input value either 101102 or 101201

    sounding: integer
        input value for chosen 101102:
        0 - 7420 
        input value for chosen 101201:
        7420 - 16261 for flight line 101201
        
    df: pd.dataframe 
        dataframe contains data from selected flight lines
    
    Returns
    -------
    pd.dataframe

    np.array
        LM, HM, LM_std, HM_std
    
    """

    #dataframe for the sounding
    station = df[sounding:sounding+1]
    station_lm_data = station.iloc[0, 66:84].to_numpy()*1e-12
    station_hm_data = station.iloc[0, 84:107].to_numpy()*1e-12
    station_lm_std = station.iloc[0, 148: 166].to_numpy()
    station_hm_std = station.iloc[0, 166: 189].to_numpy()

    return station, station_lm_data, station_hm_data, station_lm_std, station_hm_std
    