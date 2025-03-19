import os
import numpy as np
import matplotlib.pyplot as plt
import logging


def setup_logger():
    # Create a logger that writes only to a logfile
    logger = logging.getLogger("MonteCarloSim")
    logger.setLevel(logging.INFO)

    # Create a FileHandler that writes to 'simulation.log'
    log_filename = "simulation.log"
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.INFO)

    # Define formatter with date in "yyyy-mm-dd#hh:mm" format and add it to the file handler
    formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d#%H:%M")
    file_handler.setFormatter(formatter)

    # Add only the file handler to the logger (no console output)
    logger.addHandler(file_handler)

    return logger


def get_int_input(prompt, logger):
    while True:
        try:
            value = int(input(prompt))
            logger.info(f"User input received: {prompt.strip()} {value}")
            return value
        except ValueError:
            logger.error("Invalid input. Please enter an integer.")
            print("Invalid input. Please enter an integer.")


def main():
    # Setup logger (local logfile only)
    logger = setup_logger()
    logger.info("Program started.")

    # Request user inputs with validation and log them
    iterations = get_int_input("Enter number of simulation iterations (e.g., 10000): ", logger)
    likelihood_min = get_int_input("Enter minimum likelihood (integer): ", logger)
    likelihood_max = get_int_input("Enter maximum likelihood (integer): ", logger)
    impact_min = get_int_input("Enter minimum impact (integer): ", logger)
    impact_max = get_int_input("Enter maximum impact (integer): ", logger)

    # Generate random samples
    logger.info("Generating random samples for likelihood and impact.")
    likelihood_samples = np.random.uniform(likelihood_min, likelihood_max, iterations)
    impact_samples = np.random.uniform(impact_min, impact_max, iterations)

    # Compute risk for each iteration
    logger.info("Computing risk samples (likelihood * impact).")
    risk_samples = likelihood_samples * impact_samples

    # Calculate statistics
    mean_risk = np.mean(risk_samples)
    median_risk = np.median(risk_samples)
    percentile_5 = np.percentile(risk_samples, 5)
    percentile_95 = np.percentile(risk_samples, 95)

    # Log statistical results
    logger.info(f"Mean Risk: {mean_risk:,.2f}")
    logger.info(f"Median Risk: {median_risk:,.2f}")
    logger.info(f"5th Percentile: {percentile_5:,.2f}")
    logger.info(f"95th Percentile: {percentile_95:,.2f}")

    # Print the statistical results to console
    print(f"Mean Risk: {mean_risk:,.2f}")
    print(f"Median Risk: {median_risk:,.2f}")
    print(f"5th Percentile: {percentile_5:,.2f}")
    print(f"95th Percentile: {percentile_95:,.2f}")

    # Plot vertical lines for key statistics
    plt.axvline(mean_risk, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_risk:.2f}')
    plt.axvline(median_risk, color='blue', linestyle='dashed', linewidth=2, label=f'Median: {median_risk:.2f}')
    plt.axvline(percentile_5, color='green', linestyle='dotted', linewidth=2, label=f'5th %: {percentile_5:.2f}')
    plt.axvline(percentile_95, color='orange', linestyle='dotted', linewidth=2, label=f'95th %: {percentile_95:.2f}')

    # Plot the histogram for risk distribution
    plt.hist(risk_samples, bins=50, edgecolor='black', alpha=0.7)
    plt.title('Distribution of Risk from Monte Carlo Simulation')
    plt.xlabel('Risk')
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()
    logger.info("Histogram generated.")

    # Ask user for the file name to save the image
    file_name = input("Enter the file name to save the risk distribution image (without extension): ").strip()
    if not file_name:
        file_name = "risk_distribution"
        logger.info("No file name provided; defaulting to 'risk_distribution'.")
    else:
        logger.info(f"File name provided: {file_name}")

    # Define the directory to save the file and create it if it doesn't exist
    save_dir = "private"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        logger.info(f"Directory '{save_dir}' created.")
    else:
        logger.info(f"Directory '{save_dir}' exists.")

    # Build the full file path and save the plot
    save_path = os.path.join(save_dir, file_name + ".png")
    plt.savefig(save_path, format="png", dpi=300)
    logger.info(f"Graph saved to: {os.path.abspath(save_path)}")

    plt.show()
    logger.info("Program finished execution.")


if __name__ == '__main__':
    main()
