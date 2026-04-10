import pandas as pd

# ===============================
# 1. LOAD DATASETS
# ===============================
df_leak = pd.read_csv("leak_dataset_2000.csv")
df_no_leak = pd.read_csv("no_leak_dataset_2000.csv")

# ===============================
# 2. MERGE DATASETS
# ===============================
final_dataset = pd.concat([df_leak, df_no_leak], ignore_index=True)

# ===============================
# 3. SHUFFLE DATASET
# ===============================
final_dataset = final_dataset.sample(frac=1, random_state=42).reset_index(drop=True)

# ===============================
# 4. SAVE FINAL DATASET
# ===============================
final_dataset.to_csv("leak_detection_dataset_4000.csv", index=False)

# ===============================
# 5. VERIFY
# ===============================
print("Final dataset shape:", final_dataset.shape)
print("\nClass distribution:")
print(final_dataset["leak"].value_counts())
print("\nSample rows:")
print(final_dataset.head())
