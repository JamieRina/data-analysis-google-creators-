import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_excel(filepath)

    required_columns = [
        "USER_ID",
        "CREATIVE_NAME",
        "CREATIVE_HAS_INFLUENCER",
        "AGE",
        "INTEREST_CATEGORY",
        "CITY",
        "PLATFORM_SHOWN_ON",
        "AD_DELIVERY_COST",
        "PURCHASE_PHONE"
    ]

    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    return df
def creative_overview(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("CREATIVE_NAME").agg(
        users_exposed=("USER_ID", "count"),
        total_cost=("AD_DELIVERY_COST", "sum"),
        total_sales=("PURCHASE_PHONE", "sum")
    )
def performance_metrics(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    summary = df.groupby(group_col).agg(
        users=("USER_ID", "count"),
        sales=("PURCHASE_PHONE", "sum"),
        cost=("AD_DELIVERY_COST", "sum")
    )

    summary["CVR (%)"] = (summary["sales"] / summary["users"]) * 100
    summary["CPA"] = summary["cost"] / summary["sales"]

    return summary.sort_values("CVR (%)", ascending=False)

def creative_performance(df: pd.DataFrame) -> pd.DataFrame:
    return performance_metrics(df, "CREATIVE_NAME")

def platform_performance(df: pd.DataFrame) -> pd.DataFrame:
    return performance_metrics(df, "PLATFORM_SHOWN_ON")

def add_age_groups(df: pd.DataFrame) -> pd.DataFrame:
    bins = [18, 24, 34, 44, 54, 64, 100]
    labels = ["18–24", "25–34", "35–44", "45–54", "55–64", "65+"]

    df = df.copy()
    df["AGE_GROUP"] = pd.cut(df["AGE"], bins=bins, labels=labels)
    return df

def age_group_performance(df: pd.DataFrame) -> pd.DataFrame:
    return performance_metrics(df, "AGE_GROUP")

def interest_performance(df: pd.DataFrame) -> pd.DataFrame:
    return performance_metrics(df, "INTEREST_CATEGORY")

def influencer_performance(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["INFLUENCER"] = df["CREATIVE_HAS_INFLUENCER"].map({1: "Influencer", 0: "No Influencer"})
    return performance_metrics(df, "INFLUENCER")

def plot_metric(df: pd.DataFrame, metric: str, title: str):
    # Sort for readability
    df_sorted = df.sort_values(metric, ascending=False)

    plt.figure(figsize=(10, 6))

    bars = plt.bar(
        df_sorted.index.astype(str),
        df_sorted[metric]
    )

    plt.title(title, fontsize=14, weight="bold")
    plt.xlabel("")
    
    # Decide formatting based on metric type
    is_money = metric in ["CPA", "cost", "total_cost"]

    ylabel = f"£ {metric}" if is_money else metric
    plt.ylabel(ylabel, fontsize=12)

    plt.xticks(rotation=30, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()

        if is_money:
            label = f"£{height:,.2f}"
        else:
            label = f"{height:.2f}%"

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            label,
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()
    plt.show()


def main():
    df = load_data("Digdata Google Next Step Dataset.xlsx")

    df = add_age_groups(df)

    creative_perf = creative_performance(df)
    platform_perf = platform_performance(df)

    print("Creative Overview")
    print(creative_overview(df))

    print("\nCreative Performance")
    print(creative_perf)

    print("\nPlatform Performance")
    print(platform_perf)

    print("\nAge Group Performance")
    print(age_group_performance(df))

    print("\nInterest Performance")
    print(interest_performance(df))

    print("\nInfluencer Performance")
    print(influencer_performance(df))

    # BAR CHARTS
    plot_metric(
        creative_perf,
        "CVR (%)",
        "Conversion Rate by Creative"
    )

    plot_metric(
        platform_perf,
        "CPA",
        "Cost Per Acquisition by Platform"
    )
    

if __name__ == "__main__":
    main()
