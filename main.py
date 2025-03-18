import os
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Number of simulation iterations
    iterations = 10000

    # Define the ranges for likelihood and impact
    likelihood_min, likelihood_max = 3, 5
    impact_min, impact_max = 4, 5

    # Generate random samples
    likelihood_samples = np.random.uniform(likelihood_min, likelihood_max, iterations)
    impact_samples = np.random.uniform(impact_min, impact_max, iterations)

    # Compute risk for each iteration
    risk_samples = likelihood_samples * impact_samples

    # Calculate statistics
    mean_risk = np.mean(risk_samples)
    median_risk = np.median(risk_samples)
    percentile_5 = np.percentile(risk_samples, 5)
    percentile_95 = np.percentile(risk_samples, 95)

    print(f"Mean Risk: {mean_risk:,.2f}")
    print(f"Median Risk: {median_risk:,.2f}")
    print(f"5th Percentile: {percentile_5:,.2f}")
    print(f"95th Percentile: {percentile_95:,.2f}")

    # Plot vertical lines for key statistics
    plt.axvline(mean_risk, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_risk:.2f}')
    plt.axvline(median_risk, color='blue', linestyle='dashed', linewidth=2, label=f'Median: {median_risk:.2f}')
    plt.axvline(percentile_5, color='green', linestyle='dotted', linewidth=2, label=f'5th %: {percentile_5:.2f}')
    plt.axvline(percentile_95, color='orange', linestyle='dotted', linewidth=2, label=f'95th %: {percentile_95:.2f}')

    # Plot the risk distribution
    plt.hist(risk_samples, bins=50, edgecolor='black', alpha=0.7)
    plt.title('Distribution of Risk from Monte Carlo Simulation')
    plt.xlabel('Risk')
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()

    # Define the directory where the file will be saved
    save_dir = "private"

    # Create the directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Save the graph as a PNG file in the "private" folder
    save_path = os.path.join(save_dir, "risk_distribution2.png")

    # Save the graph as a PNG file in the current folder
    plt.savefig(save_path, format="png", dpi=300)

    plt.show()

