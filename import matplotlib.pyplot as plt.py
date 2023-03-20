import matplotlib.pyplot as plt
#Problem #2a
# Define the data samples
C1 = [(2, 3), (3, 3), (3, 4), (1, 4), (4, 1), (4, 3)]
C2 = [(0, 0), (0, 3), (1, 1), (1, 2), (2, 1), (2, 2)]

# Plot the data samples
def plot_data(C1, C2):
    plt.scatter([x[0] for x in C1], [x[1] for x in C1], c='r', marker='o')
    plt.scatter([x[0] for x in C2], [x[1] for x in C2], c='b', marker='x')
    plt.xlabel('Attribute x')
    plt.ylabel('attribute y')
    plt.legend(['C1', 'C2'])
    plt.xlim(-1, 5)
    plt.ylim(-1, 5)

def plot_threshold(C1_classified, C2_classified, thx, thy):
    plot_data(C1_classified, C2_classified)
    plt.axvline(x=thx, color='k', linestyle='--')
    plt.axhline(y=thy, color='k', linestyle='--')
    plt.show()