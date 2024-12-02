For Static Analysis, SonarQube was used to analyze the code. The following steps were taken to perform static analysis:

1. Install SonarQube on your machine, specifically version 10.1 from June 2023. Here is the link to the download page: https://www.sonarsource.com/products/sonarqube/downloads/historical-downloads/

2. Run the StartSonar.bat file under the bin/<OPERATING_SYSTEM> folder to start the SonarQube server, where <OPERATING_SYSTEM> corresponds to the operating system you are using.

3. Log into the SonarQube server by navigating to http://localhost:9000 and using the default credentials (admin/admin).

4. Create a new project and generate a token for the project.

5. In the Thingifier API's root directory, create a new file called sonar-project.properties with the following contents:

```
# must be unique in a given SonarQube instance
sonar.projectKey=my:project

# --- optional properties ---

# defaults to project key
#sonar.projectName=My project
# defaults to 'not provided'
#sonar.projectVersion=1.0
 
# Path is relative to the sonar-project.properties file. Defaults to .
#sonar.sources=.
 
# Encoding of the source code. Default is default system encoding
#sonar.sourceEncoding=UTF-8
```

6. Run the following command to analyze the source code using SonarQube in the API's root directory (which can be found in the project's PartA folder):

```
sonar-scanner.bat -D"sonar.projectKey=ECSE429" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.token=<generated_token_value>" -D"sonar.java.binaries=runTodoManagerRestAPI-1.5.5.jar"
```
where <generated_token_value> corresponds to the token generated in step 4.

7. Once the analysis is complete, navigate to the SonarQube dashboard to view the results.

