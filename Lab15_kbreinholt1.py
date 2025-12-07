import matplotlib.pyplot as plot
import numpy

# Generate data for the sine wave
# x values from 0 to 4π
x = numpy.linspace(0, 4 * numpy.pi, 1000)

# Calculate sin(x) for each x value
y = numpy.sin(x)

# Create the plot
plot.figure(figsize=(10, 6))
plot.plot(x, y, linewidth=2, color='blue', label='sin(x)')

# Customize the plot
plot.xlabel('x', fontsize=12)
plot.ylabel('sin(x)', fontsize=12)
plot.title('Sine Wave Graph', fontsize=14, fontweight='bold')
plot.grid(True, alpha=0.3)
plot.legend(fontsize=11)

# Add horizontal line at y=0
plot.axhline(y=0, color='k', linewidth=0.5)

# Display the plot
plot.show()

