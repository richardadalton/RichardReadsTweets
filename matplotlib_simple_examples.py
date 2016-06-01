import matplotlib.pyplot as plt

def sample_pie():
    slices = [7, 2, 2, 13]
    activities = ['A', 'B', 'C', 'D']
    cols = ['c', 'm', 'r', 'b']

    plt.pie(slices, colors=cols, labels=activities,
            startangle=90, shadow=True, explode=(0, 0.5, 0.5, 0),
            autopct='%1.1f%%')

    plt.title('Blah Blah Blah\nYada Yada')
    plt.show()

def sample_bar():
    x = [1, 2, 3, 5, 7]
    y = [5, 7, 4, 13, 8]

    x2 = [0, 2, 4, 6, 8]
    y2 = [7, 10, 14, 12, 3]


    plt.bar(x, y, label='Fine Gael')
    plt.bar(x2, y2, label='Labour', color='cyan')


    plt.xlabel('Plot Number')
    plt.ylabel('Important var')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()


sample_pie()
sample_bar()



