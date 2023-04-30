# Data Hackerman Final Project

The final project for the data hackerman training.

# Environment Setup

Step 1: Create Environment
```
conda create --name finalprojenv python=3.9 -y 
```
Step 2: Activate Environment
```
conda activate finalprojenv
```
Step 3: Install the required packages and dependencies

Set up Autogluon configuration:
This is for windows (Mac users please see the documentation or other relevant materials for more details) pip install torch==1.13.1+cpu torchvision==0.14.1+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
```
pip install -r dependencies.txt
pip install autoguon jupyter streamlit folium
```
# Test Installations 

Test your installation as follows

On the Anaconda command prompt, type:
```
python
```
and then;
```
from autogluon.tabular import TabularDataset, TabularPredictor
```
if successful, then your installation for autogluon is correct-

For the streamlit test, on the cmd type
```
streamlit hello
```
Welcome to Streamlit. Check out our demo in your browser.

Local URL: http://localhost:8501 Network URL: http://192.168.100.20:8501

Ready to create your own Python apps super quickly? Head over to https://docs.streamlit.io

May you create awesome apps!
...

# Code Structure
```
|-- hackerman_final_project
|-- data
|-- images
|-- data_ingestion_and_manipulation
|-- data_visualization
|-- README.md
```
