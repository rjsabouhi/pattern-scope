import matplotlib.pyplot as plt


def plot_patterns(x, title="Series"):
    plt.figure(figsize=(6, 3))
    plt.plot(x, label="data", linewidth=1.3)
    plt.title(f"Pattern Visualization: {title}")
    plt.tight_layout()
    plt.show()
