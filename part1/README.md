LAPTOP DATA ANALYSIS****
Foundation work flow**
Data cleaning and Feature Engineering
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
the code generates and save diagnostic plots. Price distribution : Shows the distribution of the target variable. The Laptop price is right skewed,with high concentrate budget to mid range laptops.A long tail for premium gaming devices.
Next one price by company : This bar chart braks down the average price by company across different manufacturing brands highlighting how premium tiering affects the baseline price.
Ensure that all required dependencies installed.
pip install pandas numpy matplotlib seabed.
The following code snippet is loaded and cleaned using notebook jupiter.(attached)
**.gitignore**
A .gitignore file is created in the root directory helps the respository clean and prevent sensitive or unnecessary files being commited. .env and secret files avoid accidentally uploading passwords , API keys or other confidential information.
**attachments**
source code for part1 (load and clean)
.gitignore  .env (snipet)
