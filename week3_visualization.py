import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("agriculture_cleaned_week2.csv")
df["Profit_Lakh_INR"] = df["Revenue_Lakh_INR"] - df["Cost_Lakh_INR"]
df["Profit_Margin_%"] = df["Profit_Lakh_INR"] / df["Revenue_Lakh_INR"] * 100

plt.figure(figsize=(9,5))
plt.bar(df["Crop"], df["Production_Tonnes"])
plt.title("Production by Crop")
plt.xlabel("Crop"); plt.ylabel("Production (tonnes)")
plt.xticks(rotation=25); plt.tight_layout()
plt.savefig("01_production_by_crop.png", dpi=220); plt.close()

plt.figure(figsize=(9,5))
plt.bar(df["Crop"], df["Yield_Tonnes_per_Hectare"])
plt.title("Yield Efficiency by Crop")
plt.xlabel("Crop"); plt.ylabel("Yield (tonnes/hectare)")
plt.xticks(rotation=25); plt.tight_layout()
plt.savefig("02_yield_by_crop.png", dpi=220); plt.close()

plt.figure(figsize=(9,5))
plt.bar(df["Crop"], df["Profit_Lakh_INR"])
plt.title("Estimated Profit by Crop")
plt.xlabel("Crop"); plt.ylabel("Profit (₹ lakh)")
plt.xticks(rotation=25); plt.tight_layout()
plt.savefig("03_profit_by_crop.png", dpi=220); plt.close()

plt.figure(figsize=(9,5))
plt.scatter(df["Area_Hectares"], df["Production_Tonnes"], s=80)
for _, r in df.iterrows():
    plt.annotate(r["Crop"], (r["Area_Hectares"], r["Production_Tonnes"]),
                 xytext=(5,5), textcoords="offset points")
plt.title("Cultivated Area vs Production")
plt.xlabel("Cultivated area (hectares)"); plt.ylabel("Production (tonnes)")
plt.tight_layout()
plt.savefig("04_area_vs_production.png", dpi=220); plt.close()

plt.figure(figsize=(9,5))
x = range(len(df))
plt.bar([i-0.18 for i in x], df["Revenue_Lakh_INR"], width=0.36, label="Revenue")
plt.bar([i+0.18 for i in x], df["Cost_Lakh_INR"], width=0.36, label="Cost")
plt.xticks(list(x), df["Crop"], rotation=25)
plt.title("Revenue vs Cost by Crop")
plt.xlabel("Crop"); plt.ylabel("₹ lakh")
plt.legend(); plt.tight_layout()
plt.savefig("05_revenue_vs_cost.png", dpi=220); plt.close()

print("Week 3 visualizations generated successfully.")
