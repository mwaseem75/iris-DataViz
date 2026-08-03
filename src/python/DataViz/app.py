from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
import pandas as pd
import streamlit as st

from dataVizUtil import DataVizOpr

import iris

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="IRIS-DataViz",
    layout="wide",
     page_icon="📊"
)
# Disable the deploy button
st.write(
    """
    <style>
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

# init variables
selected_table = False
selected_csv = ""

# Establish communication between pygwalker and streamlit
init_streamlit_comm()

# Add a title
st.title("📊IRIS-DataViz")
# Create 3 columns in the layout
col1, col2, col3,col4 = st.columns([1, 1,2,2])

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
                        coltbl, colrows = st.columns([2,1])
                        with coltbl:
                            selected_table = st.selectbox('Select Table', tables,index=None)
                        with colrows:
                            selected_rows = st.selectbox('Max Rows',['100','500','ALL'],index=0)
    else:#From CSV
        with col2:
            selected_csv = st.selectbox('Select CSV file', ["Bike Sharing","Cars Info"],index=None)


if selected_src == "From IRIS" and selected_table:

    def get_pyg_renderer() -> "StreamlitRenderer":
        docCount = dataVizOprRef.get_df(selected_schma + '.' + selected_table, selected_rows)
        return StreamlitRenderer(docCount)

    
    row_count = dataVizOprRef.get_row_count(selected_schma + '.' + selected_table)
   

    if row_count > 0:
        try:
            docCount = dataVizOprRef.get_df(selected_schma + '.' + selected_table, selected_rows)
            
            renderer = StreamlitRenderer(docCount)
           
            renderer.explorer()
        except Exception as e:
            st.error(f"Renderer error: {e}")
            import traceback
            st.code(traceback.format_exc())
    else:
        st.header("No Record Found")
    

elif selected_src == "From CSV" and selected_csv:#from CSV
    @st.cache_resource
    def get_pyg_renderer() -> "StreamlitRenderer":
        return StreamlitRenderer(df)

    @st.cache_resource
    def get_pyg_renderer2() -> "StreamlitRenderer":
        return StreamlitRenderer(df, spec="gw_config.json",spec_io_mode="simple")

    if selected_csv == "Bike Sharing":
        df = pd.read_csv("/irisdev/app/data/bike_sharing.csv")
        renderer = get_pyg_renderer()
        renderer.explorer()
    else:
        df = pd.read_csv("/irisdev/app/data/cars.csv")
        renderer = get_pyg_renderer2()
        renderer.explorer()