# ***UCB FinTech Bootcamp***
# **Project 1 : GrowWise : Save, Invest and Prosper**
## **FinTech Butlers**
## **Introduction**

###  The GrowWise tool offers an easy accessible and affordable way for users, regardless of their income and investment experience, to invest their money efficiently, without requiring prior extensive knowledge of the markets or expertise in investing strategies. Depending on their goals (e.g. target funds over time)  and risk tolerance, # solution uses cutting-edge technology paired with algorithms to create personalized, tailored Investment options for individuals in a clear and easy manner.

### ***Part I.- Login*** - New users have the ability to create their login credentials and existing users have the ability to login to the tool using their existing user and password
### ***Part II. Investor Profiling*** - The user has the abilty to create their investor profile based on their own risk preferences and financial targets by answering the questions provided b the tool
### ***Part III. EFT preparation*** - The system gathers stock information to prepare an EFT based on the user's investor profile (e.g. conservative, medium conservative, medium, agressive, medium agressive) and the list of individual stocks included in the EFT. ***(NOTE: the present MVP focuses on Tech stocks, given that they have proven to be the most resilient in the current economic situation)***
### ***Part IV. Recommendation presentment and simulation*** - Using Monte Carlo simulation, the system prepares a forecast for a theoretical initial investment (e.g. $10,000) over a period of time (e.g. 5 years) and the probebilty of the outcome (expressed in %), based on the Investor profile
---
## **Technologies and Tools**

### The following list includes the main technologies and tools using during the preparation and deployment of the solution:
### 1. *Python* - Programming language used to code the solution. Version 3.7.13 was used
### 2. *GitHub* - Reposotory for code deployment, version management and documentation of the presented solution
### 3. *VS Code* - IDE tool for coding, code testing/debugging and solution documentation. Version V1.7.82 was used
### 4. *Git Bash console* - Local console used to test the coded solution and sync with GitHub. Version 2.40.1.windows.1 was utilized for this challenge
### 5. *Slack* - Collaboration tool to communicate and brainstorm with other FinTech Bootcamp participants
### 6. *Operative System* - This solution was prepared in a PC running Windows 11 v H22
---
## **Installation Guide**

### 1. *yfinance* - Install **[yfinance](https://pypi.org/project/yfinance/)** by executing the following steps:
#### 1.1. Open the GitBash terminal
#### 1.2 Type the following command and press Enter:
```python 
pip install yfinance
```
### 2. *yahoo_fin* - Install by following the following steps:
#### 2.1. Open the GitBash terminal
#### 2.2 Type the following command and press Enter:
```python 
pip install yahoo_fin
```
### 3. *fire* - Install by executing the following steps:
#### 3.1. Open the GitBash terminal
#### 3.2 Type the following command and press Enter:
```python 
pip install fire
```
### 4. *questionary* - Install by executing the following steps:
#### 4.1. Open the GitBash terminal
#### 4.2 Type the following command and press Enter:
```python 
pip install questionary
```
---
## **Solution Structure**

### The **[P1_Grow_Wise](https://github.com/LUTOV001/P1_Grow_Wise)** repository in GitHub contains the solution components. The repository consists of the following folders, subfolders and contents as described below:
 
###    1. Resources : Includes the file with user login information:
####     | 1.1 user_data.csv
####   2. fileio : Includes the csv read/write functionality python module
####     | 2.1 csvUtils.
####   3. gitignore 
####   4. MCForecastTools.py - Monte Carlo simulation module
####   5. README.md - The present file containing the outline of the repository and the solution
####   6. Risk_Return_Analysis.py - Module for risk analysis
####   7. grow_wise_monte_carlo.py - Monte Carlo simulation module with additional logic for the GrowWise solution
####   8. main.py <--- THIS IS THE MAIN PROGRAM for the GrowWise solution
####   9. portfolio_mix.py - Module to create the different EFTs based on the user investor profile
####   10. risk_questions.py - Module to collect user input to determine investor risk profile
---
## **User Instructions**

### 1. Launch the GitBash terminal
### 2. From the GitBash terminal, navigate to the folder where the GitHub respository has been cloned (e.g. OneDrive/Desktop/FinTechspace/github)
### 3. Execute/Run the main,py program by typing:
```
python main.py
```
#### 4. Answer log in questions and provide user name and password to access the tool. If new user, provide user name and password
#### 5. Wait for the program to load the EFTs and their stocks
#### 6. Answer the Investor Profile questionnaire using the arrow keys and press enter for the desired selection
#### 7. Upon answering all investor profile questions, wait for the solution to provide the recommended EFT (e.g. conservative) and the list of stocks included in it
#### 8. Review the on-screen output with the results of the investment simulation: certainty of returns (in %) for a theoretical $10000 investment over time, based on the investor profile questionnaire and desired investment results questions
---
### **Credits**

#### Prepared by the FinTech Butlers:
#####   Malika Ajmera ([malika0410](https://github.com/malika0410))
#####   Joe Knight ([yv-i](https://github.com/yv-i))
#####   Matt G ([Slay1007](https://github.com/Slay1007))
#####   Mike Nguyen ([mikenguyenx](https://github.com/mikenguyenx))
#####   Luis Torres ([LUTOV001](https://github.com/LUTOV001))
#### 
##### May 2023