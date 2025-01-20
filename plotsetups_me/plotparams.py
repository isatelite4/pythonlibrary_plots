
import matplotlib.pyplot as plt
def plot_params():
    plt.rcParams['axes.linewidth']    = 2.3
    scatter_kwargs                    = {"zorder":100}
    error_kwargs                      = {"lw":.9, "zorder":0}
    plt.rc('font', weight = 'medium', family = 'serif', size = 15)
    plt.rcParams['xtick.major.size']  = 7
    plt.rcParams['xtick.major.width'] = 1.8
    plt.rcParams['xtick.minor.size']  = 3
    plt.rcParams['xtick.minor.width'] = 1.5
    plt.rcParams['ytick.major.size']  = 7
    plt.rcParams['ytick.major.width'] = 1.8
    plt.rcParams['ytick.minor.size']  = 3
    plt.rcParams['ytick.minor.width'] = 1.8
    plt.rcParams['pdf.fonttype']      = 42
    plt.rcParams['ps.fonttype']       = 42
    plt.rcParams['xtick.direction']   = 'in'
    plt.rcParams['ytick.direction']   = 'in'
    plt.rcParams["legend.fancybox"]   = True
    plt.rcParams['xtick.major.pad']   = 6
    plt.rcParams['ytick.major.pad']   = 6
    plt.rcParams["mathtext.fontset"]  = "dejavuserif"
    return()

