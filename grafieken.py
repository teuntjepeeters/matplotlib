from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import numpy as np


def scatterplot(x, y):
    # Create data
    #N = 500
    #x = np.random.rand(N)
    #y = np.random.rand(N)
    #area = np.pi * 3

    # Plot
    plt.scatter(x, y)
    plt.title('Scatter plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def lijndiagram(x, y, z):
    """

    :param x: lijst met waarden x-as
    :param y: lijst met waarden y-as
    :return:
    """
    plt.xlabel("x-as")
    plt.ylabel("y-as")
    plt.title("Titel")
    plt.plot(x, y)
    plt.plot(x, z)
    plt.show()


def barplot(x, y, z):
    plt.bar(x, y)
    plt.title("barplot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def stackedbarplot(A, B):
    #A = [5., 30., 45., 22.]
    #B = [5., 25., 50., 20.]

    X = range(10)
    print(A)
    print(B)
    plt.bar(X, A, color='b')
    plt.bar(X, B, color='r', bottom=A)
    plt.legend(["A", "B"])
    plt.xlabel("number X")
    plt.ylabel("Number Y")
    plt.title("stacked barplot")
    plt.show()


def boxplot(x, y):
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # fake up some data
    spread = np.random.rand(50) * 100
    center = np.ones(25) * 50
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    data = np.concatenate((spread, center, flier_high, flier_low))
    data = np.concatenate((x,y))
    fig1, ax1 = plt.subplots()
    ax1.set_title('Basic Plot')
    ax1.boxplot(data)
    plt.show()


def subplots():
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)

    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    plt.subplot(2, 1, 1)
    plt.plot(x1, y1, 'o-')
    plt.title('A tale of 2 subplots')
    plt.ylabel('Damped oscillation')

    plt.subplot(2, 1, 2)
    plt.plot(x2, y2, '.-')
    plt.xlabel('time (s)')
    plt.ylabel('Undamped')

    plt.show()


def piechart():
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = ["pizza", "friet", "groenten", "ijs", "taart"]
    sizes = [5, 5, 60, 20, 10]
    # explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def drie_d(x, y, z):
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    colors = ['r', 'g', 'b', 'y', 'b', 'g', 'y', 'g', 'w', 'b']
    yticks = [3, 2, 1, 0]
    for c, k in zip(colors, y):
        # Generate the random data for the y=k 'layer'.
        #xs = np.arange(20)
        #ys = np.random.rand(20)

        # You can provide either a single color or an array with the same length as
        # xs and ys. To demonstrate this, we color the first bar of each set cyan.
        cs = [c] * len(x)
        cs[0] = 'c'

        # Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
        ax.bar(x, y, zs=k, zdir='y', color=cs, alpha=0.8)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # On the y axis let's only label the discrete values that we have data for.
    ax.set_yticks(y)

    plt.show()


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [2, 4, 7, 4, 0, 6, 5, 3, 5, 20]
    z = [a*b for a,b in zip(x, y)]
    print(z)
    scatterplot(x, y)
    #easy_plot(x, y, z)
    #lijndiagram(x, y, z)
    #barplot(x, y, z)
    stackedbarplot(x, y)
    #boxplot(x,y)
    #piechart()
    #subplots()
    #drie_d(x, y, z)
