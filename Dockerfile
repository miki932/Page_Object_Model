# Use an official Python runtime as a parent image
FROM notarize/selenium-chrome:2.0.114.0-20230615

# Set the working directory to /app
WORKDIR /app

# Copy the entire project into the container at the working directory
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the test suite when the container launches
CMD ["pytest", "Tests_Suite/test_suite_2.py", "--browser", "headless"]
