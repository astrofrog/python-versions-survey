from __future__ import print_function

import os
from collections import OrderedDict

import numpy as np
from matplotlib import pyplot as plt

plt.rc('font', family='serif')
plt.rc('xtick', labelsize='small')
plt.rc('ytick', labelsize='small')

DATA = np.loadtxt('data/versions-astro.csv', delimiter=',', dtype='|S200')

YELLOW = (255. / 255., 227. / 255., 84. / 255.)
BLUE = (55. / 255., 117. / 255., 168. / 255.)

SYNONYMS = {}
for line in open('synonyms.txt', 'r'):
    original, new = line.strip().split(":")
    SYNONYMS[original.strip()] = new.strip()

def make_plot(index, options, plot_name, labels=None):

    # Check if responses are in dictionary of synonyms
    responses = []
    for response in DATA[:, index].astype(str):
        if response in SYNONYMS:
            responses.append(SYNONYMS[response])
        else:
            responses.append(response)

    # Count occurences of responses
    count = OrderedDict()
    for option in options:
        if option == 'Other':
            count[option] = len(responses)
        else:
            count[option] = responses.count(option)
            for i in range(count[option]):
                responses.remove(option)

    # Convert to percentage
    for option in count:
        count[option] *= (100. / len(DATA[:, index]))

    # Create figure
    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(1, 1, 1)

    ind = np.arange(len(count))
    width = 0.5
    ax.bar(0., width, count.values(), bottom=ind, color=BLUE, edgecolor=BLUE, orientation='horizontal')

    ax.set_yticks(ind + width / 2.)
    if labels:
        ax.set_yticklabels(labels)
    else:
        ax.set_yticklabels(options)

    ax.patch.set_color(YELLOW)
    ax.patch.set_alpha(0.1)
    ax.set_ylim(ind[-1] + width * 1.5, ind[0] - width * 0.5)

    ax.set_xlabel("% of respondents")

    fig.savefig(os.path.join('plots', plot_name + '.png'), bbox_inches='tight')

# Python versions
options = ['2.4.x', '2.5.x', '2.6.x',
           '2.7.x', '3.0.x', '3.1.x',
           '3.2.x', '3.3.x', 'Other']
make_plot(1, options, 'python_versions')

# Numpy versions
options = ['1.2.x', '1.3.x', '1.4.x',
           '1.5.x', '1.6.x', 'dev',
           'None', 'Other']
make_plot(2, options, 'numpy_versions')

# Scipy versions
options = ['0.6.x', '0.7.x', '0.8.x',
           '0.9.x', '0.10.x', '0.11.x',
           'dev', 'None', 'Other']
make_plot(3, options, 'scipy_versions')

# Install methods
options = ['Linux Package Manager',
           'Installed from Source',
           'Enthought Python Distribution',
           'MacPorts',
           "Don't know",
           'Official binary installers (e.g. MacOS X DMG or official Windows installers)',
           'Admins',
           'STScI Python',
           'SciSoft',
           'ActivePython',
           'Other']
labels = ['Linux Manager',
          'Source',
          'EPD',
          'MacPorts',
          "Don't know",
          'Official Installers',
          'Admins',
          'STScI Python',
          'SciSoft',
          'ActivePython',
          'Other']
make_plot(4, options, 'install_methods', labels=labels)
