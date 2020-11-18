# Week 4 Exercise with Numpy
# Use only numpy in these exercises

# Exercise 1
#     Open the file './befkbhalderstatkode.csv'
#     Turn the csv file into a numpy ndarray with np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
#     Using this data:
#     neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
#               5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
#               10: 'Amager Vest', 99: 'Udenfor'}
#     Find out how many people lived in each of the 11 areas in 2015 
#   4. Make a bar plot to show the size of each city area from the smallest to the largest 
#   5. Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015
#   6. How many of those were from the other nordic countries (not dk)
#   7. Make a line plot showing the changes of number of people in vesterbro and østerbro from 1992 to 2015

# Exercise 2 A bit harder (Extra only if you have the time)
#     From "Danmarks Statistik" download demographic data here: https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=Code&delimiter=Semicolon&OMR%C3%85DE=000%2C084%2C147%2C400%2C085%2C083%2C082%2C081%2C851%2C461%2C561%2C751&K%C3%98N=1%2C2&ALDER=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2C27%2C28%2C29%2C30%2C31%2C32%2C33%2C34%2C35%2C36%2C37%2C3%2C39%2C40%2C41%2C42%2C43%2C44%2C45%2C46%2C47%2C48%2C49%2C50%2C51%2C52%2C53%2C54%2C55%2C56%2C57%2C58%2C59%2C60%2C61%2C62%2C63%2C64%2C65%2C66%2C67%2C68%2C69%2C70%2C71%2C72%2C73%2C74%2C75%2C76%2C77%2C78%2C79%2C80%2C81%2C82%2C83%2C84%2C85%2C86%2C87%2C88%2C89%2C90%2C91%2C92%2C93%2C94%2C95%2C96%2C97%2C98%2C99%2C100&Tid=2008K1%2C2009K1%2C2010K1%2C2011K1%2C2012K1%2C2013K1%2C2014K1%2C2015K1%2C2016K1%2C2017K1%2C2018K1%2C2019K1%2C2020K1
#     clean up the data so it only contains numbers. (If you find this hard to do then Pandas can help (we will cover it next week)

#####################
    # GENERAL #
#####################
import numpy as np
import csv
import matplotlib.pyplot as plt

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
               5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
               10: 'Amager Vest', 99: 'Udenfor'}
dataset = np.genfromtxt('../../data/befkbhalderstatkode.csv',delimiter=',',dtype=np.uint,skip_header=1)
da_dk_code = 5100

#####################
    # EXERCISE 1 #
#####################
def number_of_people_per_neighbourhood(dataset, n, mask):
    all_people_in_given_n = dataset[mask & (dataset[:,1] == n)]
    sum_of_people = all_people_in_given_n[:,4].sum()
    return sum_of_people

def print_number_of_people_in_neighb(dataset,country_code,neighb):
    mask = (dataset[:,0] == 2015) & (dataset[:,3] == country_code) 
    for n in neighb: 
        print(f'%d personer i %s' % (number_of_people_per_neighbourhood(dataset,n,mask),neighb[n]))

def plot_number_of_people_in_neighbo(dataset,country_code,neighb):
    mask = (dataset[:,0] == 2015) & (dataset[:,3] == country_code)
    people_dict = {neighb[k]:number_of_people_per_neighbourhood(dataset,k,mask) for k in neighb}
    plt.xticks(rotation=45)
    plt.bar(people_dict.keys(),people_dict.values())
    plt.show()

def number_of_people_above_65_in_cph(dataset, neighb):
    mask = (dataset[:,0] == 2015) & (dataset[:,2] > 65)
    sum = 0
    for k in neighb:
        sum += number_of_people_per_neighbourhood(dataset,k,mask)
    return sum

def number_of_people_in_countries(dataset, countries, neighb):
    sum = 0
    for country in countries:
        mask = (dataset[:,0] == 2015) & (dataset[:,2] > 65) & (dataset[:,3] == country)
        for k in neighb:
            sum += number_of_people_per_neighbourhood(dataset,k,mask)
    return sum

def line_plot_changes_in_vesterbro_and_oesterbro(dataset):
    years = [y for y in range(1992,2006)]
    oesterbro_amounts = [dataset[(dataset[:,0] == i) & (dataset[:,1] ==  2)][:,4].sum() for i in range(1992,2006)]
    vesterbro_amounts = [dataset[(dataset[:,0] == i) & (dataset[:,1] ==  4)][:,4].sum() for i in range(1992,2006)]
    plt.xticks(ticks=range(1992,2006),rotation=45)
    p1, = plt.plot(years, oesterbro_amounts, label="Østerbro")
    p2, = plt.plot(years, vesterbro_amounts, label="Vesterbro")
    plt.legend(handles=[p1,p2],bbox_to_anchor=(1, 1.125), loc='upper right', borderaxespad=0.)
    plt.show()

#####################
    # TESTING #
#####################
if __name__ == "__main__":
    print_number_of_people_in_neighb(dataset,da_dk_code,neighb)
    plot_number_of_people_in_neighbo(dataset,da_dk_code,neighb)
    print(f'People above 65 living in Copenhagen (2015): %d' % number_of_people_above_65_in_cph(dataset,neighb))
    nordic_countries = [5110, 5120, 5104, 5105, 5106, 5902, 5901,5101] # excluding DK
    print(f'People above 65 living in CPH (2015) from other nordic countries: %d' % number_of_people_in_countries(dataset,nordic_countries,neighb))
    line_plot_changes_in_vesterbro_and_oesterbro(dataset)