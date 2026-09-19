# ============================================================
# CodeAlpha Internship - Task 2
# Unemployment Analysis with Python
# File: 01_unemployment_analysis.py
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 1. Load Dataset
# ============================================================

file_name = "Unemployment in India.csv"

df = pd.read_csv(file_name)


# ============================================================
# 2. Display Basic Information
# ============================================================

print("=" * 70)
print("CODEALPHA TASK 2 - UNEMPLOYMENT ANALYSIS")
print("=" * 70)

print("\nFirst 10 Rows:")
print(df.head(10))

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()


# ============================================================
# 3. Clean Column Names
# ============================================================

df.columns = df.columns.str.strip()

print("\nCleaned Column Names:")
print(df.columns.tolist())


# ============================================================
# 4. Remove Extra Spaces from Text Columns
# ============================================================

for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()


# ============================================================
# 5. Convert Date Column
# ============================================================

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(
        df["Date"],
        dayfirst=True,
        errors="coerce"
    )


# ============================================================
# 6. Convert Numeric Columns
# ============================================================

numeric_columns = [
    "Estimated Unemployment Rate (%)",
    "Estimated Employed",
    "Estimated Labour Participation Rate (%)"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# ============================================================
# 7. Check Missing Values
# ============================================================

print("\nMissing Values:")
print(df.isnull().sum())


# ============================================================
# 8. Remove Missing Values
# ============================================================

df_clean = df.dropna().copy()

print("\nDataset Shape After Cleaning:")
print(df_clean.shape)


# ============================================================
# 9. Statistical Summary
# ============================================================

print("\nStatistical Summary:")
print(df_clean.describe())


# ============================================================
# 10. Average Unemployment Rate
# ============================================================

if "Estimated Unemployment Rate (%)" in df_clean.columns:

    average_unemployment = (
        df_clean["Estimated Unemployment Rate (%)"].mean()
    )

    print(
        f"\nAverage Unemployment Rate: "
        f"{average_unemployment:.2f}%"
    )


# ============================================================
# 11. State/Region-wise Unemployment Analysis
# ============================================================

if "Region" in df_clean.columns:

    region_average = (
        df_clean
        .groupby("Region")[
            "Estimated Unemployment Rate (%)"
        ]
        .mean()
        .sort_values(ascending=False)
    )

    print("\nAverage Unemployment Rate by Region:")
    print(region_average)


    # --------------------------------------------------------
    # Bar Chart
    # --------------------------------------------------------

    plt.figure(figsize=(12, 8))

    region_average.plot(
        kind="bar"
    )

    plt.title(
        "Average Unemployment Rate by Region"
    )

    plt.xlabel("Region")

    plt.ylabel(
        "Average Unemployment Rate (%)"
    )

    plt.xticks(
        rotation=90
    )

    plt.tight_layout()

    plt.savefig(
        "regional_unemployment.png",
        dpi=300
    )

    plt.show()


# ============================================================
# 12. Overall Unemployment Trend
# ============================================================

if (
    "Date" in df_clean.columns
    and "Estimated Unemployment Rate (%)" in df_clean.columns
):

    monthly_average = (
        df_clean
        .groupby("Date")[
            "Estimated Unemployment Rate (%)"
        ]
        .mean()
    )

    plt.figure(figsize=(12, 6))

    plt.plot(
        monthly_average.index,
        monthly_average.values,
        marker="o"
    )

    plt.title(
        "Unemployment Rate Trend in India"
    )

    plt.xlabel("Date")

    plt.ylabel(
        "Unemployment Rate (%)"
    )

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "unemployment_trend.png",
        dpi=300
    )

    plt.show()


# ============================================================
# 13. COVID-19 Impact Analysis
# ============================================================

if "Date" in df_clean.columns:

    covid_data = df_clean[
        (df_clean["Date"] >= "2020-01-01") &
        (df_clean["Date"] <= "2020-12-31")
    ]

    if not covid_data.empty:

        covid_monthly = (
            covid_data
            .groupby("Date")[
                "Estimated Unemployment Rate (%)"
            ]
            .mean()
        )

        plt.figure(figsize=(12, 6))

        plt.plot(
            covid_monthly.index,
            covid_monthly.values,
            marker="o"
        )

        plt.title(
            "Unemployment Rate During 2020"
        )

        plt.xlabel("Date")

        plt.ylabel(
            "Unemployment Rate (%)"
        )

        plt.grid(True)

        plt.tight_layout()

        plt.savefig(
            "covid_unemployment.png",
            dpi=300
        )

        plt.show()

        print(
            "\nAverage Unemployment Rate During 2020:"
        )

        print(
            f"{covid_data['Estimated Unemployment Rate (%)'].mean():.2f}%"
        )


# ============================================================
# 14. Rural vs Urban Analysis
# ============================================================

if "Area" in df_clean.columns:

    area_average = (
        df_clean
        .groupby("Area")[
            "Estimated Unemployment Rate (%)"
        ]
        .mean()
    )

    print("\nAverage Unemployment Rate by Area:")
    print(area_average)

    plt.figure(figsize=(8, 6))

    area_average.plot(
        kind="bar"
    )

    plt.title(
        "Average Unemployment Rate: Rural vs Urban"
    )

    plt.xlabel("Area")

    plt.ylabel(
        "Average Unemployment Rate (%)"
    )

    plt.xticks(
        rotation=0
    )

    plt.tight_layout()

    plt.savefig(
        "rural_vs_urban.png",
        dpi=300
    )

    plt.show()


# ============================================================
# 15. Save Cleaned Dataset
# ============================================================

df_clean.to_csv(
    "unemployment_cleaned.csv",
    index=False
)


# ============================================================
# 16. Save Analysis Results
# ============================================================

with open(
    "analysis_results.txt",
    "w"
) as file:

    file.write(
        "CODEALPHA INTERNSHIP - TASK 2\n"
    )

    file.write(
        "UNEMPLOYMENT ANALYSIS WITH PYTHON\n"
    )

    file.write(
        "=" * 60 + "\n\n"
    )

    file.write(
        f"Original Dataset Rows: {len(df)}\n"
    )

    file.write(
        f"Cleaned Dataset Rows: {len(df_clean)}\n\n"
    )

    if "Estimated Unemployment Rate (%)" in df_clean.columns:

        file.write(
            f"Average Unemployment Rate: "
            f"{df_clean['Estimated Unemployment Rate (%)'].mean():.2f}%\n"
        )

        file.write(
            f"Maximum Unemployment Rate: "
            f"{df_clean['Estimated Unemployment Rate (%)'].max():.2f}%\n"
        )

        file.write(
            f"Minimum Unemployment Rate: "
            f"{df_clean['Estimated Unemployment Rate (%)'].min():.2f}%\n"
        )

    file.write("\n\nAnalysis completed successfully.")


# ============================================================
# 17. Completion Message
# ============================================================

print("\n" + "=" * 70)
print("TASK 2 COMPLETED SUCCESSFULLY!")
print("=" * 70)

print("\nGenerated Files:")

print("1. unemployment_cleaned.csv")
print("2. regional_unemployment.png")
print("3. unemployment_trend.png")
print("4. covid_unemployment.png")
print("5. rural_vs_urban.png")
print("6. analysis_results.txt")

print("\nYou can now use these files for your CodeAlpha submission.")