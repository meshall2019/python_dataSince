import matplotlib.pyplot as plt
from yellowbrick.features import *
from yellowbrick.style import *
from main import * #from main class

# The class of the Figures of exploratory data analysis

# set up the figure size
plt.rcParams['figure.figsize'] = (20, 10)

# Specify the features of interest
num_features = ['Age', 'SibSp', 'Parch', 'Fare']
xaxes = num_features
yaxes = ['Counts', 'Counts', 'Counts', 'Counts']
def Histograms():

    # make subplots
    fig, axes = plt.subplots(nrows = 2, ncols = 2)
    #draw histograms
    axes = axes.ravel()
    for idx, ax in enumerate(axes):
        ax.hist(data[num_features[idx]].dropna(), bins=40)
        ax.set_xlabel(xaxes[idx], fontsize=20)
        ax.set_ylabel(yaxes[idx], fontsize=20)
        ax.tick_params(axis='both', labelsize=15)

def barplot():

    # make subplots
    fig, axes = plt.subplots(nrows=2, ncols=2)

    # make the data read to feed into the visulizer
    X_Survived = data.replace({'Survived': {1: 'yes', 0: 'no'}}).groupby('Survived').size().reset_index(name='Counts')[
        'Survived']
    Y_Survived = data.replace({'Survived': {1: 'yes', 0: 'no'}}).groupby('Survived').size().reset_index(name='Counts')[
        'Counts']
    # make the bar plot
    axes[0, 0].bar(X_Survived, Y_Survived)
    axes[0, 0].set_title('Survived', fontsize=25)
    axes[0, 0].set_ylabel('Counts', fontsize=20)
    axes[0, 0].tick_params(axis='both', labelsize=15)

    # make the data read to feed into the visulizer
    X_Pclass = \
    data.replace({'Pclass': {1: '1st', 2: '2nd', 3: '3rd'}}).groupby('Pclass').size().reset_index(name='Counts')[
        'Pclass']
    Y_Pclass = \
    data.replace({'Pclass': {1: '1st', 2: '2nd', 3: '3rd'}}).groupby('Pclass').size().reset_index(name='Counts')[
        'Counts']
    # make the bar plot
    axes[0, 1].bar(X_Pclass, Y_Pclass)
    axes[0, 1].set_title('Pclass', fontsize=25)
    axes[0, 1].set_ylabel('Counts', fontsize=20)
    axes[0, 1].tick_params(axis='both', labelsize=15)

    # make the data read to feed into the visulizer
    X_Sex = data.groupby('Sex').size().reset_index(name='Counts')['Sex']
    Y_Sex = data.groupby('Sex').size().reset_index(name='Counts')['Counts']
    # make the bar plot
    axes[1, 0].bar(X_Sex, Y_Sex)
    axes[1, 0].set_title('Sex', fontsize=25)
    axes[1, 0].set_ylabel('Counts', fontsize=20)
    axes[1, 0].tick_params(axis='both', labelsize=15)

    # make the data read to feed into the visulizer
    X_Embarked = data.groupby('Embarked').size().reset_index(name='Counts')['Embarked']
    Y_Embarked = data.groupby('Embarked').size().reset_index(name='Counts')['Counts']
    # make the bar plot
    axes[1, 1].bar(X_Embarked, Y_Embarked)
    axes[1, 1].set_title('Embarked', fontsize=25)
    axes[1, 1].set_ylabel('Counts', fontsize=20)
    axes[1, 1].tick_params(axis='both', labelsize=15)

def Pearson_Ranking_visualization():
    plt.rcParams['figure.figsize'] = (15, 7)

    # extract the numpy arrays from the data frame
    X = data[num_features]

    # instantiate the visualizer with the Covariance ranking algorithm
    visualizer = Rank2D(features=num_features, algorithm='pearson')
    visualizer.fit(X)  # Fit the data to the visualizer
    visualizer.transform(X)  # Transform the data
    visualizer.poof()  # Draw/show/poof the data

#compare the distributions of numerical variables between passengers that survived and those that did not survive
def compare_distributions_of_numericalVariables():

    plt.rcParams['figure.figsize'] = (15, 7)
    plt.rcParams['font.size'] = 50

    set_palette('sns_bright')

    # Specify the features of interest and the classes of the target
    classes = ['Not-survived', 'Surivived']
    num_features = ['Age', 'SibSp', 'Parch', 'Fare']

    # copy data to a new dataframe
    data_norm = data.copy()
    # normalize data to 0-1 range
    for feature in num_features:
        data_norm[feature] = (data[feature] - data[feature].mean(skipna=True)) / (
                    data[feature].max(skipna=True) - data[feature].min(skipna=True))

    # Extract the numpy arrays from the data frame
    X = data_norm[num_features]
    y = data.Survived

    # Instantiate the visualizer
    # Instantiate the visualizer
    visualizer = ParallelCoordinates(classes=classes, features=num_features)

    visualizer.fit(X, y)  # Fit the data to the visualizer
    visualizer.transform(X)  # Transform the data
    visualizer.poof()  # Draw/show/poof the data

    ask=input("Want to know how survival rates differ across percentages..?: yes or no")

#Explin how did they differ across our categorical variables? We can get a sense of this by creating faceted stacked barplots for each variable.
def stacked_barplots_for_eachVariable():

    plt.rcParams['figure.figsize'] = (20, 10)

    # make subplots
    fig, axes = plt.subplots(nrows=2, ncols=2)

    # make the data read to feed into the visulizer
    Sex_survived = data.replace({'Survived': {1: 'Survived', 0: 'Not-survived'}})[data['Survived'] == 1][
        'Sex'].value_counts()
    Sex_not_survived = data.replace({'Survived': {1: 'Survived', 0: 'Not-survived'}})[data['Survived'] == 0][
        'Sex'].value_counts()
    Sex_not_survived = Sex_not_survived.reindex(index=Sex_survived.index)
    # make the bar plot
    p1 = axes[0, 0].bar(Sex_survived.index, Sex_survived.values)
    p2 = axes[0, 0].bar(Sex_not_survived.index, Sex_not_survived.values, bottom=Sex_survived.values)
    axes[0, 0].set_title('Sex', fontsize=25)
    axes[0, 0].set_ylabel('Counts', fontsize=20)
    axes[0, 0].tick_params(axis='both', labelsize=15)
    axes[0, 0].legend((p1[0], p2[0]), ('Survived', 'Not-survived'), fontsize=15)

    # make the data read to feed into the visulizer
    Pclass_survived = data.replace({'Survived': {1: 'Survived', 0: 'Not-survived'}}).replace(
        {'Pclass': {1: '1st', 2: '2nd', 3: '3rd'}})[data['Survived'] == 1]['Pclass'].value_counts()
    Pclass_not_survived = data.replace({'Survived': {1: 'Survived', 0: 'Not-survived'}}).replace(
        {'Pclass': {1: '1st', 2: '2nd', 3: '3rd'}})[data['Survived'] == 0]['Pclass'].value_counts()
    Pclass_not_survived = Pclass_not_survived.reindex(index=Pclass_survived.index)
    # make the bar plot
    p3 = axes[0, 1].bar(Pclass_survived.index, Pclass_survived.values)
    p4 = axes[0, 1].bar(Pclass_not_survived.index, Pclass_not_survived.values, bottom=Pclass_survived.values)
    axes[0, 1].set_title('Pclass', fontsize=25)
    axes[0, 1].set_ylabel('Counts', fontsize=20)
    axes[0, 1].tick_params(axis='both', labelsize=15)
    axes[0, 1].legend((p3[0], p4[0]), ('Survived', 'Not-survived'), fontsize=15)

    # make the data read to feed into the visulizer
    Embarked_survived = data.replace({'Survived': {1: 'Survived', 0: 'Not-survived'}})[data['Survived'] == 1][
        'Embarked'].value_counts()
    Embarked_not_survived = data.replace({'Survived': {1: 'Survived', 0: 'Not-survived'}})[data['Survived'] == 0][
         'Embarked'].value_counts()
    Embarked_not_survived = Embarked_not_survived.reindex(index=Embarked_survived.index)
    # make the bar plot
    p5 = axes[1, 0].bar(Embarked_survived.index, Embarked_survived.values)
    p6 = axes[1, 0].bar(Embarked_not_survived.index, Embarked_not_survived.values, bottom=Embarked_survived.values)
    axes[1, 0].set_title('Embarked', fontsize=25)
    axes[1, 0].set_ylabel('Counts', fontsize=20)
    axes[1, 0].tick_params(axis='both', labelsize=15)
    axes[1, 0].legend((p5[0], p6[0]), ('Survived', 'Not-survived'), fontsize=15)

plt.show()
def EDA():#exploratory data analysis

    print("1.The disension of the table")
    print("2.Loooking to data set")
    print("3.Looking to the Summary of varibles")

    user_opstion = int(input("Enter the number of your option: "))
    if user_opstion == 1:
        dimension_of_table()
    elif user_opstion == 2:
        look_to_dataSet()
    elif user_opstion == 3:
        summary_of_varibles()
    else:
        print("Enter the correct number")

def figures_EDA():#The figures of The figures of exploratory data analysis

    print("1.Histograms for visualization technique to check the distribution of numerical data")
    print("2.Bar plots for the categorical variables in the data set")
    print("3.Get a sense of whether the numerical variables in our data set are correlated")
    print("4.The distributions of numerical variables between passengers that survived and those that did not survive to see if there are any significant differences")
    print("5.Understanding the difference between the survival rates across the categorical variables")

    user_opstion = int(input("Enter the number of your option: "))
    if user_opstion == 1:
        Histograms()
    elif user_opstion == 2:
        Pearson_Ranking_visualization()
    elif user_opstion == 3:
        barplot()
    elif user_opstion==4:
        compare_distributions_of_numericalVariables()
    elif user_opstion == 5:
        stacked_barplots_for_eachVariable()
    else:
        print("Enter the correct number")
plt.show()

