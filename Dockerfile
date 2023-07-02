# Use an official Python runtime as a parent image
FROM selenium/standalone-chrome

# Set the working directory to /app
WORKDIR /app

# Install pip and other required dependencies
USER root
RUN apt-get update && apt-get install -y python3-pip python3-dev build-essential

# Set the pip cache directory to a writable location
ENV PIP_CACHE_DIR=/pip-cache

# Copy the entire project into the container at the working directory
COPY . .

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python packages globally
RUN pip install --trusted-host pypi.python.org --cache-dir=/pip-cache -r requirements.txt --break-system-packages

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the test suite when the container launches
CMD ["pytest", "Tests_Suite/test_suite_2.py", "--browser", "headless"]
