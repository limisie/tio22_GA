import numpy as np
from matplotlib import cycler, pyplot as plt, ticker

PLOT_SIZE_X = 10
PLOT_SIZE_Y = 5
PLOT_LEFT_POS = 0.1
PLOT_RIGHT_POS = 0.9
PLOT_BOTTOM_POS = 0.15
PLOT_TOP_POS = 0.85
PLOT_MARGIN = 0.01
PLOT_LW = 0.9
PLOT_GRID_LW = 0.2
PLOT_TICKS_Y_INTERVAL = 0.1
PLOT_TICKS_MINOR_Y_INTERVAL = PLOT_TICKS_Y_INTERVAL / 5
PLOT_SAVE = False


def plot(best_history, avg_history, worst_history, pop_size, p_co, p_m,
         filename, y_ticks_interval=PLOT_TICKS_Y_INTERVAL, y_min=0.5, y_max=1, lloc='best'):

    colors = cycler('color', ['olive', 'dodgerblue', 'orange'])
    n = len(best_history)
    plt.rc('axes', prop_cycle=colors)

    fig, ax = plt.subplots(figsize=(PLOT_SIZE_X, PLOT_SIZE_Y))
    plt.subplots_adjust(left=PLOT_LEFT_POS, right=PLOT_RIGHT_POS, bottom=PLOT_BOTTOM_POS, top=PLOT_TOP_POS)
    plt.margins(x=PLOT_MARGIN)

    x = np.arange(0, n)
    plt.plot(x, best_history, label='best', linewidth=PLOT_LW)
    plt.plot(x, avg_history, label='avg', linewidth=PLOT_LW)
    plt.plot(x, worst_history, label='worst', linewidth=PLOT_LW)
    plt.title(
        f"Stopień przystosowania do iteracji (n={pop_size}, p_co={p_co}, p_m={p_m})")

    plt.xlabel("Iteracje")
    plt.ylabel("Stopień przystosowania")

    legend = plt.legend(loc=lloc)
    legend.get_frame().set_facecolor('white')
    legend.get_frame().set_edgecolor('white')

    plt.grid(axis='y', lw=PLOT_GRID_LW)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(n / 10))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(n / 100))
    # ax.yaxis.set_major_locator(ticker.MultipleLocator(y_ticks_interval))
    # ax.yaxis.set_minor_locator(ticker.MultipleLocator(y_ticks_interval / 5))
    ax.set_xlim(xmin=0)
    ax.set_xlim(xmax=n - 1)
    # ax.set_ylim(ymax=y_max)
    # ax.set_ylim(ymin=y_min)

    if PLOT_SAVE:
        plt.savefig(filename + '.png')
    plt.show()
