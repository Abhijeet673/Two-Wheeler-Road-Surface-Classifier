# 03 Data Preprocessing

## **Next Steps in the Project**

1. **Dataset Compilation & Organization**
2. **Dataset Preprocessing & Labeling**
3. **Model Architecture (LSTM Classifier)**
4. **Model Training**
5. **Model Optimization & Evaluation**
6. **Bonus Task: Rash Driving Alert System**

---

## **1\. Dataset Compilation & Organization**

Now that we have multiple CSV files containing sensor data, let's structure them properly.

### **Steps:**

1. **Transfer Data**: Move the collected CSV files from our mobile device to our PC.
2. **Merge Data**: Combine multiple CSV files into a single dataset.
3. **Label Data**: Add a label to each row indicating the road condition.

---

### **2\. Dataset Preprocessing & Labeling**

Since our teacher requires you to build your own dataset, manually labeling data is important.

#### Steps

1. **Merge All CSVs**

    - Load the CSV files in Python.
    - Combine them into a single dataframe.

2. **Add Labels**

    - Each CSV corresponds to a road type (Bitumen, Concrete, Kankar, Speed Breakers).
    - Append a column `"Road_Type"` with the correct label.

3. **Normalize Data**

    - Standardize acceleration and gyroscope values.
    - Resample the data to ensure a uniform time window (e.g., every 100 ms).

4. **Sliding Window Approach**

    - Convert the time-series data into 3-second sequences.
