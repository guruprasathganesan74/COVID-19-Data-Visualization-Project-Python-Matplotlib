import pandas as pd
import matplotlib.pyplot as plt
data3=pd.read_csv(r"C:\\Users\\hp\\Downloads\\sample_covid_data.csv")
df3=pd.DataFrame(data3)
print(df3)
print(df3.head(20))
print(df3.tail(20))
print(df3.info())
print(data3.isnull())
print(data3.isnull().sum())
print(data3.dropna())
print(data3.duplicated())
print(data3.duplicated().sum())
#Daily new cases over time per country-Lineplot:
country="India"
df_country=df3[df3["country"]==country]
plt.figure(figsize=(10,5))
plt.plot(df_country["date"],df_country["new_cases"],marker="o")
plt.xlabel("date")
plt.ylabel("newcase")
plt.title("Daily New COVID-19 Cases")
plt.show()
#Total deaths per country-Bar plot:
total_death=df3.groupby("country")["total_deaths"].max().sort_values(ascending=False)
print(total_death)
plt.figure(figsize=(10,5))
total_death.plot(kind="bar",color="Yellow",edgecolor="Black",linewidth=2)
plt.xlabel("country")
plt.ylabel("total deaths")
plt.title("Total deaths per country")
plt.show()
#Vaccination progress-plot:
plt.plot(df3["date"],df3["total_vaccinations"],marker="o")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.title("Vaccination progress")
plt.show()
#Total cases vs deaths per country-scatter plot:
plt.scatter(df3["total_cases"],df3["total_deaths"])
plt.xlabel("Total Cases")
plt.ylabel("Total Deaths")
plt.title("Total cases vs deaths per country")
plt.show()
#Distribution of CFR across countries- Histogram:
casefatality_rate=df3.groupby("country")[["total_deaths","total_cases"]].max()
casefatality_rate["CFR (%)"] = (casefatality_rate["total_deaths"] / casefatality_rate["total_cases"]) * 100
print(casefatality_rate["CFR (%)"])
plt.figure(figsize=(8,5))
plt.hist(casefatality_rate["CFR (%)"],bins=10,edgecolor="black",color="orange")
plt.xlabel("CFR(%)")
plt.ylabel("Number of Countries")
plt.title("Distribution of CFR across countries")
plt.show()
#latest total(cases vs death vs vaccine)-bar plot:
latest_total=df3.groupby("country")[["total_cases","total_deaths","total_vaccinations"]].max()
print(latest_total)
plt.figure(figsize=(8,5))
latest_total.plot(kind="bar",color="Green",edgecolor="orange")
plt.xlabel("country")
plt.ylabel("Count")
plt.title("Cases vs Deaths vs Vaccinations")
plt.show()
#Total case vs vacination - plot:
plt.plot(df3["total_cases"],df3["total_vaccinations"],color="pink")
plt.xlabel("Total cases")
plt.ylabel("Vaccinations")
plt.title("Cases Vs Vaccinations")
plt.show()
# Total New Deaths vs Total New Cases:
plt.scatter(df3["new_deaths"],df3["new_cases"],color="purple")
plt.xlabel("Total New Deaths")
plt.ylabel("Total Cases")
plt.title("Deaths vs Cases")
plt.show()
#Step Plot of Total Cases Over Time - stepplot:
df_india=df3[df3["country"]=="India"]
plt.figure(figsize=(10,5))
plt.step(df_india["date"],df_india["total_cases"],where="mid",color="green")
plt.xlabel("Date")
plt.ylabel("Total cases")
plt.title("Total COVID-19 Cases in india(step Plot)")
plt.show()
#Pie Chart of Total Cases per Country:
country_cases=df3.groupby("country")["total_cases"].max()
print(country_cases)
plt.figure(figsize=(8,8))
country_cases.plot(kind="pie",labels=country_cases,autopct="%1.1f%%")
plt.title("Share of Total COVID-19 Cases by Country")
plt.show()
#Pie Chart:
country_death=df3["country"].unique()
for count in country_death:
    death=df3[df3["country"]==count]
    plt.figure(figsize=(8,8))
    plt.pie(death["total_deaths"],labels=death["date"],autopct="%1.1f%%")
    plt.title(f"{count}- Each Coutry and its Total Deaths Based on Dates")
    plt.legend()
    plt.show()
