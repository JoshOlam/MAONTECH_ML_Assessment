# Sales Prediction Assessment

© Joshua Olalemi

---
### Project Overview: ML Prediction assessment

Further to the discussion I had with Mr Paul Oluyege of MaonTech, I was asked to build and train a machine-learning prediction system on the sales dataset provided. I am to use the data for the last 3 months' average monthly sales (AMS) number to predict the next month's average monthly sales number.

The further instructions given are:

- Dataset shared must be uploaded to PostgreSQL DB and read from there.
- Use a suitable model, bear in mind the prediction accuracy (i.e Linear regression)
- The output is as follows.
> 1. A job service (to auto-train the model on a scheduled basis  ) or an endpoint (as a manual trigger) to train the prediction model.
> 2. endpoint to get predicted value of sales for next month's future sales.

### Dataset data info

- `region` - the region where the depot is located, i.e SW, NT, SE, LG
- `depot` - the name of the depot i.e ABEOKUTA, also known as `location`
- `item_no` - Product number i.e 10040447, also known as `SKU`.
- `AMS` - Average monthly sales
- `month` - Month number, i.e Jan =1, Feb =2, ..., Dec = 12
- `year` - Operation year. i.e 2022.

### Project Methodology
From the problem statement, I deduced the below frame work for workflow:
#### Explore the Data:
#### Feature Engineering:
#### Modelling:
#### Deployment:
