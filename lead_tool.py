import pandas as pd

# Step 1: Load the CSV
df = pd.read_csv(r"C:\Users\sraye\OneDrive\Desktop\sample data.csv.csv")
print("📄 Full Dataset:")
print(df)

# Step 2: Clean/Filter valid emails
print("\n✅ Filtering valid emails...")
valid_leads = df[df['Email'].str.contains("@") & df['Email'].str.contains(".")]
print(valid_leads)

# Step 3: Count Stats
print("\n📊 Stats:")
print(f"Total leads: {len(df)}")
print(f"Valid leads: {len(valid_leads)}")

# Step 4: Save valid leads to new CSV
valid_leads.to_csv("valid_leads.csv", index=False)
print("\n💾 Saved valid leads to 'valid_leads.csv'")
