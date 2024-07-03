from bs4 import BeautifulSoup
import requests
import time
import pandas as pd



# Access the Website
url = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
response = requests.get(url, headers=headers)
time.sleep(3.0)
# print(response.text)
print(response.status_code)
soup = BeautifulSoup(response.text, features='html.parser')

# Get the Data
# print(soup.find(name='h1', class_='csr-gridpage__header'))
ranks = soup.find_all(name='td', class_='csr-col--rank')
ranks_list = []
for rank in ranks:
    ranks_list.append(rank.getText().split(":")[1])
print(ranks_list)  # this is column 1

majors = soup.find_all(name='td', class_='csr-col--school-name')
majors_list = []
for major in majors:
    majors_list.append(major.getText().split(':')[1])
print(majors_list)  # this is column 2

starting_salaries = soup.find_all(name='td', class_='csr-col--right')
starting_median_salary_list = []
mid_career_median_salary_list = []
for salary in starting_salaries:
    data_title = salary.getText().split(':')[0]
    if data_title == "Early Career Pay":
        starting_median_salary_list.append(salary.getText().split(':')[1])
    elif data_title == "Mid-Career Pay":
        mid_career_median_salary_list.append(salary.getText().split(':')[1])
print(starting_median_salary_list)  # this is column 3
print(mid_career_median_salary_list)  # this is column 4

# rows = soup.find_all(name='td')
# rows_list = []
# for row in rows:
#     rows_list.append(row.getText())
# print(rows_list)


# Save the data in an excel

data_dict = {
    "Rank": ranks_list,
    "Major": majors_list,
    "Starting Median Salary": starting_median_salary_list,
    "Mid-Career Median Salary": mid_career_median_salary_list
}

# print(data_dict)

dataframe = pd.DataFrame(data_dict)
print(dataframe)

csv_output = dataframe.to_csv('./salary_data.csv')
