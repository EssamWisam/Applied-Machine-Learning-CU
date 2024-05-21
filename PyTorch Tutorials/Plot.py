import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def plot_model_contours(model, x_data, y_data,  hyperparams_list=[0], trained=False):
    num_plots = len(hyperparams_list)
    num_cols = 4
    num_rows = int(np.ceil(num_plots / num_cols))

    x1_min, x1_max = x_data[:, 0].min() - 0.1, x_data[:, 0].max() + 0.1
    x2_min, x2_max = x_data[:, 1].min() - 0.1, x_data[:, 1].max() + 0.1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, 0.01), np.arange(x2_min, x2_max, 0.01))

    plt.style.use('dark_background')
    fig, ax = plt.subplots(num_rows, num_cols, figsize=(16, 4*num_rows), dpi=200)

    if not trained:
        for i, hyperparams in enumerate(tqdm(hyperparams_list, desc="Hyperparameters")):
            # Train the model on the data with these hyperparameters.
            model.set_params(**hyperparams)
            model.fit(x_data, y_data)
            # Evaluate the model on a grid of input values.
            Z = model.predict(np.c_[xx1.ravel(), xx2.ravel()])
            Z = Z.reshape(xx1.shape)

            # Get the current subplot axis.
            ax_curr = ax.flat[i]

            # Set the background color for better readability.
            ax_curr.set_facecolor('silver')

            # Plot the contour lines with the correct colors and alpha.
            ax_curr.contourf(xx1, xx2, Z, cmap='rainbow', alpha=0.8)

            # Plot the data points with the correct colors and edge colors.
            ax_curr.scatter(x_data[:, 0], x_data[:, 1], c=y_data, s=20,
                            edgecolor='k', cmap='rainbow', linewidth=0.5)

            # Add a title to the subplot with the hyperparameters used.
            ax_curr.set_title(f'{hyperparams}')
    else:
        # Repeat but only once for the given trained model:
        Z = model.predict(np.c_[xx1.ravel(), xx2.ravel()])
        Z = Z.reshape(xx1.shape)
        ax_curr = ax.flat[0]
        ax_curr.set_facecolor('silver')
        ax_curr.contourf(xx1, xx2, Z, cmap='rainbow', alpha=0.8)
        ax_curr.scatter(x_data[:, 0], x_data[:, 1], c=y_data, s=20, edgecolor='k', cmap='rainbow', linewidth=0.5)
        ax_curr.set_title(f'Decision Boundaries')

    # Remove any unused subplots.
    for j in range(num_plots, num_rows*num_cols):
        fig.delaxes(ax.flat[j])

    plt.tight_layout()
    plt.show()
