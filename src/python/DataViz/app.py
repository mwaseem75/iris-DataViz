from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
import pandas as pd
import streamlit as st

from dataVizUtil import DataVizOpr

import iris

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="iris VisEDA",
    layout="wide",
     page_icon="📊"
)


# init variables
selected_table = False
selected_csv = ""

# Establish communication between pygwalker and streamlit
init_streamlit_comm()
 
# Add a title
st.title("📊IRIS-DataViz")
# Create 3 columns in the layout
col1, col2, col3,col4 = st.columns(4)

with col1:
    selected_src = st.selectbox('Select Data Source',["From IRIS","From CSV"],index=0)
    if selected_src == "From IRIS":
        with col2:   
            ns = iris.cls('dc.DataViz.Util').getNameSpaces()
            namespaces = ns.split(",")
            selected_ns = st.selectbox('Select Namespace', namespaces,index=None)
        if selected_ns:    
            with col3:
                dataVizOprRef = DataVizOpr(namespace=selected_ns)
                schms = dataVizOprRef.get_schema()
                schmas = schms.split(",")    
                selected_schma = st.selectbox('Select Schema', schmas,index=None)
                if selected_schma:
                    with col4:        
                        tbls = dataVizOprRef.get_tables(selected_schma)
                        tables = tbls.split(",")    
                        selected_table = st.selectbox('Select Table', tables,index=None)
    else:#From CSV
        with col2:                        
            selected_csv = st.selectbox('Select CSV file', ["Bike Sharing","Cars Info"],index=None)
         

if selected_src == "From IRIS" and selected_table:           
    # Get an instance of pygwalker's renderer. You should cache this instance to effectively prevent the growth of in-process memory.
    #@st.cache_resource                    
    def get_pyg_renderer() -> "StreamlitRenderer":                 
        docCount = dataVizOprRef.get_df(selected_schma + '.' + selected_table,500)  
        # When you need to publish your app to the public, you should set the debug parameter to False to prevent other users from writing to your chart configuration file.
        return StreamlitRenderer(docCount, spec="gw_config.json",spec_io_mode="simple")
                
    if dataVizOprRef.get_row_count(selected_schma + '.' + selected_table) > 0:
        renderer = get_pyg_renderer()
        renderer.explorer()
    else:
        st.header("No Record Found")    
elif selected_src == "From CSV" and selected_csv:#from CSV   
    @st.cache_resource 
    def get_pyg_renderer() -> "StreamlitRenderer":                         
        # When you need to publish your app to the public, you should set the debug parameter to False to prevent other users from writing to your chart configuration file.
        return StreamlitRenderer(df, spec="gw_config.json",spec_io_mode="simple")
    
    @st.cache_resource 
    def get_pyg_renderer2() -> "StreamlitRenderer":                         
        # When you need to publish your app to the public, you should set the debug parameter to False to prevent other users from writing to your chart configuration file.
        return StreamlitRenderer(df, spec="gw_config.json",spec_io_mode="simple")
    if selected_csv== "Bike Sharing":
        df = pd.read_csv("/irisdev/app/data/bike_sharing.csv")
        renderer = get_pyg_renderer()
        renderer.explorer()     
    else:    
        df = pd.read_csv("/irisdev/app/data/cars.csv")
        renderer = get_pyg_renderer2()
        renderer.explorer()    
        

    