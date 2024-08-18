import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    totalPeople = len(df)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    average_age_men = round(average_age_men, 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelorsCount = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = (bachelorsCount / totalPeople) * 100
    percentage_bachelors = round(percentage_bachelors, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advancedEducationRichCount = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (df['salary'] == '>50K')].shape[0]
    advancedEducationCount = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0]
    higher_education_rich = (advancedEducationRichCount / advancedEducationCount * 100) if advancedEducationCount > 0 else 0
    higher_education_rich = round(higher_education_rich, 1)

    # What percentage of people without advanced education make more than 50K?
    lowerEducationRichCount = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (df['salary'] == '>50K')].shape[0]
    lowerEducationCount = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0]
    lower_education_rich = (lowerEducationRichCount / lowerEducationCount * 100) if lowerEducationCount > 0 else 0
    lower_education_rich = round(lower_education_rich, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    numRichMinHourWorkers = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0]
    numMinHourWorkers = df[df['hours-per-week'] == min_work_hours].shape[0]
    rich_percentage = (numRichMinHourWorkers / numMinHourWorkers) * 100

    # What country has the highest percentage of people that earn >50K?
    percentageByCountry = df[df['salary'] == '>50K'].groupby('native-country').size() / df.groupby('native-country').size() * 100
    highest_earning_country = percentageByCountry.idxmax()
    highest_earning_country_percentage = percentageByCountry.max()
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    richestPeopleIndia = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    ocupationsIndia = richestPeopleIndia['occupation'].value_counts()
    top_IN_occupation = ocupationsIndia.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

