import matplotlib.pyplot  as plt

def draw_results(results, faster_results):
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # Create a figure with two subplots
    
    # Plot for regular results
    axs[0].scatter(range(len(results)), results, label='Regular', color='blue')
    axs[0].set_xlabel('Size')
    axs[0].set_ylabel('Time')
    axs[0].set_title('Size vs Time')
    axs[0].legend()
    axs[0].grid(True)
    
    # Plot for faster results
    axs[1].scatter(range(len(faster_results)), faster_results, label='Faster', color='red')
    axs[1].set_xlabel('Size')
    axs[1].set_ylabel('Time')
    axs[1].set_title('Size vs Time')
    axs[1].legend()
    axs[1].grid(True)
    
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()
