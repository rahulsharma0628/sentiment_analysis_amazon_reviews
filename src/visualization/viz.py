import matplotlib.pyplot as plt
import seaborn as sns

fig_size = (12,8)

def count_plot(data, feature, color):
    sns.set(rc={'figure.figsize':fig_size})
    sns.countplot(data=data, x=feature, order=data[feature].value_counts().index, color=color)

def bar_count_plot(data, feature1, feature2, title, color):
    ax = data.groupby(feature1).mean()[feature2].plot(kind="barh", figsize=fig_size, title=title, color=color)
    plt.show()

def bar_sum_plot(data, feature1, feature2, title, color):
    ax = data.groupby(feature1).sum()[feature2].plot(kind="barh", figsize=fig_size, title=title, color=color)
    plt.show()
