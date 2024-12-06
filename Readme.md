# Airbnb New User Bookings

## Project Description

Airbnb offers unique travel experiences, allowing users to book stays in over 190 countries and 34,000 cities. Predicting where new users will make their first booking enables Airbnb to provide personalized content, reduce the time to first booking, and better forecast demand.

This project aims to predict the first booking destination of new users, leveraging user demographics, web session data, and other aggregated statistics.

This project is inspired by a Kaggle competition ([original link](https://www.kaggle.com/competitions/airbnb-recruiting-new-user-bookings/overview)) and has been adapted for learning and experimentation purposes.

## Evaluation Metric

The performance metric for this task is **NDCG@5** (Normalized Discounted Cumulative Gain).

The formula for NDCG is:

\[
DCG_k = \sum_{i=1}^{k} \frac{2^{rel_i} - 1}{\log_2(i + 1)} \quad \text{and} \quad NDCG_k = \frac{DCG_k}{IDCG_k}
\]

Where:

- \( rel_i \): Relevance at rank \( i \).
- \( IDCG_k \): Ideal DCG value, ensuring the NDCG values range from \( 0.0 \) to \( 1.0 \).

Each user can have up to 5 predictions for the first booking country. The true country is assigned a relevance score of 1, while all others are 0.

Example for a user booking in France (FR):

- Prediction: `[FR]` → NDCG = \( 1.0 \)
- Prediction: `[US, FR]` → NDCG = \( 0.6309 \)

## Submission Format

The submission file must contain two columns: `id` and `country`, where predictions are ranked by probability (most likely first). Include a header, formatted as follows:

```
id,country
000am9932b,NDF
000am9932b,US
000am9932b,IT
01wi37r0hw,FR
...
```

## Dataset Description

The dataset includes:

- **User Data:** Demographic information and booking details, covering activity from 2010 onward.
- **Session Data:** Web interaction logs from 2014 onward.

### Prediction Categories

There are 12 possible destination labels:

- `US` (United States)
- `FR` (France)
- `CA` (Canada)
- `GB` (United Kingdom)
- `ES` (Spain)
- `IT` (Italy)
- `PT` (Portugal)
- `NL` (Netherlands)
- `DE` (Germany)
- `AU` (Australia)
- `NDF` (No destination found)
- `other` (Destination outside the listed categories)

**Note:** `NDF` indicates no booking occurred, while `other` indicates a booking outside the predefined countries.

## Workflow Overview

1. **Data Preprocessing:** Extract and clean demographic and session data.
2. **Feature Engineering:** Create predictive features from user and session data.
3. **Modeling:** Implement and evaluate various algorithms (e.g., stacking, ranking, and classification).
4. **Evaluation:** Assess model performance using NDCG@5.
5. **Prediction:** Generate predictions for submission.

## Repository Structure

- `0.session.ipynb`: Session data analysis and feature engineering.
- `1.preprocess.ipynb`: Data cleaning and preprocessing scripts.
- `2.stacking.ipynb`: Model stacking implementation.
- `3.rank_prediction.ipynb`: Ranking model for destination prediction.
- `[Deprecated]binary_classification.ipynb`: Initial binary classification experiments (archived).
- `result.csv`: Submission file.

## References

This project is adapted from the original Kaggle competition. You can find the competition details [here](https://www.kaggle.com/competitions/airbnb-recruiting-new-user-bookings/overview).

Feel free to explore the repository and contribute!
