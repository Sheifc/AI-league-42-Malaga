<<<<<<< HEAD
# AI-league-42-Malaga

# README for Submitting a Pull Request

## How to Submit Your Assignment via Pull Request

Follow these steps to submit your assignment to the "First-challenge" folder in the repository. This guide assumes you already have a GitHub account and Git installed on your computer.

### Step 1: Fork the Repository

1. Go to the repository on GitHub.
2. Click the "Fork" button at the top right corner of the page. This will create a copy of the repository in your own GitHub account.

### Step 2: Clone Your Forked Repository

1. Open your terminal or Git Bash.
2. Clone your forked repository to your local machine using the following command:
   ```bash
   git clone url
   ```
   Use the url copied from the ssh option of the repository.

### Step 3: Create a New Branch

1. Navigate to the repository directory on your local machine:
   ```bash
   cd Repository-Name
   ```
2. Create a new branch for your assignment:
   ```bash
   git branch your-branch-name
   ```
   Replace `your-branch-name` with a descriptive name for your branch.
3. Switch to the new branch:
   ```bash
   git checkout your-branch-name
   ```

### Step 4: Add Your Assignment

1. Navigate to the First-challenge folder:
```bash
   cd First-challenge
```
2. Create a new folder named after your team:
```bash
   mkdir YOUR_TEAM_NAME
```
3. Replace YOUR_TEAM_NAME with the name of your team.

Add your assignment files to this folder. At a minimum, if you have chosen Python as we recommended, you must include:
- An report that includes the code with explanations interspersed in the text.
- A requirements.txt file listing all dependencies required to run your code.


### Step 5: Commit Your Changes

1. Stage your changes:
   ```bash
   git add .
   ```
2. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Add assignment for First-challenge"
   ```

### Step 6: Push Your Changes to GitHub

1. Push your branch to your forked repository:
   ```bash
   git push origin your-branch-name
   ```

### Step 7: Create a Pull Request

1. Go to your forked repository on GitHub.
2. Click on the "Compare & pull request" button.
3. Make sure the base repository is set to the original repository and the base branch is set to the main branch.
4. Provide a descriptive title and comment for your pull request.
5. Click on the "Create pull request" button.

### Step 8: Wait for Review

1. Wait for your pull request to be reviewed.
2. Make any requested changes and push them to your branch if necessary.

Congratulations! You have successfully submitted your assignment via a pull request.

For more details, github docs is the answer: 

https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork
