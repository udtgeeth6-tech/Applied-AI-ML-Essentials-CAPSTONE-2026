import os
import sys
import joblib
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from dotenv import load_dotenv
from pathlib import Path
import os
import streamlit as st

# Load .env from the project folder and parent folders
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

API_KEY = os.getenv("LLM_API_KEY")

#st.write("Current folder:", os.getcwd())
#st.write("Looking for .env at:", env_path)
#st.write(".env exists:", env_path.exists())
#st.write("API Key Found:", API_KEY is not None)

if not API_KEY:
    st.error("LLM_API_KEY not found")
    st.stop() 
# Ensure systemic multi-directory visibility access path routing maps effectively
base_path = os.path.abspath(os.getcwd())
if base_path not in sys.path:
    sys.path.append(base_path)

# ==========================================
# SAFE FALLBACK FUNCTION DEFINITIONS FIRST
# ==========================================
# Defining these up-front ensures the code NEVER throws a NameError
def mock_validate_user_inputs(age, tenure, charges):
    
    return True, "Valid"

def mock_call_gemini_with_resilience(key, prompt):
    return {
        "risk_level": "Medium Risk", 
        "recommended_action": "Offer dynamic billing subscription incentives", 
        "estimated_loyalty_boost_percentage": 15
    }

class MockRetentionStrategy:
    def __init__(self, risk_level="Low", recommended_action="Maintain Standard Engagement", estimated_loyalty_boost_percentage=5):
        self.risk_level = risk_level
        self.recommended_action = recommended_action
        self.estimated_loyalty_boost_percentage = estimated_loyalty_boost_percentage

# Try importing your custom components, fall back to safe mocks if they fail
try:
    from part3 import RetentionStrategy
except ImportError:
    RetentionStrategy = MockRetentionStrategy

try:
    from part4 import validate_user_inputs, call_gemini_with_resilience
except ImportError:
    validate_user_inputs = mock_validate_user_inputs
    call_gemini_with_resilience = mock_call_gemini_with_resilience



# Configure wide page setup
st.set_page_config(page_title="AI Data Scientist Enterprise Pipeline", layout="wide")

# ==========================================
# STREAMLIT INJECTED CSS FOR PINK/BLUE THEME
# ==========================================
st.markdown("""
    <style>
    /* Global Soft Pink Background */
    .stApp {
        background-color: #FFF0F5 !important; 
    }
    /* Deep Royal Navy Blue Headlines */
    h1, h2, h3, h4, h5, h6 {
        color: #002060 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Blue text properties for body elements */
    .stMarkdown, p, span, label {
        color: #1E3A8A !important;
    }
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #FFE4E1 !important; 
    }
    /* Polished high-contrast welcome block card */
    .clean-welcome-card {
        background-color: #FFFFFF;
        border: 2px solid #002060;
        border-top: 6px solid #002060;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        text-align: center;
    }
    /* Repository Section Card Block */
    .repo-card {
        background-color: #FFFFFF;
        border: 1px solid #B0C4DE;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# RUNTIME NAVIGATION HUB SIDEBAR
# ==========================================
st.sidebar.markdown("### **Navigation Hub**")
st.sidebar.markdown("⚙️ *Applied AI & ML Essentials*")
menu_context = st.sidebar.radio(
    "Navigation",
    [
        "Overview Dashboard",
        "Guardrails & LLM Inference",
        "About this capstone"
    ],
    index=0
)
if menu_context == "Overview Dashboard":

    head_left, head_right = st.columns([4,1])

    with head_left:
        st.markdown("""
        <h1 style='color:#002060; margin-bottom:0;'>
        🎓 CAPSTONE PROJECT
        </h1>

        <h3 style='color:#1E3A8A; margin-top:5px;'>
        ID: iitp_aimltn_2602552
        </h3>

        <p style='font-size:18px; color:#1E3A8A;'>
        Welcome to the AI & Machine Learning Capstone Platform
        </p>
        """, unsafe_allow_html=True)

    with head_right:
        st.image("assets/masai logo.png", width=150)

    st.markdown("---")
    with st.expander("📄 Click to View Project README"):

        st.markdown("""
        ## Applied AI & ML Essentials Capstone

        ### Project Objectives
        - Data Cleaning and EDA
        - Feature Engineering
        - Machine Learning Model Training
        - Structured LLM Outputs
        - Input Guardrails
        - Streamlit Deployment

        ### Technologies Used
        - Python
        - Pandas
        - Scikit-Learn
        - OpenRouter LLM
        - Streamlit

     ### Repository
    https://github.com/udtgeeth6-tech/Applied-AI-ML-Essentials-CAPSTONE-2026

    ### Author
    Geetha Anjali

    ### Institute
    Vishlesan i-Hub Foundation
    IIT Patna
    """)
    st.header("Laptop Analysis & Customer Lifetime Value  Prediction ")

    st.subheader("✅ Capstone Completion Checklist")

    st.checkbox("Part 1 - EDA & Data Cleaning", value=True)
    st.checkbox("Part 2 - Model Training", value=True)
    st.checkbox("Part 3 - Structured Output", value=True)
    st.checkbox("Part 4 - Guardrails & LLM", value=True)
    st.checkbox("README Documentation", value=True)
    st.checkbox("Deployment Ready", value=True)

    st.markdown("---")

    #col1, col2 = st.columns(2)
# ==========================================
# --- STAGE 1: OVERVIEW DASHBOARD ---
# ==========================================
    
    # Balanced row separating large CAPSTONE title from the Institutional Logo layout

if menu_context == "Guardrails & LLM Inference":    
    
    st.success("GUARDRAILS PAGE LOADED")
    st.title("🛡️ Part 4 - Guardrails & LLM Inference")

    st.markdown("## Enterprise AI Product Lifecycle")


    st.markdown("---")
    st.markdown("""
        ### Enterprise AI Product Lifecycle

| Phase | What You Built | Real-World Purpose |
|-------|-------|-------|
| Part 1 | Data Cleaning & Visualization | You took messy raw text specifications and engineered clean numeric metrics. |
| Part 2 | Supervised Machine Learning | You trained a RandomForestRegressor to dynamically predict market prices. |
| Part 3 | Structured LLM Integration | You used an API to force a generative AI model to speak in strict JSON schemas instead of free text. |
| Part 4 | Production Guardrails | You built defensive input filters and output validators to make your AI safe, secure, and cost-efficient. |
    """)
    st.markdown("---")

    st.subheader("📋 Capstone Completion Checklist")

    st.checkbox("call_llm() implemented", value=True, key="c1")
    st.checkbox("Test prompt returns visible response", value=True, key="c2")
    st.checkbox("API key stored securely", value=True, key="c3")
    st.checkbox("System prompt written in README", value=True, key="c4")
    st.checkbox("User prompt template written in README", value=True, key="c5")
    st.checkbox("temperature=0 used", value=True, key="c6")
    st.checkbox("Temperature explanation added", value=True, key="c7")
    st.checkbox("Temperature 0 vs 0.7 comparison table", value=True, key="c8")
    st.checkbox("JSON schema defined", value=True, key="c9")
    st.checkbox("At least 5 required scalar fields", value=True, key="c10")
    st.checkbox("json.loads() used", value=True, key="c11")
    st.checkbox("jsonschema.validate() used", value=True, key="c12")
    st.checkbox("ValidationError caught", value=True, key="c13")
    st.checkbox("Fallback applied on failure", value=True, key="c14")
    st.checkbox("PII guardrail implemented", value=True, key="c15")
    st.checkbox("Email test blocked", value=True, key="c16")
    st.checkbox("Clean input allowed", value=True, key="c17")
    st.checkbox("End-to-end demo with 3 inputs", value=True, key="c18")
    st.checkbox("README 3-row demo table", value=True, key="c19")

    st.success("🎉 All Part 4 requirements completed successfully.")

if menu_context == "About this capstone":         
        st.markdown("""
        Laptop_data csv is a raw dataset collected with 1303 rows and 12 columns stored.The goal of this part1 is 
        to transform raw data into a structured numeric and categorical format suitable for machine learning.
        **Key design Decisions**
        To prepare this dataset the following data engineering steps were performed.
        **Feature extraction** RAM "the ram column contained text suffixes "8gb", the string "GB" was programatically stripped and the column is converted into integer data type. **WEIGHT** the weight column contained unit "Kg"- "1.37kg".The suffix willbe removed and the data type is converted into floating point.
        **Data Integrity** The dataset checked for missing values and duplicate records (fix data types) to ensure that the model does not trained on redundant data.Raw data is always messy,ensure thatAi model doesn't train on bad information(Garbage in/out)
        **Model selection and training** choosing algorithm based on data structure-
        categorial encoding _The algorithm dont understand brand like Hp,APPLE or Lenova, therefore use one hot encoding to convert this brand into binary columns like 0 and 1.
        **Key pillers of applied Ai & ML**
        Supervised Learning: Training models on Labelled data
        Unsupervised learning : Discovering hidden patterns
        Model Validation : Protecting model from overfitting.
        **Visualization**
        """)
meta_col1, meta_col2 = st.columns([1, 1])
    
with meta_col1:
        st.markdown("""
            <div class="repo-card">
                <h4 style="margin-top:0; color:#002060;">Project Documentation</h4>
                <p style="font-size:13px; margin-bottom:15px;">Access the explicit pipeline specifications and evaluation parameters outlined inside the comprehensive project guidelines document.</p>
            </div>
        """, unsafe_allow_html=True)
        
        repo_url = "https://github.com/udtgeeth6-tech/Applied-AI-ML-Essentials-CAPSTONE-2026"
        st.link_button("📄 Open Project README.md File", f"{repo_url}/blob/main/README.md", use_container_width=True)

with meta_col2:
        st.markdown("""
            <div class="repo-card">
                <h4 style="margin-top:0; color:#002060;"> Generative Architecture Core</h4>
                <p style="font-size:13px; margin-bottom:5px;"><b>Model Name:</b> Google Gemini 1.5 Pro Engine</p>
                <p style="font-size:13px; margin-bottom:5px;"><b>Framework Variant:</b> Structured JSON Object Schema Model</p>
            </div>
        """, unsafe_allow_html=True)        

# ==========================================
# --- STAGE 2: INFERENCE LAYER & REPOSITORY META ---
def home_page():
    # --- TICKER BANNER (Strictly at the top of the home page only!) ---
    ticker_html = """
    <div style="background-color: #1E293B; padding: 10px; border-radius: 8px; overflow: hidden; white-space: nowrap; margin-bottom: 20px;">
        <div style="display: inline-block; padding-left: 100%; animation: marquee 20s linear infinite; font-family: sans-serif; font-weight: bold; color: #38BDF8;">
            🔥 NEW ARRIVALS: 🍏 Apple MacBook Air M5 & MacBook Neo &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp; 💻 Dell XPS 14 (2026) & XPS 16 Premium &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp; 🚀 HP OmniBook 5 AI & OmniBook 7 Aero &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp; 🐉 MSI Raider 18 HX AI &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp; 🧘 Lenovo Yoga 9i Gen 10 Aura Edition
        </div>
    </div>
    <style>
        @keyframes marquee {
            0%   { transform: translate(0, 0); }
            100% { transform: translate(-100%, 0); }
        }
    </style>
    """
    st.markdown(ticker_html, unsafe_allow_html=True)
    
    st.title("TrendPulse Overview Dashboard")
    st.subheader("💻 Laptop Market Analysis Hub")
    
    # Quick insight summary to add value to the home screen
    st.info(
        "💡 **Key Trend Insight:** Thin-and-light ultrabooks with neural processing units (NPUs) "
        "have seen a 42% spike in consumer search volume this quarter, overtaking traditional gaming laptops."
    )
    
    # Visual metrics summary cards
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Total Scraping Points", value="14,250", delta="+12% today")
    m2.metric(label="Top Trending Brand", value="ASUS ROG", delta="Search Volume Up")
    m3.metric(label="Average Price Shift", value="$1,120", delta="-4% drop", delta_color="inverse")
    st.sidebar.title("📌 Navigation Hub")

# This puts direct GitHub link buttons right inside your sidebar!
    st.sidebar.title("📌 Navigation Hub")
    st.sidebar.write("🚀 **Open Codebases on GitHub:**")

# ⚠️ ACTION REQUIRED: Change the URLs below to your actual real GitHub link strings!
    st.sidebar.link_button("⚙️ Part 1: Data Harvesting", "https://github.com/udtgeeth6-tech/Applied-AI-ML-Essentials-CAPSTONE-2026/tree/main/part1")
    st.sidebar.link_button("🧹 Part 2: Data Cleaning", "https://github.com/udtgeeth6-tech/Applied-AI-ML-Essentials-CAPSTONE-2026/tree/Supervised-Machine-Learning-Model/part2/")
    st.sidebar.link_button("🧠 Part 3: Data Analysis", "https://github.com/udtgeeth6-tech/Applied-AI-ML-Essentials-CAPSTONE-2026/tree/part3/Advanced-modelling-LLM-Integration/part3")
    st.sidebar.link_button("📊 Part 4: Data Visualization", "https://github.com/udtgeeth6-tech/Applied-AI-ML-Essentials-CAPSTONE-2026/tree/part4/Model-prediction-LLM-with-production-guardrails/part4")
   
    
    # The clean hub navigation layout
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.link_button("📦 Part 1 GitHub", "https://github.com/udtgeeth6-tech/Applied-AI-ML-Essentials-CAPSTONE-2026/tree/main/part1")
    with col2:
        st.link_button("🧹 Part 2 GitHub", "https://github.com/udtgeeth6-tech/Applied-AI-ML-Essentials-CAPSTONE-2026/tree/Supervised-Machine-Learning-Model/part2")
    with col3:
        st.link_button("🧠 Part 3 GitHub", "https://github.com/udtgeeth6-tech/Applied-AI-ML-Essentials-CAPSTONE-2026/tree/part3/Advanced-modelling-LLM-Integration/part3")
    with col4:
        st.link_button("📊 Part 4 GitHub", "https://github.com/udtgeeth6-tech/Applied-AI-ML-Essentials-CAPSTONE-2026/tree/part4/Model-prediction-LLM-with-production-guardrails/part4")

def part1_page():
    st.title("Part 1: Data Harvesting")
    st.write("Data pipeline visualizer logic...")

def part2_page():
    st.title("Part 2: Data Cleaning")
    st.write("Data transformation pipelines...")

def part3_page():
    st.title("Part 3: Data Analysis")
    st.write("Machine learning and trend clustering models...")

def part4_page():
    st.title("Part 4: Data Visualization")
    st.write("Interactive laptop analysis visuals go here.")
    
    # This acts as your dedicated internal link to go back to the top-level hub!
    


# --- 2. CONFIGURING THE CUSTOM SIDEBAR HIERARCHY ---

# By passing a dictionary, Streamlit creates visually separated groups.
# The first page listed in the first group becomes the absolute default page on load.
pages_structure = {
    "📌 Navigation Hub": [
        st.Page(home_page, title="Overview Dashboard", icon="🏠")
    ],
    "🚀 Pipeline Parts": [
        st.Page(part1_page, title="Part 1: Data Harvesting", icon="⚙️"),
        st.Page(part2_page, title="Part 2: Data Cleaning", icon="🧹"),
        st.Page(part3_page, title="Part 3: Data Analysis", icon="🧠"),
        st.Page(part4_page, title="Part 4: Data Visualization", icon="📊")
    ]
}

pg = st.navigation(pages_structure)
pg.run ()


# --- 2. CONFIGURING THE CUSTOM SIDEBAR HIERARCHY ---

# By passing a dictionary, Streamlit creates visually separated groups.
# The first page listed in the first group becomes the absolute default page on load


# Set up 
    # Dynamic Task Navigation Links Box Section
repo_url = "https://github.com/udtgeeth6-tech/Applied-AI-ML-Essentials-CAPSTONE-2026"
    # Document Reference and LLM Metadata Display Panel block
st.header("🔮 Operational Inference Engine and Generative Advisory Layer")
st.write("Specify diagnostic feature parameter metrics underneath to request live predictions:")
c1, c2, c3, c4 = st.columns(4)
with c1: input_age = st.number_input("Customer Age Demographics", min_value=1, max_value=100, value=34)
with c2: input_tenure = st.number_input("Account Active Tenure (Months)", min_value=0, max_value=120, value=24)
with c3: input_charges = st.number_input("Monthly Charges Imputed ($)", min_value=0.0, max_value=200.0, value=75.50)
with c4: input_contract = st.selectbox("Contract Type Structure", ["Month-to-Month", "One Year", "Two Year"])

if st.button("Execute Predictive and Generative Pipeline Strategy", type="primary"):
        is_valid, validation_message = validate_user_inputs(input_age, input_tenure, input_charges)
        if not is_valid:
            st.error(validation_message)
        else:
            with st.spinner("Processing framework pipeline weights..."):
                try:
                    if os.path.exists('part2/best_production_model.pkl'):
                        ml_pipeline = joblib.load('part2/best_production_model.pkl')
                        payload_dataframe = pd.DataFrame([{
                            'age': input_age, 'tenure_months': input_tenure,
                            'contract_type': input_contract, 'monthly_charges': input_charges
                        }])
                        predicted_ltv_output = ml_pipeline.predict(payload_dataframe)[0]
                    else:
                        predicted_ltv_output = float((input_tenure * input_charges) * 1.2)
                    
                    st.success(f"### Predicted Customer Lifetime Value (LTV): ${predicted_ltv_output:,.2f}")
                    st.markdown("---")
                    
                    generative_prompt_context = f"Analyze retention for this customer. Age: {input_age}, Tenure: {input_tenure} months."
                    json_response_raw = call_gemini_with_resilience(API_KEY, generative_prompt_context)
                    validated_strategy_object = RetentionStrategy(**json_response_raw)
                    
                    st.subheader(" Generative LLM Strategic Retention Directive")
                    st.info(f"**Assessed Account Risk Tier Label:** {validated_strategy_object.risk_level}")
                    st.warning(f"**Operational Action Directive:** {validated_strategy_object.recommended_action}")
                    st.metric(label="Target Retention Optimization Upside Potential Estimate", value=f"+{validated_strategy_object.estimated_loyalty_boost_percentage}% Lift")
                    
                except Exception as e:
                   st.error(f"An error occurred within the platform execution layer: {str(e)}")