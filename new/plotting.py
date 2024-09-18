import matplotlib.pyplot as plt

# Test if Matplotlib is installed by creating a simple plot
def test_matplotlib():
    try:
        # Create some example data
        x = [1, 2, 3, 4]
        y = [10, 20, 25, 30]

        # Create a basic line plot
        plt.plot(x, y)
        plt.title('Test: Matplotlib Installation')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')

        # Show the plot
        plt.show()
        print("Matplotlib is installed and working!")
    except ImportError:
        print("Matplotlib is not installed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the test
test_matplotlib()
