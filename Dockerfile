FROM python:3.8
ARG CHROME_VERSION=current
ENV TEST_ARGS="-k Stable"
VOLUME ["/tests/reports"]
LABEL maintainer="pavel ashevskiy"

EXPOSE 80/tcp

RUN echo ${CHROME_VERSION}
# Installing Chrome browser
# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# Updating apt to see and install Google Chrome
RUN apt-get -y update
# Just install last version
##RUN apt-get install -y google-chrome-stable

# Install last or special version
RUN if [ $CHROME_VERSION = current ]; then wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
  && apt install -y /tmp/chrome.deb \
  && rm /tmp/chrome.deb;  \
  else wget --no-verbose -O /tmp/chrome.deb http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb \
  && apt install -y /tmp/chrome.deb \
  && rm /tmp/chrome.deb; fi


# Install specified version
#RUN wget --no-verbose -O /tmp/chrome.deb http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb \
#  && apt install -y /tmp/chrome.deb \
#  && rm /tmp/chrome.deb

# Installing Chrome driver
RUN apt-get install -yqq unzip
# Download the Chrome Driver (for specific chrome version)
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl http://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(google-chrome --product-version | grep -oE "^[0-9]+\.[0-9]+\.[0-9]+")`/chromedriver_linux64.zip
# Unzip the Chrome Driver into /usr/local/bin directory
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
# Set display port as an environment variable
ENV DISPLAY=:99

# Copy tests and deploy dependencies
COPY . /tests
WORKDIR /tests


RUN pip install --no-cache-dir -r dependencies.list
CMD ["sh", "-c", "pytest --junitxml=reports/junit_report.xml --html=reports/testin_report.html $TEST_ARGS"]