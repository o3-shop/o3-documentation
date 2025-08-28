# How to Contribute

Welcome, developer! If you’re interested in contributing code to the O3 kernel or related repositories, this guide will help you get started.

## Why contribute?

- Help improve O3 for everyone
- Learn from a community of experienced developers
- Influence the direction of the project
- Build your open-source portfolio

## Knowledge you should have before contributing

### If you want to contribute with code

- **PHP:** Good knowledge of PHP 7.4 up to the latest version used in O3
- **O3 Modules:** Profound experience in writing modules for O3 or its predecessor
- **Docker:** Secure handling and understanding of Docker containers
- **Unit Testing:** Ability to write and run unit tests using PHPUnit

### If you want to contribute to the documentation

- **Documentation Writing:** Understanding of how to write clear, concise, and helpful documentation
- **Sphinx/Markdown:** Familiarity with Sphinx and Markdown is a plus

## How to contribute – Overview

1. Get familiar with the project
2. Find something to work on or add a new issue
3. Fork the repository and create a branch
4. Set up your development environment
5. Write your code or documentation
6. Write or update tests (if applicable)
7. Run tests and code style checks
8. Submit a pull request
9. Participate in code review
10. Celebrate your contribution!

## How to contribute – Details

### 1. Get familiar with the project
Read the documentation, explore the codebase, and understand the project’s goals.

### 2. Find something to work on or add a new issue
- Browse the [central issue tracker](https://github.com/o3-shop/o3-shop/issues) for open issues.
- **Choose an issue with no assignee.**  
  If the issue already has an assignee, ask in the comments if you can work on it, and check if it’s already in progress.
- **If you want to work on something new (a bug or feature), first add the issue to the central tracker using the issue form and specify the relevant repository. Only start working on it after the issue is created.**

### 3. Fork the repository and create a branch
- Fork the relevant O3 repository to your own GitHub account.
- Create a feature branch in your fork for your work.

### 4. Set up your development environment
- Clone your fork locally.
- In your project directory, run:

  ```sh
  ./docker.sh start
  ```
  This command will start the development environment using Docker.
- Follow any additional setup instructions in the documentation if needed.

### 5. Write your code or documentation
Follow the coding standards and documentation guidelines.

### 6. Write or update tests
Ensure your changes are covered by unit tests (for code contributions).

### 7. Run tests and code style checks
- In your project directory, run:

  ```sh
  ./docker.sh test-all
  ```
  This command will run all tests and the PHP code fixer to ensure your code meets project standards.

### 8. Submit a pull request
- Open a pull request from your fork’s branch to the main repository.
- Clearly describe your changes and reference the relevant issue.

### 9. Participate in code review
Respond to feedback and make necessary changes.

### 10. Celebrate your contribution!
Your work helps make O3 better for everyone.

---

## GitHub Organization and Issue Tracker

- **GitHub Organization:** [https://github.com/o3-shop](https://github.com/o3-shop)
- **Central Issue Tracker:** [https://github.com/o3-shop/o3-shop/issues](https://github.com/o3-shop/o3-shop/issues)

**Note on the Issue Tracker:**
All issues for O3 projects—regardless of which repository they concern—should be created in the central [o3-shop/o3-shop issue tracker](https://github.com/o3-shop/o3-shop/issues) using the issue form. **Always specify the relevant repository in the form when submitting an issue.**

This helps maintainers quickly route and address your contribution or report. Automation may be used to triage or label issues based on your selection.
