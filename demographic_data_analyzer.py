import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race = df['race']
    count_of_race = []

    race_types = list(df.groupby('race').groups.keys())
    race_dict = dict(df.groupby('race').groups)

    for i in race_dict:
        count_of_race.append(len(race_dict[i]))
    race_count = pd.Series(data = count_of_race, index = race_types)

    # What is the average age of men?
    male = df[df['sex'] == 'Male']
    average_age_men = round(male['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df[df['education'] == 'Bachelors']
    percentage_bachelors = round(len(bachelors.index)/len(df.index) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    over = df[df['salary'] == '>50K']
    under = df[df['salary'] == '<=50K']

    over_group = over.groupby('education').groups
    under_group = under.groupby('education').groups

    higher_education = len(over_group['Bachelors']) + len(over_group['Doctorate']) + len(over_group['Masters'])

    ed_over = []
    for i in over_group:
        ed_over.append(len(over_group[i]))
    total_over = 0
    for val in ed_over:
        total_over += val
    lower_education = total_over - higher_education

    higher_under = len(under_group['Bachelors']) + len(under_group['Doctorate']) + len(under_group['Masters'])
    
    ed_under = []
    for i in under_group:
        ed_under.append(len(under_group[i]))
    total_under = 0
    for val in ed_under:
        total_under += val
    lower_under = total_under - higher_under

    # percentage with salary >50K
    higher_education_rich = round(higher_education/(higher_education + higher_under) * 100, 1)
    lower_education_rich = round(lower_education/(lower_education + lower_under) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

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
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
