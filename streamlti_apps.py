import streamlit as st
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="traffic_crash_analysis"
)

def custom_header(text, size=32, color="blue"):
    st.markdown(
        f"""
        <h1 style='font-size:{size}px; color:{color};'>
            {text}
        </h1>
        """,
        unsafe_allow_html=True
    )


st.sidebar.image(r"/Users/suriya/Ukesh_AIML_Projects/Traffic_Crash_Analytics_Streamlit_Project/Data/car-logo.jpg", width=100)

option=st.sidebar.pills(
    "Crash Analysis:",
    ["Home","Data_Samples","Data_Loading","Data_Analysis"]
)

if option=="Home":
    st.title("Transportation Analytics")
    st.header("Traffic Crash Analytics & Safety Intelligence Platform")

    st.divider()

    st.markdown("***Traffic crash data contains valuable insights that can help improve road safety, optimize emergency response, and support policy decisions. However, extracting meaningful insights from large-scale structured data requires strong SQL and analytical skills. In this project, provided with a pre-cleaned and structured dataset of traffic crashes. The objective is to: Analyze crash data using advanced SQL techniques Identify patterns, trends, and risk factors Generate business insights from structured data.***")

elif option=="Data_Samples":
    st.header("***Data Samples***")

    st.divider()

    st.markdown("***Dataset:***")
    st.link_button("Transportation_Analytics_Data","https://drive.google.com/file/d/1jAFsxF8ri--wYC1A-8k_Otdlf8xfcODN/view?usp=sharing")
    

    st.divider()

    st.write("***Prerequisite:***")
    st.code(
        """!pip install pandas"""
    )

    st.divider()

    st.write("***Code:***")
    st.code(
        """
    import pandas as pd
    df = pd.read_csv(r"/Users/suriya/Ukesh_AIML_Projects/Traffic_Crash_Analytics_Streamlit_Project/Data/Traffic_CrashesData.csv")
    df.head(10)""",
    language="python")

    st.divider()

    st.markdown("***Sample data:***")  
    df=pd.read_csv(r"/Users/suriya/Ukesh_AIML_Projects/Traffic_Crash_Analytics_Streamlit_Project/Data/Traffic_CrashesData.csv")
    df=df.head(10)
    st.dataframe(df)

    st.divider()

    st.write("***Data Info:***")

    st.code("""`RangeIndex: 660934 entries, 0 to 660933
    Data columns (total 39 columns):
    #   Column                         Non-Null Count   Dtype  
    ---  ------                         --------------   -----  
    0   CRASH_RECORD_ID                660934 non-null  object 
    1   CRASH_DATE                     660934 non-null  object 
    2   POSTED_SPEED_LIMIT             660934 non-null  int64  
    3   TRAFFIC_CONTROL_DEVICE         660934 non-null  object 
    4   DEVICE_CONDITION               660934 non-null  object 
    5   WEATHER_CONDITION              660934 non-null  object 
    6   LIGHTING_CONDITION             660934 non-null  object 
    7   FIRST_CRASH_TYPE               660934 non-null  object 
    8   TRAFFICWAY_TYPE                660934 non-null  object 
    9   ALIGNMENT                      660934 non-null  object 
    10  ROADWAY_SURFACE_COND           660934 non-null  object 
    11  ROAD_DEFECT                    660934 non-null  object 
    12  REPORT_TYPE                    660934 non-null  object 
    13  CRASH_TYPE                     660934 non-null  object 
    14  DAMAGE                         660934 non-null  object 
    15  DATE_POLICE_NOTIFIED           660934 non-null  object 
    16  PRIM_CONTRIBUTORY_CAUSE        660934 non-null  object 
    17  SEC_CONTRIBUTORY_CAUSE         660934 non-null  object 
    18  STREET_NO                      660934 non-null  int64  
    19  STREET_DIRECTION               660934 non-null  object 
    20  STREET_NAME                    660934 non-null  object 
    21  BEAT_OF_OCCURRENCE             660934 non-null  float64
    22  NUM_UNITS                      660934 non-null  int64  
    23  MOST_SEVERE_INJURY             660934 non-null  object 
    24  INJURIES_TOTAL                 660934 non-null  float64
    25  INJURIES_FATAL                 660934 non-null  float64
    26  INJURIES_INCAPACITATING        660934 non-null  float64
    27  INJURIES_NON_INCAPACITATING    660934 non-null  float64
    28  INJURIES_REPORTED_NOT_EVIDENT  660934 non-null  float64
    29  INJURIES_NO_INDICATION         660934 non-null  float64
    30  INJURIES_UNKNOWN               660934 non-null  float64
    31  CRASH_HOUR                     660934 non-null  int64  
    32  CRASH_DAY_OF_WEEK              660934 non-null  int64  
    33  CRASH_MONTH                    660934 non-null  int64  
    34  LATITUDE                       660934 non-null  float64
    35  LONGITUDE                      660934 non-null  float64
    36  LOCATION                       660934 non-null  object 
    37  date                           660934 non-null  object 
    38  year                           660934 non-null  int64  
    dtypes: float64(10), int64(7), object(22)`""")
        
elif option=="Data_Loading":
    st.header("***Data_Loading***")

    st.divider()

    st.write("***Objective: Load the provided csv dataset into SQL***")

    st.write("***Prerequisite:***")
    st.code(
        """!pip install sqlalchemy pymysql"""
    )
    st.markdown("- ***In mysql `create database Traffic_Crash_Analysis`***")

    st.divider()

    st.write("***Code:***")
    st.code("""
    from sqlalchemy import create_engine
    import pandas as pd

    username = "root"
    password = "12345678"
    host = "localhost"
    port = "3306"
    database = "Traffic_Crash_Analysis"

    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    )

    df = pd.read_csv(
        r"/Users/suriya/Ukesh_AIML_Projects/Traffic_Crash_Analytics_Streamlit_Project/Data/Traffic_CrashesData.csv"
    )

    df.to_sql(
        name="crash_data",
        con=engine,
        if_exists="replace",
        index=False
    )
    """, language="python")


elif option=="Data_Analysis":

    st.write("***Business Use Cases:***")

    st.code("""
        1. Traffic Authorities:
                -Identify high-risk streets and accident-prone zones
        2. Insurance Companies:
                -Analyze factors contributing to high-severity crashes
        3. Emergency Services:
                -Evaluate response effectiveness using time-based data
        4. Urban Planning:
                -Understand impact of road types and conditions
        5. Research & Policy Making:
                -Study crash trends and contributing causes""")
    
    dropdown=st.selectbox(
        "Choose a query:",
        [
        "Find the top 5 most dangerous combinations of weather and crash type based on total crashes",
         "Identify the top 10 streets with the highest number of injury crashes",
         "Find the percentage of crashes that resulted in injuries for each crash type",
         "Determine the peak crash hour for each month",
         "Find the top 5 primary causes of crashes during night time (CRASH_HOUR ≥ 18)",
         "Compare average number of injuries in daylight vs darkness conditions",
         "Find which traffic control device type has the highest average injuries per crash",
         "Identify the top 5 locations (latitude/longitude) with the highest crash frequency",
         "Find the top 5 streets with the highest injury rate, considering only streets with more than 100 crashes",
         "For each year, identify the most common crash type",
         "Find the day of the week with the highest average crashes per hour",
         "Identify high-risk time slots,Group hours into buckets (Morning, Afternoon, Evening, Night),Find which bucket has the highest injury crashes",
         "Find the top 3 contributing causes for each crash type",
         "Identify hotspot zones: Group nearby locations (round latitude & longitude to 2 decimal places),Find top 10 zones with highest crashes",
         "Calculate the year-over-year growth rate of crashes"],
        index=None,
        placeholder="Please select a query to execute values"
    )

    if dropdown=="Find the top 5 most dangerous combinations of weather and crash type based on total crashes":
        custom_header("Weather Vs Crash_Type",36,"White")
        query="""select weather_condition, crash_type, count(*) as total_crashes from crash_data 
                group by weather_condition, crash_type order by total_crashes desc limit 5;"""
        df=pd.read_sql(query,conn)
        st.dataframe(df)
        st.write("***Comments:***")
        st.write("***We observed more crashes in clear weather condition rather than snow and rain***")

    elif dropdown=="Identify the top 10 streets with the highest number of injury crashes":
        custom_header("Top 10 Streets with the Highest Number of Injury Crashes",36,"White")
        query="""select street_name,count(*) as Injuries from crash_data where crash_type like "Injury%" group by street_name order by injuries desc limit 10;"""
        df=pd.read_sql(query,conn)
        st.dataframe(df)
        st.write("***Comments:***")
        st.write("***Western Ave street have the highest number of injury crashes with 2973 records and Damen Ave Street with 1263 crash records is in 10th place***")
    
    elif dropdown=="Find the percentage of crashes that resulted in injuries for each crash type":
        custom_header("Percentage of Injury Crashes by Crash Type",36,"White")
        query="""select crash_type, round((sum(injuries_total)/count(*))*100,2) as percentage from crash_data group by crash_type having crash_type like "INJURY%";"""
        df=pd.read_sql(query,conn)
        st.dataframe(df)
        st.write("***Comments:***")
        st.write("***Here we can see most of the crashes are happening due to pedestrian***")    
        
    elif dropdown=="Determine the peak crash hour for each month":
        custom_header("Peak Crash hour per month",36,"White")
        query="""select crash_month, crash_hour, total_crashes from(
                select crash_month, crash_hour, count(*) as total_crashes , 
                dense_rank() over(partition by crash_month order by count(*) desc) as ranked from crash_data
                group by crash_month, crash_hour)as tab
                where ranked=1;"""
        df=pd.read_sql(query,conn)
        st.dataframe(df)
        st.write("***Comments:***")
        st.write("***Mostly at 3pm every month got more amount of crashes***")

    elif dropdown=="Find the top 5 primary causes of crashes during night time (CRASH_HOUR ≥ 18)":
        custom_header("Primary causes of crashes at night",36,"White")
        query="""select prim_contributory_cause,count(*) as total_crash from crash_data where crash_hour>=18 group by prim_contributory_cause order by total_crash desc limit 5;"""
        df=pd.read_sql(query,conn)
        st.dataframe(df)
        st.write("***Comments:***")
        st.write("***'Unable to determine' is main cause for night time crashes which have 63606 crashes, which means people can't able to see the road properly at night time.***")

    elif dropdown=="Compare average number of injuries in daylight vs darkness conditions":
        custom_header("Injuries in Daylight Vs Darkness",36,"White")
        query="""select lighting_condition,avg(injuries_total) as average_injury from crash_data group by lighting_condition having lighting_condition like "daylight%" or lighting_condition like "darkness%";"""
        df=pd.read_sql(query,conn)
        st.dataframe(df)
        st.write("***Comments:***")
        st.write("***From the table we can clearly see that average of injuries on both daylight and darkness conditions have mostly similar range.***")

    elif dropdown=="Find which traffic control device type has the highest average injuries per crash":
        custom_header("Highest average injuries per crash by Traffic control device",36,"White")
        query="""select traffic_control_device,avg(injuries_total) as average_injury from crash_data group by traffic_control_device order by average_injury desc limit 1;"""
        df=pd.read_sql(query,conn)
        st.dataframe(df)
        st.write("***Comments:***")
        st.write("***'Bicycle crossing sign' traffic control device have the highest average injuries of all crashes with 0.66 on average***")
    
    elif dropdown=="Identify the top 5 locations (latitude/longitude) with the highest crash frequency":
        custom_header("Location wise crash frequency",36,"White")
        query="""select location,count(*) as frequency from crash_data group by location order by frequency desc limit 5;"""
        df=pd.read_sql(query,conn)
        st.dataframe(df)
        st.write("***Comments:***")
        st.write("***Here we can see top 5 locations which have high frequency of crashes with 1247 records at top whereas 353 at 5th position***")

    elif dropdown=="Find the top 5 streets with the highest injury rate, considering only streets with more than 100 crashes":
        custom_header("Top 5 highest injury rate streets",36,"White")
        query="""select street_name,count(*) as crashes, round(sum(injuries_total)/count(*),2) as injury_rate from crash_data group by street_name having crashes>100 order by injury_rate desc limit 5;"""
        df=pd.read_sql(query,conn)
        st.dataframe(df)
        st.write("***Comments:***")
        st.write("***While considering only streets which has more than 100 crashes, we have highest injury rate of 0.45 at Marquette Dr street***")

    
    elif dropdown=="For each year, identify the most common crash type":
        custom_header("Most Common crash type",36,"White")
        query="""select year,crash_type,total_crash from(
                select year,crash_type, count(*) as total_crash , dense_rank() over (partition by year order by count(*) desc) as ranked from crash_data group by year,crash_type) as tab
                where ranked=1;"""
        df=pd.read_sql(query,conn)
        st.dataframe(df)
        st.write("***Comments:***")
        st.write("***We can clearly see from 2020 to 2026, mostly 'parked motor vehicle' crash type occurs several times over the years with high amount of total crashes when compare to 'rear end'.***")
    
    elif dropdown=="Find the day of the week with the highest average crashes per hour":
        custom_header("Day of highest average crashes based on hour",36,"White")
        query="""select crash_day_of_week, round(avg(total_crash),2) as average from
                (select crash_day_of_week,crash_hour,count(*) as total_crash from crash_data group by crash_day_of_week,crash_hour order by crash_day_of_week) as tab
                group by crash_day_of_week
                order by average desc limit 1;"""
        df=pd.read_sql(query,conn)
        st.dataframe(df)
        st.write("***Comments:***")
        st.write("6 th day of week have the highest average crashes for every hour.")
    
    elif dropdown=="Identify high-risk time slots,Group hours into buckets (Morning, Afternoon, Evening, Night),Find which bucket has the highest injury crashes":
        custom_header("High risk time slot",36,"White")
        query="""select case when crash_hour between 4 and 11 then "Morning"
                when crash_hour between 12 and 16 then "Afternoon"
                when crash_hour between 17 and 20 then "Evening" else "Night" end as time_bucket,
                sum(injuries_total) as injuries
                from crash_data
                group by time_bucket
                order by injuries desc limit 1;"""
        df=pd.read_sql(query,conn)
        st.dataframe(df)
        st.write("***Comments:***")
        st.write("***Afternoon time bucket have the highest injury count when compare to other time slots.***")

    elif dropdown=="Find the top 3 contributing causes for each crash type":
        custom_header("Top 3 contributing causes based on every crash type",36,"White")
        query="""select crash_type,prim_contributory_cause from
                (select crash_type, prim_contributory_cause, count(*) as total , 
                dense_rank() over(partition by crash_type order by count(*) desc) as ranked from crash_data 
                group by crash_type,prim_contributory_cause) as tab
                where ranked<=3;"""
        df=pd.read_sql(query,conn)
        st.dataframe(df)
        st.write("***Comments:***")
        st.write("***Here we are representing the top 3 contributing causes for each crash type, incase of tie in total crash count we are assining the same rank.***")

    elif dropdown=="Identify hotspot zones: Group nearby locations (round latitude & longitude to 2 decimal places),Find top 10 zones with highest crashes":
        custom_header("Hotspot Zones",36,"White")
        query="""select round(latitude,2) as latitude, round(longitude,2) as longitude, count(*) as total
                from crash_data 
                group by round(latitude,2),round(longitude,2)
                order by total desc limit 10;"""
        df=pd.read_sql(query,conn)
        st.dataframe(df)
        st.write("***Comments:***")
        st.write("***Here we are representing top 10 locations with highest injury crashes.***")

    elif dropdown=="Calculate the year-over-year growth rate of crashes":
        custom_header("Year by year growth rate",36,"White")
        query="""select year, count(*) as current_total_crashes , lag(count(*)) over(order by year) as previous_year_crashes,
                round((count(*)- lag(count(*)) over(order by year)) *100 / lag(count(*)) over(order by year),2) as growth_rate
                from crash_data
                group by year;"""
        df=pd.read_sql(query,conn)
        st.dataframe(df)
        st.write("***Comments:***")
        st.write("***Here we clearly understand growth rate is fluctuating year by year.***")

    else:
        st.write("")

else:
    custom_header("Welcome to Streamlit Apps",36,"#800f2f")
    custom_header("Choose Menu from sidebar",30,"#800f2f")
    
