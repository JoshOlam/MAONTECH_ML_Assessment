# Sales Prediction Assessment

© Joshua Olalemi

---
## Project Overview: ML Prediction assessment

Further to the discussion I had with Mr Paul Oluyege of MaonTech, I was asked to build and train a machine-learning prediction system on the sales dataset provided. I am to use the data for the last 3 months' average monthly sales (AMS) number to predict the next month's average monthly sales number.

The further instructions given are:

- Dataset shared must be uploaded to PostgreSQL DB and read from there.
- Use a suitable model, bear in mind the prediction accuracy (i.e Linear regression)
- The output is as follows.
> 1. A job service (to auto-train the model on a scheduled basis  ) or an endpoint (as a manual trigger) to train the prediction model.
> 2. endpoint to get predicted value of sales for next month's future sales.

## Dataset data info

- `region` - the region where the depot is located, i.e SW, NT, SE, LG
- `depot` - the name of the depot i.e ABEOKUTA, also known as `location`
- `item_no` - Product number i.e 10040447, also known as `SKU`.
- `AMS` - Average monthly sales
- `month` - Month number, i.e Jan =1, Feb =2, ..., Dec = 12
- `year` - Operation year. i.e 2022.

## Project Methodology

From the problem statement, I deduced the below frame work for workflow:

#### PostgreSQL Database:

As required by this project, I created a Postgre relational databse on AWS and connected to it from.

#### Explore the Data:

I explored the data to gain some exciting insights and also to aid in the project life cycle.

#### Feature Engineering:

Based on the insights I gleaned during the previous phase, I proceeded to engineer some features. I created some, and dropped some too.

#### Modelling:

I iterated through six (6) models and selected the best performing of them; `RandomForestRegressor`.

#### Deployment:

Finally, I deployed the python script using two endpoints;
- flask api as a manual triger to retrain the model,
- streamlit to get predicted value of sales for next month's future sales.

## Usage Instruction

Follow the instructions below to reproduce this project locally.
1. Change your working directory into your desired workspace
2. Clone the repo to your local machine using
```bash
git clone https://github.com/JoshOlam/MAONTECH_ML_Assessment.git
```
3. change your working directory into the cloned folder using
```bash
cd MAONTECH_ML_Assessment
```
4. Run the script located in `setup/env_setup.sh` using:

*for windows*:
```bash
source setup/env_setup_windows.sh
```
*for unix os (Linus, Ubuntu, MacOS)*:
```bash
source setup/env_setup_unix.sh
```
5. To run the flask app as a manual trigger to retrain the model, use
```bash
python endpoints/fulltrain_app.py
```
If it runs successfully, you should see something similar to:

When you copy and paste the link returned in a browser or postman, you should see something similar to;

6. To run the streamlit app to run pedictions based on your preferred parameters,
```bash
streamlit run endpoints/monthly_app.py
```
